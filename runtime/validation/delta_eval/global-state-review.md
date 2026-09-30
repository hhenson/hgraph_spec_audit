# Global-state inventory for eval/replay/record

Source inventory, 2026-09-30. The source inspection below is separate from
the focused fresh measurement described in the final section. Source paths below are package/SDK-relative so the findings can
be transferred to audit documentation without private machine paths. Python
means the existing audited 0.5.41 package; native means the existing audited
C++ wheel and its installed SDK, not a newly measured release.

## Findings from the Python reference

- `hgraph/_runtime/_global_state.py:6–163`: GlobalState owns a heterogeneous
  `dict[str, Any]`. `instance()` fails if no active state; it does not create
  one. Context entry saves the previous selection and selects this store;
  exit restores the previous selection. Indexed/get reads search the current
  store, then the previous context; set writes the current store. Missing
  indexed access raises KeyError; `get(key, default)` returns the default.
  Values are ordinary Python objects: get/set do not establish generic
  deep-copy ownership. `keys/items/values` expose the current dictionary;
  some combined-context accessors have different behavior. Do not adopt
  every convenience API or assume complete mapping/nesting equivalence.
- `hgraph/test/_node_unit_tester.py:121–168`: eval wires normal replay sources,
  the actual target and a normal record sink. For each temporal argument it
  calls `set_replay_values(label, SimpleArrayReplaySource(values, start))`.
  Labels are argument names, not special per-node capabilities.
- Same file `:168–209`: eval creates a GlobalState scope only if none exists;
  otherwise it reuses the caller's scope. It evaluates the graph, retrieves
  the recording after graph completion, and derives dense output positions.
  Empty/wholly silent results fall through to raw None. Fixed labels are safe
  for ordinary sequential runs because seeding and recording replace values;
  these facts do not prove concurrent/reentrant same-key safety.
- `hgraph/_impl/_operators/_record_replay_in_memory.py:44–65`: the replay
  object is a reusable iterable protocol, with SimpleArrayReplaySource as one
  implementation. Its iterator advances time for every input slot and yields
  only non-None values. Seeding stores that object in GlobalState under
  `nodes.replay_from_memory.<label>` by default, or `:memory:<id>.<label>`.
- Same file `:69–102`: the replay operator receives injected GlobalState,
  traits and clock. It resolves the key, gets the source, raises ValueError
  when absent, ignores entries earlier than its current evaluation time,
  then yields timed non-None values. It does not receive an injected
  replay-only buffer capability.
- Same file `:151–194`: record receives injected GlobalState plus node state.
  Start sets a recording key and an empty local list. Evaluation appends
  `(evaluation_time, ts.delta_value)` to that list. Stop sets the global-state
  key to the completed list, including an empty list after no ticks. The
  default eval key is `nodes.record.out`. Under a resolved recordable-id
  mode, stop preserves earlier entries before the run start and extends with
  the new recording; this is beyond the fresh-eval profile.
- Same file `:197–216`: get_recorded_value reads the normal keyed entry;
  reset_recorded_value removes it. No bespoke capture injectable exists.

## Findings from the native runtime and Python facade

- `include/hgraph/runtime/global_state.h:15–174`: GlobalState owns a mutable
  heterogeneous `Map<string, Any>` value; GlobalStateView is its non-owning,
  node-injected view. Operations are generic size/contains/get/set/erase and
  copy_from. Missing get returns an invalid ValueView; get_as<T> rejects a
  missing/wrong type. Set has copy and move overloads. Get unwraps Any and
  returns the stored value's own mutability: mutable lists/maps can be changed
  through the view; immutable values remain read-only. This is general value
  storage, not a replay/capture role registry.
- Same header: the top-level builder owns the seed. At graph build, it is
  copied into a runtime isolation store shared by root and nested graphs;
  results copy back at run end. The injected view must not outlive its owner.
  GlobalSeedBinding detaches when its authoring owner exits, preventing stale
  seed pointers. Native authoring's active GlobalContext and the Python
  facade's context selection are authoring conveniences, not substitutes for
  injected runtime access.
