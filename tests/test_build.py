"""Deterministic projections and frozen-source integrity regression checks."""
import json
import unittest
from pathlib import Path
from oocgraph.core import read_graph,canonical,sha256,file_inventory,file_class
from oocgraph.views import make_views,PRODUCTS
ROOT=Path(__file__).resolve().parents[1]
class BuildTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):cls.products=make_views(ROOT)
    def test_deterministic_regeneration(self):self.assertEqual(self.products,make_views(ROOT))
    def test_complete_product_set(self):self.assertEqual(set(self.products),set(PRODUCTS))
    def test_jsonld_exact_roundtrip(self):
        encoded=json.loads(self.products['generated/ooc-graph.jsonld'])
        restored=[r['record'] for r in encoded['@graph']]
        self.assertEqual(restored,read_graph(ROOT))
    def test_graph_hash_matches(self):
        graph=json.loads(self.products['generated/graph.json'])
        self.assertEqual(graph['graph_sha256'],sha256(canonical(read_graph(ROOT)).encode()))
    def test_manifest_and_current_state_agree(self):
        m=json.loads(self.products['manifest.json']);s=json.loads(self.products['generated/current_state.json'])
        for key in ['graph_sha256','subject_sha256','kernel_frozen']:self.assertEqual(m[key],s[key])
    def test_no_generated_self_hash(self):
        census=json.loads(self.products['generated/repository_coverage.json'])
        for row in census['files']:
            if row['hash_excluded']:self.assertIsNone(row['sha256'])
    def test_source_locks_match(self):
        locks=json.loads((ROOT/'config/source_locks.json').read_text())['sha256']
        for path,digest in locks.items():self.assertEqual(sha256((ROOT/path).read_bytes()),digest,path)
    def test_all_subject_files_classified(self):
        for path in file_inventory(ROOT):self.assertEqual(len(file_class(path)),2)
    def test_no_biological_releases_implicit(self):
        s=json.loads(self.products['generated/current_state.json']);p=next(r for r in read_graph(ROOT) if r['type']=='Programme');self.assertEqual(s['kernel_frozen'],p['kernel_frozen']);self.assertFalse(s['clinical_use_authorized'])
    def test_explorer_has_offline_payload(self):
        text=self.products['generated/explorer.html'];self.assertIn('application/json',text);self.assertNotIn('<script src=',text);self.assertNotIn('fetch(',text)
    def test_explorer_avoids_innerhtml(self):self.assertNotIn('innerHTML',self.products['generated/explorer.html'])
    def test_no_bibliographic_duplicate_inflation(self):
        s=json.loads(self.products['generated/current_state.json']);self.assertLessEqual(s['source_identifier_groups'],s['source_rows']);self.assertGreaterEqual(s['source_identifier_groups'],68)
    def test_gap_coverage_is_91_not_only_critical(self):
        s=json.loads(self.products['generated/current_state.json']);self.assertGreaterEqual(s['research_gaps'],91);self.assertGreaterEqual(s['critical_gaps'],43)
    def test_empty_evidence_is_explicit(self):
        s=json.loads(self.products['generated/evidence_map.json']);self.assertEqual(len(s['evidence']),sum(r['type']=='EvidenceObject' for r in read_graph(ROOT)));self.assertTrue(s['sources_are_not_evidence'])
    def test_no_frozen_backend(self):
        s=json.loads(self.products['generated/model_applicability.json']);self.assertEqual(len(s['instances']),sum(r['type']=='ModelInstance' for r in read_graph(ROOT)));self.assertFalse(s['universal_backend_selected'])
    def test_blockers_not_hidden(self):
        s=json.loads(self.products['generated/blockers.json']);expected=[r['id'] for r in read_graph(ROOT) if r['type']=='ResearchGap' and r['priority']=='CRITICAL' and r['status'] not in {'RESOLVED','BOUNDED','SUPERSEDED'}];self.assertEqual(s['critical_open'],expected);self.assertFalse(s['kernel_freeze_allowed'] and bool(expected))
if __name__=='__main__':unittest.main()
