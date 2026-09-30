"""The published release comparison is part of recorded-evidence validation."""
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]


class ReleasedEvidence(unittest.TestCase):
    def test_stale_released_assessment_is_rejected_without_rewriting_it(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            shutil.copytree(ROOT / 'runtime', root / 'runtime',
                            ignore=shutil.ignore_patterns('__pycache__'))
            released = Path('results/releases-0.5.42-0.8.30')
            shutil.copytree(ROOT / released, root / released)
            (root / 'tools').mkdir()
            checker = root / 'tools/check_recorded.py'
            shutil.copy2(ROOT / 'tools/check_recorded.py', checker)
            assessment = root / released / 'assessment.json'
            stale = json.loads(assessment.read_text())
            stale['totals']['both'] += 1
            assessment.write_text(json.dumps(stale))
            before = assessment.read_bytes()
            result = subprocess.run([sys.executable, str(checker)], capture_output=True, text=True)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn('released wiring assessment changed', result.stderr)
            self.assertEqual(assessment.read_bytes(), before)

    def test_changed_archived_expectation_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            shutil.copytree(ROOT / 'runtime', root / 'runtime',
                            ignore=shutil.ignore_patterns('__pycache__'))
            released = Path('results/releases-0.5.42-0.8.30')
            shutil.copytree(ROOT / released, root / released)
            (root / 'tools').mkdir()
            checker = root / 'tools/check_recorded.py'
            shutil.copy2(ROOT / 'tools/check_recorded.py', checker)
            reasoned = root / released / 'reasoned.json'
            altered = json.loads(reasoned.read_text())
            altered['caught_failure']['outcome']['expected'] = 'wires'
            reasoned.write_text(json.dumps(altered))
            result = subprocess.run([sys.executable, str(checker)], capture_output=True, text=True)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn('released wiring expectations changed', result.stderr)
