"""OoL-MVS 2.7.7: closed, typed evidence records and content binding.

This module never infers that an observation happened. Evaluated receipts are
conditional evidence; the separate attestation verifier authenticates reviewed
records. Synthetic records cannot be promoted to laboratory evidence.
"""
from __future__ import annotations
from dataclasses import dataclass, fields, is_dataclass, replace
from enum import Enum
from typing import Any, Iterable, Mapping, Optional, Tuple
import hashlib, json, math

class EvidenceValue(str, Enum):
    PASS='PASS'; FAIL='FAIL'; NA='NA'
class CertificateStatus(str, Enum):
    VALID='VALID'; INCOMPLETE='INCOMPLETE'; INVALID='INVALID'
class DomainCompleteness(str, Enum):
    COMPLETE='COMPLETE'; PARTIAL='PARTIAL'; UNKNOWN='UNKNOWN'

def canonical_value(x: Any) -> Any:
    """A closed, type-tagged hashing language. No repr/default=str fallback."""
    if isinstance(x, Enum):
        return {'$enum':type(x).__module__+'.'+type(x).__qualname__, 'value':x.value}
    if x is None or type(x) in (bool, str): return x
    if type(x) is int: return {'$int':str(x)}
    if type(x) is float:
        if not math.isfinite(x): raise ValueError('nonfinite_canonical_number')
        return {'$float':x.hex()}
    if type(x) is bytes: return {'$bytes':x.hex()}
    if is_dataclass(x) and not isinstance(x,type):
        return {'$record':type(x).__module__+'.'+type(x).__qualname__, 'fields':{f.name:canonical_value(getattr(x,f.name)) for f in fields(x)}}
    if type(x) is tuple: return {'$tuple':[canonical_value(v) for v in x]}
    if type(x) is list: return {'$list':[canonical_value(v) for v in x]}
    if type(x) is dict:
        if any(type(k) is not str for k in x): raise TypeError('canonical_mapping_keys_must_be_strings')
        return {'$map':{k:canonical_value(x[k]) for k in sorted(x)}}
    raise TypeError('unsupported_canonical_type:'+type(x).__name__)

def canonical_bytes(obj: Any) -> bytes:
    return json.dumps(canonical_value(obj),ensure_ascii=False,sort_keys=True,separators=(',',':'),allow_nan=False).encode('utf-8')
def stable_digest(obj: Any) -> str: return hashlib.sha256(canonical_bytes(obj)).hexdigest()
def bytes_ref(data: bytes) -> str:
    if type(data) is not bytes: raise TypeError('raw_object_must_be_bytes')
    return 'sha256:'+hashlib.sha256(data).hexdigest()

def object_refs(x: Any) -> tuple[str,...]:
    """Physical witness/proof IDs embedded in a typed argument, not text guesses."""
    out=set()
    def visit(v):
        if is_dataclass(v) and not isinstance(v,type): d={f.name:getattr(v,f.name) for f in fields(v)}
        elif type(v) is dict: d=v
        elif type(v) in (tuple,list):
            for a in v:visit(a)
            return
        else:return
        for k in ('witness_id','proof_id'):
            if type(d.get(k)) is str and d[k]:out.add(d[k])
        for k,a in d.items():
            if k not in ('witness_id','proof_id'):visit(a)
    visit(x)
    return tuple(sorted(out))

@dataclass(frozen=True)
class EvidenceReceipt:
    evidence_id: str
    witness_refs: Tuple[str,...] = ()
    raw_measurement_refs: Tuple[str,...] = ()
    provenance_refs: Tuple[str,...] = ()
    assay_id: str = ''
    observation_window: str = ''
    model_input_refs: Tuple[str,...] = ()
    input_digest: str = ''
    parent_evidence_refs: Tuple[str,...] = ()
    origin: str = 'UNCLASSIFIED'

@dataclass(frozen=True)
class LeafEvaluationReceipt:
    predicate_id: str
    args: Tuple[Any,...]
    evidence_receipt_refs: Tuple[str,...]
    evaluator_id: str
    evaluator_version: str
    input_digest: str
    result: EvidenceValue
    reason_code: str = ''
    uncertainty: Optional[float] = None
    authority_mode: str = 'AUTHORIZED_EVALUATOR'

