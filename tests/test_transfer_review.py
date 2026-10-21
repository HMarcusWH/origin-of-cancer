"""Synthetic evidence-admission regression for cross-adapter review policy."""
import shutil, tempfile, unittest
from pathlib import Path
from oocgraph.core import validate_records
from tests.test_integrity import node
from tests.test_production_contracts import fully_typed
ROOT=Path(__file__).resolve().parents[1]

def example():
    scope={'pan_cancer':True}
    cid='ooc:fixture:cross-claim'
    aid='ooc:fixture:cross-authority'
    rec=[
        node('Claim','cross-claim',scope=scope,status='PROVISIONAL',
             claim_kind='CONSTITUTIVE',statement='Synthetic scope comparison',
             modality='ASSERTION',empirical_admission='NOT_ESTABLISHED'),
        node('Authority','cross-authority',scope=scope,status='ACTIVE_RULE',
             axes=['BIOLOGICAL_SUPPORT','EVIDENCE_POLICY'],empirical_truth_authority=False),
        node('Context','cross-context'),
        node('SourceLocator','cross-loc',path='README.md',selector={'fixture':'only'})
    ]
    adapters=[];evidences=[]
    for i in range(6):
        ad=node('Adapter',f'cross-ad-{i}',dossier_complete=False)
        ev=node('EvidenceObject',f'cross-ev-{i}',status='RECORDED',
                context_ref='ooc:fixture:cross-context',source_locator_refs=['ooc:fixture:cross-loc'],
                evidence_class='PRIMARY_ANIMAL',claim_ceiling='BIOLOGICAL_CAUSAL_SCOPED',
                design_class='MIXED',study_id=f'study-{i}',system_id=f'system-{i}',
                provenance_class='CURATED_SEMANTIC')
        assessment=node('EvidenceAssessment',f'cross-ass-{i}',
                target_ref=cid,evidence_ref=ev['id'],status='ADJUDICATED',
                effect='SUPPORTS',assessment_role='CAUSAL',scope={'adapter':ad['id']},
                provenance_class='CURATED_SEMANTIC')
        rec.extend([ad,ev,assessment]);adapters.append(ad['id']);evidences.append(ev['id'])
    rec.extend([
        node('EvidenceAssessment','cross-overall',target_ref=cid,evidence_ref=evidences[0],
             status='ADJUDICATED',effect='SUPPORTS',assessment_role='CAUSAL',
             scope=scope,provenance_class='CURATED_SEMANTIC'),
        node('Decision','cross-transfer',status='RECORDED',decision_kind='TRANSFER',
             decision='ALLOW_TRANSFER',scope=scope,subject_ref=cid,authority_ref=aid,
             transfer_adapter_refs=adapters,evidence_refs=evidences,
             provenance_class='CURATED_SEMANTIC'),
        node('Verdict','cross-verdict',status='RECORDED',axis='BIOLOGICAL_SUPPORT',
             facet='synthetic',subject_ref=cid,authority_ref=aid,scope=scope,
             decision='SUPPORTED_SCOPED',assessment_refs=['ooc:fixture:cross-overall'],
             transfer_decision_ref='ooc:fixture:cross-transfer',
             result_refs=[],supersedes_refs=[])
    ])
    return fully_typed(rec)

class AdapterReviewRegression(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp=tempfile.TemporaryDirectory();cls.root=Path(cls.tmp.name)
        (cls.root/'schema').mkdir()
        for n in ('graph-record.schema.json','vocab.json','nested_reference_contract.json'):
            shutil.copy(ROOT/'schema'/n,cls.root/'schema'/n)
        (cls.root/'README.md').write_text('Synthetic fixture — no biological claims\n')
    @classmethod
    def tearDownClass(cls):cls.tmp.cleanup()
    def errors(self,records):return validate_records(records,self.root)
    def test_distinct_synthetic_adapters_are_representable(self):
        self.assertEqual(self.errors(example()),[])
    def test_explicit_denial_never_authorizes(self):
        r=example();next(x for x in r if x['type']=='Decision')['decision']='DENY_TRANSFER'
        self.assertTrue(any('MISSING_CROSS_ADAPTER_DECISION' in e for e in self.errors(r)))
    def test_recycled_study_ids_cannot_imply_independent_adapters(self):
        r=example()
        for x in r:
            if x['type']=='EvidenceObject':x['study_id']='same-study';x['system_id']='same-system'
        self.assertTrue(any('TRANSFER_INDEPENDENCE_NOT_ESTABLISHED' in e for e in self.errors(r)))
