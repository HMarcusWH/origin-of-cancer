"""Latest Codex counterexamples through the full production schema.

These are deliberately synthetic fixtures. They are NEVER biological results.
"""
import copy
import json
import shutil
import tempfile
import unittest
from pathlib import Path
from oocgraph.core import (validate_records, history_violations,
                           effective_route_state, effective_transition_state)
from tests.test_integrity import node, evidence_base, verdict
from tests.test_routes_and_data import route_fixture
from tests.test_production_contracts import fully_typed, route_records, freeze_records, mathematical_fixture

ROOT=Path(__file__).resolve().parents[1]


class LatestCodexContracts(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.temp=tempfile.TemporaryDirectory()
        cls.root=Path(cls.temp.name)
        (cls.root/'schema').mkdir()
        for name in ('graph-record.schema.json','vocab.json','nested_reference_contract.json'):
            shutil.copy(ROOT/'schema'/name, cls.root/'schema'/name)
        (cls.root/'README.md').write_text('Synthetic fixture — no biological claims\n')
    @classmethod
    def tearDownClass(cls):
        cls.temp.cleanup()
    def errors(self,rs):
        return validate_records(rs,self.root)
    def rejects(self,rs,code):
        errs=self.errors(rs)
        self.assertTrue(any(code in x for x in errs),(code,errs))

    def test_supported_verdict_other_axis_is_not_a_bypass(self):
        rs=evidence_base('PRIMARY_ANIMAL')
        auth=next(x for x in rs if x['type']=='Authority')
        auth['axes']=['RESEARCH_POLICY']
        rs.append(verdict(decision='SUPPORTED_SCOPED',
                          assessment_refs=['ooc:fixture:assessment']))
        # The fixture helper already specifies axis; construct exactly one valid object.
        rs[-1]['axis']='RESEARCH_POLICY'
        self.rejects(fully_typed(rs),'UNSUPPORTED_VERDICT_AXIS')

    def test_standalone_supported_transition_requires_evidence(self):
        rs=route_records()
        tr=next(x for x in rs if x['type']=='Transition')
        tr['evidence_assessment_refs']=[]
        self.rejects(rs,'UNSUPPORTED_STANDALONE_TRANSITION')

    def test_standalone_supported_transition_has_real_scope(self):
        rs=route_records()
        tr=next(x for x in rs if x['type']=='Transition')
        self.assertEqual(effective_transition_state(rs,tr)['effective'],
                         'ADMITTED_SUPPORTED_SCOPED')
        self.assertEqual(self.errors(rs),[])

    def test_standalone_transition_requires_declared_scope(self):
        rs=route_records()
        tr=next(x for x in rs if x['type']=='Transition')
        tr.pop('scope')
        self.rejects(rs,'UNSCOPED_SUPPORTED_TRANSITION')

    def test_history_locks_adjudicated_claim_meaning(self):
        claim=node('Claim','c',statement='historical statement')
        v=node('Verdict','v',subject_ref=claim['id'])
        before=[claim,v]
        after=copy.deepcopy(before)
        after[0]['statement']='silently rewritten'
        self.assertTrue(any('MUTATED_ADMITTED_DEPENDENCY' in x
                            for x in history_violations(before,after)))

    def test_history_locks_source_selector(self):
        loc=node('SourceLocator','locator',selector={'figure':'1A'})
        ev=node('EvidenceObject','ev',source_locator_refs=[loc['id']])
        before=[loc,ev]
        after=copy.deepcopy(before)
        after[0]['selector']={'figure':'9Z'}
        self.assertTrue(any('MUTATED_ADMITTED_DEPENDENCY' in x
                            for x in history_violations(before,after)))

    def test_history_locks_resolved_requirement_criterion(self):
        before=freeze_records()
        after=copy.deepcopy(before)
        next(r for r in after if r['type']=='Requirement')['criterion']='rewritten obligation'
        self.assertTrue(history_violations(before,after))

    def test_unrelated_draft_can_be_edited(self):
        draft=node('Claim','draft',statement='first draft')
        ev=node('EvidenceObject','ev')
        before=[draft,ev]
        after=copy.deepcopy(before)
        after[0]['statement']='new draft'
        self.assertEqual(history_violations(before,after),[])

    def test_direct_route_contradiction_downgrades_effective_state(self):
        rs=route_records()
        route=next(x for x in rs if x['type']=='Route')
        a=copy.deepcopy(next(x for x in rs if x['id']=='ooc:fixture:a2'))
        a['id']='ooc:fixture:route-contradiction'
        a['target_ref']=route['id']
        a['effect']='CONTRADICTS'
        rs.append(a)
        self.assertEqual(self.errors(rs),[])
        self.assertEqual(effective_route_state(rs,route)['effective'],'CONTESTED')

    def test_founder_contradiction_downgrades_effective_state(self):
        rs=route_records()
        route=next(x for x in rs if x['type']=='Route')
        a=copy.deepcopy(next(x for x in rs if x['id']=='ooc:fixture:fa'))
        a['id']='ooc:fixture:founder-contradiction'
        a['effect']='FALSIFIES'
        rs.append(a)
        self.assertEqual(self.errors(rs),[])
        self.assertEqual(effective_route_state(rs,route)['effective'],'CONTESTED')

    def context_transfer(self, admitted=True):
        rs=route_records()
        ctx='ooc:fixture:later-context'
        rs.append(fully_typed([node('Context','later-context',status='RECORDED',
            species='synthetic',tissue='synthetic',stage='malignant',
            time_scope='later')])[0])
        next(x for x in rs if x['id']=='ooc:fixture:s3')['context_ref']=ctx
        if admitted:
            tr=next(x for x in rs if x['id']=='ooc:fixture:t2')
            tr['source_context_ref']='ooc:fixture:c'
            tr['target_context_ref']=ctx
            tr['context_transition_assessment_ref']='ooc:fixture:context-assessment'
            evidence=fully_typed([node('EvidenceObject','context-evidence',
                context_ref=ctx,status='RECORDED',
                evidence_class='PRIMARY_ANIMAL',
                claim_ceiling='BIOLOGICAL_OBSERVATION',
                study_id='synthetic-study',system_id='synthetic-system',
                design_class='LONGITUDINAL',source_locator_refs=['ooc:fixture:l'],
                provenance_class='CURATED_SEMANTIC')])[0]
            assessment=fully_typed([node('EvidenceAssessment','context-assessment',
                status='ADJUDICATED',target_ref=tr['id'],
                evidence_ref=evidence['id'],effect='SUPPORTS',
                assessment_role='TEMPORAL',scope={'adapter':'synthetic'},
                provenance_class='CURATED_SEMANTIC')])[0]
            rs.extend([evidence,assessment])
        return rs

    def test_explicit_context_stage_transition_is_representable(self):
        self.assertEqual(self.errors(self.context_transfer()),[])

    def test_unexplained_context_stage_transition_rejected(self):
        self.rejects(self.context_transfer(admitted=False),'UNVALIDATED_CONTEXT_TRANSITION')

    def test_critical_requirement_must_match_gap_obligation(self):
        rs=freeze_records()
        q=next(x for x in rs if x['type']=='Requirement')
        q['obligation_claim_kind']='OBSERVATION'
        self.rejects(rs,'CRITICAL_GAP_OBLIGATION_MISMATCH')

    def test_proof_receipt_must_bind_exact_bytes(self):
        rs=mathematical_fixture()
        res=next(x for x in rs if x['type']=='Result')
        res['verification_receipt']['artifact_sha256']='0'*64
        self.rejects(rs,'PROOF_RECEIPT_ARTIFACT_MISMATCH')

    def retracted_route_fixture(self):
        rs=route_records()
        notice=fully_typed([node('EvidenceObject','retraction-notice',
            status='RECORDED',context_ref='ooc:fixture:c',evidence_class='REVIEW',
            claim_ceiling='VERIFICATION_ONLY',design_class='OBSERVATIONAL',
            study_id='synthetic-journal',system_id='synthetic-notice',
            source_locator_refs=['ooc:fixture:l'],finding='Synthetic correction notice',
            provenance_class='CURATED_SEMANTIC')])[0]
        authority=fully_typed([node('Authority','retraction-policy',
            status='ACTIVE_RULE',axes=['EVIDENCE_POLICY'],
            scope={'adapter':'synthetic'},empirical_truth_authority=False,
            provenance_class='CURATED_SEMANTIC')])[0]
        assessment=fully_typed([node('EvidenceAssessment','retraction-adjudication',
            status='ADJUDICATED',effect='RETRACTS',assessment_role='RETRACTION',
            target_ref='ooc:fixture:e1',evidence_ref=notice['id'],
            authority_ref=authority['id'],scope={'adapter':'synthetic'},
            rationale='Synthetic provenance correction',
            provenance_class='CURATED_SEMANTIC')])[0]
        rs.extend([notice,authority,assessment])
        return rs

    def test_authorized_retraction_preserves_historical_record_and_contests_route(self):
        from oocgraph.core import approved_retractions
        before=route_records()
        rs=self.retracted_route_fixture()
        self.assertEqual(self.errors(rs),[])
        self.assertEqual(history_violations(before,rs),[])
        route=next(x for x in rs if x['type']=='Route')
        self.assertEqual(effective_route_state(rs,route)['effective'],'CONTESTED')
        self.assertIn('ooc:fixture:e1',approved_retractions(rs))

    def test_unapproved_retraction_cannot_change_current_support(self):
        from oocgraph.core import approved_retractions
        rs=self.retracted_route_fixture()
        next(x for x in rs if x['id']=='ooc:fixture:retraction-policy')['status']='REVOKED'
        self.rejects(rs,'UNAUTHORIZED_RETRACTION')
        self.assertNotIn('ooc:fixture:e1',approved_retractions(rs))

    def test_retraction_proposal_does_not_revoke_support(self):
        rs=self.retracted_route_fixture()
        next(x for x in rs if x['id']=='ooc:fixture:retraction-adjudication')['status']='IN_REVIEW'
        self.assertEqual(self.errors(rs),[])
        route=next(x for x in rs if x['type']=='Route')
        self.assertEqual(effective_route_state(rs,route)['effective'],'ADMITTED_CLOSED')

    def test_verification_receipt_requires_exact_source_identifier(self):
        source=node('LiteratureSource','s',
                    identifiers_raw='10.1038/s41568-023-00602-5',
                    bibliographic_verification='VERIFIED',
                    verification_refs=['ooc:fixture:verify'])
        proof=node('SourceVerification','verify',status='VERIFIED',
                   source_ref=source['id'],identifier_checked='1',
                   verification_scope='BIBLIOGRAPHIC_METADATA',
                   canonical_metadata={'doi':'10.1038/s41568-023-00602-5'},
                   public_source_url='https://doi.org/10.1038/s41568-023-00602-5',
                   provenance_class='CURATED_SEMANTIC')
        rs=fully_typed([source,proof])
        self.rejects(rs,'UNBACKED_SOURCE_VERIFICATION')
        next(x for x in rs if x['type']=='SourceVerification')['identifier_checked']='10.1038/s41568-023-00602-5'
        self.assertEqual(self.errors(rs),[])


if __name__=='__main__':
    unittest.main()
