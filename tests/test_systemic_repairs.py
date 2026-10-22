"""Synthetic regressions of PR #2 scientific admission and history repairs."""
import copy
from oocgraph.core import history_violations, model_identity_digest, validate_records
from tests.test_production_contracts import ProductionValidation, mathematical_fixture, route_records, fully_typed
from tests.test_transfer_review import example as transfer_example
from tests.test_integrity import node


class SystemicRepairs(ProductionValidation):
    def test_retracted_obligation_downgrades_only_current_freeze(self):
        from oocgraph.core import effective_freeze_eligibility
        from tests.test_production_contracts import freeze_records
        rs=freeze_records()
        original=effective_freeze_eligibility(rs,["ooc:fixture:g"])
        self.assertTrue(original["eligible"])
        rs+=fully_typed([
            node("Authority","ret-auth",status="ACTIVE_RULE",
                 axes=["EVIDENCE_POLICY"],scope={"domain":"audit"}),
            node("EvidenceObject","notice",status="RECORDED",
                 evidence_class="REVIEW",claim_ceiling="VERIFICATION_ONLY",
                 context_ref="ooc:fixture:context",source_locator_refs=["ooc:fixture:freeze-loc"],
                 study_id="fixture",system_id="notice",uncertainty="synthetic",
                 finding="Retracted support",provenance_class="CURATED_SEMANTIC"),
            node("EvidenceAssessment","retract",status="ADJUDICATED",
                 target_ref="ooc:fixture:freeze-e",evidence_ref="ooc:fixture:notice",
                 authority_ref="ooc:fixture:ret-auth",effect="RETRACTS",
                 assessment_role="RETRACTION",scope={"domain":"audit"},
                 rationale="Synthetic correction",limitations="Synthetic only",
                 provenance_class="CURATED_SEMANTIC")
        ])
        self.assertEqual(self.errors(rs),[])
        effective=effective_freeze_eligibility(rs,["ooc:fixture:g"])
        self.assertFalse(effective["eligible"])
        self.assertEqual(effective["gap_states"]["ooc:fixture:g"]["effective"],"CONTESTED")

    def test_proposed_data_leakage_may_be_documented(self):
        from tests.test_routes_and_data import data_fixture, get
        rs=data_fixture()
        get(rs,"u2")["unit_keys"]=["A"]
        self.assertEqual(validate_records(rs),[])

    def test_test_must_bind_result_execution(self):
        records=mathematical_fixture()
        t=next(r for r in records if r["type"]=="Test")
        other=copy.deepcopy(next(r for r in records if r["type"]=="Execution"))
        other["id"]="ooc:fixture:other-execution"
        records.append(other)
        t["execution_ref"]=other["id"]
        self.assertTrue(any("UNVERIFIED_MATHEMATICAL_PROMOTION" in x for x in self.errors(records)))

    def test_retired_model_preserves_proposed_owned_data(self):
        rs=mathematical_fixture()
        m=next(r for r in rs if r["type"]=="ModelInstance")
        m["status"]="RETIRED"
        d=fully_typed([node("Dataset","d",family_id="family",version="v1",
                            contains_patient_identifiers=False,availability="synthetic")])[0]
        u=fully_typed([node("DataUse","u",model_instance_ref=m["id"],dataset_ref=d["id"],
                            protocol_ref="ooc:fixture:math-protocol",role="TRAIN",
                            partition_id="p",independence_status="UNKNOWN",status="PROPOSED")])[0]
        rs.extend([d,u])
        m["frozen_digest"]=model_identity_digest(rs,m)
        after=copy.deepcopy(rs)
        next(r for r in after if r["id"]==u["id"])["partition_id"]="changed"
        self.assertTrue(any("MUTATED_ADMITTED_DEPENDENCY" in x
                            for x in history_violations(rs,after)))

    def test_other_scope_ancestry_neither_breaks_nor_closes(self):
        rs=route_records()
        f=next(r for r in rs if r["type"]=="FounderEnsemble")
        other=copy.deepcopy(next(r for r in rs if r["id"]=="ooc:fixture:fa"))
        other["id"]="ooc:fixture:another-ancestry"
        other["scope"]={"adapter":"other"}
        rs.append(other)
        f["ancestry_assessment_refs"].append(other["id"])
        self.assertEqual(self.errors(rs),[])
        f["ancestry_assessment_refs"]=[other["id"]]
        self.assertTrue(any("UNSUPPORTED_ROUTE_ANCESTRY" in x for x in self.errors(rs)))

    def test_human_route_does_not_promote_animal_context(self):
        rs=route_records()
        scope={"adapter":"synthetic","species":"human"}
        next(r for r in rs if r["type"]=="Route")["scope"]=scope
        for r in rs:
            if r["type"] in {"Transition","EvidenceAssessment"}:
                r["scope"]=scope
        self.assertTrue(self.errors(rs))

    def test_human_transfer_requires_human_adapter_evidence(self):
        rs=transfer_example()
        scope={"pan_cancer":True,"species":"human"}
        for r in rs:
            if r["type"] in {"Authority","Decision","Verdict"}:
                r["scope"]=scope
            if r["type"]=="EvidenceAssessment":
                r["scope"]=({"adapter":r["scope"]["adapter"],"species":"human"}
                            if "adapter" in r["scope"] else scope)
        self.assertTrue(any("MISSING_TRANSFER_ADAPTER_SUPPORT" in x for x in self.errors(rs)))
