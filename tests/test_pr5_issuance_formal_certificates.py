"""Adversarial PR #5 review repairs, strictly synthetic engineering fixtures.

Tests separate original validity from present entitlement. They are not cancer
or mathematical theorem evidence, and cannot authorize a production release.
"""
import copy
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
import hashlib
import json
import subprocess
from jsonschema import Draft202012Validator
from oocgraph.admission.history import snapshot, issued_record_digest

from oocgraph import core
from oocgraph.admission.formal import qualify_verified_counterevidence
from oocgraph.admission.projection import project_current
from tests.test_integrity import evidence_base, verdict, node
from tests.test_production_contracts import fully_typed, mathematical_fixture, freeze_records, route_records
from tests.test_pr5_review_repairs import retract


def fixture_capability():
    rows = fully_typed(evidence_base('PRIMARY_ANIMAL') + [
        verdict(decision='SUPPORTED_SCOPED', assessment_refs=['ooc:fixture:assessment'])])
    return rows, next(r for r in rows if r['type'] == 'Verdict')


def formal_alternatives():
    rows = mathematical_fixture()
    by_id = {r['id']:r for r in rows}
    ver = by_id['ooc:fixture:math-verdict']
    for orig, name in [('math-result','second-result'),
                       ('math-evidence','second-evidence'),
                       ('math-assessment','second-assessment')]:
        rec = copy.deepcopy(by_id['ooc:fixture:'+orig])
        rec['id'] = 'ooc:fixture:'+name
        if orig == 'math-evidence':
            rec['result_ref'] = 'ooc:fixture:second-result'
        if orig == 'math-assessment':
            rec['evidence_ref'] = 'ooc:fixture:second-evidence'
        rows.append(rec)
    ver['result_refs'].append('ooc:fixture:second-result')
    ver['assessment_refs'].append('ooc:fixture:second-assessment')
    return rows,ver


def find_qualification(out, ref):
    return next(r for r in out['qualifications'] if r['subject_ref']==ref)


