"""Recorder conclusions require complete hook traces and consistent provenance."""
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

    def test_saved_evidence_passes(self):
        self.verify()

    def test_arbitrary_nonempty_package_hash_is_rejected(self):
        for value in ('not-a-digest', 'f' * 64):
            with self.subTest(value=value):
                self.evidence['engines']['python']['identity']['package']['identity_sha256'] = value
                with self.assertRaises(AssertionError):
                    self.verify()

    def test_altered_package_content_is_rejected(self):
        self.evidence['engines']['cpp']['identity']['package']['sources_sha256']['__init__.py'] = 'f' * 64
        with self.assertRaises(AssertionError):
            self.verify()

    def test_every_hook_is_required_including_dense_failure_cleanup(self):
        original = copy.deepcopy(self.evidence)
        for engine, result in original['engines'].items():
            for name, observed in result['observations'].items():
                for index, event in enumerate(observed['events']):
                    with self.subTest(engine=engine, case=name, missing=event['phase']):
                        self.evidence = copy.deepcopy(original)
                        del self.evidence['engines'][engine]['observations'][name]['events'][index]
                        with self.assertRaises(AssertionError):
                            self.verify()

    def test_reordered_or_duplicate_hooks_are_rejected(self):
        events = self.evidence['engines']['python']['observations']['sparse_eval_collision']['events']
        events[2], events[3] = events[3], events[2]
        with self.assertRaises(AssertionError):
            self.verify()
        events[2], events[3] = events[3], events[2]
        events.append(copy.deepcopy(events[-1]))
        with self.assertRaises(AssertionError):
            self.verify()

    def test_dense_failure_cannot_claim_second_input_was_processed(self):
        result = self.evidence['engines']['cpp']['observations']
        result['dense_eval_collision']['events'] = copy.deepcopy(result['sparse_eval_collision']['events'])
        with self.assertRaises(AssertionError):
            self.verify()


if __name__ == '__main__':
    unittest.main()
