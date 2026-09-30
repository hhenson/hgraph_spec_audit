"""Replay shared scalar and graph tests using released hgraph authoring APIs."""
import argparse
from datetime import date, datetime, time, timedelta
import hashlib
import importlib.metadata
import json
import operator
from pathlib import Path
import sys

import hgraph as hg
from hgraph.test import eval_node
from shared_cases import TYPES, encode, read
from evidence_support import python_fingerprint, validate_replay

SCALARS = {
    'int_sum': operator.add, 'mixed_sum': operator.add, 'text_sum': operator.add,
    'quotient': operator.truediv, 'floor_quotient': operator.floordiv, 'remainder': operator.mod,
    'test_text_length': len, 'test_text_empty': lambda x: not x,
    'test_text_contains': lambda x,y: y in x, 'test_text_prefix': str.startswith,
    'test_text_suffix': str.endswith, 'scalar_truth': bool, 'string_truth': bool,
    'bit_intersection': operator.and_, 'scalar_round': round, 'integer_power': pow,
    'float_power': pow, 'left': operator.lshift, 'right': operator.rshift,
    'text_slice': lambda x,a,b: x[a:b],
    'date_year': lambda x:x.year, 'date_month': lambda x:x.month, 'date_day': lambda x:x.day,
    'time_hour': lambda x:x.hour, 'datetime_year': lambda x:x.year,
    'datetime_hour': lambda x:x.hour, 'duration_days': lambda x:x.days,
    'duration_seconds': lambda x:x.seconds, 'duration_microseconds': lambda x:x.microseconds,
    'test_bitwise_value': operator.and_,
    'calendar_year': lambda x:x.year, 'calendar_month': lambda x:x.month, 'calendar_day': lambda x:x.day,
    'normalized_days': lambda x:x.days, 'normalized_seconds': lambda x:x.seconds, 'normalized_micros': lambda x:x.microseconds,
    'instant_timestamp': lambda x:(x-datetime(1970,1,1)).total_seconds(),
    'epoch_seconds': lambda x:(x-datetime(1970,1,1)).total_seconds(),
}
OPERATORS = {
    'true_ticks': 'if_true', 'first_two': 'take', 'frozen': 'freeze', 'latched': 'until_true',
    'sample_integer': 'sample', 'drop_integer': 'drop', 'dedup_integer': 'dedup',
    'filter_integer': 'filter_', 'sum_integer': 'sum_', 'reset_integer': 'sum_',
    'mean_integer': 'mean', 'dedup_tolerance': 'dedup', 'equals': 'eq_', 'positive_sign': 'sign',
    'average': 'mean', 'integer_power': 'pow_', 'mixed_power': 'pow_', 'shifted_left': 'lshift_',
    'shifted_right': 'rshift_', 'sliced': 'substr', 'integer_add': 'add_', 'mixed_add': 'add_',
    'text_add': 'add_', 'integer_div': 'div_', 'integer_floor': 'floordiv_', 'integer_mod': 'mod_',
    'date_year': 'year', 'instant_year': 'year', 'instant_hour': 'hour', 'duration_seconds': 'seconds',
    'with_default': 'default',
}


@hg.compute_node
def member_source(ts: hg.TS[int]) -> hg.TSS[int]:
    return {ts.value} if ts.value > 0 else {hg.Removed(-ts.value)}

@hg.compute_node
def boolean_members(ts: hg.TS[bool]) -> hg.TSS[bool]:
    return {ts.value}

@hg.compute_node
def copy_additions(ts: hg.TSS[bool]) -> hg.TSS[bool]:
    return set(ts.added())

@hg.compute_node
def instant_year(ts: hg.TS[datetime]) -> hg.TS[int]:
    return ts.value.year

@hg.compute_node
def instant_hour(ts: hg.TS[datetime]) -> hg.TS[int]:
    return ts.value.hour

@hg.compute_node
def duration_seconds(ts: hg.TS[timedelta]) -> hg.TS[int]:
    return ts.value.seconds


