# Expected errors and source rejection

The specification owns the [error catalogue](../../spec/language/docs/design/error-catalogue.md)
and [shared fixtures](../../spec/compiler/negative_testing/cases.json). A category
such as `type` groups diagnostics; a code such as `rolling.size_kind` identifies
the precise failure. These expectations are established before measurement.

All fixtures use ordinary `hgl test FILE [selectors] --part ...`. An
`# expect-error(...)` annotation creates a source-rejection case alongside
executable tests; there is no rejection command mode.

The schema-2 manifest names the required executed and rejected outcomes.
Mixed cases cover successful rejection, rejection mismatch with continued
execution, runtime failure, selection, nested test contexts, explicit module
parts, and safe syntax recovery. The observer requires every expected outcome
exactly once and checks that rejected or unselected tests never execute.
Runtime-only controls are also source-checked before execution. Mixed source
cannot be preflighted that way because its annotated owners are intentionally
invalid. Admission failures must occur without reported test execution.

The observer preserves raw output and binary, source, part and manifest
fingerprints. Timeouts and abnormal process exits never match. It reads explicit
case outcomes, not diagnostic message wording or aggregate counts.

## Reference boundary

The earlier [negative-duration](../../runtime/validation/generator_negative/README.md)
and [strict-order](../../runtime/validation/generator_ordering/README.md) audits
record Python and native-runtime behaviour, including divergences from the
accepted HGL rules. Their raw observations remain unchanged. They motivate
checking the precise cause: a duplicate-time failure is not evidence that a
negative-duration admission rule was enforced.

The new assertion and source-diagnostic vocabulary is an HGL contract. Python
source cannot test HGL parse or type diagnostics. This campaign runs the shared
HGL sources against both compiler backends and does not relabel historical
Python exceptions with new HGL identifiers.

## Reproduce

Run against built compiler executables and specification `d02ff9b`. The Rust
measurement uses standard-library revision `cbc46df` from its compiler checkout;
set `STD` to that checkout's `external/hgraph_std` directory. The library and backend-part input
fingerprints are retained in the report (the audit's historical `stdlib` pin is unchanged):

```sh
python3 compiler/negative_testing/observe.py --backend cpp \
  --compiler /path/to/hgl --source-revision COMMIT \
  --cases-dir spec/compiler/negative_testing --output /tmp/negative-cpp.json
python3 compiler/negative_testing/observe.py --backend rust \
  --compiler /path/to/hglc --source-revision COMMIT \
  --cases-dir spec/compiler/negative_testing \
  --library "$STD"/hgl/hgraph \
  --part /path/to/rust-checkout/native/stdlib/interfaces.hgl \
  --part /path/to/rust-checkout/native/stdlib/rust.hgl \
  --output /tmp/negative-rust.json
```

`--source-revision` is caller-supplied provenance; the runner independently
fingerprints the executable, fixtures and inputs but does not certify their
build chain. An existing output is never overwritten. Exit zero means every
fixture matched its recorded expectation, including controls expected to fail.


## Measured result

The previous 25-case campaign remains in repository history at `b5b7469`.
The 43 mixed-case expectations passed for C++
`6a23daad104fc4856bae0586b1b44248db29f780` and Rust
`3f1f16dd2bd50bbd5bc0408fe9dc8fc10fc53c5f`. Expected failing controls are included: zero
mismatches does not mean every fixture command returned zero.

The catalogue currently covers two execution codes and six source diagnostic
codes. This evidence does not claim that every language error has a code or
that the compilers implement every possible shape expression. Host test-runner
failures, assertion failures and cleanup failures are not substitute execution
errors. Existing Windows scripted-loader limitations are covered separately
by C++ generated native assertion tests rather than reported as CLI parity.

Check these recorded identities and outcomes without executing a compiler:

```sh
python3 compiler/negative_testing/check.py
python3 -m unittest discover -s compiler/negative_testing
```
