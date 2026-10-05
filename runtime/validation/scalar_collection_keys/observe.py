"""Measure admitted scalar families as exact temporal set elements and map keys."""
import argparse
import contextlib
from datetime import date, datetime, time, timedelta, timezone
from enum import Enum
import io
import json
from pathlib import Path
import subprocess
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / 'delta_eval'))
from observe import identity, sha


class Mode(Enum):
    first = -7
    second = 11


def values():
    import hgraph as hg
    out = {'bool': (bool, False, True), 'i64': (int, -7, 11),
           'f64': (float, -1.5, 2.25), 'str': (str, 'a', 'b'),
           'date': (date, date(2026, 1, 1), date(2026, 1, 2)),
           'time': (time, time(9, 30, 0, 1), time(9, 30, 0, 2)),
           'datetime': (datetime, datetime(2026, 1, 1), datetime(2026, 1, 2)),
           'duration': (timedelta, timedelta(microseconds=-7), timedelta(microseconds=11)),
           'enum': (Mode, Mode.first, Mode.second)}
    if hasattr(hg, 'CivilDateTime'):
        out['civil_datetime'] = (hg.CivilDateTime, hg.CivilDateTime(date(2026, 1, 1), 9, 30),
                                 hg.CivilDateTime(date(2026, 1, 2), 9, 30))
    if hasattr(hg, 'ZoneId'):
        out['timezone'] = (hg.ZoneId, hg.ZoneId('US/Eastern'), hg.ZoneId('America/New_York'))
    if hasattr(hg, 'ZonedDateTime'):
        from hgraph import temporal
        with hg.GlobalState():
            hg.set_time_zone_provider()
            instant = datetime(2026, 1, 1, 9, 30)
            out['zoned_datetime'] = (hg.ZonedDateTime, temporal.at_zone(instant, hg.ZoneId('UTC')),
                                     temporal.at_zone(instant, hg.ZoneId('Etc/UTC')))
    return out


def probe():
    import hgraph as hg
    from hgraph.test import eval_node
    before = identity()
    available = values()
    observations = {}
    for kind in json.loads((HERE / 'reasoned.json').read_text())['scope']:
        if kind not in available:
            observations[kind] = {'availability': 'canonical authoring type unavailable'}
            continue
        scalar, a, b = available[kind]
        def key(value):
            # Probe-local names are only an observation encoding. Equality and exact
            # type are checked before assigning one; no stringification controls keys.
            assert type(value) is type(a)
            if value == a:
                return 'a'
            assert value == b
            return 'b'
        observations[kind] = {'a_equals_b': a == b}
        for family in ('set', 'map'):
            received = []
            try:
                if family == 'set':
                    schema = hg.TSS[scalar]
                    samples = [{a, b}, None, {hg.Removed(a)}]
                    def encode(v):
                        if v is None:
                            return None
                        return {'add': sorted(key(x) for x in v.added),
                                'remove': sorted(key(x) for x in v.removed)}
                else:
                    schema = hg.TSD[scalar, hg.TS[int]]
                    samples = [{a: 10, b: 20}, {a: 10}, None, {a: hg.REMOVE}]
                    def encode(v):
                        if v is None:
                            return None
                        return {'upsert': sorted([key(k), x] for k, x in v.items() if x is not hg.REMOVE),
                                'remove': sorted(key(k) for k, x in v.items() if x is hg.REMOVE)}
                def forward(value):
                    delta = value.delta_value
                    received.append(encode(delta))
                    return delta
                forward.__annotations__ = {'value': schema, 'return': schema}
                raw = eval_node(hg.compute_node(forward), samples)
                observations[kind][family] = {'raw': None if raw is None else [encode(v) for v in raw],
                                               'received': received}
            except Exception as exc:
                message = str(exc).replace(str(HERE.parents[2]), '<audit-root>')
                message = message.replace(sys.prefix, '<environment>').replace(str(Path.home()), '<private-home>')
                observations[kind][family] = {'error_type': type(exc).__name__, 'error': message}
    assert before == identity()
    return {'identity': before, 'observations': observations}


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
        parser.error('two interpreters and a new output path required')
    evidence = {'measured_at': datetime.now(timezone.utc).isoformat(), 'repeats': 3,
                'reasoned_sha256': sha(HERE / 'reasoned.json'), 'harness_sha256': sha(__file__),
                'identity_helper_sha256': sha(HERE.parent / 'delta_eval/observe.py'), 'engines': {}}
    for engine, executable in [('python', args.python), ('cpp', args.cpp)]:
        runs = [json.loads(subprocess.check_output([str(executable), __file__, '--probe'],
                                                   text=True, timeout=30)) for _ in range(3)]
        assert all(run == runs[0] for run in runs), 'unstable observations'
        assert runs[0]['identity']['native'] == (engine == 'cpp')
        evidence['engines'][engine] = runs[0]
        print(engine, json.dumps(runs[0]['observations'], sort_keys=True))
    assert evidence['reasoned_sha256'] == sha(HERE / 'reasoned.json')
    args.output.write_text(json.dumps(evidence, indent=2, sort_keys=True) + '\n')


if __name__ == '__main__':
    main()
