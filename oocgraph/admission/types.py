"""Small immutable results shared by admission and current-state projections."""
from dataclasses import dataclass
from typing import Literal

@dataclass(frozen=True)
class RequiredGroupResult:
    name: str
    quantifier: str
    candidates: tuple[str, ...]
    accepted: tuple[str, ...]
    satisfied: bool

@dataclass(frozen=True)
class QualificationResult:
    subject_ref: str
    policy_id: str
    scope: tuple[tuple[str, str], ...]
    mode: Literal['HISTORICAL', 'CURRENT']
    decision: Literal['ADMITTED', 'NOT_ADMITTED', 'UNRESOLVED', 'CONTESTED']
    required_groups: tuple[RequiredGroupResult, ...] = ()
    accepted_evidence_refs: tuple[str, ...] = ()
    accepted_assessment_refs: tuple[str, ...] = ()
    formal_result_ref: str | None = None
    witness_path: tuple[tuple[str, str, str], ...] = ()
    material_contradiction_refs: tuple[str, ...] = ()
    pending_challenge_refs: tuple[str, ...] = ()
    basis_digest: str | None = None
    reason_codes: tuple[str, ...] = ()
    policy_version: str = 'OOC_ADMISSION_V2'
