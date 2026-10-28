"""Admission-kernel v2 regression and oracle tests, synthetic engineering only.

Every positive path is checked against a negative near-miss. None of these
fixtures constitutes a biological or mathematical finding about cancer.
"""
import copy
import itertools
import json
import os
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from oocgraph import core
from oocgraph.admission.evidence import qualify_groups, groups_satisfied
from oocgraph.admission.scope import scoped_claim_entails
from oocgraph.admission.history import snapshot, historical_obligations
from oocgraph.admission.route import has_ancestry_path
from oocgraph.admission.registry import registry_errors
from tests.test_integrity import node, evidence_base, verdict
from tests.test_production_contracts import mathematical_fixture, route_records, freeze_records, fully_typed
from tests.test_preemptive_origin import fixture as origin_fixture, append_withdrawal
from tests.test_preemptive_repair import add_statistical_negative, statistical_freeze

ROOT=Path(__file__).resolve().parents[1]

def get(records, ident):
    return next(r for r in records if r['id'] == 'ooc:fixture:' + ident)

def valid(records):
    return core.validate_records(records)

class TypedScopeChecks(unittest.TestCase):
    def test_restrictions(self):
        parent={'adapter':'lung','species':'human','population':['A','B']}
        for scope, expected in [
            (parent,True),({'adapter':'lung','species':'human','population':['A']},True),
            ({'adapter':'lung','species':'mouse','population':['A']},False),
            ({'adapter':'lung','species':'human'},False),
            ({**parent,'pan_cancer':True},False),
            ({**parent,'unknown_unreviewed_dimension':'x'},False),
        ]:
            with self.subTest(scope=scope):self.assertEqual(scoped_claim_entails(parent,scope),expected)
    def test_generic_capability_scope_not_promoted(self):
        rs=evidence_base('PRIMARY_HUMAN_LONGITUDINAL',{'species':'human','adapter':'lung'})
        claim=get(rs,'claim');claim['scope']={'species':'mouse','adapter':'lung'}
        rs.append(verdict(scope={'species':'human','adapter':'lung'},decision='SUPPORTED_SCOPED',
                          assessment_refs=['ooc:fixture:assessment']))
        self.assertTrue(any('SCIENTIFIC_VERDICT_SCOPE_ESCALATION' in e for e in valid(rs)))
    def test_generic_capability_same_scope(self):
        rs=evidence_base('PRIMARY_ANIMAL',{'adapter':'synthetic'})
        rs.append(verdict(decision='SUPPORTED_SCOPED',assessment_refs=['ooc:fixture:assessment']))
        self.assertEqual(valid(rs),[])
    def test_origin_verdict_scope_not_promoted(self):
        rs=origin_fixture();claim=get(rs,'origin-claim');ver=get(rs,'origin-verdict')
        claim['scope']={'adapter':'synthetic','species':'mouse'}
        ver['scope']={'adapter':'synthetic','species':'human'}
        get(rs,'origin-authority')['scope']=ver['scope']
        self.assertTrue(any('SCOPE_ESCALATION' in e or 'NONBIOLOGICAL_PROMOTION' in e
                            for e in valid(rs)))

    def test_explicit_stage_organism_and_lineage_restrictions_cannot_be_inferred(self):
        index={'ooc:fixture:c':{'type':'Context','species':'human','stage':'EARLY','tissue':'lung'}}
        evidence={'type':'EvidenceObject','context_ref':'ooc:fixture:c','evidence_class':'PRIMARY_HUMAN_LONGITUDINAL'}
        for scope in ({'species':'human','stage':'LATE'},
                      {'species':'human','organism':'homo_sapiens'},
                      {'species':'human','lineage':'LUNG_ADENO'}):
            with self.subTest(scope=scope):
                self.assertFalse(core._evidence_matches_scientific_scope(index,evidence,scope))
        self.assertTrue(core._evidence_matches_scientific_scope(
            index,evidence,{'species':'human','stage':'EARLY','tissue':'lung'}))

