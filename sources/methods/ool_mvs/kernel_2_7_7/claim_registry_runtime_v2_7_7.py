"""Canonical OoL-MVS v2.7.7 claim registry compiler/runtime.

Two deliberately separate semantics are implemented:
1) FORMAL_COMPLETE_WORLD: ordinary two-valued physical truth over explicitly complete synthetic worlds.
2) EXPERIMENTAL_EVIDENCE: strong-Kleene PASS/FAIL/NA over evidence-derived leaf/relation receipts.

Certification is a meta-layer and is not permitted to feed physical claim truth.
"""
from __future__ import annotations
import json, hashlib
from pathlib import Path
from typing import Any, Dict, Iterable, Tuple, Set
from dataclasses import replace, is_dataclass, fields
from evidence_receipts_v2_7_7 import (
    EvidenceValue, CertificateStatus, DomainCompleteness, DomainReceipt, EvidenceReceipt,
    LeafEvaluationReceipt, RelationEvaluationReceipt, EvidenceBundleReceipt, ClaimResult, ClaimCertificate, stable_digest,
)
from threshold_contracts_v2_7_7 import ThresholdReceipt, validate_required_thresholds
from evidence_receipts_v2_7_7 import (verify_evaluation_receipt, evidence_state_digest, evaluation_payload, evidence_closure, object_refs, bytes_ref)

HERE=Path(__file__).resolve().parent
REGISTRY_PATH=HERE/'claim_registry_v2_7_7.json'
OPS={'and','or','not','pred','rel','exists','forall','claim_ref','eq'}
EXACT_TRUTH_VALUES=['PASS','FAIL','NA']
EXACT_WORLD_TRUTH_VALUES=['TRUE','FALSE']
EXACT_RUNTIME_MODES=['FORMAL_COMPLETE_WORLD','EXPERIMENTAL_EVIDENCE','TEST_FIXTURE_UNSAFE']
ALLOWED_THRESHOLD_DOMAINS={'(0,1]','(0,inf)','[0,d_max)','finite','[0,inf)'}
ALLOWED_RELATION_OWNERS={'structural','provenance','assay','model','natural_mapping','experimental_equivalence'}

class RegistryError(ValueError): pass
class IncompleteWorldError(ValueError): pass

def _operator(expr:dict)->str:
    if not isinstance(expr,dict): raise RegistryError('AST_node_not_object')
    ops=set(expr)&OPS
    if len(ops)!=1: raise RegistryError(f'AST_node_must_have_exactly_one_operator:{sorted(ops)}')
    return next(iter(ops))


def load_registry(path: Path=REGISTRY_PATH)->dict:
    return json.loads(path.read_text(encoding='utf-8'))

def registry_hash(registry:dict|None=None)->str:
    r=registry or load_registry()
    return hashlib.sha256(json.dumps(r,sort_keys=True,separators=(',',':')).encode()).hexdigest()

def _get(obj:Any, key:str)->Any:
    if isinstance(obj,dict):
        if key not in obj: raise KeyError(key)
        return obj[key]
    return getattr(obj,key)

def _field_value(root:Any,path:list[str])->Any:
    cur=root
    for p in path: cur=_get(cur,p)
    return cur

def _value(x:Any,env:dict)->Any:
    if isinstance(x,str):
        if x not in env: raise RegistryError(f'unbound_variable:{x}')
        return env[x]
    if isinstance(x,dict) and set(x)=={'field'}:
        root,*path=x['field']
        if root not in env: raise RegistryError(f'unbound_field_root:{root}')
        return _field_value(env[root],path)
    if isinstance(x,dict) and set(x)=={'literal'}: return x['literal']
    raise RegistryError(f'invalid_AST_argument:{x!r}')

def _route_key(obj:Any)->Any:
    return _get(obj,'route_spec_digest')

def _domain_complete(world:dict,typ:str)->bool:
    comp=world.get('domain_completeness',{}).get(typ)
    return comp is True or comp=='COMPLETE'

