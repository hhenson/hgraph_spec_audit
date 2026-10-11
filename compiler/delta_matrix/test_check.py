"""Corrupted matrix summaries must fail recorded-evidence validation."""
import copy
import json
import subprocess
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import check

HERE = Path(__file__).resolve().parent


class MatrixEvidence(unittest.TestCase):
    def setUp(self):
        self.report = json.loads((HERE / 'results.json').read_text())
        self.expected = json.loads((HERE / 'expected.json').read_text())
        self.manifest = json.loads((HERE / 'negative_manifest.json').read_text())
        self.global_parts = json.loads((HERE / 'negative_global_parts.json').read_text())
        self.libraries = json.loads((HERE / 'negative_libraries.json').read_text())
        self.negatives = {backend: json.loads((HERE / f'negative_{backend}.json').read_text())
                          for backend in ('cpp', 'rust')}

    def reject(self, mutation, message):
        report = copy.deepcopy(self.report)
        mutation(report)
        with self.assertRaisesRegex(ValueError, message):
            check.validate(report, self.expected)

    def test_recorded_report(self):
        self.assertTrue(check.check())
        self.assertTrue(check.check(self.report))

    def test_source_hash_case_name_and_eval_counts_are_pinned(self):
        mutations = [
            lambda r: r['sources'][0].update(sha256='0' * 64),
            lambda r: r['sources'][-1]['tests'].__setitem__(0, 'invented_case'),
            lambda r: r['sources'][-1].update(eval_call_sites=99),
            lambda r: r['sources'].pop(),
        ]
        for index, mutation in enumerate(mutations):
            with self.subTest(index=index):
                self.reject(mutation, 'changed source')

    def test_aggregate_counts_must_follow_sources(self):
        for field in ('test_files', 'named_tests', 'eval_call_sites'):
            with self.subTest(field=field):
                self.reject(lambda r: r['shared_source_counts'].__setitem__(field, 1), 'inconsistent shared source counts')

    def test_every_measurement_has_exact_shared_case_names(self):
        for index in range(4):
            mutations = [
                lambda r: r['measurements'][index]['passed'].pop(),
                lambda r: r['measurements'][index]['passed'].append('invented_case'),
                lambda r: r['measurements'][index]['passed'].__setitem__(0, r['measurements'][index]['passed'][1]),
                lambda r: r['measurements'][index]['passed'].__setitem__(0, 'renamed_case'),
            ]
            for mutation in mutations:
                with self.subTest(index=index, mutation=mutation):
                    self.reject(mutation, 'passed tests')

    def test_failure_lists_are_checked_on_every_platform(self):
        for index in range(4):
            with self.subTest(index=index):
                self.reject(lambda r: r['measurements'][index]['failed'].append(r['measurements'][index]['passed'][0]), 'matrix failures')

    def test_missing_and_duplicate_measurement_rejected(self):
        self.reject(lambda r: r['measurements'].pop(), 'matrix measurement')
        self.reject(lambda r: r['measurements'].__setitem__(1, r['measurements'][0]), 'matrix measurement')

    def test_rust_suite_counts_and_failures_checked(self):
        for field in ('executed_tests', 'evaluations', 'failures'):
            with self.subTest(field=field):
                self.reject(lambda r: r['measurements'][3]['whole_suite'].__setitem__(field, 1), 'Rust whole-suite counts')

    def test_compiler_and_dependency_revisions_pinned(self):
        for field in self.report['revisions']:
            with self.subTest(field=field):
                self.reject(lambda r: r['revisions'].__setitem__(field, '0' * 40), 'revisions')
        self.reject(lambda r: r['measurements'][0].update(source_revision='0' * 40), 'measured compiler revision')

    def test_negative_case_id_count_and_match_checked(self):
        for index in range(2):
            with self.subTest(index=index):
                self.reject(lambda r: r['negative_measurements'][index]['cases'].pop(), 'negative case')
                self.reject(lambda r: r['negative_measurements'][index]['cases'][0].update(id='invented'), 'negative case identity')
                self.reject(lambda r: r['negative_measurements'][index]['cases'][0].update(matched=False), 'negative mismatch')
                self.reject(lambda r: r['negative_measurements'][index]['cases'][0].update(observed_exit=1), 'negative mismatch')

    def test_expected_failing_controls_cannot_be_relabeled_as_success(self):
        for backend_index, row in enumerate(self.report['negative_measurements']):
            for case_index, case in enumerate(row['cases']):
                if case['expected_exit']:
                    with self.subTest(backend_index=backend_index, case=case['id']):
                        self.reject(lambda r: r['negative_measurements'][backend_index]['cases'][case_index].update(expected_exit=0, observed_exit=0, matched=True), 'negative case identity')

    def test_negative_measurements_and_provenance_checked(self):
        self.reject(lambda r: r['negative_measurements'].pop(), 'negative measurement')
        self.reject(lambda r: r['negative_measurements'].__setitem__(1, r['negative_measurements'][0]), 'negative measurement')
        for field, value, message in [
            ('source_revision', '0' * 40, 'negative compiler revision'),
            ('source_revision_verified_by_runner', True, 'relabeled as verified'),
            ('manifest_sha256', '0' * 64, 'fixture manifest'),
            ('observer_sha256', '0' * 64, 'negative observer'),
        ]:
            with self.subTest(field=field):
                self.reject(lambda r: r['negative_measurements'][0].update({field: value}), message)

    def test_changed_valid_fingerprint_fails_report_integrity(self):
        for collection, field in [('measurements', 'binary_sha256'), ('measurements', 'raw_log_sha256'), ('negative_measurements', 'compiler_sha256'), ('negative_measurements', 'raw_report_sha256')]:
            with self.subTest(collection=collection, field=field):
                report = copy.deepcopy(self.report)
                report[collection][0][field] = '0' * 64
                check.validate(report, self.expected)
                with self.assertRaisesRegex(ValueError, 'changed'):
                    check.check(report)

    def test_original_negative_reports_match_pinned_detailed_expectations(self):
        for summary in self.report['negative_measurements']:
            check.validate_negative(summary, self.negatives[summary['backend']], self.manifest)

    def test_deleted_duplicated_renamed_and_wrong_outcomes_rejected_with_same_exit(self):
        for summary in self.report['negative_measurements']:
            for kind in ('executed', 'rejection'):
                original = self.negatives[summary['backend']]
                case_index = next(i for i, case in enumerate(original['cases'])
                                  if f'[{kind}]' in case['run']['stdout'])
                for mutation in ('delete', 'duplicate', 'rename', 'outcome', 'kind'):
                    with self.subTest(backend=summary['backend'], kind=kind, mutation=mutation):
                        report = copy.deepcopy(original)
                        case = report['cases'][case_index]
                        lines = case['run']['stdout'].splitlines(keepends=True)
                        line_index = next(i for i, line in enumerate(lines) if f'[{kind}]' in line)
                        line = lines[line_index]
                        if mutation == 'delete':
                            del lines[line_index]
                        elif mutation == 'duplicate':
                            lines.insert(line_index, line)
                        elif mutation == 'rename':
                            lines[line_index] = 'invented_identity ... ' + line.split(' ... ', 1)[1]
                        elif mutation == 'outcome':
                            lines[line_index] = line.replace(' ... ok [', ' ... FAILED [') if ' ... ok [' in line else line.replace(' ... FAILED [', ' ... ok [')
                        else:
                            other = 'rejection' if kind == 'executed' else 'executed'
                            lines[line_index] = line.replace(f'[{kind}]', f'[{other}]')
                        case['run']['stdout'] = ''.join(lines)
                        self.assertTrue(case['matches'])
                        self.assertEqual(case['run']['returncode'], case['expected_exit'])
                        with self.assertRaisesRegex(ValueError, 'detailed outcomes mismatch'):
                            check.validate_negative(summary, report, self.manifest)

    def test_preflight_failure_or_timeout_cannot_be_hidden_by_match_flag(self):
        for summary in self.report['negative_measurements']:
            original = self.negatives[summary['backend']]
            case_index = next(i for i, case in enumerate(original['cases']) if 'source_check' in case)
            for field, value in [('returncode', 1), ('timed_out', True)]:
                with self.subTest(backend=summary['backend'], field=field):
                    report = copy.deepcopy(original)
                    report['cases'][case_index]['source_check'][field] = value
                    with self.assertRaisesRegex(ValueError, 'detailed outcomes mismatch'):
                        check.validate_negative(summary, report, self.manifest)

    def test_forbidden_execution_cannot_pass_with_expected_exit_and_claimed_match(self):
        for summary in self.report['negative_measurements']:
            report = copy.deepcopy(self.negatives[summary['backend']])
            case = next(case for case in report['cases'] if case['expected'].get('not_executed'))
            name = case['expected']['not_executed'][0]
            case['run']['stdout'] += f'\n{name} ... ok [executed]\n'
            self.assertTrue(case['matches'])
            self.assertEqual(case['run']['returncode'], case['expected_exit'])
            with self.assertRaisesRegex(ValueError, 'detailed outcomes mismatch'):
                check.validate_negative(summary, report, self.manifest)

    def test_original_expectations_cannot_be_rewritten_to_match_wrong_outputs(self):
        for summary in self.report['negative_measurements']:
            report = copy.deepcopy(self.negatives[summary['backend']])
            case = report['cases'][0]
            case['expected']['runtime_results'] = []
            case['run']['stdout'] = ''
            with self.assertRaisesRegex(ValueError, 'outcome expectations changed'):
                check.validate_negative(summary, report, self.manifest)

    def test_original_report_hash_is_required(self):
        with tempfile.TemporaryDirectory() as folder:
            target = Path(folder)
            for name in ('provenance.json', 'expected.json', 'negative_manifest.json', 'negative_sources.json', 'negative_global_parts.json', 'negative_libraries.json'):
                (target / name).write_bytes((HERE / name).read_bytes())
            (target / 'negative_cpp.json').write_text('{}')
            with patch.object(check, 'HERE', target):
                with self.assertRaisesRegex(ValueError, 'original negative report bytes changed'):
                    check.check(self.report)

    def test_fixture_and_part_hashes_must_match_pinned_sources(self):
        for summary in self.report['negative_measurements']:
            original = self.negatives[summary['backend']]
            for field in ('source_sha256', 'part_sources'):
                report = copy.deepcopy(original)
                index = next(i for i, case in enumerate(report['cases']) if case['part_sources'])
                if field == 'source_sha256':
                    report['cases'][index][field] = '0' * 64
                else:
                    report['cases'][index][field][0]['sha256'] = '0' * 64
                with self.subTest(backend=summary['backend'], field=field):
                    with self.assertRaisesRegex(ValueError, 'pinned blob'):
                        check.validate_negative(summary, report, self.manifest)

    def test_checkout_main_and_parts_match_immutable_git_blobs(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            cases = root / 'compiler/negative_testing'
            cases.mkdir(parents=True)
            manifest = {'path_base': 'manifest_directory', 'cases': [
                {'id': 'probe', 'file': 'main.hgl', 'parts': ['part.hgl']}]}
            (cases / 'cases.json').write_text(json.dumps(manifest))
            (cases / 'main.hgl').write_text('module probe\n')
            (cases / 'part.hgl').write_text('part probe\n')
            def git(*args):
                return subprocess.check_output(['git', '-C', str(root), *args], stderr=subprocess.DEVNULL)
            git('init', '-q')
            git('add', '.')
            git('-c', 'user.name=Fixture', '-c', 'user.email=fixture@example.com',
                'commit', '-qm', 'Frozen fixture sources')
            revision = git('rev-parse', 'HEAD').decode().strip()
            frozen = check.negative_sources(root, revision)
            check.verify_negative_checkout(root, frozen)
            for name in ('main.hgl', 'part.hgl'):
                path = cases / name
                old = path.read_bytes()
                path.write_bytes(old + b'# changed source\n')
                self.assertEqual(check.negative_sources(root, revision), frozen)
                with self.assertRaisesRegex(ValueError, 'checkout source differs'):
                    check.verify_negative_checkout(root, frozen)
                path.write_bytes(old)
            (cases / 'part.hgl').write_text('part changed\n')
            git('add', '.')
            git('-c', 'user.name=Fixture', '-c', 'user.email=fixture@example.com',
                'commit', '-qm', 'Changed part; unchanged cases manifest')
            changed_revision = git('rev-parse', 'HEAD').decode().strip()
            self.assertNotEqual(check.negative_sources(root, changed_revision)['cases'], frozen['cases'])

    def test_pinned_negative_source_inventory_cannot_be_replaced(self):
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory)
            for name in ('provenance.json', 'expected.json'):
                (target / name).write_bytes((HERE / name).read_bytes())
            (target / 'negative_sources.json').write_text('{}')
            with patch.object(check, 'HERE', target):
                with self.assertRaisesRegex(ValueError, 'source inventory changed'):
                    check.check(self.report)

    def test_original_global_parts_missing_extra_hash_order_and_name_rejected(self):
        for summary in self.report['negative_measurements']:
            original=self.negatives[summary['backend']]
            mutations=[lambda r:r.pop('parts'),lambda r:r.update(parts=None),
                       lambda r:r['parts'].append({'name':'foreign.hgl','sha256':'0'*64})]
            if summary['backend']=='rust':
                mutations.extend([lambda r:r['parts'].pop(),lambda r:r['parts'].reverse(),
                                  lambda r:r['parts'][0].update(sha256='0'*64),
                                  lambda r:r['parts'][0].update(name='renamed.hgl')])
            for mutation in mutations:
                report=copy.deepcopy(original);mutation(report)
                with self.subTest(backend=summary['backend'],mutation=mutation),self.assertRaisesRegex(ValueError,'global parts'):
                    check.validate_negative(summary,report,self.manifest)

    def test_global_part_inventory_schema_paths_order_and_digests(self):
        mutations=[lambda p:p.update(rust_revision='0'*40),
                   lambda p:p['backends'].update(cpp=[{'name':'foreign.hgl'}]),
                   lambda p:p['backends']['rust'].pop(),
                   lambda p:p['backends']['rust'].reverse(),
                   lambda p:p['backends']['rust'].append(p['backends']['rust'][0]),
                   lambda p:p['backends']['rust'][0].update(file='../interfaces.hgl'),
                   lambda p:p['backends']['rust'][0].update(name='renamed.hgl'),
                   lambda p:p['backends']['rust'][0].update(sha256='z'*64),
                   lambda p:p['backends']['rust'][0].update(sha256=0)]
        for mutation in mutations:
            parts=copy.deepcopy(self.global_parts);mutation(parts)
            with self.subTest(mutation=mutation),self.assertRaises(ValueError):
                check.validate_global_parts(parts,self.expected['revisions']['rust'])

    def test_global_part_inventory_cannot_be_resealed_with_changed_valid_hash(self):
        with tempfile.TemporaryDirectory() as directory:
            target=Path(directory)
            for name in ('provenance.json','expected.json','negative_manifest.json','negative_sources.json','negative_cpp.json','negative_rust.json'):
                (target/name).write_bytes((HERE/name).read_bytes())
            parts=copy.deepcopy(self.global_parts)
            parts['backends']['rust'][0]['sha256']='0'*64
            data=json.dumps(parts).encode()
            (target/'negative_global_parts.json').write_bytes(data)
            provenance=json.loads((target/'provenance.json').read_text())
            provenance['negative_global_parts_sha256']=check.sha(data)
            (target/'provenance.json').write_text(json.dumps(provenance))
            # Loading a well-formed resealed manifest succeeds, but the
            # unchanged original report independently rejects its false hash.
            with patch.object(check,'HERE',target):
                loaded=check.load_global_parts(self.expected['revisions']['rust'])
            summary=next(r for r in self.report['negative_measurements'] if r['backend']=='rust')
            with self.assertRaisesRegex(ValueError,'global parts differ'):
                check.validate_negative(summary,self.negatives['rust'],self.manifest,global_parts=loaded)

    def test_pinned_global_part_inventory_cannot_be_replaced(self):
        with tempfile.TemporaryDirectory() as directory:
            target=Path(directory)
            (target/'provenance.json').write_bytes((HERE/'provenance.json').read_bytes())
            (target/'negative_global_parts.json').write_text('{}')
            with patch.object(check,'HERE',target),self.assertRaisesRegex(ValueError,'global part inventory changed'):
                check.load_global_parts(self.expected['revisions']['rust'])

    def test_rust_global_parts_git_blobs_and_selected_working_files(self):
        with tempfile.TemporaryDirectory() as directory:
            root=Path(directory)
            for name in check.RUST_GLOBAL_PARTS:
                path=root/name;path.parent.mkdir(parents=True,exist_ok=True)
                path.write_text('part '+Path(name).stem+'\n')
            def git(*args):
                return subprocess.check_output(['git','-C',str(root),*args],stderr=subprocess.DEVNULL)
            git('init','-q');git('add','.')
            git('-c','user.name=Fixture','-c','user.email=fixture@example.com','commit','-qm','Frozen global inputs')
            revision=git('rev-parse','HEAD').decode().strip()
            frozen=check.negative_global_parts(root,revision)
            check.validate_global_parts(frozen,revision)
            check.verify_global_parts_checkout(root,frozen)
            for name in check.RUST_GLOBAL_PARTS:
                path=root/name;original=path.read_bytes();path.write_bytes(original+b'# changed working input\n')
                self.assertEqual(check.negative_global_parts(root,revision),frozen)
                with self.assertRaisesRegex(ValueError,'checkout source differs'):
                    check.verify_global_parts_checkout(root,frozen)
                path.write_bytes(original)
            (root/check.RUST_GLOBAL_PARTS[1]).write_text('part changed\n')
            git('add','.')
            git('-c','user.name=Fixture','-c','user.email=fixture@example.com','commit','-qm','Changed global input')
            changed=git('rev-parse','HEAD').decode().strip()
            self.assertNotEqual(check.negative_global_parts(root,changed),frozen)

    def test_expected_manifest_cannot_be_replaced(self):
        with tempfile.TemporaryDirectory() as folder:
            target = Path(folder)
            (target / 'provenance.json').write_bytes((HERE / 'provenance.json').read_bytes())
            (target / 'expected.json').write_text('{}')
            with patch.object(check, 'HERE', target):
                with self.assertRaisesRegex(ValueError, 'manifest integrity changed'):
                    check.check(self.report)

    def test_original_library_inventory_missing_extra_hash_order_and_name(self):
        for summary in self.report['negative_measurements']:
            mutations=[lambda r:r.pop('libraries'),lambda r:r.update(libraries=None),
                       lambda r:r['libraries'].append({'name':'foreign','files':[]})]
            if summary['backend']=='rust':
                mutations.extend([lambda r:r['libraries'][0]['files'].pop(),
                                  lambda r:r['libraries'][0]['files'].reverse(),
                                  lambda r:r['libraries'][0]['files'][0].update(sha256='0'*64),
                                  lambda r:r['libraries'][0]['files'][0].update(file='renamed.hgl'),
                                  lambda r:r['libraries'][0].update(name='renamed')])
            for mutation in mutations:
                report=copy.deepcopy(self.negatives[summary['backend']]);mutation(report)
                with self.subTest(backend=summary['backend'],mutation=mutation),self.assertRaisesRegex(ValueError,'negative libraries differ'):
                    check.validate_negative(summary,report,self.manifest)

    def test_library_inventory_schema_paths_order_and_fingerprints(self):
        mutations=[lambda p:p.update(stdlib_revision='0'*40),
                   lambda p:p['backends'].update(cpp=[{}]),
                   lambda p:p['backends']['rust'][0].update(root='../hgraph'),
                   lambda p:p['backends']['rust'][0]['files'].reverse(),
                   lambda p:p['backends']['rust'][0]['files'].append(p['backends']['rust'][0]['files'][0]),
                   lambda p:p['backends']['rust'][0]['files'][0].update(file='../foreign.hgl'),
                   lambda p:p['backends']['rust'][0]['files'][0].update(sha256='z'*64)]
        for mutation in mutations:
            inventory=copy.deepcopy(self.libraries);mutation(inventory)
            with self.subTest(mutation=mutation),self.assertRaises(ValueError):
                check.validate_libraries(inventory,self.expected['revisions']['stdlib'])

    def test_resealed_false_library_hash_rejected_by_original_report(self):
        with tempfile.TemporaryDirectory() as directory:
            target=Path(directory)
            inventory=copy.deepcopy(self.libraries)
            inventory['backends']['rust'][0]['files'][0]['sha256']='0'*64
            data=json.dumps(inventory).encode();(target/'negative_libraries.json').write_bytes(data)
            provenance=json.loads((HERE/'provenance.json').read_text())
            provenance['negative_libraries_sha256']=check.sha(data)
            (target/'provenance.json').write_text(json.dumps(provenance))
            with patch.object(check,'HERE',target):loaded=check.load_libraries(self.expected['revisions']['stdlib'])
            summary=next(r for r in self.report['negative_measurements'] if r['backend']=='rust')
            with self.assertRaisesRegex(ValueError,'negative libraries differ'):
                check.validate_negative(summary,self.negatives['rust'],self.manifest,libraries=loaded)

    def test_library_manifest_digest_cannot_be_bypassed(self):
        with tempfile.TemporaryDirectory() as directory:
            target=Path(directory)
            (target/'provenance.json').write_bytes((HERE/'provenance.json').read_bytes())
            (target/'negative_libraries.json').write_text('{}')
            with patch.object(check,'HERE',target),self.assertRaisesRegex(ValueError,'library inventory changed'):
                check.load_libraries(self.expected['revisions']['stdlib'])

    def test_full_library_git_inventory_and_selected_working_inputs(self):
        with tempfile.TemporaryDirectory() as directory:
            root=Path(directory);library=root/'hgl/hgraph'
            for file,text in [('main.hgl','module hgraph.std\n'),('impl/helper.hgl','module hgraph.std\n'),
                              ('native/provider.hgl','module hgraph.native\n')]:
                path=library/file;path.parent.mkdir(parents=True,exist_ok=True);path.write_text(text)
            def git(*args):return subprocess.check_output(['git','-C',str(root),*args],stderr=subprocess.DEVNULL)
            git('init','-q');git('add','.')
            git('-c','user.name=Fixture','-c','user.email=fixture@example.com','commit','-qm','Frozen recursive library')
            revision=git('rev-parse','HEAD').decode().strip()
            frozen=check.negative_libraries(root,revision)
            self.assertEqual(len(frozen['backends']['rust'][0]['files']),3)
            self.assertNotIn('hgl/hgraph/native/provider.hgl',[r['file'] for r in check.source_manifest(root,revision)])
            check.verify_libraries_checkout(root,frozen)
            provider=library/'native/provider.hgl';original=provider.read_bytes()
            for mutation in ('bytes','remove','rename','extra'):
                if mutation=='bytes':provider.write_bytes(original+b'# changed input\n')
                elif mutation=='remove':provider.unlink()
                elif mutation=='rename':provider.rename(library/'native/renamed.hgl')
                else:(library/'extra.hgl').write_text('module extra\n')
                self.assertEqual(check.negative_libraries(root,revision),frozen)
                with self.subTest(mutation=mutation),self.assertRaisesRegex(ValueError,'checkout inputs differ'):
                    check.verify_libraries_checkout(root,frozen)
                if mutation=='rename':(library/'native/renamed.hgl').unlink()
                if mutation=='extra':(library/'extra.hgl').unlink()
                provider.write_bytes(original)
            provider.write_bytes(original+b'# coordinated false inventory\n')
            changed=copy.deepcopy(frozen)
            next(r for r in changed['backends']['rust'][0]['files'] if r['file']=='native/provider.hgl')['sha256']=check.sha(provider.read_bytes())
            check.verify_libraries_checkout(root,changed)
            self.assertNotEqual(check.negative_libraries(root,revision),changed)

    def test_selected_cases_manifest_bytes_must_match_pinned_blob(self):
        with tempfile.TemporaryDirectory() as directory:
            root=Path(directory);cases=root/'compiler/negative_testing';cases.mkdir(parents=True)
            original={'path_base':'manifest_directory','cases':[{'id':'probe','file':'main.hgl','expected_exit':0,'parts':['part.hgl']}]}
            (cases/'main.hgl').write_text('module probe\n');(cases/'part.hgl').write_text('part probe\n')
            manifest_path=cases/'cases.json';manifest_path.write_text(json.dumps(original))
            def git(*args):return subprocess.check_output(['git','-C',str(root),*args],stderr=subprocess.DEVNULL)
            git('init','-q');git('add','.')
            git('-c','user.name=Fixture','-c','user.email=fixture@example.com','commit','-qm','Frozen selected manifest')
            revision=git('rev-parse','HEAD').decode().strip();frozen=check.negative_sources(root,revision)
            check.verify_negative_checkout(root,frozen)
            for mutation in ('exit','parts','extra','remove','whitespace'):
                document=copy.deepcopy(original)
                if mutation=='exit':document['cases'][0]['expected_exit']=1
                elif mutation=='parts':document['cases'][0]['parts']=[]
                elif mutation=='extra':document['cases'].append(dict(document['cases'][0],id='extra'))
                elif mutation=='remove':document['cases']=[]
                text=json.dumps(document)+('\n' if mutation=='whitespace' else '')
                manifest_path.write_text(text)
                self.assertEqual(check.negative_sources(root,revision),frozen)
                with self.subTest(mutation=mutation),self.assertRaisesRegex(ValueError,'checkout manifest differs'):
                    check.verify_negative_checkout(root,frozen)


if __name__ == '__main__':
    unittest.main()
