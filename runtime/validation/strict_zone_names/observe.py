"""Measure syntax-only zone construction separately from provider admission."""
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
from observe import identity, sha


def attempt(action):
    try:
        return {'status': 'success', 'value': action()}
    except Exception as exc:
        return {'status': 'error', 'error_type': type(exc).__name__,
                'error_message': str(exc).replace(str(HERE.parents[2]), '<audit-root>')
                .replace(sys.prefix, '<environment>').replace(str(Path.home()), '<private-home>')}


def probe(name):
    import hgraph as hg
    before = identity()
    if name == '@availability':
        observed = {'exports': {n: hasattr(hg, n) for n in ('ZoneId', 'ZonedDateTime')}}
    else:
        from hgraph import temporal
        def construct():
            return hg.ZoneId(name).name
        def decode():
            return hg.from_json_builder(hg.ZoneId)(json.dumps(name)).name
        def resolve():
            value = temporal.at_zone(datetime(2026, 9, 3, 9, 30), hg.ZoneId(name))
            return {'instant': value.instant.isoformat(), 'zone': value.zone.name,
                    'offset_seconds': value.offset_seconds}
        observed = {'constructor_without_provider': attempt(construct),
                    'json_without_provider': attempt(decode)}
        with hg.GlobalState():
            hg.set_time_zone_provider()
            observed['constructor_with_provider'] = attempt(construct)
            observed['json_with_provider'] = attempt(decode)
            observed['at_zone_with_provider'] = attempt(resolve)
            observed['equal_to_new_york'] = hg.ZoneId(name) == hg.ZoneId('America/New_York')
    assert before == identity(), 'engine identity changed'
    return {'identity': before, 'observation': observed}


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
    corpus_hash = sha(HERE / 'reasoned.json')
    cases = json.loads((HERE / 'reasoned.json').read_text())['cases']
    evidence = {'measured_at': datetime.now(timezone.utc).isoformat(), 'repeats': 3,
                'reasoned_sha256': corpus_hash, 'harness_sha256': sha(__file__),
                'identity_helper_sha256': sha(HERE.parent / 'delta_eval/observe.py'), 'engines': {}}
    for engine, executable in [('python', args.python), ('cpp', args.cpp)]:
        observations, engine_identity = {}, None
        for name in ['@availability'] + (list(cases) if engine == 'cpp' else []):
            runs = [json.loads(subprocess.check_output([str(executable), __file__, '--probe', name],
                                                       text=True, timeout=30)) for _ in range(3)]
            assert all(run == runs[0] for run in runs), (engine, name, 'unstable')
            current = runs[0]
            assert current['identity']['native'] == (engine == 'cpp')
            assert engine_identity is None or engine_identity == current['identity']
            engine_identity = current['identity']
            observations[name] = current['observation']
            print(engine, name, json.dumps(current['observation'], sort_keys=True), flush=True)
        evidence['engines'][engine] = {'identity': engine_identity, 'observations': observations}
    assert sha(HERE / 'reasoned.json') == corpus_hash
    args.output.write_text(json.dumps(evidence, indent=2, sort_keys=True) + '\n')


if __name__ == '__main__':
    main()
