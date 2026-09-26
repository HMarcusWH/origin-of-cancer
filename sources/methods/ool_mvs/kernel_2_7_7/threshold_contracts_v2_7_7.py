"""Typed, dimensional, preregistration-bound thresholds. No implicit unit conversion."""
from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime
from math import isfinite
from typing import Any, Dict, Optional
import re

@dataclass(frozen=True)
class ThresholdReceipt:
    contract_id: str
    value: float
    preregistered: bool = True
    resolution_relevance_justified: bool = True
    metric: str = 'dimensionless'
    units: str = '1'
    d_max: Optional[float] = None
    receipt_id: str = ''
    preregistration_digest: str = ''
    frozen_at: str = ''
    observation_start: str = ''
    applicability: str = ''
    justification: str = ''

def finite_number(x):
    try:return type(x) in (int,float) and isfinite(float(x))
    except (OverflowError,ValueError):return False
def timestamp(x):
    if type(x) is not str or not x:raise ValueError('timestamp_required')
    d=datetime.fromisoformat(x.replace('Z','+00:00'))
    if d.tzinfo is None or d.utcoffset() is None:raise ValueError('timezone_required')
    return d

def validate_threshold_receipt(contract_id: str, spec: Dict[str,Any], receipt: ThresholdReceipt) -> tuple[bool,str]:
    if not isinstance(receipt,ThresholdReceipt):return False,'typed_threshold_receipt_required'
    if receipt.contract_id!=contract_id:return False,'contract_id_mismatch'
    if not finite_number(receipt.value):return False,'non_finite_or_non_numeric_value'
    if type(receipt.preregistered) is not bool or type(receipt.resolution_relevance_justified) is not bool:return False,'threshold_flags_must_be_booleans'
    if not receipt.preregistered:return False,'not_preregistered'
    if not receipt.resolution_relevance_justified:return False,'resolution_or_relevance_not_justified'
    if not all(type(getattr(receipt,k)) is str and getattr(receipt,k).strip() for k in ('metric','units')):return False,'metric_and_units_required'
    if spec.get('metric') and receipt.metric!=spec['metric']:return False,'metric_mismatch'
    if spec.get('units') and receipt.units!=spec['units']:return False,'units_mismatch'
    if spec.get('requires_frozen_metric') and receipt.metric=='dimensionless':return False,'explicit_distance_metric_required'
    v=float(receipt.value);domain=spec.get('domain')
    if domain=='(0,1]':ok=0<v<=1
    elif domain=='(0,inf)':ok=v>0
    elif domain in ('[0,inf)','finite'):
        # Historical finite domain never authorizes a negative distance tolerance.
        ok=v>=0 if domain=='[0,inf)' or 'distance' in contract_id else True
    elif domain=='[0,d_max)':
        if not finite_number(receipt.d_max) or receipt.d_max<=0:return False,'invalid_or_missing_d_max'
        ok=0<=v<float(receipt.d_max)
    else:return False,'unsupported_contract_domain:'+str(domain)
    if not ok:return False,'outside_'+str(domain)
    return True,'ok'

def validate_freeze(receipt: ThresholdReceipt) -> tuple[bool,str]:
    if not isinstance(receipt,ThresholdReceipt):return False,'typed_threshold_receipt_required'
    if not all(type(getattr(receipt,k)) is str for k in ('preregistration_digest','applicability','justification','receipt_id')):return False,'typed_threshold_metadata_required'
    if not re.fullmatch(r'[0-9a-f]{64}',receipt.preregistration_digest):return False,'preregistration_digest_required'
    if not receipt.applicability.strip() or not receipt.justification.strip() or not receipt.receipt_id:return False,'threshold_applicability_justification_required'
    try:
        if timestamp(receipt.frozen_at)>=timestamp(receipt.observation_start):return False,'threshold_not_frozen_before_observation'
    except (ValueError,TypeError):return False,'invalid_threshold_timestamp'
    return True,'ok'

def validate_required_thresholds(registry: dict, required_contract_ids: list[str], receipts: Dict[str,ThresholdReceipt]) -> tuple[bool,list[str]]:
    errors=[];contracts=registry.get('threshold_contracts',{})
    for cid in required_contract_ids:
        if cid not in contracts:errors.append('unknown_threshold_contract:'+cid);continue
        rec=receipts.get(cid)
        if rec is None:errors.append('missing_threshold_receipt:'+cid);continue
        ok,reason=validate_threshold_receipt(cid,contracts[cid],rec)
        if ok:ok,reason=validate_freeze(rec)
        if not ok:errors.append('invalid_threshold_receipt:'+cid+':'+reason)
    return not errors,errors
