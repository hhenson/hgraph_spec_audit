"""Harness failures must never become accepted semantic variations."""
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]


class WiringEvidence(unittest.TestCase):
    def test_failed_or_unstable_runs_do_not_publish_an_assessment(self):
        for engine in ('python', 'cpp'):
            for marker in ('harness_error', 'unstable'):
                with self.subTest(engine=engine, marker=marker), tempfile.TemporaryDirectory() as tmp:
                    root = Path(tmp) / 'runtime'
                    shutil.copytree(ROOT / 'runtime', root, ignore=shutil.ignore_patterns('__pycache__'))
                    folder = root / 'validation/wiring'
                    observed = json.loads((folder / 'observed.json').read_text())
                    case = next(iter(observed['cases']))
                    observed['cases'][case][engine] = {marker: 'failed replay'}
                    (folder / 'observed.json').write_text(json.dumps(observed))
                    assessment = folder / 'assessment.json'
                    before = assessment.read_bytes()
                    result = subprocess.run([sys.executable, str(folder / 'check.py')],
                                            capture_output=True, text=True)
                    self.assertNotEqual(result.returncode, 0)
                    self.assertIn(f'{case}.{engine}: {marker}', result.stderr)
                    self.assertEqual(assessment.read_bytes(), before)
