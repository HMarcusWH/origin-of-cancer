"""Pre-run record validation. Passing is metadata completeness, NOT lab approval.

No input defaults to PASS. Blank templates intentionally produce NOT_READY.
Exact assay calibration, risk review and independent approvals remain external.
"""
from __future__ import annotations
import json,math,re
from pathlib import Path
from threshold_contracts_v2_7_7 import timestamp
from numerical_models_v2_7_7 import cycle_gain

def preflight(config:dict)->dict:
    errors=[]
    if type(config) is not dict:return {'status':'NOT_READY','errors':['object_required']}
    def need(k,predicate,reason):
        try:ok=predicate(config.get(k))
        except (ValueError,TypeError,AttributeError):ok=False
        if not ok:errors.append(k+':'+reason)
    nonempty=lambda x:type(x) is str and bool(x.strip())
    digest=lambda x:type(x) is str and bool(re.fullmatch(r'[0-9a-f]{64}',x))
    for k in ['run_id','route_id','boundary_id','assay_qualification_ref','independent_review_ref','institutional_safety_review_ref','power_analysis_ref','control_plan_ref','analysis_plan_ref','ancestry_plan_ref','degradation_recovery_calibration_ref']:
        need(k,nonempty,'required')
    for k in ['route_spec_digest','boundary_spec_digest','preregistration_digest','analysis_code_digest']:
        need(k,digest,'sha256_required')
    need('tier',lambda x:x in ('A_TRANSITION_CORE','B_FULL_ROUTE'),'declared_tier_required')
    need('data_origin',lambda x:x=='LABORATORY','laboratory_record_required')
    for k in ['no_full_length_founder_topup','unsorted_actual_output','pilot_qualified','fresh_confirmatory_material']:
        need(k,lambda x:type(x) is bool and x,'explicit_true_required')
    try:
        if timestamp(config.get('frozen_at'))>=timestamp(config.get('first_claim_bearing_observation')):errors.append('freeze_must_precede_observation')
    except (ValueError,TypeError):errors.append('timezone_aware_freeze_and_observation_times_required')
    if config.get('tier')=='B_FULL_ROUTE':
        for k in ['U1','U2','U3','U4','U5','U6','FULL_ROUTE_FREEZE']:
            upstream=config.get('upstream_qualification')
            obj=upstream.get(k) if type(upstream) is dict else None
            if type(obj) is not dict or obj.get('status')!='QUALIFIED' or not digest(obj.get('receipt_digest')):errors.append('upstream:'+k+':qualified_receipt_required')
    budget=config.get('transfer_budget');gain=None
    if type(budget) is not dict:errors.append('transfer_budget_required')
    elif budget.get('model')=='LINEARIZED_FIXED_RATE_CYCLE':
        if budget.get('applicability_qualified') is not True or not nonempty(budget.get('calibration_ref')):errors.append('linearized_cycle_applicability_not_qualified')
        try:
            gain=cycle_gain(**{k:budget[k] for k in ['transfer_fraction','recovery','copy_rate_per_h','loss_rate_per_h','interval_h']})
            if not gain['replacement_in_this_model']:errors.append('linearized_cycle_does_not_replace_losses')
            if budget.get('rate_basis')!='CONSERVATIVE_MEASURED_BOUND':errors.append('conservative_measured_rate_bound_required')
        except (KeyError,ValueError,TypeError,ArithmeticError):errors.append('invalid_transfer_budget')
    elif budget.get('model')=='QUALIFIED_NONLINEAR_CYCLE':
        if not nonempty(budget.get('model_ref')) or not nonempty(budget.get('calibration_ref')) or budget.get('replacement_demonstrated') is not True:errors.append('nonlinear_replacement_qualification_required')
    else:errors.append('declared_qualified_cycle_model_required')
    return {'status':'RECORD_COMPLETE_PENDING_INDEPENDENT_AUTHORIZATION' if not errors else 'NOT_READY','errors':errors,'gain_diagnostic':gain,'scientific_pass':False,'safety_authorization_issued':False}

if __name__=='__main__':
    import argparse
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('config',type=Path);ns=ap.parse_args()
    try:result=preflight(json.loads(ns.config.read_text()))
    except (OSError,json.JSONDecodeError) as e:result={'status':'NOT_READY','errors':[str(e)]}
    print(json.dumps(result,indent=2,allow_nan=False));raise SystemExit(0 if result['status'].startswith('RECORD_COMPLETE') else 2)
