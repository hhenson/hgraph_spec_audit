"""Verify complete snapshot observations and preserve historical aliasing differences."""
import copy
import hashlib
import json
from pathlib import Path
from provenance import validate_identity

HERE = Path(__file__).resolve().parent


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def same(actual, expected):
    assert json.dumps(actual, sort_keys=True) == json.dumps(expected, sort_keys=True), (actual, expected)


def expected_inputs():
    scalars = [False, 0, 0.0, '', {'date': '2026-01-02'}, {'time': '03:04:05'},
               {'datetime': '2026-01-02T03:04:05'}, {'duration_us': -3}]
    return {
        'tuple_eight_scalars': [scalars, None, scalars],
        'tuple_nested_list': [[[1, 2], 4], None, [[3], 5]],
        'list_i64': [[1, 2], None, [3], [], []],
        'list_nested': [[[1], [2]], None, [[3]], [], []],
        'list_shared_captures': [[1, 2], None, [1, 2]],
        'required_nominal': [{'count': 1, 'values': [10, 11]}, None, {'count': 2, 'values': [20]}],
        'defaulted_nominal': [{'bid': 1, 'ask': 7}, None, {'bid': 2, 'ask': 9}, {'bid': 2, 'ask': 9}],
        'list_nominal': [[{'bid': 1, 'ask': 7}, {'bid': 2, 'ask': 7}], None, [{'bid': 3, 'ask': 8}], []],
    }


def changed(name, snapshots, marker, shared=False):
    values = copy.deepcopy(snapshots)
    for index in ([0, 2] if shared else [0]):
        value = values[index]
        if name in {'tuple_nested_list', 'list_nested'}:
            value[0].append(marker)
        elif name == 'required_nominal':
            value['values'].append(marker)
        elif name == 'list_nominal':
            value.append({'bid': marker, 'ask': 7})
        elif name in {'list_i64', 'list_shared_captures'}:
            value.append(marker)
    return values


def validate(reasoned, evidence):
    assert reasoned['written_before_measurement'] is True
    assert evidence['reasoned_sha256'] == sha(HERE / 'reasoned.json')
    assert evidence['harness_sha256'] == sha(HERE / 'observe.py')
    assert evidence['identity_helper_sha256'] == sha(HERE.parent / 'delta_eval/observe.py')
    assert evidence['repeats'] == 3
    inputs = expected_inputs()
    assert set(reasoned['cases']) == set(inputs) and len(reasoned['cases']) == 8
    assert set(evidence['engines']) == {'python', 'cpp'}
    for engine, result in evidence['engines'].items():
        validate_identity(result['identity'], engine)
        assert set(result['observations']) == set(inputs)
        for name, original in inputs.items():
            observed = result['observations'][name]
            assert set(observed) == {'inputs_before', 'inputs_after_mutation', 'raw_after_eval', 'received',
                    'source_mutated', 'capture_mutated', 'raw_after_source_mutation', 'raw_after_second_eval',
                    'second_raw', 'raw_after_capture_mutation', 'second_raw_after_capture_mutation'}
            mutable = name not in {'tuple_eight_scalars', 'defaulted_nominal'}
            assert observed['source_mutated'] is mutable and observed['capture_mutated'] is mutable
            same(observed['inputs_before'], original)
            same(observed['raw_after_eval'], original)
            same(observed['received'], [{'value': v, 'delta': v} for v in original if v is not None])
            altered_inputs = changed(name, original, 999, shared=name == 'list_shared_captures')
            same(observed['inputs_after_mutation'], altered_inputs)
            retained = original if engine == 'cpp' else altered_inputs
            same(observed['raw_after_source_mutation'], retained)
            same(observed['raw_after_second_eval'], retained)
            same(observed['second_raw'], altered_inputs)
            altered_capture = changed(name, retained, 888,
                                      shared=engine == 'python' and name == 'list_shared_captures')
            same(observed['raw_after_capture_mutation'], altered_capture)
            same(observed['second_raw_after_capture_mutation'],
                 altered_inputs if engine == 'cpp' else altered_capture)
            status = ('unchanged immutable control' if not mutable else
                      'independent snapshots' if engine == 'cpp' else 'mutable source/capture alias retained')
            print(engine, name, status)
    print('Eight complete-snapshot cases per engine checked; Python mutable-alias divergences preserved.')


def main():
    validate(json.loads((HERE / 'reasoned.json').read_text()),
             json.loads((HERE / 'observed.json').read_text()))


if __name__ == '__main__':
    main()
