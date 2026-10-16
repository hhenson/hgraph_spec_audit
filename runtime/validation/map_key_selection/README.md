# Live map key selection evidence

The owner-selected [MAP-CONN contract](../../../spec/language/docs/design/map-key-connections.md)
is frozen at Spec `b6bcc26`, based on main
`a7d42059b0ba51bf190f13f344419ec228c3551a`. It composes TS-11/14/16/17/23
with the merged LOOKUP-1–4 rules. `reasoned.json` was written before these
measurements; expected rows were not changed to match observations.

Five public-engine graph cases measure membership, equal-payload retargeting,
missing keys before first map publication, invalidation without removal and a
held designation through removal/reinsertion. Columns are named in the frozen
corpus. The observer activates on an independent step input. Membership reads
the published key set: merely wiring a selected input may create a routing
stub, so input-container membership alone is not the observation boundary.
A held REF output and scalar latch save the first readable child; no ordinary
REF state storage or new reference constructor is modeled.

Four additional cases execute compute nodes reading real `TS[dict[str,int]]`
inputs: safe presence/null, exact non-null fallback, present strict lookup and
absent strict lookup. Present zero is distinct from absence. A JSON string
encodes each successful observation, preserving published null separately from
silence. Strict failure requires an actual callback `KeyError` record before
the driver exception; a graph-construction error cannot substitute for it.
These public bridge controls establish neither the HGL error code nor native
SDK nullable-storage behavior.

| Boundary | Python 0.5.41 | Installed C++ interpreter |
|---|---|---|
| Membership, initial unpublished map | Matches | Matches |
| Equal-valued targets and missing-key changes | Repeated absent key ticks the equal empty REF at row 3 | Matches, including empty deduplication |
| Present child invalidated without removal | Matches: child remains a member, REF unchanged, ordinary input invalid/unmodified | Row 2 reports ordinary `modified=true`, required false |
| Held designation, removal cycle, expiry, later reinsertion | First five rows match through removal; then `AttributeError: 'NoneType' object has no attribute 'graph'`. Remaining three rows unvalidated | All eight rows match; old child expires and does not retarget |
| Four scalar-dictionary controls | Matches | Matches |

The invalidated ordinary scalar has producer timestamp NEVER and is unmodified
under TS-7; TS-14 clears the former peer sample. The fixed assembled-child
exception does not apply. The C++ modified flag remains a recorded divergence.
Python's repeated empty designation and expiry failure remain divergences,
with partial rows preserved. Successful C++ expiry does not validate the
unobserved Python suffix. Owner-selected empty coalescing and expiry agree
with existing TS-16/23 and the C++ observations.

Each engine ran three independent fresh processes with identical full payloads.
Both used Python 3.14.4; Python hgraph was independently installed at 0.5.41.
The development C++ wheel reports distribution version 0.0.0. Loaded source,
package and native-library hashes identify execution in `observed.json`.
`provenance.json` records owner-verified native source/tree context separately;
that context is not an artifact hash or direct SDK execution claim.

This is public Python/interpreter-bridge evidence, not HGL compilation or direct
native SDK evidence. It does not measure outer `ref<map<K,V>>` composition,
REF-valued children, same-cycle restoration, unreadable keys, whole-map
invalidation or temporal safe-lookup defaults. Their Spec scope is separate.

`history/2026-10-13/` preserves the original three-case inputs, probe and raw
record byte-for-byte, with hashes in `provenance.json`. That probe is an archive
at its original relative-import location, not a runnable script at its new
history location. Its narrower observations are not replaced by this run.

```sh
python3 runtime/validation/map_key_selection/check.py
python3 -m unittest discover -s runtime/validation/map_key_selection
python3 runtime/validation/map_key_selection/observe.py \
  --python <independent-python-interpreter> \
  --cpp <installed-native-interpreter> --output <new-evidence-file>
```

The checker verifies source/support hashes, engine identities, process digests,
raw-to-observer consistency, strict callback failure and the exact recorded
variations. Corruption tests attempt to silently repair divergences, discard
held values, erase equal-target samples and conflate published null with silence.
No verification command reruns a runtime or rewrites the evidence.
