import copy
import hashlib
import json
from pathlib import Path
import unittest
from unittest.mock import patch
import check
HERE=Path(__file__).resolve().parent

class RecordedEvidence(unittest.TestCase):
    def setUp(self):
        self.public=json.loads((HERE/'observed.json').read_text())
        self.native=json.loads((HERE/'native_observed.json').read_text())
    def test_recorded(self): self.assertTrue(check.check(self.public,self.native))
    def test_default_records(self): self.assertTrue(check.check())
    def test_repeat_fingerprints_are_required(self):
        for engine in ('python','cpp'):
            public=copy.deepcopy(self.public)
            del public['engines'][engine]['runs_sha256']
            with self.subTest(engine=engine),self.assertRaises(KeyError): check.check(public,self.native)
        del self.native['runs_sha256']
        self.reseal(self.native)
        with self.assertRaises(KeyError): check.check(self.public,self.native)
    def test_repeat_count_must_be_exact_integer_three(self):
        for value in (1,2,4,3.0,'3',True,None):
            public=copy.deepcopy(self.public)
            public['repeats']=value
            with self.subTest(surface='public',value=value),self.assertRaises(AssertionError): check.check(public,self.native)
            native=copy.deepcopy(self.native)
            native['repeats']=value
            self.reseal(native)
            with self.subTest(surface='native',value=value),self.assertRaises(AssertionError): check.check(self.public,native)
    def test_exactly_three_ordered_public_repeat_fingerprints(self):
        for engine in ('python','cpp'):
            correct=self.public['engines'][engine]['runs_sha256'][0]
            for value in ([],[correct],[correct]*2,[correct]*4,None,correct,{},['z'*64]*3):
                public=copy.deepcopy(self.public)
                public['engines'][engine]['runs_sha256']=value
                with self.subTest(engine=engine,value=value),self.assertRaises(AssertionError): check.check(public,self.native)
            for index in range(3):
                public=copy.deepcopy(self.public)
                public['engines'][engine]['runs_sha256'][index]='0'*64
                with self.subTest(engine=engine,index=index),self.assertRaises(AssertionError): check.check(public,self.native)
    def test_exactly_three_ordered_native_repeat_fingerprints_even_when_resealed(self):
        correct=self.native['runs_sha256'][0]
        for value in ([],[correct],[correct]*2,[correct]*4,None,correct,{},['z'*64]*3):
            native=copy.deepcopy(self.native)
            native['runs_sha256']=value
            self.reseal(native)
            with self.subTest(value=value),self.assertRaises(AssertionError): check.check(self.public,native)
        for index in range(3):
            native=copy.deepcopy(self.native)
            native['runs_sha256'][index]='0'*64
            self.reseal(native)
            with self.subTest(index=index),self.assertRaises(AssertionError): check.check(self.public,native)
    def test_public_repeat_digest_covers_identity_and_all_case_payloads(self):
        for engine in ('python','cpp'):
            record=self.public['engines'][engine]
            payloads=[record['identity'],record['cases'],{'identity':record['identity'],'cases':{'owned':record['cases']['owned']}}]
            for payload in payloads:
                public=copy.deepcopy(self.public)
                public['engines'][engine]['runs_sha256']=[check.capture_digest(payload)]*3
                with self.subTest(engine=engine,payload=payload.keys()),self.assertRaises(AssertionError): check.check(public,self.native)
    def test_native_repeat_digest_covers_all_captured_fields(self):
        payload={field:self.native[field] for field in check.NATIVE_CAPTURE_FIELDS}
        for field in check.NATIVE_CAPTURE_FIELDS:
            incomplete={key:value for key,value in payload.items() if key!=field}
            native=copy.deepcopy(self.native)
            native['runs_sha256']=[check.capture_digest(incomplete)]*3
            self.reseal(native)
            with self.subTest(field=field),self.assertRaises(AssertionError): check.check(self.public,native)
    def test_owned_assessments_derive_from_requirement_without_padding_python_error(self):
        reasoned,native_reasoned=check.load_requirements()
        check.check_requirements(reasoned,native_reasoned)
        self.assertEqual(check.assess_owned(self.public['engines']['python']['cases']['owned'],reasoned['expected_followed']),'error')
        self.assertEqual(check.assess_owned(self.public['engines']['cpp']['cases']['owned'],reasoned['expected_followed']),'divergence')
        self.assertEqual(check.assess_native(self.native,reasoned,native_reasoned),self.native['assessment'])
        self.assertEqual(len(self.public['engines']['python']['cases']['owned']['events']),3)
    def test_changed_owned_requirement_rejected_after_coordinated_recapture(self):
        original_sha=check.sha
        for expected in ([7,8,8,8,None,None],[7,8,8],[7,8,None,None,None,None],[7,8,8,8,8,None]):
            for update_native in (False,True):
                with self.subTest(expected=expected,update_native=update_native):
                    reasoned,native_reasoned=check.load_requirements()
                    public=copy.deepcopy(self.public)
                    native=copy.deepcopy(self.native)
                    reasoned['expected_followed']=expected
                    changed={'reasoned.json':hashlib.sha256(json.dumps(reasoned).encode()).hexdigest()}
                    public['sources_sha256']['reasoned.json']=changed['reasoned.json']
                    if update_native:
                        native_reasoned['owned_followed']=expected
                        changed['native_reasoned.json']=hashlib.sha256(json.dumps(native_reasoned).encode()).hexdigest()
                        native['sources_sha256']['native_reasoned.json']=changed['native_reasoned.json']
                        native['assessment']['owned']='match' if [row['value'] for row in native['owned']]==expected else 'divergence'
                    self.reseal(native)
                    with patch.object(check,'load_requirements',return_value=(reasoned,native_reasoned)),patch.object(check,'sha',side_effect=lambda path:changed[path.name] if path.name in changed else original_sha(path)):
                        with self.assertRaises(AssertionError): check.check(public,native)
    def test_divergence_assessment_cannot_be_relabeled_after_resealing(self):
        self.native['assessment']['owned']='match'
        self.reseal(self.native)
        with self.assertRaises(AssertionError): check.check(self.public,self.native)
    def test_cpp_and_native_observations_cannot_be_repaired_into_a_requirement_match(self):
        owned=self.public['engines']['cpp']['cases']['owned']
        owned['events'][3]['value']=None
        owned['events'][3]['data_valid']=False
        owned['raw']=[json.dumps(row,sort_keys=True) for row in owned['events']]
        self.native['owned']=copy.deepcopy(owned['events'])
        self.native['assessment']['owned']='match'
        self.reseal(self.native)
        reasoned,_=check.load_requirements()
        self.assertEqual(check.assess_owned(owned,reasoned['expected_followed']),'match')
        with self.assertRaises(AssertionError): check.check(self.public,self.native)
    def test_empty_public_record_is_not_replaced(self):
        with self.assertRaises(KeyError): check.check({},self.native)
    def test_empty_native_record_is_not_replaced(self):
        with self.assertRaises(KeyError): check.check(self.public,{})
    def test_missing_engine_rejected(self):
        for engine in ('python','cpp'):
            with self.subTest(engine=engine):
                public=copy.deepcopy(self.public)
                del public['engines'][engine]
                with self.assertRaises(AssertionError): check.check(public,self.native)
    def test_empty_engines_rejected(self):
        self.public['engines']={}
        with self.assertRaises(AssertionError): check.check(self.public,self.native)
    def test_extra_engine_rejected(self):
        self.public['engines']['unsupported']=copy.deepcopy(self.public['engines']['python'])
        with self.assertRaises(AssertionError): check.check(self.public,self.native)
    def test_public_owned_flags_cannot_change(self):
        for engine,record in self.public['engines'].items():
            for index,event in enumerate(record['cases']['owned']['events']):
                for field in ('reference_valid','data_valid','reference_modified','data_modified'):
                    with self.subTest(engine=engine,index=index,field=field):
                        public=copy.deepcopy(self.public)
                        public['engines'][engine]['cases']['owned']['events'][index][field]=not event[field]
                        with self.assertRaises(AssertionError): check.check(public,self.native)
    def test_native_owned_flags_cannot_change(self):
        for index,event in enumerate(self.native['owned']):
            for field in ('reference_valid','data_valid','reference_modified','data_modified'):
                with self.subTest(index=index,field=field):
                    native=copy.deepcopy(self.native)
                    native['owned'][index][field]=not event[field]
                    with self.assertRaises(AssertionError): check.check(self.public,native)
    def test_matching_cpp_and_native_owned_flag_corruption_rejected(self):
        for index,event in enumerate(self.native['owned']):
            for field in ('reference_valid','data_valid','reference_modified','data_modified'):
                with self.subTest(index=index,field=field):
                    public=copy.deepcopy(self.public)
                    native=copy.deepcopy(self.native)
                    public['engines']['cpp']['cases']['owned']['events'][index][field]=not event[field]
                    native['owned'][index][field]=not event[field]
                    with self.assertRaises(AssertionError): check.check(public,native)
    def test_owned_flags_must_be_booleans(self):
        for field in ('reference_valid','data_valid','reference_modified','data_modified'):
            with self.subTest(field=field):
                public=copy.deepcopy(self.public)
                native=copy.deepcopy(self.native)
                public['engines']['cpp']['cases']['owned']['events'][0][field]=1
                native['owned'][0][field]=1
                with self.assertRaises(AssertionError): check.check(public,native)
    def test_outer_owner_control_flags_cannot_change(self):
        for engine,record in self.public['engines'].items():
            for index,event in enumerate(record['cases']['outer_owner_control']['events']):
                for field in ('reference_valid','data_valid','reference_modified','data_modified'):
                    with self.subTest(engine=engine,index=index,field=field):
                        public=copy.deepcopy(self.public)
                        native=copy.deepcopy(self.native)
                        public['engines'][engine]['cases']['outer_owner_control']['events'][index][field]=not event[field]
                        if engine=='cpp':
                            native['outer_owner_control'][index][field]=not event[field]
                        with self.assertRaises(AssertionError): check.check(public,native)
    def test_stale_capture_cannot_be_reported_as_expired(self):
        self.native['owned'][3]['value']=None
        with self.assertRaises(AssertionError): check.check(self.public,self.native)
    def test_live_outer_owner_cannot_be_expired(self):
        self.public['engines']['python']['cases']['outer_owner_control']['events'][3]['value']=None
        with self.assertRaises(AssertionError): check.check(self.public,self.native)
    def test_identity_cannot_be_payload_equality(self):
        self.native['identity'][0]['distinct_equal_endpoints']=True
        with self.assertRaises(AssertionError): check.check(self.public,self.native)
    def test_false_bool_order_cannot_pass(self):
        self.native['bool_operations']['false_before_true']=False
        with self.assertRaises(AssertionError): check.check(self.public,self.native)
    def test_source_fingerprint_required(self):
        self.native['sources_sha256']['native.cpp']='0'*64
        with self.assertRaises(AssertionError): check.check(self.public,self.native)
    def test_public_support_manifest_required(self):
        del self.public['support_sha256']
        with self.assertRaises(KeyError): check.check(self.public,self.native)
    def test_public_support_manifest_must_be_a_dictionary(self):
        for value in (None,[],list(check.SUPPORT_NAMES),'support',False):
            public=copy.deepcopy(self.public)
            public['support_sha256']=value
            with self.subTest(value=value),self.assertRaises(AssertionError):
                check.check(public,self.native)
    def test_public_support_manifest_exact_dependencies(self):
        mutations=[lambda manifest:manifest.clear(),
                   lambda manifest:manifest.update({'arbitrary.py':'0'*64}),
                   lambda manifest:manifest.update({'../fixed/native_identity.py':'0'*64})]
        for name in check.SUPPORT_NAMES:
            mutations.extend([lambda manifest,name=name:manifest.pop(name),
                              lambda manifest,name=name:manifest.update({name:'0'*64})])
        for mutation in mutations:
            public=copy.deepcopy(self.public)
            mutation(public['support_sha256'])
            with self.subTest(mutation=mutation),self.assertRaises(AssertionError):
                check.check(public,self.native)
    def test_public_support_manifest_hex_digests(self):
        for name in check.SUPPORT_NAMES:
            for value in ('z'*64,'0'*63,0,None):
                public=copy.deepcopy(self.public)
                public['support_sha256'][name]=value
                with self.subTest(name=name,value=value),self.assertRaises(AssertionError):
                    check.check(public,self.native)
    def test_missing_and_corrupt_engine_fingerprints(self):
        for engine in ('python','cpp'):
            for field in ('package','eval_node_source_sha256','native_artifacts','loaded_hgraph_libraries'):
                with self.subTest(engine=engine,field=field):
                    public=copy.deepcopy(self.public)
                    del public['engines'][engine]['identity'][field]
                    with self.assertRaises((AssertionError,KeyError)): check.check(public,self.native)
            public=copy.deepcopy(self.public)
            public['engines'][engine]['identity']['eval_node_source_sha256']='z'*64
            with self.assertRaises(AssertionError): check.check(public,self.native)
    def test_package_digest_and_native_manifest_corruption(self):
        for engine in ('python','cpp'):
            public=copy.deepcopy(self.public)
            public['engines'][engine]['identity']['package']['identity_sha256']='0'*64
            with self.subTest(engine=engine),self.assertRaises(AssertionError): check.check(public,self.native)
        public=copy.deepcopy(self.public)
        public['engines']['cpp']['identity']['native_artifacts']={}
        with self.assertRaises(AssertionError): check.check(public,self.native)
        public=copy.deepcopy(self.public)
        public['engines']['cpp']['identity']['loaded_hgraph_libraries']={}
        with self.assertRaises(AssertionError): check.check(public,self.native)
    def test_publication_rows_must_match_events(self):
        for engine,record in self.public['engines'].items():
            for case,values in record['cases'].items():
                if 'raw' not in values: continue
                mutations=[lambda raw:raw.pop(),lambda raw:raw.append(raw[-1]),
                           lambda raw:raw.__setitem__(0,'{}'),lambda raw:raw.__setitem__(0,None),
                           lambda raw:raw.__setitem__(0,raw[0].replace('true','1'))]
                for mutation in mutations:
                    with self.subTest(engine=engine,case=case,mutation=mutation):
                        public=copy.deepcopy(self.public)
                        mutation(public['engines'][engine]['cases'][case]['raw'])
                        with self.assertRaises(AssertionError): check.check(public,self.native)
                public=copy.deepcopy(self.public)
                del public['engines'][engine]['cases'][case]['raw']
                record=public['engines'][engine]
                record['runs_sha256']=[check.capture_digest({'identity':record['identity'],'cases':record['cases']})]*3
                with self.assertRaises(KeyError): check.check(public,self.native)
    def test_failed_python_capture_cannot_claim_successful_raw(self):
        self.public['engines']['python']['cases']['owned']['raw']=[]
        with self.assertRaises(AssertionError): check.check(self.public,self.native)
    def test_native_provenance_is_sealed(self):
        for field in ('binary_sha256','compiler_sha256','compiler_version','compile_command',
                      'target_configuration','sdk_target_libraries','cmake_generator'):
            native=copy.deepcopy(self.native)
            native[field]='changed'
            with self.subTest(field=field),self.assertRaises(AssertionError): check.check(self.public,native)
    def reseal(self,native):
        content={k:v for k,v in native.items() if k!='measurement_sha256'}
        native['measurement_sha256']=hashlib.sha256(json.dumps(content,sort_keys=True,separators=(',',':')).encode()).hexdigest()
    def test_nonhex_native_fingerprints_rejected_even_when_resealed(self):
        for field in ('binary_sha256','compiler_sha256','compile_commands_sha256','target_manifest_sha256','cmake_cache_sha256'):
            native=copy.deepcopy(self.native)
            native[field]='z'*64
            self.reseal(native)
            with self.subTest(field=field),self.assertRaises(AssertionError): check.check(self.public,native)
        native=copy.deepcopy(self.native)
        native['sdk_files_sha256']['lib/libhgraph_runtime.a']='z'*64
        self.reseal(native)
        with self.assertRaises(AssertionError): check.check(self.public,native)
    def test_native_sdk_and_build_metadata_required_even_when_resealed(self):
        mutations=[lambda n:n.update(sdk_files_sha256={'arbitrary':'0'*64}),
                   lambda n:n['sdk_files_sha256'].pop('include/hgraph/types/static_node.h'),
                   lambda n:n['sdk_files_sha256'].pop('lib/libhgraph_runtime.a'),
                   lambda n:n.update(compiler_version=''),lambda n:n.update(cmake_generator=''),
                   lambda n:n.update(target_name='another_target'),lambda n:n.update(target_artifact='../ref_owner_lifetime_native'),
                   lambda n:n.update(sdk_target_libraries=['lib/arbitrary.a']*3),
                   lambda n:n.update(target_configuration='Different')]
        for mutation in mutations:
            native=copy.deepcopy(self.native)
            mutation(native)
            # A nonempty single-generator configuration cannot be inferred
            # from its flags; force an explicit contradictory clue for this control.
            if native['target_configuration']=='Different':
                native['compile_command'].append('-DCMAKE_INTDIR="Release"')
            self.reseal(native)
            with self.subTest(mutation=mutation),self.assertRaises(AssertionError): check.check(self.public,native)
        for field in ('compile_command','target_configuration','cmake_cache_sha256'):
            native=copy.deepcopy(self.native)
            del native[field]
            self.reseal(native)
            with self.subTest(field=field),self.assertRaises(KeyError): check.check(self.public,native)

if __name__=='__main__': unittest.main()
