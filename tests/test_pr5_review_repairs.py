"""Adversarial PR #5 repair regressions. All evidence is synthetic, not oncology research."""
import copy
import json
import shutil
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from jsonschema import Draft202012Validator
from oocgraph import core
from oocgraph.admission.history import snapshot, obligation_inventory
from oocgraph.admission.projection import project_current
from tests.test_integrity import node
from tests.test_production_contracts import fully_typed, route_records, freeze_records, mathematical_fixture
from tests.test_routes_and_data import bridge_fixture, get

ROOT = Path(__file__).resolve().parents[1]


def retract(records, target, *, name='withdraw'):
    """Append an authority-backed correction without modifying historical evidence."""
    ctx = next(r['id'] for r in records if r.get('type') == 'Context')
    locator = next(r['id'] for r in records if r.get('type') == 'SourceLocator')
    scope = {'domain':'corrections'}
    records.extend(fully_typed([
        node('Authority',name+'-auth',status='ACTIVE_RULE',axes=['EVIDENCE_POLICY'],scope=scope),
        node('EvidenceObject',name+'-notice',status='RECORDED',context_ref=ctx,
             source_locator_refs=[locator],evidence_class='REVIEW',
             claim_ceiling='VERIFICATION_ONLY',design_class='MIXED',
             study_id='correction',system_id='audit',
             provenance_class='CURATED_SEMANTIC'),
        node('EvidenceAssessment',name+'-retraction',status='ADJUDICATED',
             target_ref=target,evidence_ref='ooc:fixture:'+name+'-notice',
             authority_ref='ooc:fixture:'+name+'-auth',effect='RETRACTS',
             assessment_role='RETRACTION',scope=scope,
             provenance_class='CURATED_SEMANTIC'),
    ]))


class AdmissionSnapshotBinding(unittest.TestCase):
    def test_freeze_issuer_id_and_target_are_distinct_but_consistent(self):
        records=freeze_records()
        programme=get(records,'p')
        event=node('AuthorizationEvent','issuer',action='FREEZE_KERNEL',
                   subject_ref=programme['id'],scope={'domain':'PROGRAMME_GOVERNANCE'},
                   basis_refs=['ooc:fixture:g','ooc:fixture:q'])
        basis=snapshot(records,[r['id'] for r in records],subject_ref=event['id'],
                       asserted_scope=event['scope'],input_graph_tree_sha='1'*40,
                       issuer_epoch='synthetic-epoch',
                       obligation_inventory_refs=obligation_inventory(records,programme['id']),
                       critical_gap_refs=['ooc:fixture:g'])
        event['admission_basis']=basis
        self.assertIsNotNone(core._event_admission_basis(records,event,None,kind='FREEZE_KERNEL'))
        # The same identity rule must govern independently authenticated production issuance.
        with tempfile.TemporaryDirectory() as tmp:
            conf=Path(tmp)/'config';conf.mkdir();(conf/'project.json').write_text('{"critical_gap_ids": ["RG-001"]}')
            nonfixture=copy.deepcopy(event);nonfixture['id']='ooc:authorization:issued'
            nonfixture['admission_basis']=snapshot(records,[r['id'] for r in records],
                subject_ref=nonfixture['id'],asserted_scope=event['scope'],
                input_graph_tree_sha='1'*40,issuer_epoch='synthetic-epoch')
            with patch.object(core,'_independently_pinned_admission_basis',return_value=True),\
                 patch.object(core,'_historical_positive_replay',return_value=True):
                self.assertTrue(core._production_issuance_authenticated(nonfixture,Path(tmp)))
        invalid=copy.deepcopy(event)
        invalid['admission_basis']=snapshot(records,[r['id'] for r in records],
            subject_ref=programme['id'],asserted_scope=event['scope'],
            input_graph_tree_sha='1'*40,issuer_epoch='synthetic-epoch',
            obligation_inventory_refs=obligation_inventory(records,programme['id']),
            critical_gap_refs=['ooc:fixture:g'])
        self.assertIsNone(core._event_admission_basis(records,invalid,None,kind='FREEZE_KERNEL'))

    def test_unsigned_mathematical_disposition_is_rejected_in_trust_root_replay(self):
        rs=freeze_records();q=get(rs,'q');q['obligation_domain']='MATHEMATICAL'
        e=get(rs,'freeze-e');e.update(evidence_class='FORMAL',claim_ceiling='MATHEMATICAL_EXACT',
              result_ref='ooc:fixture:formal-result')
        rs.append(node('Result','formal-result',verification_mode='FORMAL_PROOF',
                       verification_receipt={},status='VALIDATED',outcome='PASS'))
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp)
            # A replay with root=None must *still* authenticate formal dispositions.
            errors=core.validate_records(rs,root=None,proof_trust_root=root)
            self.assertTrue(any('UNTRUSTED_MATHEMATICAL_DISPOSITION' in e for e in errors),errors)

    def test_proof_replay_checks_artifact_output_and_checker_bytes(self):
        rs=mathematical_fixture()
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp)
            issues=core.validate_records(rs,proof_trust_root=root)
            self.assertTrue(any('PROOF_ARTIFACT_BYTE_DRIFT' in x for x in issues),issues)
            self.assertTrue(any('EXECUTION_OUTPUT_BYTE_DRIFT' in x for x in issues),issues)
            self.assertTrue(any('VERIFIER_SOFTWARE_BYTE_DRIFT' in x for x in issues),issues)
            (root/'README.md').write_text('Synthetic fixture — no biological claims\n')
            (root/'verifier_output.txt').write_text('Synthetic checker transcript: PASS\n')
            restored=core.validate_records(rs,proof_trust_root=root)
            self.assertFalse(any('BYTE_DRIFT' in x for x in restored),restored)


