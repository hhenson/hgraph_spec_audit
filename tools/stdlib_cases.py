"""Render C++ assertions from the independently reasoned standard-library cases."""
import argparse
import json
from pathlib import Path


def render(cases):
    signatures = {'bit_and_i64': ('lhs', 'rhs'), 'sample_i64': ('signal', 'ts'), 'dedup_i64': ('ts',)}
    lines = ["    unsigned failures = 0;"]
    for case in cases:
        node = case['node']
        parameters = signatures[node]
        if set(case['inputs']) != set(parameters):
            raise ValueError('unexpected inputs for ' + node)
        def ticks(values):
            if any(v is not None and type(v) is not int for v in values):
                raise ValueError('expected i64 or absent tick')
            return 'ticks{' + ', '.join('std::nullopt' if v is None else str(v) for v in values) + '}'
        args = ', '.join(ticks(case['inputs'][p]) for p in parameters)
        label = json.dumps(json.dumps(case['name']))
        lines += [f'    if (!check<conformance::stdlib::{node}>({label}, {ticks(case["expected"])}, {args})) ++failures;']
    lines += ['    return failures == 0 ? 0 : 1;']
    return '\n'.join(lines) + '\n'


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--cases', required=True, type=Path)
    parser.add_argument('--output', required=True, type=Path)
    args = parser.parse_args()
    args.output.write_text(render(json.loads(args.cases.read_text())))
