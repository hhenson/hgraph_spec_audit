"""Measure frozen scalar-value cases against independent public reference engines."""
import argparse
import contextlib
import importlib.util
import io
import json
from pathlib import Path
import subprocess
import sys
from datetime import datetime, timezone

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('identity_support', HERE.parent / 'delta_eval/observe.py')
support = importlib.util.module_from_spec(spec)
spec.loader.exec_module(support)


def encode(value):
    if value is None:
        return None
    if isinstance(value, bytes):
        return {'bytes': list(value)}
    if isinstance(value, list):
        return {'list': [encode(v) for v in value]}
    if type(value) in (bool, int, float, str):
        return {'type': type(value).__name__, 'value': value}
    raise TypeError(type(value).__name__)


def sanitize(exc):
    return {'error_type': type(exc).__name__, 'message': str(exc)
            .replace(str(HERE.parents[2]), '<audit-root>')
            .replace(sys.prefix, '<environment>').replace(str(Path.home()), '<private-home>')}


def probe():
    import hgraph as hg
    from hgraph.test import eval_node
    before = support.identity()
    result = {'identity': before, 'cases': {}}
    corpus = json.loads((HERE / 'reasoned.json').read_text())
    def evaluate(scalar, samples):
        received = []
        def forward(value):
            received.append({'value': encode(value.value), 'delta': encode(value.delta_value)})
            return value.delta_value
        forward.__annotations__ = {'value': hg.TS[scalar], 'return': hg.TS[scalar]}
        raw = eval_node(hg.compute_node(forward), samples)
        dense = [] if raw is None else list(raw)
        return {'raw': [encode(v) for v in raw] if raw is not None else None,
                'dense': [encode(v) for v in dense + [None] * max(0, len(samples)-len(dense))],
                'received': received, 'horizon': len(samples)}
    for name, tokens in corpus['patterns'].items():
        values = {k: bytes(v) for k,v in corpus['bytes'].items()}
        samples = [None if t is None else values[t] for t in tokens]
        try:
            with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
                result['cases']['bytes_'+name] = evaluate(bytes, samples)
        except Exception as exc:
            result['cases']['bytes_'+name] = sanitize(exc)
    result['cases']['byte_constructor'] = {'valid': encode(bytes([0, 127, 128, 255])),
        'empty': encode(bytes()), 'unsigned_order': bytes([127]) < bytes([128]),
        'equal': bytes([0,255]) == bytes([0,255]),
        'equal_hash': hash(bytes([0,255])) == hash(bytes([0,255]))}
    for bad in (-1, 256):
        try:
            bytes([bad])
            result['cases']['bad_'+str(bad)] = {'unexpected_success': True}
        except Exception as exc:
            result['cases']['bad_'+str(bad)] = sanitize(exc)
    for name, samples in [('mixed', [0, False, '', b'', [1], None, 'next']),
                          ('mutable_retention', [[1], None, [2]])]:
        try:
            with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
                observed = evaluate(object, samples)
            if name == 'mutable_retention':
                saved = eval_node
                # A second public capture retains raw owning observations across mutation.
                def forward(value):
                    return value.delta_value
                forward.__annotations__ = {'value': hg.TS[object], 'return': hg.TS[object]}
                with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
                    raw = saved(hg.compute_node(forward), samples)
                samples[0].append(9)
                observed['captures_after_source_mutation'] = None if raw is None else [encode(v) for v in raw]
            result['cases']['object_bridge_'+name] = observed
        except Exception as exc:
            result['cases']['object_bridge_'+name] = sanitize(exc)
    assert support.identity() == before
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--probe', action='store_true')
    parser.add_argument('--python', type=Path)
    parser.add_argument('--cpp', type=Path)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    if args.probe:
        print(json.dumps(probe(), sort_keys=True))
        return
    if not args.python or not args.cpp or not args.output or args.output.exists():
        parser.error('Use independent interpreters and a new result path')
    hashes = {'reasoned_sha256': support.sha(HERE/'reasoned.json'),
              'observer_sha256': support.sha(Path(__file__)),
              'identity_support_sha256': support.sha(HERE.parent/'delta_eval/observe.py')}
    result = {'measured_at': datetime.now(timezone.utc).isoformat(), **hashes,
              'repeats': 3, 'engines': {}}
    for name, executable, native in [('python', args.python, False), ('cpp', args.cpp, True)]:
        runs = [json.loads(subprocess.check_output([str(executable.absolute()), __file__, '--probe'], text=True).strip().splitlines()[-1]) for _ in range(3)]
        if any(run != runs[0] for run in runs) or runs[0]['identity']['native'] != native:
            raise RuntimeError(name+': unstable or wrong engine')
        result['engines'][name] = runs[0]
        print(name, {k:v.get('error_type','observed') for k,v in runs[0]['cases'].items()})
    assert hashes == {'reasoned_sha256': support.sha(HERE/'reasoned.json'),
                      'observer_sha256': support.sha(Path(__file__)),
                      'identity_support_sha256': support.sha(HERE.parent/'delta_eval/observe.py')}
    args.output.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')


if __name__ == '__main__':
    main()
