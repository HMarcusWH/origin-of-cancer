"""Finite known-truth checks distinguish mathematical estimands, not cancer labels."""
import itertools
import math
import random
import unittest
from modeling.finite_chain import (validate, first_entry_distribution as hit,
    uninterrupted_persistence as persist, occupation_fraction as occupy, strongly_lumpable)
from modeling.branching_reference import eventual_survival_probability as survival_probability

class FiniteChainTests(unittest.TestCase):
    def test_absorbing_hit(self):self.assertEqual(hit([[0,1],[0,1]],[1,0],{1},3)['first_entry_probabilities'],[0,1,0,0])
    def test_initial_target_hit(self):self.assertEqual(hit([[1,0],[0,1]],[0,1],{1},0)['target_by_horizon'],1)
    def test_no_entry(self):self.assertEqual(hit([[1,0],[0,1]],[1,0],{1},5)['target_by_horizon'],0)
    def test_geometric_hit_distribution(self):
        x=hit([[.5,.5],[0,1]],[1,0],{1},4);self.assertEqual(x['first_entry_probabilities'],[0,.5,.25,.125,.0625])
    def test_target_and_competing_mass(self):
        x=hit([[0,.4,.6],[0,1,0],[0,0,1]],[1,0,0],{1},5,{2})
        self.assertAlmostEqual(x['target_by_horizon'],.4);self.assertAlmostEqual(x['competing_by_horizon'],.6);self.assertEqual(x['unresolved_at_horizon'],0)
    def test_competing_prevents_later_hit(self):
        x=hit([[0,1,0],[0,0,1],[0,0,1]],[1,0,0],{2},3,{1})
        self.assertEqual(x['target_by_horizon'],0);self.assertEqual(x['competing_by_horizon'],1)
    def test_initial_competing(self):
        x=hit([[1,0],[0,1]],[0,1],{0},0,{1});self.assertEqual(x['competing_by_horizon'],1)
    def test_unresolved_is_not_zero(self):
        x=hit([[.5,.5],[0,1]],[1,0],{1},2);self.assertEqual(x['unresolved_at_horizon'],.25)
    def test_empty_target(self):self.assertEqual(hit([[1]],[1],set(),2)['unresolved_at_horizon'],1)
    def test_full_region_persistence(self):self.assertAlmostEqual(persist([[.5,.5],[.3,.7]],[.2,.8],{0,1},4),1)
    def test_persistence_includes_time_zero(self):self.assertEqual(persist([[0,1],[0,1]],[1,0],{1},1),0)
    def test_exit_ends_uninterrupted_persistence(self):self.assertEqual(persist([[0,1],[1,0]],[1,0],{0},4),0)
    def test_occupation_is_not_persistence(self):
        P=[[0,1],[1,0]];self.assertEqual(occupy(P,[1,0],{0},4),.6);self.assertEqual(persist(P,[1,0],{0},4),0)
    def test_entry_is_not_occupation(self):
        P=[[0,1],[1,0]];self.assertEqual(hit(P,[1,0],{1},4)['target_by_horizon'],1);self.assertEqual(occupy(P,[1,0],{1},4),.4)
    def test_zero_horizon_occupancy(self):self.assertEqual(occupy([[1,0],[0,1]],[.3,.7],{0},0),.3)
    def test_empty_region_persistence(self):self.assertEqual(persist([[1]],[1],set(),5),0)
    def test_probability_conservation_50_random_chains(self):
        rng=random.Random(877)
        for _ in range(50):
            P=[]
            for i in range(4):
                row=[rng.random() for _ in range(4)];total=sum(row);P.append([x/total for x in row])
            x=hit(P,[1,0,0,0],{2},8,{3})
            self.assertAlmostEqual(x['target_by_horizon']+x['competing_by_horizon']+x['unresolved_at_horizon'],1,places=12)
    def test_exhaustive_path_agreement(self):
        P=[[.7,.3],[.4,.6]];H=4;law=[.2,.8]
        expected_hits=[0.]*(H+1);expected_persist=0.;expected_occ=0.
        for path in itertools.product(range(2),repeat=H+1):
            pr=law[path[0]]
            for i in range(H):pr*=P[path[i]][path[i+1]]
            if 1 in path:expected_hits[path.index(1)]+=pr
            if all(x==1 for x in path):expected_persist+=pr
            expected_occ+=pr*sum(x==1 for x in path)/(H+1)
        actual=hit(P,law,{1},H)
        for a,b in zip(actual['first_entry_probabilities'],expected_hits):self.assertAlmostEqual(a,b)
        self.assertAlmostEqual(persist(P,law,{1},H),expected_persist)
        self.assertAlmostEqual(occupy(P,law,{1},H),expected_occ)
    def test_lumpability_positive(self):self.assertTrue(strongly_lumpable([[.2,.3,.5],[.4,.1,.5],[.1,.1,.8]],[[0,1],[2]]))
    def test_lumpability_negative(self):self.assertFalse(strongly_lumpable([[.2,.3,.5],[.4,.3,.3],[.1,.1,.8]],[[0,1],[2]]))
    def test_singleton_partition_lumpable(self):self.assertTrue(strongly_lumpable([[.2,.8],[.9,.1]],[[0],[1]]))
    def test_unequal_hidden_start_affects_hitting(self):
        P=[[.2,.3,.5],[.4,.3,.3],[0,0,1]]
        self.assertNotEqual(hit(P,[1,0,0],{2},1)['target_by_horizon'],hit(P,[0,1,0],{2},1)['target_by_horizon'])
    def test_matrix_must_be_square(self):
        with self.assertRaises(ValueError):validate([[1,0]],[1])
    def test_matrix_nonempty(self):
        with self.assertRaises(ValueError):validate([],[])
    def test_initial_must_match(self):
        with self.assertRaises(ValueError):validate([[1]],[1,0])
    def test_negative_probabilities(self):
        with self.assertRaises(ValueError):validate([[-1,2],[0,1]],[1,0])
    def test_nan_probabilities(self):
        with self.assertRaises(ValueError):validate([[math.nan]],[1])
    def test_infinite_probabilities(self):
        with self.assertRaises(ValueError):validate([[math.inf]],[1])
    def test_boolean_probabilities(self):
        with self.assertRaises(ValueError):validate([[True]],[1])
    def test_nonstochastic_row(self):
        with self.assertRaises(ValueError):validate([[.8]],[1])
    def test_invalid_initial_mass(self):
        with self.assertRaises(ValueError):validate([[1]],[.5])
    def test_negative_horizon(self):
        with self.assertRaises(ValueError):hit([[1]],[1],{0},-1)
    def test_boolean_horizon(self):
        with self.assertRaises(ValueError):hit([[1]],[1],{0},True)
    def test_fractional_horizon(self):
        with self.assertRaises(ValueError):hit([[1]],[1],{0},.5)
    def test_target_index_outside(self):
        with self.assertRaises(ValueError):hit([[1]],[1],{1},1)
    def test_overlapping_target_competing(self):
        with self.assertRaises(ValueError):hit([[1]],[1],{0},1,{0})
    def test_invalid_partition_overlap(self):
        with self.assertRaises(ValueError):strongly_lumpable([[1,0],[0,1]],[[0],[0]])
    def test_invalid_partition_missing_state(self):
        with self.assertRaises(ValueError):strongly_lumpable([[1,0],[0,1]],[[0]])
    def test_negative_tolerance(self):
        with self.assertRaises(ValueError):strongly_lumpable([[1]],[[0]],-1)

class BranchingTests(unittest.TestCase):
    def test_subcritical_extinction(self):self.assertEqual(survival_probability(1,2),0)
    def test_critical_extinction(self):self.assertEqual(survival_probability(1,1),0)
    def test_supercritical_survival(self):self.assertEqual(survival_probability(2,1),.5)
    def test_two_independent_founders(self):self.assertEqual(survival_probability(2,1,2),.75)
    def test_absent_founder(self):self.assertEqual(survival_probability(2,1,0),0)
    def test_no_death(self):self.assertEqual(survival_probability(2,0),1)
    def test_frozen_population_survives(self):self.assertEqual(survival_probability(0,0),1)
    def test_death_only_extinction(self):self.assertEqual(survival_probability(0,2),0)
    def test_negative_rate(self):
        with self.assertRaises(ValueError):survival_probability(-1,0)
    def test_nan_rate(self):
        with self.assertRaises(ValueError):survival_probability(float('nan'),0)
    def test_fractional_founders(self):
        with self.assertRaises(ValueError):survival_probability(2,1,.5)
    def test_negative_founders(self):
        with self.assertRaises(ValueError):survival_probability(2,1,-1)

if __name__=='__main__':unittest.main()
