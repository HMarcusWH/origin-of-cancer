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
}
REF_LIST_TYPES = {
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
}
COMMON_SUBJECT_TYPES = {
    "Programme", "Theory", "Adapter", "Claim", "Boundary", "BiologicalState", "FounderEnsemble",
    "Mechanism", "Transition", "Route", "Estimand", "ModelClass", "ModelInstance",
    "PersistenceCriterion", "ResearchGap", "Workstream", "PathologyEntity", "NullModel",
    "Falsifier", "EvidenceObject", "EvidenceAssessment", "Requirement", "Protocol", "Test",
    "Result", "MethodApplicability", "Intervention", "Observation",
}
OWNER_REF_TYPES = {
    ("Intervention", "operator_ref"): {"InterventionOperator"},
    ("Observation", "operator_ref"): {"ObservationOperator"},
    ("Decision", "subject_ref"): COMMON_SUBJECT_TYPES,
    ("Requirement", "subject_ref"): COMMON_SUBJECT_TYPES,
    ("Test", "subject_ref"): COMMON_SUBJECT_TYPES,
    ("Verdict", "subject_ref"): COMMON_SUBJECT_TYPES,
    ("EvidenceAssessment", "target_ref"): COMMON_SUBJECT_TYPES,
    ("Falsifier", "target_ref"): COMMON_SUBJECT_TYPES,
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
NON_ADMISSIBLE_PROVENANCE = frozenset({
    "TEXTUAL_HINT", "SYNTHETIC", "ENGINEERING"
})


def _qualified_assessment(index, assessment, target_ref, scope, *,
                          effect="SUPPORTS", context_ref=None,
                          allowed_classes=BIOLOGICAL_EVIDENCE_CLASSES):
    """The same fail-closed evidence contract governs biological verdicts and routes.

    Synthetic test *fixtures* may model these fields; actual synthetic/engineering
    evidence is ineligible to establish cancer biology.
    """
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
        and evidence.get("type") == "EvidenceObject"
        and evidence.get("status") == "RECORDED"
        and evidence.get("provenance_class") not in NON_ADMISSIBLE_PROVENANCE
        and evidence.get("evidence_class") in allowed_classes
        and bool(evidence.get("source_locator_refs"))
        and (context_ref is None or evidence.get("context_ref") == context_ref)
    )


