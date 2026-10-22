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


    def test_append_only_kernel_freeze_authorization(self):
        from tests.test_production_contracts import freeze_records
        from oocgraph.core import kernel_freeze_basis_digest, effective_freeze_eligibility
        rs=freeze_records()
        programme=next(r for r in rs if r["type"]=="Programme")
        programme["kernel_frozen"]=False
        before=copy.deepcopy(rs)
        basis=["ooc:fixture:g","ooc:fixture:q"]
        event=fully_typed([node(
            "AuthorizationEvent","kernel-event",status="RECORDED",
            action="FREEZE_KERNEL",subject_ref=programme["id"],
            authority_ref="ooc:fixture:freeze-auth",
            scope={"domain":"PROGRAMME_GOVERNANCE"},
            basis_refs=basis,basis_digest=kernel_freeze_basis_digest(rs,basis),
            evidence_refs=[],provenance_class="CURATED_SEMANTIC")])[0]
        rs.append(event)
        self.assertEqual(self.errors(rs),[])
        self.assertTrue(effective_freeze_eligibility(rs,["ooc:fixture:g"])["effective_kernel_frozen"])
        self.assertEqual(history_violations(before,rs),[])

    def test_empty_model_admission_evidence_fails(self):
        rs=mathematical_fixture()
        m=next(r for r in rs if r["type"]=="ModelInstance")
        e=fully_typed([node(
            "AuthorizationEvent","bad-model-admission",status="RECORDED",
            action="ADMIT_MODEL",subject_ref=m["id"],
            authority_ref="ooc:fixture:math-auth",scope=m["scope"],
            basis_refs=[m["id"]],basis_digest=m["frozen_digest"],
            evidence_refs=[],provenance_class="CURATED_SEMANTIC")])[0]
        rs.append(e)
        self.assertTrue(any("UNQUALIFIED_MODEL_ADMISSION" in x for x in self.errors(rs)))

    def test_two_competing_freezes_do_not_resolve_by_timestamp(self):
        from tests.test_production_contracts import freeze_records
        from oocgraph.core import kernel_freeze_basis_digest
        rs=freeze_records()
        programme=next(r for r in rs if r["type"]=="Programme")
        programme["kernel_frozen"]=False
        basis=["ooc:fixture:g","ooc:fixture:q"]
        e=fully_typed([node(
            "AuthorizationEvent","e1",status="RECORDED",action="FREEZE_KERNEL",
            subject_ref=programme["id"],authority_ref="ooc:fixture:freeze-auth",
            scope={"domain":"PROGRAMME_GOVERNANCE"},
            basis_refs=basis,basis_digest=kernel_freeze_basis_digest(rs,basis),
            evidence_refs=[],provenance_class="CURATED_SEMANTIC")])[0]
        rs.extend([e,{**e,"id":"ooc:fixture:e2"}])
        self.assertTrue(any("AUTHORIZATION_HISTORY" in x for x in self.errors(rs)))


    def test_retracted_contradiction_ceases_contesting_current_route(self):
        from oocgraph.core import effective_route_state
        rs=route_records()
        route=next(r for r in rs if r["type"]=="Route")
        e=copy.deepcopy(next(r for r in rs if r["id"]=="ooc:fixture:e2"))
        e["id"]="ooc:fixture:contradicting-study"
        a=copy.deepcopy(next(r for r in rs if r["id"]=="ooc:fixture:a2"))
        a.update(id="ooc:fixture:contradiction",target_ref=route["id"],
                 evidence_ref=e["id"],effect="CONTRADICTS")
        rs.extend([e,a])
        self.assertEqual(effective_route_state(rs,route)["effective"],"CONTESTED")
        rs+=fully_typed([
            node("Authority","retraction-authority",status="ACTIVE_RULE",
                 axes=["EVIDENCE_POLICY"],scope={"domain":"corrections"}),
            node("EvidenceObject","notice-e",status="RECORDED",
                 context_ref="ooc:fixture:c",source_locator_refs=["ooc:fixture:l"],
                 evidence_class="REVIEW",claim_ceiling="VERIFICATION_ONLY",
                 finding="Retraction",study_id="paper",system_id="notice",
                 uncertainty="synthetic",provenance_class="CURATED_SEMANTIC"),
            node("EvidenceAssessment","retract-contradiction",status="ADJUDICATED",
                 target_ref=e["id"],evidence_ref="ooc:fixture:notice-e",
                 authority_ref="ooc:fixture:retraction-authority",
                 effect="RETRACTS",assessment_role="RETRACTION",
                 scope={"domain":"corrections"},
                 rationale="Corrected study",limitations="Synthetic only",
                 provenance_class="CURATED_SEMANTIC")
        ])
        self.assertEqual(self.errors(rs),[])
        self.assertEqual(effective_route_state(rs,route)["effective"],"ADMITTED_CLOSED")

    def test_retracted_adapter_evidence_contests_pan_cancer_transfer(self):
        from oocgraph.core import resolve
        rs=transfer_example()
        self.assertEqual(resolve(rs)["partitions"][0]["state"],"SUPPORTED_SCOPED")
        rs+=fully_typed([
            node("Authority","retraction-authority",status="ACTIVE_RULE",
                 axes=["EVIDENCE_POLICY"],scope={"domain":"corrections"}),
            node("EvidenceObject","correction-notice",status="RECORDED",
                 context_ref="ooc:fixture:cross-context",
                 source_locator_refs=["ooc:fixture:cross-loc"],
                 evidence_class="REVIEW",claim_ceiling="VERIFICATION_ONLY",
                 finding="Retraction",study_id="paper",system_id="notice",
                 uncertainty="synthetic",provenance_class="CURATED_SEMANTIC"),
            node("EvidenceAssessment","retract-adapter-3",status="ADJUDICATED",
                 target_ref="ooc:fixture:cross-ev-3",
                 evidence_ref="ooc:fixture:correction-notice",
                 authority_ref="ooc:fixture:retraction-authority",
                 effect="RETRACTS",assessment_role="RETRACTION",
                 scope={"domain":"corrections"},
                 rationale="Retract one independent adapter",
                 limitations="Synthetic only",provenance_class="CURATED_SEMANTIC")
        ])
        self.assertEqual(self.errors(rs),[])
        self.assertEqual(resolve(rs)["partitions"][0]["state"],"CONTESTED")

    def test_all_human_adapters_can_support_human_transfer(self):
        rs=transfer_example()
        scope={"pan_cancer":True,"species":"human"}
        for r in rs:
            if r["type"]=="Context":
                r["species"]="human"
            if r["type"]=="EvidenceObject":
                r["evidence_class"]="PRIMARY_HUMAN_LONGITUDINAL"
            if r["type"] in {"Authority","Decision","Verdict"}:
                r["scope"]=scope
            if r["type"]=="EvidenceAssessment":
                r["scope"]=({"adapter":r["scope"]["adapter"],"species":"human"}
                            if "adapter" in r["scope"] else scope)
        self.assertEqual(self.errors(rs),[])

    def test_independent_origin_entry_and_establishment(self):
        rs=route_records()
        scope={"adapter":"synthetic"}
        rs+=fully_typed([
            node("StateVariable","malignancy-readout",definition="Independent measure",
                 history_role="BIOLOGICAL",observable_status="OBSERVED",units="synthetic"),
            node("PersistenceCriterion","origin-persistence",
                 context_ref="ooc:fixture:c",estimand_ref="ooc:fixture:origin-estimand",
                 horizon="H",metric="established",preregistration_status="REGISTERED",
                 rationale="Prospective synthetic endpoint",units="time"),
            node("Estimand","origin-estimand",definition_obligation="Residence time"),
            node("Claim","origin-claim",claim_kind="ORIGIN",scope=scope,status="PROVISIONAL",
                 statement="Synthetic first entry and establishment",
                 modality="ASSERTION",empirical_admission="NOT_ESTABLISHED",
                 origin_route_ref="ooc:fixture:r",malignant_state_ref="ooc:fixture:s3",
                 persistence_criterion_ref="ooc:fixture:origin-persistence",
                 entry_assessment_refs=["ooc:fixture:origin-entry"],
                 establishment_assessment_refs=["ooc:fixture:origin-establishment"]),
            node("Authority","origin-authority",status="ACTIVE_RULE",
                 axes=["BIOLOGICAL_SUPPORT"],scope=scope,empirical_truth_authority=False),
            node("EvidenceAssessment","origin-entry",status="ADJUDICATED",
                 effect="SUPPORTS",assessment_role="TEMPORAL",
                 target_ref="ooc:fixture:origin-claim",evidence_ref="ooc:fixture:e1",
                 scope=scope,rationale="Synthetic entry",limitations="Synthetic",
                 provenance_class="CURATED_SEMANTIC"),
            node("EvidenceAssessment","origin-establishment",status="ADJUDICATED",
                 effect="SUPPORTS",assessment_role="PERSISTENCE",
                 target_ref="ooc:fixture:origin-claim",evidence_ref="ooc:fixture:e2",
                 scope=scope,rationale="Synthetic establishment",limitations="Synthetic",
                 provenance_class="CURATED_SEMANTIC"),
            node("Verdict","origin-verdict",status="RECORDED",
                 axis="BIOLOGICAL_SUPPORT",facet="malignant-origin",
                 decision="SUPPORTED_SCOPED",scope=scope,
                 subject_ref="ooc:fixture:origin-claim",
                 authority_ref="ooc:fixture:origin-authority",
                 assessment_refs=["ooc:fixture:origin-establishment"],
                 result_refs=[],supersedes_refs=[],rationale="Synthetic combined origin")
        ])
        next(r for r in rs if r["id"]=="ooc:fixture:s3")["variable_refs"]=["ooc:fixture:malignancy-readout"]
        next(r for r in rs if r["id"]=="ooc:fixture:e2")["design_class"]="MIXED"
        self.assertEqual(self.errors(rs),[])
        claim=next(r for r in rs if r["id"]=="ooc:fixture:origin-claim")
        claim["entry_assessment_refs"]=[]
        self.assertTrue(any("NONBIOLOGICAL_PROMOTION" in e for e in self.errors(rs)))

    def test_positive_model_license_uses_separate_event(self):
        from oocgraph.core import effective_model_state
        rs=mathematical_fixture()
        m=next(r for r in rs if r["type"]=="ModelInstance")
        next(r for r in rs if r["id"]=="ooc:fixture:math-auth")["axes"].append("EVIDENCE_POLICY")
        rs.append(fully_typed([node("EvidenceAssessment","model-license-assessment",
            status="ADJUDICATED",target_ref=m["id"],
            evidence_ref="ooc:fixture:math-evidence",effect="SUPPORTS",
            assessment_role="MODEL",scope=m["scope"],
            rationale="Synthetic validation",limitations="Not biological evidence",
            provenance_class="CURATED_SEMANTIC")])[0])
        before=copy.deepcopy(rs)
        event=fully_typed([node("AuthorizationEvent","model-license",
            status="RECORDED",action="ADMIT_MODEL",subject_ref=m["id"],
            authority_ref="ooc:fixture:math-auth",scope=m["scope"],
            basis_refs=[m["id"]],basis_digest=m["frozen_digest"],
            evidence_refs=["ooc:fixture:math-evidence"],
            provenance_class="CURATED_SEMANTIC")])[0]
        rs.append(event)
        self.assertEqual(self.errors(rs),[])
        self.assertEqual(effective_model_state(rs,m)["effective"],"ADMITTED")
        self.assertEqual(history_violations(before,rs),[])
        retirement=fully_typed([node("AuthorizationEvent","model-retirement",
            status="RECORDED",action="RETIRE_MODEL",subject_ref=m["id"],
            authority_ref="ooc:fixture:math-auth",scope=m["scope"],
            previous_event_ref=event["id"],basis_refs=[m["id"]],
            basis_digest=m["frozen_digest"],evidence_refs=[],
            provenance_class="CURATED_SEMANTIC")])[0]
        rs.append(retirement)
        self.assertEqual(self.errors(rs),[])
        self.assertEqual(effective_model_state(rs,m)["effective"],"RETIRED")

    def test_append_only_reinstatement_of_retraction(self):
        from oocgraph.core import approved_retractions, approved_reinstatements
        from tests.test_latest_codex import LatestCodexContracts
        helper=LatestCodexContracts()
        rs=fully_typed(helper.retracted_route_fixture())
        prior=next(r for r in rs if r["id"]=="ooc:fixture:retraction-adjudication")
        self.assertIn("ooc:fixture:e1",approved_retractions(rs))
        again=copy.deepcopy(next(r for r in rs if r["id"]=="ooc:fixture:retraction-notice"))
        again["id"]="ooc:fixture:reinstatement-notice"
        new=fully_typed([node(
            "EvidenceAssessment","reinstatement",status="ADJUDICATED",
            effect="REINSTATES",assessment_role="REASSESSMENT",
            target_ref=prior["id"],evidence_ref=again["id"],
            authority_ref=prior["authority_ref"],scope=prior["scope"],
            rationale="Correction of prior withdrawal",limitations="Synthetic only",
            provenance_class="CURATED_SEMANTIC")])[0]
        rs.extend([again,new])
        self.assertEqual(self.errors(rs),[])
        self.assertNotIn("ooc:fixture:e1",approved_retractions(rs))
        self.assertIn(prior["id"],approved_reinstatements(rs))

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