class CurrentStateAndCertificate(unittest.TestCase):
    def test_supported_transition_is_admitted_in_both_views(self):
        rs=route_records();out=project_current(rs)
        ident='ooc:fixture:t1'
        self.assertEqual(out['transitions'][ident]['effective'],'ADMITTED_SUPPORTED_SCOPED')
        cert=next(x for x in out['qualifications'] if x['subject_ref']==ident)
        self.assertEqual(cert['decision'],'ADMITTED')
        self.assertIn('ooc:fixture:a1',cert['accepted_assessment_refs'])

    def route_with_closure_verdict(self):
        rs=route_records()
        scope=get(rs,'r')['scope']
        e=copy.deepcopy(get(rs,'e2'));e['id']='ooc:fixture:closure-e'
        a=copy.deepcopy(get(rs,'a2'));a.update(id='ooc:fixture:closure-a',
                target_ref='ooc:fixture:r',evidence_ref=e['id'])
        rs.extend([e,a])
        rs.extend(fully_typed([
            node('Authority','closure-auth',status='ACTIVE_RULE',axes=['ROUTE_CLOSURE'],scope=scope),
            node('Verdict','closure-verdict',subject_ref='ooc:fixture:r',
                 axis='ROUTE_CLOSURE',facet='scientific',decision='SUPPORTED_SCOPED',
                 scope=scope,assessment_refs=[a['id']],authority_ref='ooc:fixture:closure-auth',
                 provenance_class='CURATED_SEMANTIC')
        ]))
        return rs

    def test_route_verdict_needs_its_own_live_support(self):
        rs=self.route_with_closure_verdict()
        before=core.resolve(rs)['partitions'][0]['state']
        self.assertEqual(before,'SUPPORTED_SCOPED')
        retract(rs,'ooc:fixture:closure-e',name='closure-withdraw')
        self.assertEqual(core.effective_route_state(rs,get(rs,'r'))['effective'],'ADMITTED_CLOSED')
        self.assertEqual(core.resolve(rs)['partitions'][0]['state'],'CONTESTED')
        self.assertEqual(core.validate_records(rs),[])

    def test_route_verdict_independent_surviving_support(self):
        rs=self.route_with_closure_verdict()
        e=copy.deepcopy(get(rs,'closure-e'));e['id']='ooc:fixture:closure-e2'
        a=copy.deepcopy(get(rs,'closure-a'));a.update(id='ooc:fixture:closure-a2',evidence_ref=e['id'])
        rs.extend([e,a]);get(rs,'closure-verdict')['assessment_refs'].append(a['id'])
        retract(rs,'ooc:fixture:closure-e',name='closure-withdraw')
        self.assertEqual(core.resolve(rs)['partitions'][0]['state'],'SUPPORTED_SCOPED')

    def test_bridge_certificate_excludes_withdrawn_alternative(self):
        rs=fully_typed(bridge_fixture())
        alt=copy.deepcopy(get(rs,'bridge'));alt['id']='ooc:fixture:bridge-alt'
        alt_a=copy.deepcopy(get(rs,'bridge-a'))
        alt_a.update(id='ooc:fixture:bridge-alt-a',evidence_ref=alt['id'])
        rs.extend([alt,alt_a])
        bundle=get(rs,'w')
        bundle['bridge_evidence_refs'].append(alt['id'])
        link=copy.deepcopy(bundle['bridge_links'][0])
        link.update(evidence_ref=alt['id'],assessment_ref=alt_a['id'])
        bundle['bridge_links'].append(link)
        retract(rs,'ooc:fixture:bridge',name='bridge-withdraw')
        self.assertEqual(core.effective_route_state(rs,get(rs,'r'))['effective'],'ADMITTED_CLOSED')
        out=project_current(rs)
        cert=next(x for x in out['qualifications'] if x['subject_ref']=='ooc:fixture:r')
        self.assertEqual(cert['decision'],'ADMITTED')
        self.assertIn(alt_a['id'],cert['accepted_assessment_refs'])
        self.assertNotIn('ooc:fixture:bridge-a',cert['accepted_assessment_refs'])
        self.assertNotIn('ooc:fixture:bridge',cert['accepted_evidence_refs'])

    def test_context_species_organism_lineage_can_all_be_recorded(self):
        ctx=get(route_records(),'c')
        ctx.update(species='human',organism='homo_sapiens',lineage='LUNG_ADENO')
        schema=json.loads((ROOT/'schema/graph-record.schema.json').read_text())['$defs']['Context']
        self.assertEqual(list(Draft202012Validator(schema).iter_errors(ctx)),[])
        e=get(route_records(),'e1')
        e['context_ref']=ctx['id']
        e['evidence_class']='PRIMARY_HUMAN_LONGITUDINAL'
        self.assertTrue(core._evidence_matches_scientific_scope(
            {ctx['id']:ctx},e,{'species':'human','organism':'homo_sapiens','lineage':'LUNG_ADENO'}))
        self.assertFalse(core._evidence_matches_scientific_scope(
            {ctx['id']:ctx},e,{'species':'human','organism':'homo_sapiens','lineage':'ANOTHER'}))


