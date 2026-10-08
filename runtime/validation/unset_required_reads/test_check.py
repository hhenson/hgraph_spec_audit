import json
from pathlib import Path
import unittest
from check import validate

HERE = Path(__file__).resolve().parent

class EvidenceIntegrity(unittest.TestCase):
    def setUp(self):
        self.cases = json.loads((HERE/'reasoned.json').read_text())['cases']
        self.public = json.loads((HERE/'observed.json').read_text())
        self.native = json.loads((HERE/'native_observed.json').read_text())

    def test_recorded_evidence(self):
        validate(self.cases, self.public, self.native)

    def test_false_cannot_be_mistaken_for_absence(self):
        self.native['observations']['bool_false']['retained_child_valid'] = False
        with self.assertRaises(AssertionError): validate(self.cases, self.public, self.native)

    def test_collection_coercion_variation_is_not_repaired(self):
        self.public['engines']['python']['observations']['list_unset']['reads'][1]['result'] = 0
        with self.assertRaises(AssertionError): validate(self.cases, self.public, self.native)

    def test_native_absence_cannot_be_defaulted(self):
        self.native['observations']['scalar_unset'].update(outcome='value',result=0)
        with self.assertRaises(AssertionError): validate(self.cases, self.public, self.native)

    def test_missing_case_fails(self):
        del self.native['observations']['map_unset']
        with self.assertRaises(AssertionError): validate(self.cases, self.public, self.native)

if __name__ == '__main__': unittest.main()