def _domain_world(world:dict,registry:dict,typ:str,domain_spec:str|None,env:dict)->list:
    if typ not in world.get('domains',{}):
        raise IncompleteWorldError(f'missing_domain:{typ}')
    vals=list(world['domains'][typ])
    if not _domain_complete(world,typ):
        raise IncompleteWorldError(f'formal_world_domain_not_complete:{typ}')
    if not domain_spec: return vals
    prefix,param=domain_spec.split(':',1)
    spec=registry.get('domain_constructors',{}).get(prefix)
    if not spec: raise RegistryError(f'unknown_domain_constructor:{prefix}')
    if param not in env: raise RegistryError(f'unbound_domain_parameter:{param}')
    target=_field_value(env[param],[spec['parameter_field']])
    return [v for v in vals if _field_value(v,[spec['member_field']])==target]

def validate_typed_value(value:Any,typ:str,registry:dict)->bool:
    """Structural schema validation, retaining the original typed-witness interface."""
    if typ in ('String','Digest','Timestamp','RunBlockId','ConditionId'):
        return type(value) is str and bool(value.strip())
    spec=registry.get('types',{}).get(typ)
    if spec is None:return False
    for name,ft in spec.get('fields',{}).items():
        try:val=_get(value,name)
        except (KeyError,AttributeError):return False
        if not validate_typed_value(val,ft,registry):return False
    try:stable_digest(value)
    except (ValueError,TypeError):return False
    return True

def _domain_evidence(ev:dict,registry:dict,typ:str,domain_spec:str|None,env:dict)->DomainReceipt:
    dr=ev.get('domains',{}).get(typ)
    bad=lambda why:DomainReceipt(typ,(),DomainCompleteness.UNKNOWN,why)
    if dr is None:return bad('missing_domain')
    if not isinstance(dr,DomainReceipt):raise TypeError('typed_domain_receipt_required')
    if dr.type_id!=typ:return bad('domain_type_mismatch')
    if type(dr.completeness) is not DomainCompleteness:return bad('typed_domain_completeness_required')
    if type(dr.values) is not tuple:return bad('domain_values_must_be_tuple')
    if dr.completeness is DomainCompleteness.COMPLETE and not dr.enumeration_method:return bad('complete_domain_requires_enumeration_method')
    if typ in registry.get('types',{}) and any(not validate_typed_value(v,typ,registry) for v in dr.values):return bad('invalid_domain_member_type')
    vals=list(dr.values)
    if domain_spec:
        prefix,param=domain_spec.split(':',1)
        spec=registry.get('domain_constructors',{}).get(prefix)
        if not spec:raise RegistryError('unknown_domain_constructor:'+prefix)
        if param not in env:raise RegistryError('unbound_domain_parameter:'+param)
        try:
            target=_field_value(env[param],[spec['parameter_field']])
            if dr.scope_route_digest and dr.scope_route_digest!=target:return bad('domain_scope_mismatch')
            vals=[v for v in vals if _field_value(v,[spec['member_field']])==target]
        except (AttributeError,KeyError):return bad('invalid_domain_member_fields')
    elif dr.scope_route_digest:
        return bad('restricted_domain_cannot_establish_global_completeness')
    return DomainReceipt(typ,tuple(vals),dr.completeness,dr.enumeration_method,dr.evidence_ref,dr.scope_route_digest)

# ---------- strong-Kleene evidence algebra ----------
def k_not(x:EvidenceValue)->EvidenceValue:
    if type(x) is not EvidenceValue:raise TypeError('typed_evidence_value_required')
    return {EvidenceValue.PASS:EvidenceValue.FAIL,EvidenceValue.FAIL:EvidenceValue.PASS,EvidenceValue.NA:EvidenceValue.NA}[x]
def k_and(xs:Iterable[EvidenceValue])->EvidenceValue:
    xs=list(xs)
    if any(type(x) is not EvidenceValue for x in xs):raise TypeError('typed_evidence_value_required')
    if any(x is EvidenceValue.FAIL for x in xs): return EvidenceValue.FAIL
    if all(x is EvidenceValue.PASS for x in xs): return EvidenceValue.PASS
    return EvidenceValue.NA
def k_or(xs:Iterable[EvidenceValue])->EvidenceValue:
    xs=list(xs)
    if any(type(x) is not EvidenceValue for x in xs):raise TypeError('typed_evidence_value_required')
    if any(x is EvidenceValue.PASS for x in xs): return EvidenceValue.PASS
    if all(x is EvidenceValue.FAIL for x in xs): return EvidenceValue.FAIL
    return EvidenceValue.NA