class GroupPolicyChecks(unittest.TestCase):
    def test_all_mandatory_some_alternative(self):
        groups=[('ENTRY','ANY',['e1','e2'],1),('ESTABLISH','ANY',['e3'],1)]
        res=qualify_groups(groups,lambda name, ref:ref in {'e2','e3'})
        self.assertTrue(groups_satisfied(res))
        self.assertEqual(res[0].accepted,('e2',))
    def test_missing_mandatory(self):
        res=qualify_groups([('ENTRY','ANY',['e1','e2'],1),('ESTABLISH','ANY',['e3'],1)],
                           lambda name,ref:ref=='e2')
        self.assertFalse(groups_satisfied(res))
    def test_at_least(self):
        rs=qualify_groups([('INDEPENDENT','AT_LEAST',['a','b','c'],2)],lambda g,r:r!='c')
        self.assertTrue(groups_satisfied(rs))
        self.assertFalse(groups_satisfied(qualify_groups(
            [('INDEPENDENT','AT_LEAST',['a','b','c'],3)],lambda g,r:r!='c')))
    def test_all(self):
        for passing in (set('ab'),set('a'),set()):
            res=qualify_groups([('ALL','ALL',['a','b'],2)],lambda g,r:r in passing)
            self.assertEqual(groups_satisfied(res),passing==set('ab'))

class RoutePathOracle(unittest.TestCase):
    def test_extra_witness_does_not_veto(self):
        rs=route_records()
        # All normal records carry witness A; add a second common B with
        # qualified segment evidence but no ancestry to B.
        get(rs,'e1')['witness_ids']=['A','B']
        get(rs,'e2')['witness_ids']=['A','B']
        get(rs,'w')['common_witness_ids']=['A','B']
        self.assertEqual(valid(rs),[])
        self.assertEqual(core.effective_route_state(rs,get(rs,'r'))['effective'],'ADMITTED_CLOSED')
    def test_disconnected_common_witness_denied(self):
        rs=route_records()
        get(rs,'e1')['witness_ids']=['A']
        get(rs,'e2')['witness_ids']=['B']
        get(rs,'w')['common_witness_ids']=['B']
        self.assertTrue(any('DISCONNECTED_ANCESTRY_WITNESS_PATH' in e or 'COMMON_WITNESS' in e
                            for e in valid(rs)))
    def test_small_graph_oracle_against_reachability(self):
        labels=[('s','x',x) for x in 'abc']
        for n in range(1,5):
            for start_mask in range(1,8):
                for end_mask in range(1,8):
                    a={labels[i] for i in range(3) if start_mask>>i&1}
                    b={labels[i] for i in range(3) if end_mask>>i&1}
                    seq=[a]* (n-1)+[b]
                    oracle=bool(a & set.intersection(*seq))
                    observed=has_ancestry_path(seq,a)
                    self.assertEqual(bool(observed),oracle)