class IssuanceTimeEffectiveAdmission(unittest.TestCase):
    def test_valid_issuance_snapshot_is_admitted(self):
        rows,v = fixture_capability()
        self.assertEqual(core.validate_records(rows), [])
        snapshot = {r['id']:r for r in rows if r is not v}
        self.assertTrue(core._historical_positive_replay(v,snapshot))

    def test_support_already_withdrawn_at_issuance_is_denied(self):
        rows,v = fixture_capability()
        retract(rows,'ooc:fixture:ev',name='prior-to-admission')
        self.assertEqual(core.validate_records(rows), [])
        self.assertEqual(core.resolve(rows)['partitions'][0]['state'],'CONTESTED')
        snapshot = {r['id']:r for r in rows if r is not v}
        self.assertFalse(core._historical_positive_replay(v,snapshot))

    def test_later_withdrawal_cannot_rewrite_original_validity(self):
        rows,v = fixture_capability()
        original_snapshot = {r['id']:copy.deepcopy(r) for r in rows if r is not v}
        self.assertTrue(core._historical_positive_replay(v,original_snapshot))
        retract(rows,'ooc:fixture:ev',name='after-admission')
        self.assertEqual(core.resolve(rows)['partitions'][0]['state'],'CONTESTED')
        self.assertTrue(core._historical_positive_replay(v,original_snapshot))
        self.assertFalse(core._historical_positive_replay(v,{
            r['id']:r for r in rows if r is not v}))

    def test_inactive_alternative_not_confused_with_live_support(self):
        rows,v = fixture_capability()
        source=next(r for r in rows if r['type']=='EvidenceObject')
        original=next(r for r in rows if r['type']=='EvidenceAssessment')
        second=copy.deepcopy(source);second['id']='ooc:fixture:second-support'
        assessed=copy.deepcopy(original);assessed.update(id='ooc:fixture:second-assessment',
                      evidence_ref=second['id'])
        rows.extend([second,assessed]);v['assessment_refs'].append(assessed['id'])
        retract(rows,source['id'],name='one-source-withdrawn')
        self.assertEqual(core.validate_records(rows), [])
        self.assertEqual(core.resolve(rows)['partitions'][0]['state'],'SUPPORTED_SCOPED')
        self.assertTrue(core._historical_positive_replay(v,{
            r['id']:r for r in rows if r is not v}))
        retract(rows,second['id'],name='second-source-withdrawn')
        self.assertFalse(core._historical_positive_replay(v,{
            r['id']:r for r in rows if r is not v}))

    def test_externally_pinned_issuance_cannot_certify_prior_withdrawal(self):
        rows,v = fixture_capability()
        # Separate issuance record ID from the original synthetic support IDs;
        # require a real externally presented digest, not a mocked verifier.
        v['id']='ooc:verdict:issuance-candidate'
        retract(rows,'ooc:fixture:ev',name='withdraw-before-issuance')
        basis=[r for r in rows if r is not v]
        v['admission_basis']=snapshot(
            basis,[r['id'] for r in basis],subject_ref=v['id'],
            asserted_scope=v['scope'],input_graph_tree_sha='1'*40,
            issuer_epoch='synthetic-epoch',issued_record=v)
        with tempfile.TemporaryDirectory() as temp:
            root=Path(temp)
            conf=root/'config';conf.mkdir()
            (conf/'project.json').write_text('{"critical_gap_ids": ["RG-001"]}')
            digest=v['admission_basis']['digest']
            with patch.dict('os.environ',{'OOC_AUTHORIZED_ADMISSION_BASIS_SHA256':digest}):
                self.assertFalse(core._production_issuance_authenticated(v,root))
                # Mutating the signed snapshot cannot be a valid workaround:
                # a changed basis also needs fresh independent authorization.
                v['admission_basis']=snapshot(
                    [r for r in basis if r.get('type')!='EvidenceAssessment' or
                     r.get('effect')!='RETRACTS'],
                    [r['id'] for r in basis if r.get('type')!='EvidenceAssessment' or
                     r.get('effect')!='RETRACTS'],
                    subject_ref=v['id'],asserted_scope=v['scope'],
                    input_graph_tree_sha='1'*40,issuer_epoch='synthetic-epoch',
                    issued_record=v)
                self.assertFalse(core._production_issuance_authenticated(v,root))

    def test_unrecognized_positive_path_fails_closed(self):
        self.assertFalse(core._historical_positive_replay(
            {'id':'ooc:fixture:unknown','type':'Unknown','status':'ADMITTED'},{}))


