# Ordinary value sequences and retained recording entries

Measured 2026-10-01. Ordinary timed data works in both audited runtimes without a replay-slot capability. Ownership differs between Python objects, the Python facade of C++, and native borrowed value views; those three surfaces must not be treated as one API.

[reasoned.json](reasoned.json) was frozen before measurement. [observed.json](observed.json) contains three identical fresh-process runs per engine, with full package and native identities. [native_observed.json](native_observed.json) contains three identical direct-native runs, executable/source hashes, SDK header manifest and actual loaded-library hashes. The engines remain Python hgraph 0.5.41 and the installed C++ development wheel reporting 0.0.0, identified by hashes. No new released-version parity claim is made. The prior [generic GlobalState evidence](../delta_eval/global-state-review.md) remains the evidence for eight scalar state observations; it is not rerun here.

## Timed ordinary data

A const `list[tuple[datetime,int]]` with entries `(MIN_ST,0)`, `(MIN_ST+3us,-7)`, `(MIN_ST+6us,-7)` drives an ordinary Python-authored generator whose body is `yield from data`. A compute returns `ts.delta_value`; the real eval recorder collects `[0,null,null,-7,null,null,-7]`. The same trace occurs with a tuple of timed tuples. Both authoring surfaces match. The producer receives timed entries directly, rather than dense slots; eval's output densification reports gaps. No adapter padding is added in this probe.

The existing keyed replay operators also accept those timed entries: Python's `set_replay_values` stores the iterable consumed by `replay_from_memory`; C++'s sparse memory replay reads the ordinary list under its fully qualified record key. Both measured traces match the same reasoning.

A direct native fixture uses an ordinary value-layer list of `(DateTime,Int)` tuple values as one const scalar argument. Its source reads length/index/tuple fields, retains only an integer cursor, and schedules the next absolute entry time. It wires an actual delta compute and the native eval recorder. Its trace also matches exactly. This measures the general list/tuple/scalar/scheduler facilities; it is a small probe authored against the native SDK, not a modification to the reference implementation or a claim of an existing built-in `replay(data)` overload.

Source inventory found the named built-in memory replay contracts take a key, not a const data-list parameter: Python `hgraph/_operators/_record_replay.py` and native `include/hgraph/lib/std/operators/io.h`. A direct const-data replay *can be authored* using the existing generic source APIs, as measured. `replay_const(key)` is a recovery/sampling operator, not a const timed-sequence replay constructor. No claim is made about every replay backend or existing dataframe overload.

## Copy, alias and replacement observations

| Operation | Historical Python / ordinary Python values | C++ Python facade | Direct native SDK |
|---|---|---|---|
| Ordinary nested-list assignment | Same object; later source append/indexed-child mutation is visible | Python assignment has the same normal Python semantics | Not the same operation as copying an owning `Value` |
| Shallow list copy / tuple containing a list | Nested lists still alias | Same normal Python semantics | Tuple field construction from `ValueView` copies the supplied nested value in the measured builder |
| Explicit owning copy | `deepcopy` retains `[[1],[2]]` after source mutation | `deepcopy` of exported list is independent | `Value` copy and `clone()` retain `[1,2]` while original becomes `[99,2,3]` |
| GlobalState set nested list | Stores the Python object reference | Converts/copies; later source mutation leaves stored `[[1],[2]]` | `set(const Value&)` copies; later source append leaves stored `[1,2]` |
| GlobalState get and append | Retrieved list aliases store; append changes store | Exported Python list is independent; local append does **not** change store | `get()` returns a borrowed mutable view for mutable storage; append through it changes store to `[1,2,3]` |
| Retain value then replace key | Retrieved Python object remains alive separately from replacement | Exported Python value remains independent | `Value{get(...)}` is an owning snapshot; it stays `[1,2]` after stored mutation and replacement with `[7]` |
| Append nested entry | Ordinary Python append aliases the appended object unless explicitly copied | Ordinary Python append still has normal Python behavior | `MutableListView.push_back(view)` copies nested `[1,2]`; later source append does not change the stored entry |

The ordinary-Python alias observations are descriptive, not failed owning-copy tests. Neither Python assignment nor a borrowed native `ValueView` was declared to be an independent retained copy. The explicit deep-copy/native-owning-copy tests satisfy the prewritten VAL-17 expectations for these values. They do not establish ownership of every arbitrary native or Python extension object.

