# Publication data and state changes

This memo and reasoned.json precede new runtime observations. They identify
expressiveness limits; they do not choose HGL semantics or change an engine.
References and reference-valued children are excluded.

The current HGL accessor requires valid and modified. Whole invalidation
makes the endpoint invalid and therefore falls outside that accessor's
admitted domain. An absence marker means no supplied publication; it cannot
also mean invalidate without changing the contract. Scalar delta reduction
leaves no invalidation tag. A bounded structural delta has sparse valid child
publications (plus collection removal data), not a whole-invalidation tag.

Child invalidation is different from removing a child. Fixed positions and
struct fields remain present; dictionary keys may remain members while their
children become invalid. Omitting that child from a sparse delta means no
publication for the child, not invalidate it. Similarly, creating dictionary
membership with an invalid child has no scalar publication to put in upsert.
Growing-list length and invalid appended positions need equivalent membership
information. These state changes cannot in general be reconstructed from
publication payloads alone. Enlarging the delta algebra or providing a separate
state-change/event contract requires an explicit specification decision.

Present empty data is expressible as an ordinary structural delta. Its storage
is distinct from admitting an endpoint event. Repeated empty publications may
be suppressed by apply even when an upstream endpoint was valid and modified;
existing collection E1 and its downstream control already demonstrate this.
A timestamp around an empty payload does not itself force apply to publish.

Source contracts reviewed: specification `runtime/time_series.md` TS-7 and
TS-26; `runtime/cases_ordinary_delta_types.md` DELTA-DATA;
`library/ordinary_replay_record.md` guarded recording; and audit
`runtime/validation/delta_eval/collection_reasoned.json`,
`collection_control_observed.json`, and `runtime/validation/owned_deltas`.
These separate validity, input notification, modified metadata, publication
data, membership and owned recording. An input notification need not be a
valid modified publication. A compute invocation with required-valid gating
is also not a complete notification counter.

## Measurement design, frozen before execution

Every supported case uses genuine eval_node with an ordinary producer compute,
a compute that returns delta only when valid and modified, and the actual
recorder. An independent per-cycle clock drives an observer with validity
gating disabled, after both producer and forwarded output. It records source
and forwarded state even on invalidation or silence. A separate ungated sink
records source scheduling; its calls are distinguished from valid publication
events. Producer mutation methods are public output APIs.

For invalidation, the hypothesis is that the source loses validity (or the
selected child does), existing membership survives child invalidation, and a
guarded publication-only copy retains the prior valid child. That expected
loss is evidence of insufficient data, not desired full-state replication.
For empty applications, the candidate expectation remains event preservation,
even where earlier evidence predicts disagreement. The corpus will retain
those disagreements. Zero-child fixed shapes are measured separately.

A temporal tuple must not be replaced by atomic TS[tuple] and called equivalent.
If the historical authoring surface cannot form a structural tuple or growing
list, the probe records that capability limit. A lower-level native supplement,
if used, is labeled separately and does not establish historical Python parity.
Raw eval results are preserved. Padding uses only the known input horizon and
never establishes recorder allocation or absence of notifications. JSON null
in a captured payload and null in the dense adapter must not be conflated;
explicit sink entries provide publication counts and recorder raw values remain
separate.

## Narrow source options after measurement

A general event algebra is **not required to test endpoint state**. Existing
explicit handler selectors can drive a separate observer without requiring
the watched input to be valid:

```hgl
fn observe_valid(step: i64, watched: map<i64, i64>) -> bool {
    when modified(step) && valid(step) {
        return valid(watched)
    }
}
```

`valid(step)` expressly narrows validity admission to step. Omitting it would
implicitly require every input and defeat the invalid-state observation.
For a valid map, `contains(watched, 9)` observes membership even when its child
is invalid. `items(watched)` retains child identity, so `valid(child)` within
iteration can return an ordinary scalar invalid-child count. These are
existing source contracts, not proposed new selectors. Keeping the watched
value as a dependency orders the observer after its producer; ticking step
in an otherwise idle cycle exposes held state independently of publications.

Existing `invalidate(out, key)` and `invalidate(out, index)` author map/list
child invalidation. They preserve membership and do not create new children.
Current mutation contracts do not expose these additional producer operations:

- Whole-output invalidation (`invalidate(out)` would be a proposed spelling).
- Named struct or tuple child invalidation.
- Creating a key or appending a position with an initially invalid child:
  current insert/upsert/push require an initializing payload.

A later source extension can admit only the needed mutation operations and
use scalar state observers for conformance. Its precise spelling, preconditions
and notifications remain specification choices. No delta change is necessary
for that testing scope. Creating a valid child and invalidating it in the same
cycle is a distinct experiment, not evidence for creation without an initial
publication.

If full state **recording and replay** are required, there are two larger options:

1. Preserve `delta<T>` as publication data. Add a distinct, explicitly typed
   state-change representation only for the required operations and define
   its independent capture/application API. Existing publication record/replay
   remains publication-only. Merely adding a timestamp or a present flag cannot
   encode invalidation or invalid membership.
2. Redefine the temporal change accessor and delta algebra to include tagged
   invalidation and membership operations. This would change the valid+modified
   read domain and scalar `delta<T> = T` reduction, with broad source-contract and
   generic-code implications. Payload null must not double as invalidation.

These alternatives are not adopted by this audit. The narrow observer/mutation
route is sufficient to validate state without choosing either full-state replay
API. The measurements establish why existing publication replay cannot claim
full-state reconstruction.

Empty publications require a separate decision. The candidate rule “each
supplied empty delta publishes” would change set/map repeat suppression and
would introduce events for fixed/struct shapes that currently remain invalid
when no child has published. It must specify parent validity independently
of child validity, how zero-child structures behave, modified/time metadata,
notification, and how apply preserves an empty event through another output.
An ordinary stored empty delta alone does not settle any of those rules.

Candidate mutation spellings for review (none adopted): `invalidate(out)` for
the whole output; existing `invalidate(out, key/index)` extended with a
compile-time field-name selector for a struct and a constant positional selector
for a tuple; `ensure(out, key)` to create only absent map membership without an
initial child value; and `push_invalid(out)` to append one invalid list child.
A specification could choose different spellings. Typed selector checking and
retention of existing membership/length must be stated explicitly; these do not
imply that arbitrary writable child endpoint expressions are admitted.

The smaller empty-data option is to retain shape-specific application: empty
set/map data can establish a valid empty collection initially, repeated empty
application can be silent, and empty fixed/struct/list data need not publish.
That option preserves the observed application behavior but abandons the
candidate event-preserving expectation for explicit empty records. The other
option is explicit event presence on every application, with parent-validity
and zero-child implications above. Both need an intentional specification
choice; neither follows simply from forming an ordinary empty delta value.
