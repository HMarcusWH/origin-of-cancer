"""Atomic cryptographic/formal admission: one Result must carry *all* predicates."""
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
    # The relation between the verified proposition and the target must itself
    # be formally typed/identified; a free-text FALSIFIES effect is insufficient.
    relation = evidence.get('counterclaim_relation', {})
    return (isinstance(relation, dict)
            and relation.get('target_ref') == target_ref
            and relation.get('counterclaim_ref') == result.get('subject_ref')
            and relation.get('relation') in {'EXACT_NEGATION', 'VERIFIED_COUNTEREXAMPLE'})
