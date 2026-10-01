"""Verify preserved ordinary value-sequence evidence, including descriptive alias paths."""
import hashlib
import json
from pathlib import Path
HERE=Path(__file__).resolve().parent
PY_GROUPS={'ordinary_python','global_state_aliasing','timed_direct_list','timed_direct_tuple','timed_keyed_list','retained_record_snapshots'}
NATIVE_GROUPS={'immutable_mutation','native_borrowed_owner_after_mutation','native_existing_list_view_size','native_global_borrowed_mutation','native_global_get_owned_copy','native_global_owned_after_replace','native_global_replacement','native_global_separate_clone','native_global_set_copy','native_push_nested_copy','native_timed_direct_list','native_tuple_nested_copy','native_value_clone','native_value_copy'}

def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def digest(value):assert isinstance(value,str) and len(value)==64 and all(c in '0123456789abcdef' for c in value)
def manifest(value):
    assert isinstance(value,dict) and value
    for key,v in value.items():
        assert isinstance(key,str) and key and not key.startswith('/')
        digest(v)
def main():
    corpus=HERE/'reasoned.json';expected=json.loads(corpus.read_text())['expected']
    evidence=json.loads((HERE/'observed.json').read_text())
    assert evidence['reasoned_sha256']==sha(corpus)
    assert evidence['harness_sha256']==sha(HERE/'observe.py')
    assert evidence['identity_helper_sha256']==sha(HERE.parent/'delta_eval/observe.py')
    assert evidence['repeats']==3 and set(evidence['engines'])=={'python','cpp'}
    for name,result in evidence['engines'].items():
        identity=result['identity'];assert identity['native']==(name=='cpp')
        package=identity['package'];manifest(package['sources_sha256']);manifest(package['artifacts_sha256'])
        content={k:v for k,v in package.items() if k!='identity_sha256'}
        assert hashlib.sha256(json.dumps(content,sort_keys=True).encode()).hexdigest()==package['identity_sha256']
        assert set(result['observed'])==PY_GROUPS
        assert set(result['assessment'])=={'timed_direct_list','timed_direct_tuple','timed_keyed_list','retained_record_snapshots','python_explicit_deepcopy'}
        for key in ('timed_direct_list','timed_direct_tuple','timed_keyed_list','retained_record_snapshots'):
            observed=result['observed'][key]
            assert observed['status'] in ('observed','error')
            status='error' if observed['status']=='error' else 'match' if observed['value']==expected[key] else 'divergence'
            assert result['assessment'][key]==status
        assert result['assessment']['python_explicit_deepcopy']==('match' if result['observed']['ordinary_python']['deepcopy']==expected['python_explicit_deepcopy'] else 'divergence')
        alias=result['observed']['global_state_aliasing']
        assert alias['status']=='observed'
        assert set(alias['value'])=={'after_set','after_source_mutation','retrieval_type','retrieved_mutation','after_get_mutation','retained_deepcopy','retrieved_after_replacement','replacement'}
    native=json.loads((HERE/'native_observed.json').read_text())
    assert native['reasoned_sha256']==sha(corpus) and native['recorder_sha256']==sha(HERE/'native_observe.py')
    assert native['repeats']==3
    digest(native['binary_sha256']);manifest(native['sdk_headers_sha256'])
    if native['status']=='error':
        assert native['returncode']!=0 and native['stderr']
    else:
        assert native['status']=='observed' and native['source_sha256']==sha(HERE/'native.cpp')
        assert set(native['observed'])==NATIVE_GROUPS
        manifest(native['loaded_libraries_sha256'])
        for library in ('libhgraph_runtime.so','libhgraph_wiring.so','libhgraph_stdlib.so'):
            assert native['loaded_libraries_sha256'][library]==evidence['engines']['cpp']['identity']['loaded_hgraph_libraries'][library]
        selected={k:v for k,v in expected.items() if k.startswith('native_')};selected['native_timed_direct_list']=expected['timed_direct_list']
        assert set(native['assessment'])==set(selected)
        for key,value in selected.items():
            assert native['assessment'][key]==('match' if native['observed'][key]==value else 'divergence')
    print('Saved ordinary sequence/ownership evidence verified; alias descriptions are not normalized into copy claims.')
if __name__=='__main__':main()
