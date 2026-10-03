"""Measure exact eval output-key collisions without normalizing the damage."""
import argparse
import contextlib
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


def describe(value):
    if isinstance(value, (list, tuple)):
        return {'kind': type(value).__name__, 'items': [describe(x) for x in value]}
    return type(value).__name__


def probe(case_name):
    import hgraph as hg
    from hgraph.test import eval_node
    case = json.loads((HERE / 'reasoned.json').read_text())['cases'][case_name]
    before = identity()
    native = before['native']
    recorder_key = 'eval_node::out' if native else 'nodes.record.out'
    user_key = recorder_key if case['collide'] else 'audit.user.recording'
    timed = case['layout'] == 'sparse' or not native
    events = []

    def payload(marker):
        return [(hg.MIN_ST, marker)] if timed else [marker]

    def snapshot(gs, key):
        if key not in gs:
            return {'present': False}
        value = gs[key]
        return {'present': True, 'value': encode(value), 'exported_types': describe(value)}

    def event(phase, gs):
        events.append({'phase': phase, 'recorder_entry': snapshot(gs, recorder_key),
                       'user_entry': snapshot(gs, user_key)})

    @hg.compute_node
    def target(ts: hg.TS[int], _global_state: hg.GlobalState = None) -> hg.TS[int]:
        event('eval_before_' + str(ts.value), _global_state)
        if case['write'] == 'eval':
            _global_state[user_key] = payload(900 + ts.value)
        event('eval_after_' + str(ts.value), _global_state)
        return ts.delta_value

    @target.start
    def target_start(_global_state: hg.GlobalState):
        event('start_before', _global_state)
        if case['write'] == 'start':
            _global_state[user_key] = payload(701)
        event('start_after', _global_state)

    @target.stop
    def target_stop(_global_state: hg.GlobalState):
        event('stop_before', _global_state)
        if case['write'] == 'stop':
            _global_state[user_key] = payload(703)
        event('stop_after', _global_state)

    gs = hg.GlobalState()
    with gs:
        if case['write'] == 'seed':
            gs[user_key] = payload(700)
        initial = snapshot(gs, user_key)
        try:
            raw = eval_node(target, [1, 2], __elide__=case['layout'] == 'sparse')
            result = {'raw': encode(raw)}
        except Exception as exc:
            message = str(exc).replace(str(Path.home()), '<private-home>')
            message = re.sub(r'/tmp/[^\s\n:]+', '<private-temp>', message)
            message = re.sub(r'0x[0-9a-fA-F]+', '<address>', message)
            result = {'error_type': type(exc).__name__, 'error': message}
        final_user = snapshot(gs, user_key)
        final_recorder = snapshot(gs, recorder_key)
    if before != identity():
        raise RuntimeError('engine artifacts changed during observation')
    return {'identity': before, 'recorder_key': recorder_key, 'user_key': user_key,
            'logical_entry_type': 'list[tuple[datetime,int]]' if timed else 'list[int]',
            'initial_user_entry': initial, 'events': events, 'result': result,
            'final_user_entry': final_user, 'final_recorder_entry': final_recorder}


def assess(case, result):
    output = 'error' if 'error' in result['result'] else ('match' if result['result']['raw'] == case['expected_raw'] else 'divergence')
    entry = result['final_user_entry']
    timed = result['logical_entry_type'] == 'list[tuple[datetime,int]]'
    values = None
    if entry['present']:
        values = [x[1] for x in entry['value']] if timed else entry['value']
    return {'output_isolation': output,
            'user_entry_preserved': 'match' if values == case['expected_user_payloads'] else 'divergence'}


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--probe'); p.add_argument('--python', type=Path); p.add_argument('--cpp', type=Path); p.add_argument('--output', type=Path)
    a = p.parse_args()
    if a.probe:
        with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
            result = probe(a.probe)
        print(json.dumps(result, sort_keys=True)); return
    if not a.python or not a.cpp or not a.output or a.output.exists():
        p.error('independent interpreters and new output required')
    corpus_hash = sha(HERE / 'reasoned.json')
    cases = json.loads((HERE / 'reasoned.json').read_text())['cases']
    evidence = {'reasoned_sha256': corpus_hash, 'harness_sha256': sha(__file__),
                'identity_helper_sha256': sha(HERE.parent / 'delta_eval/observe.py'),
                'measured_at': datetime.now(timezone.utc).isoformat(), 'repeats': 3, 'engines': {}}
    for engine, executable in [('python', a.python), ('cpp', a.cpp)]:
        observations = {}
        first_identity = None
        for name, case in cases.items():
            runs = [json.loads(subprocess.check_output([str(executable.absolute()), __file__, '--probe', name], text=True).strip().splitlines()[-1]) for _ in range(3)]
            if any(r != runs[0] for r in runs):
                raise RuntimeError('unstable fresh-process observations: ' + engine + '/' + name)
            result = runs[0]
            current_identity = result.pop('identity')
            if current_identity['native'] != (engine == 'cpp'):
                raise RuntimeError('wrong engine identity')
            if first_identity is None: first_identity = current_identity
            if current_identity != first_identity: raise RuntimeError('engine changed across cases')
            result['assessment'] = assess(case, result)
            observations[name] = result
            print(engine, name, result['assessment'])
        evidence['engines'][engine] = {'identity': first_identity, 'observations': observations}
    if sha(HERE / 'reasoned.json') != corpus_hash:
        raise RuntimeError('expectations changed during observation')
    a.output.write_text(json.dumps(evidence, indent=2, sort_keys=True) + '\n')


if __name__ == '__main__': main()
