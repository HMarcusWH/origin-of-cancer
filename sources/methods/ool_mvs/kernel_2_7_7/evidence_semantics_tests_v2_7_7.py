from __future__ import annotations
import json, copy
from pathlib import Path
from dataclasses import replace
from claim_registry_runtime_v2_7_7 import *
from evidence_receipts_v2_7_7 import *
from kernel_test_fixtures_v2_7_7 import *
from threshold_contracts_v2_7_7 import ThresholdReceipt

HERE=Path(__file__).resolve().parent; OUT=HERE/'evidence_semantics_results_v2_7_7.json'
r=load_registry(); w=complete_world(r); base=evidence_env_from_world(r,w); results={}
def rec(name,ok,detail=None): results[name]={'pass':bool(ok),'detail':detail}

# Algebra tables.
P,F,N=EvidenceValue.PASS,EvidenceValue.FAIL,EvidenceValue.NA
cases_and={(P,P):P,(P,F):F,(P,N):N,(F,P):F,(F,F):F,(F,N):F,(N,P):N,(N,F):F,(N,N):N}
cases_or={(P,P):P,(P,F):P,(P,N):P,(F,P):P,(F,F):F,(F,N):N,(N,P):P,(N,F):N,(N,N):N}
for i,(ab,exp) in enumerate(cases_and.items(),1):rec(f'{i:03d}_kleene_AND_{ab[0].value}_{ab[1].value}',k_and(ab) is exp)
for i,(ab,exp) in enumerate(cases_or.items(),10):rec(f'{i:03d}_kleene_OR_{ab[0].value}_{ab[1].value}',k_or(ab) is exp)
for i,(a,exp) in enumerate([(P,F),(F,P),(N,N)],19):rec(f'{i:03d}_kleene_NOT_{a.value}',k_not(a) is exp)

# Complete vs partial existential behavior.
ev=copy.deepcopy(base); cr=eval_evidence_claim('RE-ENDO-1',ev,r=R,B0=B0); rec('022_complete_evidence_RE_PASS',cr.result is P)
ev=copy.deepcopy(base); ev['domains']['REWitness']=DomainReceipt('REWitness',(),DomainCompleteness.COMPLETE,'exhaustive'); cr=eval_evidence_claim('RE-ENDO-1',ev,r=R,B0=B0);rec('023_complete_empty_RE_domain_FAIL',cr.result is F)
ev=copy.deepcopy(base); ev['domains']['REWitness']=DomainReceipt('REWitness',(),DomainCompleteness.PARTIAL,'sample'); cr=eval_evidence_claim('RE-ENDO-1',ev,r=R,B0=B0);rec('024_partial_empty_RE_domain_NA',cr.result is N)
ev=copy.deepcopy(base); ev['domains']['REWitness']=DomainReceipt('REWitness',(),DomainCompleteness.UNKNOWN,'unknown'); cr=eval_evidence_claim('RE-ENDO-1',ev,r=R,B0=B0);rec('025_unknown_RE_domain_NA',cr.result is N)

# Missing leaf, invalid receipt, binding mismatch.
ev=evidence_env_from_world(r,w,missing_leaf='G_seed'); rec('026_missing_leaf_NA',eval_evidence_claim('RE-ENDO-1',ev,r=R,B0=B0).result is N)
ev=copy.deepcopy(base); key=next(k for k in ev['leaf_receipts'] if k[0]=='G_seed'); rr=ev['leaf_receipts'][key]; ev['leaf_receipts'][key]=replace(rr,authority_mode='CALLER_ASSERTION'); rec('027_unauthorized_leaf_NA',eval_evidence_claim('RE-ENDO-1',ev,r=R,B0=B0).result is N)
ev=copy.deepcopy(base); key=next(k for k in ev['leaf_receipts'] if k[0]=='G_seed'); rr=ev['leaf_receipts'][key]; ev['leaf_receipts'][key]=replace(rr,predicate_id='G_C_RE'); rec('028_leaf_binding_mismatch_NA',eval_evidence_claim('RE-ENDO-1',ev,r=R,B0=B0).result is N)

