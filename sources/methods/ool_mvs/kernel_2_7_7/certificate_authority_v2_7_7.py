"""Externally configured Ed25519 attestation and exact evaluation replay.

Keys and evaluator approvals come from a verifier's trusted configuration, never
from the untrusted evidence environment. All laboratory adapters need independent
qualification; signatures only authenticate who approved which immutable record.
"""
from __future__ import annotations
from dataclasses import dataclass, replace
from datetime import datetime
from pathlib import Path
from typing import Tuple
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey,Ed25519PublicKey
from cryptography.exceptions import InvalidSignature
from evidence_receipts_v2_7_7 import *
from threshold_contracts_v2_7_7 import validate_freeze, timestamp

@dataclass(frozen=True)
class EvaluatorRegistration:
    evaluator_id: str
    evaluator_version: str
    code_digest: str
    symbols: Tuple[str,...]
    qualification_ref: str

@dataclass(frozen=True)
class VerifierPolicy:
    policy_id: str
    registry_hashes: Tuple[str,...]
    runtime_hashes: Tuple[str,...]
    trusted_keys: Tuple[Tuple[str,bytes],...]
    evaluators: Tuple[EvaluatorRegistration,...]
    preregistration_digests: Tuple[str,...]
    allow_synthetic: bool = False
    # Hashes of the exact, independently frozen numeric/metric/unit records.
    frozen_threshold_digests: Tuple[str,...] = ()

@dataclass(frozen=True)
class Attestation:
    object_digest: str
    object_kind: str
    issuer_id: str
    signed_at: str
    evaluator_code_digest: str
    qualification_ref: str
    signature: bytes = b''

def attestation_payload(a: Attestation):return replace(a,signature=b'')
def sign_reviewed_object(obj,kind:str,issuer_id:str,key:Ed25519PrivateKey,*,signed_at:str,evaluator_code_digest:str='',qualification_ref:str='')->Attestation:
    """Invoke only after scientific/assay review; this function cannot perform it."""
    timestamp(signed_at)
    a=Attestation(stable_digest(obj),kind,issuer_id,signed_at,evaluator_code_digest,qualification_ref)
    return replace(a,signature=key.sign(canonical_bytes(attestation_payload(a))))

def _required_objects(cr:ClaimResult,ev:dict):
    support=set(cr.support_receipt_digests);out=[]
    for key,kind,prefix in [('leaf_receipts','LEAF','leafreceipt:'),('relation_receipts','RELATION','relationreceipt:'),('domains','DOMAIN','domain_source:'),('threshold_receipts','THRESHOLD','threshold:'),('evidence_receipts','RAW','rawreceipt:')]:
        for obj in ev.get(key,{}).values():
            if prefix+stable_digest(obj) in support:out.append((kind,obj))
    return out

