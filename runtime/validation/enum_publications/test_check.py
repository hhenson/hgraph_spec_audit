"""Reject lost enum identity, dropped repeat publications and fabricated output."""
import json
from pathlib import Path
import unittest
from check import validate

HERE = Path(__file__).resolve().parent


class EnumEvidence(unittest.TestCase):
    def setUp(self):
        self.evidence = json.loads((HERE / 'observed.json').read_text())

    def test_recorded(self):
        validate(self.evidence)

    def test_dropped_repeat(self):
        self.evidence['engines']['cpp']['observations']['cases']['equal_distinct']['raw'].pop(1)
        with self.assertRaises(AssertionError):
            validate(self.evidence)

    def test_erased_nominal_identity(self):
        self.evidence['engines']['cpp']['observations']['cases']['equal_distinct']['raw'][0]['type'] = 'OtherMode'
        with self.assertRaises(AssertionError):
            validate(self.evidence)

    def test_narrowed_number(self):
        self.evidence['engines']['cpp']['observations']['cases']['equal_distinct']['raw'][-1]['number'] = 2147483647
        with self.assertRaises(AssertionError):
            validate(self.evidence)

    def test_fabricated_all_silent(self):
        self.evidence['engines']['python']['observations']['cases']['all_silent']['raw'] = [None, None]
        with self.assertRaises(AssertionError):
            validate(self.evidence)

    def test_changed_retained_recording(self):
        self.evidence['engines']['python']['observations']['cases']['equal_distinct']['first_after_second'] = []
        with self.assertRaises(AssertionError):
            validate(self.evidence)


if __name__ == '__main__':
    unittest.main()
