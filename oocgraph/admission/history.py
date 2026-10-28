"""Immutable admitted-basis snapshots and replay contracts.

A declaration within the same writable graph is not itself independent
authorization.  A production issuer must publish the hash under protected
external governance before any v2 positive is trusted.
"""
import hashlib, json

POLICY = 'OOC_ADMISSION_BASIS_V2'


def canonical_bytes(value):
    return json.dumps(value, sort_keys=True, separators=(',', ':'), ensure_ascii=False, allow_nan=False).encode()


def issued_record_digest(record):
    """Commit to every substantive issued field, excluding only the recursive envelope."""
    if not isinstance(record, dict):
        raise TypeError("Issued record must be a mapping")
    return hashlib.sha256(canonical_bytes({
        key: value for key, value in record.items() if key != 'admission_basis'
    })).hexdigest()


def obligation_inventory(records, programme_ref):
    return tuple(sorted(r['id'] for r in records if r.get('type')=='Requirement'
                        and r.get('subject_ref')==programme_ref))


def snapshot(records, refs, *, policy_version=POLICY,
             subject_ref=None, asserted_scope=None, obligation_inventory_refs=(),
             critical_gap_refs=(), input_graph_tree_sha=None, issuer_epoch=None,
             issued_record=None):
    index = {r['id']:r for r in records}
    entries = [index[ref] for ref in sorted(set(refs)) if ref in index]
    if len(entries) != len(set(refs)):
        raise ValueError('Missing basis object')
    manifest = {
        'policy_version':policy_version, 'record_ids':sorted(set(refs)), 'records':entries,
        'subject_ref':subject_ref, 'asserted_scope':asserted_scope,
        'obligation_inventory_refs':sorted(set(obligation_inventory_refs)),
        'critical_gap_refs':sorted(set(critical_gap_refs)),
        'input_graph_tree_sha':input_graph_tree_sha,
        'issuer_epoch':issuer_epoch,
    }
    if issued_record is not None:
        if not isinstance(issued_record, dict) or subject_ref != issued_record.get('id'):
            raise ValueError("Issued record identity does not match manifest subject")
        manifest['issued_record_sha256'] = issued_record_digest(issued_record)
    return {'basis':manifest,'digest':hashlib.sha256(canonical_bytes(manifest)).hexdigest()}


def historical_obligations(event, *, require_authenticated=False, verifier=None):
    """Verify an embedded original basis, never replay against new Requirements."""
    stamped = event.get('admission_basis')
    if not isinstance(stamped,dict):
        return None
    basis = stamped.get('basis')
    digest = stamped.get('digest')
    if not isinstance(basis,dict) or basis.get('policy_version')!=POLICY:
        return None
    if hashlib.sha256(canonical_bytes(basis)).hexdigest()!=digest:
        return None
    ids=basis.get('record_ids',[])
    rows=basis.get('records',[])
    if (not isinstance(ids,list) or not isinstance(rows,list)
            or sorted(ids)!=sorted({x.get('id') for x in rows if isinstance(x,dict)})):
        return None
    if not (isinstance(basis.get('input_graph_tree_sha'),str)
            and len(basis['input_graph_tree_sha']) == 40
            and isinstance(basis.get('issuer_epoch'),str)
            and basis['issuer_epoch']):
        return None
    if require_authenticated and basis.get('issued_record_sha256') != issued_record_digest(event):
        return None
    if require_authenticated and (verifier is None or not verifier(event,stamped)):
        return None
    return {r['id']:r for r in rows}