# ---------- two-valued complete-world evaluator ----------
def eval_world_expr(expr:dict,registry:dict,world:dict,env:dict)->bool:
    op=_operator(expr)
    if op=='and': return all(eval_world_expr(e,registry,world,env) for e in expr['and'])
    if op=='or': return any(eval_world_expr(e,registry,world,env) for e in expr['or'])
    if op=='not': return not eval_world_expr(expr['not'],registry,world,env)
    if op=='eq':
        a,b=expr['eq']; return _value(a,env)==_value(b,env)
    if op=='pred':
        name=expr['pred']; args=tuple(_value(a,env) for a in expr.get('args',[]))
        if name not in world.get('predicates',{}): raise IncompleteWorldError(f'missing_predicate_table:{name}')
        table=world['predicates'][name]
        if callable(table):
            v=table(*args)
            if type(v) is not bool:raise TypeError('formal_world_callable_not_bool:'+name)
            return v
        if args not in table: raise IncompleteWorldError(f'missing_predicate_value:{name}{args}')
        v=table[args]
        if type(v) is not bool: raise TypeError(f'formal_world_predicate_not_bool:{name}{args}:{v!r}')
        return v
    if op=='rel':
        name=expr['rel']; args=tuple(_value(a,env) for a in expr.get('args',[]))
        if name not in world.get('relations',{}): raise IncompleteWorldError(f'missing_relation:{name}')
        rel=world['relations'][name]
        # Complete-world relation is an explicitly complete set over its declared domain.
        return args in rel
    if op in ('exists','forall'):
        q=expr[op]; vals=_domain_world(world,registry,q['type'],q.get('domain'),env)
        answers=[]
        for v in vals:
            e2=dict(env);e2[q['var']]=v
            answers.append(eval_world_expr(q['body'],registry,world,e2))
        return any(answers) if op=='exists' else all(answers)
    if op=='claim_ref':
        c=registry['claims'][expr['claim_ref']]
        vals=[_value(a,env) for a in expr.get('args',[])]
        e2={name:val for (name,_),val in zip(c.get('args',[]),vals)}
        return eval_world_expr(c['expr'],registry,world,e2)
    raise RegistryError(f'unsupported_operator:{op}')


_CANONICAL_CACHE: tuple[str,dict] | None = None
def _load_validated_canonical_registry()->dict:
    global _CANONICAL_CACHE
    r=load_registry(); h=registry_hash(r)
    if _CANONICAL_CACHE is not None and _CANONICAL_CACHE[0]==h:
        return _CANONICAL_CACHE[1]
    vr=validate_registry(r)
    if not vr['pass']: raise RegistryError('invalid_canonical_registry:'+','.join(vr['errors'][:5]))
    _CANONICAL_CACHE=(h,r)
    return r

def eval_world_claim(claim_id:str,world:dict,**kwargs)->bool:
    r=_load_validated_canonical_registry()
    c=r['claims'][claim_id]
    env={}
    for n,_t in c.get('args',[]):
        if n not in kwargs: raise ValueError(f'missing_claim_arg:{claim_id}:{n}')
        env[n]=kwargs[n]
    return eval_world_expr(c['expr'],r,world,env)

# ---------- experimental evidence evaluator ----------
def _threshold_gate(registry:dict,predicate_name:str,ev:dict)->tuple[bool,list[str]]:
    refs=registry['leaf_predicates'][predicate_name].get('threshold_contract_refs',[])
    if not refs: return True,[]
    return validate_required_thresholds(registry,refs,ev.get('threshold_receipts',{}))

