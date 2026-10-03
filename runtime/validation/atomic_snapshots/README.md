# Atomic full snapshots and independent recordings

Measured 2026-10-03 after the rules and case inventory in
[reasoned.json](reasoned.json) and the concrete probe inputs were written.
Eight cases ran in three fresh processes per engine: 48 processes, with two
eval runs per case. The engines are historical Python hgraph 0.5.41 and an
installed native development wheel reporting 0.0.0, both under Python 3.14.4.
[observed.json](observed.json) identifies installed packages, source manifests,
native artifacts and loaded libraries by digest. It is a new measurement,
not a claim that this native wheel is a published release or identical to
earlier audit binaries.

All graphs use a `TS[V]` input, a compute returning `value.delta_value`, and
the real eval recorder. In the proposed HGL mapping this corresponds to an
`atomic<V>` boundary carrying a complete ordinary V. No implementation was
changed and no native build was required. This is Python authoring of each
engine, not a direct C++ expression-order or HGL frontend measurement.

## Full values and publication presence

| Case | Complete payloads exercised |
|---|---|
| Eight-scalar tuple | bool, i64, f64, str, date, time, datetime and duration; includes false, zero and empty text |
| Tuple containing a list | Complete tuple with an independently changing ordinary list member |
| Ordinary integer list | `[1,2]`, silence, `[3]`, `[]`, `[]` |
| Nested ordinary lists | `[[1],[2]]`, silence, `[[3]]`, `[]`, `[]` |
| Shared list at two ticks | The same original `[1,2]` object supplied before and after silence |
| Required-field struct | Complete count and list fields, changing together |
| Defaulted struct | Required bid plus ask defaulting to 7; later explicit ask 9 and an equal repeat |
| List of structs | Complete lists of the defaulted struct, shorter replacement, then empty |

Both engines return the complete supplied snapshots, and the compute's
observed current value and delta are equal to each complete payload. A later
shorter list replaces the earlier list; it is not a sparse index patch.
Defaulted fields are present because ordinary struct construction has already
filled them. Repeated equal values are captured as separate publications.
In particular, both empty-list inputs in the integer-list and nested-list
cases produce observations and recorded empty lists; neither becomes silence.
The probe preserves raw eval output without adding dense padding.

## Retention and the Python discrepancy

The six cases containing mutable lists perform these operations after the
first eval has returned:

1. Mutate the original first input using marker 999, including a nested child
   where appropriate; snapshot the first recording again.
2. Run a second eval using the now-modified input; snapshot both recordings.
3. Mutate the first exported capture using marker 888; snapshot both recordings.

| Observation | Historical Python | Native authoring surface |
|---|---|---|
| Later original-input mutation | Changes the first recording in all six mutable cases | First recording unchanged |
| Second eval and teardown alone | Does not add further changes to the already aliased first recording | First recording unchanged |
| Mutating the first capture when two ticks used the same source object | Changes both captures | Only the chosen exported capture changes |
| Mutating a first-run capture after a second eval | Also changes the second recording in all six mutable cases | Second recording unchanged |

For the shared-list case, the first native recording remains
`[[1,2],null,[1,2]]` after source mutation and the second eval. Changing its
first capture produces `[[1,2,888],null,[1,2]]`; the second recording remains
`[[1,2,999],null,[1,2,999]]`. Python instead reaches
`[[1,2,999,888],null,[1,2,999,888]]` in both recordings.

The scalar-only tuple and frozen scalar-field struct are immutable controls;
their unchanged results are not mutation-based proof of independent storage.
Physical immutable sharing is compatible with HGL's ownership contract.
Python's mutable aliases are preserved as a reference discrepancy. They do
not relax HGL's requirement that recorded ordinary snapshots be independently
retained. Ordinary Python assignment is not HGL owning-value copying.

## Bounded implications for HGL

The next source extension can specify `delta<atomic<V>>` as complete ordinary
V for its admitted finite snapshot payloads. Generic pass-through still
returns `delta_value(value)`, while replay and record retain ordinary timed
values. Atomic payloads use ordinary constructors and their defaults; they
must not be interpreted as sparse structural deltas. Present empty atomic
lists must remain publications without deciding empty *structural-delta*
event semantics.

Generic struct argument admission, inverse inference of a temporal shape
from an erased ordinary payload, fixed-size list identity, redundant atomic
scalar normalization, ordinary retention/error order and HGL syntax are source
contract decisions. This probe neither resolves them through Python typing
nor proposes a runtime shape registry. It supplies full-snapshot and bounded
retention evidence for the language design.

The measured list types are ordinary variable-length lists; no growing
structural time-series list or fixed-size HGL checking claim is added.
All payloads are finite, acyclic ordinary data with primitive or recursively
ordinary children. Optional/null fields, abstract/recursive nominal families,
sets/maps, references, signals, windows, nested temporal boundaries,
allocation failures, writable endpoint access and arbitrary type coverage
are outside this recorded profile. Host-object mutation of returned captures
establishes the measured independence behavior, not new HGL mutation syntax.

## Reproduce

```sh
python3 runtime/validation/atomic_snapshots/observe.py \
  --python /path/to/historical-python/bin/python \
  --cpp /path/to/native/bin/python \
  --output /tmp/new-atomic-snapshots.json
python3 runtime/validation/atomic_snapshots/check.py
python3 -m unittest discover -s runtime/validation/atomic_snapshots
```

The runner refuses to overwrite output and requires stable identity and
identical observations across repetitions. The checker validates complete
provenance and every preserved result, including aliases. It rejects repaired
Python outcomes, missing empty ticks, missing defaults, changed scalar types
and inconsistent native-library hashes. It verifies recorded provenance
consistency, not independent authenticity of a wheel. The aggregate recorded
evidence checker includes these checks without rerunning either engine.
