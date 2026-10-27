"""Historical Origin versus current biological evidence; synthetic only."""
import copy
import json
import shutil
import tempfile
import unittest
from pathlib import Path

from oocgraph import core
from tests.test_integrity import node
from tests.test_production_contracts import route_records, fully_typed

ROOT=Path(__file__).resolve().parents[1]
SCOPE={'adapter':'synthetic'}


def fixture():
    rs=route_records()
    rs += fully_typed([
        node('StateVariable','malignancy-readout',definition='Independent synthetic measure',history_role='BIOLOGICAL',observable_status='OBSERVED',units='synthetic'),
        node('PersistenceCriterion','origin-persistence',context_ref='ooc:fixture:c',estimand_ref='ooc:fixture:origin-estimand',horizon=1,metric='established',preregistration_status='REGISTERED',rationale='Prospective synthetic endpoint',units='time'),
        node('Estimand','origin-estimand',definition_obligation='Synthetic residence time'),
        node('Claim','origin-claim',claim_kind='ORIGIN',scope=SCOPE,status='PROVISIONAL',statement='Synthetic entry and establishment',modality='ASSERTION',empirical_admission='NOT_ESTABLISHED',origin_route_ref='ooc:fixture:r',malignant_state_ref='ooc:fixture:s3',persistence_criterion_ref='ooc:fixture:origin-persistence',entry_assessment_refs=['ooc:fixture:origin-entry'],establishment_assessment_refs=['ooc:fixture:origin-establishment']),
        node('Authority','origin-authority',status='ACTIVE_RULE',axes=['BIOLOGICAL_SUPPORT'],scope=SCOPE,empirical_truth_authority=False),
        node('EvidenceAssessment','origin-entry',status='ADJUDICATED',effect='SUPPORTS',assessment_role='TEMPORAL',target_ref='ooc:fixture:origin-claim',evidence_ref='ooc:fixture:e1',scope=SCOPE,rationale='Synthetic entry',limitations='Synthetic',provenance_class='CURATED_SEMANTIC'),
        node('EvidenceAssessment','origin-establishment',status='ADJUDICATED',effect='SUPPORTS',assessment_role='PERSISTENCE',target_ref='ooc:fixture:origin-claim',evidence_ref='ooc:fixture:e2',scope=SCOPE,rationale='Synthetic establishment',limitations='Synthetic',provenance_class='CURATED_SEMANTIC'),
        node('Verdict','origin-verdict',status='RECORDED',axis='BIOLOGICAL_SUPPORT',facet='malignant-origin',decision='SUPPORTED_SCOPED',scope=SCOPE,subject_ref='ooc:fixture:origin-claim',authority_ref='ooc:fixture:origin-authority',assessment_refs=['ooc:fixture:origin-establishment'],result_refs=[],supersedes_refs=[],rationale='Synthetic composed origin')
    ])
    idx={x['id']:x for x in rs}
    idx['ooc:fixture:s3']['variable_refs']=['ooc:fixture:malignancy-readout']
    idx['ooc:fixture:e2']['design_class']='MIXED'
    return rs


def append_withdrawal(rs,target='e1'):
    rs += fully_typed([
        node('Authority','origin-retraction-authority',status='ACTIVE_RULE',axes=['EVIDENCE_POLICY'],scope={'domain':'withdrawal'}),
        node('EvidenceObject','origin-withdrawal-notice',status='RECORDED',context_ref='ooc:fixture:c',source_locator_refs=['ooc:fixture:l'],evidence_class='REVIEW',claim_ceiling='VERIFICATION_ONLY',study_id='synthetic-notice-study',system_id='review',finding='Invalidated origin support',uncertainty='none',provenance_class='CURATED_SEMANTIC'),
        node('EvidenceAssessment','origin-withdrawal',status='ADJUDICATED',effect='RETRACTS',assessment_role='RETRACTION',target_ref='ooc:fixture:'+target,evidence_ref='ooc:fixture:origin-withdrawal-notice',authority_ref='ooc:fixture:origin-retraction-authority',scope={'domain':'withdrawal'},rationale='New synthetic evidence',limitations='Synthetic',provenance_class='CURATED_SEMANTIC')])


class HistoricalOriginContracts(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory()
        self.root=Path(self.tmp.name)
        (self.root/'schema').mkdir()
        for f in ('graph-record.schema.json','vocab.json','nested_reference_contract.json'):
            shutil.copy(ROOT/'schema'/f,self.root/'schema'/f)
        (self.root/'README.md').write_text('Synthetic fixture — no biological claims\n')
    def tearDown(self):self.tmp.cleanup()
    def check(self,records):return core.validate_records(records,self.root)
    def test_valid_origin_historically_and_currently(self):
        rs=fixture();self.assertEqual(self.check(rs),[])
        self.assertEqual(core.resolve(rs)['partitions'][0]['state'],'SUPPORTED_SCOPED')
    def test_later_retraction_contests_current_without_invalidating_history(self):
        rs=fixture();old=copy.deepcopy(next(x for x in rs if x['type']=='Verdict'))
        append_withdrawal(rs)
        self.assertEqual(self.check(rs),[])
        self.assertEqual(old,next(x for x in rs if x['type']=='Verdict'))
        self.assertEqual(core.resolve(rs)['partitions'][0]['state'],'CONTESTED')
        self.assertEqual(core.effective_route_state(rs,next(x for x in rs if x['type']=='Route'),historical=True)['effective'],'ADMITTED_CLOSED')
    def test_missing_entry_cannot_promote_origin(self):
        rs=fixture();next(x for x in rs if x['type']=='Claim' and x.get('claim_kind')=='ORIGIN')['entry_assessment_refs']=[]
        self.assertTrue(any('NONBIOLOGICAL_PROMOTION' in x for x in self.check(rs)))
    def test_missing_establishment_cannot_promote_origin(self):
        rs=fixture();next(x for x in rs if x['type']=='Claim' and x.get('claim_kind')=='ORIGIN')['establishment_assessment_refs']=[]
        self.assertTrue(any('NONBIOLOGICAL_PROMOTION' in x for x in self.check(rs)))
    def test_new_unrelated_evidence_does_not_undo_retraction(self):
        rs=fixture();append_withdrawal(rs)
        e=copy.deepcopy(next(x for x in rs if x['id']=='ooc:fixture:e1'))
        e['id']='ooc:fixture:unrelated-new-evidence';e['study_id']='other'
        rs.append(e)
        self.assertEqual(self.check(rs),[])
        self.assertEqual(core.resolve(rs)['partitions'][0]['state'],'CONTESTED')

if __name__=='__main__':unittest.main()
