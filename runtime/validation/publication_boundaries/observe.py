"""Observe publication boundaries through genuine public compute/eval APIs."""
import argparse
import contextlib
from datetime import datetime, timezone
import io
import json
from pathlib import Path
import subprocess
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / 'delta_eval'))
from observe import encode, identity, sha  # imported under script's __main__ name
CORPUS = HERE / 'reasoned.json'


def read(endpoint, shape):
    """Observe state separately from the guarded publication accessor."""
    state = {'valid': bool(endpoint.valid), 'modified': bool(endpoint.modified),
             'value': encode(endpoint.value)}
    state['publication'] = ({'present': True, 'payload': encode(endpoint.delta_value)}
                            if endpoint.valid and endpoint.modified else {'present': False})
    if shape in ('fixed', 'fixed_zero', 'struct', 'struct_zero', 'map', 'growing'):
        members = list(endpoint.keys())
        state['members'] = sorted(str(k) for k in members)
        state['children'] = {str(k): {'valid': bool(endpoint[k].valid),
                                      'modified': bool(endpoint[k].modified),
                                      'value': encode(endpoint[k].value)} for k in members}
    if shape in ('map', 'growing'):
        for prop in ('added_keys', 'removed_keys'):
            try:
                state[prop] = sorted(str(k) for k in getattr(endpoint, prop)())
            except (AttributeError, RuntimeError, TypeError) as exc:
                state[prop] = {'unavailable': type(exc).__name__}
    return state


def observe(case):
    import hgraph
    from hgraph import TS, TSS, TSL, TSB, TSD, Size, TimeSeriesSchema, OUT
    from hgraph import compute_node, graph, sink_node, set_delta
    from hgraph.test import eval_node
    shape = case['shape']
    result = {'capability': 'supported', 'producer': [], 'cycles': [],
              'source_notifications': [], 'forward_notifications': [],
              'source_events': [], 'forward_events': []}
    step_now = [0]
    phase = 'form_schema'
    try:
        if shape == 'tuple':
            # Both runtimes lack a distinct structural tuple authoring marker.
            if not hasattr(hgraph, 'TST'):
                return {'capability': 'unsupported', 'surface': 'hgraph.TST',
                        'reason': 'No structural tuple marker; TS[tuple] would test an atomic value.'}
            schema = hgraph.TST[TS[int], TS[int]]
        elif shape == 'growing':
            # Native facade passes -1 to its public dynamic-list type constructor;
            # historical Size without a bound is its declared variable-size marker.
            schema = TSL[TS[int], Size[-1] if identity()['native'] else Size]
        elif shape == 'scalar': schema = TS[int]
        elif shape == 'set': schema = TSS[int]
        elif shape in ('fixed', 'fixed_zero'):
            schema = TSL[TS[int], Size[0 if shape == 'fixed_zero' else 2]]
        elif shape in ('struct', 'struct_zero'):
            class Pair(TimeSeriesSchema):
                left: TS[int]
                right: TS[int]
            class Empty(TimeSeriesSchema):
                pass
            schema = TSB[Empty if shape == 'struct_zero' else Pair]
        elif shape == 'map': schema = TSD[int, TS[int]]
        else: raise ValueError(shape)

        def produce(step, _output=None):
            step_now[0] = step.value
            action = case['actions'][step.value - 1]
            if action == 'empty':
                _output.value = set_delta(set(), set()) if shape == 'set' else {}
            elif action == 'seed':
                _output.value = (10 if shape == 'scalar' else
                    {1, 2} if shape == 'set' else
                    {'left': 10, 'right': 20} if shape == 'struct' else
                    {7: 10, 8: 20} if shape == 'map' else {0: 10, 1: 20})
            elif action == 'invalidate': _output.invalidate()
            elif action == 'invalidate_child':
                key = 'left' if shape == 'struct' else 7 if shape == 'map' else 0
                _output[key].invalidate()
            elif action == 'create_invalid': _output.get_or_create(9)
            elif action == 'cancel':
                _output.add(1)
                _output.remove(1)
            elif action != 'idle': raise ValueError(action)
            result['producer'].append({'step': step.value, 'state': read(_output, shape)})
        produce.__annotations__ = {'step': TS[int], '_output': OUT, 'return': schema}
        producer = compute_node(produce)

        def forward(ts):
            if ts.valid and ts.modified:
                return ts.delta_value
        forward.__annotations__ = {'ts': schema, 'return': schema}
        copier = compute_node(valid=())(forward)

        def source_watch(ts):
            result['source_notifications'].append({'step': step_now[0], 'state': read(ts, shape)})
            if ts.valid and ts.modified: result['source_events'].append(step_now[0])
        source_watch.__annotations__ = {'ts': schema}
        source_sink = sink_node(valid=())(source_watch)

        def forward_watch(ts):
            result['forward_notifications'].append({'step': step_now[0], 'state': read(ts, shape)})
            if ts.valid and ts.modified: result['forward_events'].append(step_now[0])
        forward_watch.__annotations__ = {'ts': schema}
        forward_sink = sink_node(valid=())(forward_watch)

        def cycle_watch(step, source, forwarded):
            result['cycles'].append({'step': step.value, 'source': read(source, shape),
                                     'forward': read(forwarded, shape)})
        cycle_watch.__annotations__ = {'step': TS[int], 'source': schema, 'forwarded': schema}
        clock_sink = sink_node(valid=(), active=('step',))(cycle_watch)

        def target(step):
            source = producer(step)
            forwarded = copier(source)
            source_sink(source)
            forward_sink(forwarded)
            clock_sink(step, source, forwarded)
            return forwarded
        target.__annotations__ = {'step': TS[int], 'return': schema}
        phase = 'eval_node'
        raw = encode(eval_node(graph(target), list(range(1, len(case['actions']) + 1))))
        result['raw_eval_node'] = raw
        result['input_horizon'] = len(case['actions'])
        dense = [] if raw is None else list(raw)
        result['padding_added'] = max(0, len(case['actions']) - len(dense))
        result['dense_from_input_horizon'] = dense + [None] * result['padding_added']
        return result
    except Exception as exc:
        import re
        message = str(exc)
        message = re.sub(r'/(?:home|Users|tmp)/[^\s\n\"\)]+', '<private-path>', message)
        message = re.sub(r'0x[0-9a-fA-F]+', '<address>', message)
        result.update(capability='error', phase=phase, error_type=type(exc).__name__, error=message)
        return result


