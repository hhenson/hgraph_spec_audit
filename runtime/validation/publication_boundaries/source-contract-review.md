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
