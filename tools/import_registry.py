#!/usr/bin/env python3
"""Inspect a frozen registry export; emit candidate intake records, never mutate graph.

Example: python tools/import_registry.py sources/baseline/registry/anchor_sources.json
Metadata remains unverified until an independent SourceVerification is admitted.
"""
import argparse,json,sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from oocgraph.core import loads,sha256
p=argparse.ArgumentParser(description=__doc__);p.add_argument('snapshot',type=Path);a=p.parse_args()
raw=a.snapshot.read_bytes();value=loads(raw.decode('utf-8'))
print(json.dumps({'source_sha256':sha256(raw),'mode':'CANDIDATE_INTAKE_ONLY','bibliographic_verification':'NOT_PERFORMED','graph_write':False,'snapshot':value},ensure_ascii=False,indent=2))
