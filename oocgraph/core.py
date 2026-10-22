"""Strict graph I/O, scoped state resolution, and cross-record validation.

All operations are offline. This module never executes imported reference code.
Engineering conformance is not adjudication of the truth of a scientific statement.
"""
from __future__ import annotations
import hashlib
import json
import math
import re
from collections import defaultdict
from pathlib import Path, PurePosixPath
from typing import Any, Iterable

class IntegrityError(ValueError):
    """Malformed or inconsistent graph input."""

def _unique_pairs(pairs):
    obj = {}
    for key, value in pairs:
        if key in obj:
            raise IntegrityError(f"Duplicate JSON key: {key}")
        obj[key] = value
    return obj

def _bad_number(value):
    raise IntegrityError(f"Non-finite JSON number: {value}")

def loads(text: str) -> Any:
    try:
        return json.loads(text, object_pairs_hook=_unique_pairs, parse_constant=_bad_number)
    except (json.JSONDecodeError, ValueError) as exc:
        raise IntegrityError(str(exc)) from exc

def canonical(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False)

def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

def safe_path(root: Path, name: str) -> Path:
    """Require a POSIX repository-relative path without traversal or symlink escape."""
    if not isinstance(name, str) or not name or "\\" in name or "\x00" in name:
        raise IntegrityError(f"Invalid repository path: {name!r}")
    p = PurePosixPath(name)
    if not p.parts or p.is_absolute() or ".." in p.parts or ":" in p.parts[0]:
        raise IntegrityError(f"Unsafe repository path: {name!r}")
    path = root.joinpath(*p.parts)
    if not path.resolve().is_relative_to(root.resolve()):
        raise IntegrityError(f"Path escapes repository: {name}")
    return path

def read_graph(root: Path) -> list[dict]:
    collections = loads((root / "config/collections.json").read_text())
    expected = {f"{v}.jsonl": k for k, v in collections.items()}
    actual = {p.name for p in (root / "graph").glob("*.jsonl")}
    if actual != set(expected):
        raise IntegrityError(f"Collection mismatch missing={set(expected)-actual}, extra={actual-set(expected)}")
    result = []
    seen = set()
    for name, kind in sorted(expected.items()):
        for line, text in enumerate((root / "graph" / name).read_text().splitlines(), 1):
            if not text.strip():
                continue
            record = loads(text)
            if not isinstance(record, dict) or record.get("type") != kind:
                raise IntegrityError(f"Wrong record type in {name}:{line}")
            if record.get("id") in seen:
                raise IntegrityError(f"Duplicate record ID {record.get('id')}")
            seen.add(record.get("id")); result.append(record)
    return sorted(result, key=lambda r: r.get("id", ""))

def partition(verdict: dict) -> str:
    return canonical([verdict.get(k) for k in ("subject_ref", "axis", "facet", "scope", "model_instance_ref")])

def resolve(records: Iterable[dict]) -> dict:
    """Order-independent, explicit-supersession resolver; no recency ranking."""
    records = list(records)
    verdicts = {r["id"]: r for r in records if r["type"] == "Verdict"}
    buckets = defaultdict(list)
    for v in verdicts.values():
        buckets[partition(v)].append(v)
    output = []
    for key, members in sorted(buckets.items()):
        removed = set()
        edges = {}
        for v in members:
            edges[v["id"]] = v.get("supersedes_refs", [])
            for old in edges[v["id"]]:
                if old not in verdicts or partition(verdicts[old]) != key:
                    raise IntegrityError(f"Invalid or cross-partition supersession: {v['id']} -> {old}")
                removed.add(old)
        # Cycle detection, including self-supersession, is separate from biology cycles.
        visiting, done = set(), set()
        def walk(node):
            if node in visiting: raise IntegrityError("Supersession cycle")
            if node in done: return
            visiting.add(node)
            for old in edges.get(node, []): walk(old)
            visiting.remove(node); done.add(node)
        for node in sorted(edges): walk(node)
        active = sorted(v["id"] for v in members if v["id"] not in removed)
        status = verdicts[active[0]]["decision"] if len(active) == 1 else "CONFLICT"
        if len(active) == 1 and status in SCIENTIFIC_POSITIVE:
            v = verdicts[active[0]]
            index = {r["id"]: r for r in records}
            retracted = _retracted_support_refs(
                records, index, v.get("assessment_refs", []))
            subject = index.get(v.get("subject_ref"), {})
            route_contested = (subject.get("type") == "Route"
                               and effective_route_state(records, subject)["effective"] == "CONTESTED")
            used_data = [du for du in records if du.get("type") == "DataUse"
                         and du.get("model_instance_ref") == v.get("model_instance_ref")]
            model_data_contested = any(
                effective_data_use_state(records, du)["effective"] == "CONTESTED"
                for du in used_data)
            transfer_contested = (bool(v.get("scope", {}).get("pan_cancer"))
                                  and not _effective_pan_cancer_transfer(records, index, v))
            origin_contested = (
                subject.get("type") == "Claim" and subject.get("claim_kind") == "ORIGIN"
                and (bool(_retracted_support_refs(
                         records, index, list(subject.get("entry_assessment_refs", []))
                         + list(subject.get("establishment_assessment_refs", []))))
                     or effective_route_state(
                         records, index.get(subject.get("origin_route_ref"), {}))
                         ["effective"] != "ADMITTED_CLOSED"))
            if (retracted or route_contested or model_data_contested or transfer_contested
                or origin_contested
                or _material_scoped_contradictions(
                    records, index, [v.get("subject_ref")], v.get("scope"))):
                status = "CONTESTED"
        output.append({"partition": loads(key), "state": status, "active_verdict_refs": active,
                       "historical_verdict_refs": sorted(removed)})
    return {"policy": "EXPLICIT_SCOPED_SUPERSESSION_ONLY", "partitions": output,
            "missing_verdict_state": "UNKNOWN", "conflict_count": sum(x["state"] == "CONFLICT" for x in output),
            "inferred_scientific_promotions": 0}

REF_TYPES = {
    "source_state_ref": {"BiologicalState"}, "target_state_ref": {"BiologicalState"},
    "boundary_ref": {"Boundary"}, "founder_ref": {"FounderEnsemble"},
    "context_ref": {"Context"}, "adapter_ref": {"Adapter"}, "domain_ref": {"ValidityDomain"},
    "witness_bundle_ref": {"WitnessBundle"}, "evidence_ref": {"EvidenceObject"},
    "authority_ref": {"Authority"}, "dataset_ref": {"Dataset"}, "protocol_ref": {"Protocol"},
    "model_instance_ref": {"ModelInstance"}, "model_class_ref": {"ModelClass"},
    "applicability_ref": {"MethodApplicability"}, "software_ref": {"Software"},
    "execution_ref": {"Execution"}, "test_ref": {"Test"}, "gate_ref": {"Gate"},
    "gap_ref": {"ResearchGap"}, "estimand_ref": {"Estimand"}, "provenance_ref": {"ParameterProvenance"},
    "decision_ref": {"Decision"}, "completion_decision_ref": {"Decision"}, "transfer_decision_ref": {"Decision"},
    "assessment_ref": {"EvidenceAssessment"}, "same_identifier_as": {"LiteratureSource"},
    "process_ref": {"ObservationProcess"}, "observation_operator_ref": {"ObservationOperator"},
    "classification_source_ref": {"LiteratureSource"}, "source_ref": {"LiteratureSource"},
    "target_claim_ref": {"Claim"}, "target_estimand_ref": {"Estimand"}, "history_ref": {"Route"},
    "property_ref": {"Estimand", "PersistenceCriterion", "Claim"},
    "result_ref": {"Result"}, "candidate_set_ref": {"CandidateSet"},
    "source_context_ref": {"Context"}, "target_context_ref": {"Context"},
    "context_transition_assessment_ref": {"EvidenceAssessment"},
    "verification_artifact_ref": {"SourceArtifact"}, "output_artifact_ref": {"SourceArtifact"},
    "obligation_claim_ref": {"Claim"},
    "conflict_resolution_ref": {"Decision"},
    "previous_event_ref": {"AuthorizationEvent"},
    "origin_route_ref": {"Route"},
    "malignant_state_ref": {"BiologicalState"},
    "persistence_criterion_ref": {"PersistenceCriterion"},
}
REF_LIST_TYPES = {
    "basis_refs": {"ResearchGap", "Requirement", "Decision", "EvidenceObject", "ModelInstance"},
    "entry_assessment_refs": {"EvidenceAssessment"},
    "establishment_assessment_refs": {"EvidenceAssessment"},
    "evidence_refs": {"EvidenceObject"}, "bridge_evidence_refs": {"EvidenceObject"},
    "satisfaction_evidence_refs": {"EvidenceObject"}, "independence_evidence_refs": {"EvidenceObject"},
    "source_locator_refs": {"SourceLocator"}, "transition_refs": {"Transition"},
    "mechanism_refs": {"Mechanism"}, "assumption_refs": {"Assumption"}, "estimand_refs": {"Estimand"},
    "parameter_refs": {"Parameter"}, "equation_refs": {"Equation"}, "result_refs": {"Result"},
    "assessment_refs": {"EvidenceAssessment"}, "evidence_assessment_refs": {"EvidenceAssessment"},
    "supersedes_refs": {"Verdict"}, "verification_refs": {"SourceVerification"},
    "data_use_refs": {"DataUse"}, "intervention_operator_refs": {"InterventionOperator"},
    "state_variable_refs": {"StateVariable"}, "variable_refs": {"StateVariable"},
    "source_variables_refs": {"StateVariable"}, "target_variables_refs": {"StateVariable"},
    "state_refs": {"BiologicalState"}, "required_gate_refs": {"Gate"}, "null_refs": {"NullModel"},
    "ancestry_assessment_refs": {"EvidenceAssessment"},
    "transfer_adapter_refs": {"Adapter"},
    "protocol_refs": {"Protocol"},
    "completion_requirement_refs": {"Requirement"},
}
COMMON_SUBJECT_TYPES = {
    "Programme", "Theory", "Adapter", "Claim", "Boundary", "BiologicalState", "FounderEnsemble",
    "Mechanism", "Transition", "Route", "Estimand", "ModelClass", "ModelInstance",
    "PersistenceCriterion", "ResearchGap", "Workstream", "PathologyEntity", "NullModel",
    "Falsifier", "EvidenceObject", "EvidenceAssessment", "Requirement", "Protocol", "Test",
    "Result", "MethodApplicability", "Intervention", "Observation", "DataUse",
}
OWNER_REF_TYPES = {
    ("Intervention", "operator_ref"): {"InterventionOperator"},
    ("Observation", "operator_ref"): {"ObservationOperator"},
    ("AuthorizationEvent", "subject_ref"): {"ModelInstance", "Programme"},
    ("Decision", "subject_ref"): COMMON_SUBJECT_TYPES,
    ("Requirement", "subject_ref"): COMMON_SUBJECT_TYPES,
    ("Test", "subject_ref"): COMMON_SUBJECT_TYPES,
    ("Verdict", "subject_ref"): COMMON_SUBJECT_TYPES,
    ("EvidenceAssessment", "target_ref"): COMMON_SUBJECT_TYPES | {"SourceVerification"},
    ("Falsifier", "target_ref"): COMMON_SUBJECT_TYPES,
    ("Result", "subject_ref"): COMMON_SUBJECT_TYPES,
}
OWNER_REF_LIST_TYPES = {
    ("Authority", "subject_refs"): COMMON_SUBJECT_TYPES,
    ("Execution", "input_refs"): COMMON_SUBJECT_TYPES | {"Dataset", "DataUse", "Parameter", "SourceArtifact"},
    ("Protocol", "target_refs"): COMMON_SUBJECT_TYPES,
    ("Decision", "preserves_refs"): COMMON_SUBJECT_TYPES | {"SourceVerification"},
    ("CandidateSet", "member_refs"): {"ModelInstance", "ModelClass", "Route", "Transition", "Theory", "Claim", "BiologicalState", "Mechanism", "FounderEnsemble", "Estimand"},
    ("FounderEnsemble", "member_refs"): {"BiologicalState", "FounderEnsemble", "PathologyEntity"},
}
def _allowed_ref_types(record_type: str, key: str, list_field: bool = False):
    if key == "revision_of_ref":
        return {record_type}
    owner = OWNER_REF_LIST_TYPES if list_field else OWNER_REF_TYPES
    if (record_type, key) in owner:
        return owner[(record_type, key)]
    return (REF_LIST_TYPES if list_field else REF_TYPES).get(key)

SCIENTIFIC_POSITIVE = {"SUPPORTED_SCOPED", "MATHEMATICALLY_VERIFIED_SCOPED"}

BIOLOGICAL_EVIDENCE_CLASSES = frozenset({
    "PRIMARY_HUMAN_LONGITUDINAL", "PRIMARY_HUMAN_CROSS_SECTIONAL",
    "PRIMARY_ANIMAL", "PRIMARY_ORGANOID", "PRIMARY_IN_VITRO", "HUMAN_CAUSAL"
})
SCIENTIFIC_DISPOSITION_CLASSES = BIOLOGICAL_EVIDENCE_CLASSES | frozenset({
    "ANALYTIC", "FORMAL", "NUMERICAL"
})
BIOLOGICAL_CEILINGS = frozenset({
    "BIOLOGICAL_OBSERVATION", "BIOLOGICAL_CAUSAL_SCOPED"
})
EVIDENCE_OBLIGATION_POLICY = {
    "CAPABILITY": ({"BIOLOGICAL_OBSERVATION","BIOLOGICAL_CAUSAL_SCOPED"},
                   {"OBSERVATIONAL","LONGITUDINAL","LINEAGE","PERTURBATION","MIXED"},
                   {"OBSERVATION","CAUSAL"}),
    "OBSERVATION": ({"BIOLOGICAL_OBSERVATION","BIOLOGICAL_CAUSAL_SCOPED"},
                    {"OBSERVATIONAL","LONGITUDINAL","LINEAGE","MIXED"},
                    {"OBSERVATION"}),
    "ANCESTRY": ({"BIOLOGICAL_OBSERVATION","BIOLOGICAL_CAUSAL_SCOPED"},
                  {"LINEAGE","MIXED"},{"ANCESTRY"}),
    "PERSISTENCE": ({"BIOLOGICAL_OBSERVATION","BIOLOGICAL_CAUSAL_SCOPED"},
                    {"LONGITUDINAL","MIXED"},{"PERSISTENCE"}),
    "ROUTE": ({"BIOLOGICAL_CAUSAL_SCOPED"},{"PERTURBATION","MIXED"},{"CAUSAL"}),
    "HISTORICAL_ROUTE": ({"BIOLOGICAL_OBSERVATION","BIOLOGICAL_CAUSAL_SCOPED"},
                         {"LINEAGE","LONGITUDINAL","MIXED"},{"ANCESTRY","TEMPORAL"}),
    "TRANSITION": ({"BIOLOGICAL_OBSERVATION","BIOLOGICAL_CAUSAL_SCOPED"},
                   {"OBSERVATIONAL","LONGITUDINAL","LINEAGE","PERTURBATION","MIXED"},
                   {"TEMPORAL","ANCESTRY","CAUSAL"}),
    "CONSTITUTIVE": ({"BIOLOGICAL_CAUSAL_SCOPED"},{"PERTURBATION","MIXED"},{"CAUSAL"})
}
CLOSURE_DECISIONS = {
    ("ResearchGap", "RESOLVED"): ("RESEARCH_GAP_DISPOSITION", "RESOLVE"),
    ("ResearchGap", "BOUNDED"): ("RESEARCH_GAP_DISPOSITION", "BOUND"),
    ("Requirement", "SATISFIED"): ("REQUIREMENT_DISPOSITION", "SATISFY"),
    ("Requirement", "BOUNDED"): ("REQUIREMENT_DISPOSITION", "BOUND"),
}
MODEL_IDENTITY_ALGORITHM = "ooc-model-digest-v2"

