"""Corrupted reference records must fail rather than broaden scalar coverage."""
import copy
import json
import hashlib
from pathlib import Path
import unittest
from check import validate, validate_native


class ScalarEvidenceTests(unittest.TestCase):
    def setUp(self):
        self.data = json.loads((Path(__file__).parent/'observed.json').read_text())

    def test_recorded_evidence(self):
        validate(self.data)

    def test_native_record(self):
        validate_native(json.loads((Path(__file__).parent/'native_observed.json').read_text()))

    def test_native_corruption(self):
        original=json.loads((Path(__file__).parent/'native_observed.json').read_text())
        mutations=[
            lambda d:d['observed'].update(any_flattens=True),
            lambda d:d['observed'].update(any_missing_equality={'error':'expected error'}),
            lambda d:d['graphs']['any'].__setitem__(0,None),
            lambda d:d['graphs']['native'].__setitem__(1,None),
            lambda d:d['assessment'].update(any_missing_order='match'),
            lambda d:d['sdk_files_sha256'].pop('lib/libhgraph_runtime.a'),
            lambda d:d.update(target_name='another_probe'),
            lambda d:d.update(compile_command=['c++','-DFAKE=<sdk>/include']),
            lambda d:d.update(compile_command=['c++','-I<sdk>/include-other']),
            lambda d:d.update(loaded_libraries_sha256={'libhgraph_runtime.so':'0'*64}),
            lambda d:d.update(loaded_sdk_libraries_sha256={'../foreign/libhgraph_runtime.so':'0'*64}),
            lambda d:d.update(loaded_sdk_libraries_sha256={'lib/arbitrary.so':'0'*64}),
            lambda d:d.update(loaded_sdk_libraries_sha256={'lib/libhgraph_runtime.a':'0'*64}),
        ]
        for mutation in mutations:
            with self.subTest(mutation=mutation):
                data=copy.deepcopy(original);mutation(data)
                sealed={key:value for key,value in data.items() if key!='measurement_sha256'}
                data['measurement_sha256']=hashlib.sha256(json.dumps(sealed,sort_keys=True,separators=(',',':')).encode()).hexdigest()
                with self.assertRaises(AssertionError):validate_native(data)

    def test_native_provenance_cannot_change_without_run_digest(self):
        original=json.loads((Path(__file__).parent/'native_observed.json').read_text())
        for field in ('compiler_sha256','binary_sha256','compile_commands_sha256','target_manifest_sha256','cmake_cache_sha256','compiler_version','target_configuration','cmake_generator'):
            data=copy.deepcopy(original)
            data[field]='changed'
            with self.subTest(field=field), self.assertRaises(AssertionError):
                validate_native(data)

    def test_shared_target_manifest_requires_matching_loaded_artifacts(self):
        data=json.loads((Path(__file__).parent/'native_observed.json').read_text())
        runtime='lib/libhgraph_runtime.so'
        fingerprint=data['sdk_files_sha256']['lib/libhgraph_runtime.a']
        data['sdk_files_sha256'][runtime]=fingerprint
        data['sdk_target_libraries']=[runtime if p=='lib/libhgraph_runtime.a' else p for p in data['sdk_target_libraries']]
        data['loaded_sdk_libraries_sha256']={runtime:fingerprint}
        data['loaded_libraries_sha256']={'libhgraph_runtime.so':fingerprint}
        def reseal(record):
            sealed={key:value for key,value in record.items() if key!='measurement_sha256'}
            record['measurement_sha256']=hashlib.sha256(json.dumps(sealed,sort_keys=True,separators=(',',':')).encode()).hexdigest()
        reseal(data)
        # A metadata control, not a claim that the archived SDK was dynamic.
        validate_native(data)
        mutations=[lambda d:d.update(loaded_sdk_libraries_sha256={},loaded_libraries_sha256={}),
                   lambda d:d['loaded_sdk_libraries_sha256'].update({runtime:'0'*64}),
                   lambda d:d['loaded_libraries_sha256'].update({'libhgraph_runtime.so':'0'*64}),
                   lambda d:d['loaded_sdk_libraries_sha256'].update({'bin/libhgraph_runtime.so':fingerprint})]
        for mutation in mutations:
            corrupted=copy.deepcopy(data);mutation(corrupted);reseal(corrupted)
            with self.subTest(mutation=mutation),self.assertRaises(AssertionError):validate_native(corrupted)

    def test_corruption(self):
        mutations = [
            lambda d: d.update(reasoned_sha256='0'*64),
            lambda d: d['engines']['cpp']['cases']['bytes_equal_distinct']['dense'].__setitem__(0,None),
            lambda d: d['engines']['python']['cases']['bytes_all_silent'].update(raw=[]),
            lambda d: d['engines']['cpp']['cases']['bytes_silence']['received'].pop(),
            lambda d: d['engines']['cpp']['cases']['bad_256'].update(error_type='success'),
            lambda d: d['engines']['python']['cases']['object_bridge_mutable_retention']['captures_after_source_mutation'][0]['list'].pop(),
            lambda d: d['engines']['cpp']['cases'].pop('object_bridge_mixed'),
        ]
        for mutation in mutations:
            with self.subTest(mutation=mutation):
                data = copy.deepcopy(self.data)
                mutation(data)
                with self.assertRaises(AssertionError):
                    validate(data)


if __name__ == '__main__':
    unittest.main()
