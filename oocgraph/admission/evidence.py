"""Declarative AND-of-evidence-groups/OR-of-alternatives engine.

No implicit authority: a caller must supply already-adjudicated and scoped
predicate checks.  Keeping this primitive domain-neutral lets clinical,
mathematical and data-independence policies impose different requirements.
"""
from .types import RequiredGroupResult


def qualify_groups(groups, qualifies):
    """groups: iterable (name, quantifier, candidate IDs, needed).

    The predicate ``qualifies(name, ref)`` is responsible for exact target,
    scope, method, evidence ceiling, history, and current retractions.
    Repeating the same evidence under two distinct mandatory requirements is
    not a way to skip either requirement's own qualification policy.
    """
    results = []
    for name, quantifier, candidate_refs, needed in groups:
        candidates = tuple(sorted(set(candidate_refs)))
        accepted = tuple(ref for ref in candidates if qualifies(name, ref))
        if quantifier == 'ANY':
            satisfied = bool(accepted)
        elif quantifier == 'ALL':
            satisfied = len(candidates) > 0 and len(accepted) == len(candidates)
        elif quantifier == 'AT_LEAST':
            satisfied = len(accepted) >= needed and needed > 0
        else:
            raise ValueError(f'Unknown evidence quantifier: {quantifier}')
        results.append(RequiredGroupResult(name, quantifier, candidates, accepted, satisfied))
    return tuple(results)


def groups_satisfied(results):
    return bool(results) and all(group.satisfied for group in results)


def live_support(index, records, assessment_refs, qualifies, withdrawn):
    """Return surviving evidence-qualified assessments without a veto from expired alternatives."""
    return tuple(sorted(a['id'] for ref in set(assessment_refs)
        for a in [index.get(ref, {})]
        if a.get('type') == 'EvidenceAssessment'
        and a.get('evidence_ref') not in withdrawn and qualifies(a)))
