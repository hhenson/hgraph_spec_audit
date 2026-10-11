"""Cold compiler profiles validate status and preserve complete stream identity."""
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch

from compiler_identity import capture_compiler_identity, validate_compiler_identity


class CompilerIdentityTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.compiler = self.root/'cl.exe'
        self.compiler.write_bytes(b'compiler fixture')
        self.stdout = b'usage: cl [ option... ] filename... [ /link linkoption... ]\n'
        self.stderr = (b'Microsoft (R) C/C++ Optimizing Compiler Version 19.51.36256 for x64\n'
                       b'Copyright (C) Microsoft Corporation.  All rights reserved.\n\n')

    def capture(self, returncode=0, stdout=None, stderr=None):
        result = subprocess.CompletedProcess([],returncode,self.stdout if stdout is None else stdout,
                                             self.stderr if stderr is None else stderr)
        with patch('compiler_identity.subprocess.run',return_value=result) as run:
            identity = capture_compiler_identity(self.compiler)
        return identity,run

    def test_msvc_no_input_banner_and_streams(self):
        identity,run = self.capture()
        self.assertEqual(run.call_args.args[0],[str(self.compiler)])
        self.assertEqual(identity['compiler_identity']['profile'],'msvc-no-input')
        validate_compiler_identity(identity)

    def test_msvc_nonzero_status_and_missing_banner_rejected(self):
        cases=[{'returncode':2}, {'returncode':1}, {'stderr':b''}]
        for case in cases:
            with self.subTest(case=case),self.assertRaises(ValueError):self.capture(**case)

    def test_msvc_stream_identity_is_complete_and_language_independent(self):
        original,_=self.capture()
        localized,_=self.capture(stdout='lokalisierte Verwendung\n'.encode(),
                                 stderr='lokalisierte Compilerversion\nweitere Ausgabe\n'.encode())
        validate_compiler_identity(localized)
        for field in ('stdout_sha256','stderr_sha256'):
            self.assertNotEqual(original['compiler_identity'][field],localized['compiler_identity'][field])
        warning,_=self.capture(stderr=self.stderr+b'cl : Command line warning D9002 : detail\n')
        self.assertNotEqual(original['compiler_identity']['stderr_sha256'],warning['compiler_identity']['stderr_sha256'])

    def test_gcc_and_clang_keep_version_invocation(self):
        for name in ('c++','clang++','clang-cl.exe'):
            self.compiler=self.root/name
            self.compiler.write_bytes(b'compiler fixture')
            identity,run=self.capture(stdout=b'compiler version 1\n',stderr=b'')
            self.assertEqual(run.call_args.args[0],[str(self.compiler),'--version'])
            self.assertEqual(identity['compiler_identity']['profile'],'version')
            validate_compiler_identity(identity)

    def test_compiler_bytes_cannot_change_during_capture(self):
        def mutate(*args,**kwargs):
            self.compiler.write_bytes(b'replacement compiler')
            return subprocess.CompletedProcess([],0,self.stdout,self.stderr)
        with patch('compiler_identity.subprocess.run',side_effect=mutate),self.assertRaises(RuntimeError):
            capture_compiler_identity(self.compiler)


if __name__=='__main__':unittest.main()
