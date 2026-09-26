#!/usr/bin/env python3
"""Read-only scoped resolver; --check also verifies generated projections."""
import argparse,json,subprocess,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT))
from oocgraph.core import read_graph,resolve
p=argparse.ArgumentParser(description=__doc__);p.add_argument('--check',action='store_true');a=p.parse_args()
print(json.dumps(resolve(read_graph(ROOT)),indent=2))
if a.check:sys.exit(subprocess.call([sys.executable,str(ROOT/'tools/build.py'),'--check']))