# Relation receipts: missing core ancestry -> NA; explicit FAIL -> FAIL.
ev=copy.deepcopy(base); k=next(k for k in ev['relation_receipts'] if k[0]=='DescendsCore'); ev['relation_receipts'].pop(k); rec('029_missing_ancestry_relation_NA',eval_evidence_claim('RE-PCS-CONT-1',ev,r=R,B0=B0).result is N)
ev=copy.deepcopy(base); k=next(k for k in ev['relation_receipts'] if k[0]=='DescendsCore'); old=ev['relation_receipts'][k]; ev['relation_receipts'][k]=replace(old,result=F,reason_code='no_core_descent'); rec('030_explicit_failed_core_ancestry_FAIL',eval_evidence_claim('RE-PCS-CONT-1',ev,r=R,B0=B0).result is F)

# Threshold contract semantics.
for idx,cid in enumerate(['experimental_probability_floor','time_horizon'],31):
    ev=copy.deepcopy(base); ev['threshold_receipts'].pop(cid); rec(f'{idx:03d}_handoff_missing_{cid}_NA',eval_evidence_claim('HANDOFF-1',ev,w_H=base_objects()[3]).result is N)
ev=copy.deepcopy(base); ev['threshold_receipts']['time_horizon']=ThresholdReceipt('time_horizon',-1,True,True);rec('033_negative_time_horizon_NA',eval_evidence_claim('HANDOFF-1',ev,w_H=base_objects()[3]).result is N)
ev=copy.deepcopy(base); ev['threshold_receipts']['experimental_probability_floor']=ThresholdReceipt('experimental_probability_floor',0.2,False,True);rec('034_posthoc_probability_floor_NA',eval_evidence_claim('HANDOFF-1',ev,w_H=base_objects()[3]).result is N)
ev=copy.deepcopy(base); ev['threshold_receipts']['experimental_probability_floor']=ThresholdReceipt('experimental_probability_floor',0.2,True,False);rec('035_unresolved_probability_floor_NA',eval_evidence_claim('HANDOFF-1',ev,w_H=base_objects()[3]).result is N)

# Natural reachability/plausibility thresholds separate.
ev=copy.deepcopy(base); ev['threshold_receipts'].pop('plausibility_probability_floor');rec('036_nat_reach_does_not_require_plausibility_floor',eval_evidence_claim('NAT-REACH-1',ev,r=R,B0=B0).result is P)
rec('037_nat_plaus_requires_plausibility_floor',eval_evidence_claim('NAT-PLAUS-1',ev,r=R,B0=B0).result is N)
ev=copy.deepcopy(base); ev['threshold_receipts'].pop('reachability_probability');rec('038_nat_reach_requires_reachability_contract',eval_evidence_claim('NAT-REACH-1',ev,r=R,B0=B0).result is N)

# Certificates: result and integrity separate.
pcs_fail=replace(base_objects()[1],ok=False); wf=complete_world(r,pcs=[pcs_fail],routeproofs=[]); ef=evidence_env_from_world(r,wf); cr=eval_evidence_claim('PCS-LOCAL-1',ef,r=R); bundle=build_evidence_bundle(cr,cr.physical_witness_ref,ef['evidence_receipts'].keys(),bundle_id='bundle'); cert=fixture_certificate(cr,bundle,ef);rec('039_valid_TEST_certificate_can_certify_FAIL',cr.result is F and cert.certificate_status is CertificateStatus.VALID)
ena=evidence_env_from_world(r,w,missing_leaf='G_phys'); cr=eval_evidence_claim('LAB-CLOSURE-1',ena,r=R,B0=B0); bundle=build_evidence_bundle(cr,cr.physical_witness_ref,ena['evidence_receipts'].keys(),bundle_id='bundle'); cert=fixture_certificate(cr,bundle,ena);rec('040_NA_produces_INCOMPLETE_certificate',cr.result is N and cert.certificate_status is CertificateStatus.INCOMPLETE)
cr0=eval_evidence_claim('LAB-CLOSURE-1',base,r=R,B0=B0); bundle0=build_evidence_bundle(cr0,'',base['evidence_receipts'].keys(),bundle_id='bundle'); cert=fixture_certificate(cr0,bundle0,base);rec('041_unbound_physical_witness_invalid_certificate',cert.certificate_status is CertificateStatus.INVALID)
bundle0=build_evidence_bundle(cr0,cr0.physical_witness_ref,base['evidence_receipts'].keys(),bundle_id=''); bundle0=replace(bundle0,bundle_id=''); cert=fixture_certificate(cr0,bundle0,base);rec('042_unbound_evidence_bundle_invalid_certificate',cert.certificate_status is CertificateStatus.INVALID)
wrong=replace(build_evidence_bundle(cr0,cr0.physical_witness_ref,base['evidence_receipts'].keys(),bundle_id='wrong'),claim_id='PCS-LOCAL-1'); cert=fixture_certificate(cr0,wrong,base);rec('043_wrong_claim_bundle_binding_invalid',cert.certificate_status is CertificateStatus.INVALID)
missing_support=replace(build_evidence_bundle(cr0,cr0.physical_witness_ref,base['evidence_receipts'].keys(),bundle_id='missing'),support_receipt_digests=()); cert=fixture_certificate(cr0,missing_support,base);rec('044_bundle_missing_support_receipts_invalid',cert.certificate_status is CertificateStatus.INVALID)
evraw=copy.deepcopy(base); evraw['evidence_receipts'].pop('ev'); rec('045_missing_raw_evidence_makes_claim_NA',eval_evidence_claim('LAB-CLOSURE-1',evraw,r=R,B0=B0).result is N)

