"""A matching operand trace alone cannot establish duplicate-publication failure."""
import contextlib
import io
import json
from pathlib import Path
import unittest
import check

HERE = Path(__file__).resolve().parent


class EvidenceTests(unittest.TestCase):
    def setUp(self):
        self.reasoned = json.loads((HERE / 'reasoned.json').read_text())
        self.evidence = json.loads((HERE / 'observed.json').read_text())

    def verify(self):
        with contextlib.redirect_stdout(io.StringIO()):
            check.validate(self.reasoned, self.evidence)

    def test_saved_evidence_passes(self):
        self.verify()

    def test_unrelated_exception_after_operands_is_rejected(self):
        for engine in ('python', 'cpp'):
            with self.subTest(engine=engine):
                self.setUp()
                result = self.evidence['engines'][engine]
                observed = result['observations']['duplicate_due']
                observed['error_message'] = 'MemoryError: unrelated allocation failure'
                # Even relabelling the failed expectation must fail the claimed agreement.
                result['assessment']['duplicate_due'] = 'divergence'
                with self.assertRaises(AssertionError):
                    self.verify()

    def test_diagnostic_in_traceback_does_not_establish_cause(self):
        result = self.evidence['engines']['python']['observations']['duplicate_due']
        result['error_message'] = 'unrelated failure\nNodeError: memory failure\n' + result['error_message']
        with self.assertRaises(AssertionError):
            self.verify()

    def test_wrong_exception_type_is_rejected(self):
        self.evidence['engines']['cpp']['observations']['duplicate_due']['error_type'] = 'MemoryError'
        with self.assertRaises(AssertionError):
            self.verify()

    def test_missing_raw_error_is_rejected(self):
        self.evidence['engines']['python']['observations']['duplicate_due']['error_message'] = ''
        with self.assertRaises(AssertionError):
            self.verify()

    def test_fabricated_operand_sentinel_is_rejected(self):
        self.evidence['engines']['cpp']['observations']['time_failure']['error_message'] = 'unrelated failure'
        with self.assertRaises(AssertionError):
            self.verify()

    def test_native_digest_tampering_is_rejected(self):
        self.evidence['engines']['cpp']['identity']['loaded_hgraph_libraries']['libhgraph_runtime.so'] = 'f' * 64
        with self.assertRaises(AssertionError):
            self.verify()


if __name__ == '__main__':
    unittest.main()
