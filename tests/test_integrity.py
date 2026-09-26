"""Adversarial engineering tests. Synthetic records are not cancer evidence."""
import copy
import json
from pathlib import Path
import random
import tempfile
import unittest
from oocgraph.core import (IntegrityError, canonical, loads, safe_path, read_graph,
    resolve, validate_records, validate_repository, history_violations, file_class, sha256)

ROOT=Path(__file__).resolve().parents[1]
def node(typ, name, **kw):
    status=kw.pop('status','OPEN')
    return dict(id='ooc:fixture:'+name,type=typ,label=name,status=status,
                schema_version='0.1.0',provenance_class='SYNTHETIC',**kw)
def verdict(name='v', decision='UNKNOWN', scope=None, **kw):
    return node('Verdict',name,subject_ref='ooc:fixture:claim',axis='BIOLOGICAL_SUPPORT',facet='test',
                scope={'adapter':'synthetic'} if scope is None else scope,decision=decision,
                authority_ref='ooc:fixture:authority',**kw)
def vbase(scope=None):
    return [node('Claim','claim'),node('Authority','authority',axes=['BIOLOGICAL_SUPPORT'],
      scope={'adapter':'synthetic'} if scope is None else scope)]
def evidence_base(cls='SYNTHETIC',scope=None):
    return vbase(scope)+[node('Context','context'),node('SourceLocator','loc',selector={'figure':'synthetic-fixture'}),
      node('EvidenceObject','ev',evidence_class=cls,source_locator_refs=['ooc:fixture:loc'],
           context_ref='ooc:fixture:context',witness_ids=['system-1'],status='RECORDED'),
      node('EvidenceAssessment','assessment',evidence_ref='ooc:fixture:ev',target_ref='ooc:fixture:claim',
           effect='SUPPORTS',scope={'adapter':'synthetic'} if scope is None else scope,status='ADJUDICATED')]

class StrictIO(unittest.TestCase):
    def test_duplicate_json_keys(self):
        with self.assertRaises(IntegrityError):loads('{"x":1,"x":2}')
    def test_nonfinite_nan(self):
        with self.assertRaises(IntegrityError):loads('{"x":NaN}')
    def test_nonfinite_infinity(self):
        with self.assertRaises(IntegrityError):loads('{"x":Infinity}')
    def test_malformed_json(self):
        with self.assertRaises(IntegrityError):loads('{')
    def test_canonical_order(self): self.assertEqual(canonical({'b':2,'a':1}),canonical({'a':1,'b':2}))
    def test_canonical_rejects_nan(self):
        with self.assertRaises(ValueError):canonical({'x':float('nan')})
    def test_safe_local_path(self):self.assertEqual(safe_path(ROOT,'README.md'),ROOT/'README.md')
    def test_reject_parent_path(self):
        with self.assertRaises(IntegrityError):safe_path(ROOT,'../outside')
    def test_reject_absolute_path(self):
        with self.assertRaises(IntegrityError):safe_path(ROOT,'/etc/passwd')
    def test_reject_windows_path(self):
        with self.assertRaises(IntegrityError):safe_path(ROOT,'C:\\secrets')
    def test_reject_null_path(self):
        with self.assertRaises(IntegrityError):safe_path(ROOT,'a\0b')
    def test_reject_empty_posix_components(self):
        with self.assertRaises(IntegrityError):safe_path(ROOT,'.')
        with self.assertRaises(IntegrityError):safe_path(ROOT,'./')
    def test_symlink_escape(self):
        with tempfile.TemporaryDirectory() as td:
            d=Path(td);(d/'escape').symlink_to('/tmp')
            with self.assertRaises(IntegrityError):safe_path(d,'escape/something')
    def test_unknown_file_type_fails(self):
        with self.assertRaises(IntegrityError):file_class('mystery.bin')
    def test_imported_python_is_reference(self):self.assertEqual(file_class('sources/methods/test.py')[1],'REFERENCE_ONLY')
    def test_generated_has_no_authority(self):self.assertEqual(file_class('generated/graph.json')[1],'NON_AUTHORITATIVE')

class BaselineTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):cls.records=loads((ROOT/'tests/fixtures/bootstrap_graph.json').read_text())
    def oftype(self,t):return [r for r in self.records if r['type']==t]
    def test_all_records_validate(self):self.assertEqual(validate_records(self.records,ROOT),[])
    def test_repository_validate(self):self.assertEqual(validate_repository(ROOT),[])
    def test_70_sources(self):self.assertEqual(len(self.oftype('LiteratureSource')),70)
    def test_duplicate_identifiers_preserved(self):
        aliases={r['legacy_id']:r['same_identifier_as'] for r in self.oftype('LiteratureSource') if 'same_identifier_as' in r}
        self.assertEqual(set(aliases),{'W41','W45'})
    def test_no_bibliographic_verification_fabricated(self):self.assertEqual(self.oftype('SourceVerification'),[])
    def test_no_papers_marked_extracted(self):self.assertFalse(any(r['extraction_status']=='EXTRACTED' for r in self.oftype('LiteratureSource')))
    def test_37_open_theories(self):
        self.assertEqual(len(self.oftype('Theory')),37);self.assertFalse(any(r['card_complete'] for r in self.oftype('Theory')))
    def test_all_91_gaps(self):self.assertEqual({r['legacy_id'] for r in self.oftype('ResearchGap')},{f'RG-{i:03}' for i in range(1,92)})
    def test_43_critical_gaps(self):self.assertEqual(sum(r['priority']=='CRITICAL' for r in self.oftype('ResearchGap')),43)
    def test_43_freeze_requirements(self):self.assertEqual(len(self.oftype('Requirement')),43)
    def test_86_workstreams(self):self.assertEqual(len(self.oftype('Workstream')),86)
    def test_six_adapters(self):self.assertEqual(len(self.oftype('Adapter')),6)
    def test_no_completed_adapters(self):self.assertFalse(any(r['dossier_complete'] for r in self.oftype('Adapter')))
    def test_13_mvcl_modules(self):self.assertEqual(len(self.oftype('MVCLModule')),13)
    def test_17_edges_not_origin_transitions(self):
        self.assertEqual(len(self.oftype('MVCLReference')),17);self.assertEqual(self.oftype('Transition'),[])
    def test_no_biological_evidence_fabricated(self):self.assertEqual(self.oftype('EvidenceObject'),[])
    def test_no_model_instance_fabricated(self):self.assertEqual(self.oftype('ModelInstance'),[])
    def test_no_biological_verdict_fabricated(self):self.assertEqual(self.oftype('Verdict'),[])
    def test_no_freeze_or_clinical_use(self):
        p=self.oftype('Programme')[0];self.assertFalse(p['kernel_frozen']);self.assertFalse(p['clinical_use'])
    def test_ten_unexecuted_global_falsifiers(self):
        fs=self.oftype('Falsifier');self.assertEqual(len(fs),10);self.assertTrue(all(r['status']=='REGISTERED_NOT_EXECUTED' for r in fs))
    def test_unrecognized_schema_field_rejected(self):
        rs=copy.deepcopy(self.records);rs[0]['magic_truth']=True
        self.assertTrue(any('SCHEMA' in x for x in validate_records(rs,ROOT)))
    def test_invalid_enum_rejected(self):
        rs=copy.deepcopy(self.records);next(r for r in rs if r['type']=='Claim')['status']='PROVED_CANCER'
        self.assertTrue(any('SCHEMA' in x for x in validate_records(rs,ROOT)))
    def test_lost_ref_rejected(self):
        rs=copy.deepcopy(self.records);rs[0]['source_locator_refs']=['ooc:absent:x']
        self.assertTrue(any('MISSING_REF' in x for x in validate_records(rs)))
    def test_duplicate_id_rejected(self):self.assertTrue(any('DUPLICATE_ID' in x for x in validate_records([self.records[0],self.records[0]])))

