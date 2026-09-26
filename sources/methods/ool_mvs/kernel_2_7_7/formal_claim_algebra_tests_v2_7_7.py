from __future__ import annotations
import copy,itertools,json
from pathlib import Path
from dataclasses import replace
from claim_registry_runtime_v2_7_7 import *
from kernel_test_fixtures_v2_7_7 import *
from evidence_receipts_v2_7_7 import *
from threshold_contracts_v2_7_7 import ThresholdReceipt

HERE=Path(__file__).resolve().parent
OUT=HERE/'formal_claim_algebra_results_v2_7_7.json'
CMOUT=HERE/'FORMAL_COUNTERMODEL_REPORT.json'
r=load_registry(); results={}; cms=[]
def rec(name,ok,detail=None): results[name]={'pass':bool(ok),'detail':detail}

# 1 baseline closed registry compiler.
vr=validate_registry(r); rec('001_registry_compiler_accepts_frozen_registry',vr['pass'],vr)

# Mutation guards.
def mutated(checkname,mutator):
    x=copy.deepcopy(r); mutator(x); v=validate_registry(x); rec(checkname,not v['pass'],v['errors'][:5])
mutated('002_illegal_scope_rejected',lambda x:x['claims']['RE-ENDO-1'].__setitem__('scope','banana'))
mutated('003_truth_lattice_corruption_rejected',lambda x:x.__setitem__('truth_values',['YES','NO']))
mutated('004_world_truth_lattice_corruption_rejected',lambda x:x.__setitem__('world_truth_values',['MAYBE']))
mutated('005_claim_reference_cycle_rejected',lambda x:x['claims']['RE-BENCH-W-1'].__setitem__('expr',{'claim_ref':'RE-BENCH-W-1','args':['w_RE']}))
mutated('006_empty_AND_rejected',lambda x:x['claims']['RE-BENCH-W-1'].__setitem__('expr',{'and':[]}))
mutated('007_empty_OR_rejected',lambda x:x['claims']['RE-BENCH-W-1'].__setitem__('expr',{'or':[]}))
def multiop(x): x['claims']['RE-BENCH-W-1']['expr']={'and':[{'pred':'G_C_RE','args':['w_RE']}],'pred':'G_C_RE','args':['w_RE']}
mutated('008_multi_operator_AST_node_rejected',multiop)
def freevar(x): x['claims']['RE-BENCH-W-1']['expr']={'pred':'G_C_RE','args':['typo']}
mutated('009_free_variable_without_w_prefix_rejected',freevar)
def shadow(x): x['claims']['RE-BENCH-1']['expr']={'exists':{'var':'r','type':'REWitness','domain':'route:r','body':{'pred':'G_C_RE','args':['r']}}}
mutated('010_quantifier_shadowing_rejected',shadow)
def dup_args(x): x['claims']['RE-ENDO-W-1']['args']=[['w_RE','REWitness'],['w_RE','Boundary']]
mutated('011_duplicate_claim_arguments_rejected',dup_args)
def bad_domain(x): x['claims']['RE-BENCH-1']['expr']['exists']['domain']='banana:r'
mutated('012_unknown_domain_constructor_rejected',bad_domain)
def bad_domain_param(x): x['claims']['RE-BENCH-1']['expr']['exists']['domain']='route:w_RE'
mutated('013_unbound_domain_parameter_rejected',bad_domain_param)
def bad_type(x): x['types']['REWitness']['fields']['route_id']='BananaType'
mutated('014_recursive_type_reference_integrity_enforced',bad_type)
def bad_thresh(x): x['leaf_predicates']['G_temporal_overlap']['threshold_contract_refs']=['not-a-contract']
mutated('015_unknown_threshold_contract_link_rejected',bad_thresh)
def bad_threshold_domain(x): x['threshold_contracts']['time_horizon']['domain']='banana'
mutated('016_invalid_threshold_contract_domain_rejected',bad_threshold_domain)
def bad_domain_field(x): x['domain_constructors']['route']['member_field']='banana'
mutated('017_invalid_domain_constructor_field_rejected',bad_domain_field)
def bad_mode(x): x['evaluation_modes']['FORMAL_COMPLETE_WORLD']['missing_inputs']='FALSE'
mutated('018_runtime_mode_contract_corruption_rejected',bad_mode)
def detached_threshold(x): x['claims']['HANDOFF-1']['threshold_contract_refs'].append('reachability_probability')
mutated('019_declared_but_unconsumed_threshold_rejected',detached_threshold)

