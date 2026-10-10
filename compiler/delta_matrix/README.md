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

C++ runs the same generated native module on all three platforms:

```sh
cmake --preset cpp --fresh -DHGRAPH_BUILD_LANGUAGE=ON
cmake --build --preset cpp --target hgl_std_matrix_tests --parallel
ctest --preset cpp -R '^hgraph_language_generated_standard_matrix$' -V
```

C++ passes all 258 shared tests on Linux, macOS and Windows. Rust passes the
same 258 shared tests within 280 executed tests / 679 evaluations on Linux.
Both Linux compilers also match all 43 mixed negative-fixture expectations,
including controls whose expected process exit is nonzero.

Rust reruns its entire source suite on Linux:

```sh
python3 tools/test_hgl.py --stdlib
```

The Rust suite includes the same 258 standard cases plus native/operator
cases. Prior full compiler/runtime gates on all three platforms remain the
acceptance evidence for the implementation changes. This closeout reruns the
shared matrix against merged main; it does not repeat the wheel/SDK gates or
claim new full-runtime coverage.