class FirewallTests(unittest.TestCase):
    def has(self,records,code):self.assertTrue(any(code in x for x in validate_records(records)),validate_records(records))
    def test_unbacked_verified_citation(self):self.has([node('LiteratureSource','s',bibliographic_verification='VERIFIED')],'UNBACKED_SOURCE_VERIFICATION')
    def test_evidence_must_have_locator(self):self.has([node('EvidenceObject','e')],'UNLOCATED_EVIDENCE')
    def test_bibliography_is_not_finding(self):
        self.has([node('SourceLocator','l',selector={'sheet':'Anchor Sources'}),node('EvidenceObject','e',source_locator_refs=['ooc:fixture:l'])],'BIBLIOGRAPHY_AS_FINDING')
    def test_hint_cannot_close(self):
        x=node('Claim','c');x.update(status='CLOSED',provenance_class='TEXTUAL_HINT');self.has([x],'TEXT_HINT_PROMOTION')
    def test_wrong_ref_type(self):
        self.has([node('Claim','c'),node('Test','t',gate_ref='ooc:fixture:c')],'WRONG_REF_TYPE')
    def test_owner_specific_ref_type(self):
        self.has([node('Claim','c'),node('Boundary','b',state_refs=['ooc:fixture:c'])],'WRONG_REF_TYPE:state_refs')
    def test_unassessed_support_edge(self):
        self.has([node('Claim','c'),node('Claim','d'),node('Relation','r',source='ooc:fixture:c',target='ooc:fixture:d',kind='SUPPORTS')],'UNASSESSED_EVIDENCE_EDGE')
    def test_mismatched_assessment(self):
        rs=evidence_base();rs.append(node('Relation','edge',source='ooc:fixture:claim',target='ooc:fixture:ev',kind='SUPPORTS',assessment_ref='ooc:fixture:assessment'))
        self.has(rs,'ASSESSMENT_EDGE_MISMATCH')
    def test_support_without_assessment_or_result(self):self.has(vbase()+[verdict(decision='SUPPORTED_SCOPED')],'UNSUPPORTED_PROMOTION')
    def test_synthetic_is_not_biological_support(self):self.has(evidence_base()+[verdict(decision='SUPPORTED_SCOPED',assessment_refs=['ooc:fixture:assessment'])],'NONBIOLOGICAL_PROMOTION')
    def test_review_is_not_primary(self):self.has(evidence_base('REVIEW')+[verdict(decision='SUPPORTED_SCOPED',assessment_refs=['ooc:fixture:assessment'])],'NONBIOLOGICAL_PROMOTION')
    def test_primary_scoped_assessment_accepted(self):
        self.assertEqual(validate_records(evidence_base('PRIMARY_ANIMAL')+[verdict(decision='SUPPORTED_SCOPED',assessment_refs=['ooc:fixture:assessment'])]),[])
    def test_in_review_assessment_cannot_promote(self):
        rs=evidence_base('PRIMARY_ANIMAL');next(r for r in rs if r['type']=='EvidenceAssessment')['status']='IN_REVIEW'
        self.has(rs+[verdict(decision='SUPPORTED_SCOPED',assessment_refs=['ooc:fixture:assessment'])],'NONBIOLOGICAL_PROMOTION')
    def test_withdrawn_evidence_cannot_promote(self):
        rs=evidence_base('PRIMARY_ANIMAL');next(r for r in rs if r['type']=='EvidenceObject')['status']='WITHDRAWN'
        self.has(rs+[verdict(decision='SUPPORTED_SCOPED',assessment_refs=['ooc:fixture:assessment'])],'NONBIOLOGICAL_PROMOTION')
    def test_animal_to_human_not_automatic(self):
        scope={'species':'human'};self.has(evidence_base('PRIMARY_ANIMAL',scope)+[verdict(scope=scope,decision='SUPPORTED_SCOPED',assessment_refs=['ooc:fixture:assessment'])],'NONHUMAN_TO_HUMAN_PROMOTION')
    def test_one_scope_not_pan_cancer(self):
        scope={'pan_cancer':True};self.has(evidence_base('PRIMARY_ANIMAL',scope)+[verdict(scope=scope,decision='SUPPORTED_SCOPED',assessment_refs=['ooc:fixture:assessment'])],'MISSING_CROSS_ADAPTER_DECISION')
    def test_authority_scope_mismatch(self):self.has(vbase()+[verdict(scope={'adapter':'different'})],'AUTHORITY_SCOPE_MISMATCH')
    def test_authority_axis_mismatch(self):
        v=verdict();v['axis']='VALIDATION';self.has(vbase()+[v],'AUTHORITY_AXIS_MISMATCH')
    def test_unadjudicated_gap_resolution(self):
        g=node('ResearchGap','g');g['status']='RESOLVED';self.has([g],'UNADJUDICATED_CLOSURE')
    def test_unscoped_requirement_bound(self):
        g=node('Requirement','g');g['status']='BOUNDED';self.has([g],'UNSCOPED_REQUIREMENT_BOUND')
    def test_fake_card_completion(self):self.has([node('Theory','t',card_complete=True)],'UNADJUDICATED_DOCUMENT_COMPLETION')
    def test_kernel_without_requirements(self):self.has([node('Programme','p',kernel_frozen=True)],'NO_FREEZE_REQUIREMENTS')
    def test_open_freeze_requirement(self):
        self.has([node('Programme','p',kernel_frozen=True),node('Requirement','q',subject_ref='ooc:fixture:p')],'OPEN_FREEZE_REQUIREMENT')
    def test_clinical_use_prohibited(self):self.has([node('Programme','p',clinical_use=True)],'CLINICAL_USE_OUT_OF_SCOPE')
    def test_missing_applicability_assumptions(self):self.has([node('MethodApplicability','a',assessment='APPLICABLE')],'MISSING_APPLICABILITY_ASSUMPTIONS')
    def test_failed_assumption_blocks_applicability(self):
        self.has([node('Assumption','s',assessment='FAIL',required=True),node('MethodApplicability','a',assessment='APPLICABLE',assumption_refs=['ooc:fixture:s'])],'FAILED_OR_UNKNOWN_REQUIRED_ASSUMPTION')
    def test_unknown_assumption_blocks_applicability(self):
        self.has([node('Assumption','s',assessment='UNKNOWN',required=True),node('MethodApplicability','a',assessment='APPLICABLE',assumption_refs=['ooc:fixture:s'])],'FAILED_OR_UNKNOWN_REQUIRED_ASSUMPTION')
    def test_optional_assumption_not_required(self):
        self.assertEqual(validate_records([node('Assumption','s',assessment='UNKNOWN',required=False),node('MethodApplicability','a',assessment='APPLICABLE',assumption_refs=['ooc:fixture:s'])]),[])
    def test_unlicensed_frozen_model(self):
        m=node('ModelInstance','m');m['status']='FROZEN';self.has([m],'UNLICENSED_MODEL')
    def test_missing_frozen_model_identity(self):
        m=node('ModelInstance','m');m['status']='FROZEN';self.has([m],'MISSING_MODEL_IDENTITY')
    def test_model_and_applicability_assumptions_must_match(self):
        from oocgraph.core import model_identity_digest
        a1=node('Assumption','a1',assessment='PASS',required=True)
        a2=node('Assumption','a2',assessment='PASS',required=True)
        mc=node('ModelClass','mc')
        app=node('MethodApplicability','app',assessment='APPLICABLE',assumption_refs=[a1['id']],
                 model_class_ref=mc['id'],scope={'adapter':'synthetic'})
        m=node('ModelInstance','m',status='FROZEN',applicability_ref=app['id'],model_class_ref=mc['id'],
               assumption_refs=[a2['id']],scope={'adapter':'synthetic'})
        rs=[a1,a2,mc,app,m];m['frozen_digest']=model_identity_digest(rs,m)
        self.has(rs,'APPLICABILITY_ASSUMPTION_MISMATCH')
    def test_critical_gap_must_target_programme_gate(self):
        p=node('Programme','p',kernel_frozen=False)
        g=node('ResearchGap','g',priority='CRITICAL')
        c=node('Claim','c')
        q=node('Requirement','q',gap_ref=g['id'],subject_ref=c['id'])
        self.has([p,g,c,q],'MISSING_CRITICAL_PROGRAMME_REQUIREMENT')

