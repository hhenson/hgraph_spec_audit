"""A changed Rust interface or public input must fail the compatibility check."""
import hashlib
import importlib.util
import json
from pathlib import Path
import tempfile
import shutil
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location('native_interfaces', ROOT / 'compiler/native_interfaces/check.py')
audit = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(audit)


class NativeInterfaces(unittest.TestCase):
    def test_local_fingerprints_reject_missing_or_changed_files(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            output = root / 'interface.rs'
            output.write_text('pub trait Native {}\n')
            files = {'interface.rs': hashlib.sha256(output.read_bytes()).hexdigest()}
            audit.verify_files(root, files)
            output.write_text('pub trait Changed {}\n')
            with self.assertRaisesRegex(ValueError, 'missing or changed interface.rs'):
                audit.verify_files(root, files)
            output.unlink()
            with self.assertRaises(ValueError):
                audit.verify_files(root, files)

    def test_changed_generated_interface_fails(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            manifest = dict(hgraph_revision='revision', upstream_files={}, rust_toolchain='1.98.1',
                            contracts=[dict(interface='shared.hgl', implementation='impl.hgl', rust_file='interface.rs')],
                            historical_interface_files={'interface.rs': hashlib.sha256(b'expected').hexdigest()})
            def generate(command, **kwargs):
                if command[1] == 'emit-native-rust':
                    Path(command[-1]).write_text('wrong interface')
            with patch.object(audit.subprocess, 'check_output', return_value='revision\n'), \
                    patch.object(audit.subprocess, 'run', side_effect=generate):
                with self.assertRaisesRegex(ValueError, 'missing or changed interface.rs'):
                    audit.check_compiler(manifest, root, root / 'compiler')

    def test_shared_inputs_preserve_abi_and_scoped_migrations(self):
        manifest = json.loads((ROOT / 'compiler/native_interfaces/contracts.json').read_text())
        scalar = 'stdlib/hgl/hgraph/native/scalar_values_i64.hgl'
        self.assertEqual(manifest['shared_files'][scalar],
                         manifest['upstream_files']['language/stdlib/hgl/hgraph/native/scalar_values_i64.hgl'])
        audit.verify_files(ROOT, manifest['shared_files'])
        audit.verify_source_migrations(ROOT, manifest)

    def migration_fixture(self, directory):
        root = Path(directory)
        manifest = json.loads((ROOT / 'compiler/native_interfaces/contracts.json').read_text())
        files = [manifest['historical_sources']] + [m['shared'] for m in manifest['source_migrations']]
        for name in files:
            target = root / name
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(ROOT / name, target)
        return root, manifest

    def test_native_declaration_change_cannot_hide_behind_new_fingerprint(self):
        with tempfile.TemporaryDirectory() as directory:
            root, manifest = self.migration_fixture(directory)
            migration = manifest['source_migrations'][1]
            path = root / migration['shared']
            path.write_text(path.read_text().replace('native const fn audit(value: i64)',
                                                     'native const fn audit(value: bool)'))
            changed = hashlib.sha256(path.read_bytes()).hexdigest()
            manifest['shared_files'][migration['shared']] = changed
            manifest['hgl_files'][migration['hgl']] = changed
            with self.assertRaisesRegex(ValueError, 'beyond capability access spelling'):
                audit.verify_source_migrations(root, manifest)

    def test_non_call_body_change_is_not_a_syntax_migration(self):
        with tempfile.TemporaryDirectory() as directory:
            root, manifest = self.migration_fixture(directory)
            path = root / manifest['source_migrations'][0]['shared']
            path.write_text(path.read_text().replace('const_(42)', 'const_(43)'))
            with self.assertRaisesRegex(ValueError, 'beyond capability access spelling'):
                audit.verify_source_migrations(root, manifest)

    def test_clock_call_aliases_cannot_replace_property_access(self):
        for alias in ('clock.evaluation_time()', 'evaluation_time(clock)'):
            with self.subTest(alias=alias), tempfile.TemporaryDirectory() as directory:
                root, manifest = self.migration_fixture(directory)
                migration = manifest['source_migrations'][1]
                path = root / migration['shared']
                path.write_text(path.read_text().replace('return clock.evaluation_time',
                                                         'return ' + alias))
                changed = hashlib.sha256(path.read_bytes()).hexdigest()
                manifest['shared_files'][migration['shared']] = changed
                manifest['hgl_files'][migration['hgl']] = changed
                with self.assertRaisesRegex(ValueError, 'beyond capability access spelling'):
                    audit.verify_source_migrations(root, manifest)

    def test_original_source_cannot_be_updated_to_current_syntax(self):
        with tempfile.TemporaryDirectory() as directory:
            root, manifest = self.migration_fixture(directory)
            migration = manifest['source_migrations'][1]
            path = root / manifest['historical_sources']
            archive = json.loads(path.read_text())
            archive['sources'][migration['upstream']] = (root / migration['shared']).read_text()
            path.write_text(json.dumps(archive))
            with self.assertRaisesRegex(ValueError, 'changed historical source'):
                audit.verify_source_migrations(root, manifest)

    def test_migration_coverage_cannot_drop_a_source(self):
        manifest = json.loads((ROOT / 'compiler/native_interfaces/contracts.json').read_text())
        manifest['source_migrations'].pop()
        with self.assertRaisesRegex(ValueError, 'incomplete source migration coverage'):
            audit.verify_source_migrations(ROOT, manifest)

    def test_historical_abi_cannot_be_relabelled_as_current(self):
        manifest = json.loads((ROOT / 'compiler/native_interfaces/contracts.json').read_text())
        rust_file = manifest['contracts'][0]['rust_file']
        manifest['hgl_files'][rust_file] = '0' * 64
        with self.assertRaisesRegex(ValueError, 'current ABI differs'):
            audit.verify_source_migrations(ROOT, manifest)


if __name__ == '__main__':
    unittest.main()
