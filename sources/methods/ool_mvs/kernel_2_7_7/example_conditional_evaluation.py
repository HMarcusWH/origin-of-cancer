"""Explicit synthetic example: never a laboratory result."""
from dataclasses import asdict
import json
from claim_registry_runtime_v2_7_7 import load_registry,eval_evidence_claim,issue_claim_certificate
from evidence_receipts_v2_7_7 import build_evidence_bundle,consumed_raw_ids
from kernel_test_fixtures_v2_7_7 import complete_world,evidence_env_from_world,R,B0
r=load_registry();env=evidence_env_from_world(r,complete_world(r))
result=eval_evidence_claim('LAB-CLOSURE-1',env,r=R,B0=B0)
bundle=build_evidence_bundle(result,result.physical_witness_ref,consumed_raw_ids(result))
certificate=issue_claim_certificate(result,bundle,env)
print(json.dumps({'synthetic':True,'conditional_result':result.result,'certificate':asdict(certificate)},indent=2))
assert certificate.certificate_status=='INCOMPLETE'