NON_ADMISSIBLE_PROVENANCE = frozenset({
    "TEXTUAL_HINT", "SYNTHETIC", "ENGINEERING"
})


def _valid_ref_list(value):
    """Return None rather than throwing for malformed/unhashable input."""
    if not isinstance(value, list) or any(
            not isinstance(item, str) or not item for item in value):
        return None
    return set(value)


def _scope_within(parent, child):
    """An explicit *restriction* of a declared scope, never inferred promotion."""
    if not isinstance(parent, dict) or not parent or not isinstance(child, dict) or not child:
        return False
    # An affirmative breadth flag added to a narrower scope is promotion.
    for key, value in child.items():
        if key not in parent and isinstance(value, bool) and value:
            return False
    for key, value in parent.items():
        if key not in child:
            return False
        sub = child[key]
        if isinstance(value, list) and isinstance(sub, list):
            if not all(x in value for x in sub):
                return False
        elif value != sub:
            return False
    return True


def _evidence_matches_scientific_scope(index, evidence, scope):
    """Biological restrictions must survive every evidence handoff."""
    if not isinstance(scope, dict) or not isinstance(evidence, dict):
        return False
    ctx = index.get(evidence.get("context_ref"), {})
    if "species" in scope:
        species = str(scope["species"]).strip().lower()
        if str(ctx.get("species", "")).strip().lower() != species:
            return False
        if species == "human" and evidence.get("evidence_class") not in {
                "PRIMARY_HUMAN_LONGITUDINAL", "PRIMARY_HUMAN_CROSS_SECTIONAL",
                "HUMAN_CAUSAL"}:
            return False
    for key in ("tissue", "population", "time_scope"):
        if key in scope and scope[key] != ctx.get(key):
            return False
    return True


def _adapter_scientific_scope(scope, adapter):
    """Never discard species, population or temporal restrictions on transfer."""
    if not isinstance(scope, dict):
        return {}
    return {**{k: v for k, v in scope.items() if k != "pan_cancer"},
            "adapter": adapter}


def _has_active_source_locator(index, evidence):
    """Require qualified evidence to have at least one LOCATED provenance anchor."""
    return any(
        index.get(ref, {}).get("type") == "SourceLocator"
        and index[ref].get("status") == "LOCATED"
        and index[ref].get("provenance_class") not in NON_ADMISSIBLE_PROVENANCE
        and bool(index[ref].get("path"))
        and isinstance(index[ref].get("selector"), dict)
        and bool(index[ref]["selector"])
        for ref in evidence.get("source_locator_refs", []))


def _qualified_assessment(index, assessment, target_ref, scope, *,
                          effect="SUPPORTS", context_ref=None,
                          allowed_classes=BIOLOGICAL_EVIDENCE_CLASSES,
                          allowed_ceilings=BIOLOGICAL_CEILINGS,
                          assessment_role=None):
    """Independent, scoped evidence assessment: no workflow-status promotion."""
    if not isinstance(assessment, dict):
        return False
    evidence = index.get(assessment.get("evidence_ref"), {})
    return bool(
        assessment.get("type") == "EvidenceAssessment"
        and assessment.get("status") == "ADJUDICATED"
        and assessment.get("provenance_class") not in NON_ADMISSIBLE_PROVENANCE
        and assessment.get("effect") == effect
        and assessment.get("target_ref") == target_ref
        and canonical(assessment.get("scope")) == canonical(scope)
        and (assessment_role is None or assessment.get("assessment_role") == assessment_role)
        and evidence.get("type") == "EvidenceObject"
        and evidence.get("status") == "RECORDED"
        and evidence.get("provenance_class") not in NON_ADMISSIBLE_PROVENANCE
        and evidence.get("evidence_class") in allowed_classes
        and evidence.get("claim_ceiling") in allowed_ceilings
        and _has_active_source_locator(index, evidence)
        and bool(evidence.get("study_id")) and bool(evidence.get("system_id"))
        and (context_ref is None or evidence.get("context_ref") == context_ref)
        and _evidence_matches_scientific_scope(index, evidence, scope)
    )


def trusted_proof_receipt(root, index, result):
    """Verify a *trusted signer* actually attested the exact formal checker chain.

    Matching hashes and a self-reported PASS are not strong verification.
    The production trust registry begins empty; approval requires external governance.
    """
    from base64 import b64decode
    from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PublicKey
    from cryptography.exceptions import InvalidSignature
    try:
        receipt = result.get("verification_receipt", {})
        source = loads((root/"config/trusted_proof_checkers.json").read_text())
        test = index.get(result.get("test_ref"), {})
        exe = index.get(result.get("execution_ref"), {})
        model = index.get(result.get("model_instance_ref"), {})
        claim = index.get(result.get("subject_ref"), {})
        proof = index.get(result.get("verification_artifact_ref"), {})
        software = index.get(exe.get("software_ref"), {})
        signer_id = receipt.get("attestation_signer_id")
        keys = [r for r in source.get("trusted_checkers", [])
                if r.get("id") == signer_id
                and r.get("verifier_sha256") == software.get("sha256")
                and r.get("verifier_version") == receipt.get("verifier_version")]
        if len(keys) != 1:
            return False
        signature = b64decode(receipt.get("attestation_signature_b64", ""), validate=True)
        if len(signature) != 64:
            return False
        msg = canonical({
            "statement_sha256": sha256(claim.get("statement", "").encode("utf-8")),
            "proof_sha256": proof.get("sha256"),
            "checker_sha256": software.get("sha256"),
            "checker_version": receipt.get("verifier_version"),
            "execution_output_sha256": exe.get("output_sha256"),
            "model_digest": model.get("frozen_digest"),
            "model_instance_ref": model.get("id"),
            "subject_ref": claim.get("id"),
            "scope": result.get("scope"),
            "protocol_ref": test.get("protocol_ref"),
            "test_ref": test.get("id"),
            "execution_ref": exe.get("id"),
        }).encode("utf-8")
        Ed25519PublicKey.from_public_bytes(
            b64decode(keys[0].get("public_key_base64", ""),validate=True)
        ).verify(signature, msg)
        return True
    except (InvalidSignature, ValueError, TypeError, KeyError, OSError,
            IntegrityError, ImportError, AttributeError):
        return False


def _verified_result(index, result, subject_ref, scope):
    """Formal result certification is separate from successful execution or fit."""
    if not isinstance(result, dict) or result.get("type") != "Result":
        return False
    exe = index.get(result.get("execution_ref"), {})
    tst = index.get(result.get("test_ref"), {})
    protocol = index.get(tst.get("protocol_ref"), {})
    model = index.get(result.get("model_instance_ref"), {})
    artifact = index.get(result.get("verification_artifact_ref"), {})
    output_artifact = index.get(exe.get("output_artifact_ref"), {})
    receipt = result.get("verification_receipt")
    claim = index.get(subject_ref, {})
    verifier = index.get(exe.get("software_ref"), {})
    if not isinstance(receipt, dict):
        return False
    return bool(
        receipt.get("outcome") == "PASS"
        and claim.get("type") == "Claim"
        and receipt.get("statement_sha256") == sha256(
            claim.get("statement", "").encode("utf-8"))
        and receipt.get("artifact_sha256") == artifact.get("sha256")
        and receipt.get("verifier_sha256") == verifier.get("sha256")
        and receipt.get("execution_output_sha256") == exe.get("output_sha256")
        and output_artifact.get("type") == "SourceArtifact"
        and output_artifact.get("sha256") == exe.get("output_sha256")
        and bool(output_artifact.get("path"))
        and bool(receipt.get("verifier_version"))
        and result.get("status") == "VALIDATED"
        and result.get("outcome") == "PASS"
        and result.get("evidence_class") == "FORMAL"
        and result.get("claim_ceiling") == "MATHEMATICAL_EXACT"
        and result.get("verification_mode") == "FORMAL_PROOF"
        and artifact.get("type") == "SourceArtifact"
        and bool(artifact.get("path"))
        and result.get("provenance_class") not in NON_ADMISSIBLE_PROVENANCE
        and result.get("subject_ref") == subject_ref
        and canonical(result.get("scope")) == canonical(scope)
        and tst.get("type") == "Test" and tst.get("status") == "PASSED"
        and tst.get("subject_ref") == subject_ref
        and tst.get("execution_ref") == result.get("execution_ref")
        and exe.get("type") == "Execution" and exe.get("status") == "COMPLETED"
        and exe.get("outcome") == "PASS"
        and exe.get("protocol_ref") == tst.get("protocol_ref")
        and protocol.get("type") == "Protocol" and protocol.get("frozen") is True
        and protocol.get("status") == "ACTIVE"
        and protocol.get("id") in model.get("protocol_refs", [])
        and subject_ref in protocol.get("target_refs", [])
        and model.get("type") == "ModelInstance"
        and model.get("status") in {"FROZEN", "ADMITTED"}
        and result.get("model_instance_ref") == exe.get("model_instance_ref")
        and result.get("model_instance_ref") is not None
        and model.get("identity_algorithm") == MODEL_IDENTITY_ALGORITHM
        and bool(model.get("frozen_digest"))
        and canonical(model.get("scope")) == canonical(scope)
    )


def _appropriate_biological_assessment(index, assessment, target_ref, scope, claim_kind, *,
                                       context_ref=None):
    policy = EVIDENCE_OBLIGATION_POLICY.get(claim_kind)
    if policy is None:
        return False
    ceilings, designs, roles = policy
    evidence = index.get(assessment.get("evidence_ref"), {})
    return bool(
        evidence.get("design_class") in designs
        and assessment.get("assessment_role") in roles
        and _qualified_assessment(index, assessment, target_ref, scope,
                                  context_ref=context_ref, allowed_ceilings=ceilings)
    )


def _admitted_origin_claim(records, index, claim):
    """An end-to-end route is not first entry or malignant establishment."""
    if claim.get("type") != "Claim" or claim.get("claim_kind") != "ORIGIN":
        return False
    route = index.get(claim.get("origin_route_ref"), {})
    state = index.get(claim.get("malignant_state_ref"), {})
    criterion = index.get(claim.get("persistence_criterion_ref"), {})
    if not (route.get("type") == "Route"
            and route.get("status") == "CLOSED"
            and effective_route_state(records, route)["effective"] == "ADMITTED_CLOSED"
            and canonical(route.get("scope")) == canonical(claim.get("scope"))
            and route.get("transition_refs")
            and state.get("type") == "BiologicalState"
            and index.get(route["transition_refs"][-1], {}).get("target_state_ref") == state.get("id")
            and bool(state.get("variable_refs"))
            and criterion.get("type") == "PersistenceCriterion"
            and criterion.get("context_ref") == state.get("context_ref")
            and criterion.get("preregistration_status") in {"REGISTERED", "PRE_REGISTERED"}):
        return False
    witness = index.get(route.get("witness_bundle_ref"), {})
    eligible_refs = set(witness.get("evidence_refs", []))
    def admission(refs, role, designs):
        return bool(refs) and all(
            e.get("id") in eligible_refs
            and e.get("context_ref") == state.get("context_ref")
            and e.get("design_class") in designs
            and _qualified_assessment(
                index, a, claim.get("id"), claim.get("scope"),
                assessment_role=role, allowed_ceilings=BIOLOGICAL_CEILINGS)
            for ref in refs for a in [index.get(ref, {})]
            for e in [index.get(a.get("evidence_ref"), {})])
    return (
        admission(claim.get("entry_assessment_refs", []), "TEMPORAL",
                  {"LONGITUDINAL", "LINEAGE", "MIXED"})
        and admission(claim.get("establishment_assessment_refs", []), "PERSISTENCE",
                      {"LONGITUDINAL", "MIXED"}))


def _admissible_disposition_evidence(index, assessment, target_ref, scope, domain, effect):
    evidence = index.get(assessment.get("evidence_ref"), {})
    obligation = index.get(target_ref, {})
    kind = obligation.get("obligation_claim_kind")
    if evidence.get("evidence_class") in BIOLOGICAL_EVIDENCE_CLASSES:
        if domain not in {"BIOLOGICAL", "MEASUREMENT"} or kind not in EVIDENCE_OBLIGATION_POLICY:
            return False
        ceilings, designs, roles = EVIDENCE_OBLIGATION_POLICY[kind]
        return bool(
            evidence.get("design_class") in designs
            and assessment.get("assessment_role") in roles
            and _qualified_assessment(index, assessment, target_ref, scope, effect=effect,
                                      allowed_ceilings=ceilings)
        )
    if (domain == "STATISTICAL" and kind == "DATA_INDEPENDENCE"
            and evidence.get("evidence_class") == "ANALYTIC"
            and evidence.get("design_class") == "DATA_AUDIT"):
        return _qualified_assessment(
            index, assessment, target_ref, scope, effect=effect,
            allowed_classes={"ANALYTIC"}, allowed_ceilings={"DATA_PARTITION_AUDIT"},
            assessment_role="INDEPENDENCE")
    if evidence.get("evidence_class") == "FORMAL":
        if domain != "MATHEMATICAL" or kind not in {"CERTIFICATE", "MODEL_VALIDITY"}:
            return False
        if not _qualified_assessment(
                index, assessment, target_ref, scope, effect=effect,
                allowed_classes={"FORMAL"}, allowed_ceilings={"MATHEMATICAL_EXACT"}):
            return False
        result = index.get(evidence.get("result_ref"), {})
        obligation_claim = index.get(obligation.get("obligation_claim_ref"), {})
        return bool(
            obligation_claim.get("type") == "Claim"
            and obligation_claim.get("claim_kind") == "CERTIFICATE"
            and canonical(obligation_claim.get("scope")) == canonical(scope)
            and _verified_result(index, result, obligation_claim.get("id"), scope)
        )
    if evidence.get("evidence_class") == "ANALYTIC":
        # Analytical metadata alone is not independent freeze evidence.
        return False
    return False


def _decision_admission_errors(records, index, decision, subject_ref, scope, effects,
                               *, required_evidence_refs=None):
    """Gate disposition against *independent* obligation and qualified evidence.

    Decision.scope is jurisdiction; its disposition_scope cannot create an
    obligation. Status and Decision.decision have separate enforced semantics.
    """
    errors = []
    subject = index.get(subject_ref, {})
    subject_type, status = subject.get("type"), subject.get("status")
    expected = CLOSURE_DECISIONS.get((subject_type, status))
    authority = index.get(decision.get("authority_ref"), {})
    if not (expected
            and decision.get("decision_kind") == expected[0]
            and decision.get("decision") == expected[1]):
        errors.append("INCOMPATIBLE_DISPOSITION")
    obligation_scope = subject.get("obligation_scope")
    obligation_domain = subject.get("obligation_domain")
    if not _scope_within(obligation_scope, scope):
        errors.append("INVALID_OBLIGATION_SCOPE")
    if status != "BOUNDED" and canonical(obligation_scope) != canonical(scope):
        errors.append("WRONG_OBLIGATION_SCOPE")
    if status == "BOUNDED" and canonical(subject.get("bound_scope")) != canonical(scope):
        errors.append("BOUND_SCOPE_MISMATCH")
    if obligation_domain not in {"BIOLOGICAL", "MATHEMATICAL", "MEASUREMENT", "STATISTICAL", "METHODOLOGICAL"}:
        errors.append("UNKNOWN_OBLIGATION_DOMAIN")
    obligation_kind = subject.get("obligation_claim_kind")
    if obligation_domain == "BIOLOGICAL" and obligation_kind not in EVIDENCE_OBLIGATION_POLICY:
        errors.append("UNKNOWN_BIOLOGICAL_CLAIM_KIND")
    if obligation_domain == "MATHEMATICAL" and obligation_kind not in {"CERTIFICATE","MODEL_VALIDITY"}:
        errors.append("UNKNOWN_MATHEMATICAL_CLAIM_KIND")
    if not (
        decision.get("type") == "Decision"
        and decision.get("status") == "RECORDED"
        and decision.get("provenance_class") not in NON_ADMISSIBLE_PROVENANCE
        and decision.get("subject_ref") == subject_ref
        and canonical(decision.get("disposition_scope")) == canonical(scope)
        and authority.get("type") == "Authority"
        and authority.get("status") == "ACTIVE_RULE"
        and "RESEARCH_POLICY" in authority.get("axes", [])
        and canonical(decision.get("scope")) == canonical(authority.get("scope"))
        and authority.get("scope", {}).get("domain") == "PROGRAMME_GOVERNANCE"
        and (not authority.get("subject_refs")
             or subject_ref in authority.get("subject_refs", []))
    ):
        errors.append("INVALID_AUTHORIZED_DISPOSITION")
    evidence_refs = _valid_ref_list(decision.get("evidence_refs"))
    if evidence_refs is None:
        errors.append("MALFORMED_DISPOSITION_EVIDENCE")
        evidence_refs = set()
    if not evidence_refs:
        errors.append("MISSING_DISPOSITION_EVIDENCE")
    if required_evidence_refs is not None:
        required = _valid_ref_list(required_evidence_refs)
        if required is None:
            errors.append("MALFORMED_SATISFACTION_EVIDENCE")
        elif evidence_refs != required:
            errors.append("DISPOSITION_EVIDENCE_MISMATCH")
    for evidence_ref in sorted(evidence_refs):
        assessments = (a for a in records if a.get("type") == "EvidenceAssessment"
                       and a.get("evidence_ref") == evidence_ref)
        if not any(
            _admissible_disposition_evidence(index, a, subject_ref, scope, obligation_domain, effect)
            for a in assessments for effect in effects
        ):
            errors.append("UNADJUDICATED_DISPOSITION_EVIDENCE")
    return errors