@dataclass(frozen=True)
class RelationEvaluationReceipt:
    relation_id: str
    args: Tuple[Any,...]
    evidence_receipt_refs: Tuple[str,...]
    evaluator_id: str
    evaluator_version: str
    input_digest: str
    result: EvidenceValue
    reason_code: str = ''
    authority_mode: str = 'AUTHORIZED_EVALUATOR'

@dataclass(frozen=True)
class DomainReceipt:
    type_id: str
    values: Tuple[Any,...]
    completeness: DomainCompleteness
    enumeration_method: str = ''
    evidence_ref: str = ''
    scope_route_digest: str = ''

@dataclass(frozen=True)
class ClaimResult:
    claim_id: str
    result: EvidenceValue
    unresolved_dependencies: Tuple[str,...] = ()
    failed_dependencies: Tuple[str,...] = ()
    support_receipt_digests: Tuple[str,...] = ()
    registry_hash: str = ''
    evaluation_mode: str = 'EXPERIMENTAL_EVIDENCE'
    typed_arguments: Tuple[Any,...] = ()
    physical_witness_ref: str = ''
    evidence_state_digest: str = ''
    runtime_digest: str = ''
    evaluation_digest: str = ''

@dataclass(frozen=True)
class EvidenceBundleReceipt:
    bundle_id: str
    claim_id: str
    physical_witness_ref: str
    evidence_receipt_refs: Tuple[str,...]
    support_receipt_digests: Tuple[str,...]
    registry_hash: str
    bundle_digest: str
    authority_mode: str = 'AUTHORIZED_BUNDLER'
    evaluation_digest: str = ''

@dataclass(frozen=True)
class ClaimCertificate:
    claim_id: str
    physical_witness_ref: str
    evidence_bundle_id: str
    claim_result: EvidenceValue
    certificate_status: CertificateStatus
    registry_hash: str
    evaluation_mode: str
    reason_codes: Tuple[str,...] = ()
    evaluation_digest: str = ''
    assurance_scope: str = 'NO_ATTESTATION'
    policy_digest: str = ''
    scientific_validation: str = 'NOT_ESTABLISHED_BY_SOFTWARE'


def raw_payload(rec: EvidenceReceipt) -> dict:
    return {f.name:getattr(rec,f.name) for f in fields(rec) if f.name!='input_digest'}

def build_raw_evidence(evidence_id: str, witness_refs: Iterable[str], raw_objects: Mapping[str,bytes], *,
                       assay_id: str, observation_window: str, origin: str,
                       parent_evidence_refs: Iterable[str]=(), provenance_refs: Iterable[str]=()) -> EvidenceReceipt:
    for ref,data in raw_objects.items():
        if ref!=bytes_ref(data):raise ValueError('raw_content_address_mismatch')
    r=EvidenceReceipt(evidence_id,tuple(sorted(set(witness_refs))),tuple(sorted(raw_objects)),
        tuple(provenance_refs),assay_id,observation_window,(),'',tuple(parent_evidence_refs),origin)
    return replace(r,input_digest=stable_digest(raw_payload(r)))

