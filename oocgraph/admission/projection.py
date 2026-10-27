"""Canonical, non-authoritative CURRENT-state projection for all downstream views.

This module owns the materialization boundary, not scientific truth: each
admission policy is evaluated by the production core resolver, exactly once
per subject per generation. A human must still adjudicate source evidence.
"""
from dataclasses import asdict
from .types import QualificationResult
from .certificates import support_certificate


SCIENTIFIC_TYPES = frozenset({
    'Verdict', 'Transition', 'Route', 'ModelInstance', 'DataUse',
    'Requirement', 'ResearchGap', 'LiteratureSource', 'AuthorizationEvent',
    'Programme', 'SourceVerification', 'Decision',
})


def project_current(records, *, root=None, critical_gap_ids=None):
    """Return one fully deterministic, consistent status census for viewers.

    The fixture-only ``root=None`` mode never authorizes a production claim.
    The CLI passes its real repository root (and therefore trust-policy pins).
    """
    from .. import core  # avoid import cycles with compatibility API

    records = list(records)
    idx = {r['id']: r for r in records}
    resolver = core.resolve(records, root=root)
    freeze = core.effective_freeze_eligibility(records, critical_gap_ids, root=root)
    verdicts = {}
    for part in resolver['partitions']:
        for ref in part.get('active_verdict_refs', []):
            verdicts[ref] = part['state']
        for ref in part.get('historical_verdict_refs', []):
            verdicts.setdefault(ref, 'SUPERSEDED')

    transition = {r['id']: core.effective_transition_state(records, r)
                  for r in records if r.get('type') == 'Transition'}
    route = {r['id']: core.effective_route_state(records, r)
             for r in records if r.get('type') == 'Route'}
    model = {r['id']: core.effective_model_state(records, r, root=root)
             for r in records if r.get('type') == 'ModelInstance'}
    data_use = {r['id']: core.effective_data_use_state(records, r)
                for r in records if r.get('type') == 'DataUse'}
    obligations = {r['id']: core.effective_obligation_state(records, r, root=root)
                   for r in records if r.get('type') in {'ResearchGap','Requirement'}}
    source = {r['id']: core.effective_source_verification_state(records, r)
              for r in records if r.get('type') == 'LiteratureSource'}

    def status_for(record):
        typ, ident = record['type'], record['id']
        if typ == 'Verdict': return verdicts.get(ident, record.get('decision', 'UNKNOWN'))
        if typ == 'Programme':
            return ('ADMITTED' if freeze['effective_kernel_frozen'] else
                    'CONTESTED' if record.get('kernel_frozen') else 'NOT_ADMITTED')
        if typ == 'Decision':
            target = idx.get(record.get('subject_ref'), {})
            effective = obligations.get(target.get('id'), {}).get('effective')
            return 'ADMITTED' if (target.get('decision_ref') == ident
                and isinstance(effective,str) and effective.startswith('ADMITTED_')) else 'NOT_ADMITTED'
        if typ == 'SourceVerification':
            # SourceVerification.source_ref is the append-only ownership link.
            # LiteratureSource.verification_refs is historical and must not be
            # edited merely to register a new verification receipt. Reuse the
            # authoritative per-source *active* receipt list, not the source's
            # immutable back-reference or a source-wide VERIFIED flag alone.
            parent = idx.get(record.get('source_ref'), {})
            active = (parent.get('type') == 'LiteratureSource'
                      and ident in source.get(parent.get('id'), {}).get(
                          'active_verification_refs', ()))
            return ('VERIFIED' if active else
                    'CONTESTED' if record.get('status')=='VERIFIED' else 'NOT_ADMITTED')
        if typ == 'Transition': return transition[ident]['effective']
        if typ == 'Route': return route[ident]['effective']
        if typ == 'ModelInstance': return model[ident]['effective']
        if typ == 'DataUse': return data_use[ident]['effective']
        if typ in {'Requirement', 'ResearchGap'}: return obligations[ident]['effective']
        if typ == 'LiteratureSource': return source[ident]['effective']
        if typ == 'AuthorizationEvent':
            if record.get('action') == 'FREEZE_KERNEL':
                return 'ADMITTED' if freeze['effective_kernel_frozen'] else 'CONTESTED'
            if record.get('action') == 'UNFREEZE_KERNEL':
                return 'UNFROZEN' if not freeze['effective_kernel_frozen'] else 'CONTESTED'
            if record.get('action') == 'ADMIT_MODEL':
                return model.get(record.get('subject_ref'), {}).get('effective', 'UNRESOLVED')
            return 'NOT_ADMITTED'
        return 'UNKNOWN'

    positive_states = {'SUPPORTED_SCOPED', 'MATHEMATICALLY_VERIFIED_SCOPED',
                       'ADMITTED', 'ADMITTED_SUPPORTED_SCOPED', 'ADMITTED_CLOSED', 'ADMITTED_RESOLVED',
                       'ADMITTED_SATISFIED', 'ADMITTED_BOUNDED', 'VERIFIED'}
    qualification = []
    withdrawn = core.approved_retractions(records, idx)
    for rec in sorted((r for r in records if r.get('type') in SCIENTIFIC_TYPES),
                      key=lambda r:r['id']):
        current = status_for(rec)
        scope = rec.get('scope') or rec.get('obligation_scope') or {}
        if not isinstance(scope, dict): scope = {}
        basis = rec.get('admission_basis') or {}
        accepted, required_groups = support_certificate(
            rec,idx,records,withdrawn=withdrawn,root=root,
            current_status=current,route_state=route.get(rec['id']))
        group_ok = not required_groups or all(g.satisfied for g in required_groups)
        # A projection must never fabricate admission from a raw declared status
        # when its own explanatory certificate is incomplete.
        if current in positive_states and not group_ok:
            current='CONTESTED'
        if current in positive_states:
            decision = 'ADMITTED'; reason = ('CURRENT_REQUIREMENTS_SATISFIED',)
        elif current in {'CONTESTED','LICENSE_SUSPENDED'}:
            decision = 'CONTESTED'; reason = ('CURRENT_QUALIFICATION_NOT_ESTABLISHED',)
        elif current in {'UNKNOWN', 'UNRESOLVED', 'UNADMITTED'}:
            decision = 'UNRESOLVED'; reason = ('EVIDENCE_OR_AUTHORITY_UNRESOLVED',)
        else:
            decision = 'NOT_ADMITTED'; reason = ('NO_ACTIVE_SCIENTIFIC_PROMOTION',)
        path = route.get(rec['id'],{}).get('witness_path',[]) if rec['type']=='Route' else []
        formal = (core._qualified_formal_verdict(idx,rec,root)
                  if rec['type']=='Verdict' and current=='MATHEMATICALLY_VERIFIED_SCOPED' else None)
        negatives = (obligations.get(rec['id'],{}).get('contradiction_refs',[])
                     or model.get(rec['id'],{}).get('contradiction_refs',[])
                     or route.get(rec['id'],{}).get('contradiction_refs',[]))
        qual = QualificationResult(
            subject_ref=rec['id'],
            policy_id='OOC_'+rec['type'].upper()+'_CURRENT_V2',
            scope=tuple((k,core.canonical(v)) for k,v in sorted(scope.items())),
            mode='CURRENT', decision=decision,
            required_groups=required_groups,
            accepted_assessment_refs=accepted if decision=='ADMITTED' else (),
            accepted_evidence_refs=tuple(sorted({idx[a]['evidence_ref'] for a in accepted
                if idx.get(a,{}).get('evidence_ref')})) if decision=='ADMITTED' else (),
            formal_result_ref=formal,
            witness_path=tuple(tuple(w) for w in path),
            material_contradiction_refs=tuple(sorted(negatives)),
            basis_digest=basis.get('digest') if isinstance(basis,dict) else None,
            reason_codes=reason if group_ok else reason+('MANDATORY_SUPPORT_GROUP_UNSATISFIED',),
        )
        qualification.append(asdict(qual))

    return core.loads(core.canonical({
        'resolver': resolver, 'freeze': freeze,
        'models': model, 'data_uses': data_use,
        'transitions': transition, 'routes': route,
        'obligations': obligations, 'sources': source,
        'qualifications': qualification,
        'non_authoritative_projection': True,
        'formal_or_biological_truth_from_build': False,
    }))
