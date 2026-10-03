"""Preserve negative-duration disagreements and exact operand/error ordering."""
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

    def test_recorded_facts_pass(self):
        self.verify()

    def test_negative_error_cannot_be_replaced_by_generic_exception(self):
        for engine, name in [('python', 'negative_start'), ('cpp', 'negative_later')]:
            with self.subTest(engine=engine):
                self.setUp()
                self.evidence['engines'][engine]['observations'][name]['error_message'] = 'unrelated failure'
                with self.assertRaises(AssertionError):
                    self.verify()

    def test_later_python_acceptance_cannot_be_rewritten_as_rejection(self):
        observations = self.evidence['engines']['python']['observations']
        observations['negative_later'] = copy.deepcopy(observations['negative_start'])
        observations['negative_later']['trace'] = self.corpus['cases']['negative_later']['expected']['trace']
        with self.assertRaises(AssertionError):
            self.verify()

    def test_payload_cannot_run_after_explicit_time_expression_underflow(self):
        self.evidence['engines']['cpp']['observations']['time_expression_underflow']['trace'].append('value')
        with self.assertRaises(AssertionError):
            self.verify()

    def test_implicit_underflow_must_preserve_both_operand_effects(self):
        self.evidence['engines']['python']['observations']['negative_target_underflow']['trace'].pop()
        with self.assertRaises(AssertionError):
            self.verify()

    def test_sentinel_in_traceback_cannot_replace_terminal_cause(self):
        observed = self.evidence['engines']['cpp']['observations']['negative_payload_failure']
        observed['error_message'] = observed['error_message'].replace(
            '\nRuntimeError: negative-payload-operand-sentinel\n', '\nMemoryError: unrelated failure\n')
        with self.assertRaises(AssertionError):
            self.verify()

    def test_past_absolute_skip_cannot_be_changed_to_negative_admission(self):
        observations = self.evidence['engines']['python']['observations']
        observations['past_absolute_start'] = copy.deepcopy(observations['negative_start'])
        with self.assertRaises(AssertionError):
            self.verify()


if __name__ == '__main__':
    unittest.main()
