"""Explicit scope entailment for scientific promotion, not generic JSON subset.

Scientific coordinates are conjunctive. An assertion at a broader scope than
its Claim is not licensed, even if a separate narrower evidence record exists.
"""

SCIENTIFIC_KEYS = frozenset({
    'domain','species','organism','tissue','population','time_scope','stage',
    'adapter','adapters','lineage','pan_cancer','cohort','system',
})


def scoped_claim_entails(claim_scope, verdict_scope):
    """Check that requested scope is *no broader* than the Claim's scope.

    A missing parent dimension is not a license for a broader positive flag;
    new experimental restrictions such as cohort/lineage may be added.
    Different species, domains, or adapters must never be silently converted.
    """
    if not isinstance(claim_scope, dict) or not claim_scope:
        return False
    if not isinstance(verdict_scope, dict) or not verdict_scope:
        return False
    if set(claim_scope) - SCIENTIFIC_KEYS or set(verdict_scope) - SCIENTIFIC_KEYS:
        return False
    for key, original in claim_scope.items():
        if key not in verdict_scope:
            return False
        proposed = verdict_scope[key]
        if isinstance(original, list):
            if not isinstance(proposed, list) or not set(proposed).issubset(set(original)):
                return False
        elif proposed != original:
            return False
    # Universal claims require an independent transfer policy, never an
    # unannounced promotion flag attached to a narrower assertion.
    if verdict_scope.get('pan_cancer') and not claim_scope.get('pan_cancer'):
        return False
    return True


def scientific_context_entails(context, scope):
    """Compare the declared biological tissue/species against an asserted scope."""
    if not isinstance(context,dict) or not isinstance(scope,dict):
        return False
    for key in ('species','organism','tissue','population','time_scope','stage','lineage'):
        if key in scope and scope[key] != context.get(key):
            return False
    return True
