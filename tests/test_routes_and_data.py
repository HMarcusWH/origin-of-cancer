"""Prevent witness compositing and construction/confirmation contamination."""
import unittest
from tests.test_integrity import node
from oocgraph.core import validate_records

def route_fixture(mode='SAME_SYSTEM'):
    scope={'adapter':'synthetic'}
    rs=[node('Adapter','a'),node('Context','c'),node('Boundary','b'),node('FounderEnsemble','f'),
        node('BiologicalState','s1'),node('BiologicalState','s2'),node('BiologicalState','s3'),
        node('SourceLocator','l',selector={'figure':'fixture'}),
        node('EvidenceObject','e1',witness_ids=['system1'],source_locator_refs=['ooc:fixture:l'],context_ref='ooc:fixture:c',status='RECORDED'),
        node('EvidenceObject','e2',witness_ids=['system1'],source_locator_refs=['ooc:fixture:l'],context_ref='ooc:fixture:c',status='RECORDED'),
        node('EvidenceAssessment','a1',evidence_ref='ooc:fixture:e1',target_ref='ooc:fixture:t1',effect='SUPPORTS',scope=scope,status='ADJUDICATED'),
        node('EvidenceAssessment','a2',evidence_ref='ooc:fixture:e2',target_ref='ooc:fixture:t2',effect='SUPPORTS',scope=scope,status='ADJUDICATED')]
    for i in (1,2):
        rs.append(node('Transition','t'+str(i),source_state_ref=f'ooc:fixture:s{i}',target_state_ref=f'ooc:fixture:s{i+1}',context_ref='ooc:fixture:c',adapter_ref='ooc:fixture:a',evidence_assessment_refs=[f'ooc:fixture:a{i}']))
    rs.append(node('WitnessBundle','w',mode=mode,context_ref='ooc:fixture:c',evidence_refs=['ooc:fixture:e1','ooc:fixture:e2'],common_witness_ids=['system1']))
    rr=node('Route','r',context_ref='ooc:fixture:c',adapter_ref='ooc:fixture:a',boundary_ref='ooc:fixture:b',founder_ref='ooc:fixture:f',transition_refs=['ooc:fixture:t1','ooc:fixture:t2'],witness_bundle_ref='ooc:fixture:w',unresolved_segments=[],scope=scope,status='CLOSED');rs.append(rr)
    return rs

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
    def test_synthesis_is_not_closure(self):self.has(route_fixture('SYNTHESIS_ONLY'),'COMPOSITED_ROUTE')
    def test_bridge_needs_evidence(self):self.has(route_fixture('VALIDATED_BRIDGE'),'UNSUPPORTED_BRIDGE')
    def test_route_debt_blocks(self):
        r=route_fixture();get(r,'r')['unresolved_segments']=['handoff'];self.has(r,'ROUTE_HAS_DEBT')
    def test_empty_route_fails(self):
        r=route_fixture();get(r,'r')['transition_refs']=[];self.has(r,'EMPTY_CLOSED_ROUTE')
    def test_missing_founder_fails(self):
        r=route_fixture();del get(r,'r')['founder_ref'];self.has(r,'MISSING_ROUTE_ANCESTRY')
    def test_context_mismatch(self):
        r=route_fixture();get(r,'t1')['context_ref']='ooc:fixture:different';self.has(r,'ROUTE_CONTEXT_MISMATCH')
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
    def test_route_evidence_must_be_active(self):
        r=route_fixture();get(r,'e1')['status']='WITHDRAWN';self.has(r,'INACTIVE_ROUTE_EVIDENCE')
    def test_route_evidence_must_be_in_witness_bundle(self):
        r=route_fixture();get(r,'w')['evidence_refs']=['ooc:fixture:e2'];self.has(r,'ROUTE_EVIDENCE_OUTSIDE_WITNESS')
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
    def test_different_candidate_reuse_explicit(self):
        r=data_fixture();r.append(node('ModelInstance','other'));get(r,'u2')['model_instance_ref']='ooc:fixture:other';get(r,'u2')['unit_keys']=['A'];self.assertEqual(validate_records(r),[])

if __name__=='__main__':unittest.main()
