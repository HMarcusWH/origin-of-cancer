"""Frozen source locks survive an actual Git index/check-out round trip."""
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]

class GitSourceRoundtripTests(unittest.TestCase):
    def test_git_preserves_frozen_source_csv_bytes(self):
        if not shutil.which('git'):
            self.skipTest('Git is required for this source transport regression')
        with tempfile.TemporaryDirectory() as directory:
            dst = Path(directory)
            shutil.copyfile(ROOT / '.gitattributes', dst / '.gitattributes')
            for relative in ('sources/baseline/edges_v1_3.csv',
                             'sources/baseline/edges_v1_3_core_schema.csv'):
                target = dst / relative
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(ROOT / relative, target)
            subprocess.run(['git', 'init', '-q', str(dst)], check=True)
            subprocess.run(['git', '-C', str(dst), 'add', '.'], check=True)
            for relative in ('sources/baseline/edges_v1_3.csv',
                             'sources/baseline/edges_v1_3_core_schema.csv'):
                original = (ROOT / relative).read_bytes()
                indexed = subprocess.check_output(['git', '-C', str(dst), 'show', ':' + relative])
                self.assertEqual(original, indexed)
                (dst / relative).unlink()
                subprocess.run(['git', '-C', str(dst), 'checkout-index', '--', relative], check=True)
                self.assertEqual(original, (dst / relative).read_bytes())
