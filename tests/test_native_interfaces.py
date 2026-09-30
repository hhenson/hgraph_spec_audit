"""A changed Rust interface or public input must fail the compatibility check."""
import hashlib
import importlib.util
import json
from pathlib import Path
import tempfile
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
                            hgl_files={'interface.rs': hashlib.sha256(b'expected').hexdigest()})
            def generate(command, **kwargs):
                if command[1] == 'emit-native-rust':
                    Path(command[-1]).write_text('wrong interface')
            with patch.object(audit.subprocess, 'check_output', return_value='revision\n'), \
                    patch.object(audit.subprocess, 'run', side_effect=generate):
                with self.assertRaisesRegex(ValueError, 'missing or changed interface.rs'):
                    audit.check_compiler(manifest, root, root / 'compiler')

    def test_shared_inputs_match_upstream_contract_fingerprints(self):
        manifest = json.loads((ROOT / 'compiler/native_interfaces/contracts.json').read_text())
        for shared, upstream in [
            ('spec/language/examples/const-debug.hgl', 'language/examples/const-debug.hgl'),
            ('spec/language/examples/native-provider.hgl', 'language/tests/codegen/native-provider.hgl'),
            ('stdlib/hgl/hgraph/native/scalar_values_i64.hgl', 'language/stdlib/hgl/hgraph/native/scalar_values_i64.hgl'),
        ]:
            self.assertEqual(manifest['shared_files'][shared], manifest['upstream_files'][upstream])
        audit.verify_files(ROOT, manifest['shared_files'])


if __name__ == '__main__':
    unittest.main()
