import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

spec = importlib.util.spec_from_file_location('shared', Path(__file__).resolve().parents[1] / 'tools/shared_artifacts.py')
shared = importlib.util.module_from_spec(spec)
spec.loader.exec_module(shared)


class MaterializationTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        (self.root / 'spec').mkdir()
        (self.root / 'spec/a').write_text('first')
        self.manifest = {'repositories': {'spec': 'spec'}, 'files': {'docs/a': {'repository': 'spec', 'path': 'a'}}}
        self.save()

    def save(self):
        (self.root / 'shared-artifacts.json').write_text(json.dumps(self.manifest))

    def test_update_and_check(self):
        with self.assertRaises(ValueError):
            shared.materialize(self.root, True)
        shared.materialize(self.root)
        shared.materialize(self.root, True)
        (self.root / 'spec/a').write_text('second')
        with self.assertRaises(ValueError):
            shared.materialize(self.root, True)
        shared.materialize(self.root)
        self.assertEqual((self.root / 'docs/a').read_text(), 'second')

    def test_edits_survive(self):
        shared.materialize(self.root)
        (self.root / 'docs/a').write_text('user edit')
        (self.root / 'spec/a').write_text('upstream edit')
        with self.assertRaisesRegex(ValueError, 'edited shared'):
            shared.materialize(self.root)
        self.assertEqual((self.root / 'docs/a').read_text(), 'user edit')

    def test_missing_source_does_not_partially_update(self):
        self.manifest['files']['docs/z'] = {'repository': 'spec', 'path': 'missing'}
        self.save()
        with self.assertRaises(FileNotFoundError):
            shared.materialize(self.root)
        self.assertFalse((self.root / 'docs/a').exists())

    def test_reject_escape(self):
        self.manifest['files'] = {'../outside': {'repository': 'spec', 'path': 'a'}}
        self.save()
        with self.assertRaises(ValueError):
            shared.materialize(self.root)

    def test_reject_symlink_escape(self):
        (self.root / 'docs').symlink_to(self.root.parent, target_is_directory=True)
        with self.assertRaises(ValueError):
            shared.materialize(self.root)

    def test_retire_unchanged_only(self):
        shared.materialize(self.root)
        self.manifest['files'] = {}
        self.save()
        (self.root / 'docs/a').write_text('user edit')
        with self.assertRaisesRegex(ValueError, 'edited retired'):
            shared.materialize(self.root)
        (self.root / 'docs/a').write_text('first')
        shared.materialize(self.root)
        self.assertFalse((self.root / 'docs/a').exists())
