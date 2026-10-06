import json
from pathlib import Path
import unittest
from check import validate

HERE = Path(__file__).resolve().parent


class RollingEvidence(unittest.TestCase):
    def setUp(self):
        self.direct = json.loads((HERE / 'observed.json').read_text())
        self.composed = json.loads((HERE / 'composed_observed.json').read_text())

    def test_recorded(self):
        validate(self.direct)
        validate(self.composed, True)

    def test_sticky_native_readiness(self):
        self.direct['engines']['cpp']['observations']['duration_gap']['received'][-1]['all_valid'] = True
        with self.assertRaises(AssertionError):
            validate(self.direct)

    def test_hidden_native_operator_zero_min(self):
        self.composed['engines']['cpp']['observations']['duration_zero_min']['received'][0]['all_valid'] = True
        with self.assertRaises(AssertionError):
            validate(self.composed, True)

    def test_invented_python_first_arrival(self):
        self.composed['engines']['python']['observations']['duration_gap']['raw'][0] = 10
        with self.assertRaises(AssertionError):
            validate(self.composed, True)

    def test_invented_python_direct(self):
        self.direct['engines']['python']['observations']['tick'] = self.direct['engines']['cpp']['observations']['tick']
        with self.assertRaises(AssertionError):
            validate(self.direct)

    def test_dropped_equal_arrival(self):
        self.direct['engines']['cpp']['observations']['equal_arrivals']['raw'][1] = None
        with self.assertRaises(AssertionError):
            validate(self.direct)


if __name__ == '__main__':
    unittest.main()
