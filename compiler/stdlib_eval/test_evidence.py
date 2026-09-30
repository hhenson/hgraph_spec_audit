"""Bind current evidence to the unchanged source corpus and audit adapters."""
import hashlib
import json
from pathlib import Path
import sys
import shutil
import subprocess
import tempfile
import unittest

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from shared_cases import encode, literal, read
from cpp import GROUPS, digest, source_revision, stdlib_sources


class Evidence(unittest.TestCase):
    def test_current_shared_cases_and_all_results(self):
        cases, hashes = read(HERE.parents[1] / 'stdlib/hgl/hgraph')
        self.assertEqual(len(cases),84)
        self.assertEqual(len({(c['module'],c['name']) for c in cases}),45)
        for engine, failures in [('python',[77]),('cpp',[])]:
            report = json.loads((HERE / f'{engine}.json').read_text())
            self.assertEqual(report['sources'],hashes)
            self.assertEqual(report['harness_sha256'],hashlib.sha256((HERE/'replay.py').read_bytes()).hexdigest())
            self.assertEqual(report['reader_sha256'],hashlib.sha256((HERE/'shared_cases.py').read_bytes()).hexdigest())
            self.assertEqual(len(report['cases']),len(cases))
            self.assertEqual([r['index'] for r in report['cases'] if not r['matches']],failures)
            for case,row in zip(cases,report['cases']):
                self.assertEqual(row['function'],case['function'])
                self.assertEqual(row['expected'],json.loads(json.dumps(case['expected'],default=encode)))
                self.assertEqual(row['matches'],row['observed']==row['expected'])
        cpp = json.loads((HERE/'hgl-cpp.json').read_text())
        self.assertEqual(cpp['sources'],stdlib_sources(HERE.parents[1] / 'stdlib/hgl/hgraph'))
        self.assertEqual(cpp['harness_sha256'],digest(HERE / 'cpp.py'))
        self.assertEqual(cpp['reference_revision'],'540b0976ada30f313975ca90533d6a7bce02b519')
        self.assertEqual(len(cpp['native_sources']),5)
        for value in cpp['native_sources'].values():
            self.assertRegex(value, r'^[0-9a-f]{64}$')
        shared = {c['name'] for c in cases}
        observed = {t['name'] for g in cpp['groups'] for t in g['tests'] if t['result']=='ok'}
        self.assertTrue(shared <= observed)
        self.assertTrue(all(g['passed'] for g in cpp['groups']))
        self.assertEqual(cpp['tests'],47)

    def test_implementation_changes_invalidate_compiled_evidence(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            stdlib = HERE.parents[1] / 'stdlib/hgl/hgraph'
            for files in GROUPS.values():
                for file in files:
                    target = root / file
                    target.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copyfile(stdlib / file, target)
            before = stdlib_sources(root)
            target = root / 'impl/control.hgl'
            target.write_text(target.read_text() + '\n# changed implementation\n')
            self.assertNotEqual(before, stdlib_sources(root))
            self.assertEqual(set(before), {file for files in GROUPS.values() for file in files})

    def test_source_revision_rejects_mismatch_and_dirty_checkout(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            def git(*args):
                return subprocess.run(['git', '-C', directory, *args], check=True, capture_output=True)
            git('init')
            (root / 'source.hgl').write_text('module example\n')
            git('add', 'source.hgl')
            git('-c', 'user.name=Audit', '-c', 'user.email=audit@example.invalid', 'commit', '-m', 'fixture')
            revision = source_revision(root)
            self.assertEqual(source_revision(root, revision), revision)
            with self.assertRaisesRegex(ValueError, 'expected revision'):
                source_revision(root, '0' * 40)
            nested = root / 'nested'
            nested.mkdir()
            with self.assertRaisesRegex(ValueError, 'root of a Git checkout'):
                source_revision(nested)
            (root / 'source.hgl').write_text('module changed\n')
            with self.assertRaises(subprocess.CalledProcessError):
                source_revision(root)

    def test_reader_handles_silence_calendar_and_negative_duration(self):
        self.assertEqual(literal('[_, -2, 1.5, true, "a,b"]'),[None,-2,1.5,True,'a,b'])
        self.assertEqual(literal('0us - 1us').days,-1)
        self.assertEqual(literal('@1969-12-31T23:59Z').year,1969)


if __name__ == '__main__': unittest.main()
