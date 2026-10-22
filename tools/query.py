#!/usr/bin/env python3
"""Read-only graph queries. Reachability is not causal route closure."""
from pathlib import Path
import argparse
import json
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from oocgraph.core import read_graph

def expand_neighbors(records, hits):
    """Return one-hop endpoints and incident relations for node or relation hits."""
    ids={r['id'] for r in hits}
    for r in hits:
        if r.get('type')=='Relation':
            ids.update((r['source'],r['target']))
    edges=[r for r in records if r['type']=='Relation' and (r['source'] in ids or r['target'] in ids)]
    ids.update(r['source'] for r in edges);ids.update(r['target'] for r in edges)
    edge_ids={r['id'] for r in edges}
    return [r for r in records if r['id'] in ids or r['id'] in edge_ids]

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--id');p.add_argument('--type');p.add_argument('--status');p.add_argument('--text');p.add_argument('--neighbors', action='store_true')
    a=p.parse_args();records=read_graph(Path(__file__).resolve().parents[1])
    hits=[r for r in records if (not a.id or r['id']==a.id) and (not a.type or r['type']==a.type) and (not a.status or r['status']==a.status) and (not a.text or a.text.lower() in json.dumps(r,ensure_ascii=False).lower())]
    if a.neighbors:
        hits=expand_neighbors(records,hits)
    print(json.dumps(hits,ensure_ascii=False,indent=2,sort_keys=True))

if __name__=='__main__':
    main()
