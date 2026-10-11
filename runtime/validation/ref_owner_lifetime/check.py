"""Verify recorded REF ownership and scalar-capability evidence without runtimes."""
import hashlib
import json
import sys
from pathlib import Path
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent))
from evidence_identity import digest, manifest, validate_identity
from build_identity import command_configuration, include_paths

def sha(path): return hashlib.sha256(path.read_bytes()).hexdigest()

def check_flags(events, expected):
    fields=('reference_valid','data_valid','reference_modified','data_modified')
    assert len(events)==len(expected)
    for event,flags in zip(events,expected):
        assert all(event[field] is flag for field,flag in zip(fields,flags))

def check_publications(case):
    assert isinstance(case['raw'],list) and all(isinstance(row,str) for row in case['raw'])
    published=[json.loads(row) for row in case['raw']]
    assert json.dumps(published,sort_keys=True)==json.dumps(case['events'],sort_keys=True)

def check_native_provenance(native):
    sealed={key:value for key,value in native.items() if key!='measurement_sha256'}
    digest(native['measurement_sha256'])
    assert native['measurement_sha256']==hashlib.sha256(json.dumps(sealed,sort_keys=True,separators=(',',':')).encode()).hexdigest()
    for field in ('binary_sha256','compiler_sha256','compile_commands_sha256','target_manifest_sha256','cmake_cache_sha256'):
        digest(native[field])
    manifest(native['sdk_files_sha256'])
    assert isinstance(native['loaded_libraries_sha256'],dict)
    for name,value in native['loaded_libraries_sha256'].items():
        assert isinstance(name,str) and name and '/' not in name
        digest(value)
    required={'include/hgraph/types/static_node.h','include/hgraph/lib/testing/eval_node.h',
              'include/hgraph/lib/std/std_operators.h','include/hgraph/lib/std/std_nodes.h',
              'lib/cmake/hgraph/hgraphConfig.cmake',
              'lib/libhgraph_stdlib.a','lib/libhgraph_wiring.a','lib/libhgraph_runtime.a'}
    assert required<=set(native['sdk_files_sha256'])
    assert native['support_sha256']=={'fixed/native_loaded_libraries.h':sha(HERE.parent/'fixed/native_loaded_libraries.h')}
    assert native['target_name']=='ref_owner_lifetime_native'
    artifact=Path(native['target_artifact'])
    assert not artifact.is_absolute() and '..' not in artifact.parts
    assert artifact.name in {'ref_owner_lifetime_native','ref_owner_lifetime_native.exe'}
    for field in ('compiler_version','cmake_generator'):
        assert isinstance(native[field],str) and native[field].strip()
    config=native['target_configuration']
    assert isinstance(config,str)
    libraries=native['sdk_target_libraries']
    assert libraries==['lib/libhgraph_stdlib.a','lib/libhgraph_wiring.a','lib/libhgraph_runtime.a']
    command=native['compile_command']
    assert isinstance(command,list) and command and all(isinstance(arg,str) and arg for arg in command)
    assert '<sdk>/include' in include_paths(command)
    assert '-c' in command and command[command.index('-c')+1]=='<source>/native.cpp'
    selected=command_configuration({},command)
    assert selected is None or selected==config
    if native['cmake_generator']=='Ninja Multi-Config':
        assert config and selected==config and artifact.parts[0]==config

def check(public=None,native=None):
    if public is None:
        public=json.loads((HERE/'observed.json').read_text())
    if native is None:
        native=json.loads((HERE/'native_observed.json').read_text())
    reasoned=json.loads((HERE/'reasoned.json').read_text())
    native_reasoned=json.loads((HERE/'native_reasoned.json').read_text())
    for record,names in [(public,('observe.py','reasoned.json')),(native,('native.cpp','native_reasoned.json','native_observe.py','CMakeLists.txt','build_identity.py'))]:
        assert record['repeats']==3
        assert record['sources_sha256']=={name:sha(HERE/name) for name in names}
    assert set(public['engines'])=={'python','cpp'}
    for engine,record in public['engines'].items():
        validate_identity(record['identity'],engine)
        cases=record['cases']
        assert set(cases)=={'owned','outer_owner_control','scalar_and_reference_identity'}
        control=cases['outer_owner_control']
        assert [row['value'] for row in control['events']]==reasoned['outer_owner_control']['expected_followed']
        check_flags(control['events'],[(True,True,True,True)]+[(True,True,False,True)]*5)
        check_publications(control)
        scalar=cases['scalar_and_reference_identity']
        assert scalar['reference_identity']==native_reasoned['reference_identity']
        assert scalar['bool_operations']==native_reasoned['bool_operations']
        owned=cases['owned']
        # Preserve measured flags, including the C++ target's late invalidation;
        # these are evidence checks, not the reasoned owner-expiry requirement.
        owned_flags=[(True,True,True,True),(True,True,False,True),(True,True,False,False)]
        if engine=='python':
            assert [row['value'] for row in owned['events']]==[7,8,8]
            assert owned['error_type']=='AttributeError'
            assert owned['message']=="'NoneType' object has no attribute 'graph'"
            assert 'raw' not in owned
        else:
            assert [row['value'] for row in owned['events']]==[7,8,8,8,None,None]
            owned_flags += [(True,True,False,False)]+[(True,False,False,False)]*2
            check_publications(owned)
        check_flags(owned['events'],owned_flags)
    assert native['source_sha256']==native['sources_sha256']['native.cpp']
    check_native_provenance(native)
    assert native['owned']==public['engines']['cpp']['cases']['owned']['events']
    assert native['outer_owner_control']==public['engines']['cpp']['cases']['outer_owner_control']['events']
    assert native['identity']==[native_reasoned['reference_identity']]
    assert native['bool_operations']==native_reasoned['bool_operations']
    assert native['assessment']=={'owned':'divergence','outer_owner_control':'match','reference_identity':'match','bool_operations':'match'}
    assert [row['value'] for row in native['owned']]!=native_reasoned['owned_followed']
    return True

if __name__=='__main__':
    check();print('Recorded reference ownership, identity and bool evidence verified')
