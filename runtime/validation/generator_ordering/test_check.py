"""Reject fabricated ordering enforcement or missing operand effects."""
import contextlib
import copy
import io
import json
from pathlib import Path
import unittest
import check

HERE = Path(__file__).resolve().parent


class EvidenceTests(unittest.TestCase):
    def setUp(self):
        self.corpus = json.loads((HERE / 'reasoned.json').read_text())
        self.evidence = json.loads((HERE / 'observed.json').read_text())

    def verify(self):
        with contextlib.redirect_stdout(io.StringIO()):
            check.validate(self.corpus, self.evidence)

    def test_preserved_facts_pass(self):
        self.verify()

    def test_python_skips_cannot_be_rewritten_as_rejection(self):
        observations = self.evidence['engines']['python']['observations']
        observations['repeat_past_epoch']['fails'] = True
        with self.assertRaises(AssertionError):
            self.verify()

    def test_native_first_halt_cannot_claim_second_operands(self):
        observed = self.evidence['engines']['cpp']['observations']['decrease_past_preepoch']
        observed['trace'] += ['after1', 'time2', 'value2']
        with self.assertRaises(AssertionError):
            self.verify()

    def test_native_rejection_preserves_both_second_operand_effects(self):
        self.evidence['engines']['cpp']['observations']['repeat_future']['trace'].pop()
        with self.assertRaises(AssertionError):
            self.verify()

    def test_generic_error_cannot_stand_for_order_failure(self):
        self.evidence['engines']['cpp']['observations']['decrease_future']['error_message'] = 'allocation failed'
        with self.assertRaises(AssertionError):
            self.verify()

    def test_lost_and_skipped_python_payloads_cannot_be_repaired(self):
        original = copy.deepcopy(self.evidence)
        for name in ('repeat_future', 'decrease_future'):
            with self.subTest(case=name):
                self.evidence = copy.deepcopy(original)
                observed = self.evidence['engines']['python']['observations'][name]
                observed.update(raw=[None, 1, 2, 3], downstream_payloads=[1, 2, 3])
                with self.assertRaises(AssertionError):
                    self.verify()

    def test_increasing_control_must_finish_and_capture_all_payloads(self):
        self.evidence['engines']['cpp']['observations']['increase_future']['downstream_payloads'].pop()
        with self.assertRaises(AssertionError):
            self.verify()


if __name__ == '__main__':
    unittest.main()
