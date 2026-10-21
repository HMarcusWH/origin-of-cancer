"""Prevent witness compositing and construction/confirmation contamination."""
import unittest
from tests.test_integrity import node
from oocgraph.core import validate_records

def route_fixture(mode='SAME_SYSTEM'):
    """Synthetic mock objects, not empirical cancer findings."""
    scope={'adapter':'synthetic'}
    ctx='ooc:fixture:c'
    s1='ooc:fixture:s1'
    rs=[node('Adapter','a'),node('Context','c'),
        node('Boundary','b',context_ref=ctx,state_refs=[s1]),
        node('FounderEnsemble','f',context_ref=ctx,member_refs=[s1,'ooc:fixture:s2'],
             ancestry_assessment_refs=['ooc:fixture:fa']),
        node('BiologicalState','s1',context_ref=ctx),
        node('BiologicalState','s2',context_ref=ctx),
        node('BiologicalState','s3',context_ref=ctx),
        node('SourceLocator','l',selector={'figure':'fixture'}),
        node('EvidenceObject','e1',witness_ids=['system1'],source_locator_refs=['ooc:fixture:l'],
             context_ref=ctx,status='RECORDED',evidence_class='PRIMARY_ANIMAL',claim_ceiling='BIOLOGICAL_CAUSAL_SCOPED',
             design_class='MIXED',study_id='fixture-study',system_id='fixture-system',
             provenance_class='CURATED_SEMANTIC'),
        node('EvidenceObject','e2',witness_ids=['system1'],source_locator_refs=['ooc:fixture:l'],
             context_ref=ctx,status='RECORDED',evidence_class='PRIMARY_ANIMAL',claim_ceiling='BIOLOGICAL_CAUSAL_SCOPED',
             design_class='PERTURBATION',study_id='fixture-study',system_id='fixture-system',
             provenance_class='CURATED_SEMANTIC'),
        node('EvidenceAssessment','a1',evidence_ref='ooc:fixture:e1',target_ref='ooc:fixture:t1',
             effect='SUPPORTS',scope=scope,status='ADJUDICATED',assessment_role='CAUSAL',provenance_class='CURATED_SEMANTIC'),
        node('EvidenceAssessment','a2',evidence_ref='ooc:fixture:e2',target_ref='ooc:fixture:t2',
             effect='SUPPORTS',scope=scope,status='ADJUDICATED',assessment_role='CAUSAL',provenance_class='CURATED_SEMANTIC'),
        node('EvidenceAssessment','fa',evidence_ref='ooc:fixture:e1',target_ref='ooc:fixture:f',
             effect='SUPPORTS',scope=scope,status='ADJUDICATED',assessment_role='ANCESTRY',provenance_class='CURATED_SEMANTIC')]
    for i in (1,2):
        rs.append(node('Transition','t'+str(i),status='SUPPORTED_SCOPED',
                       source_state_ref=f'ooc:fixture:s{i}',target_state_ref=f'ooc:fixture:s{i+1}',
                       context_ref=ctx,adapter_ref='ooc:fixture:a',scope=scope,
                       evidence_assessment_refs=[f'ooc:fixture:a{i}']))
    rs.append(node('WitnessBundle','w',mode=mode,context_ref=ctx,
                   evidence_refs=['ooc:fixture:e1','ooc:fixture:e2'],common_witness_ids=['system1']))
    rs.append(node('Route','r',context_ref=ctx,adapter_ref='ooc:fixture:a',
                   boundary_ref='ooc:fixture:b',founder_ref='ooc:fixture:f',
                   transition_refs=['ooc:fixture:t1','ooc:fixture:t2'],
                   witness_bundle_ref='ooc:fixture:w',unresolved_segments=[],scope=scope,status='CLOSED'))
    return rs

