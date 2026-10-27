"""Source-pinned, synthetic-only state projection and policy-registry tests."""
import copy
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from oocgraph import core
from oocgraph.views import make_views
from oocgraph.admission.projection import project_current
from oocgraph.admission.registry import registry_errors
from oocgraph.admission.history import snapshot, historical_obligations
from tests.test_integrity import node, evidence_base, verdict
from tests.test_production_contracts import route_records
from tests.test_preemptive_origin import append_withdrawal

ROOT = Path(__file__).resolve().parents[1]

class CanonicalProjectionContract(unittest.TestCase):
    def test_all_generated_scientific_states_derive_from_single_projection(self):
        authored=core.read_graph(ROOT)
        projected=project_current(authored,root=ROOT,
            critical_gap_ids=json.loads((ROOT/'config/project.json').read_text())['critical_gap_ids'])
        outputs=make_views(ROOT)
        state=json.loads(outputs['generated/current_state.json'])
        routes=json.loads(outputs['generated/route_atlas.json'])
        models=json.loads(outputs['generated/model_applicability.json'])
        uses=json.loads(outputs['generated/data_use_firewall.json'])
        evidence=json.loads(outputs['generated/evidence_map.json'])
        self.assertEqual(state['resolver'],projected['resolver'])
        self.assertEqual(state['kernel_frozen'],projected['freeze']['effective_kernel_frozen'])
        self.assertEqual({r['id']:r['effective'] for r in routes['effective_routes']},
                         {k:v['effective'] for k,v in projected['routes'].items()})
        self.assertEqual({r['id']:r['effective'] for r in models['effective_model_states']},
                         {k:v['effective'] for k,v in projected['models'].items()})
        self.assertEqual({r['id']:r['effective'] for r in uses['effective_independence']},
                         {k:v['effective'] for k,v in projected['data_uses'].items()})
        self.assertEqual(evidence['admission_qualification'],projected['qualifications'])
        self.assertTrue(projected['non_authoritative_projection'])
        self.assertFalse(projected['formal_or_biological_truth_from_build'])
    def test_existing_baseline_is_unfrozen_and_unadmitted(self):
        state=json.loads(make_views(ROOT)['generated/current_state.json'])
        self.assertEqual(state['stage'],'PRE_FORMALIZATION')
        self.assertFalse(state['kernel_frozen'])
        self.assertEqual(state['critical_gaps'],43)
        self.assertEqual(state['open_critical_gaps'],43)
        self.assertEqual(state['model_instances'],0)
        self.assertEqual(state['evidence_objects'],0)
        self.assertEqual(state['completed_paper_extractions'],0)
        self.assertFalse(state['clinical_use_authorized'])
    def test_route_certificate_contains_connected_witness(self):
        records=route_records()
        result=project_current(records)
        r=next(x for x in result['qualifications'] if x['subject_ref']=='ooc:fixture:r')
        self.assertEqual(r['decision'],'ADMITTED')
        self.assertTrue(r['witness_path'])
        self.assertTrue(all(len(key)==3 for key in r['witness_path']))
    def test_route_without_ancestry_qualifies_neither_state_nor_certificate(self):
        records=route_records()
        f=next(x for x in records if x['id']=='ooc:fixture:f')
        f['ancestry_assessment_refs']=[]
        result=project_current(records)
        r=next(x for x in result['qualifications'] if x['subject_ref']=='ooc:fixture:r')
        self.assertEqual(r['decision'],'CONTESTED')
        self.assertFalse(r['witness_path'])
    def test_supported_verdict_and_withdrawn_alternative(self):
        rs=evidence_base('PRIMARY_ANIMAL')
        rs.append(verdict(decision='SUPPORTED_SCOPED',assessment_refs=['ooc:fixture:assessment']))
        v=next(x for x in project_current(rs)['qualifications'] if x['subject_ref']=='ooc:fixture:v')
        self.assertEqual(v['decision'],'ADMITTED')
        append_withdrawal(rs,target='ev')
        next(x for x in rs if x['id']=='ooc:fixture:origin-withdrawal-notice')['source_locator_refs']=['ooc:fixture:loc']
        next(x for x in rs if x['id']=='ooc:fixture:origin-withdrawal-notice')['context_ref']='ooc:fixture:context'
        v=next(x for x in project_current(rs)['qualifications'] if x['subject_ref']=='ooc:fixture:v')
        self.assertEqual(v['decision'],'CONTESTED')
        self.assertEqual(v['accepted_assessment_refs'],[])
    def test_supported_verdict_reports_only_actually_qualified_evidence(self):
        rs=evidence_base('PRIMARY_ANIMAL')
        rs.append(verdict(decision='SUPPORTED_SCOPED',assessment_refs=['ooc:fixture:assessment']))
        q=next(x for x in project_current(rs)['qualifications'] if x['subject_ref']=='ooc:fixture:v')
        self.assertEqual(q['accepted_assessment_refs'],['ooc:fixture:assessment'])
        self.assertEqual(q['accepted_evidence_refs'],['ooc:fixture:ev'])
        self.assertEqual(q['required_groups'][0]['name'],'VERDICT_SUPPORT')
        self.assertTrue(q['required_groups'][0]['satisfied'])
        # A merely declared ADJUDICATED record is not accepted if its target is foreign.
        a=next(x for x in rs if x['id']=='ooc:fixture:assessment')
        a['target_ref']='ooc:fixture:context'
        q=next(x for x in project_current(rs)['qualifications'] if x['subject_ref']=='ooc:fixture:v')
        self.assertEqual(q['decision'],'CONTESTED')
        self.assertEqual(q['accepted_assessment_refs'],[])

    def test_route_certificate_exposes_ancestry_and_segment_groups(self):
        records=route_records()
        q=next(x for x in project_current(records)['qualifications'] if x['subject_ref']=='ooc:fixture:r')
        self.assertEqual(q['decision'],'ADMITTED')
        self.assertTrue(q['witness_path'])
        mandatory={x['name'] for x in q['required_groups']}
        self.assertIn('ANCESTRY_CONTINUITY',mandatory)
        self.assertIn('SEGMENT_1',mandatory)
        self.assertIn('SEGMENT_2',mandatory)
        self.assertTrue(all(x['satisfied'] for x in q['required_groups']))

    def test_no_root_mode_is_explicitly_non_production(self):
        rs=evidence_base('PRIMARY_ANIMAL')
        rs.append(verdict(decision='SUPPORTED_SCOPED',assessment_refs=['ooc:fixture:assessment']))
        self.assertTrue(core._production_issuance_authenticated(rs[-1],root=None))
        self.assertFalse(core._production_issuance_authenticated(rs[-1],root=ROOT))
        self.assertTrue(any('UNAUTHORIZED_POSITIVE_ISSUANCE' in e
                            for e in core.validate_records(__import__('tests.test_production_contracts',fromlist=['fully_typed']).fully_typed(rs),ROOT)))

