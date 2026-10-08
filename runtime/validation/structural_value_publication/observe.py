"""Measure structural held-value return, assignment and endpoint copy separately."""
import argparse
import contextlib
import copy
from datetime import datetime, timezone
import io
import json
from pathlib import Path
import re
import subprocess
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / 'delta_eval'))
from observe import encode, identity, sha
CORPUS = HERE / 'reasoned.json'


def read_all_valid(endpoint):
    try: return bool(endpoint.all_valid)
    except Exception as exc:
        return {'error_type': type(exc).__name__, 'error': str(exc)}


def read(endpoint):
    members = list(endpoint.keys())
    children = {str(k): {'valid': bool(endpoint[k].valid),
                         'value': encode(endpoint[k].value),
                         'modified': bool(endpoint[k].modified)} for k in members}
    return {'valid': bool(endpoint.valid), 'all_valid': read_all_valid(endpoint),
            'modified': bool(endpoint.modified), 'value': encode(endpoint.value),
            'members': sorted(str(k) for k in members), 'children': children,
            'publication': {'present': True, 'payload': encode(endpoint.delta_value)}
            if endpoint.valid and endpoint.modified else {'present': False}}


def observe(case):
    from hgraph import TS, TSB, TSL, TSD, Size, TimeSeriesSchema, OUT, REMOVE
    from hgraph import compute_node, sink_node, graph
    from hgraph.test import eval_node
    result = {'status': 'observed', 'producer': [], 'transfers': [], 'cycles': [], 'events': []}
    shape, mode = case['shape'], case['mode']
    phase = 'schema'
    try:
        class Pair(TimeSeriesSchema):
            left: TS[int]
            right: TS[int]
        schema = TSB[Pair] if shape == 'struct' else TSL[TS[int], Size[2]] if shape == 'fixed' else TSD[int, TS[int]]
        keys = ['left', 'right'] if shape == 'struct' else [0, 1] if shape == 'fixed' else [7, 8]

        def source_a(step, _output=None):
            if step.value == 1:
                _output.value = {keys[0]: 10, keys[1]: 20}
            elif step.value == 2:
                if shape == 'map_remove': _output.value = {keys[1]: REMOVE}
                elif shape == 'map_invalid': _output[keys[1]].invalidate()
            result['producer'].append({'step': step.value, 'which': 'a', 'state': read(_output)})
        source_a.__annotations__ = {'step': TS[int], '_output': OUT, 'return': schema}
        a_node = compute_node(source_a)

        def source_b(step, _output=None):
            if step.value <= 2: _output.value = {keys[0]: 30}
            result['producer'].append({'step': step.value, 'which': 'b', 'state': read(_output)})
        source_b.__annotations__ = {'step': TS[int], '_output': OUT, 'return': schema}
        b_node = compute_node(source_b)

        def transfer(step, a, b, _output=None):
            chosen = a if shape.startswith('map') or step.value == 1 else b
            item = {'step': step.value, 'source': read(chosen), 'operation': mode}
            result['transfers'].append(item)
            if mode == 'delta_control':
                if chosen.valid and chosen.modified: return chosen.delta_value
            elif mode == 'copy_from':
                _output.copy_from(chosen)
            elif mode == 'copy_from_input':
                # This is the genuine public endpoint copy operation, not value assignment.
                _output.copy_from_input(chosen)
            else:
                retained = copy.deepcopy(chosen.value)
                item['retained_value'] = encode(retained)
                if mode == 'return_value': return retained
                _output.value = retained
        transfer.__annotations__ = {'step': TS[int], 'a': schema, 'b': schema, '_output': OUT, 'return': schema}
        transfer_node = compute_node(valid=('step',), active=('step',))(transfer)

        def watch(step, a, b, output):
            chosen = a if shape.startswith('map') or step.value == 1 else b
            result['cycles'].append({'step': step.value, 'source': read(chosen), 'output': read(output)})
        watch.__annotations__ = {'step': TS[int], 'a': schema, 'b': schema, 'output': schema}
        watcher = sink_node(valid=('step',), active=('step',))(watch)

        def event_watch(output):
            if output.valid and output.modified: result['events'].append(read(output))
        event_watch.__annotations__ = {'output': schema}
        event_sink = sink_node(valid=())(event_watch)

        def target(step):
            a = a_node(step)
            b = b_node(step) if not shape.startswith('map') else a
            output = transfer_node(step, a, b)
            watcher(step, a, b, output)
            event_sink(output)
            return output
        target.__annotations__ = {'step': TS[int], 'return': schema}
        phase = 'eval_node'
        result['raw_eval_node'] = encode(eval_node(graph(target), [1, 2, 3]))
    except Exception as exc:
        message = re.sub(r'/(?:home|Users|tmp)/[^\s\n\"\)]+', '<private-path>', str(exc))
        message = re.sub(r'0x[0-9a-fA-F]+', '<address>', message)
        result.update(status='error', phase=phase, error_type=type(exc).__name__, error=message)
    return result


