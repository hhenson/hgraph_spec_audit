import importlib.util
import json
from pathlib import Path
import unittest
HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('nan_check', HERE / 'check.py')
check = importlib.util.module_from_spec(spec)
spec.loader.exec_module(check)


class NaNEvidenceTest(unittest.TestCase):
    def setUp(self): self.e = json.loads((HERE / 'observed.json').read_text())
    def reject(self, edit):
        edit()
        with self.assertRaises(AssertionError): check.validate(self.e)
    def test_saved_evidence(self): check.validate(self.e)
    def test_false_is_not_silence(self):
        self.reject(lambda: self.e['engines']['cpp']['observations']['nan_nan_eq']['raw_eval_node'].__setitem__(0, None))
    def test_false_is_not_zero(self):
        self.reject(lambda: self.e['engines']['cpp']['observations']['nan_nan_eq']['raw_eval_node'].__setitem__(0, 0))
    def test_nan_inequality_cannot_be_false(self):
        self.reject(lambda: self.e['engines']['python']['observations']['nan_nan_ne']['dense'].__setitem__(0, False))
    def test_finite_control_must_really_be_finite(self):
        self.reject(lambda: self.e['engines']['cpp']['observations']['finite_equal_eq']['events']['lhs'][0].update(value={'float_class':'nan'}, delta={'float_class':'nan'}))
    def test_nan_input_cannot_be_absent(self):
        self.reject(lambda: self.e['engines']['cpp']['observations']['nan_nan_eq']['events']['lhs'].clear())
    def test_comparison_error_cannot_replace_observation(self):
        self.reject(lambda: self.e['engines']['cpp']['observations']['nan_nan_eq'].update(status='error'))
    def test_domain_error_is_not_match(self):
        self.reject(lambda: self.e['engines']['python']['assessment'].update(ln_negative='match'))
    def test_error_is_not_capture(self):
        self.reject(lambda: self.e['engines']['python']['observations']['ln_negative'].update(raw_eval_node=[{'float_class':'nan'}, None]))
    def test_predicate_cannot_be_invented(self):
        self.reject(lambda: self.e['engines']['cpp']['primitives']['is_nan'].update(public_exported=True))
    def test_native_identity_required(self):
        self.reject(lambda: self.e['engines']['cpp']['identity'].update(native_artifacts={}))
    def test_comparison_case_cannot_disappear(self):
        self.reject(lambda: self.e['engines']['python']['observations'].pop('finite_nan_ge'))
    def test_ln_nan_classification_is_not_bit_identity(self):
        self.reject(lambda: self.e['engines']['cpp']['observations']['ln_negative']['raw_eval_node'][0].update(bits='7ff8000000000000'))


if __name__ == '__main__': unittest.main()
