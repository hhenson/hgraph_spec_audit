# Delta pass-through through eval_node

Measured 2026-09-30. Thirty-seven prewritten cases match independent Python and C++ runtimes in three fresh processes each: 32 scalar cases (eight types × four traces), fixed TSB and TSL, TSS bool/int, and integer-key TSD. The compute node executes `return ts.delta_value`; the real `eval_node` wires its replay source and record sink. This is not a graph identity or a synthetic delta simulator.

[Scalar reasoning](scalar-reasoning.md) and the [specification-only review](contract-review.md) were saved before execution. [reasoned.json](reasoned.json) transcribes those literal expectations; observations never generate expectations. The bool set specialization starts with both possible elements and later removes false. The five structural cases measure publication deltas in the reference runtimes; they do not establish HGL collection harness syntax or general invalidation/membership reconstruction. REF designation and same-cycle empty-event fixtures remain explicitly deferred in the corpus.

[observed.json](observed.json) preserves raw returns, independent input-horizon normalization, every observed delta, assessment, package/distribution manifests, native artifact hashes and actual loaded hgraph library hashes. The Python engine is hgraph 0.5.41 under Python 3.14.4, with no native hgraph extension. The C++ engine is an installed development wheel reporting 0.0.0 under Python 3.12.14. Binary and package hashes identify it; this evidence does not claim a published 0.8 release identity. Source checkout context for the wheel was commit `8e899e600089902f9b755f67d9998292fcc03e84`, which alone does not authenticate a built binary.

## Empty and silent outcomes

Both Python-facing `eval_node` implementations return raw `None` for every empty-input or wholly silent scalar case. For a four-position silent input the adapter separately produces four null positions, using only the input length; for empty input it produces an empty list. The raw return remains visible and `padding_added` records the normalization. This is a return-shape difference from HGL's dense contract, not evidence that the runtime created an empty recording. The separate lifecycle probe below directly observes start/stop and post-run recording presence. Sparse interior/trailing silence and repeated equal values match the expected dense traces without adapter padding.

The returned historical deltas remain correct after later updates. The bounded mutable-producer probe below adds direct retention evidence; internal recording-buffer aliases and arbitrary atomic payload ownership remain outside its scope.

## Real replay and recording operators

In Python 0.5.41, `hgraph/test/_node_unit_tester.py` builds a graph containing `replay_from_memory` for each input, the supplied compute, and `record_to_memory` for its output. `hgraph/_impl/_operators/_record_replay_in_memory.py` registers replay as a generator overload of `replay` and record as a sink overload of `record`. The replay key identifies a typed `SimpleArrayReplaySource` seeded by eval; the recorder copies `(evaluation_time, ts.delta_value)` into its recording. Eval retrieves that recording after graph execution and presents its dense result.

The modern Python authoring facade `hgraph/_wiring/_runner.py` wires registered `__harness_replay` and `__harness_record` operators. Their definitions in `python/py_nodes.cpp` delegate to the native `stdlib::replay_impl` and `stdlib::dense_record_impl`. Native `include/hgraph/lib/testing/eval_node.h` likewise wires replay → supplied compute → record, seeds buffers, runs the graph, and extracts the recording. Native `record_replay_memory_impl.h` applies each replay delta and captures the compute output's delta. Names and buffer bridges differ, but the source/compute/sink arrangement is the same. The caller supplies the target and sequences and does not configure those operators.

Python-facing REF results are recorded through a dereferencing value port. An integer-valued REF roundtrip would therefore not establish identity, equal-designation suppression, empty references or rebinding; it was not used as a substitute for the deferred R1 designation trace.

## Replay

Supply independent interpreter paths as private local arguments. Existing environments are not modified. Each run uses a new evidence destination; the runner rejects overwrites and verifies package identity before/after execution.

```sh
python3 runtime/validation/delta_eval/observe.py \
  --python /path/to/python-hgraph/bin/python \
  --cpp /path/to/cpp-hgraph/bin/python \
  --output /tmp/new-delta-observed.json
python3 runtime/validation/delta_eval/check.py
```

[observe.py](observe.py) uses the engine's public `compute_node`, concrete type annotations and `eval_node`. The delta encoding uses actual dates/times/timedeltas, `Removed` set entries, sparse list/bundle maps, and `REMOVE` dictionary entries. It does not replace collection deltas with retained snapshots. `check.py` validates the saved corpus/harness hashes, provenance manifest identity and normalization formula before comparing output deltas. A check of saved evidence is not a fresh runtime measurement.

## Direct native C++ supplement

[native_scalar.cpp](native_scalar.cpp) repeats the 32 scalar traces with a C++ compute calling `out.apply(ts.delta_value())` inside native `testing::eval_node`. Dates use epoch days, time/datetime/duration use exact microseconds in this supplementary JSON encoding. All 32 cases match in three fresh native processes; [native_observed.json](native_observed.json) records the results. Native eval_node returns its own vector, including `[]` for empty input and four null slots for wholly silent four-cycle input; the recording adapter adds no padding. This is a second authoring path into the same C++ runtime, not a third independent runtime.

