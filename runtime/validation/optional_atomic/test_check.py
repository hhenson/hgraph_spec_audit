import json
from pathlib import Path
import unittest
from check import validate

HERE = Path(__file__).resolve().parent


class OptionalAtomicEvidence(unittest.TestCase):
    def setUp(self):
        self.evidence = json.loads((HERE / 'observed.json').read_text())

    def test_recorded(self):
        validate(self.evidence)

    def test_unset_is_not_zero(self):
        self.evidence['engines']['cpp']['observations']['OptionalRecord']['raw'][0]['value'] = 0
        with self.assertRaises(AssertionError):
            validate(self.evidence)

    def test_empty_list_is_not_unset(self):
        self.evidence['engines']['cpp']['observations']['OptionalList']['raw'][3]['values'] = None
        with self.assertRaises(AssertionError):
            validate(self.evidence)

    def test_unset_struct_is_still_a_publication(self):
        self.evidence['engines']['cpp']['observations']['OptionalList']['raw'][0] = None
        with self.assertRaises(AssertionError):
            validate(self.evidence)

    def test_python_alias_is_not_hidden(self):
        case = self.evidence['engines']['python']['observations']['OptionalList']
        case['after_source'] = case['raw']
        with self.assertRaises(AssertionError):
            validate(self.evidence)

    def test_native_capture_does_not_alias(self):
        self.evidence['engines']['cpp']['observations']['OptionalList']['after_source'][1]['values'].append(2)
        with self.assertRaises(AssertionError):
            validate(self.evidence)


if __name__ == '__main__':
    unittest.main()
