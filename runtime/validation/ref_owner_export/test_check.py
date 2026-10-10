import json
from pathlib import Path
import unittest
import check

HERE = Path(__file__).resolve().parent

class RecordedCaptures(unittest.TestCase):
    def setUp(self):
        self.record = json.loads((HERE / 'observed.json').read_text())
    def rejected(self):
        # Recompute process digests so semantic checks, not just a checksum, reject.
        for measured in self.record['engines'].values():
            measured['runs_sha256'] = [check.digest({'identity': measured['identity'], 'cases': measured['cases']})] * 3
        with self.assertRaises(AssertionError):
            check.check(self.record)
    def test_recorded(self):
        self.assertTrue(check.check(self.record))
    def test_nested_current_value_cannot_be_replaced_with_inactive_source(self):
        self.record['engines']['python']['cases']['nested_scalar_first']['events'][1] = 8
        self.rejected()
    def test_tree_partial_retarget_cannot_be_reported_as_full_sample(self):
        self.record['engines']['python']['cases']['exported_tree_first']['events'][3]['left'] = 8
        self.rejected()
    def test_equal_valued_new_child_sample_cannot_be_dropped(self):
        del self.record['engines']['python']['cases']['exported_tree_first']['events'][5]['left']
        self.rejected()
    def test_raw_capture_cannot_be_replaced_by_the_decoded_view(self):
        case = self.record['engines']['cpp']['cases']['nested_scalar_first']
        case['raw_eval_node'] = case.get('decoded_eval_node', [])
        self.rejected()
    def test_cpp_missing_retarget_cannot_be_silently_repaired(self):
        measured = self.record['engines']['cpp']
        for name in ('exported_tree_first', 'exported_tree_fresh'):
            case = measured['cases'][name]
            case['raw_eval_node'][3] = '{"right": 8}'
            case['decoded_eval_node'][3] = {"right": 8}
            case['dense_from_input_horizon'][3] = {"right": 8}
            case['events'].insert(3, {"right": 8})
            measured['assessment'][name] = 'match'
        self.rejected()
    def test_fresh_run_cannot_change_its_capture(self):
        self.record['engines']['python']['cases']['nested_scalar_fresh']['events'][0] = 0
        self.rejected()
    def test_cpp_cannot_be_reported_as_pure_python(self):
        self.record['engines']['cpp']['identity']['native'] = False
        self.rejected()
    def test_source_fingerprint_required(self):
        self.record['sources_sha256']['reasoned.json'] = '0' * 64
        self.rejected()
    def test_match_assessment_cannot_hide_a_changed_capture(self):
        measured = self.record['engines']['python']
        current = measured['assessment']['nested_scalar_first']
        measured['assessment']['nested_scalar_first'] = 'match' if current != 'match' else 'divergence'
        self.rejected()

if __name__ == '__main__':
    unittest.main()
