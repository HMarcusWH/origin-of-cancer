from __future__ import annotations
from dataclasses import dataclass
from typing import Any, Iterable
from evidence_receipts_v2_7_7 import *
from threshold_contracts_v2_7_7 import ThresholdReceipt

ROUTE_DIGEST='route-digest-r'; BOUNDARY_DIGEST='boundary-digest-b0'; NAT_BOUNDARY_DIGEST='natural-boundary-digest'; ROUTE_ID='r'

@dataclass(frozen=True)
class Route:
    route_id:str=ROUTE_ID; route_spec_digest:str=ROUTE_DIGEST
@dataclass(frozen=True)
class Boundary:
    boundary_id:str='B0'; route_spec_digest:str=ROUTE_DIGEST; boundary_spec_digest:str=BOUNDARY_DIGEST
@dataclass(frozen=True)
class NaturalBoundary:
    boundary_id:str='NB0'; route_spec_digest:str=ROUTE_DIGEST; boundary_spec_digest:str=NAT_BOUNDARY_DIGEST
@dataclass(frozen=True)
class REW:
    witness_id:str='re'; route_id:str=ROUTE_ID; route_spec_digest:str=ROUTE_DIGEST; boundary_spec_digest:str=BOUNDARY_DIGEST; run_or_block_id:str='rb'; condition_id:str='c'; observation_epoch:str='t1'; hereditary_core_id:str='core'; ok:bool=True; preloaded:bool=False; provenance:str='endo'; coop:bool=True; t:int=1
@dataclass(frozen=True)
class PCSW:
    witness_id:str='pcs'; route_id:str=ROUTE_ID; route_spec_digest:str=ROUTE_DIGEST; boundary_spec_digest:str=BOUNDARY_DIGEST; run_or_block_id:str='rb'; condition_id:str='c'; observation_epoch:str='t2'; physical_lineage_id:str='L'; hereditary_core_id:str='core2'; ok:bool=True; est:bool=True; linked:bool=True; t:int=2
@dataclass(frozen=True)
class IW:
    witness_id:str='i'; route_id:str=ROUTE_ID; route_spec_digest:str=ROUTE_DIGEST; boundary_spec_digest:str=BOUNDARY_DIGEST; run_or_block_id:str='rb'; condition_id:str='c'; observation_epoch:str='t0'; ok:bool=True
@dataclass(frozen=True)
class HW:
    witness_id:str='h'; route_id:str=ROUTE_ID; route_spec_digest:str=ROUTE_DIGEST; boundary_spec_digest:str=BOUNDARY_DIGEST; run_or_block_id:str='rb'; condition_id:str='c'; observation_epoch:str='t1.5'; source_arena_id:str='A'; target_arena_id:str='B'; transferred_batch_id:str='batch'; ok:bool=True; temporal:bool=True
@dataclass(frozen=True)
class CW:
    witness_id:str='car'; route_id:str=ROUTE_ID; route_spec_digest:str=ROUTE_DIGEST; boundary_spec_digest:str=BOUNDARY_DIGEST; run_or_block_id:str='rb'; condition_id:str='c'; observation_epoch:str='t3'; carrier_lineage_id:str='CL'; compatible:bool=True; bounded:bool=True; no_replace:bool=True; est:bool=True; persists:bool=True
@dataclass(frozen=True)
class Prog:
    proof_id:str; route_id:str; route_spec_digest:str; boundary_spec_digest:str; interface_witness:IW; handoff_witness:HW; pcs_witness:PCSW; continuity:bool=True
@dataclass(frozen=True)
class RP:
    proof_id:str; route_id:str; route_spec_digest:str; boundary_spec_digest:str; re_witness:REW; pcs_witness:PCSW; routepath:bool=True; sourcing:bool=True; forcing:bool=True; energy:bool=True; compatibility:bool=True; phys:bool=True; coverage:bool=True
