"""Verify the frozen matrix report and pinned source manifest; no compilers run."""
import argparse
import hashlib
import importlib.util
import json
import posixpath
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



def negative_sources(checkout, revision):
    """Bind every executed fixture and part to the selected immutable Git blobs."""
    manifest = json.loads(git_bytes(checkout, revision, 'compiler/negative_testing/cases.json'))
    require(manifest['path_base'] == 'manifest_directory', 'unsupported negative path base')
    def fingerprint(path):
        require(not path.startswith('/'), 'absolute negative source path')
        relative = posixpath.normpath('compiler/negative_testing/' + path)
        require(not relative.startswith('../'), 'negative source escapes repository')
        return sha(git_bytes(checkout, revision, relative))
    return {'spec_revision': revision, 'cases': [
        {'id': case['id'], 'file': case['file'], 'source_sha256': fingerprint(case['file']),
         'part_sources': [{'file': part, 'sha256': fingerprint(part)} for part in case.get('parts', [])]}
        for case in manifest['cases']]}


def verify_negative_checkout(checkout, sources):
    """The selected working files must also be the blobs that the runner reads."""
    for case in sources['cases']:
        for source in [{'file': case['file'], 'sha256': case['source_sha256']}, *case['part_sources']]:
            path = Path(checkout) / posixpath.normpath('compiler/negative_testing/' + source['file'])
            require(sha(path.read_bytes()) == source['sha256'], 'negative checkout source differs from pinned blob')


def validate_negative(summary, report, manifest, sources=None):
    """Derive matches from original process output using the measured observer."""
    observer_path = HERE.parent / 'negative_testing/observe.py'
    require(sha(observer_path.read_bytes()) == summary['observer_sha256'], 'negative matching observer changed')
    spec = importlib.util.spec_from_file_location('matrix_negative_observer', observer_path)
    observer = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(observer)
    for field in ('backend', 'source_revision', 'source_revision_verified_by_runner',
                  'compiler_sha256', 'observer_sha256', 'manifest_sha256'):
        require(report[field] == summary[field], f'original negative report changed {field}')
    cases = manifest['cases']
    if sources is None:
        sources = json.loads((HERE / 'negative_sources.json').read_text())
    require(len(sources['cases']) == len(cases), 'negative source inventory count changed')
    require(len(report['cases']) == len(cases) == len(summary['cases']), 'original negative report case count changed')
    for case, observed, condensed, source in zip(cases, report['cases'], summary['cases'], sources['cases']):
        require(source['id'] == case['id'] and source['file'] == case['file'], 'negative source inventory identity changed')
        require(observed['source_sha256'] == source['source_sha256'], f'negative fixture source differs from pinned blob: {case["id"]}')
        require(observed['part_sources'] == source['part_sources'], f'negative fixture parts differ from pinned blobs: {case["id"]}')
        for field in ('id', 'file', 'mode', 'expected_exit'):
            require(observed[field] == case[field], f'original negative case changed {field}')
        required = observer.expectations(case, report['cases_directory'])
        require(observed['expected'] == required, f'negative outcome expectations changed: {case["id"]}')
        matched = observer.matches(required, observed)
        require(matched and observed['matches'] is matched, f'negative detailed outcomes mismatch: {case["id"]}')
        require(condensed == {'id': case['id'], 'expected_exit': case['expected_exit'],
                              'observed_exit': observed['run']['returncode'], 'matched': matched},
                f'negative summary differs from original outcomes: {case["id"]}')


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
    source_bytes = (HERE / 'negative_sources.json').read_bytes()
    require(sha(source_bytes) == provenance['negative_sources_sha256'], 'pinned negative source inventory changed')
    sources = json.loads(source_bytes)
    require(sources['spec_revision'] == expected['revisions']['spec'], 'negative source inventory revision changed')
    manifest_bytes = (HERE / 'negative_manifest.json').read_bytes()
    require(sha(manifest_bytes) == expected['negative_manifest_sha256'], 'pinned detailed negative manifest changed')
    manifest = json.loads(manifest_bytes)
    raw = (HERE / 'results.json').read_bytes() if report is None else None
    if report is None:
        report = json.loads(raw)
    validate(report, expected)
    for summary in report['negative_measurements']:
        original_bytes = (HERE / f'negative_{summary["backend"]}.json').read_bytes()
        require(sha(original_bytes) == summary['raw_report_sha256'], 'original negative report bytes changed')
        validate_negative(summary, json.loads(original_bytes), manifest, sources)
    if raw is not None:
        require(sha(raw) == provenance['results_sha256'], 'frozen report bytes changed')
    require(sha(json.dumps(report, sort_keys=True, separators=(',', ':')).encode()) == provenance['results_semantic_sha256'], 'frozen report content changed')
    if stdlib_checkout is not None:
        require(source_manifest(stdlib_checkout, expected['revisions']['stdlib']) == expected['sources'], 'pinned standard-library sources differ from manifest')
    if spec_checkout is not None:
        digest, cases = negative_manifest(spec_checkout, expected['revisions']['spec'])
        require(digest == expected['negative_manifest_sha256'] and cases == expected['negative_cases'], 'pinned negative fixtures differ from manifest')
        require(negative_sources(spec_checkout, expected['revisions']['spec']) == sources, 'pinned negative source blobs differ from inventory')
        verify_negative_checkout(spec_checkout, sources)
    return True


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--stdlib-checkout', type=Path)
    parser.add_argument('--spec-checkout', type=Path)
    args = parser.parse_args()
    check(stdlib_checkout=args.stdlib_checkout, spec_checkout=args.spec_checkout)
    print('Frozen HGL matrix: 258 named tests on four backend/platform pairs, 43 negative controls per Linux backend; no fresh execution.')