class SurvivingFormalResult(unittest.TestCase):
    def test_two_valid_result_chains_are_structurally_admitted(self):
        rows,v = formal_alternatives()
        self.assertEqual(core.validate_records(rows), [])
        self.assertEqual(core.resolve(rows)['partitions'][0]['state'],
                         'MATHEMATICALLY_VERIFIED_SCOPED')

    def test_first_withdrawn_result_does_not_veto_second(self):
        rows,v = formal_alternatives()
        retract(rows,'ooc:fixture:math-evidence',name='formal-one-withdrawn')
        self.assertEqual(core.validate_records(rows), [])
        self.assertEqual(core.resolve(rows)['partitions'][0]['state'],
                         'MATHEMATICALLY_VERIFIED_SCOPED')
        out=project_current(rows);cert=find_qualification(out,v['id'])
        self.assertEqual(cert['decision'],'ADMITTED')
        self.assertEqual(cert['formal_result_ref'],'ooc:fixture:second-result')
        self.assertEqual(cert['accepted_assessment_refs'],['ooc:fixture:second-assessment'])
        self.assertEqual(cert['accepted_evidence_refs'],['ooc:fixture:second-evidence'])

    def test_result_reference_permutation_cannot_change_entitlement(self):
        rows,v = formal_alternatives()
        retract(rows,'ooc:fixture:math-evidence',name='permutation-retraction')
        verdict_states=[]
        for order in (list(v['result_refs']), list(reversed(v['result_refs']))):
            v['result_refs']=order
            out=project_current(rows)
            verdict_states.append((core.resolve(rows)['partitions'][0]['state'],
                find_qualification(out,v['id'])['formal_result_ref']))
        self.assertEqual(verdict_states[0],verdict_states[1])
        self.assertEqual(verdict_states[0][1],'ooc:fixture:second-result')

    def test_no_live_result_chain_contests_current_only(self):
        rows,v = formal_alternatives()
        retract(rows,'ooc:fixture:math-evidence',name='withdraw-proof1')
        retract(rows,'ooc:fixture:second-evidence',name='withdraw-proof2')
        self.assertEqual(core.validate_records(rows), [])
        self.assertEqual(core.resolve(rows)['partitions'][0]['state'],'CONTESTED')
        out=project_current(rows);cert=find_qualification(out,v['id'])
        self.assertEqual(cert['decision'],'CONTESTED')
        self.assertIsNone(cert['formal_result_ref'])
        self.assertEqual(cert['accepted_assessment_refs'],[])
        self.assertEqual(cert['accepted_evidence_refs'],[])

    def test_current_issuance_replay_requires_surviving_formal_chain(self):
        rows,v = formal_alternatives()
        retract(rows,'ooc:fixture:math-evidence',name='withdraw-math-first')
        self.assertTrue(core._historical_positive_replay(v,{
            r['id']:r for r in rows if r is not v}))
        retract(rows,'ooc:fixture:second-evidence',name='withdraw-math-second')
        self.assertFalse(core._historical_positive_replay(v,{
            r['id']:r for r in rows if r is not v}))


class EvidenceKeyedCertificateTraceability(unittest.TestCase):
    def test_resolved_gap_and_requirement_include_real_assessments(self):
        rows=freeze_records();self.assertEqual(core.validate_records(rows), [])
        out=project_current(rows)
        cases=(('ooc:fixture:g','ooc:fixture:gap-a'),
               ('ooc:fixture:q','ooc:fixture:freeze-a'))
        for ref,assessment in cases:
            with self.subTest(subject=ref):
                cert=find_qualification(out,ref)
                self.assertEqual(cert['decision'],'ADMITTED')
                self.assertEqual(cert['accepted_assessment_refs'],[assessment])
                self.assertEqual(cert['accepted_evidence_refs'],['ooc:fixture:freeze-e'])

    def test_unadjudicated_alternative_is_not_in_certificate(self):
        rows=freeze_records();original=next(r for r in rows
            if r['id']=='ooc:fixture:gap-a')
        other=copy.deepcopy(original);other['id']='ooc:fixture:gap-a-not-adjudicated'
        other['status']='PROPOSED';rows.append(other)
        out=project_current(rows);cert=find_qualification(out,'ooc:fixture:g')
        self.assertEqual(cert['decision'],'ADMITTED')
        self.assertEqual(cert['accepted_assessment_refs'],['ooc:fixture:gap-a'])

    @staticmethod
    def admitted_model():
        rows=mathematical_fixture()
        model=next(x for x in rows if x['type']=='ModelInstance')
        next(x for x in rows if x['id']=='ooc:fixture:math-auth')['axes'].append('EVIDENCE_POLICY')
        rows.extend(fully_typed([
          node('EvidenceAssessment','model-license-assessment',status='ADJUDICATED',
               target_ref=model['id'],evidence_ref='ooc:fixture:math-evidence',
               effect='SUPPORTS',assessment_role='MODEL',scope=model['scope'],
               rationale='Synthetic',limitations='No biological evidence',
               provenance_class='CURATED_SEMANTIC'),
          node('AuthorizationEvent','model-license',status='RECORDED',action='ADMIT_MODEL',
               subject_ref=model['id'],authority_ref='ooc:fixture:math-auth',
               scope=model['scope'],basis_refs=[model['id']],basis_digest=model['frozen_digest'],
               evidence_refs=['ooc:fixture:math-evidence'],provenance_class='CURATED_SEMANTIC')]))
        return rows,model

    def test_model_license_reports_matched_assessment_and_evidence(self):
        rows,model=self.admitted_model()
        self.assertEqual(core.validate_records(rows), [])
        out=project_current(rows);cert=find_qualification(out,model['id'])
        self.assertEqual(cert['decision'],'ADMITTED')
        self.assertEqual(cert['accepted_assessment_refs'],['ooc:fixture:model-license-assessment'])
        self.assertEqual(cert['accepted_evidence_refs'],['ooc:fixture:math-evidence'])

    def test_withdrawn_model_license_does_not_fabricate_current_support(self):
        rows,model=self.admitted_model()
        retract(rows,'ooc:fixture:math-evidence',name='withdraw-model-evidence')
        self.assertEqual(core.validate_records(rows), [])
        out=project_current(rows);cert=find_qualification(out,model['id'])
        self.assertEqual(cert['decision'],'CONTESTED')
        self.assertEqual(cert['accepted_assessment_refs'],[])
        self.assertEqual(cert['accepted_evidence_refs'],[])


