"""Reject invented graph coverage and changes to measured type availability."""
import copy
import json
from pathlib import Path
import unittest
from check import validate

HERE = Path(__file__).resolve().parent


class EvidenceBoundary(unittest.TestCase):
    def setUp(self):
        self.evidence = json.loads((HERE / 'observed.json').read_text())

    def test_recorded(self):
        validate(self.evidence)

    def test_invented_graph_coverage(self):
        for engine in ('python', 'cpp'):
            with self.subTest(engine=engine):
                changed = copy.deepcopy(self.evidence)
                changed['engines'][engine]['graph_cases_executed'] = True
                with self.assertRaises(AssertionError):
                    validate(changed)

    def test_invented_export(self):
        for engine in ('python', 'cpp'):
            with self.subTest(engine=engine):
                changed = copy.deepcopy(self.evidence)
                changed['engines'][engine]['surfaces']['hgraph']['ZonedTime_exported'] = True
                with self.assertRaises(AssertionError):
                    validate(changed)

    def test_wrong_backend(self):
        self.evidence['engines']['python']['identity']['native'] = True
        with self.assertRaises(AssertionError):
            validate(self.evidence)

    def test_changed_harness(self):
        self.evidence['harness_sha256'] = '0' * 64
        with self.assertRaises(AssertionError):
            validate(self.evidence)


if __name__ == '__main__':
    unittest.main()
