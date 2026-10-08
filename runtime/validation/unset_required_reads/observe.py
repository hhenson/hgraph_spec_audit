"""Measure genuine retained observations before required scalar/collection operations."""
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


def observe(case):
    from hgraph import TS, TSB, TSL, TSD, Size, TimeSeriesSchema, OUT, compute_node, graph
    from hgraph.test import eval_node
    result = {'status': 'observed', 'reads': []}
    try:
        child = {'scalar': TS[int], 'boolean': TS[bool],
                 'fixed_list': TSL[TS[int], Size[2]], 'map': TSD[int, TS[int]]}[case['shape']]
        Partial = type('Partial_' + case['id'], (TimeSeriesSchema,), {'__annotations__': {'sibling': TS[int], 'child': child}})
        schema = TSB[Partial]
        value = {'scalar': 4, 'boolean': True, 'fixed_list': {0: 4, 1: 5}, 'map': {7: 4}}[case['shape']]
        value = case.get('value', value)
        def source(step):
            return {'sibling': 1, **({'child': value} if case['present'] else {})}
        source.__annotations__ = {'step': TS[int], 'return': schema}
        source_node = compute_node(source)
        def consume(step, source):
            for surface in ('bundle_projection', 'child_observation'):
                row = {'surface': surface, 'child_valid': bool(source.child.valid)}
                result['reads'].append(row)
                retained = copy.deepcopy(source.value if surface == 'bundle_projection' else source.child.value)
                row['retained'] = encode(retained)
                row['retained_type'] = type(retained).__name__
                row['phase'] = 'projection'
                try:
                    payload = retained['child'] if surface == 'bundle_projection' else retained
                    row['payload'] = encode(payload)
                    row['payload_type'] = type(payload).__name__
                    row['phase'] = 'operation'
                    if case['operation'] == 'add_one': answer = payload + 1
                    elif case['operation'] == 'branch': answer = 1 if payload else 0
                    elif case['operation'] == 'len': answer = len(payload)
                    else: answer = list(payload.items())
                    row.update(outcome='value', result=encode(answer))
                except Exception as exc:
                    row.update(outcome='failure', error_type=type(exc).__name__, error=str(exc))
            return 1
        consume.__annotations__ = {'step': TS[int], 'source': schema, 'return': TS[int]}
        consume_node = compute_node(valid=('step',), active=('step',))(consume)
        def target(step): return consume_node(step, source_node(step))
        target.__annotations__ = {'step': TS[int], 'return': TS[int]}
        result['eval_result'] = encode(eval_node(graph(target), [1]))
    except Exception as exc:
        message = re.sub(r'/(?:home|Users|tmp)/[^\s\n\"\)]+', '<private-path>', str(exc))
        result.update(status='error', error_type=type(exc).__name__, error=message)
    return result


def probe():
    before = identity()
    with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
        results = {case['id']: observe(case) for case in json.loads(CORPUS.read_text())['cases']}
    if before != identity(): raise RuntimeError('Engine artifacts changed')
    return {'identity': before, 'observations': results}


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
    evidence = {'measured_at': datetime.now(timezone.utc).isoformat(), 'repeats': 3,
                'reasoned_sha256': sha(CORPUS), 'harness_sha256': sha(__file__),
                'support_sha256': sha(HERE.parent / 'delta_eval/observe.py'), 'engines': {}}
    for name, exe in [('python', args.python), ('cpp', args.cpp)]:
        runs = [json.loads(subprocess.check_output([str(exe.absolute()), __file__, '--probe'],
                        text=True, timeout=120).strip().splitlines()[-1]) for _ in range(3)]
        if any(run != runs[0] for run in runs): raise RuntimeError(name + ': unstable observations')
        result = runs[0]
        if result['identity']['native'] != (name == 'cpp'): raise RuntimeError('Wrong engine identity')
        evidence['engines'][name] = result
    args.output.write_text(json.dumps(evidence, indent=2, sort_keys=True) + '\n')
    for name, result in evidence['engines'].items():
        print(name, json.dumps(result['observations'], sort_keys=True))


if __name__ == '__main__': main()