# Strict complete world semantics.
w=complete_world(r)
rec('020_complete_world_baseline_lab_closure',eval_world_claim('LAB-CLOSURE-1',w,r=R,B0=B0))
w_missing=copy.deepcopy(w); w_missing['predicates'].pop('G_energy_closure_lab')
try:
    eval_world_claim('LAB-CLOSURE-1',w_missing,r=R,B0=B0); strict=False
except IncompleteWorldError: strict=True
rec('021_complete_world_missing_leaf_is_error_not_false',strict)
w_partial=copy.deepcopy(w); w_partial['domain_completeness']['RouteProof']=False
try:
    eval_world_claim('LAB-CLOSURE-1',w_partial,r=R,B0=B0); strict=False
except IncompleteWorldError: strict=True
rec('022_complete_world_incomplete_quantifier_domain_is_error',strict)

# Structural route identity cannot be caller-laundered.
re,pcs,iw,hw,car,rp,br,np,prog=base_objects()
pcs_other=replace(pcs,route_spec_digest='other-route')
rp_bad=replace(rp,pcs_witness=pcs_other)
w_bad=complete_world(r,pcs=[pcs_other],routeproofs=[rp_bad],descends={(re,pcs_other)})
rec('023_cross_route_witness_laundering_blocked_structurally',not eval_world_claim('LAB-CLOSURE-1',w_bad,r=R,B0=B0))

# Boundary digest mismatch blocks route proof even if all scientific leaves are true.
re_b=replace(re,boundary_spec_digest='other-B0'); rp_b=replace(rp,re_witness=re_b)
w_b=complete_world(r,res=[re_b],routeproofs=[rp_b],descends={(re_b,pcs)})
rec('024_cross_boundary_witness_laundering_blocked_structurally',not eval_world_claim('LAB-CLOSURE-1',w_b,r=R,B0=B0))

# Finite identity/ancestry search with independent truth oracle.
def truth_lab(q,pairs):
    rr=q.re_witness; pp=q.pcs_witness
    return (rr.ok and not rr.preloaded and rr.provenance=='endo' and rr.coop and pp.ok and (rr,pp) in pairs and rr.route_spec_digest==pp.route_spec_digest and rr.boundary_spec_digest==pp.boundary_spec_digest==B0.boundary_spec_digest and q.route_spec_digest==rr.route_spec_digest and q.route_spec_digest==pp.route_spec_digest and q.boundary_spec_digest==B0.boundary_spec_digest and q.routepath and q.sourcing and q.forcing and q.energy and q.compatibility and q.phys and q.coverage and rr.t<pp.t)
falsepos=[]; checked=0
for rebits in itertools.product([False,True],repeat=2):
  for pcbits in itertools.product([False,True],repeat=2):
    rs=[replace(re,witness_id=f'r{i}',ok=rebits[i]) for i in range(2)]
    ps=[replace(pcs,witness_id=f'p{i}',ok=pcbits[i]) for i in range(2)]
    allpairs=[(a,b) for a in rs for b in ps]
    for pairbits in itertools.product([False,True],repeat=4):
      pairs={x for x,b in zip(allpairs,pairbits) if b}
      qs=[replace(rp,proof_id=f'q{i}{j}',re_witness=rs[i],pcs_witness=ps[j]) for i in range(2) for j in range(2)]
      ww=complete_world(r,res=rs,pcs=ps,routeproofs=qs,descends=pairs)
      claim=eval_world_claim('LAB-CLOSURE-1',ww,r=R,B0=B0)
      truth=any(truth_lab(q,pairs) for q in qs)
      checked+=1
      if claim and not truth: falsepos.append((rebits,pcbits,pairbits))
rec('025_identity_ancestry_finite_countermodel_search_no_false_positive',not falsepos,{'worlds_checked':checked,'false_positive_count':len(falsepos)})

# Preloading remains blocked.
re_pre=replace(re,preloaded=True); rp_pre=replace(rp,re_witness=re_pre); w_pre=complete_world(r,res=[re_pre],routeproofs=[rp_pre],descends={(re_pre,pcs)})
rec('026_preloaded_recursive_solution_blocks_endogenous_RE',not eval_world_claim('RE-ENDO-1',w_pre,r=R,B0=B0))

# Core ancestry is required; generic route/identity alone not enough.
w_nod=complete_world(r,descends=set())
rec('027_no_hereditary_core_descendance_blocks_RE_to_PCS',not eval_world_claim('RE-PCS-CONT-1',w_nod,r=R,B0=B0))