def verify_claim_certificate(cr,bundle,ev,*,policy=None,attestations=()):
    import claim_registry_runtime_v2_7_7 as rt
    cid=getattr(cr,'claim_id','');value=getattr(cr,'result',EvidenceValue.NA)
    scope=getattr(bundle,'physical_witness_ref','');bid=getattr(bundle,'bundle_id','')
    def finish(status,reasons,assurance='NO_ATTESTATION'):
        return ClaimCertificate(cid,scope,bid,value if type(value) is EvidenceValue else EvidenceValue.NA,status,
            getattr(cr,'registry_hash',''),getattr(cr,'evaluation_mode',''),tuple(reasons),
            getattr(cr,'evaluation_digest',''),assurance,stable_digest(policy) if isinstance(policy,VerifierPolicy) else '')
    invalid=lambda why:finish(CertificateStatus.INVALID,(why,))
    if not isinstance(cr,ClaimResult) or type(cr.result) is not EvidenceValue:return invalid('typed_claim_result_required')
    if not isinstance(bundle,EvidenceBundleReceipt):return invalid('typed_evidence_bundle_required')
    if cr.evaluation_mode!='EXPERIMENTAL_EVIDENCE':return invalid('certificate_requires_experimental_evidence_mode')
    r=rt._load_validated_canonical_registry()
    if cr.claim_id not in r['claims']:return invalid('unregistered_claim')
    if cr.registry_hash!=rt.registry_hash(r) or cr.runtime_digest!=rt.runtime_hash():return invalid('registry_or_runtime_binding_mismatch')
    if not cr.evaluation_digest or cr.evaluation_digest!=stable_digest(evaluation_payload(cr)):return invalid('evaluation_digest_mismatch')
    if bundle.authority_mode!='AUTHORIZED_BUNDLER':return invalid('unauthorized_bundle_label')
    if not bundle.bundle_id or not scope or scope!=cr.physical_witness_ref:return invalid('physical_witness_binding_mismatch')
    if bundle.claim_id!=cr.claim_id or bundle.registry_hash!=cr.registry_hash or bundle.evaluation_digest!=cr.evaluation_digest:return invalid('bundle_evaluation_binding_mismatch')
    if bundle.bundle_digest!=stable_digest(bundle_payload(bundle)):return invalid('bundle_digest_mismatch')
    if tuple(bundle.support_receipt_digests)!=tuple(cr.support_receipt_digests):return invalid('exact_support_closure_required')
    if tuple(bundle.evidence_receipt_refs)!=consumed_raw_ids(cr):return invalid('exact_raw_evidence_closure_required')
    try:
        if evidence_state_digest(ev)!=cr.evidence_state_digest:return invalid('evidence_snapshot_changed')
        args={n:v for n,t,v in cr.typed_arguments}
        expected_types=tuple((n,t) for n,t in r['claims'][cid].get('args',[]))
        if tuple((n,t) for n,t,v in cr.typed_arguments)!=expected_types:return invalid('typed_arguments_mismatch')
        replay=rt.eval_evidence_claim(cid,ev,**args)
        if replay!=cr:return invalid('canonical_replay_mismatch')
        evidence_closure(bundle.evidence_receipt_refs,ev)
    except (ValueError,TypeError,KeyError,AttributeError) as e:return invalid('replay_rejected:'+str(e))
    if cr.result is EvidenceValue.NA:return finish(CertificateStatus.INCOMPLETE,cr.unresolved_dependencies or ('unresolved_evidence',))
    if not isinstance(policy,VerifierPolicy):return finish(CertificateStatus.INCOMPLETE,('trusted_verifier_policy_required',))
    if type(policy.allow_synthetic) is not bool:return invalid('typed_policy_flag_required')
    if cr.registry_hash not in policy.registry_hashes or cr.runtime_digest not in policy.runtime_hashes:return invalid('code_or_registry_not_authorized')
    keys=dict(policy.trusted_keys)
    if len(keys)!=len(policy.trusted_keys) or not keys:return invalid('invalid_trusted_key_configuration')
    att_by={}
    for a in attestations:
        if not isinstance(a,Attestation):return invalid('typed_attestation_required')
        if a.issuer_id not in keys:continue
        try:
            timestamp(a.signed_at)
            Ed25519PublicKey.from_public_bytes(keys[a.issuer_id]).verify(a.signature,canonical_bytes(attestation_payload(a)))
        except (ValueError,TypeError,InvalidSignature):return invalid('invalid_attestation_signature')
        att_by.setdefault((a.object_kind,a.object_digest),[]).append(a)
    pending=[];synthetic=False
    for kind,obj in _required_objects(cr,ev):
        digest=stable_digest(obj);att=att_by.get((kind,digest),[])
        if not att:pending.append('unattested_'+kind.lower()+':'+digest);continue
        if kind in ('LEAF','RELATION'):
            symbol=obj.predicate_id if kind=='LEAF' else obj.relation_id
            registrations=[x for x in policy.evaluators if x.evaluator_id==obj.evaluator_id and x.evaluator_version==obj.evaluator_version and symbol in x.symbols]
            if not registrations:return invalid('unregistered_evaluator:'+obj.evaluator_id+':'+symbol)
            if not any(a.evaluator_code_digest==reg.code_digest and a.qualification_ref==reg.qualification_ref and bool(reg.qualification_ref) for reg in registrations for a in att):return invalid('evaluator_qualification_mismatch:'+symbol)
        elif kind=='THRESHOLD':
            ok,reason=validate_freeze(obj)
            if not ok:return invalid(reason)
            if obj.preregistration_digest not in policy.preregistration_digests or digest not in policy.frozen_threshold_digests:return invalid('threshold_not_in_independently_frozen_policy')
        elif kind=='DOMAIN':
            if not obj.evidence_ref:pending.append('domain_enumeration_evidence_required:'+obj.type_id)
        elif kind=='RAW':
            if obj.origin=='MODEL':return invalid('model_evidence_cannot_certify_laboratory_claim')
            if obj.origin=='SYNTHETIC':
                synthetic=True
                if not policy.allow_synthetic:return invalid('synthetic_evidence_cannot_certify_laboratory_claim')
    if pending:return finish(CertificateStatus.INCOMPLETE,pending)
    assurance='SYNTHETIC_TEST_ONLY' if synthetic else 'ATTESTED_EVIDENCE_BINDING'
    return finish(CertificateStatus.VALID,('signatures_authenticate_reviewed_binding_not_physical_truth',),assurance)
