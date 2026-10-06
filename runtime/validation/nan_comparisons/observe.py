"""Genuine registered graph operators for NaN comparisons and logarithm."""
import argparse
import contextlib
from datetime import datetime, timezone
import io
import json
import math
from pathlib import Path
import re
import subprocess
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / 'delta_eval'))
from observe import identity, sha
CORPUS = HERE / 'reasoned.json'


def encode(value):
    if isinstance(value, float):
        if math.isnan(value): return {'float_class': 'nan'}
        if math.isinf(value): return {'float_class': 'positive_infinity' if value > 0 else 'negative_infinity'}
    if isinstance(value, (list, tuple)): return [encode(v) for v in value]
    if value is None or isinstance(value, (bool, int, float)): return value
    raise TypeError(type(value).__name__)


def observe(case):
    import hgraph
    from hgraph import TS, graph, sink_node
    from hgraph.test import eval_node
    events = {'lhs': [], 'rhs': [], 'result': []}
    def watcher(label, scalar):
        def watch(ts):
            events[label].append({'valid': bool(ts.valid), 'modified': bool(ts.modified),
                                  'value': encode(ts.value), 'delta': encode(ts.delta_value)})
        watch.__annotations__ = {'ts': TS[scalar]}
        return sink_node(watch)
    left = watcher('lhs', float)
    right = watcher('rhs', float)
    output = watcher('result', float if case['kind'] == 'ln' else bool)
    try:
        if case['kind'] == 'comparison':
            op = getattr(hgraph, case['operator'])
            @graph
            def target(lhs: TS[float], rhs: TS[float]) -> TS[bool]:
                left(lhs); right(rhs)
                value = op(lhs, rhs)
                output(value)
                return value
            operands = [float('nan') if v == 'nan' else v for v in case['operands']]
            result = eval_node(target, [operands[0], None], [operands[1], None])
        elif case['kind'] == 'ln':
            @graph
            def target(ts: TS[float]) -> TS[float]:
                left(ts)
                value = hgraph.ln(ts)
                output(value)
                return value
            result = eval_node(target, [case['operand'], None])
        else:
            op = getattr(hgraph, case['operator'])
            @graph
            def target(ts: TS[float]) -> TS[bool]:
                value = hgraph.ln(ts)
                left(value); right(value)
                result = op(value, value)
                output(result)
                return result
            result = eval_node(target, [case['operand'], None])
        raw = encode(result)
        dense = [] if raw is None else list(raw)
        padding = max(0, 2 - len(dense))
        return {'status': 'observed', 'events': events, 'raw_eval_node': raw,
                'input_horizon': 2, 'padding_added': padding, 'dense': dense + [None] * padding}
    except Exception as exc:
        message = re.sub(r'/(?:home|Users|tmp)/[^\s\n\"\)]+', '<private-path>', str(exc))
        message = re.sub(r'0x[0-9a-fA-F]+', '<address>', message)
        return {'status': 'error', 'error_type': type(exc).__name__, 'error': message, 'events': events}


def primitives(native):
    import hgraph
    names = []
    if native:
        import _hgraph
        names = _hgraph.operator_names()
    result = {}
    for name in json.loads(CORPUS.read_text())['primitive_candidates']:
        public = getattr(hgraph, name, None)
        item = {'public_exported': public is not None,
                'native_registered': name in names if native else None}
        if public is not None:
            from hgraph.test import eval_node
            try: item['raw_eval_node'] = encode(eval_node(public, [float('nan'), 1.0]))
            except Exception as exc: item['error_type'] = type(exc).__name__
        result[name] = item
    return result


def assessment(case, observed):
    if observed['status'] == 'error': return 'error'
    return 'match' if json.dumps(observed['dense'], sort_keys=True) == json.dumps(case['expected'], sort_keys=True) else 'divergence'


def probe():
    before = identity()
    observations = {}
    with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
        for case in json.loads(CORPUS.read_text())['cases']: observations[case['id']] = observe(case)
        available = primitives(before['native'])
    if before != identity(): raise RuntimeError('Engine identity changed')
    return {'identity': before, 'observations': observations, 'primitives': available}


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--probe', action='store_true')
    p.add_argument('--python', type=Path)
    p.add_argument('--cpp', type=Path)
    p.add_argument('--output', type=Path)
    a = p.parse_args()
    if a.probe: print(json.dumps(probe(), sort_keys=True, allow_nan=False)); return
    if not a.python or not a.cpp or not a.output or a.output.exists(): p.error('Independent interpreters and new output required')
    frozen = sha(CORPUS)
    evidence = {'measured_at': datetime.now(timezone.utc).isoformat(), 'reasoned_sha256': frozen,
                'harness_sha256': sha(__file__), 'identity_helper_sha256': sha(HERE.parent / 'delta_eval/observe.py'),
                'repeats': 3, 'engines': {}}
    for name, exe, native in [('python', a.python, False), ('cpp', a.cpp, True)]:
        runs = [json.loads(subprocess.check_output([str(exe.absolute()), __file__, '--probe'], text=True).strip().splitlines()[-1]) for _ in range(3)]
        if any(r != runs[0] for r in runs) or runs[0]['identity']['native'] != native: raise RuntimeError('Repeatability/identity failure')
        result = runs[0]
        result['assessment'] = {c['id']: assessment(c, result['observations'][c['id']]) for c in json.loads(CORPUS.read_text())['cases']}
        evidence['engines'][name] = result
    if frozen != sha(CORPUS): raise RuntimeError('Corpus changed')
    a.output.write_text(json.dumps(evidence, indent=2, sort_keys=True, allow_nan=False) + '\n')
    for name, result in evidence['engines'].items():
        from collections import Counter
        print(name, dict(Counter(result['assessment'].values())), result['primitives'])
        for case, obs in result['observations'].items():
            if obs['status'] == 'error': print(case, obs['error_type'])


if __name__ == '__main__': main()
