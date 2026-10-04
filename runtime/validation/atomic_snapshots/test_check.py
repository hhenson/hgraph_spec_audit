"""Snapshot agreement cannot hide omitted empty ticks, defaults or aliasing."""
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
        self.reasoned = json.loads((HERE / 'reasoned.json').read_text())
        self.evidence = json.loads((HERE / 'observed.json').read_text())

    def verify(self):
        with contextlib.redirect_stdout(io.StringIO()):
            check.validate(self.reasoned, self.evidence)

    def test_saved_evidence_passes(self):
        self.verify()

    def test_python_aliasing_cannot_be_repaired_into_independence(self):
        observed = self.evidence['engines']['python']['observations']['list_shared_captures']
        observed['raw_after_source_mutation'] = copy.deepcopy(observed['raw_after_eval'])
        with self.assertRaises(AssertionError):
            self.verify()

    def test_native_other_capture_must_remain_independent(self):
        observed = self.evidence['engines']['cpp']['observations']['list_shared_captures']
        observed['raw_after_capture_mutation'][2].append(888)
        with self.assertRaises(AssertionError):
            self.verify()

    def test_empty_atomic_list_is_a_publication(self):
        observed = self.evidence['engines']['cpp']['observations']['list_i64']
        observed['raw_after_eval'][-1] = None
        observed['received'].pop()
        with self.assertRaises(AssertionError):
            self.verify()

    def test_defaulted_fields_are_part_of_the_complete_value(self):
        observed = self.evidence['engines']['python']['observations']['defaulted_nominal']
        del observed['raw_after_eval'][0]['ask']
        with self.assertRaises(AssertionError):
            self.verify()

    def test_scalar_types_are_not_erased(self):
        observed = self.evidence['engines']['cpp']['observations']['tuple_eight_scalars']
        observed['raw_after_eval'][0][0] = 0
        with self.assertRaises(AssertionError):
            self.verify()

    def test_loaded_library_tampering_is_rejected(self):
        self.evidence['engines']['cpp']['identity']['loaded_hgraph_libraries']['libhgraph_runtime.so'] = 'f' * 64
        with self.assertRaises(AssertionError):
            self.verify()


if __name__ == '__main__':
    unittest.main()
