"""Do not conflate construction/JSON success with provider membership."""
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
        self.observed = self.evidence['engines']['cpp']['observations']

    def verify(self):
        with contextlib.redirect_stdout(io.StringIO()):
            check.validate(self.reasoned, self.evidence)

    def reject(self):
        with self.assertRaises(AssertionError):
            self.verify()

    def test_recorded_evidence(self):
        self.verify()

    def test_wrong_case_provider_acceptance_is_rejected(self):
        self.observed['utc']['at_zone_with_provider'] = self.observed['UTC']['at_zone_with_provider']
        self.reject()

    def test_synthetic_zone_cannot_fall_back_to_utc(self):
        self.observed['Etc/Unknown']['at_zone_with_provider'] = self.observed['UTC']['at_zone_with_provider']
        self.reject()

    def test_unrelated_provider_error_cannot_pass(self):
        self.observed['Missing/Zone']['at_zone_with_provider']['error_message'] = 'no provider installed'
        self.reject()

    def test_constructor_evidence_cannot_be_repaired_into_validation(self):
        self.observed['utc']['constructor_with_provider'] = self.observed['utc']['at_zone_with_provider']
        self.reject()

    def test_json_evidence_cannot_be_repaired_into_strict_decoding(self):
        self.observed['Missing/Zone']['json_with_provider'] = self.observed['Missing/Zone']['at_zone_with_provider']
        self.reject()

    def test_exact_link_spelling_must_survive(self):
        self.observed['US/Eastern']['at_zone_with_provider']['value']['zone'] = 'America/New_York'
        self.reject()

    def test_aliases_are_distinct_values(self):
        self.observed['US/Eastern']['equal_to_new_york'] = True
        self.reject()

    def test_python_substitute_coverage_is_rejected(self):
        self.evidence['engines']['python']['observations']['UTC'] = self.observed['UTC']
        self.reject()

    def test_native_provenance_is_required(self):
        self.evidence['engines']['cpp']['identity']['loaded_hgraph_libraries']['libhgraph_runtime.so'] = 'f' * 64
        self.reject()


if __name__ == '__main__':
    unittest.main()
