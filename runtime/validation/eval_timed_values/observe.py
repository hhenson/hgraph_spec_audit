"""Observe typed ordinary timed inputs; keep raw results separate from densification."""
import argparse
import contextlib
from datetime import date, datetime, time, timedelta, timezone
import io
import json
from pathlib import Path
import subprocess
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / 'delta_eval'))
from observe import encode, identity, scalar_decode, sha


def observe(case):
    import hgraph as hg
    from hgraph.test import eval_node
    scalar = {'bool': bool, 'i64': int, 'f64': float, 'str': str,
              'date': date, 'time': time, 'datetime': datetime, 'duration': timedelta}[case['type']]
    schema = hg.TS[scalar]
    entries = [(hg.MIN_ST + item['index'] * hg.MIN_TD, scalar_decode(item['value']))
               for item in case['timed_entries']]

    def source(data):
        yield from data
    source.__annotations__ = {'data': list[tuple[datetime, scalar]], 'return': schema}
    replay = hg.generator(source)

    def pass_through(value):
        return value.delta_value
    pass_through.__annotations__ = {'value': schema, 'return': schema}
    compute = hg.compute_node(pass_through)

    def composition():
        return compute(replay(entries))
    composition.__annotations__ = {'return': schema}
    raw = encode(eval_node(hg.graph(composition)))
    dense = [] if raw is None else list(raw)
    padding = max(0, case['horizon'] - len(dense))
    dense += [None] * padding
    return {'raw_eval_result': raw, 'source_entry_count': len(entries),
            'external_dense_horizon': case['horizon'], 'padding_added': padding,
            'dense_from_external_horizon': dense}


def probe():
    before = identity()
    observations = {}
    for case in json.loads((HERE / 'reasoned.json').read_text())['cases']:
        try:
            with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
                observations[case['id']] = observe(case)
        except Exception as exc:
            observations[case['id']] = {'error_type': type(exc).__name__,
                'error': str(exc).replace(str(Path.home()), '<private-home>')}
    if before != identity():
        raise RuntimeError('engine changed during observation')
    return {'identity': before, 'observations': observations}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--probe', action='store_true')
    parser.add_argument('--python', type=Path)
    parser.add_argument('--cpp', type=Path)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    if args.probe:
        print(json.dumps(probe(), sort_keys=True))
        return
    if not args.python or not args.cpp or not args.output or args.output.exists():
        parser.error('independent interpreters and a new output are required')
    corpus = HERE / 'reasoned.json'
    corpus_hash = sha(corpus)
    cases = json.loads(corpus.read_text())['cases']
    evidence = {'measured_at': datetime.now(timezone.utc).isoformat(),
                'reasoned_sha256': corpus_hash, 'harness_sha256': sha(__file__),
                'identity_helper_sha256': sha(HERE.parent / 'delta_eval/observe.py'),
                'repeats': 3, 'engines': {}}
    for name, executable, native in [('python', args.python, False), ('cpp', args.cpp, True)]:
        runs = [json.loads(subprocess.check_output([str(executable), __file__, '--probe'], text=True))
                for _ in range(3)]
        if any(run != runs[0] for run in runs) or runs[0]['identity']['native'] != native:
            raise RuntimeError('unstable or incorrect engine: ' + name)
        result = runs[0]
        result['assessment'] = {}
        for case in cases:
            outcome = result['observations'][case['id']]
            result['assessment'][case['id']] = ('error' if 'error' in outcome else
                'match' if outcome['dense_from_external_horizon'] == case['expected_dense'] else 'divergence')
        evidence['engines'][name] = result
        print(name, result['assessment'])
    if sha(corpus) != corpus_hash:
        raise RuntimeError('prewritten expectations changed')
    args.output.write_text(json.dumps(evidence, indent=2, sort_keys=True) + '\n')


if __name__ == '__main__':
    main()
