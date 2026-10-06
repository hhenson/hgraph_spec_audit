"""Regression checks against false publication/state/provenance claims."""
import copy
import importlib.util
import json
from pathlib import Path
import unittest
HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('boundary_check', HERE / 'check.py')
check = importlib.util.module_from_spec(spec)
spec.loader.exec_module(check)


class BoundaryEvidenceTest(unittest.TestCase):
    def setUp(self):
        self.e = json.loads((HERE / 'observed.json').read_text())
        self.g = json.loads((HERE / 'growing_observed.json').read_text())
    def verify(self): check.validate(self.e, 'reasoned.json', 'observe.py')
    def reject(self, edit):
        edit()
        with self.assertRaises(AssertionError): self.verify()
    def test_saved_evidence(self):
        self.verify()
        check.validate(self.g, 'growing_reasoned.json', 'growing_observe.py', True)
    def test_suppressed_empty_event_cannot_be_match(self):
        self.reject(lambda: self.e['engines']['cpp']['assessment']['cancel_set'][1].update(status='match'))
    def test_real_empty_event_cannot_disappear(self):
        self.reject(lambda: self.e['engines']['cpp']['observations']['cancel_set']['source_events'].pop())
    def test_empty_publication_is_not_silence(self):
        self.reject(lambda: self.e['engines']['python']['observations']['empty_map']['raw_eval_node'].__setitem__(0, None))
    def test_raw_no_output_is_not_empty_recording(self):
        self.reject(lambda: self.e['engines']['cpp']['observations']['empty_struct'].update(raw_eval_node=[]))
    def test_padding_cannot_be_invented(self):
        self.reject(lambda: self.e['engines']['python']['observations']['empty_fixed'].update(padding_added=0))
    def test_invalid_child_is_not_removed_membership(self):
        self.reject(lambda: self.e['engines']['cpp']['observations']['child_map']['cycles'][1]['source']['members'].remove('7'))
    def test_invalid_membership_cannot_be_claimed_copied(self):
        self.reject(lambda: self.e['engines']['cpp']['observations']['invalid_member_map']['cycles'][1]['forward']['members'].append('9'))
    def test_whole_python_list_difference_cannot_be_relabelled(self):
        self.reject(lambda: self.e['engines']['python']['assessment']['whole_fixed'][0].update(status='match'))
    def test_runtime_error_cannot_be_successful_empty_capture(self):
        self.reject(lambda: self.e['engines']['python']['observations']['whole_struct'].update(raw_eval_node=None))
    def test_zero_size_error_cannot_be_publication(self):
        self.reject(lambda: self.e['engines']['cpp']['observations']['empty_fixed_zero'].update(capability='supported'))
    def test_native_identity_is_required(self):
        self.reject(lambda: self.e['engines']['cpp']['identity'].update(loaded_hgraph_libraries={}))
    def test_boolean_metadata_is_not_zero(self):
        self.reject(lambda: self.e['engines']['cpp']['observations']['whole_scalar']['cycles'][1]['source'].update(valid=0))
    def test_missing_case_is_rejected(self):
        self.reject(lambda: self.e['engines']['cpp']['observations'].pop('child_map'))
    def test_growing_population_error_is_not_match(self):
        self.g['engines']['python']['assessment']['invalid_position'][0]['status'] = 'match'
        with self.assertRaises(AssertionError): check.validate(self.g, 'growing_reasoned.json', 'growing_observe.py', True)
    def test_growing_removal_control_cannot_drop_capture(self):
        self.g['engines']['cpp']['observations']['truncate_control']['raw_eval_node'][1] = None
        with self.assertRaises(AssertionError): check.validate(self.g, 'growing_reasoned.json', 'growing_observe.py', True)


if __name__ == '__main__': unittest.main()