def eval_evidence_expr(expr:dict,registry:dict,ev:dict,env:dict,trace:list[str],support:set[str])->EvidenceValue:
    op=_operator(expr)
    if op=='and': return k_and(eval_evidence_expr(e,registry,ev,env,trace,support) for e in expr['and'])
    if op=='or': return k_or(eval_evidence_expr(e,registry,ev,env,trace,support) for e in expr['or'])
    if op=='not': return k_not(eval_evidence_expr(expr['not'],registry,ev,env,trace,support))
    if op=='eq':
        try: return EvidenceValue.PASS if _value(expr['eq'][0],env)==_value(expr['eq'][1],env) else EvidenceValue.FAIL
        except (KeyError,AttributeError):
            trace.append('unresolved_structural_identity')
            return EvidenceValue.NA
    if op=='pred':
        name=expr['pred']; args=tuple(_value(a,env) for a in expr.get('args',[]))
        ok,errs=_threshold_gate(registry,name,ev)
        if not ok:
            trace.extend(errs); return EvidenceValue.NA
        for tc in registry['leaf_predicates'][name].get('threshold_contract_refs',[]):
            tr=ev.get('threshold_receipts',{}).get(tc)
            if tr is not None: support.add('threshold:'+stable_digest(tr))
        rec=ev.get('leaf_receipts',{}).get((name,args))
        if rec is None:
            trace.append(f'missing_leaf_receipt:{name}'); return EvidenceValue.NA
        if not isinstance(rec,LeafEvaluationReceipt):
            raise TypeError(f'leaf receipt for {name}{args} must be LeafEvaluationReceipt')
        if rec.authority_mode!='AUTHORIZED_EVALUATOR':
            trace.append(f'unauthorized_leaf_receipt:{name}'); return EvidenceValue.NA
        if rec.predicate_id!=name or rec.args!=args:
            trace.append(f'leaf_receipt_binding_mismatch:{name}'); return EvidenceValue.NA
        if not rec.evidence_receipt_refs:
            trace.append(f'leaf_receipt_without_evidence:{name}'); return EvidenceValue.NA
        ok,reason,raw,blobs=verify_evaluation_receipt(rec,'leaf',name,args,ev)
        for eid,er in raw.items():
            support.add('evidence:'+eid);support.add('rawreceipt:'+stable_digest(er))
        for bid in blobs:support.add('rawobject:'+bid)
        if not ok:trace.append('invalid_leaf:'+name+':'+reason);return EvidenceValue.NA
        support.add('leafreceipt:'+stable_digest(rec))
        if rec.result is EvidenceValue.FAIL:trace.append('failed_leaf:'+name)
        if rec.result is EvidenceValue.NA:trace.append('unresolved_leaf:'+name)
        return rec.result
    if op=='rel':
        name=expr['rel']; args=tuple(_value(a,env) for a in expr.get('args',[]))
        rec=ev.get('relation_receipts',{}).get((name,args))
        if rec is None:
            trace.append(f'missing_relation_receipt:{name}'); return EvidenceValue.NA
        if not isinstance(rec,RelationEvaluationReceipt):
            raise TypeError(f'relation receipt for {name}{args} must be RelationEvaluationReceipt')
        if rec.authority_mode!='AUTHORIZED_EVALUATOR' or rec.relation_id!=name or rec.args!=args:
            trace.append(f'relation_receipt_binding_mismatch:{name}'); return EvidenceValue.NA
        if not rec.evidence_receipt_refs:
            trace.append(f'relation_receipt_without_evidence:{name}'); return EvidenceValue.NA
        ok,reason,raw,blobs=verify_evaluation_receipt(rec,'relation',name,args,ev)
        for eid,er in raw.items():
            support.add('evidence:'+eid);support.add('rawreceipt:'+stable_digest(er))
        for bid in blobs:support.add('rawobject:'+bid)
        if not ok:trace.append('invalid_relation:'+name+':'+reason);return EvidenceValue.NA
        support.add('relationreceipt:'+stable_digest(rec))
        if rec.result is EvidenceValue.FAIL:trace.append('failed_relation:'+name)
        if rec.result is EvidenceValue.NA:trace.append('unresolved_relation:'+name)
        return rec.result
    if op in ('exists','forall'):
        q=expr[op]; dr=_domain_evidence(ev,registry,q['type'],q.get('domain'),env)
        support.add('domain:'+stable_digest(dr))
        source=ev.get('domains',{}).get(q['type'])
        if source is not None:support.add('domain_source:'+stable_digest(source))
        if dr.evidence_ref:
            try:
                raw,blobs=evidence_closure((dr.evidence_ref,),ev)
                for eid,er in raw.items():
                    support.add('evidence:'+eid);support.add('rawreceipt:'+stable_digest(er))
                for bid in blobs:support.add('rawobject:'+bid)
            except (ValueError,TypeError) as exc:
                trace.append('invalid_domain_evidence:'+str(exc));return EvidenceValue.NA
        vals=[]
        for v in dr.values:
            e2=dict(env);e2[q['var']]=v
            vals.append(eval_evidence_expr(q['body'],registry,ev,e2,trace,support))
        if op=='exists':
            if any(v is EvidenceValue.PASS for v in vals): return EvidenceValue.PASS
            if dr.completeness is DomainCompleteness.COMPLETE and all(v is EvidenceValue.FAIL for v in vals): return EvidenceValue.FAIL
            trace.append(f'incomplete_existential_domain:{q["type"]}')
            return EvidenceValue.NA
        else:
            if any(v is EvidenceValue.FAIL for v in vals): return EvidenceValue.FAIL
            if dr.completeness is DomainCompleteness.COMPLETE and all(v is EvidenceValue.PASS for v in vals): return EvidenceValue.PASS
            trace.append(f'incomplete_universal_domain:{q["type"]}')
            return EvidenceValue.NA
    if op=='claim_ref':
        c=registry['claims'][expr['claim_ref']]
        vals=[_value(a,env) for a in expr.get('args',[])]
        e2={name:val for (name,_),val in zip(c.get('args',[]),vals)}
        return eval_evidence_expr(c['expr'],registry,ev,e2,trace,support)
    raise RegistryError(f'unsupported_operator:{op}')