class PromotionPathRegistryContract(unittest.TestCase):
    def test_schema_registry_and_evaluator_ownership_pass(self):
        self.assertEqual(registry_errors(ROOT),[])
        entries=json.loads((ROOT/'config/promotion_path_registry.json').read_text())['sinks']
        self.assertTrue(any(i['id']=='Programme.kernel_frozen:true' for i in entries))
        self.assertTrue(all(i.get('evaluator') for i in entries))
    def test_missing_known_owner_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);(root/'config').mkdir();(root/'schema').mkdir()
            registry=json.loads((ROOT/'config/promotion_path_registry.json').read_text())
            target=next(x for x in registry['sinks'] if x['id']=='Verdict.decision:SUPPORTED_SCOPED')
            target['evaluator']='THIS_DOES_NOT_EXIST'
            (root/'config/promotion_path_registry.json').write_text(json.dumps(registry))
            (root/'schema/graph-record.schema.json').write_bytes((ROOT/'schema/graph-record.schema.json').read_bytes())
            self.assertTrue(any('UNOWNED_SCIENTIFIC_ADMISSION_EVALUATOR' in e
                                for e in registry_errors(root)))
    def test_non_authoritative_metadata_cannot_claim_resolver(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);(root/'config').mkdir();(root/'schema').mkdir()
            registry=json.loads((ROOT/'config/promotion_path_registry.json').read_text())
            target=next(x for x in registry['sinks'] if x['mode']=='NON_AUTHORITATIVE_METADATA')
            target['evaluator']='resolve'
            (root/'config/promotion_path_registry.json').write_text(json.dumps(registry))
            (root/'schema/graph-record.schema.json').write_bytes((ROOT/'schema/graph-record.schema.json').read_bytes())
            self.assertTrue(any('METADATA_CONFUSED_WITH_SCIENTIFIC_ADMISSION' in e
                                for e in registry_errors(root)))

