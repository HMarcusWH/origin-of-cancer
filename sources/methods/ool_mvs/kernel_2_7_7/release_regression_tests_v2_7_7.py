"""Release regressions. Synthetic software/mathematics cases, NOT experiments.

Each assertion includes an invariant label. Parameterized case counts are not
independent scientific replications. No trust keys are persisted by these tests.
"""
from __future__ import annotations
import copy,json,math,unittest
from dataclasses import replace,asdict
from pathlib import Path
import mpmath as mp
import claim_registry_runtime_v2_7_7 as rt
from evidence_receipts_v2_7_7 import *
from certificate_authority_v2_7_7 import *
from threshold_contracts_v2_7_7 import *
from kernel_test_fixtures_v2_7_7 import *
from numerical_models_v2_7_7 import *

ROOT=Path(__file__).parent
CASES=[]
def check(label,fn):
    try:
        passed=bool(fn());error='' if passed else 'invariant_false'
    except Exception as e:passed=False;error=type(e).__name__+': '+str(e)
    CASES.append({'id':label,'pass':passed,'detail':error})
    if len(CASES)%100==0: print('Regression progress:',len(CASES),flush=True)
    return passed

def raises(fn,types=(ValueError,TypeError,ArithmeticError)):
    try:fn()
    except types:return True
    return False

def bundle(cr):return build_evidence_bundle(cr,cr.physical_witness_ref,consumed_raw_ids(cr),bundle_id='release-test')
def certificate(cr,env,policy=None,attestations=None):
    if policy is None and attestations is None:policy,attestations=fixture_trust(env)
    return rt.issue_claim_certificate(cr,bundle(cr),env,policy=policy,attestations=attestations or ())
def invalid_result(cr,env):
    try:return certificate(cr,env).certificate_status is CertificateStatus.INVALID
    except (ValueError,TypeError):return True

reg=rt.load_registry();world=complete_world(reg);base=evidence_env_from_world(reg,world)
# Derive canonical argument fixtures rather than introducing new claim names.
argobjects={'RouteId':R,'Boundary':B0}
for typ,vals in world['domains'].items():
    if vals:argobjects[typ]=vals[0]
# NB0 and physical realization objects occur nested rather than the top domain.
argobjects.update({'NaturalBoundary':NB0,'BoundaryRealizationWitness':base_objects()[6]})
positive={}
for cid,spec in reg['claims'].items():
    args={name:argobjects[typ] for name,typ in spec.get('args',[])}
    cr=rt.eval_evidence_claim(cid,base,**args);positive[cid]=(cr,args)
    check('CANONICAL/'+cid+'/typed-result',lambda cr=cr:type(cr.result) is EvidenceValue)
    check('CANONICAL/'+cid+'/no-unresolved',lambda cr=cr:not cr.unresolved_dependencies)
    check('CANONICAL/'+cid+'/positive',lambda cr=cr:cr.result is EvidenceValue.PASS)
    cert=certificate(cr,base)
    check('CANONICAL/'+cid+'/attested-test-only',lambda cert=cert:cert.certificate_status is CertificateStatus.VALID and cert.assurance_scope=='SYNTHETIC_TEST_ONLY')
    check('CANONICAL/'+cid+'/no-implicit-trust',lambda cr=cr:rt.issue_claim_certificate(cr,bundle(cr),base).certificate_status is CertificateStatus.INCOMPLETE)
    check('CANONICAL/'+cid+'/flip-result-rejected',lambda cr=cr:invalid_result(replace(cr,result=EvidenceValue.FAIL),base))
    check('CANONICAL/'+cid+'/string-result-rejected',lambda cr=cr:invalid_result(replace(cr,result='PASS'),base))
    # Every consumed measured leaf is tested independently for absence and negation.
    supports=set(cr.support_receipt_digests)
    for key,receipt in base['leaf_receipts'].items():
        if 'leafreceipt:'+stable_digest(receipt) not in supports:continue
        name=receipt.predicate_id
        env=copy.deepcopy(base);env['leaf_receipts'].pop(key)
        missing=rt.eval_evidence_claim(cid,env,**args)
        check('CANONICAL/'+cid+'/'+name+'/missing-not-pass',lambda v=missing:v.result is not EvidenceValue.PASS)
        env=copy.deepcopy(base);env['leaf_receipts'][key]=replace(receipt,result=EvidenceValue.FAIL)
        neg=rt.eval_evidence_claim(cid,env,**args)
        check('CANONICAL/'+cid+'/'+name+'/negative-not-pass',lambda v=neg:v.result is not EvidenceValue.PASS)
        # A trusted review of a negative result must remain certifiable.
        check('CANONICAL/'+cid+'/'+name+'/negative-certifiable',lambda neg=neg,env=env:certificate(neg,env).certificate_status is CertificateStatus.VALID)

