# Eval recorder-key collisions

Measured 2026-10-03 after [reasoned.json](reasoned.json) was written. Six
cases ran in three fresh processes each on historical Python hgraph 0.5.41
and the current native development wheel reporting 0.0.0: 36 processes.
[observed.json](observed.json) records package/source/binary identities,
actual keys, exported element types, hook snapshots, raw results and errors.
It adds no padding and repairs no corrupted result. No published-version
native parity claim is made.

The prewritten desired ownership rule is that eval should preserve its
output while leaving source-owned state intact, even when a source chooses
the recorder's current string key. That is a proposed HGL requirement, not
an assertion that existing implementations already guarantee isolation.

## Exact keys and ordinary types

| Surface | Output key | Sparse storage | Dense storage |
|---|---|---|---|
| Historical Python | `nodes.record.out` | `list[tuple[datetime,int]]` | `list[tuple[datetime,int]]` |
| Current native authoring surface | `eval_node::out` | `list[tuple[datetime,int]]` | `list[int]` |

Each write uses the same logical exported element type as that recorder.
There is no deliberately wrong-type scalar assignment. Python class names
are not evidence of an unseen native canonical schema name, and this probe
does not add a runtime schema inspection API. Sparse mode uses the real
`eval_node(..., __elide__=True)` recorder; its raw return contains payloads
while the retained state exposes timestamp/payload tuples.

All inputs are `[1,2]`. The unrelated control writes `audit.user.recording`.
Collision cases write the exact output key: a seed containing 700, start
containing 701, each evaluation containing 901 then 902, or stop containing
703. Timed values use the ordinary minimum-start datetime as their timestamp;
they are stored data, not scheduling requests.

## Observations

| Case | Historical Python | Current native |
|---|---|---|
| Unrelated evaluation writes | Output `[1,2]`; user 902 remains | Same |
| Same-key seed 700 | Output `[1,2]`; seed replaced by recording | Same |
| Same-key start write 701 | Output `[1,2]`; write replaced by recording | Same |
| Same-key sparse evaluation writes | Output `[1,2]`; user writes replaced at recorder stop | Output `[902,2]`; user/recorder data are mixed and the first captured tick is lost |
| Same-key sparse stop write 703 | Output `[1,2]`; stop write replaced by recording | Output `[703]`; stop write replaces the extracted recording |
| Same-key dense evaluation writes | Output `[1,2]`; user writes replaced at recorder stop | First recording evaluation raises the dense tick-gap error; state retains `[901]` and the second input is never processed |

All repetitions agree. Historical target stop snapshots show its own write
before the recorder installs the final list; native snapshots expose the
recording during evaluation, and a target stop replacement changes the result
subsequently extracted by eval. These are observations at named callbacks,
not claims about exact destruction time or every possible graph stop order.

The `user_entry_preserved` assessment compares with the desired completed
run's final user payload. In the native dense failure this expected value is
902, but only the first write 901 ran; the observed 901 was not itself lost.
The preserved error and hook trace distinguish premature failure from later
clobbering. No result or state is synthesized after that failure.

## Source corroboration

[Source inventory](source_inventory.json) records relative paths and hashes.
The installed native header matches the source file at
[`8e899e6`](https://github.com/hhenson/hgraph/blob/8e899e600089902f9b755f67d9998292fcc03e84/include/hgraph/lib/std/operators/impl/record_replay_memory_impl.h#L123):
recorder start erases its key; evaluation reads that keyed list and appends.
The dense branch subtracts the existing list length from the cycle offset,
which explains the observed tick-gap rejection after a colliding insertion
at the first cycle. This explanation is source reasoning; the actual error
is retained independently in the observation.

The hashed historical recorder allocates its private capture list at start
and writes the list to `nodes.record.out` at stop. This explains why its
output survives the tested same-key writes while the target's state does not.
The native runner's package identity includes its source hash and records the
literal `eval_node::out` key. No implementation was modified.

## Proposed source boundary

The observations show that type compatibility alone does not protect eval's
recording ownership. A minimal HGL rule can select each eval-owned recorder
key before start, avoiding all closed, resolved source key requirements,
supplied seed keys and other eval-owned recorder keys for that run. Known
nested graph requirements participate in the same inventory. This is key
selection at existing construction/binding time, not a reserved prefix,
new key type, store-wide single-writer rule or runtime role check.

That selection rule is a proposed language decision, not a measured feature
of either reference. This audit neither changes ordinary user-selected key
semantics nor tests a collision-free allocator, unknown runtime-created keys,
concurrent access, incompatible-type rejection or rollback. It supplies the
within-run interference evidence absent from prior cross-run lifecycle tests.

## Reproduce

```sh
python3 runtime/validation/recorder_keys/observe.py \
  --python /path/to/historical-python/bin/python \
  --cpp /path/to/current-native/bin/python \
  --output /tmp/new-key-observations.json
python3 runtime/validation/recorder_keys/check.py
```

The runner refuses an existing destination and verifies engine identity
before/after each case and across its repetitions. It preserves errors and
normalizes only private paths or unstable addresses in error messages. The
checker validates saved corpus/harness hashes, types and assessments without
executing engines.