def runtime_hash()->str:
    paths=['claim_registry_runtime_v2_7_7.py','evidence_receipts_v2_7_7.py','threshold_contracts_v2_7_7.py','certificate_authority_v2_7_7.py']
    return stable_digest({n:hashlib.sha256((HERE/n).read_bytes()).hexdigest() for n in paths})

def eval_evidence_claim(claim_id:str,evidence_env:dict,**kwargs)->ClaimResult:
    r=_load_validated_canonical_registry()
    if claim_id not in r['claims']:raise RegistryError('unknown_claim:'+claim_id)
    c=r['claims'][claim_id];env={}
    expected={n for n,_ in c.get('args',[])}
    if set(kwargs)!=expected:raise ValueError('claim_arguments_must_match_registry:'+claim_id)
    for n,t in c.get('args',[]):
        if not validate_typed_value(kwargs[n],t,r):raise TypeError('invalid_claim_argument:'+n+':'+t)
        env[n]=kwargs[n]
    trace=[];support=set()
    value=eval_evidence_expr(c['expr'],r,evidence_env,env,trace,support)
    typed=tuple((n,t,env[n]) for n,t in c.get('args',[]))
    # Witness claims bind to the named witness. Existential claims bind to the
    # exact typed route/query scope, not an arbitrary candidate from that scope.
    scope='scope:'+stable_digest((claim_id,typed))
    if len(typed)==1:
        v=typed[0][2]
        for field in ('witness_id','proof_id'):
            try:scope=_get(v,field);break
            except (AttributeError,KeyError):pass
    cr=ClaimResult(claim_id,value,
        tuple(sorted(set(trace))) if value is EvidenceValue.NA else (),
        tuple(sorted(set(trace))) if value is EvidenceValue.FAIL else (),
        tuple(sorted(support)),registry_hash(r),'EXPERIMENTAL_EVIDENCE',typed,scope,
        evidence_state_digest(evidence_env),runtime_hash(),'')
    return replace(cr,evaluation_digest=stable_digest(evaluation_payload(cr)))

def issue_claim_certificate(claim_result:ClaimResult,evidence_bundle:EvidenceBundleReceipt,evidence_env:dict,*,policy=None,attestations=())->ClaimCertificate:
    """Replay first, then verify externally configured reviewer/evaluator authority.

    No default trust keys are shipped. VALID authenticates evidence binding, not
    the occurrence of an experiment or the truth of an interpretation.
    """
    from certificate_authority_v2_7_7 import verify_claim_certificate
    return verify_claim_certificate(claim_result,evidence_bundle,evidence_env,policy=policy,attestations=attestations)

