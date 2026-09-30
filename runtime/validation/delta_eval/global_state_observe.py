"""Measure ordinary injected global state without replay/record-specific access."""
import argparse
import contextlib
from datetime import datetime, timezone
import io
import json
from pathlib import Path
import subprocess

from observe import encode, identity, sha

HERE = Path(__file__).resolve().parent


def probe():
    import hgraph as hg
    from hgraph.test import eval_node

    before = identity()

    @hg.compute_node
    def count(ts: hg.TS[int], _global_state: hg.GlobalState = None) -> hg.TS[int]:
        _global_state['arbitrary.count'] = _global_state['arbitrary.count'] + ts.value
        return _global_state['arbitrary.count']

    @count.start
    def count_start(_global_state: hg.GlobalState):
        _global_state['arbitrary.started'] = True

    @count.stop
    def count_stop(_global_state: hg.GlobalState):
        _global_state['arbitrary.stopped'] = True

    def state(gs):
        return {name: gs['arbitrary.' + name] for name in ('count', 'started', 'stopped')}

    first = hg.GlobalState()
    with first:
        first['arbitrary.count'] = 40
        first_output = eval_node(count, [1, None, 2])
        first_state = state(first)
        try:
            first['arbitrary.missing']
        except KeyError as error:
            missing_index = type(error).__name__
        else:
            missing_index = 'no error'
        missing_default = first.get('arbitrary.missing', 99)
        for key, value in [('zero', 0), ('false', False), ('empty_text', '')]:
            first['arbitrary.' + key] = value
        ordinary = {key: first['arbitrary.' + key] for key in ('zero', 'false', 'empty_text')}
    second = hg.GlobalState()
    with second:
        second['arbitrary.count'] = 5
        second_output = eval_node(count, [3])
        second_state = state(second)
    observed = {
        'first_output': encode(first_output), 'first_state': first_state,
        'second_output': encode(second_output), 'second_state': second_state,
        'retained_first_state': state(first), 'missing_index': missing_index,
        'missing_get_default': missing_default, 'ordinary_values': ordinary,
    }
    if before != identity():
        raise RuntimeError('engine artifacts changed during observation')
    return {'identity': before, 'observed': observed}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--probe', action='store_true')
    parser.add_argument('--python', type=Path)
    parser.add_argument('--cpp', type=Path)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    if args.probe:
        with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
            result = probe()
        print(json.dumps(result, sort_keys=True))
        return
    if not args.python or not args.cpp or not args.output or args.output.exists():
        parser.error('independent interpreters and a new output required')
    corpus = HERE / 'global_state_reasoned.json'
    corpus_hash = sha(corpus)
    expected = json.loads(corpus.read_text())['expected']
    evidence = {
        'reasoned_sha256': corpus_hash, 'harness_sha256': sha(__file__),
        'identity_helper_sha256': sha(HERE / 'observe.py'),
        'measured_at': datetime.now(timezone.utc).isoformat(), 'repeats': 3, 'engines': {},
    }
    for name, executable in [('python', args.python), ('cpp', args.cpp)]:
        runs = [json.loads(subprocess.check_output(
            [str(executable.absolute()), __file__, '--probe'], text=True
        ).strip().splitlines()[-1]) for _ in range(3)]
        if any(run != runs[0] for run in runs):
            raise RuntimeError('unstable ' + name)
        result = runs[0]
        if result['identity']['native'] != (name == 'cpp'):
            raise RuntimeError('wrong engine identity: ' + name)
        result['assessment'] = {
            key: 'match' if json.dumps(result['observed'][key], sort_keys=True)
            == json.dumps(value, sort_keys=True) else 'divergence'
            for key, value in expected.items()
        }
        evidence['engines'][name] = result
    if sha(corpus) != corpus_hash:
        raise RuntimeError('expectations changed during execution')
    args.output.write_text(json.dumps(evidence, indent=2, sort_keys=True) + '\n')
    for name, result in evidence['engines'].items():
        print(name, result['assessment'])


if __name__ == '__main__':
    main()
