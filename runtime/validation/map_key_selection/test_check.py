import json
from pathlib import Path
import unittest
import check
import observe

HERE = Path(__file__).resolve().parent


class RecordedMapSelection(unittest.TestCase):
    def setUp(self):
        self.record = json.loads((HERE / 'observed.json').read_text())

    def reject(self):
        # Recompute process hashes so semantic checks also protect the evidence.
        for measured in self.record['engines'].values():
            payload = {key: measured[key] for key in ('identity', 'cases', 'scalar_dictionary')}
            measured['runs_sha256'] = [observe.digest(payload)] * 3
        with self.assertRaises(AssertionError):
            check.check(self.record)

    def rewrite_row(self, engine, case, row, column, value):
        actual = self.record['engines'][engine]['cases'][case]
        actual['events'][row][column] = value
        actual['raw_eval_node'][row] = json.dumps(actual['events'][row])

    def test_recorded(self):
        self.assertTrue(check.check(self.record))

    def test_cpp_invalidation_variation_cannot_be_silently_repaired(self):
        self.rewrite_row('cpp', 'invalid_child_membership', 2, 3, False)
        self.record['engines']['cpp']['assessment']['invalid_child_membership'] = 'match'
        self.reject()

    def test_python_empty_repeat_variation_cannot_be_silently_repaired(self):
        self.rewrite_row('python', 'key_changes', 3, 1, False)
        self.record['engines']['python']['assessment']['key_changes'] = 'match'
        self.reject()

    def test_expiry_error_cannot_be_replaced_with_required_rows(self):
        expected = json.loads((HERE / 'reasoned.json').read_text())['cases']['held_removal_readd']['expected']
        measured = self.record['engines']['python']
        measured['cases']['held_removal_readd'] = {'events': expected, 'raw_eval_node': list(map(json.dumps, expected))}
        measured['assessment']['held_removal_readd'] = 'match'
        self.reject()

    def test_removal_cycle_held_value_cannot_be_dropped(self):
        self.rewrite_row('cpp', 'held_removal_readd', 4, 8, None)
        self.reject()

    def test_equal_payload_new_target_sample_cannot_be_dropped(self):
        self.rewrite_row('cpp', 'key_changes', 1, 3, False)
        self.reject()

    def test_first_empty_designation_cannot_be_invalid(self):
        self.rewrite_row('cpp', 'unpublished_map', 0, 0, False)
        self.reject()

    def test_build_error_cannot_stand_in_for_strict_lookup_failure(self):
        self.record['engines']['cpp']['scalar_dictionary']['strict_missing']['failures'] = []
        self.reject()

    def test_strict_lookup_failure_cannot_also_return_raw_output(self):
        for engine in ('cpp', 'python'):
            with self.subTest(engine=engine):
                self.record = json.loads((HERE / 'observed.json').read_text())
                self.record['engines'][engine]['scalar_dictionary']['strict_missing']['raw_eval_node'] = ['0']
                self.reject()

    def test_null_cannot_be_replaced_by_silence(self):
        self.record['engines']['python']['scalar_dictionary']['safe']['raw_eval_node'][1] = None
        self.reject()

    def test_raw_and_observer_rows_must_agree(self):
        self.record['engines']['cpp']['cases']['membership']['raw_eval_node'][0] = 'null'
        self.reject()

    def test_support_and_source_hashes_required(self):
        self.record['support_sha256']['delta_eval/observe.py'] = '0' * 64
        self.reject()

    def test_fresh_process_fingerprints_required(self):
        self.record['engines']['cpp']['runs_sha256'][1] = '0' * 64
        with self.assertRaises(AssertionError):
            check.check(self.record)


if __name__ == '__main__':
    unittest.main()