def _witness_keys(evidence):
    """Witness IDs are meaningful only within the study and biological system."""
    return {(evidence.get("study_id"),evidence.get("system_id"),value)
            for value in evidence.get("witness_ids",[])
            if isinstance(value,str) and evidence.get("study_id") and evidence.get("system_id")}


def _founder_context_ok(index, founder_ref, context_ref, seen=None):
    """Check every nested founder and biological state; reject ancestry cycles."""
    seen = set() if seen is None else seen
    if founder_ref in seen:
        return False
    seen.add(founder_ref)
    founder = index.get(founder_ref,{})
    if founder.get("type") != "FounderEnsemble" or founder.get("context_ref") != context_ref:
        return False
    for ref in founder.get("member_refs",[]):
        member = index.get(ref,{})
        if member.get("type") == "FounderEnsemble":
            if not _founder_context_ok(index,ref,context_ref,seen):
                return False
        elif member.get("type") == "BiologicalState" and member.get("context_ref") != context_ref:
            return False
    seen.remove(founder_ref)
    return True


def _founder_states(index, founder_ref, seen=None):
    """Resolve member states of a potentially cooperative/nested founder ensemble."""
    seen = set() if seen is None else seen
    if founder_ref in seen:
        return set()
    seen.add(founder_ref)
    founder = index.get(founder_ref, {})
    result = set()
    for member_ref in founder.get("member_refs", []):
        member = index.get(member_ref, {})
        if member.get("type") == "BiologicalState":
            result.add(member_ref)
        elif member.get("type") == "FounderEnsemble":
            result.update(_founder_states(index, member_ref, seen))
    return result


def _authorized_retractions(records, index):
    """All historically valid retraction decisions, even if later reinstated."""
    result = {}
    for a in records:
        if (a.get("type") != "EvidenceAssessment"
                or a.get("effect") != "RETRACTS"
                or a.get("status") != "ADJUDICATED"):
            continue
        target = index.get(a.get("target_ref"), {})
        notice = index.get(a.get("evidence_ref"), {})
        authority = index.get(a.get("authority_ref"), {})
        if (a.get("assessment_role") == "RETRACTION"
            and a.get("provenance_class") not in NON_ADMISSIBLE_PROVENANCE
            and target.get("type") in {"EvidenceObject","SourceVerification"}
            and notice.get("type") == "EvidenceObject"
            and notice.get("status") == "RECORDED"
            and notice.get("evidence_class") in {"REVIEW", "ANALYTIC"}
            and notice.get("claim_ceiling") == "VERIFICATION_ONLY"
            and _has_active_source_locator(index, notice)
            and notice.get("provenance_class") not in NON_ADMISSIBLE_PROVENANCE
            and authority.get("type") == "Authority"
            and authority.get("status") == "ACTIVE_RULE"
            and "EVIDENCE_POLICY" in authority.get("axes", [])
            and canonical(authority.get("scope")) == canonical(a.get("scope"))
            and (not authority.get("subject_refs")
                 or a.get("target_ref") in authority.get("subject_refs", []))):
            result.setdefault(a["target_ref"], []).append(a["id"])
    return {k:sorted(v) for k,v in sorted(result.items())}


def approved_reinstatements(records, index=None):
    """Adjudicated, source-backed reversals of particular historical retractions."""
    index = {r["id"]:r for r in records} if index is None else index
    approved = _authorized_retractions(records, index)
    ids = {i for values in approved.values() for i in values}
    reinstated = {}
    for a in records:
        if (a.get("type")!="EvidenceAssessment" or a.get("effect")!="REINSTATES"
                or a.get("status")!="ADJUDICATED"):
            continue
        prior = index.get(a.get("target_ref"), {})
        notice = index.get(a.get("evidence_ref"), {})
        authority = index.get(a.get("authority_ref"), {})
        if (prior.get("id") in ids
            and a.get("assessment_role")=="REASSESSMENT"
            and a.get("provenance_class") not in NON_ADMISSIBLE_PROVENANCE
            and notice.get("type")=="EvidenceObject"
            and notice.get("status")=="RECORDED"
            and notice.get("claim_ceiling")=="VERIFICATION_ONLY"
            and notice.get("evidence_class") in {"REVIEW","ANALYTIC"}
            and _has_active_source_locator(index, notice)
            and notice.get("provenance_class") not in NON_ADMISSIBLE_PROVENANCE
            and authority.get("type")=="Authority"
            and authority.get("status")=="ACTIVE_RULE"
            and "EVIDENCE_POLICY" in authority.get("axes",[])
            and canonical(a.get("scope"))==canonical(prior.get("scope"))
            and canonical(a.get("scope"))==canonical(authority.get("scope"))
            and (not authority.get("subject_refs")
                 or prior.get("target_ref") in authority.get("subject_refs",[]))):
            reinstated.setdefault(prior["id"],[]).append(a["id"])
    return {k:sorted(v) for k,v in sorted(reinstated.items())}


def approved_retractions(records, index=None):
    """Active evidence withdrawals: never rewrite historical retraction events."""
    index = {r["id"]:r for r in records} if index is None else index
    historical = _authorized_retractions(records, index)
    restored = approved_reinstatements(records, index)
    return {k:sorted(set(v)-set(restored)) for k,v in historical.items()
            if set(v)-set(restored)}


def effective_data_use_state(records, data_use, retractions=None):
    """Historical DataUse admission remains; revoked audit support is contested."""
    raw = data_use.get("status", "PROPOSED")
    if raw != "ADMITTED":
        return {"declared": raw, "effective": raw, "retracted_audit_refs": []}
    retractions = approved_retractions(records) if retractions is None else retractions
    refs = sorted(set(data_use.get("independence_evidence_refs", [])) & set(retractions))
    return {"declared": raw, "effective": "CONTESTED" if refs else "ADMITTED",
            "retracted_audit_refs": refs}


def _retracted_support_refs(records, index, assessment_refs):
    retracted = approved_retractions(records, index)
    return sorted({a.get("evidence_ref") for ref in assessment_refs
                   if isinstance(ref,str) for a in [index.get(ref,{})]
                   if a.get("evidence_ref") in retracted})


def _transition_context_valid(index, transition):
    """Every supported transition needs endpoint and evidence-context continuity."""
    source = index.get(transition.get("source_state_ref"), {})
    target = index.get(transition.get("target_state_ref"), {})
    frame = transition.get("context_ref")
    sc, tc = source.get("context_ref"), target.get("context_ref")
    if (source.get("type") != "BiologicalState"
            or target.get("type") != "BiologicalState"
            or index.get(sc, {}).get("type") != "Context"
            or index.get(tc, {}).get("type") != "Context"
            or index.get(frame, {}).get("type") != "Context"):
        return False
    sc_context = index.get(sc, {})
    tc_context = index.get(tc, {})
    # A biological ancestry/transition never crosses organisms/species by
    # renaming its frame. Cross-species experiments are comparative evidence,
    # not a single continuous biological route.
    if str(sc_context.get("species", "")).strip().lower() != str(
            tc_context.get("species", "")).strip().lower():
        return False
    if sc == tc == frame:
        return True
    assessment = index.get(transition.get("context_transition_assessment_ref"), {})
    evidence = index.get(assessment.get("evidence_ref"), {})
    return bool(
        transition.get("source_context_ref") == sc
        and transition.get("target_context_ref") == tc
        and evidence.get("context_ref") in {sc, tc}
        and assessment.get("assessment_role") in {"TEMPORAL", "ANCESTRY", "CAUSAL"}
        and _appropriate_biological_assessment(
            index, assessment, transition.get("id"), transition.get("scope"),
            "TRANSITION", context_ref=evidence.get("context_ref"))
    )


def _admitted_transition_assessments(records, index, transition, scope):
    """Exact scoped primary support; a foreign-context finding cannot certify it."""
    if not _transition_context_valid(index, transition):
        return []
    sc = index.get(transition.get("source_state_ref"), {}).get("context_ref")
    tc = index.get(transition.get("target_state_ref"), {}).get("context_ref")
    # Validate the historical declaration against its original assessments;
    # a later retraction changes effective state, not immutable history.
    return [index.get(ref, {}) for ref in transition.get("evidence_assessment_refs", [])
            if isinstance(ref, str)
            and index.get(index.get(ref, {}).get("evidence_ref"), {}).get("context_ref") in {sc, tc}
            and _appropriate_biological_assessment(
                index, index.get(ref, {}), transition.get("id"), scope, "TRANSITION")]


def _material_scoped_contradictions(records, index, target_refs, scope):
    """Retracted negative evidence survives in history but not current support."""
    retracted = approved_retractions(records, index)
    return sorted(
        a["id"] for a in records
        if a.get("type") == "EvidenceAssessment"
        and a.get("target_ref") in set(target_refs)
        and a.get("effect") in {"CONTRADICTS", "FALSIFIES"}
        and a.get("evidence_ref") not in retracted
        and _qualified_assessment(
            index, a, a.get("target_ref"), scope, effect=a.get("effect"),
            allowed_classes=({"FORMAL"} if (
                index.get(a.get("target_ref"), {}).get("claim_kind") == "CERTIFICATE"
                or index.get(a.get("target_ref"), {}).get("obligation_domain") == "MATHEMATICAL")
                else BIOLOGICAL_EVIDENCE_CLASSES),
            allowed_ceilings=({"MATHEMATICAL_EXACT"} if (
                index.get(a.get("target_ref"), {}).get("claim_kind") == "CERTIFICATE"
                or index.get(a.get("target_ref"), {}).get("obligation_domain") == "MATHEMATICAL")
                else BIOLOGICAL_CEILINGS))
    )


def _authorization_tail(records, subject_ref, actions):
    """A linear append-only decision history, never an implicit latest timestamp."""
    events = [r for r in records if r.get("type") == "AuthorizationEvent"
              and r.get("subject_ref") == subject_ref
              and r.get("action") in actions]
    if not events:
        return None
    ids = {r["id"]: r for r in events}
    parents = {r.get("previous_event_ref") for r in events if r.get("previous_event_ref")}
    leaves = [r for r in events if r["id"] not in parents]
    if len(leaves) != 1:
        raise IntegrityError("Conflicting authorization history: " + str(subject_ref))
    seen = set()
    current = leaves[0]
    while current:
        if current["id"] in seen:
            raise IntegrityError("Authorization cycle: " + str(subject_ref))
        seen.add(current["id"])
        previous = current.get("previous_event_ref")
        if previous and previous not in ids:
            raise IntegrityError("Invalid authorization predecessor: " + str(subject_ref))
        current = ids.get(previous)
    if len(seen) != len(events):
        raise IntegrityError("Disconnected authorization chain: " + str(subject_ref))
    return leaves[0]


def kernel_freeze_basis_digest(records, ids):
    """Historical freeze evidence identified by explicit IDs, not live discovery."""
    index = {r["id"]: r for r in records}
    selected = set(ids)
    for ident in ids:
        rec = index.get(ident, {})
        if rec.get("type") in {"Requirement", "ResearchGap"} and rec.get("decision_ref"):
            selected.add(rec["decision_ref"])
            selected.update(index.get(rec["decision_ref"], {}).get("evidence_refs", []))
    if any(ident not in index for ident in selected):
        raise IntegrityError("Incomplete kernel basis")
    return sha256(canonical([index[i] for i in sorted(selected)]).encode())


def _historical_model_license_admission(records, index, event):
    model = index.get(event.get("subject_ref"), {})
    app = index.get(model.get("applicability_ref"), {})
    if not (model.get("type") == "ModelInstance"
            and model.get("status") == "FROZEN"
            and app.get("type") == "MethodApplicability"
            and app.get("assessment") == "APPLICABLE"
            and app.get("status") == "ACTIVE"
            and canonical(model.get("scope")) == canonical(event.get("scope"))
            and event.get("basis_digest") == model.get("frozen_digest")
            and model.get("identity_algorithm") == MODEL_IDENTITY_ALGORITHM
            and event.get("basis_refs") == [model.get("id")]):
        return False
    assumptions = [index.get(x, {}) for x in model.get("assumption_refs", [])]
    if not assumptions or any(
            a.get("required", True) and
            (a.get("assessment") != "PASS" or a.get("status") != "RECORDED")
            for a in assumptions):
        return False
    refs = set(event.get("evidence_refs", []))
    return bool(refs) and all(any(
        a.get("type") == "EvidenceAssessment"
        and a.get("evidence_ref") == ref
        and _qualified_assessment(
            index, a, model["id"], event["scope"],
            allowed_classes={"ANALYTIC", "FORMAL"},
            allowed_ceilings={"METHODOLOGICAL", "MATHEMATICAL_EXACT"},
            assessment_role="MODEL")
        for a in records) for ref in refs)


def effective_model_state(records, model):
    """Frozen specification and current model license are separate objects."""
    raw = model.get("status", "DRAFT")
    index = {r["id"]: r for r in records}
    event = _authorization_tail(records, model.get("id"),
                                {"ADMIT_MODEL", "RETIRE_MODEL"})
    if event is None:
        return {"declared": raw, "effective": raw, "authorization_ref": None}
    if event["action"] == "RETIRE_MODEL":
        return {"declared": raw, "effective": "RETIRED",
                "authorization_ref": event["id"]}
    retracted = approved_retractions(records, index)
    revoked = sorted(set(event.get("evidence_refs", [])) & set(retracted))
    data_contested = any(
        effective_data_use_state(records, du, retracted)["effective"] == "CONTESTED"
        for du in records if du.get("type") == "DataUse"
        and du.get("model_instance_ref") == model.get("id"))
    app = index.get(model.get("applicability_ref"), {})
    current = not (revoked or data_contested) and (
        app.get("status") == "ACTIVE" and app.get("assessment") == "APPLICABLE")
    return {"declared": raw, "effective": "ADMITTED" if current else "CONTESTED",
            "authorization_ref": event["id"], "retracted_support_refs": revoked}