```sh
cmake -S runtime/validation/delta_eval -B /tmp/delta-native \
  -Dhgraph_DIR=/path/to/sdk/lib/cmake/hgraph \
  -DPython_EXECUTABLE=/path/to/cpp-hgraph/bin/python
cmake --build /tmp/delta-native --parallel 2
python3 runtime/validation/delta_eval/native_observe.py \
  --executable /tmp/delta-native/delta_eval_native \
  --sdk-include /path/to/sdk/include \
  --output /tmp/new-native-observed.json
```

The C++ probe embeds its source SHA256, reports actual loaded library paths privately to the recorder, and the recorder stores names/hashes only. The evidence includes executable identity and a stable SDK header manifest. Local paths and machine details are excluded. Build flags are C++23 and Release; the recorded compiler is GNU C++ 14.3.0. No HGL compilation or structural native-C++ behavior is asserted by the scalar supplement.

## Recorder lifecycle and retained captures

[lifecycle_reasoned.json](lifecycle_reasoned.json) freezes the OP-11/ownership expectations before the separate [lifecycle.py](lifecycle.py) probe. [lifecycle_observed.json](lifecycle_observed.json) preserves raw callback events, external recording presence, post-run mutation observations, and field-by-field disagreement. All runs repeated identically in three fresh processes per engine.

- Both engines invoke the actual recorder's start and stop callbacks for empty and all-silent runs. The graph-stop callback precedes return from eval, so the observed result is extracted after graph stop. No destruction callback was available; this does not assert the exact storage-destruction point.
- The separate [positive-control reasoning](lifecycle_control_reasoned.json) and [observations](lifecycle_control_observed.json) verify key observability before interpreting absence. In the same external GlobalState, `[1,2]` exposes the actual recording key with two entries in both engines; a following all-silent run exposes a present empty recording in Python and no recording key in C++. The original lifecycle evidence was retained unchanged.
- Python's external GlobalState contains an empty recording after recorder stop and after eval. The C++ harness leaves its output key absent after a never-ticking run. The latter disagrees with the prewritten accessible-empty-record expectation in four recorded fields (presence and length, for empty and all-silent inputs). Absence is retained as absence and is not replaced by an empty buffer.
- Lookup during lifecycle callbacks inspects externally supplied GlobalState. The native runtime copies its graph-local state back after execution. Missing external entries during callbacks therefore do not prove missing internal allocation. This probe does not establish before-first-tick public accessibility of the native recorder's storage.
- Three eval calls sharing one GlobalState and output key produce `[1,2]`, then `[3]`, then silence. The second call does not append to the first; the saved first result remains `[1,2]` after later calls. Native no-tick output storage remains absent after the final call.
- A TSD-producing compute reuses and mutates one dictionary on each tick. Captures remain `[{1:10},{1:20},{1:30}]` after later publications, eval return, further mutation of the same producer dictionary and garbage collection. This directly tests retention of these published dictionary deltas. It does not prove arbitrary mutable atomic payload copying or permit clients to retain borrowed endpoint views.

The lifecycle observations are API-specific evidence, not a general resource-capability design or a claim of restart/checkpoint/concurrent-alias behavior. The checker regenerates divergence classifications and rejects relabeling an observed disagreement as a match.

```sh
python3 runtime/validation/delta_eval/lifecycle.py \
  --python /path/to/python-hgraph/bin/python \
  --cpp /path/to/cpp-hgraph/bin/python \
  --output /tmp/new-lifecycle-observed.json
python3 -m unittest discover -s tests -p test_delta_eval.py
```

The positive control can be repeated with `lifecycle_control.py` and the same
`--python`, `--cpp`, and new `--output` arguments used for `lifecycle.py`.

## Multi-input and outputless operator cases

[operator_reasoned.json](operator_reasoned.json) freezes 12 additional expectations from the prewritten [HGL replay/record tests](https://github.com/hhenson/hgraph_std/blob/codex/delta-replay-record-scalars/hgl/hgraph/tests/replay_record.hgl): separate inputs with unequal lengths, an empty required input, string sampling on false trigger ticks, fresh successive evaluations, and outputless sinks. Both engines match all 12 in three fresh processes; [operator_observed.json](operator_observed.json) retains their raw returns, input-derived horizons and engine-identity hashes. These supplement the 37 basic traces above for 49 total cases per engine.

[operator_observe.py](operator_observe.py) runs ordinary compute/sink nodes through the real `eval_node`. The sampling compute tests the trigger's modification rather than its boolean payload. An outputless run is recorded as successful without an output result (`null`); it is never normalized into an empty recording. Empty output-producing runs retain the earlier, separately described dense normalization.

```sh
python3 runtime/validation/delta_eval/operator_observe.py \
  --python /path/to/python-hgraph/bin/python \
  --cpp /path/to/cpp-hgraph/bin/python \
  --output /tmp/new-operator-observed.json
```
