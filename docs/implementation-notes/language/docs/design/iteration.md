# Relocated notes: language/docs/design/iteration.md

Source: [specification before separation](https://github.com/hhenson/hgraph_spec/blob/766033278bef6e9403cc99c0d8f318ba46a03919/language/docs/design/iteration.md).

These excerpts preserve earlier implementation notes and their surrounding
context. They were not revalidated during relocation and do not assert current
support or define language behavior. The current specification owns the rules.
HGL source examples remain in the linked specification revision.

## Excerpt 1

> Status: phase-dependent iteration and the independent-body boundary for
> dynamic graph loops agreed, 2026-09-05. The compiler implements fixed temporal
> list traversal and independent dynamic map/unbounded-list traversal in graph
> composition. Map/reduce lowering of loop-carried accumulators remains a future
> extension and is explicitly unsupported in the initial implementation.
> Graph-phase iterator predicates were also deferred on 2026-09-06; further
> loop design is paused while other language features are discussed. The
> `elements` spelling for lists and sets was agreed on 2026-09-06 and remains
> compiler work; it does not expand the supported graph-loop subset.

## Excerpt 2

> This supersedes the earlier rule excluding `elements`. The compiler still
> implements list/set traversal under `values`; retention of that spelling as
> a compatibility alias remains undecided. The worked examples below and
> [elements-iteration.hgl](https://github.com/hhenson/hgraph_spec/blob/766033278bef6e9403cc99c0d8f318ba46a03919/language/stdlib/examples/elements-iteration.hgl) use the
> agreed target spelling, not implemented compiler support. Dynamic-list loops
> retain their existing independent-body restriction, and graph-phase set
> traversal remains unsupported. No predicate-to-switch or reduction inference
> is introduced.

## Excerpt 3

> The expected C++ wiring is:

## Excerpt 4

> This uses the public native `tsl_element` contract and assumes the standard
> operators are registered before wiring. Both compiler backends already perform
> this expansion for the older `values` spelling in
> [fixed-list-iteration.hgl](https://github.com/hhenson/hgraph_spec/blob/766033278bef6e9403cc99c0d8f318ba46a03919/language/examples/fixed-list-iteration.hgl). The
> `elements` example is the agreed migration target, not current emitted output.

## Excerpt 5

> The current compiler accepts temporal captures such as `offset`. Capturing a
> `const` configuration value in a dynamic child is still unsupported: the
> native mapping contract accepts time-series boundary inputs, while the scalar
> capture ABI and identity rules have not yet been agreed. Such a capture is
> diagnosed rather than silently promoted to a time series.

## Excerpt 6

> Map keys determine child identity. Dynamic lists use index identity, not the
> identity of a stored value. Updating an existing member does not recreate its
> child; membership removal or list truncation stops the affected children using
> the native lifetime protocol. Surviving children retain their own node state.
> The native ownership, binding, and scheduling contracts remain authoritative;
> see [Nested graphs](https://github.com/hhenson/hgraph/blob/main/docs/source/developer_guide/nested_graphs.rst) and
> the public-wiring coverage in [test_map.cpp](https://github.com/hhenson/hgraph/blob/main/tests/cpp/test_map.cpp).

## Excerpt 7

> The incoming accumulator binding must also be preserved. Native associative
> `reduce` uses `zero` for an empty collection, combines it with a singleton, and
> does not include it for two or more live values. It is therefore not a general
> loop initializer: changing `result` above to start at `10.0` cannot simply
> become `zero=10.0`. Ordered reduction provides a true initial accumulator.
> See the [native reduce contract](https://github.com/hhenson/hgraph/blob/main/include/hgraph/lib/std/operators/higher_order.h),
> [ordered dynamic-list tests](https://github.com/hhenson/hgraph/blob/main/tests/cpp/test_reduce.cpp), and
> [zero-semantics tests](https://github.com/hhenson/hgraph/blob/main/python/tests/test_reduce_zero_semantics.py).

## Excerpt 8

> The classifier and typed HIR keep `for`, `keys`, `values`, `elements`, and
> `items` phase-neutral. In a composition function, both direct wiring and
> generated C++ implement `elements(fixed_list)` and `items(fixed_list)` by
> statically expanding the body in index order. `items` supplies an `i64`
> wiring-time index and a child time-series connection.

## Excerpt 9

> For maps and unbounded lists, both backends lower independent map
> `values`/`items` bodies and list `elements`/`items` bodies to hgraph's
> outputless native `map_` path. The child signature
> uses the native `key` or `ndx` convention for `items`; temporal captures are
> explicit pass-through broadcast inputs, including captured maps and lists. The
> shared HGraph-IR `TraversalPlan` rejects
> assignments to enclosing bindings and returns before either backend lowers the
> loop.

## Excerpt 10

> Graph-phase `keys`, iterator predicates, scalar captures, bundles, sets,
> loop-result construction, reductions, and loop exits remain design or
> implementation boundaries and fail closed.
