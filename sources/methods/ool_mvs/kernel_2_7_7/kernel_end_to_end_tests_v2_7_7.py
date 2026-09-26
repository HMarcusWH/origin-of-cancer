"""End-to-end scientific claim evaluation through the one canonical v2.7.7 registry.

This suite deliberately contains no hand-written composite claim formulas. It constructs typed
witnesses/leaf and relation receipts and asks the canonical runtime for claim results.
"""
from __future__ import annotations
import copy,json
from dataclasses import replace
from pathlib import Path
from claim_registry_runtime_v2_7_7 import *
from evidence_receipts_v2_7_7 import *
from kernel_test_fixtures_v2_7_7 import *
from threshold_contracts_v2_7_7 import ThresholdReceipt

HERE=Path(__file__).resolve().parent; OUT=HERE/'kernel_end_to_end_results_v2_7_7.json'
r=load_registry(); results={}
def rec(name,ok,detail=None):results[name]={'pass':bool(ok),'detail':detail}
def baseline():
    w=complete_world(r); return w,evidence_env_from_world(r,w),base_objects()
def set_leaf(ev,name,args,value,reason='fixture_mutation'):
    ev['leaf_receipts'][(name,tuple(args))]=build_leaf_receipt(name,args,EvidenceValue(value),['ev'],f'eval:{name}','2.7.7',reason,evidence_env=ev)
def del_leaf(ev,name,args):ev['leaf_receipts'].pop((name,tuple(args)),None)
def set_rel(ev,name,args,value,reason='fixture_mutation'):
    ev['relation_receipts'][(name,tuple(args))]=build_relation_receipt(name,args,EvidenceValue(value),['ev'],f'evalrel:{name}','2.7.7',reason,evidence_env=ev)
def expect(idx,name,cid,exp,ev,args):
    cr=eval_evidence_claim(cid,ev,**args); rec(f'{idx:03d}_{name}',cr.result is EvidenceValue(exp),{'claim':cid,'got':cr.result.value,'expected':EvidenceValue(exp).value,'unresolved':cr.unresolved_dependencies})

# Baseline end-to-end route and capability claims.
w,ev,o=baseline(); re,pcs,iw,hw,car,rp,br,np,prog=o
baseclaims=[
 ('benchmark_RE','RE-BENCH-1',P:=EvidenceValue.PASS,dict(r=R)),
 ('endogenous_RE','RE-ENDO-1',P,dict(r=R,B0=B0)),
 ('PCS','PCS-LOCAL-1',P,dict(r=R)),
 ('linked_PCS','PCS-LINKED-1',P,dict(r=R)),
 ('RE_to_PCS','RE-PCS-CONT-1',P,dict(r=R,B0=B0)),
 ('Interface','INTERFACE-1',P,dict(r=R)),
 ('bridge','BRIDGE-1',P,dict(r=R)),
 ('current_programme','PROGRAMME-CURRENT-1',P,dict(r=R)),
 ('lab_closure','LAB-CLOSURE-1',P,dict(r=R,B0=B0)),
 ('natural_reachable','NAT-REACH-1',P,dict(r=R,B0=B0)),
 ('natural_plausible','NAT-PLAUS-1',P,dict(r=R,B0=B0)),
 ('carrier','CARRIER-1',P,dict(r=R)),
 ('individuated','INDIVIDUATED-1',P,dict(r=R)),
 ('molecular_establishment','EST-MOL-1',P,dict(r=R)),
 ('carrier_establishment','EST-CARRIER-1',P,dict(r=R)),
]
for i,(name,cid,exp,args) in enumerate(baseclaims,1):expect(i,name,cid,exp,ev,args)

# RE gates one at a time. Benchmark excludes seed/provenance/preloading, endogenous requires them.
for i,leaf in enumerate(['G_seed','G_F','G_support_endo','G_no_preloaded_solution_RE','G_coop_complete','G_C_RE','G_R_RE','G_H_RE','G_Arep'],16):
    _,e,o=baseline(); rr=o[0]; args=[rr,B0] if leaf in {'G_F','G_support_endo','G_no_preloaded_solution_RE'} else [rr]; set_leaf(e,leaf,args,EvidenceValue.FAIL)
    expect(i,f'endogenous_RE_requires_{leaf}','RE-ENDO-1',EvidenceValue.FAIL,e,dict(r=R,B0=B0))