def effective_obligation_state(records, obligation, retractions=None, historical=False):
    """Historical disposition remains; present evidential license can disappear."""
    raw = obligation.get("status", "OPEN")
    if raw not in {"RESOLVED", "SATISFIED", "BOUNDED"}:
        return {"declared": raw, "effective": raw,
                "retracted_support_refs": [], "contradiction_refs": []}
    index = {r["id"]: r for r in records}
    decision = index.get(obligation.get("decision_ref"), {})
    scope = (obligation.get("bound_scope") if raw == "BOUNDED"
             else decision.get("disposition_scope"))
    effects = ({"CONSTRAINS", "DOES_NOT_ESTABLISH"} if raw == "BOUNDED"
               else {"SUPPORTS"})
    issues = _decision_admission_errors(
        records, index, decision, obligation.get("id"), scope, effects,
        required_evidence_refs=(obligation.get("satisfaction_evidence_refs", [])
                                if obligation.get("type") == "Requirement" else None))
    retractions = approved_retractions(records, index) if retractions is None else retractions
    revoked = [] if historical else sorted(set(decision.get("evidence_refs", [])) & set(retractions))
    contradictions = ([] if historical else _material_scoped_contradictions(
        records, index, [obligation.get("id")], scope))
    effective = ("UNADMITTED" if issues else
                 "CONTESTED" if revoked or contradictions else
                 "ADMITTED_" + raw)
    return {"declared": raw, "effective": effective,
            "retracted_support_refs": revoked, "contradiction_refs": contradictions,
            "historical_admission_issues": issues}


def effective_freeze_eligibility(records, critical_gap_ids=None, historical=False):
    """Require CURRENT supported dispositions for all configured freeze burdens."""
    index = {r["id"]: r for r in records}
    programmes = [r for r in records if r.get("type") == "Programme"]
    programme = programmes[0] if len(programmes) == 1 else {}
    gaps = ([("ooc:gap:" + x if not x.startswith("ooc:") else x)
             for x in critical_gap_ids]
            if critical_gap_ids is not None else
            [r["id"] for r in records if r.get("type") == "ResearchGap"
             and r.get("priority") == "CRITICAL"])
    retractions = approved_retractions(records, index)
    requirement_states, gap_states, blockers = {}, {}, []
    for gap_ref in sorted(set(gaps)):
        gap = index.get(gap_ref, {})
        matching = [r for r in records if r.get("type") == "Requirement"
                    and r.get("gap_ref") == gap_ref
                    and r.get("subject_ref") == programme.get("id")]
        if gap.get("type") != "ResearchGap" or len(matching) != 1:
            blockers.append(gap_ref)
            continue
        req = matching[0]
        gs = effective_obligation_state(records, gap, retractions, historical)
        qs = effective_obligation_state(records, req, retractions, historical)
        gap_states[gap_ref] = gs
        requirement_states[req["id"]] = qs
        matches = (
            gap.get("status") in {"RESOLVED", "BOUNDED"}
            and req.get("status") in {"SATISFIED", "BOUNDED"}
            and (gap.get("status") == "RESOLVED") == (req.get("status") == "SATISFIED")
            and canonical(gap.get("obligation_scope")) == canonical(req.get("obligation_scope"))
            and gap.get("obligation_domain") == req.get("obligation_domain")
            and gap.get("obligation_claim_kind") == req.get("obligation_claim_kind")
            and (gap.get("status") != "BOUNDED" or
                 canonical(gap.get("bound_scope")) == canonical(req.get("bound_scope")))
        )
        if not (matches and gs["effective"].startswith("ADMITTED_")
                and qs["effective"].startswith("ADMITTED_")):
            blockers.append(gap_ref)
    # Additional programme requirements may be stricter than the critical subset.
    for req in records:
        if (req.get("type") == "Requirement"
                and req.get("subject_ref") == programme.get("id")
                and req.get("gap_ref") not in set(gaps)):
            qs = effective_obligation_state(records, req, retractions, historical)
            requirement_states[req["id"]] = qs
            if not qs["effective"].startswith("ADMITTED_"):
                blockers.append(req.get("gap_ref", req["id"]))
    authorized = False
    if programme and not historical:
        event = _authorization_tail(records, programme.get("id"),
                                    {"FREEZE_KERNEL", "UNFREEZE_KERNEL"})
        authorized = bool(event and event.get("action") == "FREEZE_KERNEL")
    return {"eligible": bool(programme) and bool(gaps) and not blockers,
            "blocking_gap_refs": sorted(set(blockers)),
            "gap_states": gap_states,
            "requirement_states": requirement_states,
            "declared_kernel_frozen": bool(programme.get("kernel_frozen")),
            "freeze_authorized_by_event": authorized,
            "effective_kernel_frozen": (bool(programme.get("kernel_frozen"))
                                        or authorized) and not blockers}


def effective_transition_state(records, transition):
    """The current scoped admission of a biological transition, not its raw label."""
    declared = transition.get("status", "OPEN")
    if declared != "SUPPORTED_SCOPED":
        return {"declared": declared, "effective": declared, "contradiction_refs": []}
    index = {r["id"]: r for r in records}
    scope = transition.get("scope")
    contradictions = _material_scoped_contradictions(
        records, index, [transition.get("id")], scope)
    retracted = _retracted_support_refs(
        records, index, list(transition.get("evidence_assessment_refs", []))
        + ([transition["context_transition_assessment_ref"]]
           if transition.get("context_transition_assessment_ref") else []))
    qualified = _admitted_transition_assessments(records, index, transition, scope)
    effective = ("CONTESTED" if (contradictions or retracted) else
                 "ADMITTED_SUPPORTED_SCOPED" if qualified else "UNADMITTED")
    return {"declared": declared, "effective": effective,
            "contradiction_refs": contradictions, "retracted_support_refs": retracted}


def effective_route_state(records, route):
    """Current projection, not a mutation of immutable historical declarations."""
    declared = route.get("status", "OPEN")
    if declared != "CLOSED":
        return {"declared": declared, "effective": declared, "contradiction_refs": []}
    index = {r["id"]: r for r in records}
    targets = [route["id"], route.get("founder_ref")] + list(route.get("transition_refs", []))
    contradictions = _material_scoped_contradictions(records, index, targets, route.get("scope"))
    refs = []
    for tr in route.get("transition_refs", []):
        transition = index.get(tr, {})
        refs.extend(ref for ref in transition.get("evidence_assessment_refs", [])
                    if canonical(index.get(ref, {}).get("scope")) == canonical(route.get("scope")))
        if transition.get("context_transition_assessment_ref"):
            refs.append(transition["context_transition_assessment_ref"])
    refs.extend(ref for ref in index.get(route.get("founder_ref"), {}).get("ancestry_assessment_refs", [])
                if canonical(index.get(ref, {}).get("scope")) == canonical(route.get("scope")))
    for link in index.get(route.get("witness_bundle_ref"), {}).get("bridge_links", []):
        if isinstance(link, dict):
            refs.append(link.get("assessment_ref"))
    retracted = _retracted_support_refs(records, index, refs)
    return {"declared": declared,
            "effective": "CONTESTED" if (contradictions or retracted) else "ADMITTED_CLOSED",
            "contradiction_refs": contradictions, "retracted_support_refs": retracted}


def _effective_pan_cancer_transfer(records, index, verdict):
    """Recheck independent surviving support for every transfer adapter."""
    transfer = index.get(verdict.get("transfer_decision_ref"), {})
    if transfer.get("type") != "Decision" or transfer.get("decision") != "ALLOW_TRANSFER":
        return False
    refs = set(transfer.get("evidence_refs", []))
    retracted = approved_retractions(records, index)
    adapters = {r["id"] for r in records if r.get("type") == "Adapter"}
    if not adapters or set(transfer.get("transfer_adapter_refs", [])) != adapters:
        return False
    subject = index.get(verdict.get("subject_ref"), {})
    kind = ("HISTORICAL_ROUTE" if subject.get("type") == "Route"
            and subject.get("claim_kind") == "HISTORICAL" else
            "ROUTE" if subject.get("type") == "Route" else subject.get("claim_kind"))
    options = {}
    for adapter in adapters:
        scope = _adapter_scientific_scope(verdict.get("scope"), adapter)
        options[adapter] = {
            (e.get("study_id"), e.get("system_id"))
            for a in records if a.get("type") == "EvidenceAssessment"
            for e in [index.get(a.get("evidence_ref"), {})]
            if e.get("id") in refs and e.get("id") not in retracted
            and _appropriate_biological_assessment(
                index, a, verdict.get("subject_ref"), scope, kind)
        }
        if not options[adapter]:
            return False
    def independent(remaining, used):
        if not remaining:
            return True
        return any(k not in used and independent(remaining[1:], used | {k})
                   for k in options[remaining[0]])
    return independent(sorted(adapters), set())


def _normalized_source_identifiers(raw):
    """Normalize complete DOI / PMID / PMCID / URL identifiers, never substrings."""
    from urllib.parse import urlsplit, unquote
    if not isinstance(raw, str):
        return set()
    ids = set()
    for match in re.finditer(r"https?://[^\s;|<>]+", raw, re.I):
        url = match.group(0).rstrip(".,);]")
        parts = urlsplit(url)
        if parts.hostname and parts.hostname.lower() in {"doi.org", "dx.doi.org"}:
            doi = unquote(parts.path).strip("/").lower()
            if re.fullmatch(r"10\.\d{4,9}/\S+", doi):
                ids.add("doi:" + doi)
        elif parts.hostname:
            ids.add("url:" + parts.scheme.lower() + "://" + parts.netloc.lower() + parts.path.rstrip("/") + ("?" + parts.query if parts.query else ""))
    for match in re.finditer(r"(?<![a-z0-9])10\.\d{4,9}/[^\s;,|<>]+", raw, re.I):
        ids.add("doi:" + match.group(0).rstrip(".,);]").lower())
    for match in re.finditer(r"\bPMCID\s*:?[\s]*(PMC\d+)\b|\b(PMC\d+)\b", raw, re.I):
        ids.add("pmcid:" + (match.group(1) or match.group(2)).upper())
    for match in re.finditer(r"\bPMID\s*:?\s*(\d+)\b", raw, re.I):
        ids.add("pmid:" + match.group(1))
    return ids


def effective_source_verification_state(records, source, retractions=None):
    """A historical VERIFIED source is not CURRENTLY verified after revocation.

    Multiple independent valid receipts can survive retraction of one receipt.
    Registered citations and metadata verification are not paper extraction.
    """
    raw = source.get("bibliographic_verification", "UNVERIFIED")
    if raw != "VERIFIED":
        return {"declared": raw, "effective": raw,
                "active_verification_refs": [], "retracted_verification_refs": []}
    index = {r["id"]: r for r in records}
    retractions = approved_retractions(records, index) if retractions is None else retractions
    candidate = [index.get(ref, {}) for ref in source.get("verification_refs", [])]
    verified = [
        v["id"] for v in candidate
        if v.get("type") == "SourceVerification"
        and v.get("status") == "VERIFIED"
        and v.get("source_ref") == source.get("id")
        and v.get("verification_scope") == "BIBLIOGRAPHIC_METADATA"
        and len(_normalized_source_identifiers(v.get("identifier_checked", ""))) == 1
        and _normalized_source_identifiers(v.get("identifier_checked", "")).issubset(
            _normalized_source_identifiers(source.get("identifiers_raw", "")))
        and bool(v.get("canonical_metadata"))
        and v.get("public_source_url", "").startswith("https://")
        and v.get("provenance_class") not in NON_ADMISSIBLE_PROVENANCE
    ]
    current = sorted(ref for ref in verified if ref not in retractions)
    revoked = sorted(ref for ref in verified if ref in retractions)
    return {"declared": raw,
            "effective": "VERIFIED" if current else "CONTESTED",
            "active_verification_refs": current,
            "retracted_verification_refs": revoked}


def _nested_reference_errors(record, index, contract):
    """Every nested reference is typed, including objects not yet admitted."""
    violations = []
    type_name = record.get("type")
    def walk(obj, keypath, contractpath):
        if isinstance(obj, list):
            for child in obj:
                walk(child, keypath+"[]", contractpath+"[].items")
        elif isinstance(obj, dict):
            for key, value in obj.items():
                loc = keypath + "." + key
                contract_key = contractpath + ".properties." + key
                if key.endswith("_ref") or key.endswith("_refs"):
                    allowed = contract.get(type_name + "." + contract_key)
                    if allowed is None:
                        violations.append("UNDECLARED_NESTED_REF:"+loc)
                    else:
                        refs = value if key.endswith("_refs") else [value]
                        if not isinstance(refs, list):
                            violations.append("MALFORMED_NESTED_REF:"+loc)
                            continue
                        for ref in refs:
                            if not isinstance(ref, str) or ref not in index:
                                violations.append("MISSING_NESTED_REF:"+loc)
                            elif index[ref].get("type") not in allowed:
                                violations.append("WRONG_NESTED_REF_TYPE:"+loc)
                elif isinstance(value,(dict,list)):
                    walk(value,loc,contract_key)
    for key,value in record.items():
        # Arbitrary scope/configuration data may contain descriptive keys ending
        # in _refs. Only schema-declared nested structures are graph references.
        if isinstance(value,(list,dict)) and any(
                k.startswith(type_name+"."+key+"[") or
                k.startswith(type_name+"."+key+".") for k in contract):
            walk(value,key,key)
    return violations


