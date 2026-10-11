"""Verify the frozen matrix report and pinned source manifest; no compilers run."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import subprocess

HERE = Path(__file__).resolve().parent


def sha(data):
    return hashlib.sha256(data).hexdigest()


def require(condition, message):
    if not condition:
        raise ValueError(message)


def git_bytes(checkout, revision, path):
    return subprocess.check_output(['git', '-C', str(checkout), 'show', f'{revision}:{path}'])


def source_manifest(checkout, revision):
    """Apply the recorded C++ matrix's module selection to pinned Git sources."""
    paths = subprocess.check_output([
        'git', '-C', str(checkout), 'ls-tree', '-r', '--name-only', revision,
        'hgl/hgraph',
    ], text=True).splitlines()
    parents = ['hgl/hgraph', 'hgl/hgraph/impl', 'hgl/hgraph/tests']
    selected = [p for p in paths if Path(p).suffix == '.hgl' and str(Path(p).parent) in parents]
    selected.sort(key=lambda p: (parents.index(str(Path(p).parent)), Path(p).name))
    sources = []
    for path in selected:
        data = git_bytes(checkout, revision, path)
        text = data.decode()
        if not re.search(r'^module hgraph\.std(?:\s|$)', text, re.MULTILINE):
            continue
        sources.append({
            'file': path, 'sha256': sha(data),
            'tests': re.findall(r'^\s*test ([A-Za-z_][A-Za-z_0-9]*)\s*\{', text, re.MULTILINE),
            'eval_call_sites': len(re.findall(r'\beval\s*\(', text)),
        })
    return sources


def negative_manifest(checkout, revision):
    data = git_bytes(checkout, revision, 'compiler/negative_testing/cases.json')
    manifest = json.loads(data)
    return sha(data), [{'id': row['id'], 'expected_exit': row['expected_exit']} for row in manifest['cases']]


def validate(report, expected):
    require(report['schema_version'] == 1, 'unsupported report schema')
    require(report['revisions'] == expected['revisions'], 'changed dependency or compiler revisions')
    require(report['sources'] == expected['sources'], 'changed source hashes, case names or eval call sites')
    sources = report['sources']
    names = sorted(name for source in sources for name in source['tests'])
    require(len(names) == len(set(names)), 'duplicate shared test names')
    counts = {
        'test_files': sum(bool(source['tests']) for source in sources),
        'named_tests': len(names),
        'eval_call_sites': sum(source['eval_call_sites'] for source in sources),
    }
    require(counts == {'test_files': 40, 'named_tests': 258, 'eval_call_sites': 600}, 'changed shared source coverage')
    require(report['shared_source_counts'] == counts, 'inconsistent shared source counts')
    measurements = report['measurements']
    identities = [(row['backend'], row['platform']) for row in measurements]
    require(len(identities) == 4 and set(identities) == {
        ('cpp', 'linux'), ('cpp', 'mac'), ('cpp', 'windows'), ('rust', 'linux'),
    }, 'missing, extra or duplicated matrix measurement')
    for row in measurements:
        require(row['source_revision'] == expected['revisions'][row['backend']], 'changed measured compiler revision')
        require(row['passed'] == names, 'missing, extra, duplicated or renamed passed tests')
        require(row['failed'] == [], 'recorded matrix failures')
        for field in ('binary_sha256', 'raw_log_sha256'):
            require(re.fullmatch('[0-9a-f]{64}', row[field]) is not None, f'invalid {field}')
        if row['backend'] == 'rust':
            require(row['whole_suite'] == {'executed_tests': 280, 'evaluations': 679, 'failures': 0}, 'changed Rust whole-suite counts')
    negatives = report['negative_measurements']
    require(len(negatives) == 2 and {(row['backend'], row['platform']) for row in negatives} == {
        ('cpp', 'linux'), ('rust', 'linux'),
    }, 'missing, extra or duplicated negative measurement')
    for row in negatives:
        require(row['source_revision'] == expected['revisions'][row['backend']], 'changed negative compiler revision')
        require(row['source_revision_verified_by_runner'] is False, 'caller-supplied revision relabeled as verified')
        require(row['manifest_sha256'] == expected['negative_manifest_sha256'], 'changed negative fixture manifest')
        require(row['observer_sha256'] == expected['negative_observer_sha256'], 'changed negative observer')
        cases = row['cases']
        require(len(cases) == 43, 'missing or extra negative case')
        require([{'id': case['id'], 'expected_exit': case['expected_exit']} for case in cases] == expected['negative_cases'], 'changed negative case identity or expected exit')
        for case in cases:
            require(case['observed_exit'] == case['expected_exit'] and case['matched'] is True, f'negative mismatch: {case["id"]}')
        for field in ('compiler_sha256', 'raw_report_sha256'):
            require(re.fullmatch('[0-9a-f]{64}', row[field]) is not None, f'invalid {field}')


def check(report=None, stdlib_checkout=None, spec_checkout=None):
    provenance = json.loads((HERE / 'provenance.json').read_text())
    expected_bytes = (HERE / 'expected.json').read_bytes()
    require(sha(expected_bytes) == provenance['expected_sha256'], 'pinned source manifest integrity changed')
    expected = json.loads(expected_bytes)
    raw = (HERE / 'results.json').read_bytes() if report is None else None
    if report is None:
        report = json.loads(raw)
    validate(report, expected)
    if raw is not None:
        require(sha(raw) == provenance['results_sha256'], 'frozen report bytes changed')
    require(sha(json.dumps(report, sort_keys=True, separators=(',', ':')).encode()) == provenance['results_semantic_sha256'], 'frozen report content changed')
    if stdlib_checkout is not None:
        require(source_manifest(stdlib_checkout, expected['revisions']['stdlib']) == expected['sources'], 'pinned standard-library sources differ from manifest')
    if spec_checkout is not None:
        digest, cases = negative_manifest(spec_checkout, expected['revisions']['spec'])
        require(digest == expected['negative_manifest_sha256'] and cases == expected['negative_cases'], 'pinned negative fixtures differ from manifest')
    return True


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--stdlib-checkout', type=Path)
    parser.add_argument('--spec-checkout', type=Path)
    args = parser.parse_args()
    check(stdlib_checkout=args.stdlib_checkout, spec_checkout=args.spec_checkout)
    print('Frozen HGL matrix: 258 named tests on four backend/platform pairs, 43 negative controls per Linux backend; no fresh execution.')
