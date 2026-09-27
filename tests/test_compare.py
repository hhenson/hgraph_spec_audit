from pathlib import Path
import subprocess
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]


class OutputSafety(unittest.TestCase):
    def test_output_under_source_is_rejected_before_runtime_probe(self):
        output = ROOT / 'runtime/validation/wiring/rejected-output'
        self.assertFalse(output.exists())
        result = subprocess.run([sys.executable, str(ROOT / 'tools/compare.py'),
                                 '--reference', 'missing-reference', '--candidate', 'missing-candidate',
                                 '--output', str(output)], capture_output=True, text=True)
        self.assertEqual(result.returncode, 2)
        self.assertIn('outside the wiring source', result.stderr)
        self.assertFalse(output.exists())