# Provenance and absence utilities.
for n,(nodes,prov,complete,exp) in enumerate([
 (['a'],{},False,N),(['a'],{},True,N),(['a'],{'a':'EXTERNAL'},True,F),(['a'],{'a':'ADMITTED_ROOT'},True,P),(['a'],{'a':'DESCENDANT_OF_ADMITTED'},True,P)],43):
    val,_=provenance_leaf_result(nodes,prov,complete);rec(f'{n:03d}_provenance_{exp.value}',val is exp)
for n,(forbidden,complete,exp) in enumerate([(False,False,N),(False,True,P),(True,False,F),(True,True,F)],48):
    val,_=absence_leaf_result(forbidden,complete);rec(f'{n:03d}_absence_{exp.value}',val is exp)

# Evidence conflict policy represented by unresolved leaf -> NA (not a fourth physical truth value).
ev=copy.deepcopy(base); key=next(k for k in ev['leaf_receipts'] if k[0]=='G_H_PCS'); old=ev['leaf_receipts'][key]; ev['leaf_receipts'][key]=replace(old,result=N,reason_code='UNRESOLVED_CONFLICT');rec('055_unresolved_conflicting_assays_reduce_leaf_to_NA',eval_evidence_claim('PCS-LOCAL-1',ev,r=R).result is N)

# Algebraic invariants: De Morgan and monotonicity under consistent information refinement.
vals=[P,F,N]
rec('056_de_morgan_strong_kleene',all(k_not(k_and([a,b])) is k_or([k_not(a),k_not(b)]) and k_not(k_or([a,b])) is k_and([k_not(a),k_not(b)]) for a in vals for b in vals))
# Information order NA <= PASS and NA <= FAIL; PASS/FAIL incomparable.
def leq_info(a,b): return a is b or a is N
refinements=[(N,P),(N,F),(P,P),(F,F)]
rec('057_AND_information_monotone',all(leq_info(k_and([a,c]),k_and([b,d])) for a,b in refinements for c,d in refinements))
rec('058_OR_information_monotone',all(leq_info(k_or([a,c]),k_or([b,d])) for a,b in refinements for c,d in refinements))
rec('059_NOT_information_monotone',all(leq_info(k_not(a),k_not(b)) for a,b in refinements))

# Complete-evidence collapse across every canonical physical claim with a satisfied baseline.
re0,pcs0,iw0,hw0,car0,rp0,br0,np0,prog0=base_objects()
claim_args={
 'RE-BENCH-W-1':dict(w_RE=re0),
 'RE-ENDO-W-1':dict(w_RE=re0,B0=B0),
 'PCS-W-1':dict(w_PCS=pcs0),
 'RE-PCS-PAIR-1':dict(w_RE=re0,w_PCS=pcs0,B0=B0),
 'INTERFACE-W-1':dict(w_I=iw0),
 'HANDOFF-1':dict(w_H=hw0),
 'BRIDGE-W-1':dict(w_H=hw0),
 'RE-BENCH-1':dict(r=R),
 'RE-ENDO-1':dict(r=R,B0=B0),
 'PCS-LOCAL-1':dict(r=R),
 'PCS-LINKED-1':dict(r=R),
 'RE-PCS-CONT-1':dict(r=R,B0=B0),
 'INTERFACE-1':dict(r=R),
 'BRIDGE-1':dict(r=R),
 'PROGRAMME-CURRENT-1':dict(r=R),
 'LAB-CLOSURE-W-1':dict(w_route=rp0,B0=B0),
 'LAB-CLOSURE-1':dict(r=R,B0=B0),
 'NAT-REACH-W-1':dict(w_nat=np0,B0=B0),
 'NAT-REACH-1':dict(r=R,B0=B0),
 'NAT-PLAUS-1':dict(r=R,B0=B0),
 'CARRIER-1':dict(r=R),
 'INDIVIDUATED-1':dict(r=R),
 'EST-MOL-1':dict(r=R),
 'EST-CARRIER-1':dict(r=R),
}
for i,(cid,args) in enumerate(claim_args.items(),60):
    b=eval_world_claim(cid,w,**args); e=eval_evidence_claim(cid,base,**args).result
    rec(f'{i:03d}_complete_evidence_collapse_{cid}',(b and e is P) or ((not b) and e is F),{'world':b,'evidence':e.value})