def state_view(cycle, endpoint):
    return {k: {field: child[field] for field in ('valid', 'value')}
            for k, child in cycle[endpoint]['children'].items()}


def assess(case, result):
    if result['status'] != 'observed': return {'state': 'error', 'all_valid': 'unobservable'}
    actual = [state_view(cycle, 'output') for cycle in result['cycles']]
    source = [state_view(cycle, 'source') for cycle in result['cycles']]
    queried = [item['state'] for item in result['producer']]
    queried += [cycle[endpoint] for cycle in result['cycles'] for endpoint in ('source', 'output')]
    return {'state': 'match' if json.dumps(actual, sort_keys=True) == json.dumps(case['expected_states'], sort_keys=True) else 'divergence',
            'source': 'match' if json.dumps(source, sort_keys=True) == json.dumps(case['expected_source_states'], sort_keys=True) else 'divergence',
            'all_valid': 'error' if any(isinstance(state['all_valid'], dict) for state in queried) else 'observed'}


def probe():
    import hgraph
    before = identity()
    with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
        results = {case['id']: observe(case) for case in json.loads(CORPUS.read_text())['cases']}
    if before != identity(): raise RuntimeError('Engine artifacts changed during observation')
    return {'identity': before, 'observations': results,
            'structural_tuple': {'public_TST_available': hasattr(hgraph, 'TST'),
                                 'measured': False, 'atomic_substitute_used': False}}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--probe', action='store_true')
    parser.add_argument('--python', type=Path)
    parser.add_argument('--cpp', type=Path)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    if args.probe:
        print(json.dumps(probe(), sort_keys=True)); return
    if not args.python or not args.cpp or not args.output or args.output.exists():
        parser.error('Supply independent interpreters and a new output destination')
    corpus_hash = sha(CORPUS)
    cases = json.loads(CORPUS.read_text())['cases']
    evidence = {'measured_at': datetime.now(timezone.utc).isoformat(), 'repeats': 3,
                'reasoned_sha256': corpus_hash, 'harness_sha256': sha(__file__),
                'support_sha256': sha(HERE.parent / 'delta_eval/observe.py'), 'engines': {}}
    for name, exe in [('python', args.python), ('cpp', args.cpp)]:
        runs = [json.loads(subprocess.check_output([str(exe.absolute()), __file__, '--probe'],
                              text=True, timeout=120).strip().splitlines()[-1]) for _ in range(3)]
        if any(run != runs[0] for run in runs): raise RuntimeError(name + ': unstable observations')
        result = runs[0]
        if result['identity']['native'] != (name == 'cpp'): raise RuntimeError('Wrong engine identity')
        result['assessment'] = {case['id']: assess(case, result['observations'][case['id']]) for case in cases}
        evidence['engines'][name] = result
    if sha(CORPUS) != corpus_hash: raise RuntimeError('Expectations changed during observation')
    args.output.write_text(json.dumps(evidence, indent=2, sort_keys=True) + '\n')
    for name, result in evidence['engines'].items(): print(name, result['assessment'])


if __name__ == '__main__': main()
