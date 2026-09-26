#!/usr/bin/env python3
"""Compatibility entrypoint: the unified build owns every generated view."""
from pathlib import Path
import subprocess
import sys
raise SystemExit(subprocess.call([sys.executable,str(Path(__file__).with_name('build.py')),*sys.argv[1:]]))
