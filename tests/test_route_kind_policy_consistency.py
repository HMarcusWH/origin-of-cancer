"""Synthetic, schema-valid route-policy cross-consumer regressions.

These are engineering tests of evidence qualification, not cancer evidence.
"""
import copy
import unittest

from oocgraph import core
from oocgraph.admission.projection import project_current
from tests.test_pr5_review_repairs import CurrentStateAndCertificate, retract
from tests.test_routes_and_data import get


class RouteKindPolicyConsistency(unittest.TestCase):
    @staticmethod
    def fixture(claim_kind):
        records = CurrentStateAndCertificate().route_with_closure_verdict()
        route = get(records, 'r')
        route['claim_kind'] = claim_kind
        if claim_kind == 'HISTORICAL':
            # Every segment, founder handoff, and closure verdict remains
            # causally consistent while using the historical policy's
            # longitudinal/mixed and temporal evidence requirements.
            for name in ('a1', 'a2', 'closure-a'):
                get(records, name)['assessment_role'] = 'TEMPORAL'
            for name in ('e1', 'e2', 'closure-e'):
                get(records, name)['design_class'] = 'MIXED'
        return records

    def assert_positive_verdict(self, records):
        self.assertEqual(core.validate_records(records), [])
        self.assertEqual(core.resolve(records)['partitions'][0]['state'],
                         'SUPPORTED_SCOPED')
        view = project_current(records)
        verdict = next(q for q in view['qualifications']
                       if q['subject_ref'] == 'ooc:fixture:closure-verdict')
        self.assertEqual(verdict['decision'], 'ADMITTED')
        self.assertIn('ooc:fixture:closure-a', verdict['accepted_assessment_refs'])
        self.assertIn('ooc:fixture:closure-e', verdict['accepted_evidence_refs'])
        self.assertTrue(all(g['satisfied'] for g in verdict['required_groups']))

    def test_causal_route_closure_uses_route_policy(self):
        records = self.fixture('CAUSAL')
        self.assertEqual(core.route_evidence_policy_key(get(records, 'r')), 'ROUTE')
        self.assert_positive_verdict(records)

    def test_historical_route_closure_uses_historical_route_policy(self):
        records = self.fixture('HISTORICAL')
        self.assertEqual(core.route_evidence_policy_key(get(records, 'r')),
                         'HISTORICAL_ROUTE')
        self.assert_positive_verdict(records)

    def test_default_route_kind_preserves_legacy_causal_semantics(self):
        records = self.fixture('CAUSAL')
        del get(records, 'r')['claim_kind']
        self.assertEqual(core.route_evidence_policy_key(get(records, 'r')), 'ROUTE')
        self.assert_positive_verdict(records)

    def test_wrong_assessment_policy_does_not_qualify_closure_verdict(self):
        for route_kind, invalid_role in [('CAUSAL', 'TEMPORAL'),
                                         ('HISTORICAL', 'CAUSAL')]:
            with self.subTest(route_kind=route_kind):
                records = self.fixture(route_kind)
                get(records, 'closure-a')['assessment_role'] = invalid_role
                violations = core.validate_records(records)
                self.assertTrue(any('NONBIOLOGICAL_PROMOTION' in x
                                    for x in violations), violations)
                view = project_current(records)
                verdict = next(q for q in view['qualifications']
                               if q['subject_ref'] == 'ooc:fixture:closure-verdict')
                self.assertNotEqual(verdict['decision'], 'ADMITTED')

    def test_retracted_closure_evidence_contests_both_kinds(self):
        for kind in ('CAUSAL', 'HISTORICAL'):
            with self.subTest(kind=kind):
                records = self.fixture(kind)
                retract(records, 'ooc:fixture:closure-e',
                        name='withdraw-' + kind.lower())
                self.assertEqual(core.validate_records(records), [])
                self.assertEqual(core.resolve(records)['partitions'][0]['state'],
                                 'CONTESTED')
                view = project_current(records)
                verdict = next(q for q in view['qualifications']
                               if q['subject_ref'] == 'ooc:fixture:closure-verdict')
                self.assertEqual(verdict['decision'], 'CONTESTED')
                self.assertNotIn('ooc:fixture:closure-e',
                                 verdict['accepted_evidence_refs'])

    def test_surviving_alternative_support_preserves_both_kinds(self):
        for kind in ('CAUSAL', 'HISTORICAL'):
            with self.subTest(kind=kind):
                records = self.fixture(kind)
                evidence = copy.deepcopy(get(records, 'closure-e'))
                evidence['id'] = 'ooc:fixture:closure-e-alternative'
                assessment = copy.deepcopy(get(records, 'closure-a'))
                assessment['id'] = 'ooc:fixture:closure-a-alternative'
                assessment['evidence_ref'] = evidence['id']
                records.extend([evidence, assessment])
                get(records, 'closure-verdict')['assessment_refs'].append(
                    assessment['id'])
                retract(records, 'ooc:fixture:closure-e',
                        name='withdraw-alt-' + kind.lower())
                self.assertEqual(core.validate_records(records), [])
                self.assertEqual(core.resolve(records)['partitions'][0]['state'],
                                 'SUPPORTED_SCOPED')
                verdict = next(q for q in project_current(records)['qualifications']
                               if q['subject_ref'] == 'ooc:fixture:closure-verdict')
                self.assertEqual(verdict['decision'], 'ADMITTED')
                self.assertIn(assessment['id'], verdict['accepted_assessment_refs'])
                self.assertNotIn('ooc:fixture:closure-a',
                                 verdict['accepted_assessment_refs'])

    def test_unknown_route_kind_never_maps_to_valid_policy(self):
        self.assertIsNone(core.route_evidence_policy_key({'claim_kind': 'UNSUPPORTED'}))


if __name__ == '__main__':
    unittest.main()