# seed failure does not erase benchmark RE.
_,e,o=baseline();set_leaf(e,'G_seed',[o[0]],EvidenceValue.FAIL);expect(25,'seed_not_required_for_benchmark_RE','RE-BENCH-1',EvidenceValue.PASS,e,dict(r=R))
# external/preloaded support can still benchmark.
_,e,o=baseline();set_leaf(e,'G_no_preloaded_solution_RE',[o[0],B0],EvidenceValue.FAIL);expect(26,'preloading_blocks_endogenous','RE-ENDO-1',EvidenceValue.FAIL,e,dict(r=R,B0=B0));expect(27,'preloading_does_not_erase_benchmark','RE-BENCH-1',EvidenceValue.PASS,e,dict(r=R))

# PCS one-factor guards.
for i,leaf in enumerate(['G_P','G_C_PCS','G_R_PCS','G_H_PCS','G_V','G_S'],28):
    _,e,o=baseline(); set_leaf(e,leaf,[o[1]],EvidenceValue.FAIL);expect(i,f'PCS_requires_{leaf}','PCS-LOCAL-1',EvidenceValue.FAIL,e,dict(r=R))
_,e,o=baseline();set_leaf(e,'G_L',[o[1]],EvidenceValue.FAIL);expect(34,'linked_mechanistic_mediation_stronger_than_local_PCS','PCS-LOCAL-1',EvidenceValue.PASS,e,dict(r=R));expect(35,'linked_PCS_requires_G_L','PCS-LINKED-1',EvidenceValue.FAIL,e,dict(r=R))

# RE->PCS continuity: absence/mismatch handling.
_,e,o=baseline();set_rel(e,'DescendsCore',[o[0],o[1]],EvidenceValue.FAIL);expect(36,'core_ancestry_failure_blocks_continuity','RE-PCS-CONT-1',EvidenceValue.FAIL,e,dict(r=R,B0=B0))
_,e,o=baseline();e['relation_receipts'].pop(('DescendsCore',(o[0],o[1])),None);expect(37,'unknown_core_ancestry_is_NA','RE-PCS-CONT-1',EvidenceValue.NA,e,dict(r=R,B0=B0))
_,e,o=baseline();set_leaf(e,'NoXFullLengthReplacement',[o[0],o[1]],EvidenceValue.FAIL);expect(38,'full_length_external_replacement_blocks_continuity','RE-PCS-CONT-1',EvidenceValue.FAIL,e,dict(r=R,B0=B0))
_,e,o=baseline();set_leaf(e,'CoreTimeOrder',[o[0],o[1]],EvidenceValue.FAIL);expect(39,'backwards_time_order_blocks_continuity','RE-PCS-CONT-1',EvidenceValue.FAIL,e,dict(r=R,B0=B0))

# Interface and bridge.
for i,leaf in enumerate(['G_I1','G_I2','G_I3','G_I4'],40):
    _,e,o=baseline();set_leaf(e,leaf,[o[2]],EvidenceValue.FAIL);expect(i,f'Interface_requires_{leaf}','INTERFACE-1',EvidenceValue.FAIL,e,dict(r=R))
for i,leaf in enumerate(['G_transfer','G_complete','G_target_establish','G_handoff_multivariate','G_temporal_overlap','G_currency_native_effect','G_currency_depletion_control','G_currency_restoration_control'],44):
    _,e,o=baseline();set_leaf(e,leaf,[o[3]],EvidenceValue.FAIL);expect(i,f'bridge_requires_{leaf}','BRIDGE-1',EvidenceValue.FAIL,e,dict(r=R))
# Missing temporal threshold -> NA, not false.
_,e,o=baseline();e['threshold_receipts'].pop('time_horizon');expect(52,'handoff_unresolved_threshold_NA','HANDOFF-1',EvidenceValue.NA,e,dict(w_H=o[3]))

# Programme proof must be continuous and structurally one route.
_,e,o=baseline();set_leaf(e,'ProgrammeContinuity',[o[8]],EvidenceValue.FAIL);expect(53,'programme_continuity_required','PROGRAMME-CURRENT-1',EvidenceValue.FAIL,e,dict(r=R))
# Missing programme continuity evidence -> NA.
_,e,o=baseline();del_leaf(e,'ProgrammeContinuity',[o[8]]);expect(54,'programme_missing_continuity_NA','PROGRAMME-CURRENT-1',EvidenceValue.NA,e,dict(r=R))