# ---------- closed registry compiler / validator ----------
def validate_registry(registry:dict|None=None)->dict:
    r=registry or load_registry(); errors=[]; warnings=[]
    if r.get('registry_version')!='2.7.7': errors.append('registry_version_must_equal_2.7.7')
    if r.get('truth_values')!=EXACT_TRUTH_VALUES: errors.append('truth_lattice_integrity_failure')
    if r.get('world_truth_values')!=EXACT_WORLD_TRUTH_VALUES: errors.append('world_truth_lattice_integrity_failure')
    modes=r.get('evaluation_modes',{})
    if list(modes.keys())!=EXACT_RUNTIME_MODES: errors.append('runtime_mode_contract_integrity_failure')
    else:
        if modes['FORMAL_COMPLETE_WORLD'].get('semantics')!='two-valued' or modes['FORMAL_COMPLETE_WORLD'].get('missing_inputs')!='ERROR' or modes['FORMAL_COMPLETE_WORLD'].get('scientific_certificate') is not False: errors.append('formal_world_mode_semantics_failure')
        if modes['EXPERIMENTAL_EVIDENCE'].get('semantics')!='strong-kleene PASS/FAIL/NA' or modes['EXPERIMENTAL_EVIDENCE'].get('missing_inputs')!='NA' or modes['EXPERIMENTAL_EVIDENCE'].get('scientific_certificate') is not True: errors.append('experimental_evidence_mode_semantics_failure')
        if modes['TEST_FIXTURE_UNSAFE'].get('scientific_certificate') is not False: errors.append('unsafe_fixture_certificate_must_be_false')
    scopes=set(r.get('scopes',[])); claims=r.get('claims',{}); types=r.get('types',{}); leaves=r.get('leaf_predicates',{}); rels=r.get('relations',{})
    if not scopes: errors.append('declared_scopes_empty')
    # Threshold-contract schema integrity.
    contracts=r.get('threshold_contracts',{})
    for cid,spec in contracts.items():
        if not isinstance(spec,dict): errors.append(f'malformed_threshold_contract:{cid}'); continue
        if spec.get('domain') not in ALLOWED_THRESHOLD_DOMAINS:
            errors.append(f'invalid_threshold_contract_domain:{cid}:{spec.get("domain")}')
        if not isinstance(spec.get('extra',''),str) or not spec.get('extra','').strip():
            errors.append(f'threshold_contract_missing_semantic_note:{cid}')
    # Domain-constructor schema integrity.
    for dcid,dspec in r.get('domain_constructors',{}).items():
        if not isinstance(dspec,dict): errors.append(f'malformed_domain_constructor:{dcid}'); continue
        ptyp=dspec.get('parameter_type'); pf=dspec.get('parameter_field'); mf=dspec.get('member_field')
        if ptyp not in types: errors.append(f'domain_constructor_unknown_parameter_type:{dcid}:{ptyp}')
        elif pf not in types.get(ptyp,{}).get('fields',{}): errors.append(f'domain_constructor_unknown_parameter_field:{dcid}:{ptyp}.{pf}')
        if not isinstance(mf,str) or not mf: errors.append(f'domain_constructor_missing_member_field:{dcid}')
    # Type graph integrity.
    for t,spec in types.items():
        if not isinstance(spec,dict): errors.append(f'type_spec_not_object:{t}'); continue
        for f,ft in spec.get('fields',{}).items():
            if ft not in types: errors.append(f'unknown_field_type:{t}.{f}:{ft}')
    # Relation integrity.
    for rel,spec in rels.items():
        if not isinstance(spec,dict) or 'args' not in spec or 'owner' not in spec: errors.append(f'malformed_relation_spec:{rel}'); continue
        if spec.get('owner') not in ALLOWED_RELATION_OWNERS: errors.append(f'illegal_relation_owner:{rel}:{spec.get("owner")}')
        for typ in spec['args']:
            if typ not in types: errors.append(f'unknown_relation_arg_type:{rel}:{typ}')
    # Leaf integrity + threshold linkage.
    for p,spec in leaves.items():
        if not isinstance(spec,dict) or 'args' not in spec: errors.append(f'malformed_leaf_spec:{p}'); continue
        if spec.get('scope') not in scopes: errors.append(f'illegal_leaf_scope:{p}:{spec.get("scope")}')
        for typ in spec['args']:
            if typ not in types: errors.append(f'unknown_leaf_arg_type:{p}:{typ}')
        for cid in spec.get('threshold_contract_refs',[]):
            if cid not in contracts: errors.append(f'unknown_threshold_contract_ref:{p}:{cid}')
    # Claim symbols/IDs/scopes/args.
    syms=[c.get('symbol') for c in claims.values()]
    if len(syms)!=len(set(syms)): errors.append('duplicate_claim_symbols')
    dep={cid:set() for cid in claims}
    def field_type(arg,bound,where):
        if isinstance(arg,str):
            if arg not in bound: errors.append(f'{where}:free_variable:{arg}'); return None
            return bound[arg]
        if isinstance(arg,dict) and set(arg)=={'field'}:
            root,*path=arg['field']
            if root not in bound: errors.append(f'{where}:unbound_field_root:{root}'); return None
            typ=bound[root]
            for f in path:
                fields=types.get(typ,{}).get('fields',{})
                if f not in fields: errors.append(f'{where}:unknown_field:{typ}.{f}'); return None
                typ=fields[f]
            return typ
        if isinstance(arg,dict) and set(arg)=={'literal'}: return None
        errors.append(f'{where}:invalid_AST_argument:{arg!r}'); return None
    def walk(expr,bound,where):
        if not isinstance(expr,dict): errors.append(f'{where}:AST_node_not_object'); return
        ops=set(expr)&OPS
        if len(ops)!=1: errors.append(f'{where}:AST_node_must_have_exactly_one_operator:{sorted(ops)}'); return
        op=next(iter(ops))
        if op in ('and','or'):
            xs=expr[op]
            if not isinstance(xs,list) or (not xs and not r.get('empty_boolean_nodes_allowed',False)):
                errors.append(f'{where}:empty_or_invalid_{op}')
                return
            for x in xs: walk(x,bound,where)
        elif op=='not': walk(expr['not'],bound,where)
        elif op=='eq':
            if not isinstance(expr['eq'],list) or len(expr['eq'])!=2: errors.append(f'{where}:eq_arity')
            else:
                a=field_type(expr['eq'][0],bound,where); b=field_type(expr['eq'][1],bound,where)
                if a and b and a!=b: errors.append(f'{where}:eq_type_mismatch:{a}:{b}')
        elif op in ('exists','forall'):
            q=expr[op]; var=q.get('var'); typ=q.get('type')
            if typ not in types: errors.append(f'{where}:unknown_quantified_type:{typ}')
            if var in bound: errors.append(f'{where}:quantifier_shadowing:{var}')
            ds=q.get('domain')
            if ds:
                if ':' not in ds: errors.append(f'{where}:malformed_domain:{ds}')
                else:
                    prefix,param=ds.split(':',1); dspec=r.get('domain_constructors',{}).get(prefix)
                    if not dspec: errors.append(f'{where}:unknown_domain_constructor:{prefix}')
                    if param not in bound: errors.append(f'{where}:unbound_domain_parameter:{param}')
                    elif dspec and bound[param]!=dspec.get('parameter_type'): errors.append(f'{where}:domain_parameter_type_mismatch:{param}')
                    if dspec and typ in types:
                        mf=dspec.get('member_field'); pf=dspec.get('parameter_field'); ptyp=dspec.get('parameter_type')
                        mfields=types.get(typ,{}).get('fields',{})
                        pfields=types.get(ptyp,{}).get('fields',{})
                        if mf not in mfields: errors.append(f'{where}:domain_member_field_missing:{typ}.{mf}')
                        elif pf in pfields and mfields[mf]!=pfields[pf]: errors.append(f'{where}:domain_field_type_mismatch:{typ}.{mf}:{ptyp}.{pf}')
            b2=dict(bound); b2[var]=typ; walk(q.get('body',{}),b2,where)
        elif op=='pred':
            p=expr['pred']; spec=leaves.get(p)
            if not spec: errors.append(f'{where}:undefined_leaf:{p}'); return
            args=expr.get('args',[]); exp=spec['args']
            if len(args)!=len(exp): errors.append(f'{where}:arity_mismatch_leaf:{p}')
            for a,e in zip(args,exp):
                at=field_type(a,bound,where)
                if at and at!=e: errors.append(f'{where}:leaf_type_mismatch:{p}:{e}:{at}')
        elif op=='rel':
            rel=expr['rel']; spec=rels.get(rel)
            if not spec: errors.append(f'{where}:undefined_relation:{rel}'); return
            args=expr.get('args',[]); exp=spec['args']
            if len(args)!=len(exp): errors.append(f'{where}:arity_mismatch_relation:{rel}')
            for a,e in zip(args,exp):
                at=field_type(a,bound,where)
                if at and at!=e: errors.append(f'{where}:relation_type_mismatch:{rel}:{e}:{at}')
        elif op=='claim_ref':
            target=expr['claim_ref'];
            if target not in claims: errors.append(f'{where}:undefined_claim_ref:{target}'); return
            dep[where].add(target)
            args=expr.get('args',[]); exp=claims[target].get('args',[])
            if len(args)!=len(exp): errors.append(f'{where}:arity_mismatch_claim_ref:{target}')
            for a,(_n,e) in zip(args,exp):
                at=field_type(a,bound,where)
                if at and at!=e: errors.append(f'{where}:claim_ref_type_mismatch:{target}:{e}:{at}')
    for cid,c in claims.items():
        if c.get('scope') not in scopes: errors.append(f'illegal_claim_scope:{cid}:{c.get("scope")}')
        args=c.get('args',[]); names=[a[0] for a in args]
        if len(names)!=len(set(names)): errors.append(f'duplicate_claim_arguments:{cid}')
        bound={}
        for n,t in args:
            if t not in types: errors.append(f'{cid}:unknown_arg_type:{t}')
            bound[n]=t
        for tc in c.get('threshold_contract_refs',[]):
            if tc not in contracts: errors.append(f'{cid}:unknown_threshold_contract_ref:{tc}')
        walk(c.get('expr',{}),bound,cid)
    # Claim-reference acyclicity.
    visiting=set(); visited=set()
    def dfs(n):
        if n in visiting: errors.append(f'claim_reference_cycle:{n}'); return
        if n in visited:return
        visiting.add(n)
        for m in dep.get(n,()): dfs(m)
        visiting.remove(n);visited.add(n)
    for n in claims: dfs(n)
    # A threshold contract declared on a claim must be consumed somewhere in its transitive expression.
    def threshold_refs_in_expr(expr,seen=None):
        seen=set() if seen is None else seen
        try: op=_operator(expr)
        except RegistryError: return set()
        out=set()
        if op in ('and','or'):
            for x in expr[op]: out |= threshold_refs_in_expr(x,seen)
        elif op=='not': out |= threshold_refs_in_expr(expr['not'],seen)
        elif op=='pred': out |= set(leaves.get(expr['pred'],{}).get('threshold_contract_refs',[]))
        elif op in ('exists','forall'): out |= threshold_refs_in_expr(expr[op]['body'],seen)
        elif op=='claim_ref':
            target=expr['claim_ref']
            if target not in seen:
                seen.add(target); out |= threshold_refs_in_expr(claims[target]['expr'],seen)
        return out
    for cid,c in claims.items():
        declared=set(c.get('threshold_contract_refs',[])); reachable=threshold_refs_in_expr(c['expr'])
        for tc in declared-reachable: errors.append(f'{cid}:declared_threshold_not_consumed:{tc}')
    # Physical/epistemic noninterference: canonical claim registry is physical-only in v2.7.7.
    for cid,c in claims.items():
        if c.get('scope')!='physical': errors.append(f'nonphysical_claim_in_physical_registry:{cid}:{c.get("scope")}')
    # Architecture guards.
    expected={'PROGRAMME-CURRENT-1':'ProgrammeProof','LAB-CLOSURE-1':'RouteProof','NAT-REACH-1':'NaturalProof','NAT-PLAUS-1':'NaturalProof'}
    for cid,typ in expected.items():
        ex=claims[cid]['expr']
        if 'exists' not in ex or ex['exists'].get('type')!=typ: errors.append(f'{cid}:top_level_proof_object_required:{typ}')
    return {'pass':not errors,'error_count':len(errors),'errors':errors,'warnings':warnings,'claim_count':len(claims),'registry_hash':registry_hash(r)}

if __name__=='__main__':
    print(json.dumps(validate_registry(),indent=2))