cr,args=positive['LAB-CLOSURE-1'];pol,att=fixture_trust(base);b=bundle(cr)
check('I01/unregistered-claim',lambda:invalid_result(replace(cr,claim_id='made-up-claim'),base))
# Recompute a tampered digest too: canonical re-evaluation must still reject it.
tampered=replace(cr,result=EvidenceValue.FAIL);tampered=replace(tampered,evaluation_digest=stable_digest(evaluation_payload(tampered)))
check('I02/rehashed-result-canonical-replay',lambda:invalid_result(tampered,base))
check('I03/NA-string',lambda:invalid_result(replace(cr,result='NA'),base))
check('I04/no-signatures',lambda:certificate(cr,base,pol,()).certificate_status is CertificateStatus.INCOMPLETE)
check('I04/untrusted-key',lambda:certificate(cr,base,replace(pol,trusted_keys=()),att).certificate_status is CertificateStatus.INVALID)
check('I04/corrupt-signature',lambda:certificate(cr,base,pol,(replace(att[0],signature=b'X'*64),)+att[1:]).certificate_status is CertificateStatus.INVALID)
check('I04/wrong-evaluator-registration',lambda:certificate(cr,base,replace(pol,evaluators=()),att).certificate_status is CertificateStatus.INVALID)
check('I04/no-synthetic-lab-promotion',lambda:certificate(cr,base,replace(pol,allow_synthetic=False),att).certificate_status is CertificateStatus.INVALID)
check('I04/claim-scientific-truth-unasserted',lambda:certificate(cr,base,pol,att).scientific_validation=='NOT_ESTABLISHED_BY_SOFTWARE')
check('I05/empty-raw-closure',lambda:rt.issue_claim_certificate(cr,replace(b,evidence_receipt_refs=()),base,policy=pol,attestations=att).certificate_status is CertificateStatus.INVALID)
check('I05/empty-support',lambda:rt.issue_claim_certificate(cr,replace(b,support_receipt_digests=()),base,policy=pol,attestations=att).certificate_status is CertificateStatus.INVALID)
changed=copy.deepcopy(base);old=changed['evidence_receipts']['ev'];changed['evidence_receipts']['ev']=replace(old,assay_id='another-assay')
check('I06/raw-id-same-content-changed',lambda:certificate(cr,changed,pol,att).certificate_status is CertificateStatus.INVALID)
changed=copy.deepcopy(base);ref=next(iter(changed['raw_objects']));changed['raw_objects'][ref]=b'tampered'
check('I06/raw-bytes-changed',lambda:certificate(cr,changed,pol,att).certificate_status is CertificateStatus.INVALID)
check('I07/bundle-wrong-witness',lambda:rt.issue_claim_certificate(cr,replace(b,physical_witness_ref='other-witness'),base,policy=pol,attestations=att).certificate_status is CertificateStatus.INVALID)
changed=copy.deepcopy(base);key=next(k for k,v in changed['leaf_receipts'].items() if 'leafreceipt:'+stable_digest(v) in cr.support_receipt_digests);lr=changed['leaf_receipts'][key];changed['leaf_receipts'][key]=replace(lr,input_digest='0'*64)
check('I08/input-digest-verified',lambda:rt.eval_evidence_claim('LAB-CLOSURE-1',changed,**args).result is EvidenceValue.NA)
changed=copy.deepcopy(base);dr=changed['domains']['REWitness'];changed['domains']['REWitness']=replace(dr,type_id='PCSWitness')
check('I09/wrong-domain-label',lambda:rt.eval_evidence_claim('RE-ENDO-1',changed,r=R,B0=B0).result is EvidenceValue.NA)
for x in [True,False,'False',float('inf'),float('nan'),-1]:
    tr=fixture_threshold('distance_tolerance_normalized',.1,d_max=x)
    check('I11/invalid-dmax/'+repr(x),lambda tr=tr:not validate_threshold_receipt(tr.contract_id,{'domain':'[0,d_max)'},tr)[0])