@dataclass(frozen=True)
class BRW:
    witness_id:str='br'; route_spec_digest:str=ROUTE_DIGEST; lab_boundary_spec_digest:str=BOUNDARY_DIGEST; natural_boundary_spec_digest:str=NAT_BOUNDARY_DIGEST; ok:bool=True
@dataclass(frozen=True)
class NP:
    proof_id:str; route_id:str; route_spec_digest:str; lab_proof:RP; natural_boundary:NaturalBoundary; boundary_realization_witness:BRW; natural_sourcing:bool=True; ops:bool=True; reach:bool=True; energy:bool=True; forcing:bool=True; adaptive:bool=True; plausible:bool=True

B0=Boundary(); R=Route(); NB0=NaturalBoundary()

def base_objects():
    re=REW(); pcs=PCSW(); iw=IW(); hw=HW(); car=CW(); rp=RP('rp',ROUTE_ID,ROUTE_DIGEST,BOUNDARY_DIGEST,re,pcs); br=BRW(); np=NP('np',ROUTE_ID,ROUTE_DIGEST,rp,NB0,br); prog=Prog('prog',ROUTE_ID,ROUTE_DIGEST,BOUNDARY_DIGEST,iw,hw,pcs)
    return re,pcs,iw,hw,car,rp,br,np,prog

def predicate_truth(name,args):
    a=args[0] if args else None
    if name in {'G_seed','G_C_RE','G_R_RE','G_H_RE','G_Arep'}: return a.ok
    if name=='G_F': return a.ok
    if name=='G_support_endo': return a.ok and a.provenance=='endo'
    if name=='G_no_preloaded_solution_RE': return not a.preloaded
    if name=='G_coop_complete': return a.coop
    if name in {'G_P','G_C_PCS','G_R_PCS','G_H_PCS','G_V','G_S'}: return a.ok
    if name=='G_L': return a.ok and a.linked
    if name=='NoXFullLengthReplacement': return args[0].provenance=='endo'
    if name=='CoreTimeOrder': return args[0].t < args[1].t
    if name in {'G_I1','G_I2','G_I3','G_I4'}: return a.ok
    if name in {'G_transfer','G_complete','G_target_establish','G_handoff_multivariate'}: return a.ok
    if name=='G_temporal_overlap': return a.temporal
    if name in {'G_currency_native_effect','G_currency_depletion_control','G_currency_restoration_control'}: return a.ok
    if name=='ProgrammeContinuity': return a.continuity
    if name=='G_route_path_lab': return a.routepath
    if name=='G_sourcing': return a.sourcing
    if name=='G_forcing_scope': return a.forcing
    if name=='G_energy_closure_lab': return a.energy
    if name=='G_compatibility': return a.compatibility
    if name=='G_phys': return a.phys
    if name=='G_declared_causal_coverage': return a.coverage
    if name=='G_boundary_realization': return args[0].ok and args[0].lab_boundary_spec_digest==args[1].boundary_spec_digest and args[0].natural_boundary_spec_digest==args[2].boundary_spec_digest
    if name=='G_sourcing_natural': return a.natural_sourcing
    if name=='G_natural_ops_joint': return a.ops
    if name=='G_natural_reach': return a.reach
    if name=='G_energy_closure_natural': return a.energy
    if name=='NaturalForcingLawAdmissible': return a.forcing
    if name=='AdaptivePolicyMappedOrIrrelevant': return a.adaptive
    if name=='G_natural_plaus': return a.plausible
    if name=='CarrierCompatible': return a.compatible
    if name=='CarrierBoundedReproduction': return a.bounded
    if name=='CarrierNoInvestigatorReplacement': return a.no_replace
    if name=='P_est_mol_positive': return a.est
    if name=='P_est_carrier_positive': return a.est
    if name=='EmbeddedMolecularLineagePersists': return a.persists
    raise KeyError(name)