def evidence_closure(refs: Iterable[str], env: dict) -> tuple[dict[str,EvidenceReceipt],dict[str,bytes]]:
    """Resolve all evidence parents and all content-addressed byte objects; reject cycles."""
    raw=env.get('evidence_receipts',{}); blobs=env.get('raw_objects',{})
    resolved={}; used={}; visiting=set()
    def walk(eid):
        if eid in visiting:raise ValueError('cyclic_evidence_ancestry')
        if eid in resolved:return
        rec=raw.get(eid)
        if not isinstance(rec,EvidenceReceipt) or rec.evidence_id!=eid:raise ValueError('missing_or_invalid_raw_evidence:'+str(eid))
        if not rec.witness_refs or not rec.assay_id or not rec.observation_window:raise ValueError('incomplete_observation_metadata:'+eid)
        if rec.origin not in ('LABORATORY','MODEL','SYNTHETIC'):raise ValueError('unclassified_evidence_origin:'+eid)
        if type(rec.witness_refs) is not tuple or not all(type(v) is str and v for v in rec.witness_refs):raise TypeError('invalid_witness_refs')
        if not rec.raw_measurement_refs and not rec.model_input_refs:raise ValueError('raw_observation_required:'+eid)
        if rec.input_digest!=stable_digest(raw_payload(rec)):raise ValueError('raw_receipt_digest_mismatch:'+eid)
        for b in (*rec.raw_measurement_refs,*rec.model_input_refs,*rec.provenance_refs):
            if b not in blobs or type(blobs[b]) is not bytes or bytes_ref(blobs[b])!=b:raise ValueError('missing_or_modified_raw_object:'+b)
            used[b]=blobs[b]
        visiting.add(eid)
        for parent in rec.parent_evidence_refs:walk(parent)
        visiting.remove(eid);resolved[eid]=rec
    for ref in refs:walk(ref)
    return resolved,used

def input_payload(kind: str, symbol: str, args: tuple, refs: tuple, evaluator_id: str, version: str, env: dict) -> dict:
    raw,blobs=evidence_closure(refs,env)
    return {'kind':kind,'symbol':symbol,'args':args,'refs':refs,'evaluator_id':evaluator_id,'version':version,
            'raw':raw,'blobs':{k:bytes_ref(v) for k,v in blobs.items()}}

def build_leaf_receipt(predicate_id: str, args: Iterable[Any], result: EvidenceValue, evidence_refs: Iterable[str], evaluator_id: str, evaluator_version: str, reason_code: str='', *, evidence_env: dict|None=None) -> LeafEvaluationReceipt:
    args=tuple(args);refs=tuple(evidence_refs)
    digest=stable_digest(input_payload('leaf',predicate_id,args,refs,evaluator_id,evaluator_version,evidence_env)) if evidence_env is not None else ''
    return LeafEvaluationReceipt(predicate_id,args,refs,evaluator_id,evaluator_version,digest,EvidenceValue(result),reason_code)

def build_relation_receipt(relation_id: str, args: Iterable[Any], result: EvidenceValue, evidence_refs: Iterable[str], evaluator_id: str, evaluator_version: str, reason_code: str='', *, evidence_env: dict|None=None) -> RelationEvaluationReceipt:
    args=tuple(args);refs=tuple(evidence_refs)
    digest=stable_digest(input_payload('relation',relation_id,args,refs,evaluator_id,evaluator_version,evidence_env)) if evidence_env is not None else ''
    return RelationEvaluationReceipt(relation_id,args,refs,evaluator_id,evaluator_version,digest,EvidenceValue(result),reason_code)

def verify_evaluation_receipt(rec: Any, kind: str, name: str, args: tuple, env: dict) -> tuple[bool,str,dict,dict]:
    if type(rec.result) is not EvidenceValue:return False,'typed_evidence_value_required',{},{}
    if not rec.evaluator_id or not rec.evaluator_version or not rec.evidence_receipt_refs:return False,'incomplete_evaluator_receipt',{},{}
    if rec.authority_mode!='AUTHORIZED_EVALUATOR':return False,'unauthorized_evaluator_label',{},{}
    try:
        raw,blobs=evidence_closure(rec.evidence_receipt_refs,env)
        expected=stable_digest(input_payload(kind,name,args,rec.evidence_receipt_refs,rec.evaluator_id,rec.evaluator_version,env))
        if rec.input_digest!=expected:return False,'evaluation_input_digest_mismatch',raw,blobs
        required=set(object_refs(args))
        if not required:
            required={a for a in args if type(a) is str}
        direct_refs=set().union(*(set(raw[eid].witness_refs) for eid in rec.evidence_receipt_refs))
        if not required.issubset(direct_refs):return False,'raw_witness_binding_mismatch',raw,blobs
        return True,'ok',raw,blobs
    except (ValueError,TypeError,KeyError) as e:return False,str(e),{},{}

