import json
from pathlib import Path
import unittest
from check import validate

HERE = Path(__file__).resolve().parent


class GrowingListEvidence(unittest.TestCase):
    def setUp(self):
        self.evidence = json.loads((HERE / 'observed.json').read_text())

    def test_recorded(self):
        validate(self.evidence)

    def test_lost_tail_removal(self):
        self.evidence['engines']['cpp']['observations']['growth_update_shrink']['raw'][-1].pop('2')
        with self.assertRaises(AssertionError):
            validate(self.evidence)

    def test_empty_truncation_hidden(self):
        self.evidence['engines']['cpp']['observations']['shrink_empty_regrow']['raw'][1] = None
        with self.assertRaises(AssertionError):
            validate(self.evidence)

    def test_fabricated_python_growth(self):
        self.evidence['engines']['python']['observations']['repeat_child'] = self.evidence['engines']['cpp']['observations']['repeat_child']
        with self.assertRaises(AssertionError):
            validate(self.evidence)

    def test_unrelated_python_failure(self):
        self.evidence['engines']['python']['observations']['repeat_child']['error'] = 'unrelated failure'
        with self.assertRaises(AssertionError):
            validate(self.evidence)


if __name__ == '__main__':
    unittest.main()
