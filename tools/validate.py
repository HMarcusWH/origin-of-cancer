#!/usr/bin/env python3
"""Validate authored inputs, source locks and documentation coverage offline."""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from oocgraph.core import IntegrityError, validate_repository
try:
    errors = validate_repository(Path(__file__).resolve().parents[1])
    if errors:
        print('\n'.join(errors)); raise SystemExit(1)
    print('PASS: repository/graph/source integrity. No biological truth is inferred.')
except (IntegrityError, OSError, ValueError) as exc:
    print(f'VALIDATION_FAILED: {exc}', file=sys.stderr); raise SystemExit(1)
