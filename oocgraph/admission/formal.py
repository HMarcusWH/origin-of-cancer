"""Atomic cryptographic/formal admission: one Result must carry *all* predicates."""
import hashlib
from .types import QualificationResult


def qualify_formal_result(index, result, *, claim_ref, model_ref, scope, verify_result,
                          evidence_refs=(), assessments=(), qualifies_assessment=None,
                          verify_signature=None):
    """Return a Result ID only if one *same* Result discharges every contract.

    verify_signature must be externally pinned in production. The only use of
    verify_signature=None is in explicitly synthetic reference tests; production
    callers must supply a rejecting/pinned verifier.
    """
    if not (isinstance(result, dict) and result.get('type') == 'Result'
            and result.get('model_instance_ref') == model_ref
            and result.get('subject_ref') == claim_ref
            and verify_result(index, result, claim_ref, scope)
            and verify_signature is not None and verify_signature(index, result)):
        return None
    if not evidence_refs:
        return None
    for evidence_ref in evidence_refs:
        evidence = index.get(evidence_ref, {})
        if (evidence.get('type') != 'EvidenceObject'
                or evidence.get('evidence_class') != 'FORMAL'
                or evidence.get('claim_ceiling') != 'MATHEMATICAL_EXACT'
                or evidence.get('result_ref') != result.get('id')):
            return None
        if not any(index.get(ref, {}).get('evidence_ref') == evidence_ref
                   and qualifies_assessment(index.get(ref, {}), evidence_ref)
                   for ref in assessments):
            return None
    return result['id']


def qualify_verified_counterevidence(index, assessment, scope, *, target_ref,
                                     qualified_assessment, verify_result, verify_signature):
    """Labels FALSIFIES/CONTRADICTS are not formally checked counterexamples."""
    evidence = index.get(assessment.get('evidence_ref'), {})
    result = index.get(evidence.get('result_ref'), {})
    if (evidence.get('evidence_class') != 'FORMAL'
            or evidence.get('claim_ceiling') != 'MATHEMATICAL_EXACT'
            or not qualified_assessment(assessment)
            or result.get('type') != 'Result'
            or not verify_result(index, result, result.get('subject_ref'), scope)
            or not verify_signature(index, result)):
        return False
    # A label on EvidenceObject is unsigned. Only checker-attested V3
    # counterproofs can contradict an exact mathematical proposition.
    receipt = result.get('verification_receipt', {})
    binding = receipt.get('counterproof_binding', {})
    relation = evidence.get('counterclaim_relation', {})
    target = index.get(target_ref, {})
    if target.get('type') in {'Requirement', 'ResearchGap'}:
        target = index.get(target.get('obligation_claim_ref'), {})
    counterclaim = index.get(result.get('subject_ref'), {})
    if (receipt.get('attestation_version') != 'OOC_FORMAL_PROOF_ATTESTATION_V3'
            or not isinstance(binding, dict) or not isinstance(relation, dict)
            or target.get('type') != 'Claim'
            or counterclaim.get('type') != 'Claim'
            or not isinstance(target.get('statement'), str)
            or not isinstance(counterclaim.get('statement'), str)):
        return False
    digest = lambda statement: hashlib.sha256(statement.encode('utf-8')).hexdigest()
    return bool(
        binding.get('target_id') == target_ref
        and binding.get('counterclaim_id') == result.get('subject_ref')
        and binding.get('relation') in {'EXACT_NEGATION', 'VERIFIED_COUNTEREXAMPLE'}
        and binding.get('relation') == relation.get('relation')
        and relation.get('target_ref') == target_ref
        and relation.get('counterclaim_ref') == result.get('subject_ref')
        and binding.get('target_statement_sha256') == digest(target['statement'])
        and binding.get('counterclaim_statement_sha256') == digest(counterclaim['statement'])
        and receipt.get('statement_sha256') == digest(counterclaim['statement'])
    )
