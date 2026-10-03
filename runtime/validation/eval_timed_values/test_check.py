"""Tampered successes and incomplete provenance must not verify."""
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

    def test_consistently_labelled_error_is_rejected(self):
        result = self.evidence['engines']['python']
        name = self.reasoned['cases'][0]['id']
        result['observations'][name] = {'error': 'unrelated failure', 'error_type': 'RuntimeError'}
        result['assessment'][name] = 'error'
        with self.assertRaises(AssertionError):
            self.verify()

    def test_consistently_labelled_divergence_is_rejected(self):
        result = self.evidence['engines']['python']
        case = next(case for case in self.reasoned['cases'] if case['id'] == 'i64_silence')
        observed = result['observations'][case['id']]
        observed['raw_eval_result'][0] = 999
        observed['dense_from_external_horizon'][0] = 999
        result['assessment'][case['id']] = 'divergence'
        with self.assertRaises(AssertionError):
            self.verify()

    def test_bool_is_not_an_integer_payload(self):
        observed = self.evidence['engines']['python']['observations']['bool_silence']
        for field in ('raw_eval_result', 'dense_from_external_horizon'):
            observed[field] = [int(value) if type(value) is bool else value for value in observed[field]]
        with self.assertRaises(AssertionError):
            self.verify()

    def test_bad_provenance_is_rejected(self):
        original = copy.deepcopy(self.evidence)
        mutations = [
            lambda x: x.update(native=1),
            lambda x: x.update(python=''),
            lambda x: x.update(hgraph='changed'),
            lambda x: x.update(eval_node_source_sha256='f' * 64),
            lambda x: x['package'].update(identity_sha256='f' * 64),
            lambda x: x['package'].update(sources_sha256={}),
            lambda x: x['package'].update(artifacts_sha256={}),
            lambda x: x['native_artifacts'].clear(),
            lambda x: x['native_artifacts'].update({'lib/libhgraph_runtime.so': 'f' * 64}),
            lambda x: x['loaded_hgraph_libraries'].clear(),
            lambda x: x['loaded_hgraph_libraries'].pop('libhgraph_runtime.so'),
            lambda x: x['loaded_hgraph_libraries'].update({'libhgraph_runtime.so': 'f' * 64}),
            lambda x: x['loaded_hgraph_libraries'].update({'libhgraph_runtime.so': 'not-a-digest'}),
        ]
        for index, mutation in enumerate(mutations):
            with self.subTest(mutation=index):
                self.evidence = copy.deepcopy(original)
                mutation(self.evidence['engines']['cpp']['identity'])
                with self.assertRaises(AssertionError):
                    self.verify()

    def test_python_cannot_claim_native_artifacts(self):
        self.evidence['engines']['python']['identity']['native_artifacts'] = {'x.so': 'f' * 64}
        with self.assertRaises(AssertionError):
            self.verify()


if __name__ == '__main__':
    unittest.main()
