# Relocated notes: language/docs/design/decisions/0011-cache-declarations.md

Source: [specification before separation](https://github.com/hhenson/hgraph_spec/blob/766033278bef6e9403cc99c0d8f318ba46a03919/language/docs/design/decisions/0011-cache-declarations.md).

These excerpts preserve earlier implementation notes and their surrounding
context. They were not revalidated during relocation and do not assert current
support or define language behavior. The current specification owns the rules.
HGL source examples remain in the linked specification revision.

## Excerpt 1

> Status: accepted. Scalar cache declarations and aggregation are implemented.
> Native mixed recordable state/cache storage, pending scheduler recovery, and
> finite `schedule` progress recovery are implemented. Mixed HGL state/cache
> lowering is implemented, with construction and recovery coverage.

## Excerpt 2

> A single scalar cache lowers to `hgraph::State<T>`. Multiple scalar cache
> variables lower to fields of a generated C++ struct in one `State<Struct>`.
> Reads use the corresponding field and writes mutate it in place. The native
> one-`State<>` constraint is a storage-slot constraint, not a one-variable limit.
> All cache fields are constructed before `start` and initialized on every start.
> Native nodes support `State<>` alongside `RecordableState<>`, restoring the
> latter before `start` rebuilds the former, and an HGL function declaring both
> lowers to both selectors. The asymmetry in `start` is the whole contract: a
> state field is seeded only `if (!valid())`, so a restored value wins, while
> every cache field is assigned its initializer unconditionally. Nothing else
> distinguishes them -- one recordable TSB and one cache struct, planned
> independently, exactly as hgraph's two separate `<= 1` selector asserts allow.
> Initializers run in DECLARATION order across both kinds, not states then
> caches: one may name an earlier declaration of the other kind, and resolution
> already requires a declaration to precede its use, so source order is the order
> in which each dependency is ready. `RuntimeState::declaration_order` carries
> that position in the shared IR rather than in one backend. Generated-C++
> coverage runs a component across a checkpoint and asserts that the state
> resumes while the cache restarts, and that a cache seeded from restored state
> sees the restored value. Non-scalar caches and generic
> recordable state without an initializer remain future work.

## Excerpt 3

> Pending native `NodeScheduler` events have a dedicated checkpoint element,
> independent of `State<>`, `RecordableState<>`, and HGL `cache` declarations.
> At a completed checkpoint cut it stores the pending deadlines and tags. Restore
> replaces bootstrap scheduler data after the normal node `start` hook, rebuilds
> the tag lookup, and notifies the graph through its ordinary scheduling path.
> An empty saved schedule clears bootstrap events too. Events at the restart time
> are delivered in that cycle; restarting after a saved deadline is refused.
> Component recovery currently supports simulation only.

## Excerpt 4

> Native and Python persistence tests cover pending deadlines, equal deadlines,
> cancelled/replaced tags, empty schedules, and repeated checkpoints. Native
> `schedule` keeps its emitted-tick count in `RecordableState<TS<Int>>`; the HGL
> constant-delay implementation uses `state ticks`. A three-tick schedule
> checkpointed after one emission resumes with exactly two emissions remaining
> at the original deadlines. Both immediate and delayed first emissions,
> checkpoints before the first emission, and exhausted budgets are covered.
> A completed schedule does not restart when the graph starts again.

## Excerpt 5

> The native time-series-delay overloads also retain their progress. A fresh
> `start` input still resets their emission budget and re-bases the grid. HGL
> has not yet implemented these overloads. Scalar configuration participates in
> checkpoint compatibility, so changing a delay or budget requires a new run.
