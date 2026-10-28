#!/usr/bin/env python3
"""Check immutable scientific memory against an exact prior Git revision."""
from pathlib import Path
import argparse
import subprocess
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from oocgraph.core import (loads, read_graph, history_violations,
                           scientific_dependency_closure, safe_path, IntegrityError)
root=Path(__file__).resolve().parents[1]
p=argparse.ArgumentParser(description=__doc__);p.add_argument('--base',required=True);a=p.parse_args()
def git(*args):
    return subprocess.check_output(['git','-C',str(root),*args],text=True)
base=git('rev-parse','--verify',a.base+'^{commit}').strip()
paths=git('ls-tree','-r','--name-only',base,'graph').splitlines()
before=[]
for path in paths:
    if path.endswith('.jsonl'):
        before.extend(loads(line) for line in git('show',base+':'+path).splitlines() if line.strip())
errors=history_violations(before,read_graph(root))
if errors: print('\n'.join(errors));raise SystemExit(1)
# Protect bytes underlying admitted SourceLocators / proof artifacts / software,
# not only the graph records carrying their semantic selectors and checksums.
locked = scientific_dependency_closure(before)
for rec in before:
    if rec.get('id') not in locked or rec.get('type') not in {
            'SourceLocator', 'SourceArtifact', 'Software'}:
        continue
    relpath = rec.get('path')
    if not relpath:
        continue
    try:
        current = safe_path(root, relpath)
        prior = subprocess.check_output(
            ['git', '-C', str(root), 'show', base+':'+relpath])
    except (subprocess.CalledProcessError, IntegrityError, OSError) as exc:
        print('LOST_ADMITTED_ARTIFACT:'+rec['id']+':'+str(exc))
        raise SystemExit(1)
    if not current.is_file() or current.read_bytes() != prior:
        print('MUTATED_ADMITTED_ARTIFACT:'+rec['id']+':'+relpath)
        raise SystemExit(1)
print('PASS: admitted semantic dependencies and artifact bytes preserved against '+base)
print('PASS: immutable evidence/result/decision history preserved against '+base)
# Frozen source bytes cannot be rewritten by changing both content and a local lock.
old_lock_path='config/source_locks.json'
tracked=git('ls-tree','-r','--name-only',base,'config').splitlines()
if old_lock_path in tracked:
    from oocgraph.core import sha256
    old_locks=loads(git('show',base+':'+old_lock_path))['sha256']
    for path,digest in old_locks.items():
        f=root/path
        if not f.is_file() or sha256(f.read_bytes())!=digest:
            print('MUTATED_FROZEN_SOURCE:'+path);raise SystemExit(1)
    print('PASS: prior frozen source bytes remain unchanged.')
# Lock the physical bytes behind previously admitted scientific source selectors.
# The original graph declarations alone cannot catch rewriting a referenced file.
from oocgraph.core import scientific_dependency_closure, safe_path
old_index={r['id']:r for r in before}
for ident in sorted(scientific_dependency_closure(before)):
    old=old_index[ident]
    if old.get('type') not in {'SourceLocator','SourceArtifact','Software'}:
        continue
    path=old.get('path')
    if not path:
        continue
    local=safe_path(root,path)
    try:
        prior=subprocess.check_output(['git','-C',str(root),'show',base+':'+path])
    except subprocess.CalledProcessError:
        print('MISSING_HISTORICAL_SEMANTIC_FILE:'+path)
        raise SystemExit(1)
    if not local.is_file() or local.read_bytes()!=prior:
        print('MUTATED_ADMITTED_SEMANTIC_FILE:'+path)
        raise SystemExit(1)
for path in ('BASELINE.md','tests/fixtures/bootstrap_graph.json'):
    if path in git('ls-tree','-r','--name-only',base,path).splitlines():
        if not (root/path).is_file() or (root/path).read_text()!=git('show',base+':'+path):
            print('MUTATED_BOOTSTRAP_BASELINE:'+path);raise SystemExit(1)