def validate_records(records: list[dict], root: Path | None = None) -> list[str]:
    """Return integrity violations; scientific incompleteness is not a violation."""
    errors = []
    ids = [r.get("id") for r in records]
    if len(ids) != len(set(ids)): errors.append("DUPLICATE_ID")
    index = {r.get("id"): r for r in records}
    if root is not None and (root / "config/project.json").is_file():
        project_config = loads((root / "config/project.json").read_text())
        configured_critical_gap_refs = {"ooc:gap:"+x for x in project_config.get("critical_gap_ids", [])}
    else:
        configured_critical_gap_refs = {r.get("id") for r in records
                                        if r.get("type") == "ResearchGap" and r.get("priority") == "CRITICAL"}
    if root is not None:
        from jsonschema import Draft202012Validator
        schema = loads((root / "schema/graph-record.schema.json").read_text())
        vocab = loads((root / "schema/vocab.json").read_text())
        validators = {t: Draft202012Validator(s) for t, s in schema["$defs"].items()}
        for model_type, followed in MODEL_IDENTITY_FORWARD_REFS.items():
            definition = schema["$defs"].get(model_type, {})
            declared_refs = {k for k in definition.get("properties", {})
                             if (k.endswith("_ref") or k.endswith("_refs"))
                             and k != "revision_of_ref"}
            excluded = MODEL_IDENTITY_REFERENCE_EXCLUSIONS.get(model_type,set())
            if declared_refs - followed - excluded:
                errors.append("UNDECLARED_MODEL_IDENTITY_REFERENCE:" + model_type
                              + ":" + ",".join(sorted(declared_refs-followed-excluded)))
        for schema_type, definition in schema["$defs"].items():
            for key in definition.get("properties", {}):
                if key.endswith("_ref") or key == "same_identifier_as":
                    if _allowed_ref_types(schema_type, key, False) is None:
                        errors.append(f"UNDECLARED_REF_TYPE:{schema_type}:{key}")
                elif key.endswith("_refs"):
                    if _allowed_ref_types(schema_type, key, True) is None:
                        errors.append(f"UNDECLARED_REF_TYPE:{schema_type}:{key}")
        nested_contract = loads((root/"schema/nested_reference_contract.json").read_text())
        def check_nested_schema(obj, path):
            if not isinstance(obj, dict):
                return
            final = path.rsplit(".",1)[-1]
            if path.count(".properties.") >= 1 and (
                    final.endswith("_ref") or final.endswith("_refs")):
                if obj.get("x-ooc-target-types") != nested_contract.get(path):
                    errors.append("NESTED_REFERENCE_CONTRACT_DRIFT:"+path)
            for key, sub in obj.get("properties", {}).items():
                check_nested_schema(sub, path+".properties."+key)
            if "items" in obj:
                check_nested_schema(obj["items"], path+"[].items")
        for type_name, definition in schema["$defs"].items():
            for field_name, node in definition.get("properties", {}).items():
                if "items" in node or "properties" in node:
                    check_nested_schema(node, type_name+".properties."+field_name)
        for r in records:
            validator = validators.get(r.get("type"))
            if validator is None: errors.append(f"UNKNOWN_TYPE:{r.get('id')}"); continue
            for e in validator.iter_errors(r): errors.append(f"SCHEMA:{r.get('id')}:{list(e.path)}:{e.message}")
        if errors: return sorted(set(errors))
    else: vocab = None
    def error(code, record): errors.append(f"{code}:{record.get('id')}")
    def check_ref(record, key, value, allowed=None):
        if not isinstance(value, str) or value not in index: error("MISSING_REF:"+key, record)
        elif allowed and index[value]["type"] not in allowed: error("WRONG_REF_TYPE:"+key, record)
    ref_root = root if root is not None else Path(__file__).resolve().parents[1]
    nested_contract = loads((ref_root/"schema/nested_reference_contract.json").read_text())
    for r in records:
        for violation in _nested_reference_errors(r,index,nested_contract):
            error(violation,r)
    for r in records:
        typ = r.get("type")
        for key, value in r.items():
            if key.endswith("_ref") or key == "same_identifier_as":
                allowed = _allowed_ref_types(typ, key, False)
                if allowed is None: error("UNDECLARED_REF_TYPE:"+key, r)
                else: check_ref(r, key, value, allowed)
            elif key.endswith("_refs"):
                if not isinstance(value, list): error("INVALID_REFS:"+key, r); continue
                allowed = _allowed_ref_types(typ, key, True)
                if allowed is None: error("UNDECLARED_REF_TYPE:"+key, r)
                else:
                    for ref in value: check_ref(r, key, ref, allowed)
        if r.get("provenance_class") == "TEXTUAL_HINT" and (
            r.get("decision") in SCIENTIFIC_POSITIVE or r.get("status") in {"ADMITTED", "CLOSED"}):
            error("TEXT_HINT_PROMOTION", r)
        if root:
            for field in ("path", "doc_path"):
                if field in r:
                    try:
                        if not safe_path(root, r[field]).is_file(): error("MISSING_PATH:"+field, r)
                    except IntegrityError: error("UNSAFE_PATH:"+field, r)
        if typ == "Relation":
            check_ref(r, "source", r.get("source")); check_ref(r, "target", r.get("target"))
            if vocab and r.get("kind") not in vocab["relation_types"]: error("UNKNOWN_RELATION_KIND", r)
            if r.get("kind") in {"SUPPORTS", "CONTRADICTS", "DOES_NOT_ESTABLISH"}:
                a = index.get(r.get("assessment_ref"), {})
                if a.get("type") != "EvidenceAssessment": error("UNASSESSED_EVIDENCE_EDGE", r)
                elif (a.get("evidence_ref") != r.get("source") or a.get("target_ref") != r.get("target")
                      or a.get("effect") != r.get("kind")):
                    error("ASSESSMENT_EDGE_MISMATCH", r)
                elif r.get("kind") == "SUPPORTS" and not (
                    a.get("status") == "ADJUDICATED"
                    and index.get(a.get("evidence_ref"),{}).get("status") == "RECORDED"
                    and canonical(a.get("scope")) == canonical(r.get("scope"))
                    and a.get("provenance_class") not in NON_ADMISSIBLE_PROVENANCE
                    and index.get(a.get("evidence_ref"),{}).get("provenance_class") not in NON_ADMISSIBLE_PROVENANCE):
                    error("UNADMITTED_SUPPORT_RELATION", r)
        if typ == "AuthorizationEvent":
            subject = index.get(r.get("subject_ref"), {})
            authority = index.get(r.get("authority_ref"), {})
            action = r.get("action")
            model_event = action in {"ADMIT_MODEL", "RETIRE_MODEL"}
            kernel_event = action in {"FREEZE_KERNEL", "UNFREEZE_KERNEL"}
            previous = index.get(r.get("previous_event_ref"), {})
            if not (authority.get("type") == "Authority"
                    and authority.get("status") == "ACTIVE_RULE"
                    and ("EVIDENCE_POLICY" in authority.get("axes", []) if model_event
                         else "RESEARCH_POLICY" in authority.get("axes", []))
                    and (subject.get("type") == "ModelInstance" if model_event
                         else subject.get("type") == "Programme")
                    and r.get("provenance_class") not in NON_ADMISSIBLE_PROVENANCE
                    and canonical(authority.get("scope")) == canonical(r.get("scope"))
                    and (not authority.get("subject_refs")
                         or r.get("subject_ref") in authority.get("subject_refs", []))):
                error("INVALID_AUTHORIZATION_EVENT", r)
            if r.get("previous_event_ref"):
                expected = ({"ADMIT_MODEL"} if action == "RETIRE_MODEL" else
                            {"RETIRE_MODEL"} if action == "ADMIT_MODEL" else
                            {"FREEZE_KERNEL"} if action == "UNFREEZE_KERNEL" else
                            {"UNFREEZE_KERNEL"})
                if (previous.get("type") != "AuthorizationEvent"
                    or previous.get("subject_ref") != r.get("subject_ref")
                    or previous.get("action") not in expected):
                    error("BROKEN_AUTHORIZATION_HISTORY", r)
            elif action in {"RETIRE_MODEL", "UNFREEZE_KERNEL"}:
                error("MISSING_AUTHORIZATION_PREDECESSOR", r)
            if action == "ADMIT_MODEL":
                if (root is not None and (root/"config/project.json").is_file()
                    and any(index.get(ref,{}).get("evidence_class") == "FORMAL"
                            and not trusted_proof_receipt(
                                root,index,index.get(index.get(ref,{}).get("result_ref"),{}))
                            for ref in r.get("evidence_refs", []))):
                    error("UNTRUSTED_FORMAL_MODEL_ADMISSION", r)
                if not _historical_model_license_admission(records, index, r):
                    error("UNQUALIFIED_MODEL_ADMISSION", r)
            if action == "RETIRE_MODEL" and (
                    r.get("basis_digest") != subject.get("frozen_digest") or
                    r.get("basis_refs") != [subject.get("id")]):
                error("RETIREMENT_IDENTITY_MISMATCH", r)
            if kernel_event:
                try:
                    if r.get("basis_digest") != kernel_freeze_basis_digest(
                            records, r.get("basis_refs", [])):
                        error("KERNEL_BASIS_MISMATCH", r)
                except IntegrityError:
                    error("INCOMPLETE_KERNEL_BASIS", r)
                if action == "FREEZE_KERNEL":
                    expected_gaps = configured_critical_gap_refs
                    included_gaps = {x for x in r.get("basis_refs", [])
                                     if index.get(x, {}).get("type") == "ResearchGap"}
                    included_reqs = {x for x in r.get("basis_refs", [])
                                     if index.get(x, {}).get("type") == "Requirement"}
                    required = {q["id"] for q in records
                                if q.get("type") == "Requirement"
                                and q.get("gap_ref") in expected_gaps
                                and q.get("subject_ref") == subject.get("id")}
                    if included_gaps != expected_gaps or included_reqs != required:
                        error("INCOMPLETE_KERNEL_FREEZE_BASIS", r)
                    historic = effective_freeze_eligibility(
                        records, sorted(expected_gaps), historical=True)
                    if not historic["eligible"]:
                        error("UNQUALIFIED_KERNEL_FREEZE", r)
        if typ == "LiteratureSource":
            if r.get("bibliographic_verification") == "VERIFIED":
                verifications = [
                    index.get(ref,{}) for ref in r.get("verification_refs",[])
                    if isinstance(ref,str)
                ]
                if not verifications or not any(
                    v.get("type") == "SourceVerification"
                    and v.get("status") == "VERIFIED"
                    and v.get("source_ref") == r.get("id")
                    and v.get("verification_scope") == "BIBLIOGRAPHIC_METADATA"
                    and len(_normalized_source_identifiers(v.get("identifier_checked",""))) == 1
                    and _normalized_source_identifiers(v.get("identifier_checked","")).issubset(
                        _normalized_source_identifiers(r.get("identifiers_raw","")))
                    and bool(v.get("canonical_metadata"))
                    and v.get("public_source_url","").startswith("https://")
                    and v.get("provenance_class") not in NON_ADMISSIBLE_PROVENANCE
                    for v in verifications):
                    error("UNBACKED_SOURCE_VERIFICATION",r)
        if typ in {"ResearchGap", "Requirement"} and r.get("status") in {"RESOLVED", "SATISFIED", "BOUNDED", "SUPERSEDED"}:
            decision = index.get(r.get("decision_ref"), {})
            if decision.get("type") != "Decision" or decision.get("subject_ref") != r.get("id"):
                error("UNADJUDICATED_CLOSURE", r)
            if r.get("status") == "BOUNDED" and not r.get("bound_scope"):
                error("UNSCOPED_REQUIREMENT_BOUND", r)
            if r.get("status") in {"RESOLVED", "SATISFIED", "BOUNDED"}:
                scientific_scope = (
                    r.get("bound_scope") if r.get("status") == "BOUNDED"
                    else decision.get("disposition_scope"))
                effects = ({"SUPPORTS"} if r.get("status") in {"RESOLVED", "SATISFIED"}
                           else {"CONSTRAINS", "DOES_NOT_ESTABLISH"})
                registered_refs = (r.get("satisfaction_evidence_refs", [])
                                   if typ == "Requirement" else None)
                issues = _decision_admission_errors(
                    records, index, decision, r.get("id"), scientific_scope,
                    effects, required_evidence_refs=registered_refs)
                for issue in issues:
                    error("INVALID_SCIENTIFIC_DISPOSITION:"+issue, r)
        if typ in {"Theory", "Adapter"} and (r.get("card_complete") or r.get("dossier_complete")):
            decision = index.get(r.get("completion_decision_ref"), {})
            authority = index.get(decision.get("authority_ref"), {})
            expected_kind = ("THEORY_CARD_COMPLETION" if typ == "Theory" else "ADAPTER_DOSSIER_COMPLETION")
            requirements = [index.get(ref,{}) for ref in r.get("completion_requirement_refs",[])]
            if (decision.get("type") != "Decision" or decision.get("subject_ref") != r.get("id")
                or decision.get("decision_kind") != expected_kind
                or decision.get("decision") != "COMPLETE"
                or decision.get("status") != "RECORDED"
                or authority.get("status") != "ACTIVE_RULE"
                or "EVIDENCE_POLICY" not in authority.get("axes",[])
                or canonical(decision.get("scope")) != canonical(authority.get("scope"))
                or (authority.get("subject_refs") and r.get("id") not in authority.get("subject_refs",[]))
                or not requirements
                or any(q.get("type") != "Requirement" or q.get("subject_ref") != r.get("id")
                       or q.get("status") != "SATISFIED" for q in requirements)):
                error("UNADJUDICATED_DOCUMENT_COMPLETION", r)
            for evidence_ref in decision.get("evidence_refs",[]):
                if not any(a.get("type") == "EvidenceAssessment"
                           and a.get("evidence_ref") == evidence_ref
                           and _qualified_assessment(index,a,r.get("id"),decision.get("scope"),
                               allowed_classes=BIOLOGICAL_EVIDENCE_CLASSES | {"REVIEW"},
                               allowed_ceilings={"METHODOLOGICAL"},assessment_role="DOCUMENT_COMPLETION")
                           for a in records):
                    error("UNSUPPORTED_DOCUMENT_COMPLETION", r)
            if not decision.get("evidence_refs"):
                error("UNSUPPORTED_DOCUMENT_COMPLETION", r)
        if (typ in {"ResearchGap", "Requirement"}
                and r.get("status") in {"RESOLVED", "SATISFIED", "BOUNDED"}
                and r.get("obligation_domain") == "MATHEMATICAL"
                and root is not None and (root/"config/project.json").is_file()):
            decision = index.get(r.get("decision_ref"), {})
            proofs = [index.get(index.get(e, {}).get("result_ref"), {})
                      for e in decision.get("evidence_refs", [])]
            if not proofs or not all(
                    x.get("type") == "Result" and trusted_proof_receipt(root,index,x)
                    for x in proofs):
                error("UNTRUSTED_MATHEMATICAL_DISPOSITION", r)
        if typ == "Result" and r.get("verification_mode") == "FORMAL_PROOF":
            artifact = index.get(r.get("verification_artifact_ref"), {})
            receipt = r.get("verification_receipt", {})
            if artifact.get("type") != "SourceArtifact" or not artifact.get("sha256"):
                error("UNHASHED_PROOF_ARTIFACT", r)
            if isinstance(receipt, dict) and receipt.get("artifact_sha256") != artifact.get("sha256"):
                error("PROOF_RECEIPT_ARTIFACT_MISMATCH", r)
            if root is not None and artifact.get("path"):
                try:
                    proof_path = safe_path(root, artifact["path"])
                    if not proof_path.is_file() or sha256(proof_path.read_bytes()) != artifact.get("sha256"):
                        error("PROOF_ARTIFACT_BYTE_DRIFT", r)
                except (IntegrityError, OSError):
                    error("INVALID_PROOF_ARTIFACT_PATH", r)
            exe = index.get(r.get("execution_ref"), {})
            output = index.get(exe.get("output_artifact_ref"), {})
            if (output.get("type") != "SourceArtifact"
                or not output.get("sha256")
                or output.get("sha256") != exe.get("output_sha256")):
                error("UNBOUND_EXECUTION_OUTPUT", r)
            if root is not None and output.get("path"):
                try:
                    output_path = safe_path(root, output["path"])
                    if (not output_path.is_file()
                        or sha256(output_path.read_bytes()) != output.get("sha256")):
                        error("EXECUTION_OUTPUT_BYTE_DRIFT", r)
                except (IntegrityError, OSError):
                    error("INVALID_EXECUTION_OUTPUT_PATH", r)
            software = index.get(exe.get("software_ref"), {})
            if root is not None and software.get("path"):
                try:
                    verifier_path = safe_path(root, software["path"])
                    if not verifier_path.is_file() or sha256(verifier_path.read_bytes()) != software.get("sha256"):
                        error("VERIFIER_SOFTWARE_BYTE_DRIFT", r)
                except (IntegrityError, OSError):
                    error("INVALID_VERIFIER_SOFTWARE_PATH", r)
        if typ == "EvidenceAssessment" and r.get("status") == "ADJUDICATED":
            if r.get("effect") == "RETRACTS":
                authorizations = _authorized_retractions(records, index)
                if r.get("id") not in authorizations.get(r.get("target_ref"), []):
                    error("UNAUTHORIZED_RETRACTION", r)
            if r.get("effect") == "REINSTATES":
                if r.get("target_ref") not in approved_reinstatements(records, index):
                    error("UNAUTHORIZED_REINSTATEMENT", r)
        if typ == "EvidenceObject":
            if not r.get("source_locator_refs"): error("UNLOCATED_EVIDENCE", r)
            for lr in r.get("source_locator_refs", []):
                selector = index.get(lr, {}).get("selector", {})
                if "sheet" in selector and selector["sheet"] in {"Anchor Sources", "Theory Queue"}:
                    error("BIBLIOGRAPHY_AS_FINDING", r)
        if typ == "Transition" and r.get("status") == "SUPPORTED_SCOPED":
            if not isinstance(r.get("scope"), dict) or not r["scope"]:
                error("UNSCOPED_SUPPORTED_TRANSITION", r)
            if not _transition_context_valid(index, r):
                error("INVALID_STANDALONE_TRANSITION_CONTEXT", r)
            if not _admitted_transition_assessments(records, index, r, r.get("scope")):
                error("UNSUPPORTED_STANDALONE_TRANSITION", r)
        if typ == "MethodApplicability" and r.get("assessment") == "APPLICABLE":
            if not r.get("assumption_refs"): error("MISSING_APPLICABILITY_ASSUMPTIONS", r)
            for ar in r.get("assumption_refs", []):
                assumption = index.get(ar, {})
                if assumption.get("required", True) and assumption.get("assessment") != "PASS":
                    error("FAILED_OR_UNKNOWN_REQUIRED_ASSUMPTION", r)
        if typ == "ModelInstance" and r.get("status") in {"ADMITTED", "FROZEN", "RETIRED"}:
            if (r.get("status") == "ADMITTED" and root is not None
                    and (root / "config/project.json").is_file()):
                error("DIRECT_MODEL_ADMISSION_FORBIDDEN", r)
            if not r.get("protocol_refs"):
                error("UNBOUND_MODEL_PROTOCOL", r)
            app = index.get(r.get("applicability_ref"), {})
            if r.get("identity_algorithm") != MODEL_IDENTITY_ALGORITHM:
                error("UNVERSIONED_MODEL_IDENTITY", r)
            if r.get("status") == "ADMITTED":
                if app.get("assessment") != "APPLICABLE" or app.get("status") != "ACTIVE":
                    error("UNLICENSED_MODEL", r)
            if not r.get("frozen_digest") or not re.fullmatch("[0-9a-f]{64}", r["frozen_digest"]):
                error("MISSING_MODEL_IDENTITY", r)
            else:
                try:
                    if r['frozen_digest'] != model_identity_digest(records,r): error("MODEL_IDENTITY_MISMATCH",r)
                except IntegrityError: error("INCOMPLETE_MODEL_IDENTITY",r)
            if app.get("model_class_ref") != r.get("model_class_ref"): error("APPLICABILITY_MODEL_MISMATCH",r)
            if app.get("scope") != r.get("scope"): error("APPLICABILITY_SCOPE_MISMATCH",r)
            declared = _valid_ref_list(r.get("assumption_refs"))
            applied = _valid_ref_list(app.get("assumption_refs"))
            required_from_equations = set()
            for er in r.get("equation_refs", []):
                eq = index.get(er, {})
                eq_assumptions = _valid_ref_list(eq.get("assumption_refs"))
                if eq_assumptions is None:
                    error("MALFORMED_EQUATION_ASSUMPTIONS", r)
                else:
                    required_from_equations.update(eq_assumptions)
            if r.get("status") == "ADMITTED" and app.get("status") != "ACTIVE":
                error("INACTIVE_MODEL_APPLICABILITY", r)
            if declared is None or applied is None:
                error("MALFORMED_MODEL_ASSUMPTIONS", r)
            else:
                if declared != applied:
                    error("APPLICABILITY_ASSUMPTION_MISMATCH", r)
                if not required_from_equations.issubset(declared):
                    error("UNDECLARED_EQUATION_ASSUMPTION", r)
                for ar in sorted(declared | required_from_equations):
                    assumption = index.get(ar, {})
                    if (r.get("status") == "ADMITTED" and assumption.get("required", True) and
                        (assumption.get("assessment") != "PASS" or assumption.get("status") != "RECORDED")):
                        error("FAILED_OR_UNKNOWN_MODEL_ASSUMPTION", r)
        if typ == "Route" and r.get("status") == "CLOSED":
            if r.get("unresolved_segments"): error("ROUTE_HAS_DEBT", r)
            transitions = r.get("transition_refs", [])
            if not transitions: error("EMPTY_CLOSED_ROUTE", r)
            if not r.get("founder_ref"): error("MISSING_ROUTE_ANCESTRY", r)
            scope = r.get("scope")
            if not isinstance(scope, dict) or not scope: error("MISSING_ROUTE_SCOPE", r)
            boundary = index.get(r.get("boundary_ref"), {})
            founder = index.get(r.get("founder_ref"), {})
            if boundary.get("context_ref") != r.get("context_ref"):
                error("ROUTE_BOUNDARY_CONTEXT_MISMATCH", r)
            if not _founder_context_ok(index,r.get("founder_ref"),r.get("context_ref")):
                error("ROUTE_FOUNDER_CONTEXT_MISMATCH", r)
            if transitions:
                first_state = index.get(transitions[0], {}).get("source_state_ref")
                if index.get(first_state,{}).get("context_ref") != r.get("context_ref"):
                    error("ROUTE_INITIAL_STATE_CONTEXT_MISMATCH", r)
                if first_state not in boundary.get("state_refs", []):
                    error("ROUTE_BOUNDARY_NOT_ANCHORED", r)
                if first_state not in _founder_states(index, r.get("founder_ref")):
                    error("ROUTE_FOUNDER_NOT_ANCHORED", r)
            wb = index.get(r.get("witness_bundle_ref"), {})
            mode = wb.get("mode")
            if mode not in {"SAME_SYSTEM", "VALIDATED_BRIDGE"}:
                error("COMPOSITED_ROUTE", r)
            if wb.get("context_ref") != r.get("context_ref"):
                error("WITNESS_CONTEXT_MISMATCH", r)
            witness_evidence = set(wb.get("evidence_refs", []))
            if not witness_evidence:
                error("EMPTY_WITNESS_EVIDENCE", r)
            previous = None
            current_context = r.get("context_ref")
            segment_witnesses = []
            for tr in transitions:
                t = index.get(tr, {})
                if t.get("context_ref") != r.get("context_ref") or t.get("adapter_ref") != r.get("adapter_ref"):
                    error("ROUTE_CONTEXT_MISMATCH", r)
                if canonical(t.get("scope")) != canonical(scope):
                    error("ROUTE_TRANSITION_SCOPE_MISMATCH", r)
                if not _transition_context_valid(index, t):
                    error("INVALID_ROUTE_TRANSITION_CONTEXT", r)
                source = index.get(t.get("source_state_ref"), {})
                target = index.get(t.get("target_state_ref"), {})
                sc, tc = source.get("context_ref"), target.get("context_ref")
                if sc != current_context:
                    error("BROKEN_ROUTE_CONTEXT_HANDOFF", r)
                if sc != tc:
                    a = index.get(t.get("context_transition_assessment_ref"), {})
                    e = index.get(a.get("evidence_ref"), {})
                    if not (
                        t.get("source_context_ref") == sc
                        and t.get("target_context_ref") == tc
                        and e.get("context_ref") in {sc, tc}
                        and _appropriate_biological_assessment(index, a, tr, scope, "TRANSITION")
                        and a.get("assessment_role") in {"TEMPORAL", "ANCESTRY", "CAUSAL"}
                    ):
                        error("UNVALIDATED_CONTEXT_TRANSITION", r)
                current_context = tc
                if t.get("status") != "SUPPORTED_SCOPED":
                    error("INACTIVE_ROUTE_TRANSITION", r)
                if previous is not None and previous != t.get("source_state_ref"):
                    error("BROKEN_ROUTE_HANDOFF", r)
                previous = t.get("target_state_ref")
                segment_supported = False
                witnesses = set()
                refs = t.get("evidence_assessment_refs", [])
                if not refs: error("UNSUPPORTED_ROUTE_SEGMENT", r)
                for ar in refs:
                    a = index.get(ar, {})
                    # Adjudications for other scopes belong to their own claim partition.
                    if canonical(a.get("scope")) != canonical(scope):
                        continue
                    e = index.get(a.get("evidence_ref"), {})
                    valid = True
                    if a.get("status") != "ADJUDICATED":
                        error("UNADJUDICATED_ROUTE_ASSESSMENT", r); valid = False
                    if a.get("target_ref") != tr:
                        error("ROUTE_ASSESSMENT_TARGET_MISMATCH", r); valid = False
                    if a.get("effect") != "SUPPORTS":
                        error("NON_SUPPORTING_ROUTE_ASSESSMENT", r); valid = False
                    if e.get("status") != "RECORDED":
                        error("INACTIVE_ROUTE_EVIDENCE", r); valid = False
                    if e.get("context_ref") not in {r.get("context_ref"), sc, tc}:
                        error("ROUTE_EVIDENCE_CONTEXT_MISMATCH", r); valid = False
                    if e.get("id") not in witness_evidence:
                        error("ROUTE_EVIDENCE_OUTSIDE_WITNESS", r); valid = False
                    route_kind = r.get("claim_kind", "CAUSAL")
                    evidence_kind = "ROUTE" if route_kind == "CAUSAL" else "HISTORICAL_ROUTE"
                    if not _appropriate_biological_assessment(
                            index, a, tr, scope, evidence_kind):
                        error("NONBIOLOGICAL_ROUTE_SUPPORT", r); valid = False
                    if valid:
                        segment_supported = True
                        witnesses.update(_witness_keys(e))
                if not segment_supported:
                    error("UNSUPPORTED_ROUTE_SEGMENT", r)
                # Scientific contradictions never make incoming evidence structurally
                # invalid. effective_route_state() projects this claim as CONTESTED.
                # Historical CLOSED declarations remain visible as historical records.
                segment_witnesses.append(witnesses)
            if mode == "SAME_SYSTEM":
                common = set.intersection(*segment_witnesses) if segment_witnesses else set()
                declared = set(wb.get("common_witness_ids", []))
                if not common or not declared or not declared.issubset({x[2] for x in common}):
                    error("MISSING_COMMON_WITNESS", r)
                if wb.get("bridge_links") or wb.get("bridge_evidence_refs"):
                    error("BRIDGE_EVIDENCE_NOT_ALLOWED_IN_SAME_SYSTEM", r)
            if mode == "VALIDATED_BRIDGE":
                bridge_evidence = set(wb.get("bridge_evidence_refs", []))
                links = wb.get("bridge_links", [])
                if not bridge_evidence or not links:
                    error("UNSUPPORTED_BRIDGE", r)
                valid_links = set()
                used_bridge_evidence = set()
                for link in links:
                    left, right = link.get("from_transition_ref"), link.get("to_transition_ref")
                    pair = (left, right)
                    if pair not in set(zip(transitions, transitions[1:])):
                        error("UNRELATED_BRIDGE_LINK", r)
                        continue
                    i = transitions.index(left)
                    e_ref, a_ref = link.get("evidence_ref"), link.get("assessment_ref")
                    a = index.get(a_ref, {})
                    e = index.get(e_ref, {})
                    from_key = (link.get("from_study_id"), link.get("from_system_id"),
                                link.get("from_witness_id"))
                    to_key = (link.get("to_study_id"), link.get("to_system_id"),
                              link.get("to_witness_id"))
                    bridge_pair = {
                        "from_study_id": from_key[0], "from_system_id": from_key[1],
                        "from_witness_id": from_key[2], "to_study_id": to_key[0],
                        "to_system_id": to_key[1], "to_witness_id": to_key[2]
                    }
                    if not (
                        e_ref in bridge_evidence
                        and from_key in segment_witnesses[i]
                        and to_key in segment_witnesses[i+1]
                        and bridge_pair in e.get("witness_bridge_pairs", [])
                        and a.get("evidence_ref") == e_ref
                        and _appropriate_biological_assessment(
                            index, a, r["id"], scope, "ROUTE",
                            context_ref=r.get("context_ref"))
                    ):
                        error("INVALID_BRIDGE_LINK", r)
                    else:
                        valid_links.add(pair)
                        used_bridge_evidence.add(e_ref)
                for i in range(max(0, len(transitions)-1)):
                    if not (segment_witnesses[i] & segment_witnesses[i+1]):
                        if (transitions[i], transitions[i+1]) not in valid_links:
                            error("UNBRIDGED_WITNESS_HANDOFF", r)
                if not valid_links:
                    error("UNSUPPORTED_BRIDGE", r)
                if bridge_evidence != used_bridge_evidence:
                    error("UNBOUND_BRIDGE_EVIDENCE", r)
            ancestry_assessments = founder.get("ancestry_assessment_refs", [])
            if not ancestry_assessments:
                error("UNSUPPORTED_ROUTE_ANCESTRY", r)
            admitted_ancestry = False
            for ar in ancestry_assessments:
                a = index.get(ar, {})
                if canonical(a.get("scope")) != canonical(scope):
                    continue
                e = index.get(a.get("evidence_ref"), {})
                if (e.get("id") not in witness_evidence or
                    not _appropriate_biological_assessment(
                        index, a, founder.get("id"), scope, "ANCESTRY",
                        context_ref=r.get("context_ref"))):
                    error("INVALID_ROUTE_ANCESTRY_ASSESSMENT", r)
                else:
                    # Ancestry must attach to the *first admitted route segment*
                    # irrespective of whether later transitions require bridges.
                    if not segment_witnesses or not (
                        _witness_keys(e) & segment_witnesses[0]):
                        error("ROUTE_ANCESTRY_WITNESS_MISMATCH", r)
                    else:
                        admitted_ancestry = True
            if not admitted_ancestry:
                error("UNSUPPORTED_ROUTE_ANCESTRY", r)
        if typ == "Verdict":
            authority = index.get(r.get("authority_ref"), {})
            if authority.get("status") != "ACTIVE_RULE": error("INACTIVE_VERDICT_AUTHORITY", r)
            if r.get("axis") not in authority.get("axes", []): error("AUTHORITY_AXIS_MISMATCH", r)
            if canonical(r.get("scope")) != canonical(authority.get("scope")):
                error("AUTHORITY_SCOPE_MISMATCH", r)
            if authority.get("subject_refs") and r.get("subject_ref") not in authority["subject_refs"]:
                error("AUTHORITY_SUBJECT_MISMATCH", r)
            if r.get("decision") in SCIENTIFIC_POSITIVE and not (r.get("assessment_refs") or r.get("result_refs")):
                error("UNSUPPORTED_PROMOTION", r)
            if r.get("decision") == "SUPPORTED_SCOPED":
                allowed_axes = {
                    "BIOLOGICAL_SUPPORT": None,
                    "ANCESTRY": "ANCESTRY",
                    "PERSISTENCE": "PERSISTENCE",
                    "OBSERVABILITY": "OBSERVATION",
                    "ROUTE_CLOSURE": "ROUTE",
                }
                subject = index.get(r.get("subject_ref"), {})
                if r.get("axis") not in allowed_axes:
                    error("UNSUPPORTED_VERDICT_AXIS", r)
                elif r.get("axis") == "ROUTE_CLOSURE" and (
                        subject.get("type") != "Route"
                        or subject.get("status") != "CLOSED"
                        or effective_route_state(records, subject)["effective"]
                           not in {"ADMITTED_CLOSED", "CONTESTED"}):
                    error("UNQUALIFIED_ROUTE_CLOSURE_VERDICT", r)
                elif r.get("axis") == "BIOLOGICAL_SUPPORT" and (
                        subject.get("type") != "Claim"
                        or subject.get("claim_kind") not in
                        (set(EVIDENCE_OBLIGATION_POLICY) | {"ORIGIN"})):
                    error("UNQUALIFIED_BIOLOGICAL_VERDICT_SUBJECT", r)
                elif r.get("axis") != "BIOLOGICAL_SUPPORT" and (
                        (subject.get("type") == "Route" and r.get("axis") != "ROUTE_CLOSURE")
                        or subject.get("type") not in {"Claim", "Route"}):
                    error("UNQUALIFIED_VERDICT_SUBJECT", r)
                required_kind = allowed_axes.get(r.get("axis"))
                if (required_kind == "ROUTE" and subject.get("type") == "Route"
                        and subject.get("claim_kind") == "HISTORICAL"):
                    required_kind = "HISTORICAL_ROUTE"
                if required_kind and subject.get("type") == "Claim" and subject.get("claim_kind") != required_kind:
                    error("VERDICT_CLAIM_KIND_MISMATCH", r)
                if subject.get("type") == "Claim" and subject.get("claim_kind") == "CERTIFICATE":
                    error("CERTIFICATE_NOT_BIOLOGICAL_SUPPORT", r)
                assessments = [index.get(x, {}) for x in r.get("assessment_refs", [])]
                admissible = []
                subject = index.get(r.get("subject_ref"), {})
                kind = subject.get("claim_kind") if subject.get("type") == "Claim" else None
                for a in assessments:
                    gated_kind = required_kind or kind
                    qualified = (
                        _admitted_origin_claim(records, index, subject)
                        and _appropriate_biological_assessment(
                            index,a,r.get("subject_ref"),r.get("scope"),"PERSISTENCE")
                        if gated_kind == "ORIGIN" else
                        _appropriate_biological_assessment(
                            index,a,r.get("subject_ref"),r.get("scope"),gated_kind)
                        if gated_kind in EVIDENCE_OBLIGATION_POLICY else False
                    )
                    if qualified:
                        admissible.append(a)
                if not admissible: error("NONBIOLOGICAL_PROMOTION", r)
                # Species and cross-adapter promotion need their own reviewed scope.
                if r.get("scope", {}).get("species") == "human" and not any(
                    index.get(a.get("evidence_ref"), {}).get("evidence_class") in {
                        "PRIMARY_HUMAN_LONGITUDINAL", "PRIMARY_HUMAN_CROSS_SECTIONAL", "HUMAN_CAUSAL"}
                    for a in admissible):
                    error("NONHUMAN_TO_HUMAN_PROMOTION", r)
                if r.get("scope", {}).get("pan_cancer"):
                    transfer = index.get(r.get("transfer_decision_ref"), {})
                    authority_t = index.get(transfer.get("authority_ref"), {})
                    adapters = {ad.get("id") for ad in records if ad.get("type") == "Adapter"}
                    declared_adapters = _valid_ref_list(transfer.get("transfer_adapter_refs"))
                    allowed = (
                        transfer.get("type") == "Decision"
                        and transfer.get("decision_kind") == "TRANSFER"
                        and transfer.get("decision") == "ALLOW_TRANSFER"
                        and transfer.get("status") == "RECORDED"
                        and transfer.get("subject_ref") == r.get("subject_ref")
                        and canonical(transfer.get("scope")) == canonical(r.get("scope"))
                        and authority_t.get("status") == "ACTIVE_RULE"
                        and ("EVIDENCE_POLICY" in authority_t.get("axes", [])
                             or "BIOLOGICAL_SUPPORT" in authority_t.get("axes", []))
                        and canonical(authority_t.get("scope")) == canonical(r.get("scope"))
                        and (not authority_t.get("subject_refs")
                             or r.get("subject_ref") in authority_t.get("subject_refs", []))
                        and declared_adapters is not None and bool(adapters)
                        and declared_adapters == adapters
                    )
                    evidence_refs = _valid_ref_list(transfer.get("evidence_refs"))
                    if not allowed or not evidence_refs:
                        error("MISSING_CROSS_ADAPTER_DECISION", r)
                    else:
                        independent_sources = {}
                        for ad in sorted(adapters):
                            # A distinct scope needs its own primary evidence. A
                            # single study/system reused under six adapter labels
                            # does not establish pan-cancer transfer.
                            eligible = [
                                index.get(a.get("evidence_ref"), {}) for a in records
                                if a.get("type") == "EvidenceAssessment"
                                and a.get("target_ref") == r.get("subject_ref")
                                and index.get(a.get("evidence_ref"), {}).get("id") in evidence_refs
                                and _appropriate_biological_assessment(
                                    index, a, r.get("subject_ref"),
                            _adapter_scientific_scope(r.get("scope"), ad),
                            gated_kind)
                            ]
                            keys = {(e.get("study_id"), e.get("system_id")) for e in eligible}
                            independent_sources[ad] = keys
                            if not keys:
                                error("MISSING_TRANSFER_ADAPTER_SUPPORT", r)
                        def independent_assignment(remaining, used):
                            if not remaining:
                                return True
                            first = remaining[0]
                            return any(
                                key not in used
                                and independent_assignment(remaining[1:], used | {key})
                                for key in independent_sources[first])
                        if not independent_assignment(sorted(adapters), set()):
                            error("TRANSFER_INDEPENDENCE_NOT_ESTABLISHED", r)
            if (r.get("decision") == "MATHEMATICALLY_VERIFIED_SCOPED"
                    and root is not None and (root/"config/project.json").is_file()
                    and not any(trusted_proof_receipt(root,index,index.get(i,{}))
                                for i in r.get("result_refs", []))):
                error("UNTRUSTED_FORMAL_PROOF", r)
            if r.get("decision") == "MATHEMATICALLY_VERIFIED_SCOPED":
                if r.get("axis") != "MATHEMATICAL_VERIFICATION":
                    error("MATHEMATICAL_VERDICT_AXIS_MISMATCH", r)
                if not r.get("model_instance_ref") or not r.get("result_refs"):
                    error("UNSUPPORTED_MATHEMATICAL_VERDICT", r)
                qualifying = [index.get(x, {}) for x in r.get("result_refs", []) if isinstance(x, str)]
                admitting = [index.get(x, {}) for x in r.get("assessment_refs", []) if isinstance(x, str)]
                if not any(
                    result.get("model_instance_ref") == r.get("model_instance_ref")
                    and _verified_result(index, result, r.get("subject_ref"), r.get("scope"))
                    and any(
                        index.get(a.get("evidence_ref"), {}).get("result_ref") == result.get("id")
                        and _qualified_assessment(
                            index, a, r.get("subject_ref"), r.get("scope"),
                            allowed_classes={"FORMAL"}, allowed_ceilings={"MATHEMATICAL_EXACT"})
                        for a in admitting
                    ) for result in qualifying
                ):
                    error("UNVERIFIED_MATHEMATICAL_PROMOTION", r)
            if r.get("decision") in SCIENTIFIC_POSITIVE and r.get("scope", {}).get("domain") == "PROGRAMME_GOVERNANCE":
                error("GOVERNANCE_AS_SCIENTIFIC_SUPPORT", r)
        if typ == "Programme":
            if r.get("clinical_use"): error("CLINICAL_USE_OUT_OF_SCOPE", r)
            requirements = [x for x in records if x.get("type") == "Requirement"
                            and x.get("subject_ref") == r["id"]]
            for gap_ref in sorted(configured_critical_gap_refs):
                gap = index.get(gap_ref, {})
                if gap.get("type") != "ResearchGap":
                    error("MISSING_CONFIGURED_CRITICAL_GAP", r)
                    continue
                if gap.get("priority") != "CRITICAL":
                    error("CRITICAL_GAP_PRIORITY_DRIFT", gap)
                if not any(q.get("gap_ref") == gap_ref for q in requirements):
                    error("MISSING_CRITICAL_PROGRAMME_REQUIREMENT", gap)
            if r.get("kernel_frozen"):
                if not requirements: error("NO_FREEZE_REQUIREMENTS", r)
                for q in requirements:
                    gap = index.get(q.get("gap_ref"), {})
                    q_status = q.get("status")
                    gap_status = gap.get("status")
                    if q_status not in {"SATISFIED", "BOUNDED"}:
                        error("OPEN_FREEZE_REQUIREMENT", r)
                    if q_status == "BOUNDED" and not q.get("bound_scope"):
                        error("UNSCOPED_REQUIREMENT_BOUND", q)
                    q_decision = index.get(q.get("decision_ref"), {})
                    q_scope = (q.get("bound_scope") if q_status == "BOUNDED"
                               else q_decision.get("disposition_scope"))
                    allowed_effects = ({"SUPPORTS"} if q_status == "SATISFIED"
                                       else {"CONSTRAINS", "DOES_NOT_ESTABLISH"})
                    q_errors = _decision_admission_errors(
                        records, index, q_decision, q.get("id"), q_scope, allowed_effects,
                        required_evidence_refs=q.get("satisfaction_evidence_refs", []))
                    if q_errors:
                        error("INVALID_FREEZE_DECISION", q)
                        for issue in q_errors:
                            error(issue, q)
                    if q.get("gap_ref") in configured_critical_gap_refs:
                        if gap_status == "SUPERSEDED":
                            error("SUPERSEDED_CRITICAL_GAP_ON_FREEZE", q)
                        if gap_status not in {"RESOLVED", "BOUNDED"}:
                            error("OPEN_CRITICAL_GAP_ON_FREEZE", q)
                        if gap_status == "BOUNDED" and (
                            q_status != "BOUNDED" or
                            canonical(q.get("bound_scope")) != canonical(gap.get("bound_scope"))):
                            error("REQUIREMENT_GAP_BOUND_MISMATCH", q)
                        if gap_status == "RESOLVED" and q_status != "SATISFIED":
                            error("REQUIREMENT_GAP_DISPOSITION_MISMATCH", q)
                        if (q.get("obligation_domain") != gap.get("obligation_domain")
                            or q.get("obligation_claim_kind") != gap.get("obligation_claim_kind")
                            or canonical(q.get("obligation_scope")) != canonical(gap.get("obligation_scope"))):
                            error("CRITICAL_GAP_OBLIGATION_MISMATCH", q)
                        gap_decision = index.get(gap.get("decision_ref"), {})
                        gap_scope = (gap.get("bound_scope") if gap_status == "BOUNDED"
                                     else gap_decision.get("disposition_scope"))
                        gap_effects = ({"SUPPORTS"} if gap_status == "RESOLVED"
                                       else {"CONSTRAINS", "DOES_NOT_ESTABLISH"})
                        gap_errors = _decision_admission_errors(
                            records, index, gap_decision, gap.get("id"), gap_scope, gap_effects)
                        if gap_errors:
                            error("INVALID_CRITICAL_GAP_DECISION", gap)
                            for issue in gap_errors:
                                error(issue, gap)
    uses = [r for r in records if r.get("type") == "DataUse"]
    candidate_sets = [r for r in records if r.get("type") == "CandidateSet"]
    def related_candidates(left, right):
        lm, rm = left.get("model_instance_ref"), right.get("model_instance_ref")
        if lm == rm or (left.get("protocol_ref") and left.get("protocol_ref") == right.get("protocol_ref")):
            return True
        if (left.get("selection_family_id") and
            left.get("selection_family_id") == right.get("selection_family_id")):
            return True
        if (left.get("candidate_set_ref") and
            left.get("candidate_set_ref") == right.get("candidate_set_ref")):
            return True
        return any(lm in cs.get("member_refs", []) and rm in cs.get("member_refs", [])
                   for cs in candidate_sets)
    def documented_partition_pair(left, right, dataset_left, dataset_right):
        al = _valid_ref_list(left.get("independence_evidence_refs"))
        ar = _valid_ref_list(right.get("independence_evidence_refs"))
        if not al or not ar or not (al & ar):
            return False
        scoped = {
            "data_use_refs": sorted([left["id"], right["id"]]),
            "dataset_refs": sorted([left.get("dataset_ref"), right.get("dataset_ref")]),
            "dataset_versions": {
                left["id"]: dataset_left.get("version"),
                right["id"]: dataset_right.get("version")},
            "partition_ids": {
                left["id"]: left.get("partition_id"),
                right["id"]: right.get("partition_id")}
        }
        for er in al & ar:
            ev = index.get(er, {})
            if ev.get("design_class") != "DATA_AUDIT":
                continue
            if all(any(a.get("type") == "EvidenceAssessment"
                       and a.get("evidence_ref") == er
                       and _qualified_assessment(index, a, du["id"], scoped,
                            allowed_classes={"ANALYTIC"}, allowed_ceilings={"DATA_PARTITION_AUDIT"},
                            assessment_role="INDEPENDENCE")
                       for a in records) for du in (left, right)):
                return True
        return False
    for i, a in enumerate(uses):
        for b in uses[i+1:]:
            roles = {a.get("role"), b.get("role")}
            if "CONFIRM" not in roles or not roles.intersection({"TRAIN", "SELECT", "CALIBRATION"}):
                continue
            da, db = index.get(a.get("dataset_ref"), {}), index.get(b.get("dataset_ref"), {})
            same = a.get("dataset_ref") == b.get("dataset_ref")
            family = bool(da.get("family_id") and da.get("family_id") == db.get("family_id"))
            if not (same or family):
                continue
            au, bu = _valid_ref_list(a.get("unit_keys", [])), _valid_ref_list(b.get("unit_keys", []))
            if au is None or bu is None:
                error("MALFORMED_DATA_USE_UNITS", a)
                continue
            if (same and a.get("partition_id") == b.get("partition_id")) or (au & bu):
                # A rejected/proposed contaminated plan is historical research data,
                # not an admitted independent confirmation.
                if a.get("status") == b.get("status") == "ADMITTED":
                    error("DATA_USE_LEAKAGE", a)
                continue
            if related_candidates(a, b) and a.get("status") == b.get("status") == "ADMITTED":
                if not (
                    a.get("independence_status") == b.get("independence_status") == "DOCUMENTED_DISJOINT"
                    and documented_partition_pair(a, b, da, db)
                ):
                    error("UNKNOWN_PARTITION_INDEPENDENCE", a)
    for subject in (r for r in records
                    if r.get("type") in {"ModelInstance", "Programme"}):
        try:
            actions = ({"ADMIT_MODEL", "RETIRE_MODEL"}
                       if subject["type"] == "ModelInstance" else
                       {"FREEZE_KERNEL", "UNFREEZE_KERNEL"})
            _authorization_tail(records, subject["id"], actions)
        except IntegrityError as exc:
            error("AUTHORIZATION_HISTORY:" + str(exc), subject)
    try:
        state = resolve(records)
        if state["conflict_count"]: errors.append("UNRESOLVED_AUTHORITY_CONFLICT")
    except IntegrityError as exc: errors.append("RESOLVER:"+str(exc))
    return sorted(set(errors))

