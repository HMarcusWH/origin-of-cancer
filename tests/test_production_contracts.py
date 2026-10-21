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
from tests.test_integrity import freeze_fixture, node
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
    def test_same_scope_contradiction_is_ingested_and_contests_route(self):
        from oocgraph.core import effective_route_state
        rs=route_records()
        other=copy.deepcopy(next(r for r in rs if r['id']=='ooc:fixture:a2'))
        other['id']='ooc:fixture:contradiction'
        other['effect']='CONTRADICTS'
        rs.append(other)
        self.assertEqual(self.errors(rs),[])
        route=next(r for r in rs if r['type']=='Route')
        state=effective_route_state(rs,route)
        self.assertEqual(state['effective'],'CONTESTED')
        self.assertEqual(state['contradiction_refs'],[other['id']])
    def test_cross_context_founder_rejected(self):
        rs=route_records()
        next(r for r in rs if r['type']=='FounderEnsemble')['context_ref']='ooc:fixture:wrong'
        self.assert_problem(rs,'ROUTE_FOUNDER_CONTEXT_MISMATCH')



def mathematical_fixture():
    """Fully typed formal chain for synthetic math proposition; not a cancer proof."""
    sc={'adapter':'synthetic-math'}
    ctx='ooc:fixture:math-context'
    refs=lambda key:'ooc:fixture:'+key
    records=[
        node('Context','math-context'),
        node('Claim','math-claim',scope=sc,status='PROVISIONAL',
             statement='Synthetic verification target',claim_kind='CERTIFICATE',
             modality='ASSERTION',empirical_admission='NOT_ESTABLISHED'),
        node('Authority','math-auth',status='ACTIVE_RULE',
             axes=['MATHEMATICAL_VERIFICATION'],scope=sc,empirical_truth_authority=False),
        node('SourceLocator','math-loc',path='README.md',selector={'fixture':'formal'}),
        node('SourceArtifact','proof-art',path='README.md',role='SYNTHETIC_PROOF',
             representation='synthetic',
             sha256=__import__('hashlib').sha256(
                 'Synthetic fixture — no biological claims\n'.encode('utf-8')).hexdigest()),
        node('Assumption','assumption',status='RECORDED',assessment='PASS',required=True,
             statement='Synthetic assumption',basis='test'),
        node('ModelClass','model-class',status='IMPLEMENTED_REFERENCE',cancer_backend_implemented=False),
        node('ValidityDomain','math-domain',context_ref=ctx,conditions=[]),
        node('Estimand','math-estimand',definition_obligation='Synthetic exact theorem'),
        node('Equation','equation',domain_ref=refs('math-domain'),
             assumption_refs=[refs('assumption')],variable_refs=[],
             expression='synthetic',source_locator_refs=[refs('math-loc')]),
        node('MethodApplicability','app',assessment='APPLICABLE',status='ACTIVE',
             domain_ref=refs('math-domain'),estimand_ref=refs('math-estimand'),
             model_class_ref=refs('model-class'),scope=sc,assumption_refs=[refs('assumption')],
             diagnostics=[],numerical_requirements=[],identification='fixture',
             limitations='synthetic',observation_adequacy='synthetic'),
        node('ModelInstance','model',status='FROZEN',identity_algorithm='ooc-model-digest-v2',
             context_ref=ctx,scope=sc,model_class_ref=refs('model-class'),
             applicability_ref=refs('app'),assumption_refs=[refs('assumption')],
             equation_refs=[refs('equation')],estimand_refs=[refs('math-estimand')],
             protocol_refs=[refs('math-protocol')],
             parameter_refs=[],state_variable_refs=[],boundary_conditions={},
             initial_conditions={},configuration={}),
        node('Gate','math-gate'),
        node('Protocol','math-protocol',status='ACTIVE',frozen=True,
             metrics=['exact synthetic claim'],null_refs=[],
             target_refs=[refs('math-claim')],revision_rule='new instance'),
        node('Test','math-test',status='PASSED',gate_ref=refs('math-gate'),
             protocol_ref=refs('math-protocol'),subject_ref=refs('math-claim')),
        node('Software','math-software',path='README.md',
             sha256=__import__('hashlib').sha256(
                 'Synthetic fixture — no biological claims\n'.encode('utf-8')).hexdigest(),
             runtime_role='REFERENCE_ONLY'),
        node('Execution','math-execution',status='COMPLETED',outcome='PASS',
             environment={},input_refs=[refs('model')],protocol_ref=refs('math-protocol'),
             model_instance_ref=refs('model'),software_ref=refs('math-software'),
             output_sha256='b'*64),
        node('Result','math-result',status='VALIDATED',outcome='PASS',
             claim_ceiling='MATHEMATICAL_EXACT',evidence_class='FORMAL',
             verification_mode='FORMAL_PROOF',verification_artifact_ref=refs('proof-art'),
             verification_receipt={
                 'statement_sha256':__import__('hashlib').sha256(
                     'Synthetic verification target'.encode('utf-8')).hexdigest(),
                 'artifact_sha256':__import__('hashlib').sha256(
                     'Synthetic fixture — no biological claims\n'.encode('utf-8')).hexdigest(),
                 'verifier_sha256':__import__('hashlib').sha256(
                     'Synthetic fixture — no biological claims\n'.encode('utf-8')).hexdigest(),
                 'execution_output_sha256':'b'*64,
                 'verifier_version':'synthetic-v0','outcome':'PASS'},
             model_instance_ref=refs('model'),subject_ref=refs('math-claim'),scope=sc,
             test_ref=refs('math-test'),execution_ref=refs('math-execution'),
             provenance_class='CURATED_SEMANTIC'),
        node('EvidenceObject','math-evidence',status='RECORDED',context_ref=ctx,
             claim_ceiling='MATHEMATICAL_EXACT',evidence_class='FORMAL',
             finding='Synthetic formal artifact',study_id='synthetic',system_id='math-fixture',
             uncertainty='Fixture only',result_ref=refs('math-result'),
             source_locator_refs=[refs('math-loc')],provenance_class='CURATED_SEMANTIC'),
        node('EvidenceAssessment','math-assessment',status='ADJUDICATED',
             target_ref=refs('math-claim'),evidence_ref=refs('math-evidence'),
             effect='SUPPORTS',scope=sc,rationale='Synthetic formal test',
             limitations='No biological import',provenance_class='CURATED_SEMANTIC'),
        node('Verdict','math-verdict',status='RECORDED',
             subject_ref=refs('math-claim'),authority_ref=refs('math-auth'),
             axis='MATHEMATICAL_VERIFICATION',facet='synthetic',
             decision='MATHEMATICALLY_VERIFIED_SCOPED',
             model_instance_ref=refs('model'),scope=sc,
             result_refs=[refs('math-result')],assessment_refs=[refs('math-assessment')],
             supersedes_refs=[],rationale='Synthetic exact chain')
    ]
    records=fully_typed(records)
    from oocgraph.core import model_identity_digest
    model=next(r for r in records if r['id']==refs('model'))
    model['frozen_digest']=model_identity_digest(records,model)
    return records