tr=fixture_threshold('reachability_probability',.01)
check('I12/string-preregistered',lambda:not validate_threshold_receipt(tr.contract_id,{'domain':'(0,1]'},replace(tr,preregistered='False'))[0])
check('I13/negative-unbounded-distance',lambda:not validate_threshold_receipt('distance_tolerance_unbounded',{'domain':'[0,inf)'},fixture_threshold('distance_tolerance_unbounded',-.1))[0])
check('I14/non-string-key-rejected',lambda:raises(lambda:stable_digest({1:'a'})))
check('I14/int-float-distinct',lambda:stable_digest(1)!=stable_digest(1.0))
check('I14/tuple-list-distinct',lambda:stable_digest((1,))!=stable_digest([1]))
check('I14/enum-string-distinct',lambda:stable_digest(EvidenceValue.PASS)!=stable_digest('PASS'))
check('I14/nonfinite-rejected',lambda:raises(lambda:stable_digest(float('nan'))))
check('THRESHOLD/freeze-after-observation',lambda:not validate_freeze(replace(tr,frozen_at='2026-09-03T00:00:00Z'))[0])
check('THRESHOLD/timezone-required',lambda:not validate_freeze(replace(tr,frozen_at='2026-09-01T00:00:00'))[0])
changed=copy.deepcopy(base);changed['threshold_receipts']['time_horizon']=replace(changed['threshold_receipts']['time_horizon'],units='h')
check('THRESHOLD/no-implicit-unit-conversion',lambda:rt.eval_evidence_claim('HANDOFF-1',changed,**positive['HANDOFF-1'][1]).result is EvidenceValue.NA)
check('POLICY/frozen-threshold-pinning',lambda:certificate(positive['NAT-REACH-1'][0],base,replace(pol,frozen_threshold_digests=()),att).certificate_status is CertificateStatus.INVALID)

# Explicit complete-world callable type checking (I10).
for bad in ['FAIL','NA',1,None]:
    cw=copy.deepcopy(world);cw['predicates']['G_coop_complete']=lambda *a,bad=bad:bad
    check('I10/formal-callable/'+repr(bad),lambda cw=cw:raises(lambda:rt.eval_world_claim('RE-BENCH-W-1',cw,w_RE=base_objects()[0])))
# Parent ancestry must resolve transitively, reject missing bytes and cyclic refs.
e=copy.deepcopy(base);parent=e['evidence_receipts']['ev'];child=replace(parent,evidence_id='child',parent_evidence_refs=('ev',));child=replace(child,input_digest=stable_digest(raw_payload(child)));e['evidence_receipts']['child']=child
check('ANCESTRY/transitive-parent',lambda:set(evidence_closure(('child',),e)[0])=={'ev','child'})
e_missing=copy.deepcopy(e);del e_missing['evidence_receipts']['ev']
check('ANCESTRY/missing-parent-rejected',lambda:raises(lambda:evidence_closure(('child',),e_missing)))
e_cycle=copy.deepcopy(e);cyc=replace(parent,parent_evidence_refs=('child',));cyc=replace(cyc,input_digest=stable_digest(raw_payload(cyc)));e_cycle['evidence_receipts']['ev']=cyc
check('ANCESTRY/cycle-rejected',lambda:raises(lambda:evidence_closure(('child',),e_cycle)))
e=copy.deepcopy(base);e['domains']['REWitness']=replace(e['domains']['REWitness'],scope_route_digest='different-route')
check('DOMAIN/route-scope-mismatch',lambda:rt.eval_evidence_claim('RE-ENDO-1',e,r=R,B0=B0).result is EvidenceValue.NA)
check('THRESHOLD/production-pins-numbers',lambda:certificate(positive['HANDOFF-1'][0],base,replace(pol,frozen_threshold_digests=()),att).certificate_status is CertificateStatus.INVALID)