EPHEMERAL_PARTS = {".git", ".venv", "__pycache__", ".pytest_cache", ".mypy_cache"}
GENERATED_PREFIXES = ("generated/", "releases/")
GENERATED_ROOTS = {"manifest.json"}

def file_class(path: str) -> tuple[str, str]:
    if path.startswith("sources/"): return "FROZEN_SOURCE", "REFERENCE_ONLY"
    if path.startswith("generated/") or path in GENERATED_ROOTS: return "GENERATED_VIEW", "NON_AUTHORITATIVE"
    if path.startswith("releases/"): return "RELEASE_DESCRIPTOR", "PACKAGING_ONLY"
    if path.startswith("graph/") and path.endswith(".jsonl"): return "AUTHORED_GRAPH", "CURATED_RESEARCH"
    if path.startswith(".github/workflows/"): return "CI_WORKFLOW", "ENGINEERING"
    if path.startswith("tests/"): return "SYNTHETIC_TEST", "ENGINEERING"
    if path.startswith("modeling/"): return "MATHEMATICAL_REFERENCE", "SYNTHETIC_ONLY"
    if path.startswith(("oocgraph/", "tools/", "resolver/")): return "ENGINEERING", "NO_BIOLOGICAL_AUTHORITY"
    if path.startswith(("config/", "schema/")): return "CONTRACT", "PROCEDURAL"
    if path.endswith(".md"): return "DOCUMENTATION", "RESEARCH_OR_GOVERNANCE"
    if path in {".gitignore", ".gitattributes", "requirements.txt", "pyproject.toml", "CITATION.cff", ".github/CODEOWNERS", ".github/dependabot.yml"}: return "BUILD_METADATA", "ENGINEERING"
    if path.startswith(".github/ISSUE_TEMPLATE/"): return "BUILD_METADATA", "ENGINEERING"
    if path.startswith("assets/") and path.endswith((".png", ".jpg", ".svg")): return "ILLUSTRATION", "DOCUMENTATION"
    raise IntegrityError(f"Unclassified file: {path}")