class FormalQualificationChecks(unittest.TestCase):
    def fixture_event(self):
        rs=mathematical_fixture();m=get(rs,'model')
        get(rs,'math-auth')['axes'].append('EVIDENCE_POLICY')
        rs.append(fully_typed([node('EvidenceAssessment','license-a',
            status='ADJUDICATED',target_ref=m['id'],
            evidence_ref='ooc:fixture:math-evidence',effect='SUPPORTS',
            assessment_role='MODEL',scope=m['scope'],rationale='Synthetic',
            limitations='Not cancer evidence',provenance_class='CURATED_SEMANTIC')])[0])
        event=fully_typed([node('AuthorizationEvent','license',
            status='RECORDED',action='ADMIT_MODEL',subject_ref=m['id'],
            authority_ref='ooc:fixture:math-auth',scope=m['scope'],
            basis_refs=[m['id']],basis_digest=m['frozen_digest'],
            evidence_refs=['ooc:fixture:math-evidence'],
            provenance_class='CURATED_SEMANTIC')])[0]
        rs.append(event)
        return rs
    def test_exact_pass_supports_model_license_in_synthetic_only(self):
        self.assertEqual(valid(self.fixture_event()),[])
    def test_signed_fail_not_enough_for_model(self):
        rs=self.fixture_event();get(rs,'math-result')['outcome']='FAIL';get(rs,'math-result')['verification_receipt']['outcome']='FAIL'
        self.assertTrue(any('UNQUALIFIED_MODEL_ADMISSION' in e for e in valid(rs)))
    def test_current_formal_model_requalifies_same_signed_pass_chain(self):
        rs=self.fixture_event();model=get(rs,'model')
        self.assertEqual(core.effective_model_state(rs,model)['effective'],'ADMITTED')
        get(rs,'math-result')['outcome']='FAIL'
        get(rs,'math-result')['verification_receipt']['outcome']='FAIL'
        self.assertEqual(core.effective_model_state(rs,model)['effective'],'CONTESTED')

    def test_wrong_formal_subject_not_enough_for_model(self):
        rs=self.fixture_event();get(rs,'math-result')['subject_ref']='ooc:fixture:model'
        self.assertTrue(any('UNQUALIFIED_MODEL_ADMISSION' in e for e in valid(rs)))
    def test_exact_verified_counterclaim_contests_math_state(self):
        rs=mathematical_fixture()
        claim=copy.deepcopy(get(rs,'math-claim'))
        claim.update(id='ooc:fixture:math-counterclaim',statement='Synthetic opposite statement')
        protocol=copy.deepcopy(get(rs,'math-protocol'))
        protocol.update(id='ooc:fixture:counter-protocol',target_refs=[claim['id']])
        test=copy.deepcopy(get(rs,'math-test'))
        test.update(id='ooc:fixture:counter-test',protocol_ref=protocol['id'],
                    subject_ref=claim['id'],execution_ref='ooc:fixture:counter-execution')
        execution=copy.deepcopy(get(rs,'math-execution'))
        execution.update(id='ooc:fixture:counter-execution',protocol_ref=protocol['id'])
        result=copy.deepcopy(get(rs,'math-result'))
        result.update(id='ooc:fixture:counter-result',subject_ref=claim['id'],
                      test_ref=test['id'],execution_ref=execution['id'])
        receipt=result['verification_receipt']
        receipt['statement_sha256']=core.sha256(claim['statement'].encode())
        # The checker, not an unsigned EvidenceObject, must attest the relation.
        receipt['attestation_version']='OOC_FORMAL_PROOF_ATTESTATION_V3'
        receipt['counterproof_binding']={
            'target_id':get(rs,'math-claim')['id'],
            'counterclaim_id':claim['id'],
            'relation':'EXACT_NEGATION',
            'target_statement_sha256':core.sha256(
                get(rs,'math-claim')['statement'].encode()),
            'counterclaim_statement_sha256':core.sha256(claim['statement'].encode())}
        evidence=copy.deepcopy(get(rs,'math-evidence'))
        evidence.update(id='ooc:fixture:counter-evidence',result_ref=result['id'],
                        counterclaim_relation={'target_ref':get(rs,'math-claim')['id'],
                        'counterclaim_ref':claim['id'],'relation':'EXACT_NEGATION'})
        assessment=copy.deepcopy(get(rs,'math-assessment'))
        assessment.update(id='ooc:fixture:counter-assessment',effect='FALSIFIES',
                          evidence_ref=evidence['id'])
        rs.extend(fully_typed([claim,protocol,test,execution,result,evidence,assessment]))
        model=get(rs,'model');model['protocol_refs'].append(protocol['id'])
        model['frozen_digest']=core.model_identity_digest(rs,model)
        self.assertTrue(core._verified_result({x['id']:x for x in rs},result,claim['id'],claim['scope']))
        self.assertEqual(valid(rs),[])
        self.assertEqual(core.resolve(rs)['partitions'][0]['state'],'CONTESTED')

    def test_formal_label_without_counterproof_is_not_refutation(self):
        rs=mathematical_fixture();negative=copy.deepcopy(get(rs,'math-evidence'))
        negative['id']='ooc:fixture:negative-formal';negative.pop('result_ref',None)
        assessment=copy.deepcopy(get(rs,'math-assessment'))
        assessment.update(id='ooc:fixture:negative-formal-a',effect='FALSIFIES',
                          evidence_ref=negative['id'])
        rs.extend([negative,assessment])
        self.assertEqual(valid(rs),[])
        self.assertEqual(core.resolve(rs)['partitions'][0]['state'],'MATHEMATICALLY_VERIFIED_SCOPED')

