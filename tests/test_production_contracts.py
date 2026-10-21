"""Production-schema integration tests: synthetic objects, not cancer findings.

Unlike the intentionally minimal unit fixtures, these fixtures are run through
the actual JSON Schema validator AND the complete graph semantic gate.
"""
import copy
import json
import shutil
import tempfile
import unittest
from pathlib import Path
from jsonschema import Draft202012Validator
from oocgraph.core import validate_records
from tests.test_integrity import freeze_fixture
from tests.test_routes_and_data import route_fixture, bridge_fixture

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = json.loads((ROOT/'schema/graph-record.schema.json').read_text())


def _sample(prop, key):
    if 'const' in prop:
        return prop['const']
    if 'enum' in prop:
        if key == 'status' and 'RECORDED' in prop['enum']:
            return 'RECORDED'
        return prop['enum'][0]
    kind = prop.get('type')
    if isinstance(kind, list):
        kind = next((t for t in kind if t != 'null'), kind[0])
    if key == 'id':
        return 'ooc:fixture:generated'
    if key == 'label':
        return 'Synthetic fixture'
    if key == 'path':
        return 'README.md'
    if key == 'claim_ceiling':
        return 'BIOLOGICAL_CAUSAL_SCOPED'
    if key in {'output_sha256', 'sha256'}:
        return 'a'*64
    if key.endswith('_ref'):
        return 'ooc:fixture:missing'
    if kind == 'boolean':
        return False
    if kind == 'object':
        return {'fixture': 'synthetic'} if prop.get('minProperties', 0) else {}
    if kind == 'array':
        return ['synthetic'] if prop.get('minItems', 0) else []
    if kind == 'integer' or kind == 'number':
        return 1
    return 'synthetic'


def fully_typed(records):
    """Populate uninteresting required schema fields, preserving test semantics."""
    result = copy.deepcopy(records)
    for r in result:
        definition = SCHEMA['$defs'][r['type']]
        for key in definition['required']:
            if key not in r:
                r[key] = _sample(definition['properties'][key], key)
        status_spec = definition['properties'].get('status', {})
        if r.get('status') == 'OPEN' and 'enum' in status_spec and 'OPEN' not in status_spec['enum']:
            r['status'] = _sample(status_spec, 'status')
        errors = list(Draft202012Validator(definition).iter_errors(r))
        if errors:
            raise AssertionError((r['id'],[(list(x.path),x.message) for x in errors]))
    return result


def freeze_records():
    records = freeze_fixture()
    records.append({
        'id': 'ooc:fixture:context', 'type': 'Context', 'label': 'Synthetic context',
        'status': 'OPEN', 'provenance_class': 'CURATED_SEMANTIC', 'schema_version': '0.1.0'
    })
    next(r for r in records if r['type'] == 'EvidenceObject')['context_ref'] = 'ooc:fixture:context'
    return fully_typed(records)


def route_records():
    return fully_typed(route_fixture())


class ProductionValidation(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.TemporaryDirectory()
        cls.root = Path(cls.tmp.name)
        (cls.root/'schema').mkdir()
        for source in ('graph-record.schema.json','vocab.json','nested_reference_contract.json'):
            shutil.copy(ROOT/'schema'/source,cls.root/'schema'/source)
        (cls.root/'README.md').write_text('Synthetic fixture — no biological claims\n')
    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()
    def errors(self, records):
        return validate_records(records,self.root)
    def assert_problem(self, records, code):
        errors = self.errors(records)
        self.assertTrue(any(code in x for x in errors),errors)
    def test_fully_schema_valid_positive_freeze(self):
        self.assertEqual(self.errors(freeze_records()),[])
    def test_fully_schema_valid_positive_same_system_route(self):
        self.assertEqual(self.errors(route_records()),[])
    def test_fully_schema_valid_positive_bridge_route(self):
        self.assertEqual(self.errors(fully_typed(bridge_fixture())),[])
    def test_negative_disposition_against_status(self):
        rs=freeze_records()
        next(r for r in rs if r['id']=='ooc:fixture:freeze-d')['decision']='REJECT'
        self.assert_problem(rs,'INCOMPATIBLE_DISPOSITION')
    def test_negative_ceiling(self):
        rs=freeze_records()
        next(r for r in rs if r['type']=='EvidenceObject')['claim_ceiling']='VERIFICATION_ONLY'
        self.assert_problem(rs,'UNADJUDICATED_DISPOSITION_EVIDENCE')
    def test_no_crash_schema_invalid_disposition(self):
        rs=freeze_records()
        next(r for r in rs if r['id']=='ooc:fixture:freeze-d')['evidence_refs']=[{'bad':'object'}]
        self.assert_problem(rs,'SCHEMA')
    def test_no_crash_schema_invalid_requirement(self):
        rs=freeze_records()
        next(r for r in rs if r['type']=='Requirement')['satisfaction_evidence_refs']=[{'bad':'object'}]
        self.assert_problem(rs,'SCHEMA')
    def test_bridge_refs_validated_even_while_open(self):
        rs=fully_typed(bridge_fixture())
        next(r for r in rs if r['type']=='Route')['status']='OPEN'
        next(r for r in rs if r['type']=='WitnessBundle')['bridge_links'][0]['evidence_ref']='ooc:fixture:missing'
        self.assert_problem(rs,'MISSING_NESTED_REF')
    def test_bridge_refs_wrong_type(self):
        rs=fully_typed(bridge_fixture())
        next(r for r in rs if r['type']=='Route')['status']='OPEN'
        next(r for r in rs if r['type']=='WitnessBundle')['bridge_links'][0]['assessment_ref']='ooc:fixture:t1'
        self.assert_problem(rs,'WRONG_NESTED_REF_TYPE')
    def test_review_only_route_evidence_rejected(self):
        rs=route_records()
        next(r for r in rs if r['id']=='ooc:fixture:e2')['evidence_class']='REVIEW'
        self.assert_problem(rs,'NONBIOLOGICAL_ROUTE_SUPPORT')
    def test_out_of_scope_assessment_does_not_poison_valid_route(self):
        rs=route_records()
        other=copy.deepcopy(next(r for r in rs if r['id']=='ooc:fixture:a2'))
        other['id']='ooc:fixture:other-scope'
        other['scope']={'adapter':'other'}
        rs.append(other)
        next(r for r in rs if r['id']=='ooc:fixture:t2')['evidence_assessment_refs'].append(other['id'])
        self.assertEqual(self.errors(rs),[])
    def test_same_scope_contradiction_blocks_route(self):
        rs=route_records()
        other=copy.deepcopy(next(r for r in rs if r['id']=='ooc:fixture:a2'))
        other['id']='ooc:fixture:contradiction'
        other['effect']='CONTRADICTS'
        rs.append(other)
        self.assert_problem(rs,'UNRESOLVED_ROUTE_CONTRADICTION')
    def test_cross_context_founder_rejected(self):
        rs=route_records()
        next(r for r in rs if r['type']=='FounderEnsemble')['context_ref']='ooc:fixture:wrong'
        self.assert_problem(rs,'ROUTE_FOUNDER_CONTEXT_MISMATCH')


if __name__ == '__main__':
    unittest.main()