def _decision_admission_errors(records, index, decision, subject_ref, scope, effects,
                               *, required_evidence_refs=None):
    """Admit a scientific disposition only with active, scoped authority and
    per-evidence adjudication for the *specific subject* and scientific scope.

    Decision.scope is governance jurisdiction; Decision.disposition_scope
    is the scientific extent of resolution/bounding. They must never be conflated.
    """
    errors = []
    authority = index.get(decision.get("authority_ref"), {})
    if not (
        decision.get("type") == "Decision"
        and decision.get("status") == "RECORDED"
        and decision.get("provenance_class") not in NON_ADMISSIBLE_PROVENANCE
        and decision.get("subject_ref") == subject_ref
        and isinstance(scope, dict) and bool(scope)
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
    evidence_refs = decision.get("evidence_refs", [])
    if not isinstance(evidence_refs, list) or not evidence_refs:
        errors.append("MISSING_DISPOSITION_EVIDENCE")
        evidence_refs = []
    if required_evidence_refs is not None and (
            set(evidence_refs) != set(required_evidence_refs)):
        errors.append("DISPOSITION_EVIDENCE_MISMATCH")
    for evidence_ref in evidence_refs:
        assessments = (
            a for a in records
            if a.get("type") == "EvidenceAssessment"
            and a.get("evidence_ref") == evidence_ref
        )
        if not any(
            _qualified_assessment(index, a, subject_ref, scope,
                                  effect=effect, allowed_classes=SCIENTIFIC_DISPOSITION_CLASSES)
            for a in assessments for effect in effects
        ):
            errors.append("UNADJUDICATED_DISPOSITION_EVIDENCE")
    return errors


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
        for schema_type, definition in schema["$defs"].items():
            for key in definition.get("properties", {}):
                if key.endswith("_ref") or key == "same_identifier_as":
                    if _allowed_ref_types(schema_type, key, False) is None:
                        errors.append(f"UNDECLARED_REF_TYPE:{schema_type}:{key}")
                elif key.endswith("_refs"):
                    if _allowed_ref_types(schema_type, key, True) is None:
                        errors.append(f"UNDECLARED_REF_TYPE:{schema_type}:{key}")
        for r in records:
            validator = validators.get(r.get("type"))
            if validator is None: errors.append(f"UNKNOWN_TYPE:{r.get('id')}"); continue
            for e in validator.iter_errors(r): errors.append(f"SCHEMA:{r.get('id')}:{list(e.path)}:{e.message}")
    else: vocab = None
    def error(code, record): errors.append(f"{code}:{record.get('id')}")
    def check_ref(record, key, value, allowed=None):
        if not isinstance(value, str) or value not in index: error("MISSING_REF:"+key, record)
        elif allowed and index[value]["type"] not in allowed: error("WRONG_REF_TYPE:"+key, record)
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
        if typ == "LiteratureSource":
            if r.get("bibliographic_verification") == "VERIFIED" and not r.get("verification_refs"):
                error("UNBACKED_SOURCE_VERIFICATION", r)
        if typ in {"ResearchGap", "Requirement"} and r.get("status") in {"RESOLVED", "SATISFIED", "BOUNDED", "SUPERSEDED"}:
            decision = index.get(r.get("decision_ref"), {})
            if decision.get("type") != "Decision" or decision.get("subject_ref") != r.get("id"):
                error("UNADJUDICATED_CLOSURE", r)
            if r.get("status") == "BOUNDED" and not r.get("bound_scope"):
                error("UNSCOPED_REQUIREMENT_BOUND", r)
        if typ in {"Theory", "Adapter"} and (r.get("card_complete") or r.get("dossier_complete")):
            decision = index.get(r.get("completion_decision_ref"), {})
            if decision.get("type") != "Decision" or decision.get("subject_ref") != r.get("id"):
                error("UNADJUDICATED_DOCUMENT_COMPLETION", r)
        if typ == "EvidenceObject":
            if not r.get("source_locator_refs"): error("UNLOCATED_EVIDENCE", r)
            for lr in r.get("source_locator_refs", []):
                selector = index.get(lr, {}).get("selector", {})
                if "sheet" in selector and selector["sheet"] in {"Anchor Sources", "Theory Queue"}:
                    error("BIBLIOGRAPHY_AS_FINDING", r)
        if typ == "MethodApplicability" and r.get("assessment") == "APPLICABLE":
            if not r.get("assumption_refs"): error("MISSING_APPLICABILITY_ASSUMPTIONS", r)
            for ar in r.get("assumption_refs", []):
                assumption = index.get(ar, {})
                if assumption.get("required", True) and assumption.get("assessment") != "PASS":
                    error("FAILED_OR_UNKNOWN_REQUIRED_ASSUMPTION", r)
        if typ == "ModelInstance" and r.get("status") in {"ADMITTED", "FROZEN"}:
            app = index.get(r.get("applicability_ref"), {})
            if app.get("assessment") != "APPLICABLE": error("UNLICENSED_MODEL", r)
            if not r.get("frozen_digest") or not re.fullmatch("[0-9a-f]{64}", r["frozen_digest"]):
                error("MISSING_MODEL_IDENTITY", r)
            else:
                try:
                    if r['frozen_digest'] != model_identity_digest(records,r): error("MODEL_IDENTITY_MISMATCH",r)
                except IntegrityError: error("INCOMPLETE_MODEL_IDENTITY",r)
            if app.get("model_class_ref") != r.get("model_class_ref"): error("APPLICABILITY_MODEL_MISMATCH",r)
            if app.get("scope") != r.get("scope"): error("APPLICABILITY_SCOPE_MISMATCH",r)
            if set(app.get("assumption_refs", [])) != set(r.get("assumption_refs", [])):
                error("APPLICABILITY_ASSUMPTION_MISMATCH", r)
            for ar in r.get("assumption_refs", []):
                assumption = index.get(ar, {})
                if assumption.get("required", True) and assumption.get("assessment") != "PASS":
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
            if founder.get("context_ref") != r.get("context_ref"):
                error("ROUTE_FOUNDER_CONTEXT_MISMATCH", r)
            if transitions:
                first_state = index.get(transitions[0], {}).get("source_state_ref")
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
            segment_witnesses = []
            for tr in transitions:
                t = index.get(tr, {})
                if t.get("context_ref") != r.get("context_ref") or t.get("adapter_ref") != r.get("adapter_ref"):
                    error("ROUTE_CONTEXT_MISMATCH", r)
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
                    if e.get("context_ref") != r.get("context_ref"):
                        error("ROUTE_EVIDENCE_CONTEXT_MISMATCH", r); valid = False
                    if e.get("id") not in witness_evidence:
                        error("ROUTE_EVIDENCE_OUTSIDE_WITNESS", r); valid = False
                    if canonical(a.get("scope")) != canonical(scope):
                        error("ROUTE_ASSESSMENT_SCOPE_MISMATCH", r); valid = False
                    if not _qualified_assessment(index, a, tr, scope, context_ref=r.get("context_ref")):
                        error("NONBIOLOGICAL_ROUTE_SUPPORT", r); valid = False
                    if valid:
                        segment_supported = True
                        witnesses.update(e.get("witness_ids", []))
                if not segment_supported:
                    error("UNSUPPORTED_ROUTE_SEGMENT", r)
                segment_witnesses.append(witnesses)
            if mode == "SAME_SYSTEM":
                common = set.intersection(*segment_witnesses) if segment_witnesses else set()
                declared = set(wb.get("common_witness_ids", []))
                if not common or not declared or not declared.issubset(common):
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
                    if not (
                        e_ref in bridge_evidence
                        and link.get("from_witness_id") in segment_witnesses[i]
                        and link.get("to_witness_id") in segment_witnesses[i+1]
                        and {link.get("from_witness_id"), link.get("to_witness_id")}
                            .issubset(set(e.get("witness_ids", [])))
                        and a.get("evidence_ref") == e_ref
                        and _qualified_assessment(index, a, r["id"], scope,
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
            for ar in ancestry_assessments:
                a = index.get(ar, {})
                e = index.get(a.get("evidence_ref"), {})
                if (e.get("id") not in witness_evidence or
                    not _qualified_assessment(index, a, founder.get("id"), scope,
                                              context_ref=r.get("context_ref"))):
                    error("INVALID_ROUTE_ANCESTRY_ASSESSMENT", r)
                elif mode == "SAME_SYSTEM":
                    if not set(e.get("witness_ids", [])) & set(wb.get("common_witness_ids", [])):
                        error("ROUTE_ANCESTRY_WITNESS_MISMATCH", r)
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
            if r.get("axis") == "BIOLOGICAL_SUPPORT" and r.get("decision") == "SUPPORTED_SCOPED":
                assessments = [index.get(x, {}) for x in r.get("assessment_refs", [])]
                admissible = []
                for a in assessments:
                    if _qualified_assessment(index, a, r.get("subject_ref"), r.get("scope")):
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
                    if (transfer.get("type") != "Decision" or transfer.get("subject_ref") != r.get("subject_ref")
                        or transfer.get("scope") != r.get("scope") or not transfer.get("evidence_refs")):
                        error("MISSING_CROSS_ADAPTER_DECISION", r)
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
    for i, a in enumerate(uses):
        for b in uses[i+1:]:
            if a.get("model_instance_ref") != b.get("model_instance_ref"): continue
            roles = {a.get("role"), b.get("role")}
            if "CONFIRM" not in roles or not roles.intersection({"TRAIN", "SELECT", "CALIBRATION"}): continue
            da, db = index.get(a.get("dataset_ref"), {}), index.get(b.get("dataset_ref"), {})
            same = a.get("dataset_ref") == b.get("dataset_ref")
            family = da.get("family_id") and da.get("family_id") == db.get("family_id")
            overlap = bool(set(a.get("unit_keys", [])) & set(b.get("unit_keys", [])))
            if (same and a.get("partition_id") == b.get("partition_id")) or ((same or family) and overlap):
                error("DATA_USE_LEAKAGE", a)
            elif (same or family) and b.get("status") == "ADMITTED" and a.get("status") == "ADMITTED":
                if not (a.get("independence_status") == b.get("independence_status") == "DOCUMENTED_DISJOINT"
                        and a.get("independence_evidence_refs") and b.get("independence_evidence_refs")):
                    error("UNKNOWN_PARTITION_INDEPENDENCE", a)
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

def history_violations(before: list[dict], after: list[dict]) -> list[str]:
    """Immutable evidence/decisions retain memory; draft claims may still evolve."""
    new = {r['id']: r for r in after}
    failures = []
    immutable = {'Result', 'Execution', 'Verdict', 'Decision', 'EvidenceObject', 'SourceVerification'}
    for old in before:
        locked = (old.get('type') in immutable
                  or (old.get('type') == 'ModelInstance' and old.get('status') in {'FROZEN','ADMITTED','RETIRED'})
                  or (old.get('type') == 'Protocol' and old.get('frozen') is True)
                  or (old.get('type') == 'EvidenceAssessment' and old.get('status') == 'ADJUDICATED')
                  or (old.get('type') == 'DataUse' and old.get('status') == 'ADMITTED'))
        if not locked: continue
        if old['id'] not in new:
            failures.append('DELETED_IMMUTABLE:'+old['id'])
        elif canonical(old) != canonical(new[old['id']]):
            failures.append('MUTATED_IMMUTABLE:'+old['id'])
    return failures

MODEL_IDENTITY_FORWARD_REFS = {
    "ModelInstance": {"applicability_ref", "assumption_refs", "context_ref",
        "equation_refs", "estimand_refs", "intervention_operator_refs",
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
        "source_locator_refs"},
    "Protocol": {"null_refs", "source_locator_refs"},
    "Dataset": {"source_locator_refs"},
    "ModelClass": {"source_locator_refs"},
    "Assumption": {"source_locator_refs"},
    "Software": {"source_locator_refs"},
    "SourceArtifact": {"source_locator_refs"},
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
