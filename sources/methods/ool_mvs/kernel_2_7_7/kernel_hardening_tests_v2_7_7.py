from pathlib import Path
import json, re, hashlib
HERE=Path(__file__).resolve().parent
DOC=(HERE/'OoL_MVS_Kernel_v2.7.7_Mathematically_Unified.md').read_text(encoding='utf-8')
LED=(HERE/'OoL_MVS_v2.7.7_Mathematical_Source_Ledger.md').read_text(encoding='utf-8')
REG=json.loads((HERE/'claim_registry_v2_7_7.json').read_text(encoding='utf-8'))
r={}
def check(name,ok,detail=''): r[name]={'pass':bool(ok),'detail':detail}
check('001_registry_version',REG.get('registry_version')=='2.7.7',REG.get('registry_version'))
check('002_state_tuple_explicit_generated_objects','P = (mu_poly, mu_gen, J_gen, Mu_gen' in DOC)
check('003_mu_gen_normalized','`mu_gen`: **normalized source-conditioned distribution**' in DOC)
check('004_J_gen_absolute','`J_gen`: **unnormalized absolute production-flux measure**' in DOC)
check('005_Mu_gen_joint_local','`Mu_gen`: **joint local generated-configuration measure**' in DOC)
check('006_generated_objects_not_life_claims','not independent life claims' in DOC)
check('007_discovery_freeze_confirmatory_section','Discovery -> route freeze -> confirmatory execution' in DOC)
check('008_route_change_requires_new_digest','creates a **new route version/digest**' in DOC)
check('009_actual_output_not_synthetic_replacement','actual upstream-output claim-bearing lane' in DOC)
check('010_protocol_cannot_redefine_kernel','may not weaken or redefine the canonical kernel predicates' in DOC)
check('011_three_trace_sources',all(x in DOC and x in LED for x in ['MIZ23','SER24','MIS26']))
check('012_old_authority_sentence_removed','next laboratory-protocol revision' not in DOC and 'current Integrated Theory and Sequential Laboratory Protocol remains authoritative' not in DOC)
out={'version':'2.7.7','passed':sum(v['pass'] for v in r.values()),'total':len(r),'all_pass':all(v['pass'] for v in r.values()),'results':r}
(HERE/'kernel_hardening_results_v2_7_7.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
