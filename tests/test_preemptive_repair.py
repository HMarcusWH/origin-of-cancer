"""Adversarial tests for the 2026-10-27 PR2 contract.

These cases are synthetic engineering fixtures, never cancer or theorem evidence.
"""
import copy
import itertools
import json
import os
import random
import shutil
import tempfile
import unittest
from base64 import b64encode
from pathlib import Path
from urllib.parse import quote
from unittest.mock import patch

from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey
from cryptography.hazmat.primitives.serialization import Encoding, PublicFormat

from oocgraph import core
from tests.test_integrity import node
from tests.test_production_contracts import (
    mathematical_fixture, route_records, freeze_records, fully_typed,
)
from tests.test_routes_and_data import bridge_fixture

ROOT = Path(__file__).resolve().parents[1]


def byid(records, name):
    return next(r for r in records if r['id'] == 'ooc:fixture:' + name)


def make_root(path, with_project=False):
    (path / 'schema').mkdir(parents=True, exist_ok=True)
    for name in ('graph-record.schema.json','vocab.json','nested_reference_contract.json'):
        shutil.copy(ROOT / 'schema' / name, path / 'schema' / name)
    (path / 'README.md').write_text('Synthetic fixture — no biological claims\n')
    (path / 'verifier_output.txt').write_text('Synthetic checker transcript: PASS\n')
    if with_project:
        (path / 'config').mkdir(exist_ok=True)
        (path / 'config/project.json').write_text(json.dumps({'critical_gap_ids': []}))
    return path


def other_witness_route():
    rs = route_records()
    e = copy.deepcopy(byid(rs, 'e1'))
    e.update(id='ooc:fixture:extra-B', witness_ids=['B'])
    a = copy.deepcopy(byid(rs, 'a1'))
    a.update(id='ooc:fixture:assessment-B', evidence_ref=e['id'])
    byid(rs, 'e1')['witness_ids'] = ['A']
    byid(rs, 'e2')['witness_ids'] = ['B']
    byid(rs, 't1')['evidence_assessment_refs'].append(a['id'])
    byid(rs, 'w')['evidence_refs'].append(e['id'])
    byid(rs, 'w')['common_witness_ids'] = ['B']
    rs.extend(fully_typed([e,a]))
    return rs


def statistical_freeze():
    rs = freeze_records()
    for suffix in ('q','g'):
        byid(rs,suffix).update(obligation_domain='STATISTICAL',obligation_claim_kind='DATA_INDEPENDENCE')
    byid(rs,'freeze-e').update(evidence_class='ANALYTIC',design_class='DATA_AUDIT',claim_ceiling='DATA_PARTITION_AUDIT')
    for suffix in ('freeze-a','gap-a'):
        byid(rs,suffix)['assessment_role'] = 'INDEPENDENCE'
    return rs


def add_statistical_negative(rs, suffix='negative', targets=('q','g')):
    negative = copy.deepcopy(byid(rs,'freeze-e'))
    negative.update(id='ooc:fixture:'+suffix+'-e',finding='Evidence of partition overlap',study_id=suffix)
    additions=[negative]
    for x in targets:
        a=copy.deepcopy(byid(rs,'freeze-a' if x=='q' else 'gap-a'))
        a.update(id='ooc:fixture:'+suffix+'-'+x,evidence_ref=negative['id'],effect='CONTRADICTS')
        additions.append(a)
    rs.extend(fully_typed(additions))
    return byid(rs, suffix+'-e'), [byid(rs,suffix+'-'+x) for x in targets]


def signed_math(rs, root):
    result = next(r for r in rs if r['type']=='Result')
    index={r['id']:r for r in rs}
    software = next(r for r in rs if r['type']=='Software')
    software.update(runtime_role='FORMAL_PROOF_CHECKER',provenance_class='CURATED_SEMANTIC')
    signer='fixture-signing-authority'
    key=Ed25519PrivateKey.generate()
    result['verification_receipt'].update(attestation_version='OOC_FORMAL_PROOF_ATTESTATION_V2',attestation_signer_id=signer)
    registry={'trusted_checkers':[{'id':signer,'status':'ACTIVE',
       'verifier_sha256':software['sha256'],
       'verifier_version':result['verification_receipt']['verifier_version'],
       'public_key_base64':b64encode(key.public_key().public_bytes(Encoding.Raw,PublicFormat.Raw)).decode()}]}
    raw=json.dumps(registry).encode('utf-8')
    (root/'config/trusted_proof_checkers.json').write_bytes(raw)
    result['verification_receipt']['attestation_signature_b64'] = b64encode(
        key.sign(core.canonical(core.proof_attestation_payload(index,result)).encode())).decode()
    return result,key,core.sha256(raw)


