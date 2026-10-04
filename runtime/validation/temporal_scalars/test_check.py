"""Evidence must not erase publications, zone identity, failures or ownership."""
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

    def test_equal_tick_cannot_be_deduplicated(self):
        self.observed['civil_datetime_equal_distinct']['raw'][1] = None
        self.reject()

    def test_silence_cannot_be_filled(self):
        row = self.observed['timezone_silence']
        row['raw'][2] = row['raw'][1]
        self.reject()

    def test_all_silent_raw_cannot_be_fabricated_dense(self):
        self.observed['timezone_all_silent']['raw'] = [None] * 3
        self.reject()

    def test_offset_must_be_exact(self):
        self.observed['same_instant_different_zone']['raw'][1]['offset_seconds'] = 0
        self.reject()

    def test_zone_alias_cannot_be_normalized(self):
        self.observed['zone_alias']['raw'][0]['timezone'] = 'America/New_York'
        self.reject()

    def test_same_instant_does_not_erase_value_identity(self):
        self.observed['same_instant_different_zone']['a_equals_b'] = True
        self.reject()

    def test_source_alias_is_rejected(self):
        row = self.observed['civil_datetime_retention']
        row['raw_after_source_mutation'] = row['inputs_second']
        self.reject()

    def test_other_capture_must_remain_independent(self):
        row = self.observed['timezone_retention']['first_after_capture_mutation']
        row[2] = row[0]
        self.reject()

    def test_second_run_must_remain_independent(self):
        row = self.observed['zoned_datetime_retention']
        row['second_after_capture_mutation'] = row['first_after_capture_mutation']
        self.reject()

    def test_provider_failure_cause_is_required(self):
        self.observed['provider']['events'][3]['error_message'] = 'unrelated error'
        self.reject()

    def test_provider_phase_order_is_required(self):
        self.observed['provider']['events'][6:8] = reversed(self.observed['provider']['events'][6:8])
        self.reject()

    def test_python_substitute_parity_is_rejected(self):
        self.evidence['engines']['python']['observations']['timezone_equal_distinct'] = self.observed['timezone_equal_distinct']
        self.reject()

    def test_unavailable_type_cannot_be_admitted(self):
        self.observed['availability']['exports']['ZonedTime'] = True
        self.reject()

    def test_provenance_must_be_consistent(self):
        self.evidence['engines']['cpp']['identity']['package']['identity_sha256'] = 'f' * 64
        self.reject()


if __name__ == '__main__':
    unittest.main()
