import importlib.util
import json
from pathlib import Path
import unittest

HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location('structural_publication_check', HERE / 'check.py')
CHECK = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(CHECK)


class EvidenceChecks(unittest.TestCase):
    def setUp(self):
        self.e = json.loads((HERE / 'observed.json').read_text())
        self.n = json.loads((HERE / 'native_observed.json').read_text())

    def test_recorded_evidence(self):
        CHECK.verify(self.e, self.n)

    def test_cannot_relabel_merging_return_as_reconciliation(self):
        self.e['engines']['cpp']['assessment']['map_remove_return_value']['state'] = 'match'
        with self.assertRaises(AssertionError): CHECK.verify(self.e, self.n)

    def test_cannot_relabel_missing_copy_method_as_success(self):
        self.e['engines']['cpp']['assessment']['fixed_copy_from_input']['state'] = 'match'
        with self.assertRaises(AssertionError): CHECK.verify(self.e, self.n)

    def test_boolean_validity_is_not_integer_one(self):
        case = self.e['engines']['python']['observations']['fixed_copy_from_input']
        case['cycles'][0]['output']['children']['0']['valid'] = 1
        with self.assertRaises(AssertionError): CHECK.verify(self.e, self.n)

    def test_no_atomic_tuple_substitution(self):
        self.e['engines']['python']['structural_tuple']['atomic_substitute_used'] = True
        with self.assertRaises(AssertionError): CHECK.verify(self.e, self.n)

    def test_native_nil_loss_is_not_a_match(self):
        self.n['assessment']['fixed']['state'] = 'match'
        with self.assertRaises(AssertionError): CHECK.verify(self.e, self.n)

    def test_native_retention_observation_required(self):
        self.n['observed']['fixed'].pop('retentions')
        with self.assertRaises((AssertionError, KeyError)): CHECK.verify(self.e, self.n)


if __name__ == '__main__': unittest.main()
