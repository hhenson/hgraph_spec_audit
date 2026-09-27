"""Public source packages contain contracts and HGL, never host implementations."""
from pathlib import Path
import re
import subprocess
import unittest

ROOT = Path(__file__).resolve().parents[1]


class PackageBoundaries(unittest.TestCase):
    def test_source_only_packages(self):
        for directory in ('spec', 'stdlib'):
            root = ROOT / directory
            files = subprocess.check_output(['git', 'ls-files'], cwd=root, text=True).splitlines()
            self.assertTrue(files, f'{directory} is not initialized')
            for name in files:
                with self.subTest(package=directory, path=name):
                    path = root / name
                    self.assertNotIn(path.suffix, ('.py', '.cpp', '.cc', '.c', '.h', '.hpp', '.rs'))
                    if path.suffix in ('.md', '.hgl'):
                        source = path.read_text()
                        self.assertIsNone(re.search(r'^\s*```(?:python|py|cpp|c\+\+|rust)\b', source, re.M))
                        if path.suffix == '.hgl':
                            self.assertIsNone(re.search(r'^\s*cpp\s*\(', source, re.M))

    def test_audit_does_not_own_hgl(self):
        files = subprocess.check_output(['git', 'ls-files', '*.hgl'], cwd=ROOT, text=True).splitlines()
        self.assertEqual(files, [], 'HGL belongs to the pinned spec or standard library')