- `hgraph/_wiring/_state.py:141–313`: Python GlobalState wraps the native
  owner. Indexed access raises on missing keys; get/default, setdefault,
  contains, pop and key enumeration are generic. GlobalContext explicitly
  rejects nested activation. `_global_state_scope` reuses an existing caller
  scope or opens/closes one around the operation. `_active_global_state`
  (`:12–31`) rejects ambient lookup during runtime and instructs callbacks
  to declare the injectable. These lifetime/nesting rules differ from the
  historical Python class; do not transplant its process-global singleton.
- `hgraph/_wiring/_runner.py:757–940`: eval creates/reuses an authoring state,
  passes it explicitly to Wiring, wires `__harness_replay` with keys such as
  `eval_node::<parameter>`, sets replay data after target wiring, and wires
  `__harness_record` to `eval_node::out`. It runs, releases its seed/scope in
  finally, then extracts through the run result. No-tick results are raw None.
- `include/hgraph/lib/testing/eval_node.h:164–168,378,493–544`: direct native
  eval uses `eval_node::inN` and `eval_node::out`, seeds the builder's generic
  state, runs the actual replay/target/record graph, copies completed graph
  state back to an active authoring state, and reads the graph's state. It
  pads the returned vector to the supplied input horizon.
- `include/hgraph/lib/testing/record_replay.h:35–131`: testing helpers put
  ordinary value-layer lists in GlobalState. Dense seed slots contain a
  delta or absence. Retrieval makes owned delta copies; a missing recording
  key returns an empty vector. This helper behavior is not proof that a
  recording key existed.
- `include/hgraph/lib/std/operators/impl/record_replay_memory_impl.h:123–207`:
  the harness dense recorder is given generic GlobalStateView. Start erases
  an earlier result at the key and resolves its delta schema. Evaluation
  captures an owned observable delta, creates the mutable typed list lazily,
  pads skipped cycle positions and appends. There is no recorder stop flush;
  writes already reside in the graph-global store. A no-tick run leaves its
  key absent. The harness's sparse-output option is still this lazy backend.
- Same header `:233–273`: the separate production sparse-memory recorder
  creates an empty timestamped list in start if missing and appends directly
  during evaluation. It retains an existing list for recovery. Therefore
  "C++ recorder does not create an empty recording" is too broad: the observed
  issue is specific to the dense harness backend.
- Same header `:287–375`: normal replay receives a const string key, generic
  GlobalStateView, cursor, scheduler and output. Dense replay gets the list,
  reads indexed delta/absence and applies it, then advances/schedules. Missing
  state returns without publication, unlike Python replay's missing-key
  error. Sparse replay uses a fully qualified key and timed entries. Both
  are clients of generic global state, not an injected replay-only facility.

## Existing observed evidence and limits

The audit's `runtime/validation/delta_eval/` files already establish:

- `observed.json`, `operator_observed.json`, `native_observed.json`: genuine
  replay → compute → record publication traces, repeated fresh processes.
- `lifecycle_observed.json`: record start/stop callbacks even with no input
  publications; graph-stop precedes extraction; sequential reuse of the same
  external state/key does not append a previous run; retained TSD delta
  captures survive later producer mutation and collection.
- `lifecycle_control_observed.json`: the exact external output key contains
  two entries after `[1,2]` in both engines; after silence Python exposes an
  empty list while the native harness key is absent. The control establishes
  visibility, not just a wrong guessed key. During native callbacks the
  observer reads external seed state, not the internal graph store, so it
  does not establish internal visibility before the first tick.
- `indexing_observed.json`: six publication traces distinguish absence from
  zero, false and empty text. They do not validate any HGL get/index/null
  syntax, type refinement, global-state key API or arbitrary stored values.
- `collection_observed.json` and its control retain empty-set application
  disagreement. Changing the storage capability does not settle it.

No existing probe establishes all generic GlobalState type errors, aliasing,
failed-run copy-back, nested/concurrent runs, cross-thread access, same-key
writers or ownership of arbitrary mutable atomic objects. The general store
source API is inspected evidence; do not claim those behaviors measured.

## Recommended minimal HGL direction (proposal, not a specification)

