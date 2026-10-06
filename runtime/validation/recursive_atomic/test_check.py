import json
from pathlib import Path
import unittest
from check import validate

HERE = Path(__file__).resolve().parent


class RecursiveAtomicEvidence(unittest.TestCase):
    def setUp(self):
        self.evidence = json.loads((HERE / 'observed.json').read_text())

    def test_recorded(self):
        validate(self.evidence)

    def test_missing_repeat(self):
        self.evidence['engines']['cpp']['observations']['self_snapshots']['raw'][1] = None
        with self.assertRaises(AssertionError):
            validate(self.evidence)

    def test_wrong_deep_identity(self):
        self.evidence['engines']['cpp']['observations']['mutual_snapshots']['raw'][0]['other']['type'] = 'MutualA'
        with self.assertRaises(AssertionError):
            validate(self.evidence)

    def test_leaf_retains_old_subtree(self):
        case = self.evidence['engines']['cpp']['observations']['self_snapshots']
        case['raw'][-1]['next'] = case['raw'][0]['next']
        with self.assertRaises(AssertionError):
            validate(self.evidence)

    def test_hidden_python_alias(self):
        case = self.evidence['engines']['python']['observations']['self_retention']
        case['first_after_source_mutation'] = case['raw']
        with self.assertRaises(AssertionError):
            validate(self.evidence)

    def test_native_deep_alias(self):
        case = self.evidence['engines']['cpp']['observations']['self_retention']
        case['first_after_source_mutation'] = case['second_raw']
        with self.assertRaises(AssertionError):
            validate(self.evidence)


if __name__ == '__main__':
    unittest.main()