def bridge_fixture():
    r=route_fixture('VALIDATED_BRIDGE')
    get(r,'e2')['witness_ids']=['system2']
    b=node('EvidenceObject','bridge',status='RECORDED',context_ref='ooc:fixture:c',
           source_locator_refs=['ooc:fixture:l'],witness_ids=['system1','system2'],
           evidence_class='PRIMARY_ANIMAL',claim_ceiling='BIOLOGICAL_CAUSAL_SCOPED',
           design_class='MIXED',study_id='fixture-study',system_id='fixture-system',
           witness_bridge_pairs=[{
             'from_study_id':'fixture-study','from_system_id':'fixture-system',
             'from_witness_id':'system1','to_study_id':'fixture-study',
             'to_system_id':'fixture-system','to_witness_id':'system2'
           }],provenance_class='CURATED_SEMANTIC')
    a=node('EvidenceAssessment','bridge-a',status='ADJUDICATED',evidence_ref=b['id'],
           target_ref='ooc:fixture:r',effect='SUPPORTS',scope={'adapter':'synthetic'},
           assessment_role='CAUSAL',provenance_class='CURATED_SEMANTIC')
    r.extend([b,a])
    get(r,'w')['bridge_evidence_refs']=[b['id']]
    get(r,'w')['bridge_links']=[{
        'from_transition_ref':'ooc:fixture:t1','to_transition_ref':'ooc:fixture:t2',
        'evidence_ref':b['id'],'assessment_ref':a['id'],
        'from_study_id':'fixture-study','from_system_id':'fixture-system',
        'to_study_id':'fixture-study','to_system_id':'fixture-system',
        'from_witness_id':'system1','to_witness_id':'system2'}]
    return r

def data_fixture():
    return [node('ModelInstance','m'),node('Protocol','p'),node('Dataset','d1',family_id='family'),node('Dataset','d2',family_id='family'),
      node('DataUse','u1',model_instance_ref='ooc:fixture:m',protocol_ref='ooc:fixture:p',dataset_ref='ooc:fixture:d1',role='TRAIN',partition_id='train',unit_keys=['A']),
      node('DataUse','u2',model_instance_ref='ooc:fixture:m',protocol_ref='ooc:fixture:p',dataset_ref='ooc:fixture:d2',role='CONFIRM',partition_id='confirm',unit_keys=['B'])]

def get(rs,id):return next(r for r in rs if r['id']=='ooc:fixture:'+id)