class PreemptiveContracts(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = make_root(Path(self.tmp.name))
    def tearDown(self):
        self.tmp.cleanup()
    def assert_valid(self,records):
        self.assertEqual(core.validate_records(records,self.root), [])
    def test_route_all_ancestry_connected(self):
        rs=route_records()
        self.assert_valid(rs)
        self.assertEqual(core.effective_route_state(rs,byid(rs,'r'))['effective'],'ADMITTED_CLOSED')
    def test_route_rejects_disconnected_ancestry_despite_continuous_other_witness(self):
        rs=other_witness_route()
        errors=core.validate_records(rs,self.root)
        self.assertTrue(any('DISCONNECTED_ANCESTRY_WITNESS_PATH' in e for e in errors),errors)
        self.assertEqual(core.effective_route_state(rs,byid(rs,'r'))['effective'],'CONTESTED')
    def test_route_ancestry_alternative_can_recover_connected_path(self):
        rs=other_witness_route()
        e=copy.deepcopy(byid(rs,'extra-B'))
        a=copy.deepcopy(byid(rs,'fa'))
        e['id']='ooc:fixture:ancestry-B';a.update(id='ooc:fixture:founder-B',evidence_ref=e['id'])
        rs.extend(fully_typed([e,a]))
        byid(rs,'f')['ancestry_assessment_refs'].append(a['id'])
        byid(rs,'w')['evidence_refs'].append(e['id'])
        self.assert_valid(rs)
        self.assertEqual(core.effective_route_state(rs,byid(rs,'r'))['effective'],'ADMITTED_CLOSED')
    def test_valid_two_segment_bridge_still_closes(self):
        rs=fully_typed(bridge_fixture())
        self.assert_valid(rs)
        self.assertEqual(core.effective_route_state(rs,byid(rs,'r'))['effective'],'ADMITTED_CLOSED')
    def test_reversed_bridge_can_not_close(self):
        rs=fully_typed(bridge_fixture())
        link=byid(rs,'w')['bridge_links'][0]
        for left,right in [('from_study_id','to_study_id'),('from_system_id','to_system_id'),('from_witness_id','to_witness_id')]:
            link[left],link[right]=link[right],link[left]
        self.assertTrue(core.validate_records(rs,self.root))
        self.assertEqual(core.effective_route_state(rs,byid(rs,'r'))['effective'],'CONTESTED')
    def test_statistical_current_negative_vetoes_freeze(self):
        rs=statistical_freeze()
        self.assertTrue(core.effective_freeze_eligibility(rs,['ooc:fixture:g'])['effective_kernel_frozen'])
        add_statistical_negative(rs)
        self.assert_valid(rs)
        state=core.effective_freeze_eligibility(rs,['ooc:fixture:g'])
        self.assertFalse(state['effective_kernel_frozen'])
        self.assertIn('ooc:fixture:g',state['blocking_gap_refs'])
    def test_statistical_negative_one_obligation_suffices_to_block(self):
        for target in ('q','g'):
            with self.subTest(target=target):
                rs=statistical_freeze();add_statistical_negative(rs,targets=(target,))
                self.assert_valid(rs)
                self.assertFalse(core.effective_freeze_eligibility(rs,['ooc:fixture:g'])['effective_kernel_frozen'])
    def test_statistical_negative_wrong_scope_is_not_material(self):
        rs=statistical_freeze();_,assess=add_statistical_negative(rs)
        for a in assess:a['scope']={'unrelated':'adapter'}
        self.assertTrue(core.effective_freeze_eligibility(rs,['ooc:fixture:g'])['effective_kernel_frozen'])
    def test_statistical_unadjudicated_negative_is_not_material(self):
        rs=statistical_freeze();_,assess=add_statistical_negative(rs)
        for a in assess:a['status']='IN_REVIEW'
        self.assertTrue(core.effective_freeze_eligibility(rs,['ooc:fixture:g'])['effective_kernel_frozen'])
    def test_statistical_wrong_ceiling_is_not_material(self):
        rs=statistical_freeze();e,_=add_statistical_negative(rs)
        e['claim_ceiling']='VERIFICATION_ONLY'
        self.assertTrue(core.effective_freeze_eligibility(rs,['ooc:fixture:g'])['effective_kernel_frozen'])
    def test_mixed_proof_results_cannot_launder_signature(self):
        rs=mathematical_fixture()
        make_root(self.root,with_project=True)
        result,key,digest=signed_math(rs,self.root)
        verdict=next(r for r in rs if r['type']=='Verdict')
        invalid=copy.deepcopy(result)
        invalid.update(id='ooc:fixture:signed-failed-result',outcome='FAIL')
        invalid['verification_receipt']['outcome']='FAIL'
        # Sign the failing result, leaving the PASS result unsigned.
        result['verification_receipt'].pop('attestation_signature_b64')
        index={r['id']:r for r in rs};index[invalid['id']]=invalid
        invalid['verification_receipt']['attestation_signature_b64']=b64encode(
            key.sign(core.canonical(core.proof_attestation_payload(index,invalid)).encode())).decode()
        rs.append(invalid)
        verdict['result_refs'].append(invalid['id'])
        with patch.dict(os.environ,{'OOC_TRUST_POLICY_SHA256':digest}):
            self.assertTrue(any('UNVERIFIED_MATHEMATICAL_PROMOTION' in x for x in core.validate_records(rs,self.root)))
            self.assertIsNone(core._qualified_formal_verdict({r['id']:r for r in rs},verdict,self.root))
    def test_exact_signed_result_is_admissible_with_unrelated_non_support_result(self):
        rs=mathematical_fixture()
        (self.root/'config').mkdir(); (self.root/'config/project.json').write_text('{"critical_gap_ids":[]}')
        result,key,digest=signed_math(rs,self.root)
        verdict=next(r for r in rs if r['type']=='Verdict')
        unrelated=copy.deepcopy(result)
        unrelated.update(id='ooc:fixture:unrelated-result',outcome='FAIL')
        unrelated['verification_receipt']['outcome']='FAIL'
        unrelated['verification_receipt'].pop('attestation_signature_b64')
        rs.append(unrelated);verdict['result_refs'].append(unrelated['id'])
        with patch.dict(os.environ,{'OOC_TRUST_POLICY_SHA256':digest}):
            self.assert_valid(rs)
    def test_source_w61_full_identifier_and_url_percent_encoding(self):
        source=next(json.loads(l) for l in (ROOT/'graph/literature_sources.jsonl').read_text().splitlines()
                    if '"id":"ooc:source:W61"' in l)
        full=source['identifiers_raw'].split('; PMID')[0]
        for url in ('https://doi.org/'+full,
                    'https://doi.org/'+quote(full,safe='/')):
            with self.subTest(url=url):
                receipt={'identifier_checked':full,'canonical_metadata':{'doi':full},'public_source_url':url}
                self.assertTrue(core._source_verification_consistent(source,receipt))
        prefix='10.1002/1097-0142(195309)6:5'
        self.assertFalse(core._source_verification_consistent(
            source,{'identifier_checked':prefix,'canonical_metadata':{'doi':prefix},
                    'public_source_url':'https://doi.org/'+prefix}))
    def test_w61_complete_and_prefix_end_to_end(self):
        source=next(json.loads(l) for l in (ROOT/'graph/literature_sources.jsonl').read_text().splitlines()
                    if '"id":"ooc:source:W61"' in l)
        raw=source['identifiers_raw'];full=raw.split('; PMID')[0]
        for doi,expected in ((full,True),('10.1002/1097-0142(195309)6:5',False)):
            with self.subTest(doi=doi):
                rs=fully_typed([
                    node('LiteratureSource','W61',identifiers_raw=raw,bibliographic_verification='UNVERIFIED',extraction_status='REGISTERED_NOT_EXTRACTED'),
                    node('SourceVerification','W61-verification',status='VERIFIED',
                         source_ref='ooc:fixture:W61',identifier_checked=doi,
                         verification_scope='BIBLIOGRAPHIC_METADATA',
                         canonical_metadata={'doi':doi},public_source_url='https://doi.org/'+doi,
                         provenance_class='CURATED_SEMANTIC')])
                errors=core.validate_records(rs,self.root)
                self.assertEqual(not errors,expected)
    def test_reinstatement_fixed_point_is_record_and_id_order_invariant(self):
        history={'E':['R_E'],'N':['R_N']}
        for i in range(12):
            names=['x_A','y_G','z_E'];random.Random(i).shuffle(names)
            idx={names[0]:{'type':'EvidenceAssessment','evidence_ref':'N'},names[1]:{'type':'EvidenceAssessment','evidence_ref':'G'},
                 names[2]:{'type':'EvidenceAssessment','evidence_ref':'E'}}
            restored={'R_E':[names[0],names[1]],'R_N':[names[2]]}
            idx.update({x:{'type':'EvidenceObject'} for x in ('E','N','G')})
            with patch.object(core,'_authorized_retractions',return_value=history), \
                 patch.object(core,'_historical_reinstatements',return_value=restored):
                got=core.approved_reinstatements([],idx)
            self.assertEqual(set(got),{'R_E','R_N'})
    def test_ungrounded_reinstatement_cycle_never_bootstraps(self):
        hist={'E':['R_E'],'N':['R_N']}
        idx={'fromN':{'type':'EvidenceAssessment','evidence_ref':'N'},'fromE':{'type':'EvidenceAssessment','evidence_ref':'E'}}
        idx.update({x:{'type':'EvidenceObject'} for x in ('E','N')})
        with patch.object(core,'_authorized_retractions',return_value=hist), \
             patch.object(core,'_historical_reinstatements',return_value={'R_E':['fromN'],'R_N':['fromE']}):
            self.assertEqual(core.approved_reinstatements([],idx),{})
    def test_reinstatement_matches_independent_subset_oracle(self):
        """Brute-force least supported fixed point, independent of production loop."""
        rng=random.Random(31)
        names=['E'+str(i) for i in range(5)]
        hist={e:['R'+e] for e in names}
        for attempt in range(45):
            idx={'notice'+str(i):{'type':'EvidenceAssessment','evidence_ref':rng.choice(names+['GROUND'])}
                 for i in range(9)}
            cands={r:[k for k in idx if rng.choice([True,False])]
                   for r in ['R'+e for e in names]}
            idx.update({x:{'type':'EvidenceObject'} for x in names+['GROUND']})
            # An independently enumerated truth table finds the least fixed point:
            events=set('R'+e for e in names)
            fixed=[]
            for size in range(6):
                for group in itertools.combinations(sorted(events),size):
                    selected=set(group)
                    derivable={r for r in events if any(
                        not ({'R'+idx[k]['evidence_ref']} if idx[k]['evidence_ref'] in names else set())-selected
                        for k in cands[r])}
                    if derivable==selected:fixed.append(selected)
            expected=min(fixed,key=lambda x:(len(x),sorted(x)))
            with patch.object(core,'_authorized_retractions',return_value=hist), \
                 patch.object(core,'_historical_reinstatements',return_value=cands):
                actual=set(core.approved_reinstatements([],idx))
            self.assertEqual(actual,expected,attempt)
    def test_critical_research_baseline_is_unchanged(self):
        from oocgraph.core import read_graph
        records=read_graph(ROOT)
        gaps=[r for r in records if r.get('type')=='ResearchGap' and r.get('priority')=='CRITICAL']
        self.assertEqual(len(gaps),43)
        self.assertTrue(all(r.get('status')=='OPEN' for r in gaps))
        prog=next(r for r in records if r.get('type')=='Programme')
        self.assertFalse(prog.get('kernel_frozen'))
        self.assertFalse(prog.get('clinical_use'))
        self.assertEqual(len([r for r in records if r.get('type')=='Route' and r.get('status')=='CLOSED']),0)


def _registered_identifier_case(source):
    def check(self):
        raw=source['identifiers_raw']
        tokens=core._normalized_source_identifiers(raw)
        if raw.startswith('IARC '):
            self.assertEqual(tokens,set())
            return
        self.assertTrue(tokens,(source['id'],raw))
        # Typed PMID is a separate token, never swallowed by a punctuation-bearing DOI.
        if '; PMID ' in raw:
            self.assertIn('pmid:'+raw.split('; PMID ',1)[1].split(';')[0],tokens)
        if raw.startswith('10.'):
            complete=raw.split('; PMID',1)[0]
            self.assertIn('doi:'+complete.lower(),tokens)
    return check

for record in map(json.loads,(ROOT/'graph/literature_sources.jsonl').read_text().splitlines()):
    method_name='test_registered_identifier_'+record['id'].rsplit(':',1)[1].lower()
    setattr(PreemptiveContracts,method_name,_registered_identifier_case(record))

if __name__=='__main__':unittest.main()

# Each necessary formal predicate receives an independent one-field mutation.
# Dynamic methods are real unittest cases, counted and run separately.
def _formal_mutation(name, mutation):
    def check(self):
        rs=mathematical_fixture()
        make_root(self.root,with_project=True)
        result,key,digest=signed_math(rs,self.root)
        index={r['id']:r for r in rs}
        verdict=next(r for r in rs if r['type']=='Verdict')
        mutation(rs,index,result,verdict)
        with patch.dict(os.environ,{'OOC_TRUST_POLICY_SHA256':digest}):
            self.assertIsNone(core._qualified_formal_verdict(index,verdict,self.root),name)
            errors=core.validate_records(rs,self.root)
            self.assertTrue(any('UNVERIFIED_MATHEMATICAL_PROMOTION' in x
                            or x.startswith('SCHEMA:') for x in errors),
                            (name,errors))
    return check

_FORMAL_MUTATIONS = {
    'fail_result': lambda rs,i,r,v:r.update(outcome='FAIL'),
    'result_in_review':lambda rs,i,r,v:r.update(status='IN_REVIEW'),
    'test_not_passed':lambda rs,i,r,v:i[r['test_ref']].update(status='FAILED'),
    'execution_failed':lambda rs,i,r,v:i[r['execution_ref']].update(outcome='FAIL'),
    'execution_not_complete':lambda rs,i,r,v:i[r['execution_ref']].update(status='FAILED'),
    'protocol_not_frozen':lambda rs,i,r,v:i[i[r['test_ref']]['protocol_ref']].update(frozen=False),
    'protocol_inactive':lambda rs,i,r,v:i[i[r['test_ref']]['protocol_ref']].update(status='RETIRED'),
    'protocol_wrong_target':lambda rs,i,r,v:i[i[r['test_ref']]['protocol_ref']].update(target_refs=[]),
    'result_wrong_subject':lambda rs,i,r,v:r.update(subject_ref='ooc:fixture:math-gate'),
    'result_wrong_model':lambda rs,i,r,v:r.update(model_instance_ref='ooc:fixture:math-gate'),
    'result_wrong_scope':lambda rs,i,r,v:r.update(scope={'adapter':'other-model'}),
    'test_wrong_subject':lambda rs,i,r,v:i[r['test_ref']].update(subject_ref='ooc:fixture:math-gate'),
    'test_wrong_execution':lambda rs,i,r,v:i[r['test_ref']].update(execution_ref='ooc:fixture:math-gate'),
    'receipt_outcome_fail':lambda rs,i,r,v:r['verification_receipt'].update(outcome='FAIL'),
    'receipt_signer_changed':lambda rs,i,r,v:r['verification_receipt'].update(attestation_signer_id='unauthorized'),
    'receipt_version_changed':lambda rs,i,r,v:r['verification_receipt'].update(attestation_version='UNSIGNED'),
    'signature_tampered':lambda rs,i,r,v:r['verification_receipt'].update(attestation_signature_b64='AA=='),
    'model_not_frozen':lambda rs,i,r,v:i[r['model_instance_ref']].update(status='DRAFT'),
    'claim_statement_changed':lambda rs,i,r,v:i[r['subject_ref']].update(statement='Different theorem'),
    'proof_digest_changed':lambda rs,i,r,v:i[r['verification_artifact_ref']].update(sha256='0'*64),
    'checker_digest_changed':lambda rs,i,r,v:i[i[r['execution_ref']]['software_ref']].update(sha256='0'*64),
}
for name, mutate in _FORMAL_MUTATIONS.items():
    setattr(PreemptiveContracts, 'test_formal_mutation_'+name,
            _formal_mutation(name,mutate))


def _route_mutation(name,mutation):
    def check(self):
        rs=route_records()
        mutation(rs)
        errors=core.validate_records(rs,self.root)
        state=core.effective_route_state(rs,byid(rs,'r'))
        self.assertTrue(errors or state['effective']=='CONTESTED',(name,errors,state))
    return check

_ROUTE_MUTATIONS={
    'second_study_changed':lambda rs:byid(rs,'e2').update(study_id='other-study'),
    'second_system_changed':lambda rs:byid(rs,'e2').update(system_id='other-system'),
    'second_witness_changed':lambda rs:byid(rs,'e2').update(witness_ids=['other']),
    'founder_witness_missing':lambda rs:byid(rs,'fa').update(evidence_ref='ooc:fixture:e2'),
    'founder_assessments_removed':lambda rs:byid(rs,'f').update(ancestry_assessment_refs=[]),
    'common_witness_declared_extra':lambda rs:byid(rs,'w').update(common_witness_ids=['system1','absent']),
    'first_segment_support_removed':lambda rs:byid(rs,'t1').update(evidence_assessment_refs=[]),
    'second_segment_support_removed':lambda rs:byid(rs,'t2').update(evidence_assessment_refs=[]),
    'break_state_handoff':lambda rs:byid(rs,'t2').update(source_state_ref='ooc:fixture:s1'),
    'route_unrelated_context':lambda rs:byid(rs,'r').update(context_ref='ooc:fixture:missing'),
    'incorrect_scope':lambda rs:byid(rs,'t2').update(scope={'adapter':'different'}),
    'inactive_transition':lambda rs:byid(rs,'t2').update(status='REJECTED'),
}
for name, mutate in _ROUTE_MUTATIONS.items():
    setattr(PreemptiveContracts,'test_route_mutation_'+name,_route_mutation(name,mutate))


def _statistical_mutation(name,mutation,should_block):
    def check(self):
        rs=statistical_freeze()
        e, assessments=add_statistical_negative(rs)
        mutation(rs,e,assessments)
        state=core.effective_freeze_eligibility(rs,['ooc:fixture:g'])
        self.assertEqual(state['effective_kernel_frozen'], not should_block,
                         (name,state['gap_states'],state['requirement_states']))
    return check

_STATISTICAL_MUTATIONS={
    'negative_supports_not_contradicts':(lambda rs,e,a:[x.update(effect='SUPPORTS') for x in a],False),
    'negative_unadjudicated':(lambda rs,e,a:[x.update(status='IN_REVIEW') for x in a],False),
    'negative_wrong_role':(lambda rs,e,a:[x.update(assessment_role='OBSERVATION') for x in a],False),
    'negative_wrong_evidence_class':(lambda rs,e,a:e.update(evidence_class='REVIEW'),False),
    'negative_wrong_design':(lambda rs,e,a:e.update(design_class='OBSERVATIONAL'),False),
    'negative_wrong_ceiling':(lambda rs,e,a:e.update(claim_ceiling='METHODOLOGICAL'),False),
    'negative_wrong_scope':(lambda rs,e,a:[x.update(scope={'adapter':'foreign'}) for x in a],False),
    'negative_wrong_target':(lambda rs,e,a:[x.update(target_ref='ooc:fixture:freeze-e') for x in a],False),
    'negative_falsifies_exact':(lambda rs,e,a:[x.update(effect='FALSIFIES') for x in a],True),
    'negative_contradicts_exact':(lambda rs,e,a:None,True),
}
for name,(mutate,blocks) in _STATISTICAL_MUTATIONS.items():
    setattr(PreemptiveContracts,'test_statistical_policy_'+name,
            _statistical_mutation(name,mutate,blocks))


def _doi_case(name,change,expected):
    def check(self):
        source=next(json.loads(l) for l in (ROOT/'graph/literature_sources.jsonl').read_text().splitlines()
                    if '"id":"ooc:source:W61"' in l)
        complete=source['identifiers_raw'].split('; PMID')[0]
        receipt={'identifier_checked':complete,'canonical_metadata':{'doi':complete},
                 'public_source_url':'https://doi.org/'+complete}
        change(receipt,complete)
        self.assertEqual(core._source_verification_consistent(source,receipt),expected,name)
    return check

_DOI_VARIANTS={
    'correct_mixed_case':(lambda r,c:r.update(identifier_checked=c.upper(),canonical_metadata={'doi':c.upper()},public_source_url='https://doi.org/'+c.upper()),True),
    'correct_encoded_resolver':(lambda r,c:r.update(public_source_url='https://doi.org/'+quote(c,safe='/')),True),
    'wrong_doi_metadata':(lambda r,c:r.update(canonical_metadata={'doi':'10.1000/unrelated'}),False),
    'wrong_doi_url':(lambda r,c:r.update(public_source_url='https://doi.org/10.1000/unrelated'),False),
    'truncated_checked_identifier':(lambda r,c:r.update(identifier_checked=c.split('<')[0]),False),
    'truncated_metadata_doi':(lambda r,c:r.update(canonical_metadata={'doi':c.split('<')[0]}),False),
    'truncated_doi_resolver':(lambda r,c:r.update(public_source_url='https://doi.org/'+c.split('<')[0]),False),
    'wrong_pmids':(lambda r,c:r.update(canonical_metadata={'doi':c,'pmid':'999'}),False),
    'correct_pmid_companion':(lambda r,c:r.update(canonical_metadata={'doi':c,'pmid':'13094644'}),True),
    'invalid_percent_url':(lambda r,c:r.update(public_source_url='https://doi.org/'+c+'%ZZ'),False),
}
for name,(mutate,expected) in _DOI_VARIANTS.items():
    setattr(PreemptiveContracts,'test_doi_variant_'+name,
            _doi_case(name,mutate,expected))

def _three_segment_bridge():
    rs=fully_typed(bridge_fixture())
    e3=copy.deepcopy(byid(rs,'e2'))
    e3.update(id='ooc:fixture:e3',witness_ids=['system3'],system_id='fixture-system')
    a3=copy.deepcopy(byid(rs,'a2'))
    a3.update(id='ooc:fixture:a3',target_ref='ooc:fixture:t3',evidence_ref=e3['id'])
    t3=copy.deepcopy(byid(rs,'t2'))
    t3.update(id='ooc:fixture:t3',source_state_ref='ooc:fixture:s3',
              target_state_ref='ooc:fixture:s4',evidence_assessment_refs=[a3['id']])
    s4=copy.deepcopy(byid(rs,'s3'));s4['id']='ooc:fixture:s4'
    be=copy.deepcopy(byid(rs,'bridge'))
    be.update(id='ooc:fixture:bridge2',witness_ids=['system2','system3'],
              witness_bridge_pairs=[{
                  'from_study_id':'fixture-study','from_system_id':'fixture-system',
                  'from_witness_id':'system2','to_study_id':'fixture-study',
                  'to_system_id':'fixture-system','to_witness_id':'system3'}])
    ba=copy.deepcopy(byid(rs,'bridge-a'))
    ba.update(id='ooc:fixture:bridge2-a',evidence_ref=be['id'])
    rs.extend(fully_typed([e3,a3,t3,s4,be,ba]))
    byid(rs,'r')['transition_refs'].append(t3['id'])
    bundle=byid(rs,'w')
    bundle['evidence_refs'].append(e3['id'])
    bundle['bridge_evidence_refs'].append(be['id'])
    bundle['bridge_links'].append({
        'from_transition_ref':'ooc:fixture:t2',
        'to_transition_ref':'ooc:fixture:t3',
        'from_study_id':'fixture-study','from_system_id':'fixture-system',
        'from_witness_id':'system2','to_study_id':'fixture-study',
        'to_system_id':'fixture-system','to_witness_id':'system3',
        'evidence_ref':be['id'],'assessment_ref':ba['id']})
    return rs


def _test_three_segment_positive(self):
    rs=_three_segment_bridge()
    self.assert_valid(rs)
    self.assertEqual(core.effective_route_state(rs,byid(rs,'r'))['effective'],'ADMITTED_CLOSED')

def _test_three_segment_missing_link(self):
    rs=_three_segment_bridge()
    byid(rs,'w')['bridge_links'].pop()
    self.assertTrue(any('UNBRIDGED_WITNESS_HANDOFF' in x or
                        'DISCONNECTED_ANCESTRY_WITNESS_PATH' in x
                        for x in core.validate_records(rs,self.root)))
    self.assertEqual(core.effective_route_state(rs,byid(rs,'r'))['effective'],'CONTESTED')

def _test_three_segment_wrong_link(self):
    rs=_three_segment_bridge()
    byid(rs,'w')['bridge_links'][-1]['from_witness_id']='system1'
    self.assertTrue(core.validate_records(rs,self.root))
    self.assertEqual(core.effective_route_state(rs,byid(rs,'r'))['effective'],'CONTESTED')

setattr(PreemptiveContracts,'test_three_segment_bridge_valid',_test_three_segment_positive)
setattr(PreemptiveContracts,'test_three_segment_bridge_missing_second_link',_test_three_segment_missing_link)
setattr(PreemptiveContracts,'test_three_segment_bridge_invalid_second_link',_test_three_segment_wrong_link)
