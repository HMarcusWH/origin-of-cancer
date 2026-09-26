#!/usr/bin/env python3
"""Build a deterministic review ZIP outside the repository; no scientific promotion."""
import argparse
from pathlib import Path
import subprocess
import sys
import zipfile
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from oocgraph.core import file_inventory,sha256
root=Path(__file__).resolve().parents[1]
p=argparse.ArgumentParser(description=__doc__);p.add_argument('--output',required=True,type=Path);a=p.parse_args()
output=a.output.resolve()
if output.is_relative_to(root):p.error('Output must be outside the source tree to avoid self-inclusion.')
subprocess.run([sys.executable,str(root/'tools/build.py'),'--check'],check=True)
output.parent.mkdir(parents=True,exist_ok=True)
with zipfile.ZipFile(output,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
    for name in file_inventory(root):
        info=zipfile.ZipInfo(name,date_time=(2026,9,26,0,0,0));info.compress_type=zipfile.ZIP_DEFLATED
        info.external_attr=0o100644<<16;info.create_system=3
        z.writestr(info,(root/name).read_bytes(),compress_type=zipfile.ZIP_DEFLATED,compresslevel=9)
print(f'{sha256(output.read_bytes())}  {output}')