# Lab closure leaf receipts: no missing-as-PASS.
for i,leaf in enumerate(['G_route_path_lab','G_sourcing','G_forcing_scope','G_energy_closure_lab','G_compatibility','G_phys','G_declared_causal_coverage'],55):
    _,e,o=baseline();set_leaf(e,leaf,[o[5]],EvidenceValue.FAIL);expect(i,f'lab_closure_requires_{leaf}','LAB-CLOSURE-1',EvidenceValue.FAIL,e,dict(r=R,B0=B0))
for i,leaf in enumerate(['G_sourcing','G_forcing_scope','G_energy_closure_lab','G_declared_causal_coverage'],62):
    _,e,o=baseline();del_leaf(e,leaf,[o[5]]);expect(i,f'missing_{leaf}_is_NA_not_PASS','LAB-CLOSURE-1',EvidenceValue.NA,e,dict(r=R,B0=B0))

# Natural boundary + operations + energy + forcing + adaptive policy.
for i,leaf in enumerate(['G_boundary_realization','G_sourcing_natural','G_natural_ops_joint','G_natural_reach','G_energy_closure_natural','NaturalForcingLawAdmissible','AdaptivePolicyMappedOrIrrelevant'],66):
    _,e,o=baseline();args=[o[6],B0,NB0] if leaf=='G_boundary_realization' else [o[7]];set_leaf(e,leaf,args,EvidenceValue.FAIL);expect(i,f'natural_reach_requires_{leaf}','NAT-REACH-1',EvidenceValue.FAIL,e,dict(r=R,B0=B0))
_,e,o=baseline();set_leaf(e,'G_natural_plaus',[o[7]],EvidenceValue.FAIL);expect(73,'natural_reachable_can_pass_when_plausibility_fails','NAT-REACH-1',EvidenceValue.PASS,e,dict(r=R,B0=B0));expect(74,'natural_plausibility_is_stronger','NAT-PLAUS-1',EvidenceValue.FAIL,e,dict(r=R,B0=B0))
# Natural boundary evidence missing -> NA.
_,e,o=baseline();del_leaf(e,'G_boundary_realization',[o[6],B0,NB0]);expect(75,'missing_natural_boundary_realization_is_NA','NAT-REACH-1',EvidenceValue.NA,e,dict(r=R,B0=B0))

# Carrier/individuation/establishment.
_,e,o=baseline();set_leaf(e,'CarrierCompatible',[o[4]],EvidenceValue.FAIL);expect(76,'carrier_compatibility_required','CARRIER-1',EvidenceValue.FAIL,e,dict(r=R));expect(77,'carrier_establishment_requires_carrier_compatibility','EST-CARRIER-1',EvidenceValue.FAIL,e,dict(r=R))
_,e,o=baseline();set_leaf(e,'CarrierBoundedReproduction',[o[4]],EvidenceValue.FAIL);expect(78,'bounded_reproduction_required_only_for_individuation','CARRIER-1',EvidenceValue.PASS,e,dict(r=R));expect(79,'individuation_requires_bounded_reproduction','INDIVIDUATED-1',EvidenceValue.FAIL,e,dict(r=R))
_,e,o=baseline();set_leaf(e,'P_est_mol_positive',[o[1]],EvidenceValue.FAIL);expect(80,'PCS_does_not_imply_establishment','PCS-LOCAL-1',EvidenceValue.PASS,e,dict(r=R));expect(81,'molecular_establishment_requires_positive_probability','EST-MOL-1',EvidenceValue.FAIL,e,dict(r=R))
_,e,o=baseline();set_leaf(e,'P_est_carrier_positive',[o[4]],EvidenceValue.FAIL);expect(82,'carrier_capability_does_not_imply_carrier_establishment','CARRIER-1',EvidenceValue.PASS,e,dict(r=R));expect(83,'carrier_establishment_requires_positive_probability','EST-CARRIER-1',EvidenceValue.FAIL,e,dict(r=R))
_,e,o=baseline();set_leaf(e,'EmbeddedMolecularLineagePersists',[o[4]],EvidenceValue.FAIL);expect(84,'carrier_establishment_requires_embedded_molecular_persistence','EST-CARRIER-1',EvidenceValue.FAIL,e,dict(r=R))

