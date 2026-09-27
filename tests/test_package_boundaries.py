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


    def test_stdlib_contracts_implementations_and_tests_are_separate(self):
        root = ROOT / 'stdlib/hgl/hgraph'
        for name in ('operators', 'standard', 'control', 'stream', 'temporal'):
            with self.subTest(module=name):
                contract = (root / f'{name}.hgl').read_text()
                implementation = (root / 'impl' / f'{name}.hgl').read_text()
                tests = (root / 'tests' / f'{name}.hgl').read_text()
                self.assertRegex(contract, r'(?m)^operator ')
                self.assertNotRegex(contract, r'(?m)^(impl fn |fn |instantiate |test[ {])')
                self.assertRegex(implementation, r'(?m)^impl fn ')
                self.assertNotRegex(implementation, r'(?m)^(operator |property |test[ {])')
                self.assertRegex(tests, r'(?m)^test \{')
                self.assertNotRegex(tests, r'(?m)^(operator |impl fn |property |instantiate )')

    def test_scalar_reference_traces_match_reasoning(self):
        import hashlib
        import json
        corpus = ROOT / 'spec/compiler/native_scalar/cases.json'
        expected = {case['name']: case['expected'] for case in json.loads(corpus.read_text())}
        for engine, prefix in (('python', '0.5.'), ('cpp', '0.8.')):
            report = json.loads((ROOT / f'compiler/native_scalar/{engine}.json').read_text())
            self.assertEqual(report['observed'], expected)
            self.assertEqual(report['repeats'], 3)
            self.assertTrue(report['hgraph'].startswith(prefix))
            self.assertEqual(bool(report['native_binary_sha256']), engine == 'cpp')
            self.assertEqual(report['corpus_sha256'], hashlib.sha256(corpus.read_bytes()).hexdigest())
            self.assertEqual(report['harness_sha256'], hashlib.sha256((ROOT / 'tools/native_scalar_cases.py').read_bytes()).hexdigest())
