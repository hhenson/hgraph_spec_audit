"""Expected failure needs evidence of the specified case, not an arbitrary exit."""
import unittest
from observe import expectations, matches, outcomes


def result(code, stdout='', timed_out=False):
    return dict(returncode=code, stdout=stdout, stderr='', timed_out=timed_out)


def mixed(runtime='passed', rejection='passed'):
    return dict(mode='test', expected_exit=int('failed' in (runtime, rejection)),
                runtime_results=[dict(name='sentinel', outcome=runtime)],
                rejection_results=[dict(identity='/spec/example.hgl:4', outcome=rejection)])


def output(runtime='ok', rejection='ok'):
    return (f'/spec/example.hgl:4 (invalid) ... {rejection} [rejection]\n'
            f'example::sentinel ... {runtime} [executed]\n')


class ExpectedFailureEvidence(unittest.TestCase):
    def test_mixed_success_requires_both_outcomes(self):
        case = mixed()
        self.assertTrue(matches(case, dict(run=result(0, output()))))
        for text in ('', 'sentinel ... ok [executed]', '/spec/example.hgl:4 ... ok [rejection]'):
            self.assertFalse(matches(case, dict(run=result(0, text))))

    def test_rejection_mismatch_still_requires_executed_sentinel(self):
        case = mixed(rejection='failed')
        self.assertTrue(matches(case, dict(run=result(1, output(rejection='FAILED')))))
        self.assertFalse(matches(case, dict(run=result(1, '/spec/example.hgl:4 ... FAILED [rejection]'))))

    def test_runtime_failure_remains_distinct(self):
        case = mixed(runtime='failed')
        self.assertTrue(matches(case, dict(run=result(1, output(runtime='FAILED')))))
        self.assertFalse(matches(case, dict(run=result(1, output(rejection='FAILED')))))

    def test_duplicate_and_wrong_kind_outcomes_fail(self):
        for text in (output() + 'sentinel ... ok [executed]\n',
                     output().replace('[executed]', '[rejection]'),
                     output().replace('[rejection]', '[executed]')):
            self.assertFalse(matches(mixed(), dict(run=result(0, text))))

    def test_admission_failure_has_no_case_execution(self):
        case = dict(mode='test', expected_exit=1)
        self.assertTrue(matches(case, dict(run=result(1, 'invalid annotation metadata'))))
        self.assertFalse(matches(case, dict(run=result(1, 'sentinel ... FAILED [executed]'))))

    def test_rejected_or_unselected_test_must_not_execute(self):
        case = dict(mixed(), not_executed=['invalid'])
        self.assertFalse(matches(case, dict(run=result(0, output() + 'invalid ... ok [executed]\n'))))
        self.assertTrue(matches(case, dict(run=result(0, output()))))

    def test_compile_and_build_failures_are_not_executed_controls(self):
        case = dict(mixed(runtime='failed'), preflight=True)
        self.assertFalse(matches(case, dict(source_check=result(1), run=result(1, output(runtime='FAILED')))))
        self.assertFalse(matches(case, dict(source_check=result(0), run=result(1, 'build failed'))))
        self.assertTrue(matches(case, dict(source_check=result(0), run=result(1, output(runtime='FAILED')))))

    def test_crashes_timeouts_and_wrong_exit_never_match(self):
        for code, timed_out in ((-11, False), (101, False), (None, True), (1, True), (0, False)):
            self.assertFalse(matches(mixed(runtime='failed'), dict(run=result(code, output(runtime='FAILED'), timed_out))))

    def test_quoted_diagnostic_text_is_not_an_outcome(self):
        for text in ('error: "sentinel ... ok [executed]"', '  sentinel ... ok [executed] (source text)',
                     'sentinel ... ok', '1 executed tests passed'):
            self.assertFalse(outcomes(text))

    def test_original_recorded_directory_resolves_declaration_identity(self):
        case = dict(rejection_results=[dict(file='../../language/a.hgl', owner_line=4, outcome='passed')])
        expected = expectations(case, '/original/spec/compiler/negative_testing')
        self.assertEqual(expected['rejection_results'][0]['identity'], '/original/spec/language/a.hgl:4')
        self.assertNotIn('identity', case['rejection_results'][0])


if __name__ == '__main__':
    unittest.main()