def evidence_state_digest(env: dict) -> str:
    # Receipt lookups use typed tuple keys internally; serialize them as sorted records.
    state={}
    for key in ('leaf_receipts','relation_receipts'):
        table=env.get(key,{})
        state[key]=sorted([{'key':k,'receipt':v} for k,v in table.items()],key=stable_digest)
    for key in ('domains','evidence_receipts','threshold_receipts'):state[key]=env.get(key,{})
    state['raw_objects']={k:bytes_ref(v) for k,v in env.get('raw_objects',{}).items()}
    return stable_digest(state)

def evaluation_payload(result: ClaimResult) -> dict:
    return {f.name:getattr(result,f.name) for f in fields(result) if f.name!='evaluation_digest'}

def bundle_payload(bundle: EvidenceBundleReceipt) -> dict:
    return {f.name:getattr(bundle,f.name) for f in fields(bundle) if f.name!='bundle_digest'}

def build_evidence_bundle(claim_result: ClaimResult, physical_witness_ref: str, evidence_receipt_refs: Iterable[str], support_receipt_digests: Iterable[str]|None=None, bundle_id: str='') -> EvidenceBundleReceipt:
    refs=tuple(sorted(set(evidence_receipt_refs)))
    support=tuple(sorted(set(claim_result.support_receipt_digests if support_receipt_digests is None else support_receipt_digests)))
    bid=bundle_id or f'bundle:{claim_result.claim_id}:{physical_witness_ref}'
    b=EvidenceBundleReceipt(bid,claim_result.claim_id,physical_witness_ref,refs,support,claim_result.registry_hash,'','AUTHORIZED_BUNDLER',claim_result.evaluation_digest)
    return replace(b,bundle_digest=stable_digest(bundle_payload(b)))

def consumed_raw_ids(result: ClaimResult) -> tuple[str,...]:
    return tuple(sorted(s[len('evidence:'):] for s in result.support_receipt_digests if s.startswith('evidence:')))

def decode_claim_result(data: dict, typed_arguments: tuple=()) -> ClaimResult:
    """Explicit JSON boundary. Witness objects must already be schema decoded by caller."""
    if type(data) is not dict:raise TypeError('claim_result_object_required')
    allowed={f.name for f in fields(ClaimResult)}
    if set(data)-allowed:raise ValueError('unknown_claim_result_fields')
    d=dict(data);d['result']=EvidenceValue(d['result'])
    for key in ('unresolved_dependencies','failed_dependencies','support_receipt_digests'):
        d[key]=tuple(d.get(key,()))
    if 'typed_arguments' in d and d['typed_arguments'] not in ([],()):
        raise ValueError('decode_typed_arguments_against_registry_before_use')
    d['typed_arguments']=typed_arguments
    return ClaimResult(**d)

def provenance_leaf_result(required_nodes: Iterable[str], provenance: Mapping[str,str], complete: bool) -> tuple[EvidenceValue,str]:
    if type(complete) is not bool:raise TypeError('complete_must_be_bool')
    vals=[provenance.get(n,'UNKNOWN') for n in required_nodes]
    if 'EXTERNAL' in vals:return EvidenceValue.FAIL,'external_ancestry'
    if any(v not in {'ADMITTED_ROOT','DESCENDANT_OF_ADMITTED'} for v in vals):return EvidenceValue.NA,'incomplete_or_unknown_provenance'
    if not complete:return EvidenceValue.NA,'provenance_domain_not_complete'
    return EvidenceValue.PASS,'provenance_closed_to_admitted_roots'

def absence_leaf_result(observed_forbidden: bool, search_domain_complete: bool) -> tuple[EvidenceValue,str]:
    if type(observed_forbidden) is not bool or type(search_domain_complete) is not bool:raise TypeError('absence_flags_must_be_bool')
    if observed_forbidden:return EvidenceValue.FAIL,'forbidden_item_observed'
    if not search_domain_complete:return EvidenceValue.NA,'absence_domain_incomplete'
    return EvidenceValue.PASS,'certified_absence_over_complete_domain'