class RouteTests(unittest.TestCase):
    def has(self,rs,code):self.assertTrue(any(code in x for x in validate_records(rs)),validate_records(rs))
    def test_common_witness_route(self):self.assertEqual(validate_records(route_fixture()),[])
    def test_disjoint_witnesses_rejected(self):
        r=route_fixture();get(r,'e2')['witness_ids']=['system2'];self.has(r,'MISSING_COMMON_WITNESS')
    def test_same_witness_name_different_system_is_not_continuity(self):
        r=route_fixture();get(r,'e2')['system_id']='another-system'
        self.has(r,'MISSING_COMMON_WITNESS')
    def test_nested_founder_wrong_state_context_rejected(self):
        r=route_fixture()
        r.append(node('FounderEnsemble','nested',context_ref='ooc:fixture:c',
                      member_refs=['ooc:fixture:s1']))
        get(r,'f')['member_refs']=['ooc:fixture:nested']
        get(r,'s1')['context_ref']='ooc:fixture:other'
        self.has(r,'ROUTE_FOUNDER_CONTEXT_MISMATCH')
    def test_noncausal_observation_cannot_close_route(self):
        r=route_fixture()
        get(r,'e2')['claim_ceiling']='BIOLOGICAL_OBSERVATION'
        get(r,'e2')['design_class']='OBSERVATIONAL'
        get(r,'a2')['assessment_role']='OBSERVATION'
        self.has(r,'NONBIOLOGICAL_ROUTE_SUPPORT')

    def test_synthesis_is_not_closure(self):self.has(route_fixture('SYNTHESIS_ONLY'),'COMPOSITED_ROUTE')
    def test_bridge_needs_evidence(self):self.has(route_fixture('VALIDATED_BRIDGE'),'UNSUPPORTED_BRIDGE')
    def test_route_debt_blocks(self):
        r=route_fixture();get(r,'r')['unresolved_segments']=['handoff'];self.has(r,'ROUTE_HAS_DEBT')
    def test_empty_route_fails(self):
        r=route_fixture();get(r,'r')['transition_refs']=[];self.has(r,'EMPTY_CLOSED_ROUTE')
    def test_missing_founder_fails(self):
        r=route_fixture();del get(r,'r')['founder_ref'];self.has(r,'MISSING_ROUTE_ANCESTRY')
    def test_boundary_context_must_match(self):
        r=route_fixture();get(r,'b')['context_ref']='another-context'
        self.has(r,'ROUTE_BOUNDARY_CONTEXT_MISMATCH')
    def test_founder_context_must_match(self):
        r=route_fixture();get(r,'f')['context_ref']='another-context'
        self.has(r,'ROUTE_FOUNDER_CONTEXT_MISMATCH')
    def test_boundary_must_anchor_first_source_state(self):
        r=route_fixture();get(r,'b')['state_refs']=['ooc:fixture:s2']
        self.has(r,'ROUTE_BOUNDARY_NOT_ANCHORED')
    def test_founder_must_anchor_first_source_state(self):
        r=route_fixture();get(r,'f')['member_refs']=['ooc:fixture:s2']
        self.has(r,'ROUTE_FOUNDER_NOT_ANCHORED')
    def test_nested_cooperative_founder_allowed(self):
        r=route_fixture()
        nested=node('FounderEnsemble','nested',context_ref='ooc:fixture:c',
                    member_refs=['ooc:fixture:s1'])
        r.append(nested);get(r,'f')['member_refs']=[nested['id'],'ooc:fixture:s2']
        self.assertEqual(validate_records(r),[])
    def test_ancestry_requires_adjudicated_support(self):
        r=route_fixture();get(r,'f')['ancestry_assessment_refs']=[]
        self.has(r,'UNSUPPORTED_ROUTE_ANCESTRY')
    def test_ancestry_cannot_use_review(self):
        r=route_fixture();get(r,'e1')['evidence_class']='REVIEW'
        self.has(r,'INVALID_ROUTE_ANCESTRY_ASSESSMENT')
    def test_closed_route_requires_explicit_scope(self):
        r=route_fixture();del get(r,'r')['scope'];self.has(r,'MISSING_ROUTE_SCOPE')
    def test_route_assessment_scope_must_match(self):
        r=route_fixture();get(r,'a1')['scope']={'adapter':'other'};self.has(r,'UNSUPPORTED_ROUTE_SEGMENT')
    def test_context_mismatch(self):
        r=route_fixture();get(r,'t1')['context_ref']='ooc:fixture:different';self.has(r,'ROUTE_CONTEXT_MISMATCH')
    def test_inactive_transition_cannot_close_route(self):
        r=route_fixture();get(r,'t1')['status']='OPEN';self.has(r,'INACTIVE_ROUTE_TRANSITION')
    def test_broken_handoff(self):
        r=route_fixture();get(r,'t2')['source_state_ref']='ooc:fixture:s1';self.has(r,'BROKEN_ROUTE_HANDOFF')
    def test_segment_support_required(self):
        r=route_fixture();get(r,'t1')['evidence_assessment_refs']=[];self.has(r,'UNSUPPORTED_ROUTE_SEGMENT')
    def test_route_assessment_must_be_adjudicated(self):
        r=route_fixture();get(r,'a1')['status']='IN_REVIEW';self.has(r,'UNADJUDICATED_ROUTE_ASSESSMENT')
    def test_route_assessment_must_target_segment(self):
        r=route_fixture();get(r,'a1')['target_ref']='ooc:fixture:t2';self.has(r,'ROUTE_ASSESSMENT_TARGET_MISMATCH')
    def test_route_assessment_must_support(self):
        r=route_fixture();get(r,'a1')['effect']='CONTRADICTS';self.has(r,'NON_SUPPORTING_ROUTE_ASSESSMENT')
    def test_review_cannot_close_biological_route(self):
        r=route_fixture();get(r,'e2')['evidence_class']='REVIEW'
        self.has(r,'NONBIOLOGICAL_ROUTE_SUPPORT')
    def test_synthetic_cannot_close_biological_route(self):
        r=route_fixture();get(r,'e2')['evidence_class']='SYNTHETIC'
        self.has(r,'NONBIOLOGICAL_ROUTE_SUPPORT')
    def test_engineering_cannot_close_biological_route(self):
        r=route_fixture();get(r,'e2')['evidence_class']='ENGINEERING'
        self.has(r,'NONBIOLOGICAL_ROUTE_SUPPORT')
    def test_unrelated_witness_placeholder_does_not_close_route(self):
        r=route_fixture();get(r,'e2')['witness_ids']=['system2']
        phantom=node('EvidenceObject','phantom',context_ref='ooc:fixture:c',status='RECORDED',
                     source_locator_refs=['ooc:fixture:l'],evidence_class='PRIMARY_ANIMAL',
                     witness_ids=['system1','system2'],claim_ceiling='BIOLOGICAL_CAUSAL_SCOPED',
                     study_id='fixture-study',system_id='fixture-system',provenance_class='CURATED_SEMANTIC')
        r.append(phantom);get(r,'w')['evidence_refs'].append(phantom['id'])
        self.has(r,'MISSING_COMMON_WITNESS')
    def test_route_evidence_must_be_active(self):
        r=route_fixture();get(r,'e1')['status']='WITHDRAWN';self.has(r,'INACTIVE_ROUTE_EVIDENCE')
    def test_route_evidence_must_be_in_witness_bundle(self):
        r=route_fixture();get(r,'w')['evidence_refs']=['ooc:fixture:e2'];self.has(r,'ROUTE_EVIDENCE_OUTSIDE_WITNESS')
    def test_same_system_cannot_use_bridge_evidence_as_segment_support(self):
        r=route_fixture();get(r,'w')['evidence_refs']=['ooc:fixture:e2'];get(r,'w')['bridge_evidence_refs']=['ooc:fixture:e1']
        self.has(r,'ROUTE_EVIDENCE_OUTSIDE_WITNESS')
    def test_validated_bridge_requires_adjudicated_bridge_evidence(self):
        r=bridge_fixture();get(r,'bridge-a')['status']='IN_REVIEW'
        self.has(r,'INVALID_BRIDGE_LINK')
    def test_validated_bridge_rejects_wrong_context(self):
        r=bridge_fixture();get(r,'bridge')['context_ref']='ooc:fixture:other'
        self.has(r,'INVALID_BRIDGE_LINK')
    def test_validated_bridge_with_adjudication_is_allowed(self):
        self.assertEqual(validate_records(bridge_fixture()),[])
    def test_cross_study_bridge_requires_exact_identity_mapping(self):
        r=bridge_fixture()
        get(r,'e2')['study_id']='independent-study'
        get(r,'w')['bridge_links'][0]['to_study_id']='independent-study'
        get(r,'bridge')['witness_bridge_pairs'][0]['to_study_id']='independent-study'
        self.assertEqual(validate_records(r),[])
    def test_cross_study_bridge_rejects_name_only_matching(self):
        r=bridge_fixture()
        get(r,'e2')['study_id']='independent-study'
        self.has(r,'INVALID_BRIDGE_LINK')
    def test_bridge_evidence_requires_explicit_pair_mapping(self):
        r=bridge_fixture()
        get(r,'bridge')['witness_bridge_pairs']=[]
        self.has(r,'INVALID_BRIDGE_LINK')
    def test_bridged_route_unrelated_ancestry_witness_rejected(self):
        r=bridge_fixture()
        e=node('EvidenceObject','foreign-ancestry',status='RECORDED',
               context_ref='ooc:fixture:c',source_locator_refs=['ooc:fixture:l'],
               evidence_class='PRIMARY_ANIMAL',claim_ceiling='BIOLOGICAL_CAUSAL_SCOPED',
               design_class='LINEAGE',study_id='another-study',system_id='another-system',
               witness_ids=['system1'],provenance_class='CURATED_SEMANTIC')
        r.append(e);get(r,'fa')['evidence_ref']=e['id']
        get(r,'w')['evidence_refs'].append(e['id'])
        self.has(r,'ROUTE_ANCESTRY_WITNESS_MISMATCH')

    def test_bridge_must_link_adjacent_transitions(self):
        r=bridge_fixture();get(r,'w')['bridge_links'][0]['from_transition_ref']='ooc:fixture:t2'
        self.has(r,'UNRELATED_BRIDGE_LINK')
    def test_bridge_must_bind_declared_witnesses(self):
        r=bridge_fixture();get(r,'w')['bridge_links'][0]['to_witness_id']='unrelated'
        self.has(r,'INVALID_BRIDGE_LINK')
    def test_bridge_must_bind_primary_biological_evidence(self):
        r=bridge_fixture();get(r,'bridge')['evidence_class']='SYNTHETIC'
        self.has(r,'INVALID_BRIDGE_LINK')
    def test_bridge_must_bind_all_disjoint_handoffs(self):
        r=bridge_fixture();get(r,'w')['bridge_links']=[]
        self.has(r,'UNBRIDGED_WITNESS_HANDOFF')
    def test_bridge_cannot_include_unbound_evidence(self):
        r=bridge_fixture();get(r,'w')['bridge_evidence_refs'].append('ooc:fixture:e1')
        self.has(r,'UNBOUND_BRIDGE_EVIDENCE')
    def test_empty_common_witness_ids(self):
        r=route_fixture();get(r,'w')['common_witness_ids']=[];self.has(r,'MISSING_COMMON_WITNESS')
    def test_witness_context_mismatch(self):
        r=route_fixture();get(r,'w')['context_ref']='ooc:fixture:b';self.has(r,'WITNESS_CONTEXT_MISMATCH')