class ResolutionTests(unittest.TestCase):
    def test_no_verdict_is_unknown(self):self.assertEqual(resolve([])['missing_verdict_state'],'UNKNOWN')
    def test_single_partition(self):self.assertEqual(resolve([verdict()])['partitions'][0]['state'],'UNKNOWN')
    def test_newer_is_not_automatic_supersession(self):
        self.assertEqual(resolve([verdict('old'),verdict('new')])['conflict_count'],1)
    def test_explicit_supersession(self):
        rs=[verdict('old'),verdict('new',supersedes_refs=['ooc:fixture:old'])];x=resolve(rs)['partitions'][0]
        self.assertEqual(x['active_verdict_refs'],['ooc:fixture:new']);self.assertEqual(x['historical_verdict_refs'],['ooc:fixture:old'])
    def test_cross_scope_preserved(self):self.assertEqual(len(resolve([verdict(),verdict('v2',scope={'adapter':'other'})])['partitions']),2)
    def test_cross_facet_preserved(self):
        a=verdict();b=verdict('v2');b['facet']='different';self.assertEqual(len(resolve([a,b])['partitions']),2)
    def test_cross_scope_supersession_rejected(self):
        with self.assertRaises(IntegrityError):resolve([verdict('old'),verdict('new',scope={'adapter':'other'},supersedes_refs=['ooc:fixture:old'])])
    def test_unknown_supersession_rejected(self):
        with self.assertRaises(IntegrityError):resolve([verdict(supersedes_refs=['ooc:fixture:absent'])])
    def test_supersession_cycle(self):
        with self.assertRaises(IntegrityError):resolve([verdict('a',supersedes_refs=['ooc:fixture:b']),verdict('b',supersedes_refs=['ooc:fixture:a'])])
    def test_self_supersession(self):
        with self.assertRaises(IntegrityError):resolve([verdict(supersedes_refs=['ooc:fixture:v'])])
    def test_permutation_100_shuffles(self):
        rs=[verdict('a'),verdict('b',supersedes_refs=['ooc:fixture:a']),verdict('c',scope={'adapter':'other'})]
        expected=canonical(resolve(rs));rng=random.Random(381)
        for _ in range(100):rng.shuffle(rs);self.assertEqual(canonical(resolve(rs)),expected)
    def test_no_inferred_promotion(self):self.assertEqual(resolve([verdict()])['inferred_scientific_promotions'],0)

