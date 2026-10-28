"""Explain *qualified* support for current admission decisions.

Not an alternate scientific permission evaluator: the authorization outcome is
owned by ``core.resolve`` and the effective-state functions. This module records
which of their admissible witnesses/assessments actually discharged the claim;
it never confers new authority from a raw EvidenceAssessment reference.
"""
from .evidence import qualify_groups


def support_certificate(record, index, records, *, withdrawn, root=None,
                        current_status=None, route_state=None):
    """Return (qualified assessment refs, mandatory group certificates).

    Missing groups are deliberate for objects where a separate authority
    contract (source verification or event issuance) governs admission.
    """
    from .. import core
    typ=record.get('type')
    scope=record.get('scope') or record.get('obligation_scope') or {}
    groups=[]
    accepted=set()

    def group(name, candidate_refs, predicate, quantifier='ANY', *, evidence_assessments=None):
        refs=[r for r in candidate_refs if isinstance(r,str)]
        result=qualify_groups([(name,quantifier,refs,len(refs))],
                              lambda _,ref:predicate(ref))[0]
        groups.append(result)
        for ref in result.accepted:
            if index.get(ref,{}).get('type')=='EvidenceAssessment':
                accepted.add(ref)
            # Some policies nominate EvidenceObject IDs, not assessment IDs.
            # Only include the exact adjudicated assessments that qualified
            # each accepted evidence candidate, never every associated claim.
            if evidence_assessments is not None:
                accepted.update(aid for aid in evidence_assessments(ref)
                                if index.get(aid,{}).get('type')=='EvidenceAssessment')

    def live_assessment(ref, *, target, role=None, kind=None, formal=False):
        a=index.get(ref,{})
        if a.get('type')!='EvidenceAssessment' or a.get('evidence_ref') in withdrawn:
            return False
        if formal:
            return core._qualified_assessment(index,a,target,scope,
                effect='SUPPORTS',allowed_classes={'FORMAL'},
                allowed_ceilings={'MATHEMATICAL_EXACT'})
        if kind:
            return core._appropriate_biological_assessment(index,a,target,scope,kind)
        return core._qualified_assessment(index,a,target,scope,
            effect='SUPPORTS',assessment_role=role)

    if typ == 'Verdict':
        subject=index.get(record.get('subject_ref'),{})
        # Route declares CAUSAL/HISTORICAL but evidence policy expects
        # ROUTE/HISTORICAL_ROUTE. Use the same mapper as validate and resolve.
        kind=(core.route_evidence_policy_key(subject)
              if subject.get('type')=='Route' else subject.get('claim_kind'))
        formal=record.get('decision')=='MATHEMATICALLY_VERIFIED_SCOPED'
        selected=(core._qualified_formal_verdict(index,record,root,withdrawn=withdrawn)
                  if formal else None)
        group('SIGNED_FORMAL_RESULT' if formal else 'VERDICT_SUPPORT',
              record.get('result_refs',[]) if formal else record.get('assessment_refs',[]),
              (lambda ref:ref==selected) if formal else
              (lambda ref:live_assessment(ref,target=subject.get('id'),
                       kind='PERSISTENCE' if kind=='ORIGIN' else kind)))
        if formal:
            for ref in record.get('assessment_refs',[]):
                a=index.get(ref,{})
                if (index.get(a.get('evidence_ref'),{}).get('result_ref')==selected
                        and live_assessment(ref,target=subject.get('id'),formal=True)):
                    accepted.add(ref)
        if kind=='ORIGIN':
            route=index.get(subject.get('origin_route_ref'),{})
            route_info=route_state or core.effective_route_state(records,route)
            group('ORIGIN_ROUTE', [route.get('id')],
                lambda ref:route_info.get('effective')=='ADMITTED_CLOSED'
                    and core.scoped_claim_entails(route.get('scope'),scope))
            wb=index.get(route.get('witness_bundle_ref'),{})
            state=index.get(subject.get('malignant_state_ref'),{})
            for name,refs,role,design in (
                ('ORIGIN_FIRST_ENTRY',subject.get('entry_assessment_refs',[]),'TEMPORAL',{'LONGITUDINAL','LINEAGE','MIXED'}),
                ('ORIGIN_ESTABLISHMENT',subject.get('establishment_assessment_refs',[]),'PERSISTENCE',{'LONGITUDINAL','MIXED'}),
            ):
                group(name, refs,lambda ref,role=role,design=design:(
                    (a:=index.get(ref,{})).get('assessment_role')==role
                    and (e:=index.get(a.get('evidence_ref'),{})).get('design_class') in design
                    and e.get('id') in wb.get('evidence_refs',[])
                    and e.get('context_ref')==state.get('context_ref')
                    and live_assessment(ref,target=subject.get('id'))))

    elif typ=='Transition':
        qualified={a['id'] for a in core._admitted_transition_assessments(
            records,index,record,scope) if a.get('evidence_ref') not in withdrawn}
        group('SUPPORTED_TRANSITION',record.get('evidence_assessment_refs',[]),
              lambda ref:ref in qualified)

    elif typ=='Route':
        route_info=route_state or core.effective_route_state(records,record)
        path=route_info.get('witness_path') or []
        route_scope=record.get('scope')
        founder=index.get(record.get('founder_ref'),{})
        bundle=index.get(record.get('witness_bundle_ref'),{})
        transitions=[index.get(ref,{}) for ref in record.get('transition_refs',[])]
        group('ANCESTRY_CONTINUITY',founder.get('ancestry_assessment_refs',[]),
              lambda ref:(
                  (a:=index.get(ref,{})).get('evidence_ref') in bundle.get('evidence_refs',[])
                  and a.get('evidence_ref') not in withdrawn
                  and core._appropriate_biological_assessment(
                      index,a,founder.get('id'),route_scope,'ANCESTRY',
                      context_ref=record.get('context_ref'))
                  and bool(path) and tuple(path[0]) in core._witness_keys(
                      index.get(a.get('evidence_ref'),{}))))
        for i,t in enumerate(transitions):
            qualified={a['id'] for a in core._admitted_transition_assessments(
                records,index,t,route_scope)
                if a.get('evidence_ref') not in withdrawn
                and a.get('evidence_ref') in bundle.get('evidence_refs',[])}
            group('SEGMENT_'+str(i+1),t.get('evidence_assessment_refs',[]),
                  lambda ref,i=i:ref in qualified and len(path)>i and
                  tuple(path[i]) in core._witness_keys(
                      index.get(index.get(ref,{}).get('evidence_ref'),{})))
        if bundle.get('mode')=='VALIDATED_BRIDGE':
            for i in range(max(0,len(transitions)-1)):
                links=[link for link in bundle.get('bridge_links',[])
                       if link.get('from_transition_ref')==transitions[i].get('id')
                       and link.get('to_transition_ref')==transitions[i+1].get('id')]
                if len(path)>i+1 and tuple(path[i])==tuple(path[i+1]):
                    continue  # Common witness needs no separate bridge
                def exact_bridge_link(ref):
                    # A contested route can have no complete witness path. Still
                    # report this mandatory bridge group as unsatisfied instead
                    # of indexing a missing pair and crashing all reviewer views.
                    if len(path) <= i + 1:
                        return False
                    # A surviving alternative qualifies only itself: never certify
                    # every candidate merely because one path remains reachable.
                    for link in links:
                        if link.get('assessment_ref') != ref:
                            continue
                        single_link_bundle = {**bundle, 'bridge_links': [link]}
                        if core._qualified_bridge_successors(
                                index, record, transitions, single_link_bundle, i,
                                {tuple(path[i])}, {tuple(path[i+1])}, withdrawn):
                            return True
                    return False
                group('BRIDGE_'+str(i+1),
                      [link.get('assessment_ref') for link in links], exact_bridge_link)

    elif typ in {'Requirement','ResearchGap'} and record.get('status') in {'SATISFIED','RESOLVED','BOUNDED'}:
        decision=index.get(record.get('decision_ref'),{})
        bound=record.get('bound_scope') if record.get('status')=='BOUNDED' else decision.get('disposition_scope')
        effects=({'CONSTRAINS','DOES_NOT_ESTABLISH'} if record.get('status')=='BOUNDED' else {'SUPPORTS'})
        def disposition_assessments(ref):
            if ref in withdrawn:
                return ()
            return tuple(sorted(a['id'] for a in records
                if a.get('type')=='EvidenceAssessment' and a.get('evidence_ref')==ref
                and any(core._admissible_disposition_evidence(
                    index,a,record.get('id'),bound,record.get('obligation_domain'),effect)
                    for effect in effects)))
        group('ADJUDICATED_DISPOSITION',decision.get('evidence_refs',[]),
              lambda ref:bool(disposition_assessments(ref)),
              evidence_assessments=disposition_assessments)

    elif typ=='ModelInstance' and current_status=='ADMITTED':
        try:
            event=core._authorization_tail(records,record.get('id'),{'ADMIT_MODEL','RETIRE_MODEL'})
        except core.IntegrityError:
            event=None
        if event and event.get('action')=='ADMIT_MODEL':
            def model_license_assessments(ref):
                if ref in withdrawn:
                    return ()
                return tuple(sorted(a['id'] for a in records
                    if a.get('type')=='EvidenceAssessment' and a.get('evidence_ref')==ref
                    and core._qualified_assessment(index,a,record.get('id'),record.get('scope'),
                        allowed_classes={'ANALYTIC','FORMAL'},
                        allowed_ceilings={'METHODOLOGICAL','MATHEMATICAL_EXACT'},
                        assessment_role='MODEL')))
            group('MODEL_LICENSE',event.get('evidence_refs',[]),
                  lambda ref:bool(model_license_assessments(ref)),quantifier='ALL',
                  evidence_assessments=model_license_assessments)

    return tuple(sorted(accepted)), tuple(groups)
