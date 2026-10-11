# Reference ownership and scalar capability observations

Reasoned traces were frozen before measurement. Public Python and current
C++ wheel probes run in three fresh processes; the direct C++ probe builds
against a copied installed SDK and also runs in three fresh processes. Source,
package, binary, compiler and SDK fingerprints identify measured artifacts;
installed versions alone do not establish source revisions. All recorded
checker assertions preserve observed divergences rather than silently making
implementation behavior the required result.

| Case | Reasoned result | Observed result |
|---|---|---|
| Save reference to branch-owned producer; branch stops in cycle 3 | `[7, 8, 8, null, null, null]`; logical expiry starts next cycle | C++ public/native `[7, 8, 8, 8, null, null]`; target stays readable until child storage is reused. Python records first three observations then raises `AttributeError`. |
| Save reference through stopped relay to a surviving outer input | `[7, 8, 20, 21, 9, 10]` | Matches both public runtimes and native C++. |
| Alias versus distinct equal-valued endpoints | Same endpoint equals; distinct endpoints differ | Matches both public runtimes and native C++; comparison does not read target values. |
| Boolean scalar capabilities | Equal Boolean values have equal hashes; `false < true` | Matches Python ordinary values and the native C++ scalar operations. Public C++ interpreter Boolean operations are Python ordinary operations, not a second native comparison. |

The owner-expiry expectation follows TS-23's dictionary-child timing together
with GRF-25's logical finalization and the rule that references do not prolong
target lifetime. Generalizing the explicit timing to stopped nested endpoint
owners requires a concise spec clarification. This audit does not claim that
conditional HGL tests already execute or conform. The outer-owner control
shows that stopping a forwarding relay must not invalidate a surviving target.

The captured reference output remains designation-valid after the target
expires; the followed ordinary input becomes invalid. Independent step ticks
separate those observations and allow silence to be checked.
The checker validates both installed engine identities, including package
sources, distribution artifacts and loaded native libraries. The public recorder
fingerprints `delta_eval/observe.py`, `fixed/reference_identity.py` and
`fixed/native_identity.py` before and after measurement; the checker requires
exactly these support dependencies with their current hexadecimal SHA-256 hashes.
For successful captures, every parsed raw published row must match the process-local event
rows exactly, with no missing, extra or duplicated publications. The failed
Python owned-reference capture preserves its partial events and error without
claiming a successful raw result.
Each public engine retains the ordered SHA-256 fingerprints of all three
process payloads, covering its identity and every case. Native repeats cover
the source identity, loaded libraries and all observations; their fingerprints
are also covered by the native measurement seal. The checker requires exactly
three matching fingerprints derived from the recorded payload, rather than
accepting a repeat count alone.
The checker derives the public/native owned assessments from the frozen
next-cycle expiry requirement and checks that both reasoned corpora agree.
Refreshing source fingerprints cannot move expiry to the later observed C++
cycle or turn its divergence into a match. The Python exception remains an
error with three partial events, without padding it into a completed trace.

The native recorder accepts only the executable declared by its configured
`ref_owner_lifetime_native` CMake target. It verifies the supplied SDK package,
three imported archives and exact header search path, then uses
`cmake --build --clean-first` to rebuild that target. A newer executable copied
over the target cannot masquerade as the configured build.
Compile-command selection supports Makefiles, Ninja and Ninja Multi-Config,
including the selected configuration. Source and loaded-library support hashes,
SDK manifests, executable/compiler hashes, build metadata and observations are
sealed together; the checker requires hexadecimal fingerprints and the SDK
artifacts used by this probe. Fresh native measurements reproduce the original
owner-expiry divergence with the same frozen SDK.
Before and after its clean build, the recorder preprocesses the selected source
with the configured command's include/definition options, response files and
inherited environment. Compiler line directives identify every selected
`hgraph` header; a same-named foreign header is rejected, and the selected SDK
header hashes are sealed into the capture and checked against the SDK manifest.
This handles [GCC's search ordering](https://gcc.gnu.org/onlinedocs/gcc/Directory-Options.html)
without assuming that an earlier `-isystem` wins over `-I`. GNU-style
preprocessing and [MSVC `/E` line directives](https://learn.microsoft.com/en-us/cpp/build/reference/e-preprocess-to-stdout)
are supported; missing or unsuccessful header lookup cannot certify a build.
Legitimate dependency directories remain admitted when the compiler selects
the measured SDK's headers.
MSVC command strings retain Windows quoting and path separators. Attached or
separate `/Fo` operands identify the configured target even when the compile
database omits its optional `output` field; conflicting configuration clues
are rejected. The recorder shares `fixed/compiler_identity.py`: GCC/Clang use
`--version`, while bare `cl` supplies its stderr banner. Successful status and
complete stdout/stderr digests are recorded, and the helper bytes are sealed.

Run the evidence-only checker with `python check.py`; run its corruption tests
with `python -m unittest discover -s . -p test_check.py`. Measurement scripts
require independent interpreter paths or an installed SDK/binary, provided
through command arguments; private host paths are not tracked.

```sh
cmake -S runtime/validation/ref_owner_lifetime -B <build> -DCMAKE_PREFIX_PATH=<sdk>
python3 runtime/validation/ref_owner_lifetime/native_observe.py \
  --executable <build>/ref_owner_lifetime_native --sdk <sdk> --build-dir <build> \
  --output <new-native-result.json>
python3 -m unittest discover -s runtime/validation/ref_owner_lifetime
```

For a multi-configuration build, supply its selected artifact, for example
`<build>/Release/ref_owner_lifetime_native`.

The captures and recorders preceding per-process fingerprints remain unchanged
in [the archive](archive/pre-repeat-fingerprints/observed.json), including the
[native capture](archive/pre-repeat-fingerprints/native_observed.json).
Fresh repeats use matching installed runtime/SDK identities and preserve the
Python partial failure and the C++ owner-expiry divergence. Isolated native
build paths may change build metadata without changing the frozen SDK.
The native capture and recorder before selected-header validation, together
with their build helper, remain unchanged in
[their archive](archive/pre-selected-headers/native_observed.json).
The capture and helpers before Windows compiler identity handling remain
unchanged in [their archive](archive/pre-windows-compiler-identity/native_observed.json).
A supplemental Windows Ninja control compiled and preprocessed a temporary
four-header fixture with MSVC. Removing the generated entry's optional
`output` field verified its actual `/Fo` operand; bare-compiler identity capture
also passed. This control supplies no REF runtime observations. The fresh
three-process Linux capture retains the same SDK, compiler, executable, repeat
digests and owner-expiry divergence.