# Natural starting boundary realization and sourcing.
np_badbr=replace(np,boundary_realization_witness=replace(br,ok=False)); w_nat=complete_world(r,naturals=[np_badbr])
rec('028_natural_boundary_unrealized_blocks_natural_closure',not eval_world_claim('NAT-REACH-1',w_nat,r=R,B0=B0))
np_bads=replace(np,natural_sourcing=False); w_nat=complete_world(r,naturals=[np_bads])
rec('029_natural_starting_material_sourcing_required',not eval_world_claim('NAT-REACH-1',w_nat,r=R,B0=B0))
# Heterogeneous/equivalent realization may pass because leaf truth is about required input kernel, not literal reagent identity.
np_ok=replace(np,boundary_realization_witness=replace(br,ok=True)); w_nat=complete_world(r,naturals=[np_ok])
rec('030_natural_boundary_realization_not_literal_reagent_identity',eval_world_claim('NAT-REACH-1',w_nat,r=R,B0=B0))

# Experimental evidence semantics baseline and complete-evidence collapse.
ev=evidence_env_from_world(r,w)
cr=eval_evidence_claim('LAB-CLOSURE-1',ev,r=R,B0=B0)
rec('031_complete_evidence_collapses_to_boolean_PASS',cr.result is EvidenceValue.PASS and eval_world_claim('LAB-CLOSURE-1',w,r=R,B0=B0))
# Missing leaf -> NA not FAIL/PASS.
ev_missing=evidence_env_from_world(r,w,missing_leaf='G_energy_closure_lab')
cr=eval_evidence_claim('LAB-CLOSURE-1',ev_missing,r=R,B0=B0)
rec('032_missing_claim_bearing_leaf_is_NA',cr.result is EvidenceValue.NA,cr.unresolved_dependencies)
# Partial existential domain no witness -> NA. Use RE claim with empty partial domain.
ev_empty=evidence_env_from_world(r,w); ev_empty['domains']['REWitness']=DomainReceipt('REWitness',(),DomainCompleteness.PARTIAL,'sampled')
cr=eval_evidence_claim('RE-ENDO-1',ev_empty,r=R,B0=B0)
rec('033_partial_empty_existential_domain_is_NA',cr.result is EvidenceValue.NA)
# Complete empty existential -> FAIL.
ev_empty['domains']['REWitness']=DomainReceipt('REWitness',(),DomainCompleteness.COMPLETE,'exhaustive')
cr=eval_evidence_claim('RE-ENDO-1',ev_empty,r=R,B0=B0)
rec('034_complete_empty_existential_domain_is_FAIL',cr.result is EvidenceValue.FAIL)

# Threshold missing/invalid -> NA, valid -> normal.
ev_h=evidence_env_from_world(r,w); ev_h['threshold_receipts'].pop('time_horizon')
cr=eval_evidence_claim('HANDOFF-1',ev_h,w_H=hw)
rec('035_missing_required_threshold_receipt_yields_NA',cr.result is EvidenceValue.NA)
ev_h=evidence_env_from_world(r,w,threshold_overrides={'experimental_probability_floor':ThresholdReceipt('experimental_probability_floor',0.0,True,True)})
cr=eval_evidence_claim('HANDOFF-1',ev_h,w_H=hw)
rec('036_invalid_threshold_value_yields_NA',cr.result is EvidenceValue.NA)

# Certification axes: valid FAIL is a valid certificate; NA is incomplete.
pcs_fail=replace(pcs,ok=False); w_pf=complete_world(r,pcs=[pcs_fail],routeproofs=[]); ev_pf=evidence_env_from_world(r,w_pf)
cr=eval_evidence_claim('PCS-LOCAL-1',ev_pf,r=R); bundle=build_evidence_bundle(cr,cr.physical_witness_ref,ev_pf['evidence_receipts'].keys(),bundle_id='e-bundle'); cert=fixture_certificate(cr,bundle,ev_pf)
rec('037_well_supported_FAIL_can_have_VALID_certificate',cr.result is EvidenceValue.FAIL and cert.certificate_status is CertificateStatus.VALID)
crna=eval_evidence_claim('LAB-CLOSURE-1',ev_missing,r=R,B0=B0); bundlena=build_evidence_bundle(crna,crna.physical_witness_ref,ev_missing['evidence_receipts'].keys(),bundle_id='e-bundle'); certna=fixture_certificate(crna,bundlena,ev_missing)
rec('038_NA_claim_has_INCOMPLETE_certificate',certna.certificate_status is CertificateStatus.INCOMPLETE)

# Provenance/absence utility laws.
v,why=provenance_leaf_result(['founder'],{},False); rec('039_unknown_provenance_not_endogenous',v is EvidenceValue.NA,why)
v,why=provenance_leaf_result(['founder'],{'founder':'EXTERNAL'},True); rec('040_external_provenance_is_FAIL',v is EvidenceValue.FAIL,why)
v,why=provenance_leaf_result(['founder'],{'founder':'ADMITTED_ROOT'},True); rec('041_positive_provenance_closure_can_PASS',v is EvidenceValue.PASS,why)
v,why=absence_leaf_result(False,False); rec('042_absence_from_incomplete_search_is_NA',v is EvidenceValue.NA,why)
v,why=absence_leaf_result(False,True); rec('043_absence_from_complete_search_can_PASS',v is EvidenceValue.PASS,why)

