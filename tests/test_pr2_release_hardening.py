"""Synthetic PR #2 review regressions; never empirical cancer or theorem evidence."""
import copy
import json
import shutil
import os
import tempfile
import unittest
from base64 import b64encode
from pathlib import Path
from unittest.mock import patch

from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey
from cryptography.hazmat.primitives.serialization import Encoding,PublicFormat
from oocgraph.core import (
    canonical, sha256, validate_records, trusted_proof_receipt, proof_attestation_payload,
    approved_retractions, approved_reinstatements, effective_transition_state,
    effective_route_state, effective_data_use_state, effective_freeze_eligibility,
    effective_source_verification_state, resolve, kernel_freeze_basis_digest,
)
from tests.test_integrity import node
from tests.test_production_contracts import (
    fully_typed, freeze_records, mathematical_fixture,
)
from tests.test_latest_codex import LatestCodexContracts
from tests.test_transfer_review import example as pan_cancer_fixture
from tests.test_routes_and_data import bridge_fixture

ROOT = Path(__file__).resolve().parents[1]


class PR2ReleaseHardening(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp=tempfile.TemporaryDirectory()
        cls.root=Path(cls.tmp.name)
        (cls.root/'schema').mkdir()
        for name in ('graph-record.schema.json','vocab.json','nested_reference_contract.json'):
            shutil.copy(ROOT/'schema'/name,cls.root/'schema'/name)
        (cls.root/'README.md').write_text('Synthetic fixture — no biological claims\n')
        (cls.root/'verifier_output.txt').write_text('Synthetic checker transcript: PASS\n')

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()

    def errors(self,records):
        return validate_records(records,self.root)

    def test_unfreeze_event_overrides_old_true_flag(self):
        rs=freeze_records(); programme=next(r for r in rs if r['type']=='Programme')
        programme['kernel_frozen']=True
        basis=['ooc:fixture:g','ooc:fixture:q']
        digest=kernel_freeze_basis_digest(rs,basis)
        events=[]
        for name,action,previous in [('freeze','FREEZE_KERNEL',None),('unfreeze','UNFREEZE_KERNEL','ooc:fixture:freeze')]:
            event=node('AuthorizationEvent',name,status='RECORDED',action=action,
                       subject_ref=programme['id'],authority_ref='ooc:fixture:freeze-auth',
                       scope={'domain':'PROGRAMME_GOVERNANCE'},basis_refs=basis,
                       basis_digest=digest,evidence_refs=[],provenance_class='CURATED_SEMANTIC')
            if previous:event['previous_event_ref']=previous
            events.append(event)
        rs+=fully_typed(events)
        self.assertEqual(self.errors(rs),[])
        self.assertFalse(effective_freeze_eligibility(rs,['ooc:fixture:g'])['effective_kernel_frozen'])
        self.assertTrue(effective_freeze_eligibility(rs,['ooc:fixture:g'])['eligible'])
        rs.pop()
        self.assertTrue(effective_freeze_eligibility(rs,['ooc:fixture:g'])['effective_kernel_frozen'])

    def test_appended_adapter_preserves_history_but_narrows_current(self):
        rs=pan_cancer_fixture()
        self.assertEqual(self.errors(rs),[])
        rs+=fully_typed([node('Adapter','cross-seventh-adapter',dossier_complete=False)])
        self.assertEqual(self.errors(rs),[])
        self.assertEqual(resolve(rs)['partitions'][0]['state'],'CONTESTED')

    def test_surviving_transition_without_common_route_witness(self):
        rs=LatestCodexContracts.retracted_route_fixture(None)
        e=copy.deepcopy(next(r for r in rs if r['id']=='ooc:fixture:e1'))
        a=copy.deepcopy(next(r for r in rs if r['id']=='ooc:fixture:a1'))
        e.update(id='ooc:fixture:independent-evidence',study_id='other-study',
                 system_id='other-system',witness_ids=['other-witness'])
        a.update(id='ooc:fixture:independent-assessment',evidence_ref=e['id'])
        rs.extend([e,a])
        t=next(r for r in rs if r['id']=='ooc:fixture:t1')
        r=next(r for r in rs if r['type']=='Route')
        t['evidence_assessment_refs'].append(a['id'])
        next(x for x in rs if x['type']=='WitnessBundle')['evidence_refs'].append(e['id'])
        # The newly added evidence shares no old common witness; do not treat
        # it as a substitute for every other segment of the route.
        # Don't change immutable route witness bundle: a newly discovered
        # alternate study can support the transition without closing the old route.
        self.assertEqual(self.errors(fully_typed(rs)),[])
        self.assertEqual(effective_transition_state(rs,t)['effective'],'ADMITTED_SUPPORTED_SCOPED')
        self.assertEqual(effective_route_state(rs,r)['effective'],'CONTESTED')

    def test_reinstatement_notice_retraction_reactivates_original_withdrawal(self):
        rs=fully_typed(LatestCodexContracts.retracted_route_fixture(None))
        prior=next(r for r in rs if r['id']=='ooc:fixture:retraction-adjudication')
        notice=copy.deepcopy(next(r for r in rs if r['id']=='ooc:fixture:retraction-notice'))
        notice['id']='ooc:fixture:reinstate-notice'
        rein=node('EvidenceAssessment','reinstate',status='ADJUDICATED',effect='REINSTATES',
                  assessment_role='REASSESSMENT',target_ref=prior['id'],
                  evidence_ref=notice['id'],authority_ref=prior['authority_ref'],
                  scope=prior['scope'],rationale='Correction',limitations='Synthetic',
                  provenance_class='CURATED_SEMANTIC')
        rs+=fully_typed([notice,rein]);self.assertNotIn('ooc:fixture:e1',approved_retractions(rs))
        negative=copy.deepcopy(notice);negative['id']='ooc:fixture:notice-retraction-evidence'
        rev=node('EvidenceAssessment','revoke-notice',status='ADJUDICATED',
                 effect='RETRACTS',assessment_role='RETRACTION',target_ref=notice['id'],
                 evidence_ref=negative['id'],authority_ref=prior['authority_ref'],
                 scope=prior['scope'],rationale='Reinstatement notice invalidated',
                 limitations='Synthetic',provenance_class='CURATED_SEMANTIC')
        rs+=fully_typed([negative,rev])
        self.assertEqual(self.errors(rs),[])
        self.assertIn(notice['id'],approved_retractions(rs))
        self.assertIn('ooc:fixture:e1',approved_retractions(rs))
        self.assertNotIn(prior['id'],approved_reinstatements(rs))

    def test_contrary_partition_audit_contests_both_uses_only_if_pair_scoped(self):
        from tests.test_routes_and_data import IndependenceEvidenceTests
        fx=IndependenceEvidenceTests();fx.setUp()
        rs=fx.records
        prior=next(r for r in rs if r['id']=='ooc:fixture:audit-e')
        audit=copy.deepcopy(prior)
        audit.update(id='ooc:fixture:negative-audit',finding='Discovered unit overlap',study_id='later-audit')
        rs.append(audit)
        for suffix in ('a','b'):
            a=copy.deepcopy(next(r for r in rs if r['id']=='ooc:fixture:audit-'+suffix))
            a.update(id='ooc:fixture:negative-'+suffix,evidence_ref=audit['id'],effect='CONTRADICTS')
            rs.append(a)
        self.assertEqual(validate_records(rs),[])
        self.assertEqual(effective_data_use_state(rs,fx.a)['effective'],'CONTESTED')
        self.assertEqual(effective_data_use_state(rs,fx.b)['effective'],'CONTESTED')
        rs[-1]['scope']={'adapter':'unrelated'}
        self.assertEqual(effective_data_use_state(rs,fx.a)['effective'],'ADMITTED')

    def test_identifier_must_match_canonical_metadata_and_public_link(self):
        records=fully_typed([
            node('LiteratureSource','source-id',identifiers_raw='10.1000/correct',
                 bibliographic_verification='UNVERIFIED',extraction_status='REGISTERED_NOT_EXTRACTED'),
            node('SourceVerification','receipt',status='VERIFIED',
                 source_ref='ooc:fixture:source-id',identifier_checked='10.1000/correct',
                 verification_scope='BIBLIOGRAPHIC_METADATA',
                 canonical_metadata={'doi':'10.1000/correct'},
                 public_source_url='https://doi.org/10.1000/correct',
                 provenance_class='CURATED_SEMANTIC')])
        source=records[0];receipt=records[1]
        self.assertEqual(self.errors(records),[])
        self.assertEqual(effective_source_verification_state(records,source)['effective'],'VERIFIED')
        receipt['canonical_metadata']['doi']='10.1000/different'
        self.assertTrue(any('UNBACKED_VERIFICATION_CERTIFICATE' in e for e in self.errors(records)))
        self.assertNotEqual(effective_source_verification_state(records,source)['effective'],'VERIFIED')
        receipt['canonical_metadata']['doi']='10.1000/correct'
        receipt['public_source_url']='https://doi.org/10.1000/different'
        self.assertTrue(self.errors(records))

    def test_bridge_evidence_uses_adjacent_handoff_not_route_origin(self):
        rs=fully_typed(bridge_fixture())
        rs.extend(fully_typed([node('Context','later-context',status='RECORDED')]))
        a_ctx='ooc:fixture:c';b_ctx='ooc:fixture:later-context'
        for ident in ('s2','s3'):
            next(r for r in rs if r['id']=='ooc:fixture:'+ident)['context_ref']=b_ctx
        next(r for r in rs if r['id']=='ooc:fixture:e2')['context_ref']=b_ctx
        next(r for r in rs if r['id']=='ooc:fixture:f')['member_refs']=['ooc:fixture:s1']
        for name,sc,tc in [('t1',a_ctx,b_ctx),('t2',b_ctx,b_ctx)]:
            transition=next(r for r in rs if r['id']=='ooc:fixture:'+name)
            transition.update(source_context_ref=sc,target_context_ref=tc,
                              context_transition_assessment_ref='ooc:fixture:'+name+'-handoff-a')
            evidence=node('EvidenceObject',name+'-handoff-e',status='RECORDED',
                         context_ref=b_ctx,source_locator_refs=['ooc:fixture:l'],
                         evidence_class='PRIMARY_ANIMAL',claim_ceiling='BIOLOGICAL_CAUSAL_SCOPED',
                         design_class='LONGITUDINAL',study_id='handoff',system_id=name,
                         provenance_class='CURATED_SEMANTIC')
            assessment=node('EvidenceAssessment',name+'-handoff-a',status='ADJUDICATED',
                            effect='SUPPORTS',evidence_ref=evidence['id'],target_ref=transition['id'],
                            assessment_role='TEMPORAL',scope={'adapter':'synthetic'},
                            provenance_class='CURATED_SEMANTIC')
            rs.extend(fully_typed([evidence,assessment]))
        bridge=next(r for r in rs if r['id']=='ooc:fixture:bridge')
        invalid=self.errors(rs)
        self.assertTrue(any('INVALID_BRIDGE_LINK' in x for x in invalid),invalid)
        bridge['context_ref']=b_ctx
        self.assertEqual(self.errors(rs),[])

    def test_proof_trust_requires_external_digest_and_attested_outcomes(self):
        rs=mathematical_fixture()
        index={r['id']:r for r in rs}
        result=next(r for r in rs if r['type']=='Result')
        execution=index[result['execution_ref']]
        software=index[execution['software_ref']]
        software['runtime_role']='FORMAL_PROOF_CHECKER'
        software['provenance_class']='CURATED_SEMANTIC'
        signer='synthetic-proof-signer'
        key=Ed25519PrivateKey.generate()
        receipt=result['verification_receipt']
        receipt['attestation_version']='OOC_FORMAL_PROOF_ATTESTATION_V2'
        receipt['attestation_signer_id']=signer
        registry={'trusted_checkers':[{
            'id':signer,'status':'ACTIVE','verifier_sha256':software['sha256'],
            'verifier_version':receipt['verifier_version'],
            'public_key_base64':b64encode(key.public_key().public_bytes(
                Encoding.Raw,PublicFormat.Raw)).decode()}]}
        with tempfile.TemporaryDirectory() as dirname:
            root=Path(dirname);(root/'config').mkdir()
            path=root/'config/trusted_proof_checkers.json'
            path.write_text(json.dumps(registry))
            raw_digest=sha256(path.read_bytes())
            receipt['attestation_signature_b64']=b64encode(key.sign(
                canonical(proof_attestation_payload(index,result)).encode())).decode()
            with patch.dict(os.environ,{'OOC_TRUST_POLICY_SHA256':''}):
                self.assertFalse(trusted_proof_receipt(root,index,result))
            with patch.dict(os.environ,{'OOC_TRUST_POLICY_SHA256':'0'*64}):
                self.assertFalse(trusted_proof_receipt(root,index,result))
            with patch.dict(os.environ,{'OOC_TRUST_POLICY_SHA256':raw_digest}):
                self.assertTrue(trusted_proof_receipt(root,index,result))
                (root/'schema').mkdir()
                for schema_file in ('graph-record.schema.json','vocab.json','nested_reference_contract.json'):
                    shutil.copy(ROOT/'schema'/schema_file,root/'schema'/schema_file)
                (root/'config/project.json').write_text(json.dumps({'critical_gap_ids':[]}))
                (root/'README.md').write_text('Synthetic fixture — no biological claims\n')
                (root/'verifier_output.txt').write_text('Synthetic checker transcript: PASS\n')
                self.assertEqual(validate_records(rs,root),[])
                # Old signature must not authorize altered validation outcomes.
                result['outcome']='FAIL';receipt['outcome']='FAIL'
                self.assertFalse(trusted_proof_receipt(root,index,result))
                result['outcome']='PASS';receipt['outcome']='PASS'
                self.assertTrue(trusted_proof_receipt(root,index,result))
                software['runtime_role']='REFERENCE_ONLY'
                self.assertFalse(trusted_proof_receipt(root,index,result))

if __name__=='__main__':unittest.main()