class HistoricalSnapshotContract(unittest.TestCase):
    def test_content_addressed_original_basis_survives_new_obligations(self):
        old=[{'id':'ooc:fixture:requirement','type':'Requirement','status':'SATISFIED',
             'subject_ref':'ooc:fixture:programme'},
             {'id':'ooc:fixture:evidence','type':'EvidenceObject','status':'RECORDED'}]
        snap=snapshot(old,[x['id'] for x in old],subject_ref='ooc:fixture:programme',
            asserted_scope={'domain':'research'},
            obligation_inventory_refs=['ooc:fixture:requirement'],
            input_graph_tree_sha='a'*40,issuer_epoch='1')
        event={'admission_basis':snap}
        basis=historical_obligations(event)
        self.assertIn('ooc:fixture:requirement',basis)
        new=old+[{'id':'ooc:fixture:later','type':'Requirement','status':'OPEN',
                  'subject_ref':'ooc:fixture:programme'}]
        self.assertNotIn('ooc:fixture:later',historical_obligations(event))
        self.assertEqual(historical_obligations(event),basis)
    def test_snapshot_record_mutation_rejected_without_repinning(self):
        record={'id':'ooc:fixture:g','type':'ResearchGap','status':'RESOLVED'}
        stamp=snapshot([record],[record['id']],subject_ref='ooc:fixture:programme',
                       input_graph_tree_sha='a'*40,issuer_epoch='1')
        stamp['basis']['records'][0]['status']='OPEN'
        self.assertIsNone(historical_obligations({'admission_basis':stamp}))
    def test_later_evidence_cannot_backfill_invalid_origin_issuance(self):
        from tests.test_preemptive_origin import fixture
        import copy
        current=fixture()
        verdict=next(x for x in current if x['id']=='ooc:fixture:origin-verdict')
        historical=copy.deepcopy({x['id']:x for x in current if x is not verdict})
        historical['ooc:fixture:origin-claim']['entry_assessment_refs']=[]
        # The present graph contains a valid entry claim, but issuance did not.
        self.assertEqual(core.validate_records(current),[])
        self.assertFalse(core._historical_positive_replay(verdict,historical))
        good={x['id']:x for x in current if x is not verdict}
        self.assertTrue(core._historical_positive_replay(verdict,good))

    def test_production_requires_external_authorization_even_for_valid_checksum(self):
        record={'id':'ooc:fixture:g','type':'ResearchGap','status':'RESOLVED'}
        stamp=snapshot([record],[record['id']],subject_ref='ooc:fixture:programme',
                       input_graph_tree_sha='a'*40,issuer_epoch='1')
        with patch.dict('os.environ',{},clear=True):
            self.assertIsNone(historical_obligations({'admission_basis':stamp},
                require_authenticated=True,verifier=core._independently_pinned_admission_basis))

if __name__=='__main__':unittest.main()
