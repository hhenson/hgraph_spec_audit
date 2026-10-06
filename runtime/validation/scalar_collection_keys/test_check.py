import json
from pathlib import Path
import unittest
from check import validate, validate_float

HERE = Path(__file__).resolve().parent


class ScalarKeyEvidence(unittest.TestCase):
    def setUp(self):
        self.evidence = json.loads((HERE / 'observed.json').read_text())
        self.floating = json.loads((HERE / 'float_observed.json').read_text())

    def test_recorded(self):
        validate(self.evidence)
        validate_float(self.floating)

    def test_missing_repeat(self):
        self.evidence['engines']['cpp']['observations']['enum']['map']['raw'][1] = None
        with self.assertRaises(AssertionError):
            validate(self.evidence)

    def test_collapsed_alias(self):
        self.evidence['engines']['cpp']['observations']['timezone']['a_equals_b'] = True
        with self.assertRaises(AssertionError):
            validate(self.evidence)

    def test_fabricated_zoned_time(self):
        self.evidence['engines']['cpp']['observations']['zoned_time'] = self.evidence['engines']['cpp']['observations']['timezone']
        with self.assertRaises(AssertionError):
            validate(self.evidence)

    def test_erased_nan_divergence(self):
        self.floating['engines']['cpp']['observations']['nan'] = self.floating['engines']['python']['observations']['nan']
        with self.assertRaises(AssertionError):
            validate_float(self.floating)

    def test_signed_zero_distinct(self):
        self.floating['engines']['cpp']['observations']['signed_zero']['a_equals_b'] = False
        with self.assertRaises(AssertionError):
            validate_float(self.floating)

    def test_missing_infinity(self):
        self.floating['engines']['cpp']['observations']['infinities']['set']['raw'][0]['add'].pop()
        with self.assertRaises(AssertionError):
            validate_float(self.floating)


if __name__ == '__main__':
    unittest.main()
