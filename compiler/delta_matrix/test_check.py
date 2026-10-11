"""Corrupted matrix summaries must fail recorded-evidence validation."""
import copy
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import check

HERE = Path(__file__).resolve().parent


class MatrixEvidence(unittest.TestCase):
    def setUp(self):
        self.report = json.loads((HERE / 'results.json').read_text())
        self.expected = json.loads((HERE / 'expected.json').read_text())

    def reject(self, mutation, message):
        report = copy.deepcopy(self.report)
        mutation(report)
        with self.assertRaisesRegex(ValueError, message):
            check.validate(report, self.expected)

    def test_recorded_report(self):
        self.assertTrue(check.check())
        self.assertTrue(check.check(self.report))

    def test_source_hash_case_name_and_eval_counts_are_pinned(self):
        mutations = [
            lambda r: r['sources'][0].update(sha256='0' * 64),
            lambda r: r['sources'][-1]['tests'].__setitem__(0, 'invented_case'),
            lambda r: r['sources'][-1].update(eval_call_sites=99),
            lambda r: r['sources'].pop(),
        ]
        for index, mutation in enumerate(mutations):
            with self.subTest(index=index):
                self.reject(mutation, 'changed source')

    def test_aggregate_counts_must_follow_sources(self):
        for field in ('test_files', 'named_tests', 'eval_call_sites'):
            with self.subTest(field=field):
                self.reject(lambda r: r['shared_source_counts'].__setitem__(field, 1), 'inconsistent shared source counts')

    def test_every_measurement_has_exact_shared_case_names(self):
        for index in range(4):
            mutations = [
                lambda r: r['measurements'][index]['passed'].pop(),
                lambda r: r['measurements'][index]['passed'].append('invented_case'),
                lambda r: r['measurements'][index]['passed'].__setitem__(0, r['measurements'][index]['passed'][1]),
                lambda r: r['measurements'][index]['passed'].__setitem__(0, 'renamed_case'),
            ]
            for mutation in mutations:
                with self.subTest(index=index, mutation=mutation):
                    self.reject(mutation, 'passed tests')

    def test_failure_lists_are_checked_on_every_platform(self):
        for index in range(4):
            with self.subTest(index=index):
                self.reject(lambda r: r['measurements'][index]['failed'].append(r['measurements'][index]['passed'][0]), 'matrix failures')

    def test_missing_and_duplicate_measurement_rejected(self):
        self.reject(lambda r: r['measurements'].pop(), 'matrix measurement')
        self.reject(lambda r: r['measurements'].__setitem__(1, r['measurements'][0]), 'matrix measurement')

    def test_rust_suite_counts_and_failures_checked(self):
        for field in ('executed_tests', 'evaluations', 'failures'):
            with self.subTest(field=field):
                self.reject(lambda r: r['measurements'][3]['whole_suite'].__setitem__(field, 1), 'Rust whole-suite counts')

    def test_compiler_and_dependency_revisions_pinned(self):
        for field in self.report['revisions']:
            with self.subTest(field=field):
                self.reject(lambda r: r['revisions'].__setitem__(field, '0' * 40), 'revisions')
        self.reject(lambda r: r['measurements'][0].update(source_revision='0' * 40), 'measured compiler revision')

    def test_negative_case_id_count_and_match_checked(self):
        for index in range(2):
            with self.subTest(index=index):
                self.reject(lambda r: r['negative_measurements'][index]['cases'].pop(), 'negative case')
                self.reject(lambda r: r['negative_measurements'][index]['cases'][0].update(id='invented'), 'negative case identity')
                self.reject(lambda r: r['negative_measurements'][index]['cases'][0].update(matched=False), 'negative mismatch')
                self.reject(lambda r: r['negative_measurements'][index]['cases'][0].update(observed_exit=1), 'negative mismatch')

    def test_expected_failing_controls_cannot_be_relabeled_as_success(self):
        for backend_index, row in enumerate(self.report['negative_measurements']):
            for case_index, case in enumerate(row['cases']):
                if case['expected_exit']:
                    with self.subTest(backend_index=backend_index, case=case['id']):
                        self.reject(lambda r: r['negative_measurements'][backend_index]['cases'][case_index].update(expected_exit=0, observed_exit=0, matched=True), 'negative case identity')

    def test_negative_measurements_and_provenance_checked(self):
        self.reject(lambda r: r['negative_measurements'].pop(), 'negative measurement')
        self.reject(lambda r: r['negative_measurements'].__setitem__(1, r['negative_measurements'][0]), 'negative measurement')
        for field, value, message in [
            ('source_revision', '0' * 40, 'negative compiler revision'),
            ('source_revision_verified_by_runner', True, 'relabeled as verified'),
            ('manifest_sha256', '0' * 64, 'fixture manifest'),
            ('observer_sha256', '0' * 64, 'negative observer'),
        ]:
            with self.subTest(field=field):
                self.reject(lambda r: r['negative_measurements'][0].update({field: value}), message)

    def test_changed_valid_fingerprint_fails_report_integrity(self):
        for collection, field in [('measurements', 'binary_sha256'), ('measurements', 'raw_log_sha256'), ('negative_measurements', 'compiler_sha256'), ('negative_measurements', 'raw_report_sha256')]:
            with self.subTest(collection=collection, field=field):
                report = copy.deepcopy(self.report)
                report[collection][0][field] = '0' * 64
                check.validate(report, self.expected)
                with self.assertRaisesRegex(ValueError, 'frozen report content changed'):
                    check.check(report)

    def test_expected_manifest_cannot_be_replaced(self):
        with tempfile.TemporaryDirectory() as folder:
            target = Path(folder)
            (target / 'provenance.json').write_bytes((HERE / 'provenance.json').read_bytes())
            (target / 'expected.json').write_text('{}')
            with patch.object(check, 'HERE', target):
                with self.assertRaisesRegex(ValueError, 'manifest integrity changed'):
                    check.check(self.report)


if __name__ == '__main__':
    unittest.main()
