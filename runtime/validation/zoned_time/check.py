"""Check the measured boundary; unavailable authoring types are not parity."""
import json
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / 'atomic_snapshots'))
from provenance import validate_identity
sys.path.insert(0, str(HERE.parent / 'delta_eval'))
from observe import sha


def validate(evidence):
    assert evidence['repeats'] == 3 and type(evidence['repeats']) is int
    assert evidence['reasoned_sha256'] == sha(HERE / 'reasoned.json')
    assert evidence['harness_sha256'] == sha(HERE / 'observe.py')
    assert evidence['identity_helper_sha256'] == sha(HERE.parent / 'delta_eval/observe.py')
    assert set(evidence['engines']) == {'python', 'cpp'}
    for engine, result in evidence['engines'].items():
        validate_identity(result['identity'], engine)
        assert result['graph_cases_executed'] is False
        missing = {'module_available': False}
        no_type = {'module_available': True, 'ZonedTime_exported': False}
        assert result['surfaces'] == {'hgraph': no_type,
                                     'hgraph.temporal': no_type if engine == 'cpp' else missing,
                                     '_hgraph': no_type if engine == 'cpp' else missing}


if __name__ == '__main__':
    validate(json.loads((HERE / 'observed.json').read_text()))
    print('ZonedTime unavailable on measured surfaces; no graph parity established.')