class DataUseTests(unittest.TestCase):
    def test_disjoint_proposed_use_allowed(self):self.assertEqual(validate_records(data_fixture()),[])
    def test_unit_overlap_across_family(self):
        r=data_fixture();get(r,'u2')['unit_keys']=['A'];self.assertTrue(any('DATA_USE_LEAKAGE' in x for x in validate_records(r)))
    def test_same_partition_leakage(self):
        r=data_fixture();get(r,'u2').update(dataset_ref='ooc:fixture:d1',partition_id='train');self.assertTrue(any('DATA_USE_LEAKAGE' in x for x in validate_records(r)))
    def test_unknown_independence_blocks_admission(self):
        r=data_fixture();get(r,'u1')['status']=get(r,'u2')['status']='ADMITTED';self.assertTrue(any('UNKNOWN_PARTITION_INDEPENDENCE' in x for x in validate_records(r)))
    def test_calibration_counts_as_construction(self):
        r=data_fixture();get(r,'u1')['role']='CALIBRATION';get(r,'u2')['unit_keys']=['A'];self.assertTrue(any('DATA_USE_LEAKAGE' in x for x in validate_records(r)))
    def test_selection_counts_as_construction(self):
        r=data_fixture();get(r,'u1')['role']='SELECT';get(r,'u2')['unit_keys']=['A'];self.assertTrue(any('DATA_USE_LEAKAGE' in x for x in validate_records(r)))
    def test_protocol_change_does_not_reset_data_independence(self):
        r=data_fixture();r.append(node('Protocol','p2'));get(r,'u2')['protocol_ref']='ooc:fixture:p2';get(r,'u2')['unit_keys']=['A']
        self.assertTrue(any('DATA_USE_LEAKAGE' in x for x in validate_records(r)))
    def test_cross_candidate_confirm_reuse_is_not_independent(self):
        r=data_fixture();r.append(node('ModelInstance','other'))
        get(r,'u2')['model_instance_ref']='ooc:fixture:other';get(r,'u2')['unit_keys']=['A']
        self.assertTrue(any('DATA_USE_LEAKAGE' in x for x in validate_records(r)))

