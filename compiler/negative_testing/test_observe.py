"""The audit must not turn an unrelated process failure into a passing control."""
import unittest
from observe import matches


def result(code, stdout='', timed_out=False):
    return dict(returncode=code, stdout=stdout, stderr='', timed_out=timed_out)


class ExpectedFailureEvidence(unittest.TestCase):
    def test_success_requires_an_executed_named_test(self):
        case = dict(mode='test', expected_exit=0)
        self.assertFalse(matches(case, dict(source_check=result(0), run=result(0))))
        self.assertTrue(matches(case, dict(source_check=result(0), run=result(0, 'sample ... ok'))))

    def test_executed_failing_control(self):
        case = dict(mode='test', expected_exit=1)
        self.assertTrue(matches(case, dict(source_check=result(0), run=result(1, 'sample ... FAILED: wrong error'))))

    def test_compile_or_build_failure_is_not_executed_control(self):
        case = dict(mode='test', expected_exit=1)
        self.assertFalse(matches(case, dict(source_check=result(1), run=result(1, 'sample ... FAILED'))))
        self.assertFalse(matches(case, dict(source_check=result(0), run=result(1, 'build failed'))))

    def test_crashes_and_timeouts_are_never_expected_failure(self):
        for mode in ('test', 'reject'):
            for code, timed_out in ((-11, False), (101, False), (None, True), (1, True)):
                row = dict(source_check=result(0), run=result(code, 'sample ... FAILED', timed_out))
                self.assertFalse(matches(dict(mode=mode, expected_exit=1), row))

    def test_wrong_exit_fails_each_fixture_kind(self):
        for mode in ('test', 'reject'):
            for expected in (0, 1):
                self.assertFalse(matches(dict(mode=mode, expected_exit=expected),
                                         dict(source_check=result(0), run=result(1 - expected))))


if __name__ == '__main__':
    unittest.main()