class MathematicalAdmissionContracts(ProductionValidation):
    """Every positive/negative passes the actual schema+semantic check."""
    def test_production_valid_mathematical_certificate(self):
        self.assertEqual(self.errors(mathematical_fixture()),[])
    def test_equation_assumption_missing_from_model_fails(self):
        records=mathematical_fixture()
        model=next(r for r in records if r['id']=='ooc:fixture:model')
        model['assumption_refs']=[]
        self.assert_problem(records,'UNDECLARED_EQUATION_ASSUMPTION')
    def test_equation_assumption_unknown_blocks_admitted_model(self):
        records=mathematical_fixture()
        a=next(r for r in records if r['id']=='ooc:fixture:assumption')
        a['assessment']='UNKNOWN'
        from oocgraph.core import model_identity_digest
        model=next(r for r in records if r['id']=='ooc:fixture:model')
        model['status']='ADMITTED'
        model['frozen_digest']=model_identity_digest(records,model)
        self.assert_problem(records,'FAILED_OR_UNKNOWN_MODEL_ASSUMPTION')
    def test_failed_formal_execution_blocks_mathematical_promotion(self):
        records=mathematical_fixture()
        exe=next(r for r in records if r['id']=='ooc:fixture:math-execution')
        exe['status']='FAILED'
        self.assert_problem(records,'UNVERIFIED_MATHEMATICAL_PROMOTION')
    def test_checker_byte_mismatch_blocks_formal_promotion(self):
        records=mathematical_fixture()
        software=next(x for x in records if x['type']=='Software')
        software['sha256']='a'*64
        self.assert_problem(records,'VERIFIER_SOFTWARE_BYTE_DRIFT')

    def test_execution_output_not_bound_blocks_formal_promotion(self):
        records=mathematical_fixture()
        result=next(x for x in records if x['type']=='Result')
        result['verification_receipt']['execution_output_sha256']='0'*64
        self.assert_problem(records,'UNVERIFIED_MATHEMATICAL_PROMOTION')

    def test_missing_proof_artifact_blocks_mathematical_promotion(self):
        records=mathematical_fixture()
        result=next(r for r in records if r['id']=='ooc:fixture:math-result')
        result.pop('verification_artifact_ref')
        self.assert_problem(records,'UNVERIFIED_MATHEMATICAL_PROMOTION')
    def test_formal_result_protocol_must_belong_to_model(self):
        records=mathematical_fixture()
        m=next(r for r in records if r['id']=='ooc:fixture:model')
        m['protocol_refs']=[]
        from oocgraph.core import model_identity_digest
        m['frozen_digest']=model_identity_digest(records,m)
        self.assert_problem(records,'UNVERIFIED_MATHEMATICAL_PROMOTION')

    def test_formal_protocol_must_target_exact_claim(self):
        records=mathematical_fixture()
        p=next(r for r in records if r['id']=='ooc:fixture:math-protocol')
        p['target_refs']=['ooc:fixture:model']
        from oocgraph.core import model_identity_digest
        m=next(r for r in records if r['id']=='ooc:fixture:model')
        m['frozen_digest']=model_identity_digest(records,m)
        self.assert_problem(records,'UNVERIFIED_MATHEMATICAL_PROMOTION')

    def test_inactive_applicability_blocks_admitted_model(self):
        records=mathematical_fixture()
        m=next(r for r in records if r['id']=='ooc:fixture:model')
        m['status']='ADMITTED'
        a=next(r for r in records if r['id']=='ooc:fixture:app')
        a['status']='RETIRED'
        from oocgraph.core import model_identity_digest
        m['frozen_digest']=model_identity_digest(records,m)
        self.assert_problem(records,'INACTIVE_MODEL_APPLICABILITY')

    def test_frozen_specification_can_retain_unknown_assumption(self):
        records=mathematical_fixture()
        records=[r for r in records if r['type'] not in {
            'Result','Verdict','Test','Execution','EvidenceObject','EvidenceAssessment'}]
        a=next(r for r in records if r['id']=='ooc:fixture:app')
        a['assessment']='UNKNOWN';a['status']='DRAFT'
        assumption=next(r for r in records if r['id']=='ooc:fixture:assumption')
        assumption['assessment']='UNKNOWN'
        from oocgraph.core import model_identity_digest
        m=next(r for r in records if r['id']=='ooc:fixture:model')
        m['frozen_digest']=model_identity_digest(records,m)
        self.assertEqual(self.errors(records),[])

    def test_null_target_changes_digest(self):
        from oocgraph.core import model_identity_digest
        records=mathematical_fixture()
        target=next(r for r in records if r['id']=='ooc:fixture:math-claim')
        null=node('NullModel','null',model_class_ref='ooc:fixture:model-class',
                  target_claim_ref=target['id'],discriminating_prediction='synthetic')
        records.append(fully_typed([null])[0])
        proto=next(r for r in records if r['id']=='ooc:fixture:math-protocol')
        proto['null_refs']=['ooc:fixture:null']
        model=next(r for r in records if r['id']=='ooc:fixture:model')
        before=model_identity_digest(records,model)
        target['statement']='Changed target'
        self.assertNotEqual(before,model_identity_digest(records,model))


if __name__ == '__main__':
    unittest.main()