# Property-style conservative-extension check over deterministic varied complete worlds.
# This exercises both TRUE and FALSE outcomes, including false ancestry/carrier relations.
import random
rng=random.Random(275)
comparisons=0; mismatches=[]
for case in range(64):
    re1=replace(re0,ok=rng.choice([True,False]),preloaded=rng.choice([True,False]),provenance=rng.choice(['endo','external']),coop=rng.choice([True,False]))
    pcs1=replace(pcs0,ok=rng.choice([True,False]),est=rng.choice([True,False]),linked=rng.choice([True,False]))
    iw1=replace(iw0,ok=rng.choice([True,False])); hw1=replace(hw0,ok=rng.choice([True,False]),temporal=rng.choice([True,False]))
    car1=replace(car0,compatible=rng.choice([True,False]),bounded=rng.choice([True,False]),no_replace=rng.choice([True,False]),est=rng.choice([True,False]),persists=rng.choice([True,False]))
    rp1=replace(rp0,re_witness=re1,pcs_witness=pcs1,routepath=rng.choice([True,False]),sourcing=rng.choice([True,False]),forcing=rng.choice([True,False]),energy=rng.choice([True,False]),compatibility=rng.choice([True,False]),phys=rng.choice([True,False]),coverage=rng.choice([True,False]))
    br1=replace(br0,ok=rng.choice([True,False])); np1=replace(np0,lab_proof=rp1,boundary_realization_witness=br1,natural_sourcing=rng.choice([True,False]),ops=rng.choice([True,False]),reach=rng.choice([True,False]),energy=rng.choice([True,False]),forcing=rng.choice([True,False]),adaptive=rng.choice([True,False]),plausible=rng.choice([True,False]))
    prog1=replace(prog0,interface_witness=iw1,handoff_witness=hw1,pcs_witness=pcs1,continuity=rng.choice([True,False]))
    desc={(re1,pcs1)} if rng.choice([True,False]) else set(); links={(pcs1,car1)} if rng.choice([True,False]) else set()
    ww=complete_world(r,res=[re1],pcs=[pcs1],interfaces=[iw1],handoffs=[hw1],carriers=[car1],routeproofs=[rp1],naturals=[np1],programmes=[prog1],descends=desc,carrier_links=links)
    ee=evidence_env_from_world(r,ww,completeness=DomainCompleteness.COMPLETE)
    objs={'w_RE':re1,'w_PCS':pcs1,'w_I':iw1,'w_H':hw1,'w_route':rp1,'w_nat':np1}
    for cid,args0 in claim_args.items():
        args={k:objs.get(k,v) for k,v in args0.items()}
        bw=eval_world_claim(cid,ww,**args); eeval=eval_evidence_claim(cid,ee,**args).result
        comparisons+=1
        if not ((bw and eeval is P) or ((not bw) and eeval is F)):
            mismatches.append({'case':case,'claim':cid,'world':bw,'evidence':eeval.value})
rec('084_complete_evidence_conservative_extension_64_worlds',not mismatches,{'worlds':64,'claim_comparisons':comparisons,'mismatches':mismatches[:5]})

passed=sum(v['pass'] for v in results.values()); total=len(results)
OUT.write_text(json.dumps({'suite':'evidence_semantics_v2.7.7','passed':passed,'total':total,'all_pass':passed==total,'tests':results},indent=2))
print(json.dumps({'passed':passed,'total':total,'all_pass':passed==total},indent=2))
if passed!=total:
    for k,v in results.items():
        if not v['pass']:print('FAIL',k,v)
    raise SystemExit(1)
