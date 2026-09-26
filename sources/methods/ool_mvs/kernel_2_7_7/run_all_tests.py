"""Run every suite; reject stale output and failed assertions, not only exit codes."""
from __future__ import annotations
import hashlib,json,os,platform,subprocess,sys,time
from pathlib import Path
from importlib.metadata import version
ROOT=Path(__file__).resolve().parent
SUITES=[
('formal_claim_algebra_tests_v2_7_7.py','formal_claim_algebra_results_v2_7_7.json'),
('evidence_semantics_tests_v2_7_7.py','evidence_semantics_results_v2_7_7.json'),
('kernel_stress_tests_v2_7_7.py','kernel_stress_test_results_v2_7_7.json'),
('kernel_numerical_math_tests_v2_7_7.py','kernel_numerical_math_results_v2_7_7.json'),
('kernel_end_to_end_tests_v2_7_7.py','kernel_end_to_end_results_v2_7_7.json'),
('kernel_hardening_tests_v2_7_7.py','kernel_hardening_results_v2_7_7.json'),
('release_regression_tests_v2_7_7.py','release_regression_results_v2_7_7.json')]

def main():
    rows=[];(ROOT/'test_logs').mkdir(exist_ok=True)
    for script,out in SUITES:
        dest=ROOT/out;dest.unlink(missing_ok=True);start=time.monotonic()
        try:
            run=subprocess.run([sys.executable,script],cwd=ROOT,text=True,capture_output=True,timeout=240,env={**os.environ,'PYTHONDONTWRITEBYTECODE':'1'})
            (ROOT/'test_logs'/Path(script).with_suffix('.log').name).write_text(run.stdout+'\n'+run.stderr)
            data=json.loads(dest.read_text()) if dest.exists() else {};count=data.get('test_count',data.get('total',0));passed=data.get('passed')
            if passed is None:
                cases=data.get('tests',{})
                if cases:passed=sum(bool(x.get('pass',x.get('assertion',False))) for x in cases.values())
                elif data.get('overall_pass') is True:passed=count
                else:passed=0
            ok=run.returncode==0 and bool(data.get('all_pass',data.get('overall_pass',False))) and count>0 and passed==count
            row={'suite':script,'returncode':run.returncode,'count':count,'passed':passed,'pass':ok,'seconds':round(time.monotonic()-start,3),'result_file':out}
        except (OSError,ValueError,subprocess.TimeoutExpired) as e:row={'suite':script,'pass':False,'count':0,'passed':0,'error':str(e)}
        rows.append(row);print(json.dumps(row),flush=True)
    report={'version':'2.7.7','python':sys.version,'platform':platform.platform(),'dependencies':{p:version(p) for p in ['numpy','scipy','cryptography','mpmath']},'suites':rows,'test_count':sum(x['count'] for x in rows),'passed':sum(x['passed'] for x in rows),'all_pass':all(x['pass'] for x in rows),'source_sha256':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(ROOT.glob('*.py'))},'scope':'Software, finite fixtures, source-scope assertions and model arithmetic. NOT completed experiments.'}
    (ROOT/'TEST_REPORT.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps({k:report[k] for k in ['test_count','passed','all_pass']}));return 0 if report['all_pass'] else 1
if __name__=='__main__':raise SystemExit(main())
