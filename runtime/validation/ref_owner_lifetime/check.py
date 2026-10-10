"""Verify recorded REF ownership and scalar-capability evidence without runtimes."""
import hashlib
import json
from pathlib import Path
HERE=Path(__file__).resolve().parent

def sha(path): return hashlib.sha256(path.read_bytes()).hexdigest()

def check(public=None,native=None):
    public=public or json.loads((HERE/'observed.json').read_text())
    native=native or json.loads((HERE/'native_observed.json').read_text())
    reasoned=json.loads((HERE/'reasoned.json').read_text())
    native_reasoned=json.loads((HERE/'native_reasoned.json').read_text())
    for record,names in [(public,('observe.py','reasoned.json')),(native,('native.cpp','native_reasoned.json','native_observe.py','CMakeLists.txt'))]:
        assert record['repeats']==3
        assert record['sources_sha256']=={name:sha(HERE/name) for name in names}
    for engine,record in public['engines'].items():
        assert record['identity']['native']==(engine=='cpp')
        cases=record['cases']
        control=cases['outer_owner_control']
        assert [row['value'] for row in control['events']]==reasoned['outer_owner_control']['expected_followed']
        assert all(row['data_valid'] and row['data_modified'] for row in control['events'])
        scalar=cases['scalar_and_reference_identity']
        assert scalar['reference_identity']==native_reasoned['reference_identity']
        assert scalar['bool_operations']==native_reasoned['bool_operations']
        owned=cases['owned']
        if engine=='python':
            assert [row['value'] for row in owned['events']]==[7,8,8]
            assert owned['error_type']=='AttributeError'
            assert owned['message']=="'NoneType' object has no attribute 'graph'"
        else:
            assert [row['value'] for row in owned['events']]==[7,8,8,8,None,None]
    assert native['source_sha256']==native['sources_sha256']['native.cpp']
    assert native['sdk_files_sha256'] and len(native['binary_sha256'])==64 and len(native['compiler_sha256'])==64
    assert native['owned']==public['engines']['cpp']['cases']['owned']['events']
    assert native['outer_owner_control']==public['engines']['cpp']['cases']['outer_owner_control']['events']
    assert native['identity']==[native_reasoned['reference_identity']]
    assert native['bool_operations']==native_reasoned['bool_operations']
    assert native['assessment']=={'owned':'divergence','outer_owner_control':'match','reference_identity':'match','bool_operations':'match'}
    assert [row['value'] for row in native['owned']]!=native_reasoned['owned_followed']
    return True

if __name__=='__main__':
    check();print('Recorded reference ownership, identity and bool evidence verified')
