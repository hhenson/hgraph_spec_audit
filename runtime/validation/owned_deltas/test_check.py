"""Native evidence must identify its executable and the installed SDK headers."""
import json
from pathlib import Path
import unittest
import check

HERE = Path(__file__).resolve().parent


class NativeProvenanceTests(unittest.TestCase):
    def setUp(self):
        self.corpus = json.loads((HERE / 'reasoned.json').read_text())
        self.native = json.loads((HERE / 'native_observed.json').read_text())

    def test_saved_native_evidence_passes(self):
        check.validate_native(self.native, self.corpus)

    def test_missing_or_malformed_binary_digest_is_rejected(self):
        for value in (None, '', 'arbitrary', 'z' * 64, '1' * 63):
            with self.subTest(value=value):
                self.native['binary_sha256'] = value
                with self.assertRaises(AssertionError):
                    check.validate_native(self.native, self.corpus)
        del self.native['binary_sha256']
        with self.assertRaises(KeyError):
            check.validate_native(self.native, self.corpus)

    def test_missing_empty_or_malformed_sdk_manifest_is_rejected(self):
        for value in (None, {}, {'': '1' * 64}, {'/private/header.h': '1' * 64}, {'header.h': 'arbitrary'}):
            with self.subTest(value=value):
                self.native['sdk_headers_sha256'] = value
                with self.assertRaises(AssertionError):
                    check.validate_native(self.native, self.corpus)
        del self.native['sdk_headers_sha256']
        with self.assertRaises(KeyError):
            check.validate_native(self.native, self.corpus)

    def test_failed_measurement_still_requires_provenance(self):
        self.native.update(status='error', returncode=1, stderr='actual failure', sdk_headers_sha256={})
        with self.assertRaises(AssertionError):
            check.validate_native(self.native, self.corpus)


if __name__ == '__main__':
    unittest.main()
