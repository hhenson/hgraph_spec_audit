"""Public growing-list sequence application, invalidation, and removal control."""
import argparse
import contextlib
from datetime import datetime, timezone
import importlib.util
import io
import json
from pathlib import Path
import re
import subprocess

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('boundary_probe', HERE / 'observe.py')
base = importlib.util.module_from_spec(spec)
spec.loader.exec_module(base)
CORPUS = HERE / 'growing_reasoned.json'


def observe(case):
    from hgraph import TS, TSL, Size, OUT, compute_node, graph, sink_node
    from hgraph.test import eval_node
    schema = TSL[TS[int], Size[-1] if base.identity()['native'] else Size]
    result = {'capability': 'supported', 'producer': [], 'cycles': [],
              'source_notifications': [], 'forward_notifications': [],
              'source_events': [], 'forward_events': []}
    step_now = [0]
    def produce(step, _output=None):
        step_now[0] = step.value
        action = case['actions'][step.value - 1]
        if isinstance(action, dict): _output.value = action['assign']
        elif action == 'invalidate': _output.invalidate()
        elif action == 'invalidate_child': _output[0].invalidate()
        elif action != 'idle': raise ValueError(action)
        result['producer'].append({'step': step.value, 'state': base.read(_output, 'growing')})
    produce.__annotations__ = {'step': TS[int], '_output': OUT, 'return': schema}
    producer = compute_node(produce)
    def forward(ts):
        if ts.valid and ts.modified: return ts.delta_value
    forward.__annotations__ = {'ts': schema, 'return': schema}
    copier = compute_node(valid=())(forward)
    def watch_source(ts):
        result['source_notifications'].append({'step': step_now[0], 'state': base.read(ts, 'growing')})
        if ts.valid and ts.modified: result['source_events'].append(step_now[0])
    watch_source.__annotations__ = {'ts': schema}
    source_sink = sink_node(valid=())(watch_source)
    def watch_forward(ts):
        result['forward_notifications'].append({'step': step_now[0], 'state': base.read(ts, 'growing')})
        if ts.valid and ts.modified: result['forward_events'].append(step_now[0])
    watch_forward.__annotations__ = {'ts': schema}
    forward_sink = sink_node(valid=())(watch_forward)
    def cycles(step, source, forwarded):
        result['cycles'].append({'step': step.value, 'source': base.read(source, 'growing'),
                                 'forward': base.read(forwarded, 'growing')})
    cycles.__annotations__ = {'step': TS[int], 'source': schema, 'forwarded': schema}
    cycle_sink = sink_node(valid=(), active=('step',))(cycles)
    def target(step):
        source = producer(step)
        forwarded = copier(source)
        source_sink(source)
        forward_sink(forwarded)
        cycle_sink(step, source, forwarded)
        return forwarded
    target.__annotations__ = {'step': TS[int], 'return': schema}
    try:
        raw = base.encode(eval_node(graph(target), list(range(1, len(case['actions']) + 1))))
        dense = [] if raw is None else list(raw)
        padding = max(0, len(case['actions']) - len(dense))
        result.update(raw_eval_node=raw, input_horizon=len(case['actions']), padding_added=padding,
                      dense_from_input_horizon=dense + [None] * padding)
    except Exception as exc:
        message = re.sub(r'/(?:home|Users|tmp)/[^\s\n\"\)]+', '<private-path>', str(exc))
        message = re.sub(r'0x[0-9a-fA-F]+', '<address>', message)
        result.update(capability='error', phase='eval_node', error_type=type(exc).__name__, error=message)
    return result


def probe():
    before = base.identity()
    observations = {}
    for case in json.loads(CORPUS.read_text())['cases']:
        with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
            observations[case['id']] = observe(case)
    if base.identity() != before: raise RuntimeError('Engine changed')
    return {'identity': before, 'observations': observations}


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--probe', action='store_true')
    p.add_argument('--python', type=Path)
    p.add_argument('--cpp', type=Path)
    p.add_argument('--output', type=Path)
    a = p.parse_args()
    if a.probe: print(json.dumps(probe(), sort_keys=True)); return
    if not a.python or not a.cpp or not a.output or a.output.exists(): p.error('Separate interpreters and new output required')
    frozen = base.sha(CORPUS)
    evidence = {'measured_at': datetime.now(timezone.utc).isoformat(), 'reasoned_sha256': frozen,
                'harness_sha256': base.sha(__file__), 'baseline_harness_sha256': base.sha(HERE / 'observe.py'),
                'support_sha256': base.sha(HERE.parent / 'delta_eval/observe.py'), 'repeats': 3, 'engines': {}}
    for name, exe, native in [('python', a.python, False), ('cpp', a.cpp, True)]:
        runs = [json.loads(subprocess.check_output([str(exe.absolute()), __file__, '--probe'], text=True).strip().splitlines()[-1]) for _ in range(3)]
        if any(r != runs[0] for r in runs) or runs[0]['identity']['native'] != native: raise RuntimeError('Identity or repeatability failure')
        result = runs[0]
        result['assessment'] = {c['id']: base.assess(c, result['observations'][c['id']]) for c in json.loads(CORPUS.read_text())['cases']}
        evidence['engines'][name] = result
    if frozen != base.sha(CORPUS): raise RuntimeError('Expectations changed')
    a.output.write_text(json.dumps(evidence, indent=2, sort_keys=True) + '\n')
    for name, result in evidence['engines'].items():
        for case, obs in result['observations'].items(): print(name, case, obs.get('error_type', obs['capability']), result['assessment'][case])


if __name__ == '__main__': main()