class HistoryAndCurrentState(unittest.TestCase):
    def test_snapshot_changes_are_detected(self):
        rec=freeze_records();idx={x['id']:x for x in rec}
        basis=snapshot(rec,list(idx),subject_ref='ooc:fixture:p',asserted_scope={'adapter':'synthetic'},
            input_graph_tree_sha='a'*40,issuer_epoch='synthetic-only',
            obligation_inventory_refs=['ooc:fixture:q'],critical_gap_refs=['ooc:fixture:g'])
        event={'admission_basis':basis,'scope':{'adapter':'synthetic'},'subject_ref':'ooc:fixture:p'}
        self.assertEqual(len(historical_obligations(event)),len(rec))
        copy_event=copy.deepcopy(event)
        copy_event['admission_basis']['basis']['records'][0]['label']='tampered'
        self.assertIsNone(historical_obligations(copy_event))
    def test_new_requirement_does_not_change_basis(self):
        rs=freeze_records()
        first=snapshot(rs,[r['id'] for r in rs],subject_ref='ooc:fixture:p',
           asserted_scope={'domain':'PROGRAMME_GOVERNANCE'},issuer_epoch='synthetic-only',
           input_graph_tree_sha='b'*40,obligation_inventory_refs=['ooc:fixture:q'],
           critical_gap_refs=['ooc:fixture:g'])
        rs.append(node('Requirement','later',subject_ref='ooc:fixture:p',gap_ref='ooc:fixture:g',status='OPEN'))
        self.assertIsNotNone(historical_obligations({'admission_basis':first}))
        self.assertNotIn('ooc:fixture:later',historical_obligations({'admission_basis':first}))
        self.assertFalse(core.effective_freeze_eligibility(rs,['ooc:fixture:g'])['eligible'])
    def test_unpinned_production_basis_rejected(self):
        rs=freeze_records()
        event=fully_typed([node('AuthorizationEvent','auth-event',status='RECORDED',
                 action='FREEZE_KERNEL',subject_ref='ooc:fixture:p',
                 authority_ref='ooc:fixture:freeze-auth',
                 scope={'domain':'PROGRAMME_GOVERNANCE'},
                 basis_refs=['ooc:fixture:g','ooc:fixture:q'],
                 basis_digest=core.kernel_freeze_basis_digest(rs,['ooc:fixture:g','ooc:fixture:q']),
                 evidence_refs=[],provenance_class='CURATED_SEMANTIC')])[0]
        with tempfile.TemporaryDirectory() as folder:
            root=Path(folder);(root/'config').mkdir();(root/'config/project.json').write_text('{}')
            self.assertIsNone(core._event_admission_basis(rs,event,root,kind='FREEZE_KERNEL'))

