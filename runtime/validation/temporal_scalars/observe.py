"""Measure three canonical native temporal scalars, without reference substitutes."""
import argparse
import contextlib
from datetime import date, datetime, timezone
import io
import json
from pathlib import Path
import subprocess
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / 'delta_eval'))
from observe import identity, sha


def snapshot(value):
    import hgraph as hg
    if value is None:
        return None
    if isinstance(value, (list, tuple)):
        return [snapshot(v) for v in value]
    if isinstance(value, hg.CivilDateTime):
        return {'civil_datetime': str(value)}
    if isinstance(value, hg.ZoneId):
        return {'timezone': value.name}
    if isinstance(value, hg.ZonedDateTime):
        return {'instant': value.instant.isoformat(), 'zone': value.zone.name,
                'offset_seconds': value.offset_seconds}
    raise TypeError(type(value).__name__)


def error(exc):
    return {'error_type': type(exc).__name__, 'error_message': str(exc)
            .replace(str(HERE.parents[2]), '<audit-root>')
            .replace(sys.prefix, '<environment>').replace(str(Path.home()), '<private-home>')}


def run_eval(scalar, samples):
    import hgraph as hg
    from hgraph.test import eval_node
    received = []
    def forward(value):
        received.append({'value': snapshot(value.value), 'delta': snapshot(value.delta_value)})
        return value.delta_value
    forward.__annotations__ = {'value': hg.TS[scalar], 'return': hg.TS[scalar]}
    raw = eval_node(hg.compute_node(forward), samples)
    return raw, received


def provider_probe():
    import hgraph as hg
    from hgraph import temporal
    events = []
    instant, zone = datetime(2026, 9, 3, 9, 30), hg.ZoneId('Europe/London')
    def attempt(label):
        events.append({'phase': label + ':before'})
        try:
            value = temporal.at_zone(instant, zone)
            events.append({'phase': label + ':success', 'value': snapshot(value)})
            return value
        except Exception as exc:
            events.append({'phase': label + ':failure', **error(exc)})
    attempt('outside_state')
    with hg.GlobalState():
        attempt('state_without_provider')
        hg.set_time_zone_provider()
        saved = attempt('state_with_provider')
    events.append({'phase': 'after_state_before_eval'})
    try:
        raw, received = run_eval(hg.ZonedDateTime, [saved, saved])
        events.append({'phase': 'eval_without_active_provider:success',
                       'raw': snapshot(raw), 'received': received})
    except Exception as exc:
        events.append({'phase': 'eval_without_active_provider:failure', **error(exc)})
    return {'events': events}


def probe(name):
    import hgraph as hg
    before = identity()
    if name == 'availability':
        observation = {'exports': {n: hasattr(hg, n) for n in
                       ('CivilDateTime', 'ZoneId', 'ZonedDateTime', 'ZonedTime')}}
    elif name == 'provider':
        observation = provider_probe()
    else:
        from hgraph import temporal
        with hg.GlobalState():
            hg.set_time_zone_provider()
            instant = datetime(2026, 9, 3, 9, 30)
            values = {
                'civil_datetime': (hg.CivilDateTime, hg.CivilDateTime(date(1970, 1, 1), 0),
                                   hg.CivilDateTime(date(2026, 9, 3), 10, 30)),
                'timezone': (hg.ZoneId, hg.ZoneId('UTC'), hg.ZoneId('Europe/London')),
                'zoned_datetime': (hg.ZonedDateTime,
                                   temporal.at_zone(instant, hg.ZoneId('UTC')),
                                   temporal.at_zone(instant, hg.ZoneId('Europe/London'))),
            }
            if name == 'zone_alias':
                scalar, a, b = hg.ZoneId, hg.ZoneId('US/Eastern'), hg.ZoneId('America/New_York')
                samples = [a, b, a]
            elif name == 'same_instant_different_zone':
                scalar, a, b = values['zoned_datetime']
                samples = [a, b, a]
            else:
                kind, pattern = next((k, name[len(k) + 1:]) for k in values if name.startswith(k + '_'))
                scalar, a, b = values[kind]
                if pattern == 'retention':
                    shared = [a]
                    scalar, samples = list[scalar], [shared, None, shared]
                else:
                    tokens = json.loads((HERE / 'reasoned.json').read_text())['patterns'][pattern]
                    samples = [None if t is None else a if t == 'a' else b for t in tokens]
            observation = {'inputs_before': snapshot(samples), 'a_equals_b': a == b}
            raw, received = run_eval(scalar, samples)
            observation.update(raw=snapshot(raw), received=received)
            if name.endswith('_retention'):
                samples[0].append(b)
                observation['raw_after_source_mutation'] = snapshot(raw)
            second, second_received = run_eval(scalar, samples)
            observation.update(inputs_second=snapshot(samples), second_raw=snapshot(second),
                               second_received=second_received, first_after_second=snapshot(raw))
            if name.endswith('_retention'):
                raw[0].append(a)
                observation.update(first_after_capture_mutation=snapshot(raw),
                                   second_after_capture_mutation=snapshot(second))
    assert before == identity(), 'engine identity changed'
    return {'identity': before, 'observation': observation}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--probe')
    parser.add_argument('--python', type=Path)
    parser.add_argument('--cpp', type=Path)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    if args.probe:
        with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
            result = probe(args.probe)
        print(json.dumps(result, sort_keys=True))
        return
    if not args.python or not args.cpp or not args.output or args.output.exists():
        parser.error('two interpreters and a new output path required')
    reasoned = json.loads((HERE / 'reasoned.json').read_text())
    case_ids = [k + '_' + p for k in reasoned['scope'] for p in reasoned['patterns']] + reasoned['extra_cases']
    evidence = {'measured_at': datetime.now(timezone.utc).isoformat(), 'repeats': 3,
                'reasoned_sha256': sha(HERE / 'reasoned.json'), 'harness_sha256': sha(__file__),
                'identity_helper_sha256': sha(HERE.parent / 'delta_eval/observe.py'), 'engines': {}}
    for engine, executable in [('python', args.python), ('cpp', args.cpp)]:
        observations, package = {}, None
        for name in ['availability'] + (case_ids + ['provider'] if engine == 'cpp' else []):
            runs = [json.loads(subprocess.check_output([str(executable), __file__, '--probe', name],
                                                       text=True, timeout=30)) for _ in range(3)]
            assert all(run == runs[0] for run in runs), (engine, name, 'unstable')
            current = runs[0]
            assert current['identity']['native'] == (engine == 'cpp')
            assert package is None or package == current['identity']
            package = current['identity']
            observations[name] = current['observation']
            print(engine, name, json.dumps(current['observation'], sort_keys=True), flush=True)
        evidence['engines'][engine] = {'identity': package, 'observations': observations}
    assert evidence['reasoned_sha256'] == sha(HERE / 'reasoned.json')
    args.output.write_text(json.dumps(evidence, indent=2, sort_keys=True) + '\n')


if __name__ == '__main__':
    main()
