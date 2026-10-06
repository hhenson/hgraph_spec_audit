# Publication boundaries and separately observed state

Measured 2026-10-06 using historical Python hgraph 0.5.41 and the installed
native development runtime reporting 0.0.0, both on Python 3.14.4. The 18-case
[baseline corpus](reasoned.json) was committed before execution. The six-case
[growing supplement](growing_reasoned.json) was frozen after baseline empty
shape formation but before any growing sequence population or transition.
Each corpus repeated identically in three fresh processes per engine.

[The source-contract review](source-contract-review.md) separates publication
payloads from endpoint state and lists concrete, non-normative source options.
No HGL semantics, compiler, standard library or reference engine is changed.
References and reference-valued children are excluded.

## Observations

| Scenario | Historical Python | Native runtime |
|---|---|---|
| Apply empty set/map twice | First event only | First event only |
| Apply empty fixed list/named struct twice | No event, parent remains invalid | No event, parent remains invalid |
| Zero-child fixed list | No event | Empty assignment fails: unresolved element type |
| Zero-field struct | No event | No event |
| Set add/remove cancellation twice | Two real source events, one copied event | Same |
| Whole scalar/set/map invalidation | Source invalid; copied output retains prior state | Same |
| Whole fixed list invalidation | All children invalid but parent remains valid | Parent and children invalid |
| Whole named struct invalidation | Runtime AttributeError in `_ts_value` access, graph aborts | Parent and children invalid |
| Invalidate fixed/struct/map child | Membership retained, no parent publication; copy keeps valid child | Membership retained, parent publishes empty delta; copy keeps valid child |
| Create map key with invalid child | Source adds key, delta is empty; copy loses new membership | Same |
| Growing list with empty dictionary/sequence | Empty shape forms, no event | Empty shape forms, no event |
| Populate growing list by sequence | Every nonempty sequence fails: expected zero elements | Supported |
| Growing invalid position/suffix | Unobservable after population failure | Source membership grows; delta copy loses invalid position |
| Growing whole/child invalidation | Unobservable after population failure | Copy retains old validity/value |
| Growing trailing removal control | Unobservable after population failure | Explicit removal delta copies length change |
| Distinct structural tuple public marker | Unavailable | Unavailable |

The structural tuple row is a **public authoring-surface limit**, not a claim
that native TSB storage cannot represent positional structures. No atomic
`TS[tuple]` result is substituted for structural-tuple evidence. Named struct
results do not establish source tuple admission or exact tuple delta identity.

The candidate “every explicit empty delta is an event” expectation remains a
disagreement. For set cancellation, upstream state and a sink directly prove
both present empty events; the forwarded output and real recorder both expose
only the first. This localizes suppression to output application. No recorder
normalization is used to infer event absence.

For invalidation/membership cases, the frozen hypothesis deliberately predicts
loss through a guarded publication-only copier. Its matches demonstrate a
limitation of that copy, not successful full-state reconstruction. Native
invalid-child map creation provides a minimal counterexample: source keys are
7, 8, 9; key 9 is invalid; source is valid and modified; publication payload is
`{}`; forwarded keys stay 7 and 8. Native growing `[None]` similarly creates
invalid position 0 and exposes delta `{0: None}` through the reference Python
facade, but the apply path skips that entry. This null is a **reference adapter
payload**, not an admitted HGL invalidation instruction or a silent cycle.

Held-value renderings themselves differ: a historical map input includes an
invalid child as null while the native input omits it. Both have the same
live key membership. Membership/child-validity observations therefore remain
separate from the held value. The producer's output view and downstream input
view are retained separately; their modified flags can differ at invalidation.

## Evidence and execution boundary

[observe.py](observe.py) and [growing_observe.py](growing_observe.py) run public
`compute_node`, output mutation methods, `graph`, `sink_node`, and the real
`eval_node` replay/record graph. A step input drives the producer and a separate
observer after producer and copier. The latter observes both endpoints each
cycle with watched-input validity gating disabled, including idle cycles.
Ungated sinks capture scheduling calls separately from valid+modified events.
The compute forwards only `ts.delta_value` when that guard holds. Neither a
graph identity, synthetic runtime simulator, nor a direct internal TS buffer
probe is used. No runtime files are patched.

[observed.json](observed.json) and [growing_observed.json](growing_observed.json)
retain producer state, input/output state, membership, child validity, sink
calls, guarded event presence/payload, raw eval results, input-derived dense
normalization, errors and field-level assessments. A successful partial field
in an aborted graph does not turn the error into a successful case. Capability
failure is distinct from a silent or empty successful recording.

Each file fingerprints the installed source/package manifest, actual loaded
native libraries, eval implementation, harness, support code and frozen corpus.
The development wheel's version string does not authenticate a release identity;
the artifact hashes identify this measurement. The package identity is checked
before and after each process and matches across both corpora. Private paths
are never provenance fields; exception paths and unstable diagnostic addresses
are redacted, while exception classes and messages remain visible.

No-event eval runs returned raw `None`. Their dense adapter pads to the known
three-step input horizon. This does not prove recorder storage allocation or
that raw `None` means a materialized empty recording. Where events exist,
raw captures agree with the independent forwarded-event sink and cycle state.
The checker verifies those relationships, including false-vs-zero metadata,
empty payload-vs-silence, errors and missing identity. Sixteen negative/control
tests prevent relabeling disagreements and unsupported observations as success.

The state observer does not count every internal notification, establish a
generic event serialization format, or validate every available mutation
spelling. It samples public callback state and public sink scheduling; native
and historical callback behavior are intentionally left distinct. There is
no native-C++ authoring supplement and no cross-platform conformance claim.

## Repeat and check

Pass independent existing interpreters as private local arguments. Each run
requires a new destination and rejects overwriting evidence:

```sh
python3 runtime/validation/publication_boundaries/observe.py \
  --python /path/to/historical/bin/python \
  --cpp /path/to/native/bin/python --output /tmp/new-boundaries.json
python3 runtime/validation/publication_boundaries/growing_observe.py \
  --python /path/to/historical/bin/python \
  --cpp /path/to/native/bin/python --output /tmp/new-growing-boundaries.json
python3 runtime/validation/publication_boundaries/check.py
python3 -m unittest discover -s runtime/validation/publication_boundaries -p 'test_*.py'
```

The offline checker runs through `tools/check_recorded.py`. Checking saved
observations is not a fresh engine measurement. Earlier collection and owned
capture evidence remains unchanged.

Focused validation passed: both new evidence checkers, all 16 new regression
tests, and the existing delta-eval and owned-delta checkers. The repository-wide
recorded-evidence runner was also attempted, but its pre-existing first check
fails because `runtime/validation/assertions.json` is absent from this checkout.
That failure occurs before the new checker and is not converted into a pass.