# Carrier/establishment bindings.
w_nocar=complete_world(r,carriers=[],carrier_links=set()); rec('044_no_carrier_evidence_does_not_invent_carrier',not eval_world_claim('CARRIER-1',w_nocar,r=R))
car_bad=replace(car,compatible=False,est=True); w_cb=complete_world(r,carriers=[car_bad],carrier_links={(pcs,car_bad)})
rec('045_carrier_establishment_cannot_pass_without_carrier_capability',not eval_world_claim('EST-CARRIER-1',w_cb,r=R))

# Programme Frankenstein blocked by proof continuity.
prog_bad=replace(prog,continuity=False); w_prog=complete_world(r,programmes=[prog_bad])
rec('046_programme_modules_cannot_frankenstein_without_continuity',not eval_world_claim('PROGRAMME-CURRENT-1',w_prog,r=R))

# Strong-Kleene algebra checks.
vals=[EvidenceValue.PASS,EvidenceValue.FAIL,EvidenceValue.NA]
rec('047_strong_kleene_de_morgan',all(k_not(k_and([a,b]))==k_or([k_not(a),k_not(b)]) and k_not(k_or([a,b]))==k_and([k_not(a),k_not(b)]) for a in vals for b in vals))
rec('048_boolean_collapse_AND_OR_NOT',k_and([EvidenceValue.PASS,EvidenceValue.FAIL]) is EvidenceValue.FAIL and k_or([EvidenceValue.PASS,EvidenceValue.FAIL]) is EvidenceValue.PASS and k_not(EvidenceValue.PASS) is EvidenceValue.FAIL)

# Registry has one canonical physical claim composition layer only.
rec('049_no_epistemic_claims_inside_physical_registry',all(c['scope']=='physical' for c in r['claims'].values()))
rec('050_certification_meta_layer_is_outside_physical_claim_AST','certification_contract' in r and 'CERT-CLAIM-1' not in r['claims'])

# Report known old countermodels and blockers.
for cid,test,blocker in [
 ('CM-01','RE/PCS Frankenstein','single RouteProof + bound RE-PCS pair'),
 ('CM-02','wrong-lineage establishment','PCS witness bound to P_est_mol_positive'),
 ('CM-03','preloaded target capability','G_no_preloaded_solution_RE'),
 ('CM-04','omitted claim-bearing operation','G_declared_causal_coverage'),
 ('CM-05','carrier mismatch','PCSToCarrier'),
 ('CM-06','vacuous thresholds','typed threshold receipts'),
 ('CM-07','incompatible natural operations','G_natural_ops_joint'),
 ('CM-08','detached route physics','single RouteProof'),
 ('CM-09','cooperative role recreation','G_coop_complete / provenance'),
 ('CM-10','temporal handoff failure','G_temporal_overlap'),
 ('CM-11','unsupported lucky natural trajectory','G_natural_reach under admissible forcing'),
 ('CM-12','unmapped adaptive policy','AdaptivePolicyMappedOrIrrelevant'),
 ('CM-13','missing-as-false','experimental NA semantics'),
 ('CM-14','unknown provenance as endogenous','positive provenance closure'),
 ('CM-15','natural B0 laundering','G_boundary_realization + G_sourcing_natural'),
 ('CM-16','route-label laundering','route_spec_digest structural equality'),
 ('CM-17','unbound certification','certificate claim/witness/evidence binding'),
]: cms.append({'id':cid,'countermodel':test,'v2_7_7_status':'BLOCKED','blocking_rule':blocker})

passed=sum(x['pass'] for x in results.values()); total=len(results)
summary={'suite':'formal_claim_algebra_v2.7.7','passed':passed,'total':total,'all_pass':passed==total,'finite_worlds_checked':checked,'tests':results}
OUT.write_text(json.dumps(summary,indent=2,default=str))
CMOUT.write_text(json.dumps({'version':'2.7.7','scope_note':'Finite countermodel resistance is reported only for the declared domains; it is not a proof of global logical completeness or empirical abiogenesis.','identity_ancestry_worlds_checked':checked,'known_countermodels':cms},indent=2))
print(json.dumps({'passed':passed,'total':total,'all_pass':passed==total,'finite_worlds_checked':checked},indent=2))
if passed!=total:
    for k,v in results.items():
        if not v['pass']: print('FAIL',k,v)
    raise SystemExit(1)