def node(case):
    function, params = case['function'], case['parameters']
    annotations = [f'{name}: {ty}' if fixed else f'{name}: TS[{ty}]' for name,ty,fixed,_ in params]
    names = [p[0] for p in params]
    scope = dict(hg=hg, TS=hg.TS, **TYPES)
    if case['module'] == 'hgraph.native':
        operation = str if function.startswith('text_of_') else SCALARS[function]
        scope['operation'] = operation
        expression = 'operation(' + ','.join(name+'.value' for name in names) + ')'
        decorator = hg.compute_node
    else:
        scope['operation'] = getattr(hg, OPERATORS.get(function,''), None)
        expression = 'operation(' + ','.join(names) + ')'
        decorator = hg.graph
        if function == 'latched' and '_hgraph' not in sys.modules: expression = 'hg.until_true(lambda value: value, ts)'
        if function in ('instant_year','instant_hour','duration_seconds') and '_hgraph' not in sys.modules:
            scope['operation'] = {'instant_year': instant_year, 'instant_hour': instant_hour, 'duration_seconds': duration_seconds}[function]
        if function == 'first_two': expression = 'hg.take(ts, 2)'
        if function == 'reset_integer': expression = 'hg.sum_(ts, reset=reset)'
        if function == 'dedup_tolerance': expression = 'hg.dedup(ts, abs_tol=abs_tol)'
        if function == 'convert_integer': expression = 'hg.convert[TS[int]](ts)'
        if function == 'convert_float': expression = 'hg.convert[TS[float]](ts)'
        if function == 'with_zero': expression = 'hg.default(ts, hg.const(0.0))'
        if function in ('watched','printed','checked'): expression = 'ts'
        if function in ('forty_two','text','later','never'):
            expression = {'forty_two':'hg.const(42)', 'text':'hg.const("hgl")', 'later':'hg.const(7, delay=duration(microseconds=2))', 'never':'hg.nothing(TS[int])'}[function]
        if function in ('membership','boolean_copy_size'):
            scope.update(member_source=member_source, boolean_members=boolean_members, copy_additions=copy_additions)
            expression = 'hg.contains_(member_source(ts), item)' if function == 'membership' else 'hg.len_(copy_additions(boolean_members(ts)))'
    output = f"TS[{case['output']}]"
    definition = f"def scenario({','.join(annotations)}) -> {output}:\n    return {expression}\n"
    exec(definition, scope)
    return decorator(scope['scenario'])


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--stdlib', type=Path, required=True)
    parser.add_argument('--engine', choices=['python','cpp'], required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    engine = 'cpp' if '_hgraph' in sys.modules else 'python'
    if engine != args.engine: raise RuntimeError(f'expected {args.engine}, got {engine}')
    cases, hashes = read(args.stdlib)
    rows = []
    for index, case in enumerate(cases):
        adapter = 'released_operator'
        if case['module'] == 'hgraph.native': adapter = 'python_scalar_lift'
        elif case['function'] in ('membership','boolean_copy_size'): adapter = 'python_set_producer_with_released_operator'
        elif case['function'] in ('instant_year','instant_hour','duration_seconds') and engine == 'python': adapter = 'python_temporal_projection'
        elif case['function'] in ('watched','printed','checked'): adapter = 'tick_passthrough_only'
        row = dict(index=index, module=case['module'], name=case['name'], function=case['function'], adapter=adapter, expected=case['expected'])
        try:
            ticks = eval_node(node(case), **case['arguments'])
            horizon = max((len(v) for v in case['arguments'].values() if isinstance(v,list)), default=0)
            if ticks is None: ticks = [None] * horizon
            elif len(ticks) < horizon: ticks = ticks + [None] * (horizon-len(ticks))
            row.update(observed=ticks, matches=ticks == case['expected'])
        except Exception as error:
            row.update(error=f'{type(error).__name__}: {error}', matches=False)
        rows.append(row)
    binary = getattr(sys.modules.get('_hgraph'), '__file__', None)
    report = dict(engine=engine, version=importlib.metadata.version('hgraph'),
                  python_sources=python_fingerprint(Path(hg.__file__).parent),
                  support_sha256=hashlib.sha256(Path(__file__).with_name('evidence_support.py').read_bytes()).hexdigest(),
                  native_sha256=hashlib.sha256(Path(binary).read_bytes()).hexdigest() if binary else None,
                  sources=hashes, harness_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                  reader_sha256=hashlib.sha256(Path(__file__).with_name('shared_cases.py').read_bytes()).hexdigest(), cases=rows)
    args.output.write_text(json.dumps(report, indent=2, default=encode)+'\n')
    print(f"{engine}: {sum(r['matches'] for r in rows)}/{len(rows)} match")
    try:
        validate_replay(engine, rows)
    except ValueError as error:
        raise SystemExit(str(error)) from error


if __name__ == '__main__': main()
