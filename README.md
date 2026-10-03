# hgraph_spec_audit

Executable conformance checks and recorded evidence for
[hgraph_spec](https://github.com/hhenson/hgraph_spec) and
[hgraph_std](https://github.com/hhenson/hgraph_std). Python/C++ examples,
probes, harnesses and measured results live here. HGL inputs come from the
pinned specification and standard library; this repository owns no HGL files. Native implementations of
the standard library remain with their runtime.

## Reproduce recorded evidence

```sh
git clone --recurse-submodules https://github.com/hhenson/hgraph_spec_audit.git
cd hgraph_spec_audit
python3 tools/shared_artifacts.py
python3 tools/check_recorded.py
python3 -m unittest discover -s tests
```

The pinned `spec` and `stdlib` submodules are the source of expected traces
and portable code. Materialized inputs are ignored working files; edit their
owning repository. Existing result identities, historical adapters and
variation reports are retained. The check reproduces the historical fixed-collection failure status (318
unvalidated observations); it does not claim full conformance. A passing
recorded-evidence check is not a fresh runtime measurement.

## Delta evaluation evidence

The [delta eval audit](runtime/validation/delta_eval/README.md) measures actual
replay → compute → record graphs across eight scalar types and five structural
publication-delta cases, with direct native C++ scalar corroboration. It retains
raw no-output returns separately from dense horizon normalization, and records
lifecycle/capture divergences with an external-key positive control.

The [ordinary value-sequence audit](runtime/validation/value_sequences/README.md)
measures timed const-data replay, mutable and immutable lists, retained copies
and the distinct alias behavior of Python objects, native Python exports and
direct native borrowed views.

The [constructor-order audit](runtime/validation/constructor_order/README.md)
measures named scalar argument evaluation and early exceptions on both Python
authoring surfaces, without claiming native C++ expression-order guarantees.

The [timed-value eval audit](runtime/validation/eval_timed_values/README.md)
tests ordinary const timestamp/payload lists for all eight scalar types,
keeping raw output separate from dense horizon materialization.

The [generator operand audit](runtime/validation/generator_operands/README.md)
records operand evaluation and failure traces, retaining differences at the
minimum start-time boundary.

## Exercise the two reference implementations

Both distributions import as `hgraph`, so use independent environments:

```sh
uv venv --python 3.14 .venv-python
uv pip install --python .venv-python/bin/python -r environments/python.txt
uv venv --python 3.14 .venv-cpp
uv pip install --python .venv-cpp/bin/python -r environments/cpp.txt
python3 tools/compare.py --reference .venv-python/bin/python --candidate .venv-cpp/bin/python --output results/local
```

On Windows pass each environment's `Scripts/python.exe`. The runner checks
versions and engine identity, repeats wiring cases in fresh processes, and
writes separate observations, assessment and provenance. It never overwrites
the archived results or derives expectations from observations.

Native C++ probes use an installed hgraph 0.8 SDK:

```sh
cmake -S runtime/validation/fixed -B build/native -DCMAKE_PREFIX_PATH=<sdk>
cmake --build build/native --parallel
ctest --test-dir build/native --output-on-failure
```

[Wiring](runtime/validation/wiring/README.md),
[fixed collections](runtime/validation/fixed/README.md), and
[description boundaries](runtime/validation/descriptions/README.md) document
previous experiments and their exact harness requirements. Historical probes
are retained as evidence; they are not claimed to support every later SDK.
[Compiled-HGL conformance](compiler/stdlib/) checks the current standard library
through an installed compiler/SDK. Other compiler records retain their stated
measurement dates and scope.
The [native-interface audit](compiler/native_interfaces/) owns the C++ to Rust
interface compatibility CI job. It uses public sources and publishes fingerprints
that HGL checks locally, without a C++ build.
The [catalogue](catalogue/) records implementation coverage.
[Relocated implementation notes](docs/implementation-notes/) preserve earlier
compiler status, source references and build guidance; they are historical
context, not fresh conformance results.

Reason first. Compare Python 0.5.x and C++ 0.8.x independently. Reasoning plus
one reference supports acceptance with a variation report. If both references
agree against reasoning, revisit the reasoning. If no pair agrees, obtain an
owner ruling; do not change an expectation to make a run pass. Recorded owner
rulings remain authoritative.

The [released reference audit](results/releases-0.5.42-0.8.30/) records the first
independent run after extraction.