def at(value, path):
    for key in path.split('.'):
        value = value[int(key)] if isinstance(value, list) else value[key]
    return value


def assess(case, observed):
    findings = []
    for rule in case['expectations']:
        try:
            actual = at(observed, rule['path'])
            expected = at(observed, rule['same_as']) if 'same_as' in rule else rule['equals']
            status = 'match' if json.dumps(actual, sort_keys=True) == json.dumps(expected, sort_keys=True) else 'divergence'
        except (KeyError, IndexError, TypeError): status = 'unobservable'
        findings.append({'path': rule['path'], 'status': status})
    return findings


def probe():
    before = identity()
    observations = {}
    for case in json.loads(CORPUS.read_text())['cases']:
        with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
            observations[case['id']] = observe(case)
    if identity() != before: raise RuntimeError('Engine changed during observation')
    return {'identity': before, 'observations': observations}


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
        parser.error('Supply separate interpreters and a new output path')
    corpus_hash = sha(CORPUS)
    evidence = {'measured_at': datetime.now(timezone.utc).isoformat(), 'reasoned_sha256': corpus_hash,
                'harness_sha256': sha(__file__), 'support_sha256': sha(HERE.parent / 'delta_eval/observe.py'),
                'repeats': 3, 'engines': {}}
    for name, executable, native in [('python', args.python, False), ('cpp', args.cpp, True)]:
        runs = [json.loads(subprocess.check_output([str(executable.absolute()), __file__, '--probe'],
                              text=True).strip().splitlines()[-1]) for _ in range(3)]
        if any(run != runs[0] for run in runs): raise RuntimeError(name + ': nonrepeatable observations')
        if runs[0]['identity']['native'] != native: raise RuntimeError(name + ': wrong engine')
        result = runs[0]
        result['assessment'] = {c['id']: assess(c, result['observations'][c['id']])
                                for c in json.loads(CORPUS.read_text())['cases']}
        evidence['engines'][name] = result
    if sha(CORPUS) != corpus_hash: raise RuntimeError('Expectations changed during observation')
    args.output.write_text(json.dumps(evidence, sort_keys=True, indent=2) + '\n')
    for name, data in evidence['engines'].items():
        for case, outcome in data['observations'].items():
            print(name, case, outcome.get('error_type', outcome['capability']),
                  [(x['path'], x['status']) for x in data['assessment'][case]])


if __name__ == '__main__': main()
