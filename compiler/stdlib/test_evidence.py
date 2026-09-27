"""The accepted port traces and fixtures must stay tied to their evidence."""
import hashlib
import json
from pathlib import Path
import unittest

HERE = Path(__file__).resolve().parent


class Evidence(unittest.TestCase):
    def test_independent_engines_match_reasoned_ticks(self):
        corpus = HERE / 'cases.json'
        cases = json.loads(corpus.read_text())
        expected = {case['name']: case['expected'] for case in cases}
        self.assertEqual(len(expected), len(cases))
        for engine in ('python', 'cpp'):
            with self.subTest(engine=engine):
                evidence = json.loads((HERE / f'{engine}.json').read_text())
                self.assertEqual(evidence['engine'], engine)
                self.assertEqual(evidence['corpus_sha256'], hashlib.sha256(corpus.read_bytes()).hexdigest())
                self.assertEqual(set(evidence['observed']), set(expected))
                self.assertEqual(bool(evidence['native_binary_sha256']), engine == 'cpp')
                for name, ticks in expected.items():
                    self.assertEqual(evidence['observed'][name]['ticks'], ticks)
                    self.assertTrue(evidence['observed'][name]['matches'])

    def test_compiled_hgl_matches_current_shared_sources_and_ticks(self):
        evidence = json.loads((HERE / 'hgl-reference.json').read_text())
        expected = {c['name']: c['expected'] for c in json.loads((HERE / 'cases.json').read_text())}
        self.assertEqual(evidence['runtime_test_status'], 'passed')
        self.assertEqual(evidence['runtime_test_exit_code'], 0)
        self.assertEqual(evidence['repeats'], 3)
        self.assertEqual(set(evidence['observed']), set(expected))
        for name, ticks in expected.items():
            self.assertEqual(evidence['observed'][name], {'ticks': ticks, 'matches': True})
        digest = hashlib.sha256(json.dumps(evidence['observed'], sort_keys=True).encode()).hexdigest()
        self.assertEqual(evidence['replay_digests'], [digest] * 3)
        for name, digest in evidence['checked_source_sha256'].items():
            self.assertEqual(hashlib.sha256((HERE / name).read_bytes()).hexdigest(), digest)
        root = HERE.parents[1]
        for name, digest in evidence['harness_sha256'].items():
            self.assertEqual(hashlib.sha256((root / name).read_bytes()).hexdigest(), digest)
        for name, digest in evidence['stdlib_source_sha256'].items():
            self.assertEqual(hashlib.sha256((root / 'stdlib/hgl' / name).read_bytes()).hexdigest(), digest)
        self.assertTrue(evidence['compiler_sha256'])
        self.assertTrue(evidence['sdk_libraries_sha256'])


if __name__ == '__main__':
    unittest.main()