def file_inventory(root: Path) -> list[str]:
    files = []
    for p in root.rglob("*"):
        rel = p.relative_to(root)
        if any(x in EPHEMERAL_PARTS for x in rel.parts): continue
        if p.is_symlink(): raise IntegrityError(f"Symlink not allowed in source inventory: {rel}")
        if p.is_file(): files.append(rel.as_posix())
    return sorted(files)

def subject_digest(root: Path, files: list[str]) -> str:
    entries = []
    for p in files:
        if p in GENERATED_ROOTS or p.startswith(GENERATED_PREFIXES): continue
        entries.append([p, sha256(safe_path(root, p).read_bytes())])
    return sha256(canonical(entries).encode())

def validate_repository(root: Path) -> list[str]:
    records = read_graph(root)
    errors = validate_records(records, root)
    project = loads((root / "config/project.json").read_text())
    for typ, minimum in project["required_baseline_counts"].items():
        if sum(r["type"] == typ for r in records) < minimum: errors.append("LOST_BASELINE_POPULATION:"+typ)
    programmes = [r for r in records if r['type'] == 'Programme']
    if len(programmes) != 1: errors.append('PROGRAMME_IDENTITY_COUNT')
    elif programmes[0]['kernel_frozen'] != project['kernel_frozen']:
        errors.append('KERNEL_STATE_DISAGREEMENT')
    if project.get('clinical_use_authorized'): errors.append('CLINICAL_CONFIG_OUT_OF_SCOPE')
    gaps = {r.get("legacy_id") for r in records if r["type"] == "ResearchGap"}
    if not {f"RG-{i:03}" for i in range(1, 92)}.issubset(gaps): errors.append("LOST_RESEARCH_GAP")
    programme_id = programmes[0]["id"] if len(programmes) == 1 else None
    req = {(r.get("gap_ref"), r.get("subject_ref")) for r in records if r["type"] == "Requirement"}
    for gid in project["critical_gap_ids"]:
        if ("ooc:gap:"+gid, programme_id) not in req: errors.append("LOST_CRITICAL_REQUIREMENT:"+gid)
    frozen_gap_register = loads((root / "sources/baseline/research_gaps_91.json").read_text())
    original_critical = {g["legacy_id"] for g in frozen_gap_register if g["priority"] == "CRITICAL"}
    if set(project["critical_gap_ids"]) != original_critical:
        errors.append("CRITICAL_GATE_CONFIG_DRIFT")
    for p in loads((root / "config/documentation_contract.json").read_text())["required_documents"]:
        if not safe_path(root, p).is_file(): errors.append("MISSING_DOCUMENT:"+p)
    for p, expected in loads((root / "config/source_locks.json").read_text())["sha256"].items():
        path = safe_path(root, p)
        if not path.is_file() or sha256(path.read_bytes()) != expected: errors.append("SOURCE_DRIFT:"+p)
    for p in file_inventory(root):
        try: file_class(p)
        except IntegrityError as exc: errors.append(str(exc))
    # Source transcriptions have their own fidelity limitations; lint working Markdown links.
    for p in file_inventory(root):
        if not p.endswith(".md") or p.startswith(("sources/", "generated/")): continue
        text = (root / p).read_text()
        for target in re.findall(r"\]\(([^)\s]+)\)", text):
            if target.startswith(("http:", "https:", "mailto:", "#")): continue
            target = target.split("#", 1)[0]
            path = ((root / p).parent / target).resolve()
            if not path.is_relative_to(root.resolve()):
                errors.append(f"BROKEN_DOC_LINK:{p}:{target}")
            elif not path.exists():
                from .views import PRODUCTS
                if path.relative_to(root.resolve()).as_posix() not in PRODUCTS:
                    errors.append(f"BROKEN_DOC_LINK:{p}:{target}")
    return sorted(set(errors))