def complete_world(registry, res=None, pcs=None, interfaces=None, handoffs=None, carriers=None, routeproofs=None, naturals=None, programmes=None, descends=None, carrier_links=None):
    re0,pcs0,iw0,hw0,car0,rp0,br0,np0,prog0=base_objects()
    res=list(res if res is not None else [re0]); pcs=list(pcs if pcs is not None else [pcs0]); interfaces=list(interfaces if interfaces is not None else [iw0]); handoffs=list(handoffs if handoffs is not None else [hw0]); carriers=list(carriers if carriers is not None else [car0]); routeproofs=list(routeproofs if routeproofs is not None else [rp0]); naturals=list(naturals if naturals is not None else [np0]); programmes=list(programmes if programmes is not None else [prog0])
    domains={'REWitness':res,'PCSWitness':pcs,'InterfaceWitness':interfaces,'HandoffWitness':handoffs,'CarrierWitness':carriers,'RouteProof':routeproofs,'NaturalProof':naturals,'ProgrammeProof':programmes,'EvidenceBundle':[],'Operation':[],'NaturalOperation':[],'BoundaryRealizationWitness':[],'NaturalBoundary':[],'RouteId':[],'Boundary':[],'ForcingLaw':[],'Threshold':[]}
    predicates={}
    for name,spec in registry['leaf_predicates'].items():
        table={}
        # enumerate Cartesian product only from domains where possible; unary/binary actual claim tuples are populated from known objects below.
        predicates[name]=table
    # Populate leaf tables for objects that can occur in claims.
    objs=res+pcs+interfaces+handoffs+carriers+routeproofs+naturals+programmes
    import itertools
    for name,spec in registry['leaf_predicates'].items():
        argtypes=spec['args']
        pools=[]
        for typ in argtypes:
            if typ=='Boundary': pools.append([B0])
            elif typ=='NaturalBoundary': pools.append([n.natural_boundary for n in naturals])
            elif typ=='BoundaryRealizationWitness': pools.append([n.boundary_realization_witness for n in naturals])
            else: pools.append(domains.get(typ,[]))
        for args in itertools.product(*pools):
            try: predicates[name][tuple(args)]=bool(predicate_truth(name,args))
            except KeyError: pass
    relations={name:set() for name in registry['relations']}
    relations['DescendsCore']=set(descends if descends is not None else {(r,p) for r in res for p in pcs if r.hereditary_core_id and p.hereditary_core_id and r.route_spec_digest==p.route_spec_digest})
    relations['PCSToCarrier']=set(carrier_links if carrier_links is not None else {(p,c) for p in pcs for c in carriers if p.route_spec_digest==c.route_spec_digest})
    return {'domains':domains,'domain_completeness':{k:True for k in domains},'predicates':predicates,'relations':relations}

