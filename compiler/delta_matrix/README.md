# HGL delta pass-through coverage

Measured 2026-10-10 against merged compiler revisions. The shared HGL sources
wire `eval` to replay, `pass_through` and record; pass-through returns
`delta_value(value)`. Eval callers supply typed deltas and receive dense results.
References are excluded.

## Covered types

Links select the exact tested standard-library revision.

| Spec type | Covered behavior | HGL evidence |
|---|---|---|
| `bool`, `i64`, `f64`, `str`, `date`, `time`, `datetime`, `duration` | First/equal/distinct publications; leading/interior/trailing silence; wholly silent and empty inputs; scalar atomic normalization | [Scalar cases](https://github.com/hhenson/hgraph_std/blob/3a2e0379f1134f969c850316f828d208af33cbc3/hgl/hgraph/tests/pass_through_scalars.hgl), [atomic equivalence](https://github.com/hhenson/hgraph_std/blob/3a2e0379f1134f969c850316f828d208af33cbc3/hgl/hgraph/tests/atomic_scalar_values.hgl) |
| `civil_datetime`, `timezone`, `zoned_datetime`, `zoned_time` | Exact fields/zone identity; repeated ticks and silence; nested sparse and atomic values; owned timed replay and recordings | `temporal_scalar_values.hgl`, `temporal_structural_values.hgl`, `temporal_retention_values.hgl`, `zoned_time_values.hgl` |
| An enum | Exact nominal/member identity; repeated ticks and silence; sparse children, atomic values, defaults, keys and retained recordings | `enum_values.hgl`, `scalar_key_values.hgl` |
| `set<T>` | Membership additions/removals; scalar and composite keys; cancellation; initial empty tick and silent repeated empties | `pass_through_structural.hgl`, `scalar_key_values.hgl`, `composite_key_values.hgl`, `empty_delta_validity.hgl` |
| `map<K,V>` | Sparse updates; removal/recreation; held siblings; nested children and exact key identity | `recursive_eval_values.hgl`, `composite_key_values.hgl`, `empty_delta_validity.hgl` |
| Fixed `list<T,N>`, growing `list<T>` | Sparse child updates; nested lists; append/shrink/regrow; zero-size fixed shape; independent retained deltas | `pass_through_structural.hgl`, `growing_list_values.hgl`, `empty_delta_validity.hgl` |
| Tuple, concrete struct | Independent positional/field presence; omitted defaults; required unset children; nested structural publications | `pass_through_structural.hgl`, `pass_through_defaults.hgl`, `tuple_observation_values.hgl` |
| `atomic<T>` | Complete replacement including present empties; optional clearing; nested containers; finite recursive trees and closed abstract families; captures survive mutation and later runs | `atomic_eval_values.hgl`, `atomic_set_map_values.hgl`, `optional_atomic_values.hgl`, `recursive_atomic_values.hgl`, `abstract_atomic_values.hgl` |
| `rolling<V,Max,Min>` | Arrival deltas; count/duration bounds; omitted Min equals Max; readiness, retention and timestamps; empty composite arrivals remain publications | `rolling_values.hgl`, `rolling_structural_values.hgl`, `rolling_retention_values.hgl` |
| `signal` input | Observe scalar/structural publications and metadata without payload access | `signal_observation_values.hgl`; signal is input-only, so no signal-output pass-through case is required |
| `delta<T>` ordinary values | Exact originating type; generic batches and independent copies retained through global-state replacement | `delta_identity_values.hgl`, `atomic_replay_values.hgl` |

All filenames above resolve under the [tested HGL sources](https://github.com/hhenson/hgraph_std/tree/3a2e0379f1134f969c850316f828d208af33cbc3/hgl/hgraph/tests).

## Scenarios and failures

[Empty sparse applications](https://github.com/hhenson/hgraph_spec/blob/c0e55d1511f11a798acc07b9e47054c18beef5ae/language/docs/design/empty-delta-validity.md)
cover all six sparse families: an invalid target validates and ticks once;
valid targets ignore subsequent empty applications. Independent observers
check `valid`, `modified`, `all_valid`, timestamps, membership and held payloads.
Explicit nested empty children validate; omitted children stay absent. Child
invalidation/revalidation and preservation of a same-cycle tick are covered.

Payload-read failures use representative integer, boolean and list children;
they are not a separate negative test for every scalar leaf. The standard
module executes four `value.unset_read` assertions and four
`eval.input_delta_profile` assertions, together with successful controls.
The [mixed negative-testing campaign](../negative_testing/README.md) separately
checks source rejection and executable cases in the same script, exact error
codes, selection, and controls that must fail. Its historical observations
remain unchanged; this closeout records fresh Linux executions separately.

## Scope and remaining limits

All type families admitted by the shared eval profile have executable HGL cases.
This is a finite matrix, not every possible generic instantiation or every
combination of scalar leaves and container nesting.

The broader runtime scalar catalogue also names `bytes`, `any` and opaque
native atomic types. They have no shared HGL eval authoring/provider fixtures
in this matrix; they are not certified by these results. Whole-output
invalidation is not a dense replay literal. The HGL tests exercise admitted
child invalidation; native/reference invalidation observations remain separate.
Signal has metadata-only inputs. References remain explicitly outside scope.

## Results and reproduction

See [results.json](results.json) for compiler revisions, dependency pins,
source hashes, exact shared case outcomes and binary fingerprints. The portable
standard module contains 40 files, 258 named tests and 600 authored eval call
sites. These totals include other standard-library smoke tests; they are not
258 distinct pass-through type combinations. Counts are source call sites,
not necessarily the number of dynamic eval invocations.

Check the frozen report from the audit repository root without running a compiler:

```sh
python3 compiler/delta_matrix/check.py
python3 -m unittest discover -s compiler/delta_matrix
```

The checker requires every recorded backend/platform pair, exact shared case
names, empty failure lists, consistent counts and the expected failing negative
controls. [expected.json](expected.json) was independently extracted from the
recorded standard-library and specification Git revisions.
[provenance.json](provenance.json) anchors the original report bytes and this
manifest. The original detailed [C++](negative_cpp.json) and
[Rust](negative_rust.json) negative reports are archived byte-for-byte, with
hashes matching `results.json`. The checker derives exact executed and rejection
outcomes from their original process output using the fingerprinted observer
and [pinned fixture manifest](negative_manifest.json); it checks preflight,
selection, forbidden executions and expected failures before accepting the
summary's match flags. The standard-module raw logs remain represented by their
recorded hashes. This check does not independently establish the compiler build
chain or make a fresh execution claim.

Fresh executions use the compiler repositories, whose CMake presets and Rust
test runner are outside this audit. Start in a directory for sibling checkouts:

```sh
git clone https://github.com/hhenson/hgraph.git hgraph-matrix
git -C hgraph-matrix checkout --detach 7375739918765b82ee119fa15a96efde40f685c7
git clone https://github.com/hhenson/hgl.git hgl-matrix
git -C hgl-matrix checkout --detach 0324243dbfaa7d0568e99eabd30c10ca09d8383d
```

Both compiler revisions pin specification
`c0e55d1511f11a798acc07b9e47054c18beef5ae`, standard library
`3a2e0379f1134f969c850316f828d208af33cbc3` and audit
`6b3c6334188023b26542e1d75c40491f463ae1a3`. Their shared-artifact setup below
initializes those dependencies at the recorded pins.

C++ requires a C++23 toolchain, CMake supporting preset schema 6, Ninja and
Python 3.12 or later with PyArrow 25. Prepare `.venv` at the compiler root with
PyArrow (`python3 -m venv .venv`, then
`.venv/bin/python -m pip install 'pyarrow==25.0.0'` on Unix). The preset selects
that Python executable; on Windows override it with
`-DPython_EXECUTABLE=/path/to/.venv/Scripts/python.exe` and use the platform's
Python launcher. From the directory containing both clones, run the generated
native module in the C++ checkout:

```sh
cd hgraph-matrix
python3 tools/shared_artifacts.py
cmake --preset cpp --fresh -DHGRAPH_BUILD_LANGUAGE=ON
cmake --build --preset cpp --target hgl_std_matrix_tests --parallel
ctest --preset cpp -R '^hgraph_language_generated_standard_matrix$' -V
cd ..
```

C++ passes all 258 shared tests on Linux, macOS and Windows. Rust passes the
same 258 shared tests within 280 executed tests / 679 evaluations on Linux.
Both Linux compilers also match all 43 mixed negative-fixture expectations,
including controls whose expected process exit is nonzero.

Rust requires rustup (the checkout pins Rust 1.98.1), Cargo and Python 3.
From the directory containing both clones, run its source suite in the Rust
checkout. The recorded Rust revision includes `tools/test_hgl.py`:

```sh
cd hgl-matrix
python3 tools/shared_artifacts.py
cargo fetch --locked
python3 tools/test_hgl.py --stdlib
cd ..
```

The Rust suite includes the same 258 standard cases plus native/operator
cases. To verify the stored source manifest against these exact checkout Git
objects, run from the audit repository root (adjust sibling paths as needed):

```sh
python3 compiler/delta_matrix/check.py \
  --stdlib-checkout ../hgraph-matrix/external/hgraph_std \
  --spec-checkout ../hgraph-matrix/external/hgraph_spec \
  --rust-checkout ../hgl-matrix
```

This verifies the recorded revision, regardless of each checkout's current
working files. Fresh negative-fixture executions use
`compiler/negative_testing/observe.py` from the pinned audit dependency and
`external/hgraph_spec/compiler/negative_testing` from the compiler checkout;
use the [observer commands](../negative_testing/README.md#reproduce) with the
compiler revisions and dependency paths above, writing new reports outside
this frozen report. `source_revision_verified_by_runner` remains false: the
negative observer records caller-supplied source revision metadata.

Prior full compiler/runtime gates on all three platforms remain the
acceptance evidence for the implementation changes. This closeout reruns the
shared matrix against merged main; it does not repeat the wheel/SDK gates or
claim new full-runtime coverage.

Negative fixture and part hashes are derived from the pinned Spec Git blobs in
`negative_sources.json` and checked against both original backend reports.
`--spec-checkout` also checks the selected working files against those blobs.
It requires the working `compiler/negative_testing/cases.json` bytes to equal
the pinned Git blob, including expectation metadata and file/part selection.
The compiler revision supplied to the original runners remains unverified.

The ordered command-wide Rust parts, `native/stdlib/interfaces.hgl` and
`native/stdlib/rust.hgl`, are independently derived from tracked blobs at the
pinned Rust revision in [negative_global_parts.json](negative_global_parts.json).
Its provenance digest seals their paths, names, order and hashes; both original
reports must match it, including C++'s empty global-part list. `--rust-checkout`
verifies those Git blobs and the selected working input files, regardless of
checkout HEAD. This input-content proof does not certify the original compiler
binary's build revision. Original reports and measurements remain unchanged.

The complete Rust negative-run library directory inventory is independently
derived from pinned standard-library Git blobs in
[negative_libraries.json](negative_libraries.json). Its provenance digest seals
all 58 ordered relative paths and hashes, including native provider files that
the narrower standard-matrix module selection excludes. The archived Rust
`libraries` array must match exactly, and C++ must retain an empty array.
`--stdlib-checkout` verifies the pinned full inventory and the actual recursive
working `.hgl` inputs, rejecting changes, removals, renames and additional files.
