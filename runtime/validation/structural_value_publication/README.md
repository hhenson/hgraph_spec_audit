# Ordinary structural values at an output boundary

Measured 2026-10-08, separately from ordinary tuple construction. The candidate
HGL rule reconciles an output with an ordinary retained value's membership and
child validity, while `delta<T>` remains sparse application. Existing HGL text
calls a return a complete-output assignment but does not spell out these state
transitions. The observations below inform an intentional source decision;
they are not evidence that existing return paths already implement it.

## Distinct measured surfaces

Twenty public-authoring cases run three times in fresh processes under Python
hgraph 0.5.41 and a frozen C++ development wheel reporting 0.0.0, both on Python
3.14.4. The four scenarios are named-struct and fixed-list selection from a
complete A to a separately partial B, map removal leaving a valid sibling key,
and invalidation of an existing map child with another valid child retained.
Each scenario separately exercises:

- Returning an independently copied current Python value.
- Assigning that retained value through `_output.value`.
- Calling `_output.copy_from_input(source)` directly.
- Calling `_output.copy_from(source)` directly, without fallback.
- A guarded raw-delta return as a distinct control.

An independent step drives transfers and state observers for all three cycles,
including an idle source cycle. Source A and B have separate endpoints; B never
held A's second child. Endpoint membership and child validity are observed
independently from aggregate value rendering. The real `eval_node` recorder,
raw returned deltas, per-cycle states and event sink observations are retained.

| Operation | Python package | C++ Python facade |
| --- | --- | --- |
| Return retained current value | Retains old child values and absent map keys | Same |
| Assign retained current value | Retains old child values and absent map keys | Same |
| `copy_from_input` | Reconciles all four observed scenarios | AttributeError: method unavailable |
| `copy_from` | AttributeError: method unavailable | AttributeError: method unavailable |
| Raw-delta control | Explicit map removal propagates; omitted invalid children keep prior output values | Same |

The historical named-struct **output** `all_valid` getter raises an
AttributeError. That query error is recorded separately rather than aborting
the graph or replacing the getter with a derived Boolean. Child-state
observations still distinguish the transitions; the assessment retains both
the state result and accessor error. Both packages lack a public structural
TST marker. Atomic `TS[tuple]` is not substituted.

## Genuine native value-copy supplement

A separate installed-SDK graph constructs an owning `Value` from the chosen
input's held value and calls `TSDataMutationView.copy_value_from`. A step-driven
node records source/output child state independently. This is neither Python
value assignment nor the historical endpoint-copy operation. Three fresh
processes agree:

| Scenario | Native source/retained ordinary value at step 2 | Output after native value copy |
| --- | --- | --- |
| Named-field bundle | `{left:30,right:null}` in both views | Right stays valid with 20: copy does not invalidate it |
| Fixed list | Source view already exposes `[30,0]` despite invalid child 1; retained value is identical | Child 1 becomes valid with 0 |
| Map removal | `{7:10}` in both views | Key 8 is removed |
| Map child invalidation | Source view already exposes `{7:10,8:20}` despite invalid child 8; retained value is identical | Child 8 stays valid with 20 |

Thus the fixed-list and map-invalid cases lose child-state information at the
held-value observation boundary before owning retention or output application.
The named-struct case preserves nil through retention but not publication.
Do not attribute all three differences to the final copy operation. The
C++ Python map rendering also omits invalid keys; it is a different surface
from this native view and from independently observed live membership.

Full reconciliation is supported by reasoning and the historical endpoint-copy
surface; native whole-value copying additionally corroborates map removal.
The contrary paths remain variations. These probes neither prescribe backend
APIs nor claim structural-tuple, empty/zero-child, last-valid-child, whole-
invalidation, new-invalid-membership or empty-event-forwarding conformance.
They do not test arbitrary failures during ownership or output mutation.

## Evidence and reproduction

`reasoned.json` and `native_reasoned.json` were written before their respective
measurements. Evidence records package/source manifests, loaded native library
hashes, SDK header hashes, compiler flags, executable identities and harness
hashes. The development version is not a released-version identity. Private
paths are excluded or redacted. No compiler or runtime implementation was
changed.

```sh
python3 runtime/validation/structural_value_publication/observe.py \
  --python /path/to/python-hgraph/bin/python \
  --cpp /path/to/cpp-hgraph/bin/python --output /tmp/structural-value.json
cmake -S runtime/validation/structural_value_publication -B /tmp/structural-value-native \
  -Dhgraph_DIR=/path/to/sdk/lib/cmake/hgraph \
  -DPython_EXECUTABLE=/path/to/cpp-hgraph/bin/python -DCMAKE_BUILD_TYPE=Release
cmake --build /tmp/structural-value-native --parallel 2
python3 runtime/validation/structural_value_publication/native_observe.py \
  --executable /tmp/structural-value-native/structural_value_publication_native \
  --sdk-include /path/to/sdk/include --build-dir /tmp/structural-value-native \
  --output /tmp/structural-value-native.json
python3 runtime/validation/structural_value_publication/check.py
python3 -m unittest discover -s runtime/validation/structural_value_publication
```

Runners require new output destinations. Offline checks preserve divergence,
missing-method errors, nil-versus-zero distinctions and missing retention
observations; passing those checks is not a new runtime measurement.