class FollowupProjectionRegressions(unittest.TestCase):
    """Two Codex P2 findings on e63f759; schema-valid append-only fixtures."""

    @staticmethod
    def appended_source_receipts():
        source=node('LiteratureSource','append-source',
                    status='REGISTERED_NOT_EXTRACTED',
                    identifiers_raw='10.1000/xyz123',
                    bibliographic_verification='UNVERIFIED',
                    extraction_status='REGISTERED_NOT_EXTRACTED',
                    verification_refs=[])
        receipt=node('SourceVerification','append-receipt',status='VERIFIED',
                     source_ref=source['id'],identifier_checked='10.1000/xyz123',
                     verification_scope='BIBLIOGRAPHIC_METADATA',
                     canonical_metadata={'doi':'10.1000/xyz123'},
                     public_source_url='https://doi.org/10.1000/xyz123',
                     provenance_class='CURATED_SEMANTIC')
        rows=fully_typed([
            node('Context','receipt-context',species='synthetic',
                 tissue='synthetic',stage='source',time_scope='past'),
            node('SourceLocator','receipt-locator',path='README.md',
                 selector={'record':'source-verification'}),
            source, receipt,
        ])
        return rows,source,receipt

    @staticmethod
    def qualification(projected,ref):
        return next(q for q in projected['qualifications']
                    if q['subject_ref']==ref)

    def test_withdrawn_only_bridge_projects_contested_without_crashing(self):
        rs=fully_typed(bridge_fixture())
        self.assertEqual(core.validate_records(rs),[])
        before=project_current(rs)
        self.assertEqual(before['routes']['ooc:fixture:r']['effective'],
                         'ADMITTED_CLOSED')
        retract(rs,'ooc:fixture:bridge',name='sole-bridge-withdrawal')
        self.assertEqual(core.validate_records(rs),[])
        self.assertEqual(core.effective_route_state(rs,get(rs,'r'))['witness_path'],[])
        projected=project_current(rs)  # Must not raise IndexError.
        self.assertEqual(projected['routes']['ooc:fixture:r']['effective'],'CONTESTED')
        q=self.qualification(projected,'ooc:fixture:r')
        self.assertEqual(q['decision'],'CONTESTED')
        bridges=[g for g in q['required_groups'] if g['name']=='BRIDGE_1']
        self.assertEqual(len(bridges),1)
        self.assertFalse(bridges[0]['satisfied'])
        self.assertEqual(bridges[0]['accepted'],[])
        self.assertNotIn('ooc:fixture:bridge',q['accepted_evidence_refs'])

    def test_append_only_source_receipt_qualifies_without_legacy_backref(self):
        rows,src,receipt=self.appended_source_receipts()
        original_source=copy.deepcopy(src)
        self.assertEqual(core.validate_records(rows),[])
        out=project_current(rows)
        self.assertEqual(src,original_source)
        self.assertEqual(src['verification_refs'],[])
        self.assertEqual(out['sources'][src['id']]['effective'],'VERIFIED')
        self.assertEqual(out['sources'][src['id']]['active_verification_refs'],
                         [receipt['id']])
        self.assertEqual(self.qualification(out,receipt['id'])['decision'],'ADMITTED')

    def test_source_receipt_retraction_does_not_contaminate_active_alternative(self):
        rows,src,receipt=self.appended_source_receipts()
        alternative=copy.deepcopy(receipt)
        alternative['id']='ooc:fixture:second-append-receipt'
        rows.append(alternative)
        original_source=copy.deepcopy(src)
        retract(rows,receipt['id'],name='receipt-revocation')
        self.assertEqual(core.validate_records(rows),[])
        out=project_current(rows)
        self.assertEqual(src,original_source)
        self.assertEqual(out['sources'][src['id']]['effective'],'VERIFIED')
        self.assertEqual(out['sources'][src['id']]['active_verification_refs'],
                         [alternative['id']])
        self.assertEqual(self.qualification(out,receipt['id'])['decision'],'CONTESTED')
        self.assertEqual(self.qualification(out,alternative['id'])['decision'],
                         'ADMITTED')
        retract(rows,alternative['id'],name='second-receipt-revocation')
        self.assertEqual(core.validate_records(rows),[])
        out=project_current(rows)
        self.assertEqual(out['sources'][src['id']]['effective'],'CONTESTED')
        self.assertEqual(self.qualification(out,alternative['id'])['decision'],
                         'CONTESTED')

if __name__=='__main__':
    unittest.main()