1. Use one reusable `inject global_state` capability backed by the enclosing
   graph/run store, shared by its nodes. It must work for an ordinary scalar
   counter/configuration value as well as replay sequences and recordings.
   Eval allocates/seeds its run store. A normal record operator receives an
   ordinary const key argument. Replay can receive its input sequence as an
   ordinary const argument; using a key for replay is an alternative, not a
   required injectable or a separate runtime capability. The eval caller still supplies only its
   target and input sequences. Remove the replay_input/capture injectables
   rather than disguising their roles behind a new name.
2. Define generic typed value get/set (plus contains or required-read only
   if needed), string keys, insert-or-replace behavior, missing-key and wrong-
   type outcomes, and the store's lifetime. Keep role-specific begin/append,
   timestamps, slot-indexing and scheduler policy out of the global-state
   capability. Those belong to normal value/container operations and HGL
   operator bodies. Type erasure inside a native store does not require an
   unrestricted source-language Any type.
3. Use ordinary owned value sequences for replay and recording. Sequence
   indexing/length and list append must be reusable independently of eval.
   Distinguish missing key from a present sequence's absent element and from
   a present empty sequence. Retrieval typing and mutable-view ownership
   must be specified: source inspection supports borrowed mutable views in
   C++ and object references in Python, not a universal deep-copy get rule.
   A scoped borrowed container view plus explicit owning capture is a small
   faithful option if HGL already supports the necessary value borrows.
4. Choose a simple fresh-run orchestration policy rather than exposing all
   authoring ambient-context behavior. Eval owns the store through stop and
   extraction, generates its recording key, and supplies replay data internally. A
   general store may allow arbitrary clients to replace keys; uniqueness is
   eval's wiring responsibility, not a replay-role restriction on get/set.
5. Recorder start should deliberately establish its empty ordinary list;
   append owned `(time, delta)` values through generic collection operations.
   It may publish that list to global state at start and mutate it there,
   or retain ordinary local storage and set the key at stop. Both patterns
   occur in reference operators. The first avoids requiring new list-valued
   node cache merely to reproduce Python's stop-flush implementation detail.
   Stop-flush is a separate visibility choice, not inherent in GlobalState.

Before claiming a fully HGL-authored implementation, settle three real gaps:
(a) how typed get obtains its expected ordinary value type without invented
explicit generic-call syntax; (b) whether scalar/recursive contextual deltas
and absence can inhabit a general owned sequence, including timestamped
record entries; (c) how an HGL value list grows and how borrowed global values
may be mutated or retained. If these facilities are absent, the honest next
extension is reusable value/container and global-state semantics, not native
methods secretly named after replay/capture. Missing-key behavior and recorder
visibility have reference differences and need explicit HGL choices.

## Fresh generic-state measurement

[global_state_reasoned.json](global_state_reasoned.json) freezes expectations
before the three-process repeated measurement, following an exploratory
lifecycle smoke check. [global_state_observe.py](global_state_observe.py) uses
an ordinary compute node with injected GlobalState and arbitrary keys that
are independent of eval's replay/record keys. Both engines match all eight
observation groups in [global_state_observed.json](global_state_observed.json):
seed 40, add input publications 1 and 2 around silence, retrieve 43 after stop;
start and stop writes remain readable; a separate store seeded with 5 yields
8 without changing the first; missing indexed lookup raises KeyError while
get with a default returns the default; zero, false and empty text remain
present values. Package, source and loaded-native-library identities are
recorded with the probe hash.

This establishes scalar seeding, injected get/set, lifecycle availability,
post-run retrieval and sequential independent-store isolation. It does not
measure arbitrary container aliasing, typed HGL retrieval, nested graph
sharing, concurrent writers or failed-run extraction. Those boundaries must
not be inferred from this successful scalar probe. Python source is the
0.5.41 package; the native run is the recorded development build (distribution
version 0.0.0), not a claimed released 0.8 version.

The proposed HGL required-read operation intentionally reports a missing key
as an error. Reference optional/default reads remain different operations;
this probe does not imply that optional get should silently supply a value in
HGL. Native get_as<T> provides inspected evidence for exact typed retrieval;
Python's dynamic lookup does not independently establish that source rule.
