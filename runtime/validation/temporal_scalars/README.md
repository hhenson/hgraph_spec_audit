# Three additional temporal scalar publications

This audit measures `civil_datetime`, `timezone` and `zoned_datetime` as a
proposed extension to the finite publication profile. The merged
[scalar baseline](https://github.com/hhenson/hgraph_spec/blob/73f03bfa77349bfa284a23eb781e4c79c85eff8a/language/docs/design/ordinary-delta-types.md)
still admits eight scalar leaves; these observations do not admit new HGL
syntax, prove compiler support or change that specification.

[reasoned.json](reasoned.json) and the concrete inputs in [observe.py](observe.py)
were written before measurement. [observed.json](observed.json) records three
identical fresh-process runs for each probe: 60 processes, 105 eval calls.
The native installed development package reports 0.0.0; historical Python
reports 0.5.41. Package/source/native-library digests identify what ran.
No native build or implementation modification was needed.

| HGL name | Native Python authoring type | Measured coverage |
|---|---|---|
| `civil_datetime` | `CivilDateTime` | Distinct civil dates/times, equal repeats, silence, retained lists |
| `timezone` | `ZoneId` | Exact `UTC`/`Europe/London` names; `US/Eastern` remains distinct from `America/New_York` |
| `zoned_datetime` | `ZonedDateTime` | Same instant with UTC offset 0 and London offset 3600; complete identity retained |
| `zoned_time` | No exported `ZonedTime` | Explicitly unavailable in this installed authoring surface |

Historical Python exports none of these four canonical types. Its recorded
probe tests availability only. Naive/aware Python datetimes or custom structs
are not substituted for missing types, so this is not a two-engine parity
result. Export absence bounds this surface, not every possible internal API.

The 17 native cases reuse the [scalar audit](../delta_eval/README.md) patterns:
four traces per type (equal/distinct, leading/interior/trailing silence,
all-silent and empty), two zone/equality controls and three retention controls.
A real `TS[S]` compute returns `delta_value`; the actual eval recorder captures
its output. Current value and delta both contain the complete supplied scalar.
Equal repeats remain publications. Raw all-silent and empty output is `null`;
other raw traces retain input-horizon silence. No output is padded or repaired.
Each case runs a second eval, and the first recording remains unchanged.

For each scalar's retention control, the same ordinary list is supplied at two
ticks. Appending the second scalar to the source changes neither first-run
capture. A second eval sees that appended scalar. Appending to one first-run
capture changes neither its sibling capture nor the second run. This establishes
bounded ordinary-list independence with these scalar leaves, not proof from
immutable-object identity or coverage of arbitrary composites, maps or sets.

The provider probe records exact failure text and phase order: `at_zone`
fails before eval outside `GlobalState`, then fails inside a state without a
timezone provider. It succeeds after `set_time_zone_provider`. After exiting
that state, passing the preconstructed London value through eval still succeeds
and retains its instant, exact zone and offset. This measures construction
versus publication; it does not establish HGL literal validation/preflight
ordering, prove that no provider is consulted internally, or cover changed
provider rules, invalid zones, DST ambiguities or nonexistent civil times.

The bounded next contract is `delta<S> = S` for these three additional leaves,
with existing replay/record/pass-through behavior, equal publications and owning
ordinary captures. Zone aliases and zoned instant/zone/offset identity must be
preserved. Extending structural/atomic payload admission requires a separate
specification decision; these list controls do not prove HGL shape inference.

## Reproduce and check

```sh
python3 runtime/validation/temporal_scalars/observe.py \
  --python /path/to/historical-python/bin/python \
  --cpp /path/to/native/bin/python \
  --output /tmp/new-temporal-scalars.json
python3 runtime/validation/temporal_scalars/check.py
python3 -m unittest discover -s runtime/validation/temporal_scalars
python3 tools/check_recorded.py
```

The observer refuses overwrite and requires all fresh runs and identities to
agree. The checker validates exact observations, unavailable-type boundaries,
provider failures and complete provenance consistency; it does not authenticate
the installed wheel independently. Negative tests reject omitted equal ticks,
filled silence, fabricated dense output, changed offsets/aliases, capture
aliasing, reordered provider phases, unrelated errors and invented Python parity.
