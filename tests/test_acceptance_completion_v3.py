"""Explicit, scenario-named acceptance tests for remaining high-risk v3 gates.

These are *synthetic engineering worlds*, not evidence for any cancer theory.
"""
import copy
import unittest
from oocgraph import core
from tests.test_integrity import node
from tests.test_production_contracts import mathematical_fixture, route_records, fully_typed
from tests.test_preemptive_origin import fixture as origin_fixture, append_withdrawal
from tests.test_preemptive_repair import statistical_freeze, add_statistical_negative
from tests.test_admission_v3 import FormalQualificationChecks
from tests.test_integrity import evidence_base, verdict


def find(rs,name):
    return next(x for x in rs if x['id']=='ooc:fixture:'+name)


class AcceptanceCompletionV3(unittest.TestCase):
    def test_FORM_005_cross_model_result_must_not_borrow_a_proof(self):
        rs=mathematical_fixture()
        good=find(rs,'math-result')
        verdict=find(rs,'math-verdict')
        # Even a PASS Result cannot certify a different model instance.
        other=copy.deepcopy(good)
        other.update(id='ooc:fixture:other-model-result', model_instance_ref='ooc:fixture:other-model')
        rs.append(other)
        verdict['result_refs']=[other['id']]
        self.assertIsNone(core._qualified_formal_verdict({r['id']:r for r in rs},verdict))
        self.assertTrue(any('UNVERIFIED_MATHEMATICAL_PROMOTION' in x for x in core.validate_records(rs)))

    def test_ROUT_005_three_segments_share_an_ancestry_witness(self):
        rs=route_records()
        state=copy.deepcopy(find(rs,'s3'))
        state['id']='ooc:fixture:s4'
        e=copy.deepcopy(find(rs,'e2'))
        e.update(id='ooc:fixture:e3')
        a=copy.deepcopy(find(rs,'a2'))
        a.update(id='ooc:fixture:a3',evidence_ref=e['id'],target_ref='ooc:fixture:t3')
        t=copy.deepcopy(find(rs,'t2'))
        t.update(id='ooc:fixture:t3',source_state_ref='ooc:fixture:s3',
                 target_state_ref=state['id'],evidence_assessment_refs=[a['id']])
        rs.extend(fully_typed([state,e,a,t]))
        find(rs,'r')['transition_refs'].append(t['id'])
        find(rs,'w')['evidence_refs'].append(e['id'])
        self.assertEqual(core.validate_records(rs),[])
        route=core.effective_route_state(rs,find(rs,'r'))
        self.assertEqual(route['effective'],'ADMITTED_CLOSED')
        self.assertEqual(len(route['witness_path']),3)

    def test_ROUT_012_ancestry_withdrawal_does_not_rewrite_closed_route(self):
        rs=route_records()
        old=copy.deepcopy(find(rs,'r'))
        append_withdrawal(rs,'e1')
        find(rs,'origin-withdrawal-notice')['source_locator_refs']=['ooc:fixture:l']
        self.assertEqual(core.validate_records(rs),[])
        self.assertEqual(find(rs,'r'),old)
        self.assertEqual(core.effective_route_state(rs,old,historical=True)['effective'],'ADMITTED_CLOSED')
        self.assertEqual(core.effective_route_state(rs,old)['effective'],'CONTESTED')

    def test_STAT_007_negative_audit_wrong_dataset_version_is_not_material(self):
        rs=statistical_freeze()
        _,assess=add_statistical_negative(rs)
        for a in assess:
            a['scope']={'dataset_versions':{'fixture':'WRONG_VERSION'}}
        self.assertTrue(core.effective_freeze_eligibility(rs,['ooc:fixture:g'])['effective_kernel_frozen'])

    def test_ORIG_003_entry_evidence_withdrawn_history_remains_valid(self):
        rs=origin_fixture(); old=copy.deepcopy(find(rs,'origin-verdict'))
        append_withdrawal(rs,'e1')
        self.assertEqual(core.validate_records(rs),[])
        self.assertEqual(find(rs,'origin-verdict'),old)
        self.assertEqual(core.resolve(rs)['partitions'][0]['state'],'CONTESTED')

    def test_ORIG_004_establishment_evidence_withdrawn_history_remains_valid(self):
        rs=origin_fixture(); old=copy.deepcopy(find(rs,'origin-verdict'))
        append_withdrawal(rs,'e2')
        self.assertEqual(core.validate_records(rs),[])
        self.assertEqual(find(rs,'origin-verdict'),old)
        self.assertEqual(core.resolve(rs)['partitions'][0]['state'],'CONTESTED')

    def test_REIN_011_irrelevant_append_does_not_change_retraction_state(self):
        rs=origin_fixture();append_withdrawal(rs,'e1')
        baseline=core.approved_retractions(rs)
        rs.append(fully_typed([node('EvidenceObject','unrelated',status='RECORDED',
            context_ref='ooc:fixture:c',source_locator_refs=['ooc:fixture:l'],
            evidence_class='PRIMARY_ANIMAL',claim_ceiling='BIOLOGICAL_CAUSAL_SCOPED',
            study_id='irrelevant-study',system_id='other',design_class='LONGITUDINAL',
            provenance_class='CURATED_SEMANTIC')])[0])
        self.assertEqual(core.approved_retractions(rs),baseline)

    def test_DOI_015_untyped_identifier_is_not_silently_verified(self):
        self.assertFalse(core._normalized_source_identifiers('1234567'))
        self.assertFalse(core._normalized_source_identifiers('PMC_not_an_id'))
        self.assertEqual(core._normalized_source_identifiers('PMID:1234567'),{'pmid:1234567'})

    def test_WHOL_002_unrelated_valid_evidence_does_not_revise_route(self):
        rs=route_records();before=core.effective_route_state(rs,find(rs,'r'))
        extra=copy.deepcopy(find(rs,'e2'))
        extra.update(id='ooc:fixture:unrelated',study_id='unrelated',witness_ids=['another'])
        rs.append(extra)
        self.assertEqual(core.effective_route_state(rs,find(rs,'r')),before)

    def test_STAT_014_negative_data_use_audit_contests_model_and_verdict(self):
        rs=FormalQualificationChecks().fixture_event()
        ref=lambda name:'ooc:fixture:'+name
        datasets=fully_typed([
            node('Dataset','independent-d1',family_id='same-audit-family',version='v1',
                 availability='synthetic',contains_patient_identifiers=False),
            node('Dataset','independent-d2',family_id='same-audit-family',version='v1',
                 availability='synthetic',contains_patient_identifiers=False)])
        uses=fully_typed([
            node('DataUse','independent-train',status='ADMITTED',model_instance_ref=ref('model'),
                 protocol_ref=ref('math-protocol'),dataset_ref=ref('independent-d1'),role='TRAIN',
                 partition_id='train',unit_keys=['A'],independence_status='DOCUMENTED_DISJOINT'),
            node('DataUse','independent-confirm',status='ADMITTED',model_instance_ref=ref('model'),
                 protocol_ref=ref('math-protocol'),dataset_ref=ref('independent-d2'),role='CONFIRM',
                 partition_id='confirm',unit_keys=['B'],independence_status='DOCUMENTED_DISJOINT')])
        rs.extend(datasets+uses)
        scope=core._data_pair_scope(uses[0],uses[1],{x['id']:x for x in datasets})
        positive=fully_typed([node('EvidenceObject','independent-good',status='RECORDED',
            context_ref=ref('math-context'),source_locator_refs=[ref('math-loc')],
            evidence_class='ANALYTIC',claim_ceiling='DATA_PARTITION_AUDIT',design_class='DATA_AUDIT',
            study_id='audit-study',system_id='partition',provenance_class='CURATED_SEMANTIC')])[0]
        rs.append(positive)
        for i,du in enumerate(uses):
            du['independence_evidence_refs']=[positive['id']]
            rs.append(fully_typed([node('EvidenceAssessment','independent-good-a'+str(i),
                status='ADJUDICATED',effect='SUPPORTS',assessment_role='INDEPENDENCE',
                target_ref=du['id'],evidence_ref=positive['id'],scope=scope,
                provenance_class='CURATED_SEMANTIC')])[0])
        model=find(rs,'model');model['frozen_digest']=core.model_identity_digest(rs,model)
        find(rs,'license')['basis_digest']=model['frozen_digest']
        self.assertEqual(core.validate_records(rs),[])
        self.assertEqual(core.effective_model_state(rs,model)['effective'],'ADMITTED')
        # Both pair members have a full, qualified negative assessment, but
        # different negative effects. This must revoke their current license.
        bad=copy.deepcopy(positive)
        bad.update(id=ref('independent-bad'),study_id='negative-audit')
        rs.append(bad)
        for i,(du,effect) in enumerate(zip(uses,['CONTRADICTS','FALSIFIES'])):
            rs.append(fully_typed([node('EvidenceAssessment','independent-bad-a'+str(i),
                status='ADJUDICATED',effect=effect,assessment_role='INDEPENDENCE',
                target_ref=du['id'],evidence_ref=bad['id'],scope=scope,
                provenance_class='CURATED_SEMANTIC')])[0])
        self.assertEqual(core.validate_records(rs),[])
        for use in uses:
            self.assertEqual(core.effective_data_use_state(rs,use)['effective'],'CONTESTED')
        self.assertEqual(core.effective_model_state(rs,model)['effective'],'CONTESTED')
        self.assertEqual(core.resolve(rs)['partitions'][0]['state'],'CONTESTED')

    def test_STAT_010_retracted_negative_audit_restores_uncontested_freeze_eligibility(self):
        rs=statistical_freeze()
        self.assertTrue(core.effective_freeze_eligibility(rs,['ooc:fixture:g'])['effective_kernel_frozen'])
        negative,_=add_statistical_negative(rs)
        self.assertFalse(core.effective_freeze_eligibility(rs,['ooc:fixture:g'])['effective_kernel_frozen'])
        append_withdrawal(rs,'negative-e')
        notice=find(rs,'origin-withdrawal-notice')
        support=find(rs,'freeze-e')
        notice['context_ref']=support['context_ref']
        notice['source_locator_refs']=support['source_locator_refs']
        self.assertEqual(core.validate_records(rs),[])
        self.assertIn(negative['id'],core.approved_retractions(rs))
        self.assertTrue(core.effective_freeze_eligibility(rs,['ooc:fixture:g'])['effective_kernel_frozen'])

    def test_ORIG_005_valid_origin_reinstatement_restores_every_mandatory_group(self):
        rs=origin_fixture()
        append_withdrawal(rs,'e1')
        self.assertEqual(core.resolve(rs)['partitions'][0]['state'],'CONTESTED')
        prior=find(rs,'origin-withdrawal')
        new_notice=copy.deepcopy(find(rs,'origin-withdrawal-notice'))
        new_notice.update(id='ooc:fixture:origin-restoration-notice',study_id='restoration-study')
        restoration=fully_typed([node('EvidenceAssessment','origin-restoration',
            status='ADJUDICATED',effect='REINSTATES',assessment_role='REASSESSMENT',
            target_ref=prior['id'],evidence_ref=new_notice['id'],authority_ref=prior['authority_ref'],
            scope=prior['scope'],rationale='Independent synthetic correction',
            limitations='Not real oncology evidence',provenance_class='CURATED_SEMANTIC')])[0]
        rs.extend([new_notice,restoration])
        self.assertEqual(core.validate_records(rs),[])
        self.assertNotIn('ooc:fixture:e1',core.approved_retractions(rs))
        self.assertEqual(core.resolve(rs)['partitions'][0]['state'],'SUPPORTED_SCOPED')

    def test_ORIG_011_historical_model_license_survives_new_negative_method_audit(self):
        rs=FormalQualificationChecks().fixture_event()
        model=find(rs,'model')
        old=copy.deepcopy(find(rs,'license'))
        self.assertEqual(core.effective_model_state(rs,model)['effective'],'ADMITTED')
        negative=fully_typed([node('EvidenceObject','new-model-negative',
            status='RECORDED',context_ref='ooc:fixture:math-context',
            source_locator_refs=['ooc:fixture:math-loc'],evidence_class='ANALYTIC',
            claim_ceiling='METHODOLOGICAL',design_class='DATA_AUDIT',
            study_id='model-review',system_id='method',provenance_class='CURATED_SEMANTIC')])[0]
        a=fully_typed([node('EvidenceAssessment','new-model-negative-a',status='ADJUDICATED',
            effect='CONTRADICTS',assessment_role='MODEL',target_ref=model['id'],
            evidence_ref=negative['id'],scope=model['scope'],
            rationale='Synthetic model challenge',provenance_class='CURATED_SEMANTIC')])[0]
        rs.extend([negative,a])
        self.assertEqual(core.validate_records(rs),[])
        self.assertEqual(find(rs,'license'),old)
        self.assertEqual(core.effective_model_state(rs,model)['effective'],'CONTESTED')

    def test_REIN_015_retraction_notice_cannot_be_mutated_after_adjudication(self):
        from tests.test_latest_codex import LatestCodexContracts
        rs=fully_typed(LatestCodexContracts().retracted_route_fixture())
        before=copy.deepcopy(rs)
        self.assertEqual(core.history_violations(before,rs),[])
        find(rs,'retraction-notice')['finding']='Rewritten notice after adjudication'
        self.assertTrue(any('MUTATED_ADMITTED_DEPENDENCY' in issue
                            for issue in core.history_violations(before,rs)))

    def test_WHOL_001_unrelated_verdict_remains_supported_after_scoped_retraction(self):
        rs=evidence_base('PRIMARY_ANIMAL')
        primary=verdict(decision='SUPPORTED_SCOPED',assessment_refs=['ooc:fixture:assessment'])
        rs.append(primary)
        second_claim=copy.deepcopy(find(rs,'claim'))
        second_claim.update(id='ooc:fixture:unrelated-claim',statement='Unrelated biology')
        second_e=copy.deepcopy(find(rs,'ev'))
        second_e.update(id='ooc:fixture:unrelated-ev',study_id='unrelated-study')
        second_a=copy.deepcopy(find(rs,'assessment'))
        second_a.update(id='ooc:fixture:unrelated-a',target_ref=second_claim['id'],
                        evidence_ref=second_e['id'])
        second_v=copy.deepcopy(primary)
        second_v.update(id='ooc:fixture:unrelated-verdict',subject_ref=second_claim['id'],
                        assessment_refs=[second_a['id']])
        rs.extend([second_claim,second_e,second_a,second_v])
        self.assertEqual(core.validate_records(rs),[])
        append_withdrawal(rs,'ev')
        notice=find(rs,'origin-withdrawal-notice')
        notice['context_ref']='ooc:fixture:context'
        notice['source_locator_refs']=['ooc:fixture:loc']
        self.assertEqual(core.validate_records(rs),[])
        partitions={p['partition'][0]:p['state'] for p in core.resolve(rs)['partitions']}
        self.assertEqual(partitions[second_claim['id']],'SUPPORTED_SCOPED')
        self.assertEqual(partitions[find(rs,'claim')['id']],'CONTESTED')

    def test_ORIG_009_invalid_origin_cannot_be_backfilled(self):
        from tests.test_admission_projection import HistoricalSnapshotContract
        HistoricalSnapshotContract().test_later_evidence_cannot_backfill_invalid_origin_issuance()

    def test_WHOL_014_preformalization_and_43_critical_gaps_are_not_promoted(self):
        from pathlib import Path
        root=Path(__file__).resolve().parents[1]
        records=core.read_graph(root)
        programme=next(r for r in records if r['type']=='Programme')
        self.assertEqual(programme['status'],'PRE_FORMALIZATION')
        self.assertFalse(programme['kernel_frozen'])
        self.assertEqual(sum(r['priority']=='CRITICAL' and r['status']=='OPEN'
                             for r in records if r['type']=='ResearchGap'),43)
        self.assertFalse([r for r in records if r['type'] in {'ModelInstance','Route','Verdict'}])

if __name__=='__main__': unittest.main()
