"""Check complete tuple/struct key identity and ordinary membership deltas."""
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
        cases = result['observations']
        assert set(cases) == {'tuple_set', 'tuple_map', 'struct_set', 'struct_map'}
        for shape in ('tuple', 'struct'):
            first = {'tuple': [1, 'a']} if shape == 'tuple' else {'type': 'Key', 'number': 1, 'label': 'a'}
            second = {'tuple': [2, 'b']} if shape == 'tuple' else {'type': 'Key', 'number': 2, 'label': 'b'}
            sets = [{'added': [first], 'removed': []}, {'added': [second], 'removed': []}, None,
                    {'added': [], 'removed': [first]}, {'added': [first], 'removed': []}]
            maps = [[{'key': first, 'value': 1}], [{'key': first, 'value': 1}, {'key': second, 'value': 2}], None,
                    [{'key': first, 'value': {'remove': True}}], [{'key': first, 'value': 3}]]
            for family, values in [('set', sets), ('map', maps)]:
                assert cases[shape+'_'+family] == {'raw': values, 'received': [v for v in values if v is not None],
                    'second_raw': values, 'first_after_second': values, 'empty': None, 'silent': None}, (engine,shape,family)


if __name__ == '__main__':
    validate(json.loads((HERE / 'observed.json').read_text()))
    print('Tuple/struct set and map key publications match on both recorded engines.')