class IssuanceCrossPathMirrors(unittest.TestCase):
    def test_current_qualified_transition_route_gap_requirement_and_programme(self):
        for rows in (route_records(),freeze_records()):
            for record in rows:
                if core._is_scientific_positive(record):
                    with self.subTest(path=record['type'],id=record['id']):
                        basis={r['id']:r for r in rows if r is not record}
                        self.assertTrue(core._historical_positive_replay(record,basis))

    def test_freeze_event_requires_current_obligation_support_at_issuance(self):
        rows=freeze_records()
        programme=next(r for r in rows if r['type']=='Programme')
        programme['kernel_frozen']=False
        ids=['ooc:fixture:g','ooc:fixture:q']
        event=fully_typed([node('AuthorizationEvent','freeze-at-issuance',
              status='RECORDED',action='FREEZE_KERNEL',subject_ref=programme['id'],
              authority_ref='ooc:fixture:freeze-auth',
              scope={'domain':'PROGRAMME_GOVERNANCE'},basis_refs=ids,
              basis_digest=core.kernel_freeze_basis_digest(rows,ids),
              evidence_refs=[],provenance_class='CURATED_SEMANTIC')])[0]
        rows.append(event)
        before={r['id']:copy.deepcopy(r) for r in rows if r is not event}
        self.assertTrue(core._historical_positive_replay(event,before))
        retract(rows,'ooc:fixture:freeze-e',name='prior-to-freeze')
        self.assertEqual(core.validate_records(rows),[])
        self.assertFalse(core._historical_positive_replay(event,{
            r['id']:r for r in rows if r is not event}))
        self.assertTrue(core._historical_positive_replay(event,before))

    def test_model_admission_event_replays_without_fabricated_license(self):
        rows,model=EvidenceKeyedCertificateTraceability.admitted_model()
        event=next(r for r in rows if r.get('type')=='AuthorizationEvent')
        before={r['id']:copy.deepcopy(r) for r in rows if r is not event}
        self.assertTrue(core._historical_positive_replay(event,before))
        retract(rows,'ooc:fixture:math-evidence',name='prior-model-admission')
        self.assertEqual(core.validate_records(rows),[])
        self.assertFalse(core._historical_positive_replay(event,{
            r['id']:r for r in rows if r is not event}))
        self.assertTrue(core._historical_positive_replay(event,before))

    def test_source_receipt_requires_effective_current_verification(self):
        from tests.test_production_contracts import fully_typed
        rows=fully_typed([
            node('Context','receipt-context',species='synthetic',
                 tissue='synthetic',stage='source',time_scope='past'),
            node('SourceLocator','receipt-loc',path='README.md',
                 selector={'source':'synthetic'}),
            node('LiteratureSource','receipt-source',status='REGISTERED_NOT_EXTRACTED',
                 identifiers_raw='10.1000/xyz123',bibliographic_verification='UNVERIFIED',
                 extraction_status='REGISTERED_NOT_EXTRACTED',verification_refs=[]),
            node('SourceVerification','receipt',status='VERIFIED',
                 source_ref='ooc:fixture:receipt-source',identifier_checked='10.1000/xyz123',
                 verification_scope='BIBLIOGRAPHIC_METADATA',
                 canonical_metadata={'doi':'10.1000/xyz123'},
                 public_source_url='https://doi.org/10.1000/xyz123',
                 provenance_class='CURATED_SEMANTIC')])
        receipt=next(r for r in rows if r['type']=='SourceVerification')
        original={r['id']:copy.deepcopy(r) for r in rows if r is not receipt}
        self.assertTrue(core._historical_positive_replay(receipt,original))
        retract(rows,receipt['id'],name='prior-source-withdrawal')
        self.assertEqual(core.validate_records(rows),[])
        self.assertFalse(core._historical_positive_replay(receipt,{
            r['id']:r for r in rows if r is not receipt}))
        self.assertTrue(core._historical_positive_replay(receipt,original))


