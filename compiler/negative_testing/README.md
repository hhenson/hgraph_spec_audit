# Expected errors and source rejection

The specification owns the [error catalogue](../../spec/language/docs/design/error-catalogue.md)
and [shared fixtures](../../spec/compiler/negative_testing/cases.json). A category
such as `type` groups diagnostics; a code such as `rolling.size_kind` identifies
the precise failure. These expectations are established before measurement.

The fixtures exercise matching execution errors and continuation, nested
assertions, source rejection and controls that must fail. Runtime controls are
source-checked separately so a compiler rejection cannot stand in for an
executed failing test; failing controls must also report a named test failure. Timeouts and abnormal process exits never match.
The observer preserves output, binary and source fingerprints, and mismatches;
it does not infer error identifiers from human-readable messages.

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

Run against built compiler executables and specification `4c5a22d`. The Rust
measurement uses standard-library revision `0cd99ff` from its compiler checkout;
set `STD` to that checkout's `external/hgraph_std` directory. The four input
fingerprints are retained in the report (the audit's historical `stdlib` pin is unchanged):

```sh
python3 compiler/negative_testing/observe.py --backend cpp \
  --compiler /path/to/hgl --source-revision COMMIT \
  --cases-dir spec/compiler/negative_testing --output /tmp/negative-cpp.json
python3 compiler/negative_testing/observe.py --backend rust \
  --compiler /path/to/hglc --source-revision COMMIT \
  --cases-dir spec/compiler/negative_testing \
  --part "$STD"/hgl/hgraph/replay_record.hgl \
  --part "$STD"/hgl/hgraph/impl/replay_record.hgl \
  --part "$STD"/hgl/hgraph/control.hgl \
  --part "$STD"/hgl/hgraph/impl/control.hgl \
  --output /tmp/negative-rust.json
```

`--source-revision` is caller-supplied provenance; the runner independently
fingerprints the executable, fixtures and inputs but does not certify their
build chain. An existing output is never overwritten. Exit zero means every
fixture matched its recorded expectation, including controls expected to fail.


## Measured result

All 25 shared cases matched their expected outcomes on Linux for C++
`83fd507556b6c9c91d8af2d69a3edaf547962c0e` and Rust
`d9a35cf0df76b3d4b0df7786342f817be5bf1a75`. This includes expected failures:
zero mismatches does not mean every fixture command returned zero.

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