IMMUTABLE_ROOT_TYPES = frozenset({
    "Result", "Execution", "Verdict", "Decision", "AuthorizationEvent", "EvidenceObject",
    "SourceVerification"
})
IMMUTABLE_REFERENCES = {
    "AuthorizationEvent": {"subject_ref", "authority_ref", "previous_event_ref",
                           "basis_refs", "evidence_refs", "source_locator_refs"},
    "Result": {"subject_ref", "test_ref", "execution_ref", "verification_artifact_ref",
               "model_instance_ref", "source_locator_refs"},
    "Execution": {"input_refs", "protocol_ref", "software_ref",
                  "model_instance_ref", "source_locator_refs"},
    "Verdict": {"subject_ref", "authority_ref", "assessment_refs", "result_refs",
                "model_instance_ref", "transfer_decision_ref", "source_locator_refs"},
    "Decision": {"subject_ref", "authority_ref", "evidence_refs", "source_locator_refs",
                 "transfer_adapter_refs"},
    "EvidenceObject": {"source_locator_refs", "source_ref", "context_ref",
                       "result_ref", "model_instance_ref"},
    "EvidenceAssessment": {"evidence_ref", "target_ref", "authority_ref", "source_locator_refs"},
    "SourceVerification": {"source_ref", "source_locator_refs"},
    "ResearchGap": {"source_locator_refs", "decision_ref", "obligation_claim_ref"},
    "Requirement": {"gap_ref", "subject_ref", "decision_ref", "obligation_claim_ref",
                    "source_locator_refs", "satisfaction_evidence_refs"},
    "Claim": {"assumption_refs", "required_gate_refs", "source_locator_refs"},
    "SourceLocator": {"source_locator_refs"},
    "SourceArtifact": {"source_locator_refs"},
    "Route": {"boundary_ref", "founder_ref", "context_ref", "adapter_ref", "transition_refs",
              "witness_bundle_ref", "source_locator_refs"},
    "Transition": {"source_state_ref", "target_state_ref", "context_ref",
                   "source_context_ref", "target_context_ref", "adapter_ref", "mechanism_refs",
                   "context_transition_assessment_ref", "evidence_assessment_refs"},
    "FounderEnsemble": {"context_ref", "member_refs", "ancestry_assessment_refs"},
    "Boundary": {"context_ref", "state_refs", "source_locator_refs"},
    "Protocol": {"null_refs", "target_refs", "source_locator_refs"},
    "ModelInstance": {"model_class_ref", "applicability_ref", "assumption_refs", "context_ref",
                      "equation_refs", "parameter_refs", "estimand_refs",
                      "protocol_refs", "state_variable_refs", "software_ref",
                      "observation_operator_ref", "intervention_operator_refs",
                      "source_locator_refs"},
    "MethodApplicability": {"assumption_refs", "domain_ref", "estimand_ref",
                             "model_class_ref", "source_locator_refs"},
    "Parameter": {"provenance_ref", "source_locator_refs"},
    "ParameterProvenance": {"source_locator_refs", "data_use_refs"},
    "Equation": {"domain_ref", "variable_refs", "assumption_refs", "source_locator_refs"},
    "NullModel": {"target_claim_ref", "model_class_ref", "source_locator_refs"},
    "DataUse": {"dataset_ref", "protocol_ref", "independence_evidence_refs",
                "candidate_set_ref", "source_locator_refs"},
    "WitnessBundle": {"evidence_refs", "bridge_evidence_refs", "context_ref"},
    "Test": {"gate_ref", "protocol_ref", "subject_ref", "execution_ref",
             "source_locator_refs"},
    "Gate": {"source_locator_refs"},
    "BiologicalState": {"context_ref", "history_ref", "variable_refs", "source_locator_refs"},
    "StateVariable": {"source_locator_refs"},
    "Context": {"source_locator_refs"},
    "ValidityDomain": {"context_ref", "source_locator_refs"},
    "Software": {"source_locator_refs"},
    "ObservationProcess": {"context_ref", "source_locator_refs"},
    "ObservationOperator": {"process_ref", "variable_refs", "source_locator_refs"},
    "InterventionOperator": {"context_ref", "property_ref", "source_locator_refs"},
    "Dataset": {"source_locator_refs"},
    "Assumption": {"evidence_refs", "source_locator_refs"},
    "ModelClass": {"source_locator_refs"},
    "Estimand": {"source_locator_refs"},
    "CandidateSet": {"target_estimand_ref", "member_refs", "source_locator_refs"},
    "ReductionMap": {"source_variables_refs", "target_variables_refs", "estimand_refs",
                     "evidence_refs", "source_locator_refs"},
    "Falsifier": {"target_ref", "protocol_ref", "source_locator_refs"},
    "LiteratureSource": {"verification_refs", "source_locator_refs"},
}


def _locked_scientific_roots(records):
    for r in records:
        typ, status = r.get("type"), r.get("status")
        if (typ in IMMUTABLE_ROOT_TYPES
            or (typ == "ModelInstance" and status in {"FROZEN", "ADMITTED", "RETIRED"})
            or (typ == "Protocol" and r.get("frozen") is True)
            or (typ == "EvidenceAssessment" and status == "ADJUDICATED")
            or (typ == "DataUse" and status == "ADMITTED")
            or (typ == "Claim" and status == "FROZEN")
            or (typ == "Route" and status == "CLOSED")
            or (typ == "Transition" and status == "SUPPORTED_SCOPED")
            or (typ == "ResearchGap" and status in {"RESOLVED", "BOUNDED"})
            or (typ == "Requirement" and status in {"SATISFIED", "BOUNDED"})):
            yield r["id"]


def scientific_dependency_closure(records):
    """Content-addressed scientific meaning; no reverse associations or prose mentions.

    Cycles in biological mechanism records cannot cause infinite recursion here.
    Only *existing* historical refs are followed; new scientific references on a
    successor must use a new ID and their own admission receipt.
    """
    index = {r["id"]: r for r in records}
    pending = list(_locked_scientific_roots(records))
    locked = set()
    while pending:
        ident = pending.pop()
        if ident in locked:
            continue
        record = index.get(ident)
        if not record:
            continue
        locked.add(ident)
        forward = set(IMMUTABLE_REFERENCES.get(record.get("type"), {"source_locator_refs"}))
        # Newly declared semantic references are locked by default; explicit
        # reverse indexes do not pull other models or unrelated draft subjects.
        for field in record:
            if field.endswith(("_ref", "_refs")) and field != "revision_of_ref":
                if (record.get("type"), field) not in {
                    ("Protocol", "data_use_refs"), ("Authority", "subject_refs"),
                    ("ParameterProvenance", "data_use_refs"),
                }:
                    forward.add(field)
        for field in forward:
            val = record.get(field)
            if isinstance(val, str):
                pending.append(val)
            elif isinstance(val, list):
                pending.extend(item for item in val if isinstance(item, str))
        if record.get("type") == "ModelInstance":
            # Only this model's directly owned uses: no reverse protocol clients.
            pending.extend(r["id"] for r in records
                           if r.get("type") == "DataUse"
                           and r.get("model_instance_ref") == ident)
        if record.get("type") == "WitnessBundle":
            for link in record.get("bridge_links", []):
                if isinstance(link, dict):
                    pending.extend(str(link[k]) for k in (
                        "from_transition_ref", "to_transition_ref", "assessment_ref",
                        "evidence_ref") if isinstance(link.get(k), str))
        # A source locator's path points to a SHA-locked imported source or to
        # a revisioned authored artifact, not another mutable graph identity.
    return locked


def history_violations(before: list[dict], after: list[dict]) -> list[str]:
    """Protect exact admitted historical meanings, not unrelated mutable drafts."""
    old = {r["id"]: r for r in before}
    new = {r["id"]: r for r in after}
    failures = []
    for ident in sorted(scientific_dependency_closure(before)):
        if ident not in new:
            failures.append("DELETED_ADMITTED_DEPENDENCY:" + ident)
        elif canonical(old[ident]) != canonical(new[ident]):
            failures.append("MUTATED_ADMITTED_DEPENDENCY:" + ident)
    return failures


MODEL_IDENTITY_REFERENCE_EXCLUSIONS = {
    "DataUse": {"model_instance_ref"},  # owned by the model itself
    "Protocol": {"data_use_refs", "target_refs"},  # reverse memberships
}


MODEL_IDENTITY_FORWARD_REFS = {
    "ModelInstance": {"applicability_ref", "assumption_refs", "context_ref",
        "equation_refs", "estimand_refs", "protocol_refs", "intervention_operator_refs",
        "model_class_ref", "observation_operator_ref", "parameter_refs",
        "software_ref", "state_variable_refs", "source_locator_refs"},
    "MethodApplicability": {"assumption_refs", "domain_ref", "estimand_ref",
        "model_class_ref", "source_locator_refs"},
    "Parameter": {"provenance_ref", "source_locator_refs"},
    "ParameterProvenance": {"source_locator_refs", "data_use_refs"},
    "Equation": {"assumption_refs", "domain_ref", "variable_refs", "source_locator_refs"},
    "ObservationOperator": {"process_ref", "variable_refs", "source_locator_refs"},
    "InterventionOperator": {"context_ref", "property_ref", "source_locator_refs"},
    "DataUse": {"dataset_ref", "protocol_ref", "independence_evidence_refs",
        "candidate_set_ref", "source_locator_refs"},
    "Protocol": {"null_refs", "source_locator_refs"},
    "Dataset": {"source_locator_refs"},
    "ModelClass": {"source_locator_refs"},
    "Assumption": {"evidence_refs", "source_locator_refs"},
    "Software": {"source_locator_refs"},
    "SourceArtifact": {"source_locator_refs"},
    "NullModel": {"target_claim_ref", "model_class_ref", "source_locator_refs"},
    "Claim": {"assumption_refs", "assessment_refs", "required_gate_refs",
              "origin_route_ref", "malignant_state_ref",
              "persistence_criterion_ref", "entry_assessment_refs",
              "establishment_assessment_refs", "source_locator_refs"},
}


def model_identity_digest(records: list[dict], model: dict) -> str:
    """Digest only claim-bearing dependencies owned by this model.

    The model binds its own DataUses (including their partitions). Shared Protocol
    configuration is included, but its reverse data_use_refs/target_refs do *not*
    import other models. Malformed references raise IntegrityError rather than
    exceptions escaping validation.
    """
    if model.get("type") != "ModelInstance":
        raise IntegrityError("Model identity requires ModelInstance")
    if model.get("identity_algorithm", MODEL_IDENTITY_ALGORITHM) != MODEL_IDENTITY_ALGORITHM:
        raise IntegrityError("Unrecognized model digest algorithm")
    index = {r["id"]: r for r in records}
    model_id = model["id"]
    bound_uses = sorted(r["id"] for r in records
                        if r.get("type") == "DataUse"
                        and r.get("model_instance_ref") == model_id)
    bound_set = set(bound_uses)
    pending = [model_id, *bound_uses]
    visited, content = set(), []
    ignored = {"frozen_digest", "status", "label", "notes", "doc_path"}
    while pending:
        ref_id = pending.pop()
        if not isinstance(ref_id, str):
            raise IntegrityError("Non-string model identity reference")
        if ref_id in visited:
            continue
        record = index.get(ref_id)
        if record is None:
            raise IntegrityError("Missing model identity reference " + ref_id)
        if record.get("type") == "ModelInstance" and ref_id != model_id:
            raise IntegrityError("Cross-model identity dependency " + ref_id)
        if record.get("type") == "DataUse" and record.get("model_instance_ref") != model_id:
            raise IntegrityError("Cross-model data use dependency " + ref_id)
        visited.add(ref_id)
        projection = {}
        follow = MODEL_IDENTITY_FORWARD_REFS.get(record.get("type"), {"source_locator_refs"})
        for key, value in record.items():
            if key.endswith("_refs") and (
                    not isinstance(value, list)
                    or any(not isinstance(item, str) for item in value)):
                raise IntegrityError("Malformed model identity reference list: " + key)
            if key.endswith("_ref") and not isinstance(value, str):
                raise IntegrityError("Malformed model identity reference: " + key)
            if key in ignored:
                continue
            # Protocol target memberships and clients are reverse associations.
            # They are not part of an individual model's frozen specification.
            if record.get("type") == "Protocol" and key in {"data_use_refs", "target_refs"}:
                continue
            if record.get("type") == "ParameterProvenance" and key == "data_use_refs":
                projection[key] = sorted(x for x in value if x in bound_set)
                pending.extend(projection[key])
                continue
            projection[key] = value
            if key in follow:
                if key.endswith("_refs"):
                    pending.extend(value)
                elif key.endswith("_ref"):
                    pending.append(value)
        content.append(projection)
    return sha256(canonical(sorted(content, key=lambda item: item["id"])).encode())
