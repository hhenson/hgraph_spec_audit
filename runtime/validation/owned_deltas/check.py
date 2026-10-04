"""Verify owned sparse delta evidence without erasing alias or sentinel differences."""
import hashlib
import json
from pathlib import Path
import sys
HERE=Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
from evidence_identity import digest, manifest

def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()

def main():
    corpus=json.loads((HERE/'reasoned.json').read_text());assert corpus['written_before_measurement']
    for name in ('observe','control','control_deepcopy'):
        filename='observed.json' if name=='observe' else name+'_observed.json'
        evidence=json.loads((HERE/filename).read_text())
        assert evidence['reasoned_sha256']==sha(HERE/'reasoned.json')
        assert evidence['harness_sha256']==sha(HERE/(name+'.py'))
        assert evidence['identity_helper_sha256']==sha(HERE.parent/'delta_eval/observe.py')
        assert evidence['repeats']==3 and set(evidence['engines'])=={'python','cpp'}
        for engine,result in evidence['engines'].items():
            assert result['identity']['native']==(engine=='cpp')
            expected=corpus['expected'];assert set(result['observations'])==set(expected)==set(result['assessment'])
            for case,want in expected.items():
                outcome=result['observations'][case]
                if 'error' in outcome:assessment='error'
                else:
                    assert outcome['unchanged']==(outcome['before_owner_cleanup']==outcome['after_owner_cleanup'])
                    assessment='match' if outcome['before_owner_cleanup']==want and outcome['after_owner_cleanup']==want else 'divergence'
                assert result['assessment'][case]==assessment
            print(name,engine,result['assessment'])
    native=json.loads((HERE/'native_observed.json').read_text())
    validate_native(native, corpus)
    print('Owned-delta evidence verified; no engines were executed.')

def validate_native(native, corpus):
    digest(native['binary_sha256'])
    manifest(native['sdk_headers_sha256'])
    assert native['status'] in {'error', 'observed'}
    assert native['reasoned_sha256']==sha(HERE/'reasoned.json') and native['recorder_sha256']==sha(HERE/'native_observe.py')
    assert native['repeats']==3
    if native['status']=='error':assert native['returncode']!=0 and native['stderr']
    else:
        assert native['source_sha256']==sha(HERE/'native.cpp')
        assert set(native['observed'])==set(corpus['native_expected'])==set(native['assessment'])
        for case,want in corpus['native_expected'].items():assert native['assessment'][case]==('match' if native['observed'][case]==want else 'divergence')
        authoring=json.loads((HERE/'observed.json').read_text())['engines']['cpp']['identity']['loaded_hgraph_libraries']
        for name in ('libhgraph_runtime.so','libhgraph_wiring.so','libhgraph_stdlib.so'):assert native['loaded_libraries_sha256'][name]==authoring[name]

if __name__=='__main__':main()