# Structural route/boundary mismatch uses AST fields, not caller booleans.
re,pcs,iw,hw,car,rp,br,np,prog=base_objects(); pcs2=replace(pcs,route_spec_digest='other-route'); rp2=replace(rp,pcs_witness=pcs2); w2=complete_world(r,pcs=[pcs2],routeproofs=[rp2],descends={(re,pcs2)});e2=evidence_env_from_world(r,w2);expect(85,'cross_route_structural_mismatch_blocks_lab_closure','LAB-CLOSURE-1',EvidenceValue.FAIL,e2,dict(r=R,B0=B0))
re2=replace(re,boundary_spec_digest='other-boundary');rp2=replace(rp,re_witness=re2);w2=complete_world(r,res=[re2],routeproofs=[rp2],descends={(re2,pcs)});e2=evidence_env_from_world(r,w2);expect(86,'cross_boundary_structural_mismatch_blocks_lab_closure','LAB-CLOSURE-1',EvidenceValue.FAIL,e2,dict(r=R,B0=B0))

# Natural proof structural mismatch.
np2=replace(np,route_spec_digest='other-route');w2=complete_world(r,naturals=[np2]);e2=evidence_env_from_world(r,w2);expect(87,'natural_proof_route_mismatch_blocks_natural_closure','NAT-REACH-1',EvidenceValue.FAIL,e2,dict(r=R,B0=B0))

# Certificate binding and valid failure.
_,e,o=baseline();cr=eval_evidence_claim('LAB-CLOSURE-1',e,r=R,B0=B0);bundle=build_evidence_bundle(cr,cr.physical_witness_ref,e['evidence_receipts'].keys(),bundle_id='bundle-1');cert=fixture_certificate(cr,bundle,e);rec('088_synthetic_lab_claim_gets_VALID_TEST_certificate',cert.certificate_status is CertificateStatus.VALID and cert.claim_result is EvidenceValue.PASS)
_,e,o=baseline();set_leaf(e,'G_phys',[o[5]],EvidenceValue.FAIL);cr=eval_evidence_claim('LAB-CLOSURE-1',e,r=R,B0=B0);bundle=build_evidence_bundle(cr,cr.physical_witness_ref,e['evidence_receipts'].keys(),bundle_id='bundle-2');cert=fixture_certificate(cr,bundle,e);rec('089_failed_lab_claim_can_get_VALID_failure_certificate',cert.certificate_status is CertificateStatus.VALID and cert.claim_result is EvidenceValue.FAIL)
_,e,o=baseline();del_leaf(e,'G_phys',[o[5]]);cr=eval_evidence_claim('LAB-CLOSURE-1',e,r=R,B0=B0);bundle=build_evidence_bundle(cr,cr.physical_witness_ref,e['evidence_receipts'].keys(),bundle_id='bundle-3');cert=fixture_certificate(cr,bundle,e);rec('090_unresolved_lab_claim_gets_INCOMPLETE_certificate',cert.certificate_status is CertificateStatus.INCOMPLETE and cert.claim_result is EvidenceValue.NA)

# Final end-to-end complete-evidence collapse on key closure tiers.
for i,(cid,args) in enumerate([('LAB-CLOSURE-1',dict(r=R,B0=B0)),('NAT-REACH-1',dict(r=R,B0=B0)),('NAT-PLAUS-1',dict(r=R,B0=B0)),('EST-MOL-1',dict(r=R)),('EST-CARRIER-1',dict(r=R))],91):
    ww,ee,_=baseline(); b=eval_world_claim(cid,ww,**args); er=eval_evidence_claim(cid,ee,**args).result; rec(f'{i:03d}_end_to_end_boolean_collapse_{cid}',(b and er is EvidenceValue.PASS) or ((not b) and er is EvidenceValue.FAIL),{'world':b,'evidence':er.value})

passed=sum(v['pass'] for v in results.values());total=len(results)
OUT.write_text(json.dumps({'suite':'kernel_end_to_end_v2.7.7','passed':passed,'total':total,'all_pass':passed==total,'composition_engine':'claim_registry_runtime_v2_7_7.py only','tests':results},indent=2))
print(json.dumps({'passed':passed,'total':total,'all_pass':passed==total},indent=2))
if passed!=total:
    for k,v in results.items():
        if not v['pass']:print('FAIL',k,v)
    raise SystemExit(1)