class DataAndVerdictAlternatives(unittest.TestCase):
    def test_mixed_qualified_negative_pair_effects(self):
        rs=mathematical_fixture()
        ref=lambda x:'ooc:fixture:'+x
        datasets=[node('Dataset','pair-d1',family_id='same-family',version='v1',
                       availability='synthetic',contains_patient_identifiers=False),
                  node('Dataset','pair-d2',family_id='same-family',version='v1',
                       availability='synthetic',contains_patient_identifiers=False)]
        uses=[node('DataUse','pair-u1',status='ADMITTED',model_instance_ref=ref('model'),
                   protocol_ref=ref('math-protocol'),dataset_ref=ref('pair-d1'),role='TRAIN',
                   partition_id='train',unit_keys=['1'],independence_status='DOCUMENTED_DISJOINT'),
              node('DataUse','pair-u2',status='ADMITTED',model_instance_ref=ref('model'),
                   protocol_ref=ref('math-protocol'),dataset_ref=ref('pair-d2'),role='CONFIRM',
                   partition_id='confirm',unit_keys=['2'],independence_status='DOCUMENTED_DISJOINT')]
        rs.extend(fully_typed(datasets+uses))
        uses=[get(rs,'pair-u1'),get(rs,'pair-u2')]
        scope=core._data_pair_scope(uses[0],uses[1],{r['id']:r for r in datasets})
        evidence=[];assessments=[]
        for label, effects in [('positive',['SUPPORTS','SUPPORTS']),
                               ('negative',['CONTRADICTS','FALSIFIES'])]:
            e=node('EvidenceObject','pair-'+label,status='RECORDED',
                context_ref=ref('math-context'),source_locator_refs=[ref('math-loc')],
                evidence_class='ANALYTIC',claim_ceiling='DATA_PARTITION_AUDIT',
                design_class='DATA_AUDIT',study_id='study-'+label,system_id='independence',
                provenance_class='CURATED_SEMANTIC')
            evidence.append(e)
            for i,du in enumerate(uses):
                assessments.append(node('EvidenceAssessment',label+'-pair-a'+str(i),
                   status='ADJUDICATED',effect=effects[i],assessment_role='INDEPENDENCE',
                   target_ref=du['id'],evidence_ref=e['id'],scope=scope,
                   provenance_class='CURATED_SEMANTIC'))
        rs.extend(fully_typed(evidence+assessments))
        for du in uses:du['independence_evidence_refs']=[ref('pair-positive')]
        get(rs,'model')['frozen_digest']=core.model_identity_digest(rs,get(rs,'model'))
        self.assertEqual(valid(rs),[])
        for du in uses:
            self.assertEqual(core.effective_data_use_state(rs,du)['effective'],'CONTESTED')
        # Both effects are individually permitted, not required to be equal.
        get(rs,'negative-pair-a1')['effect']='CONTRADICTS'
        self.assertEqual(valid(rs),[])
        for du in uses:
            self.assertEqual(core.effective_data_use_state(rs,du)['effective'],'CONTESTED')
    def test_independent_verdict_alternative_survives(self):
        rs=evidence_base('PRIMARY_ANIMAL')
        e=copy.deepcopy(get(rs,'ev'));e.update(id='ooc:fixture:ev2',study_id='different-study')
        a=copy.deepcopy(get(rs,'assessment'));a.update(id='ooc:fixture:assessment2',evidence_ref=e['id'])
        rs.extend([e,a]);rs.append(verdict(decision='SUPPORTED_SCOPED',assessment_refs=[get(rs,'assessment')['id'],a['id']]))
        self.assertEqual(valid(rs),[])
        self.assertEqual(core.resolve(rs)['partitions'][0]['state'],'SUPPORTED_SCOPED')
        # Supplied retractions act on one source only, not all alternatives.
        from tests.test_preemptive_origin import append_withdrawal
        append_withdrawal(rs,target='ev')
        # Notice fixture references an existing context/locator compatible with
        # this graph after mapping the target.
        get(rs,'origin-withdrawal-notice')['context_ref']='ooc:fixture:context'
        get(rs,'origin-withdrawal-notice')['source_locator_refs']=['ooc:fixture:loc']
        self.assertEqual(core.resolve(rs)['partitions'][0]['state'],'SUPPORTED_SCOPED')
    def test_retracting_both_verdict_supports_contests(self):
        rs=evidence_base('PRIMARY_ANIMAL');rs.append(verdict(decision='SUPPORTED_SCOPED',assessment_refs=['ooc:fixture:assessment']))
        append_withdrawal(rs,target='ev')
        get(rs,'origin-withdrawal-notice')['context_ref']='ooc:fixture:context'
        get(rs,'origin-withdrawal-notice')['source_locator_refs']=['ooc:fixture:loc']
        self.assertEqual(core.resolve(rs)['partitions'][0]['state'],'CONTESTED')

class SinkInventory(unittest.TestCase):
    def test_current_registry_matches_schema(self):
        self.assertEqual(registry_errors(ROOT),[])
    def test_new_positive_status_requires_policy_record(self):
        with tempfile.TemporaryDirectory() as folder:
            tmp=Path(folder);(tmp/'schema').mkdir();(tmp/'config').mkdir()
            sc=json.loads((ROOT/'schema/graph-record.schema.json').read_text())
            sc['$defs']['Verdict']['properties']['decision']['enum'].append('SUPPORTED_UNREVIEWED')
            (tmp/'schema/graph-record.schema.json').write_text(json.dumps(sc))
            (tmp/'config/promotion_path_registry.json').write_bytes((ROOT/'config/promotion_path_registry.json').read_bytes())
            self.assertTrue(any('UNREGISTERED_SCIENTIFIC_PROMOTION' in s for s in registry_errors(tmp)))

if __name__=='__main__':unittest.main()