def evidence_env_from_world(registry, world, completeness:DomainCompleteness=DomainCompleteness.COMPLETE, missing_leaf=None, relation_overrides=None, threshold_overrides=None):
    # Explicit synthetic byte content and witness binding. These are not lab data.
    import json
    payload=json.dumps({'fixture':'complete_world','predicates':{n:[(stable_digest(args),bool(v)) for args,v in table.items()] for n,table in world['predicates'].items()}},sort_keys=True).encode()
    blobs={bytes_ref(payload):payload}
    refs=set()
    for values in world['domains'].values():refs.update(object_refs(values))
    env={'domains':{},'evidence_receipts':{},'raw_objects':blobs,'leaf_receipts':{},'relation_receipts':{},'threshold_receipts':{}}
    env['evidence_receipts']['ev']=build_raw_evidence('ev',refs or ('empty-fixture',),blobs,assay_id='SYNTHETIC-TRUTH-TABLE',observation_window='NOT-AN-EXPERIMENT',origin='SYNTHETIC')
    for typ,vals in world['domains'].items():env['domains'][typ]=DomainReceipt(typ,tuple(vals),completeness,'synthetic-exhaustive-world','ev')
    for name,table in world['predicates'].items():
        for args,v in table.items():
            if missing_leaf and name==missing_leaf: continue
            env['leaf_receipts'][(name,args)]=build_leaf_receipt(name,args,EvidenceValue.PASS if v else EvidenceValue.FAIL,['ev'],f'eval:{name}','2.7.7',evidence_env=env)
    import itertools
    for name,relset in world['relations'].items():
        spec=registry['relations'][name]; pools=[world['domains'].get(t,[]) for t in spec['args']]
        for args in itertools.product(*pools):
            if args in relset:
                value=EvidenceValue.PASS
            elif completeness is DomainCompleteness.COMPLETE:
                value=EvidenceValue.FAIL
            else:
                continue
            env['relation_receipts'][(name,args)]=build_relation_receipt(name,args,value,['ev'],f'evalrel:{name}','2.7.7',reason_code='complete_relation_evaluation',evidence_env=env)
    if relation_overrides:
        env['relation_receipts'].update(relation_overrides)
    env['threshold_receipts']={cid:fixture_threshold(cid,value) for cid,value in [('reachability_probability',1e-6),('plausibility_probability_floor',.01),('experimental_probability_floor',.01),('time_horizon',3.0)]}
    if threshold_overrides: env['threshold_receipts'].update(threshold_overrides)
    return env


def fixture_threshold(cid,value,d_max=None):
    """Synthetic frozen threshold. No real preregistration is asserted."""
    metric='elapsed_time' if cid=='time_horizon' else ('euclidean_distance' if 'distance' in cid else 'probability')
    units='s' if cid=='time_horizon' else '1'
    return ThresholdReceipt(cid,value,True,True,metric,units,d_max,'test-threshold:'+cid,'a'*64,'2026-09-01T00:00:00Z','2026-09-02T00:00:00Z','synthetic fixture only','explicit test resolution, not a laboratory qualification')

def fixture_trust(ev):
    """Ephemeral test-only Ed25519 key. Never stored or shipped as an authority key."""
    from certificate_authority_v2_7_7 import VerifierPolicy,EvaluatorRegistration,sign_reviewed_object,Ed25519PrivateKey
    import claim_registry_runtime_v2_7_7 as rt
    from cryptography.hazmat.primitives import serialization
    key=Ed25519PrivateKey.generate();pub=key.public_key().public_bytes(serialization.Encoding.Raw,serialization.PublicFormat.Raw)
    code=stable_digest('SYNTHETIC-TEST-EVALUATOR');qualification='NOT-LAB-QUALIFIED-SYNTHETIC-ONLY'
    regs=[];att=[]
    for tab,kind in [('leaf_receipts','LEAF'),('relation_receipts','RELATION'),('domains','DOMAIN'),('threshold_receipts','THRESHOLD'),('evidence_receipts','RAW')]:
        for obj in ev.get(tab,{}).values():
            if kind in ('LEAF','RELATION'):
                symbol=obj.predicate_id if kind=='LEAF' else obj.relation_id
                regs.append(EvaluatorRegistration(obj.evaluator_id,obj.evaluator_version,code,(symbol,),qualification))
            att.append(sign_reviewed_object(obj,kind,'SYNTHETIC-TEST-ISSUER',key,signed_at='2026-09-25T00:00:00Z',evaluator_code_digest=code,qualification_ref=qualification))
    policy=VerifierPolicy('SYNTHETIC-TEST-POLICY',(rt.registry_hash(),),(rt.runtime_hash(),),(('SYNTHETIC-TEST-ISSUER',pub),),tuple(regs),('a'*64,),True,tuple(stable_digest(v) for v in ev.get('threshold_receipts',{}).values()))
    return policy,tuple(att)

def fixture_certificate(cr,bundle,ev):
    from claim_registry_runtime_v2_7_7 import issue_claim_certificate
    policy,att=fixture_trust(ev)
    return issue_claim_certificate(cr,bundle,ev,policy=policy,attestations=att)