# Independent numerical reference: high-precision roots, plus analytic boundary cases.
mp.mp.dps=100
for m in [0,.5,1,1+1e-12,1.000001,1.01,1.4,2,3,10,50]:
    est=poisson_branching_estimate(m)
    if m<=1:ref=mp.mpf(0)
    else:
        mm=mp.mpf(str(m));ref=1+mp.lambertw(-mm*mp.exp(-mm),0)/mm
    check('N02/reference/'+str(m),lambda est=est,ref=ref:est.status=='CONVERGED' and math.isclose(est.survival,float(ref),rel_tol=2e-11,abs_tol=1e-30))
    check('N02/bracket/'+str(m),lambda est=est,ref=ref:mp.mpf(est.survival_lower)-mp.mpf('1e-85')<=ref<=mp.mpf(est.survival_upper)+mp.mpf('1e-85'))
check('N02/iteration-budget',lambda:poisson_branching_estimate(1.001,max_iter=1).status=='NONCONVERGED')
check('N02/bool-mean',lambda:raises(lambda:poisson_branching_estimate(True)))
g=cycle_gain(transfer_fraction=.1,recovery=1,copy_rate_per_h=.0011,loss_rate_per_h=0,interval_h=48)
check('D01/transfer-budget',lambda:math.isclose(g['gain'],.1*math.exp(.0011*48),rel_tol=1e-14) and not g['replacement_in_this_model'])
check('D01/gain-overflow-explicit',lambda:cycle_gain(transfer_fraction=1,recovery=1,copy_rate_per_h=1000,loss_rate_per_h=0,interval_h=1)['numerical_status']=='OVERFLOW_GAIN')
check('D01/reject-zero-transfer',lambda:raises(lambda:cycle_gain(transfer_fraction=0,recovery=1,copy_rate_per_h=1,loss_rate_per_h=0,interval_h=1)))
x=immigration_trajectory(100,.1,90,10)['trajectory'][-1]
check('D02/abundance-is-not-lineage',lambda:math.isclose(x['abundance'],100) and x['founder_descendant_contribution']<1e-7)
p=finite_birth_death_survival(birth_per_h=1.4,death_per_h=1,capacity=20,initial=1,horizon_h=10)
check('T01/finite-horizon-vs-indefinite',lambda:0<p['survival_through_horizon']<1 and p['eventual_extinction']==1)
p=finite_birth_death_survival(birth_per_h=0,death_per_h=.2,capacity=20,initial=1,horizon_h=3)
check('T01/pure-death-analytic',lambda:math.isclose(p['survival_through_horizon'],math.exp(-.6),rel_tol=1e-11))
check('T01/no-death-survives',lambda:finite_birth_death_survival(birth_per_h=1,death_per_h=0,capacity=20,initial=1,horizon_h=10)['survival_through_horizon']>1-1e-10)
check('T02/perfect-copy-standing-selection',lambda:(2*1)/(2*1+1*1)>1/2)
p=conditional_poisson_mixture([0,10],[.5,.5]);check('D03/mixture-not-mean',lambda:p['probability']<p['naive_mean_hazard_probability'])
u=generated_measure([[1,0],[0,9]],[.5,.5]);check('MEASURE/molecule-vs-compartment',lambda:u['molecule_weighted_mu_gen']==[.1,.9])
check('MEASURE/empty-population',lambda:generated_measure([[0,0]],[1])['molecule_weighted_mu_gen'] is None)

