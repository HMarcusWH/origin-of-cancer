#!/usr/bin/env python3
"""Validate and deterministically render the complete offline reviewer surface."""
from pathlib import Path
import argparse
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from oocgraph.core import IntegrityError, validate_repository
from oocgraph.views import make_views

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument('--write', action='store_true')
    mode.add_argument('--check', action='store_true')
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    root = args.root.resolve()
    try:
        errors = validate_repository(root)
        if errors:
            print('\n'.join(errors), file=sys.stderr); return 1
        products = make_views(root)
        stale = []
        for name, text in products.items():
            path = root / name
            expected = text.encode('utf-8')
            if args.write:
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_bytes(expected)
            elif not path.is_file() or path.read_bytes() != expected:
                stale.append(name)
        if stale:
            print('GENERATED_DRIFT:\n'+'\n'.join(stale), file=sys.stderr); return 1
        print(f'PASS: {len(products)} deterministic products; engineering conformance only.')
        print('Biological validation: NOT ESTABLISHED. Cancer kernel: UNFROZEN.')
        return 0
    except (IntegrityError, OSError, ValueError) as exc:
        print(f'BUILD_FAILED: {exc}', file=sys.stderr); return 1
if __name__ == '__main__':
    raise SystemExit(main())