The two GlobalState Python surfaces demonstrably differ. Recommending `get → local append` as a portable in-place update would be incorrect: C++ Python export requires a subsequent set to publish that Python-list change. Direct C++ `GlobalStateView.get` is a different route and does expose in-place list mutation. Whether HGL exposes an owning result, a scoped mutable entry borrow, or both is a specification decision; the successful native probe does not define HGL syntax or borrowed-access rules.

## Mutable access and view lifetimes

The native fixture obtains both an owner view and a list container view, then sets element zero and appends to that same owner. The owner view sees `[99,2,3]`; the already-created list view reports size three. This is live mutable-owner access, not a cycle-stable read snapshot. VAL-16 cannot be asserted for this access merely because the type is named `ValueView`. The specification must distinguish a read snapshot from an explicit mutable place/owner borrow if it offers both.

Native immutable compact lists reject mutation. Native list push and set install copies of their payloads. Source inspection in `include/hgraph/types/value/specialized_views.h` shows `at(index)` returns a view into element storage. This SDK's mutable-list implementation uses `ValueSlotStore`/`StableSlotStore`, whose source describes stable payload slots during capacity growth; that representation fact is not a blanket lifetime guarantee for every list representation, replacement, erase, or nested mutation. `GlobalStateView` borrows its owner, and replacing an entry assigns its boxed value in place. No epoch/generation-checked stale-borrow contract was established by this audit. A borrowed element/entry was **not** dereferenced after replacement, growth or owner destruction to manufacture an unsafe lifetime test. Only explicit owning retained copies were used across replacement. Same-key replacement invalidation policy, simultaneous borrows, callback escape, and nested mutation transactions remain unmeasured.

For native sources, see `include/hgraph/types/value/value.h` (owning construction and clone), `value_builder.h` (owned list and tuple assembly), `specialized_views.h` (list indexing/mutation), `mutable_container_ops.h` (mutable storage copies), and `include/hgraph/runtime/global_state.h` (copy/move set versus borrowed get). Python facade get/set conversion is implemented in `python/py_state_services.cpp`; the historical Python store is in `hgraph/_runtime/_global_state.py`. Installed headers are hashed in the native evidence; this source inventory is not a fresh behavioral test of every documented overload.

## Retained recording deltas

The publisher reuses one mutable dictionary, replacing its contents each tick before publishing a TSD delta. The real recorder returns `[{1:10},{1:20},{1:30}]`; after the producer dictionary is cleared/mutated again and garbage collection runs, the returned entries retain that same trace in both engines. Native nested-list push and tuple construction additionally demonstrate independent copied payloads at ordinary value-container boundaries. This supports implementing owned timestamp/delta entries with general value operations. It does not claim every arbitrary mutable TS atomic payload is cloned, or that holding a borrowed endpoint view is permitted.

No timings, allocation counts or complexity benchmark were recorded. The native in-place append path avoids a required full-list get/export/set in the probe's call structure; no measured asymptotic performance claim is made.

## Reproduction

```sh
python3 runtime/validation/value_sequences/observe.py \
  --python /path/to/python-hgraph/bin/python \
  --cpp /path/to/cpp-hgraph/bin/python \
  --output /tmp/new-value-sequence-observed.json
cmake -S runtime/validation/value_sequences -B /tmp/value-sequences \
  -Dhgraph_DIR=/path/to/sdk/lib/cmake/hgraph \
  -DPython_EXECUTABLE=/path/to/cpp-hgraph/bin/python
cmake --build /tmp/value-sequences --parallel 2
python3 runtime/validation/value_sequences/native_observe.py \
  --executable /tmp/value-sequences/value_sequences_native \
  --sdk-include /path/to/sdk/include \
  --output /tmp/new-native-value-observed.json
python3 runtime/validation/value_sequences/check.py
```

Runners reject existing result destinations and preserve unsupported/error outcomes. The checked-in results use GNU C++ 14.3.0, C++23 and Release for the native supplement. The checker validates saved evidence; it does not rerun engines. Source metadata records no private host paths. No HGL specification or implementation is changed by these probes.
