import json
from pathlib import Path
import unittest
from check import validate

HERE = Path(__file__).resolve().parent


class AtomicCollectionsEvidence(unittest.TestCase):
    def setUp(self):
        self.evidence = json.loads((HERE / 'observed.json').read_text())

    def test_recorded(self):
        validate(self.evidence)

    def test_empty_snapshot_lost(self):
        self.evidence['engines']['cpp']['observations']['set_snapshots']['raw'][1] = None
        with self.assertRaises(AssertionError):
            validate(self.evidence)

    def test_sparse_merge_substituted(self):
        self.evidence['engines']['cpp']['observations']['map_snapshots']['raw'][-1]['map'].append(['b', 2])
        with self.assertRaises(AssertionError):
            validate(self.evidence)

    def test_python_alias_hidden(self):
        case = self.evidence['engines']['python']['observations']['map_list_retention']
        case['first_after_source_mutation'] = case['raw']
        with self.assertRaises(AssertionError):
            validate(self.evidence)

    def test_native_nested_alias(self):
        case = self.evidence['engines']['cpp']['observations']['map_list_retention']
        case['first_after_source_mutation'] = case['second_raw']
        with self.assertRaises(AssertionError):
            validate(self.evidence)

    def test_immutable_set_failure_hidden(self):
        self.evidence['engines']['cpp']['observations']['set_retention'].pop('capture_mutation_error')
        with self.assertRaises(AssertionError):
            validate(self.evidence)


if __name__ == '__main__':
    unittest.main()