class HistoryTests(unittest.TestCase):
    def test_result_deletion_fails(self):self.assertTrue(history_violations([node('Result','x')],[]))
    def test_negative_result_mutation_fails(self):
        a=node('Result','x',negative_result=True);b={**a,'negative_result':False};self.assertTrue(history_violations([a],[b]))
    def test_verdict_mutation_fails(self):
        a=verdict();b={**a,'decision':'SUPPORTED_SCOPED'};self.assertTrue(history_violations([a],[b]))
    def test_frozen_model_mutation_fails(self):
        a=node('ModelInstance','m');a['status']='FROZEN';b={**a,'label':'renamed'};self.assertTrue(history_violations([a],[b]))
    def test_frozen_protocol_mutation_fails(self):
        a=node('Protocol','p',frozen=True);b={**a,'metrics':['changed']};self.assertTrue(history_violations([a],[b]))
    def test_adjudicated_assessment_mutation_fails(self):
        a=node('EvidenceAssessment','a',status='ADJUDICATED');b={**a,'effect':'CONTRADICTS'};self.assertTrue(history_violations([a],[b]))
    def test_draft_claim_may_evolve(self):
        a=node('Claim','x');b={**a,'label':'revised claim'};self.assertEqual(history_violations([a],[b]),[])
    def test_append_only_evidence_allowed(self):
        a=node('EvidenceObject','a');b=node('EvidenceObject','b');self.assertEqual(history_violations([a],[a,b]),[])

class ModelIdentityTests(unittest.TestCase):
    def test_parameter_change_changes_identity(self):
        from oocgraph.core import model_identity_digest
        p=node('Parameter','p',value=1);m=node('ModelInstance','m',parameter_refs=[p['id']])
        before=model_identity_digest([p,m],m);p['value']=2
        self.assertNotEqual(before,model_identity_digest([p,m],m))
    def test_status_change_not_identity_change(self):
        from oocgraph.core import model_identity_digest
        m=node('ModelInstance','m');before=model_identity_digest([m],m);m['status']='FROZEN'
        self.assertEqual(before,model_identity_digest([m],m))
    def test_digest_does_not_hash_itself(self):
        from oocgraph.core import model_identity_digest
        m=node('ModelInstance','m');before=model_identity_digest([m],m);m['frozen_digest']=before
        self.assertEqual(before,model_identity_digest([m],m))
    def test_digest_order_invariant(self):
        from oocgraph.core import model_identity_digest
        p=node('Parameter','p',value=1);m=node('ModelInstance','m',parameter_refs=[p['id']])
        self.assertEqual(model_identity_digest([p,m],m),model_identity_digest([m,p],m))
    def test_forged_digest_rejected(self):
        m=node('ModelInstance','m',frozen_digest='0'*64);m['status']='FROZEN'
        self.assertTrue(any('MODEL_IDENTITY_MISMATCH' in x for x in validate_records([m])))
    def test_data_use_change_changes_identity(self):
        from oocgraph.core import model_identity_digest
        m=node('ModelInstance','m')
        d=node('Dataset','d')
        p=node('Protocol','p')
        u=node('DataUse','u',model_instance_ref=m['id'],dataset_ref=d['id'],protocol_ref=p['id'],
               role='TRAIN',partition_id='train',unit_keys=['A'])
        rs=[m,d,p,u];before=model_identity_digest(rs,m);u['unit_keys']=['B']
        self.assertNotEqual(before,model_identity_digest(rs,m))

class QueryToolTests(unittest.TestCase):
    def test_relation_neighbor_expansion_includes_endpoints(self):
        from tools.query import expand_neighbors
        a=node('Claim','qa');b=node('Claim','qb')
        e=node('Relation','qe',source=a['id'],target=b['id'],kind='REQUIRES')
        got=expand_neighbors([a,b,e],[e])
        self.assertEqual({r['id'] for r in got},{a['id'],b['id'],e['id']})

if __name__=='__main__':
    unittest.main()