class IndependenceEvidenceTests(unittest.TestCase):
    def setUp(self):
        self.records=data_fixture()
        self.a=get(self.records,'u1');self.b=get(self.records,'u2')
        self.a.update(status='ADMITTED',independence_status='DOCUMENTED_DISJOINT')
        self.b.update(status='ADMITTED',independence_status='DOCUMENTED_DISJOINT')
        get(self.records,'d1')['version']='fixture-v1'
        get(self.records,'d2')['version']='fixture-v1'
        scope={
            'data_use_refs':sorted([self.a['id'],self.b['id']]),
            'dataset_refs':sorted([self.a['dataset_ref'],self.b['dataset_ref']]),
            'dataset_versions':{self.a['id']:'fixture-v1',self.b['id']:'fixture-v1'},
            'partition_ids':{self.a['id']:'train',self.b['id']:'confirm'}
        }
        self.records.extend([
            node('Context','audit-context'),
            node('SourceLocator','audit-loc',selector={'audit':'synthetic'}),
            node('EvidenceObject','audit-e',status='RECORDED',context_ref='ooc:fixture:audit-context',
                 evidence_class='ANALYTIC',claim_ceiling='DATA_PARTITION_AUDIT',
                 design_class='DATA_AUDIT',study_id='synthetic',system_id='audit',
                 source_locator_refs=['ooc:fixture:audit-loc'],provenance_class='CURATED_SEMANTIC'),
            node('EvidenceAssessment','audit-a',status='ADJUDICATED',effect='SUPPORTS',
                 evidence_ref='ooc:fixture:audit-e',target_ref=self.a['id'],
                 assessment_role='INDEPENDENCE',scope=scope,provenance_class='CURATED_SEMANTIC'),
            node('EvidenceAssessment','audit-b',status='ADJUDICATED',effect='SUPPORTS',
                 evidence_ref='ooc:fixture:audit-e',target_ref=self.b['id'],
                 assessment_role='INDEPENDENCE',scope=scope,provenance_class='CURATED_SEMANTIC')
        ])
        self.a['independence_evidence_refs']=['ooc:fixture:audit-e']
        self.b['independence_evidence_refs']=['ooc:fixture:audit-e']
    def has(self,code):
        e=validate_records(self.records)
        self.assertTrue(any(code in x for x in e),e)
    def test_pair_specific_audit_accepted(self):
        self.assertEqual(validate_records(self.records),[])
    def test_withdrawn_audit_rejected(self):
        get(self.records,'audit-e')['status']='WITHDRAWN'
        self.has('UNKNOWN_PARTITION_INDEPENDENCE')
    def test_textual_audit_rejected(self):
        get(self.records,'audit-e')['provenance_class']='TEXTUAL_HINT'
        self.has('UNKNOWN_PARTITION_INDEPENDENCE')
    def test_wrong_audit_scope_rejected(self):
        get(self.records,'audit-a')['scope']={'adapter':'other'}
        self.has('UNKNOWN_PARTITION_INDEPENDENCE')
    def test_unadjudicated_pair_rejected(self):
        get(self.records,'audit-b')['status']='IN_REVIEW'
        self.has('UNKNOWN_PARTITION_INDEPENDENCE')
    def test_overlapping_units_never_accepted(self):
        self.b['unit_keys']=['A']
        self.has('DATA_USE_LEAKAGE')
    def test_cross_candidate_selection_family_rejected(self):
        self.records.append(node('ModelInstance','other'))
        self.b['model_instance_ref']='ooc:fixture:other'
        self.a['selection_family_id']=self.b['selection_family_id']='selection-a'
        self.b['independence_evidence_refs']=[]
        self.has('UNKNOWN_PARTITION_INDEPENDENCE')


if __name__=='__main__':unittest.main()
