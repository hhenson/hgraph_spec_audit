# Standard-library conformance

The shared HGL wrappers import `bit_and`, `sample` and `dedup` from the actual
standard library. No node body or native implementation is copied into this
audit. Sources and independently reasoned expectations belong to
[hgraph_spec](https://github.com/hhenson/hgraph_spec/tree/main/compiler/stdlib).

Current results: four scenarios, 23 tick cells match reasoning on Python
0.5.42, C++ 0.8.30 and compiled HGL linked to the installed C++ SDK.
The compiled-HGL evidence was refreshed against the current library pin using
hgraph native-provider commit `540b0976ada30f313975ca90533d6a7bce02b519`;
the earlier released-runtime records remain unchanged. The HGL
run repeats three times in fresh processes. `hgl-reference.json` records actual
ticks, compiler/library fingerprints, shared-source hashes and harness hashes.
The previous blocked compiler experiment has been replaced by this passing
end-to-end check.

From this checkout, after initializing the pinned dependencies:

```sh
python tools/shared_artifacts.py
.venv-python/bin/python -I compiler/stdlib/replay.py --engine python --output results/python-new.json
.venv-cpp/bin/python -I compiler/stdlib/replay.py --engine cpp --output results/cpp-new.json
.venv-cpp/bin/python tools/run_stdlib.py --sdk <installed-sdk> --build-dir build/stdlib --output results/hgl-new.json
python -m unittest discover -s compiler/stdlib
```

Use a full hgraph SDK install containing the compiler and standard library.
The runner requires its installed HGL sources to match the `stdlib` pin and
uses the invoking Python environment for SDK dependency discovery. On Windows,
use the environments' `Scripts/python.exe` paths. Review new results before
replacing the recorded files. Rust-specific tests and fixture generation stay
in the private Rust implementation.