# Operational preflight is a record-completeness check, never scientific authorization.
from operational_preflight_v2_7_7 import preflight
cfg={k:'test-reference-not-real' for k in ['run_id','route_id','boundary_id','assay_qualification_ref','independent_review_ref','institutional_safety_review_ref','power_analysis_ref','control_plan_ref','analysis_plan_ref','ancestry_plan_ref','degradation_recovery_calibration_ref']}
cfg.update({k:'a'*64 for k in ['route_spec_digest','boundary_spec_digest','preregistration_digest','analysis_code_digest']})
cfg.update({k:True for k in ['no_full_length_founder_topup','unsorted_actual_output','pilot_qualified','fresh_confirmatory_material']})
cfg.update(tier='A_TRANSITION_CORE',data_origin='LABORATORY',frozen_at='2026-01-01T00:00:00Z',first_claim_bearing_observation='2026-01-02T00:00:00Z',transfer_budget={'model':'LINEARIZED_FIXED_RATE_CYCLE','applicability_qualified':True,'calibration_ref':'synthetic-record-test','transfer_fraction':.095,'recovery':.9,'copy_rate_per_h':.1,'loss_rate_per_h':.01,'interval_h':48,'rate_basis':'CONSERVATIVE_MEASURED_BOUND'})
check('PREFLIGHT/complete-record-not-authorization',lambda:preflight(cfg)['status']=='RECORD_COMPLETE_PENDING_INDEPENDENT_AUTHORIZATION' and preflight(cfg)['scientific_pass'] is False and preflight(cfg)['safety_authorization_issued'] is False)
check('PREFLIGHT/empty-record',lambda:preflight({})['status']=='NOT_READY')
check('PREFLIGHT/wrong-input-type',lambda:preflight([])['status']=='NOT_READY')
for field,bad in [('pilot_qualified','True'),('power_analysis_ref',''),('route_spec_digest','none'),('first_claim_bearing_observation','2025-01-01T00:00:00Z'),('frozen_at','2026-01-01'),('data_origin','SYNTHETIC')]:
    testcfg={**cfg,field:bad}
    check('PREFLIGHT/reject-'+field,lambda c=testcfg:preflight(c)['status']=='NOT_READY')
check('PREFLIGHT/B-missing-upstream',lambda:preflight({**cfg,'tier':'B_FULL_ROUTE','upstream_qualification':None})['status']=='NOT_READY')
budget={**cfg['transfer_budget'],'copy_rate_per_h':.0011,'loss_rate_per_h':0}
check('PREFLIGHT/washout-not-ready',lambda:preflight({**cfg,'transfer_budget':budget})['status']=='NOT_READY')
check('PREFLIGHT/malformed-budget',lambda:preflight({**cfg,'transfer_budget':{**budget,'copy_rate_per_h':[]}})['status']=='NOT_READY')
check('PREFLIGHT/sampling-budget-fraction',lambda:math.isclose((20-1)/20 * (1.9/19),.095,rel_tol=1e-14))
for bad in [None,{},123]:
    testrec=replace(next(iter(base['threshold_receipts'].values())),preregistration_digest=bad)
    check('THRESHOLD/malformed-freeze-'+str(type(bad).__name__),lambda r=testrec:validate_freeze(r)[0] is False)
check('THRESHOLD/extreme-integer-reject',lambda:finite_number(10**10000) is False)

if __name__=='__main__':
    report={'suite':'release_regressions','version':'2.7.7','category':'synthetic_invariants_and_mathematics','test_count':len(CASES),'passed':sum(x['pass'] for x in CASES),'failed':[x for x in CASES if not x['pass']],'cases':CASES}
    report['overall_pass']=report['passed']==report['test_count']
    (ROOT/'release_regression_results_v2_7_7.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({k:v for k,v in report.items() if k!='cases'},indent=2))
    raise SystemExit(0 if report['overall_pass'] else 1)