if __name__=='__main__':
    unittest.main()

class October28P1Regressions(unittest.TestCase):
    """Fail closed on invalid issuances and counterproofs; engineering fixtures."""

    def test_stamped_positive_schemas_accept_required_metadata(self):
        schema=json.loads((Path(__file__).resolve().parents[1]/
                           'schema/graph-record.schema.json').read_text())
        types=('Verdict','Route','Transition','DataUse','SourceVerification',
               'ResearchGap','Requirement','ModelInstance','AuthorizationEvent',
               'LiteratureSource','Programme')
        issuer={'id':'ooc:fixture:stamped','type':'Verdict','decision':'SUPPORTED_SCOPED'}
        for typ in types:
            with self.subTest(typ=typ):
                stamp=snapshot([],[],subject_ref=issuer['id'],
                    asserted_scope={'adapter':'synthetic'},input_graph_tree_sha='a'*40,
                    issuer_epoch='synthetic',issued_record=issuer)
                definition=schema['$defs'][typ]['properties']['admission_basis']
                self.assertTrue(Draft202012Validator(definition).is_valid(stamp))
                for key in ('issuer_epoch','input_graph_tree_sha','issued_record_sha256'):
                    invalid=copy.deepcopy(stamp);del invalid['basis'][key]
                    self.assertFalse(Draft202012Validator(definition).is_valid(invalid))

    def test_external_digest_binds_issued_status_decision_and_scope(self):
        rows=freeze_records();gap=next(r for r in rows if r['type']=='ResearchGap')
        candidate=copy.deepcopy(gap);candidate['id']='ooc:gap:issued'
        basis=[r for r in rows if r is not gap]
        candidate['admission_basis']=snapshot(basis,[r['id'] for r in basis],
            subject_ref=candidate['id'],asserted_scope=candidate['obligation_scope'],
            input_graph_tree_sha='a'*40,issuer_epoch='synthetic',
            issued_record=candidate)
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);(root/'config').mkdir()
            (root/'config/project.json').write_text('{"critical_gap_ids":["RG-001"]}')
            digest=candidate['admission_basis']['digest']
            with patch.dict('os.environ',{'OOC_AUTHORIZED_ADMISSION_BASIS_SHA256':digest}), \
                 patch.object(core,'_historical_positive_replay',return_value=True):
                self.assertTrue(core._production_issuance_authenticated(candidate,root))
                for change in ({'status':'BOUNDED','bound_scope':{'adapter':'synthetic'}},
                               {'decision_ref':'ooc:decision:unapproved'},
                               {'obligation_scope':{'adapter':'unapproved'}}):
                    altered=copy.deepcopy(candidate);altered.update(change)
                    self.assertFalse(core._production_issuance_authenticated(altered,root))
        unchanged=copy.deepcopy(candidate)
        unchanged['admission_basis']={'arbitrary':'different'}
        self.assertEqual(issued_record_digest(unchanged),issued_record_digest(candidate))

    def test_unsigned_counterproof_relation_cannot_contest_formal_claim(self):
        rows=mathematical_fixture();result=next(r for r in rows if r['type']=='Result')
        claim=next(r for r in rows if r['type']=='Claim')
        ev=copy.deepcopy(next(r for r in rows if r['type']=='EvidenceObject'))
        ev['id']='ooc:fixture:counterevidence'
        ev['counterclaim_relation']={'target_ref':claim['id'],
             'counterclaim_ref':claim['id'],'relation':'EXACT_NEGATION'}
        assessor=copy.deepcopy(next(r for r in rows if r['type']=='EvidenceAssessment'))
        assessor.update(id='ooc:fixture:counterassessment',evidence_ref=ev['id'],
                        effect='FALSIFIES')
        rows.extend([ev,assessor]);index={r['id']:r for r in rows}
        qualifies=lambda:qualify_verified_counterevidence(
            index,assessor,result['scope'],target_ref=claim['id'],
            qualified_assessment=lambda a:core._qualified_assessment(
                index,a,claim['id'],result['scope'],effect='FALSIFIES',
                allowed_classes={'FORMAL'},allowed_ceilings={'MATHEMATICAL_EXACT'}),
            verify_result=core._verified_result,
            verify_signature=lambda ix,r:core._formal_signature_active(ix,r))
        self.assertFalse(qualifies())
        digest=hashlib.sha256(claim['statement'].encode()).hexdigest()
        receipt=result['verification_receipt']
        receipt['attestation_version']='OOC_FORMAL_PROOF_ATTESTATION_V3'
        receipt['counterproof_binding']={'target_id':claim['id'],
            'counterclaim_id':claim['id'],'relation':'EXACT_NEGATION',
            'target_statement_sha256':digest,'counterclaim_statement_sha256':digest}
        self.assertTrue(qualifies())  # synthetic checker identity, not production trust
        ev['counterclaim_relation']['relation']='VERIFIED_COUNTEREXAMPLE'
        self.assertFalse(qualifies())
        ev['counterclaim_relation']['relation']='EXACT_NEGATION'
        claim['statement']='A changed claim'
        self.assertFalse(qualifies())

    def test_original_git_tree_controls_historical_biological_sources(self):
        root=Path(__file__).resolve().parents[1]
        tree=subprocess.check_output(
            ['git','-C',str(root),'rev-parse','HEAD^{tree}'],text=True).strip()
        records,ver=fixture_capability()
        prior={r['id']:copy.deepcopy(r) for r in records if r is not ver}
        self.assertTrue(core._historical_positive_replay(
            ver,prior,proof_trust_root=root,issuance_tree_sha=tree))
        current=copy.deepcopy(prior)
        locator=next(r for r in prior.values() if r['type']=='SourceLocator')
        locator['path']='../../cannot-be-proven-by-todays-README.md'
        self.assertFalse(core._historical_positive_replay(
            ver,prior,proof_trust_root=root,issuance_tree_sha=tree))
        self.assertTrue(core._historical_positive_replay(
            ver,current,proof_trust_root=root,issuance_tree_sha=tree))
        locator['path']='untracked-historical-source.txt'
        self.assertFalse(core._historical_positive_replay(
            ver,prior,proof_trust_root=root,issuance_tree_sha=tree))
        self.assertFalse(core._historical_positive_replay(
            ver,current,proof_trust_root=root,issuance_tree_sha='f'*40))

    def test_original_source_byte_hash_must_match(self):
        root=Path(__file__).resolve().parents[1]
        tree=subprocess.check_output(
            ['git','-C',str(root),'rev-parse','HEAD^{tree}'],text=True).strip()
        source={'type':'SourceArtifact','path':'README.md',
            'sha256':hashlib.sha256((root/'README.md').read_bytes()).hexdigest()}
        self.assertTrue(core._historical_repository_paths_valid([source],root,tree))
        source['sha256']='0'*64
        self.assertFalse(core._historical_repository_paths_valid([source],root,tree))
