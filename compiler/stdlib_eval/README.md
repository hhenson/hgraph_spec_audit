# Current standard-library eval conformance

Pinned hgraph_std `9bd7a26`: **45 tests, 84 dense eval assertions**. Expectations
are read directly from the unchanged HGL files; this audit contains no HGL copy.
The shared language guide defines dense alignment, silence and strict length.

| Check | Result |
|---|---|
| HGL compiled and run by C++ | All 45 shared tests pass; 2 additional upstream native-view tests pass |
| C++ engine through Python authoring | 84/84 traces match |
| Python 0.5.42 | 83/84 traces match; `sum_reset` variation below |

The C++ compiler and wheel use hgraph commit
`540b0976ada30f313975ca90533d6a7bce02b519` (native-provider PR #1669).
The wheel labels itself `0.0.0`; its binary hash identifies the actual build.
The compiled-HGL run validates native C++ scalar functions and sink effects.
Python-authoring runs exercise released operators where available. Embedded
native tests lift independent Python scalar operations into compute nodes;
three temporal projections missing in Python 0.5.42 use explicit compute nodes.
Set producers are Python-authored, with released contains/len consumers. The
three diagnostic wrappers compare passthrough ticks only in these two runs.
Every row labels its adapter; these checks are not interchangeable. Authoring
results are padded only to the input horizon when the runtime omits trailing
silence. Expectations never determine that length.

## Reasoning

- Native scalar lifts wait for all inputs, then evaluate whenever any input
  ticks. Arithmetic, string slicing and calendar components use the documented
  scalar result; an absent input cell contributes no delta.
- Sources publish once at the requested delay. `nothing` stays silent. Default
  follows its fallback until the primary is valid, then follows the primary.
- Sample wakes only for its trigger. Drop counts ticks, take/freeze/until_true
  passivate at their stopping condition. Dedup compares the last emitted value;
  filter emits the latest unseen value when reopened.
- Folds retain their own state. Reset runs before addition in a simultaneous
  cycle and can emit zero before a first value. Set duplicates do not change
  membership; element iteration exposes bool values, not storage keys.
- Date component wrappers deduplicate unchanged values. Instant component
  wrappers preserve input ticks. Duration fields use normalized remainders.

These rules explain the existing shared expectations. C++ execution confirms
all of them; the accepted Python variation does not alter an expected trace.
The Rust implementation records its own engine validation in its repository.
Updating the library pin also reran the four existing compiled-HGL regression
scenarios (23 cells) against the matching C++ SDK, three times with identical
results; `compiler/stdlib/hgl-reference.json` contains the refreshed evidence.

## Accepted variation: reset before addition

`hgraph.std::folds_and_reset_before_first_value`, `reset_integer`:

| | Dense cells |
|---|---|
| Input | `_, 2, 3, _, 1` |
| Reset | `true, _, false, false, _` |
| Reasoned / HGL C++ / C++ operator | `0, 2, 3, 0, 1` |
| Python 0.5.42 | `_, 2, 0, 0, 1` |

Reset is triggered by a reset *tick*, including false. At cycle 0 it publishes
zero with no input value. At cycle 2 it clears the accumulator before adding
3. Python requires input validity and gives reset precedence over simultaneous
addition. Accept the shared result under the agreed two-way alignment rule;
retain this difference for Python review.

## Reproduce

```sh
python tools/shared_artifacts.py
<python-runtime> compiler/stdlib_eval/replay.py --engine python \
  --stdlib stdlib/hgl/hgraph --output results/python-eval.json
<cpp-runtime> compiler/stdlib_eval/replay.py --engine cpp \
  --stdlib stdlib/hgl/hgraph --output results/cpp-eval.json
python compiler/stdlib_eval/cpp.py --source <hgraph-source> --build <hgraph-build> \
  --stdlib stdlib/hgl/hgraph --revision <hgraph-commit> --output results/hgl-cpp-eval.json
python -m unittest discover -s compiler/stdlib_eval
```

Build `hgl_stdlib_test_driver` with language/testing enabled. Its linked native
provider and generated descriptor must match the supplied source and build.
`shared_cases.py` accepts the current flat scalar assertion syntax and fails
on unrecognized values. It is an audit reader, not another HGL compiler.
