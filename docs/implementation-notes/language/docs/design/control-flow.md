# Relocated notes: language/docs/design/control-flow.md

Source: [specification before separation](https://github.com/hhenson/hgraph_spec/blob/766033278bef6e9403cc99c0d8f318ba46a03919/language/docs/design/control-flow.md).

These excerpts preserve earlier implementation notes and their surrounding
context. They were not revalidated during relocation and do not assert current
support or define language behavior. The current specification owns the rules.
HGL source examples remain in the linked specification revision.

## Excerpt 1

> Status: agreed conditional strategy, 2026-09-05; partially implemented. Both
> backends lower an explicit two-branch temporal `if` whose result is the tail
> value of each branch through the native switch. They also lower outputless
> temporal conditionals with an optional block `else` through the native sink
> switch, including discarded conditionals inside value-producing graphs.
> One predeclared temporal variable assigned by both explicit branches is also
> remapped from the switch output for later composition. Several such variables
> are returned through one compiler-generated structural TSB and remapped by
> field; a used expression result can share the same result structure. A branch
> can also forward an existing binding through a reference-qualified generated
> input. A consumed temporal conditional without `else` receives a typed
> never-ticking false branch in both backends. Early-return continuations work
> for top-level and nested direct temporal conditional statements and block
> tails. A temporal conditional embedded in another expression form is
> implemented in both backends and pinned by the parity fixture
> (`tests/codegen/parity.hgl`, `choose_embedded`). Scalar branch captures and
> temporal `else if` remain staged.
> A temporal `else if` is rejected rather than silently treated as an omitted
> `else`. This record uses the existing `if`/`else` syntax. It does not settle the
> other control-flow constructs or introduce new keywords.

## Excerpt 2

> The compiler accepts the typed declaration without an initializer,
> `var r: i64`. It does not supply a value or connection: a later read is valid
> only after definite-assignment analysis proves that every reaching path has
> assigned it. This single-result form is implemented in both compiler backends;
> see the runnable
> [conditional-result.hgl](https://github.com/hhenson/hgraph_spec/blob/766033278bef6e9403cc99c0d8f318ba46a03919/language/examples/conditional-result.hgl) example.

## Excerpt 3

> This multiple-result form is implemented in both compiler backends; see the
> runnable [conditional-results.hgl](https://github.com/hhenson/hgraph_spec/blob/766033278bef6e9403cc99c0d8f318ba46a03919/language/examples/conditional-results.hgl)
> example. The direct backend constructs the structural result from runtime
> metadata, while generated C++ names the equivalent `UnNamedTSB` explicitly and
> projects its fields after `switch_`.

## Excerpt 4

> This form is implemented in both compiler backends, including independent
> forwarding within a multi-result bundle; see the runnable
> [conditional-forwarding.hgl](https://github.com/hhenson/hgraph_spec/blob/766033278bef6e9403cc99c0d8f318ba46a03919/language/examples/conditional-forwarding.hgl)
> example.

## Excerpt 5

> The negative design-corpus example is
> [conditional-unassigned-result.hgl](https://github.com/hhenson/hgraph_spec/blob/766033278bef6e9403cc99c0d8f318ba46a03919/language/stdlib/examples/invalid/conditional-unassigned-result.hgl).
> The compiler now implements this path-sensitive rejection; the file remains in
> the design corpus rather than the positive runnable examples.

## Excerpt 6

> This form is implemented in both compiler backends; see the runnable
> [conditional-mixed-results.hgl](https://github.com/hhenson/hgraph_spec/blob/766033278bef6e9403cc99c0d8f318ba46a03919/language/examples/conditional-mixed-results.hgl)
> example.

## Excerpt 7

> See the runnable
> [conditional-early-return.hgl](https://github.com/hhenson/hgraph_spec/blob/766033278bef6e9403cc99c0d8f318ba46a03919/language/examples/conditional-early-return.hgl)
> example. HGraph IR represents the ordered callable-suffix path, branch
> fallthrough, complete-path captures, and enclosing-function result explicitly.
> The path retains a separate segment for every enclosing lexical block so
> intermediate tail expressions keep their source order. Both compiler backends
> consume that plan for top-level and nested direct temporal conditional
> statements, including paths nested inside an already-attached continuation.
> A temporal conditional embedded in another expression form is implemented in
> both backends and pinned by the parity fixture; it carries no early return,
> so it needs no continuation plan.

## Excerpt 8

> `debug_print` takes the label first and the time series second, matching the
> [native operator contract](https://github.com/hhenson/hgraph/blob/main/include/hgraph/lib/std/operators/io.h).

## Excerpt 9

> Result analysis is local to the conditional. A discarded outputless
> conditional uses this sink-switch path even when a later expression supplies
> the enclosing graph's return value. The current implementation accepts an
> omitted `else` or a block `else`; temporal `else if` lowering remains staged and
> is diagnosed explicitly, once, by the shared analysis (`PlanIssue` in
> `hgraph_ir/control_flow.h`) rather than by each backend.

## Excerpt 10

> The true branch takes `value` as a temporal input, with `"enabled"` as its
> fixed label. The selector is `enabled`. The false path has no conditional
> work. This switch has no output: no returned time-series connection, bundle,
> dummy value, or `signal` output is required. There are no escaping bindings to
> remap. Native sink-switch behavior is covered in
> [test_switch.cpp](https://github.com/hhenson/hgraph/blob/main/tests/cpp/test_switch.cpp).

## Excerpt 11

> The existing native machinery distinguishes explicit callable arguments from
> captured outer ports. In
> [higher_order_impl.h](https://github.com/hhenson/hgraph/blob/main/include/hgraph/lib/std/operators/impl/higher_order_impl.h),
> `compile_switch_branch` adds `CompiledSubGraph::captured_inputs` to shared outer
> slots, deduplicates by source identity, and remaps child boundary inputs onto
> those slots. The switch's complete temporal input schema is its selector plus
> the resulting outer slots.

## Excerpt 12

> Explicit call arguments have a different constraint:
> `bind_wired_fn_args` in
> [wired_fn.h](https://github.com/hhenson/hgraph/blob/main/include/hgraph/types/wired_fn.h) validates each branch's
> arity and parameter names. It does not silently discard arguments that one
> branch does not accept. A language lowering must therefore provide consistent
> explicit branch signatures or use the native capture-boundary mapping; it
> cannot pass a union of arguments to differently shaped lambdas and assume the
> binder filters them.

## Excerpt 13

> [Arrow control flow](https://github.com/hhenson/hgraph/blob/main/python/hgraph/arrow/_control_flow.py) constructs
> true and false branch callables in `_IfThenOtherwise.__call__`, then calls
> `hg.switch_`. The
> [Arrow tests](https://github.com/hhenson/hgraph/blob/main/python/tests/ported/arrow/test_arrow.py) exercise
> `if_then(...).otherwise(...)` and `if_(...).then(...).otherwise(...)`.

## Excerpt 14

> The lifetime contract is owned by the native switch, documented in
> [Nested graphs](https://github.com/hhenson/hgraph/blob/main/docs/source/developer_guide/nested_graphs.rst)
> and tested through public wiring in
> [test_switch.cpp](https://github.com/hhenson/hgraph/blob/main/tests/cpp/test_switch.cpp). HGL should reuse that
> contract rather than implement branch execution independently.

## Excerpt 15

> The examples above establish predeclared escaping bindings, forwarding existing
> bindings, definite assignment, early-return continuations, outputless
> conditional wiring, mixed expression/assignment results, and subsequent
> composition. [Iteration](https://github.com/hhenson/hgraph_spec/blob/766033278bef6e9403cc99c0d8f318ba46a03919/language/docs/design/iteration.md) records the subsequent agreement about
> `for` in graph composition and node evaluation.
> [Explicit switch dispatch](https://github.com/hhenson/hgraph_spec/blob/766033278bef6e9403cc99c0d8f318ba46a03919/language/docs/design/switch.md) records the subsequent agreement about
> node-style C++ dispatch, graph-style branch captures and results, and the
> `default: ...` fallback with no-match failure. The source form is
> `switch selector { case value: ... default: ... }`, with constant case values.
> The [paired HGL/C++ mappings](https://github.com/hhenson/hgraph/blob/main/language/docs/developer-guide/control-flow-cpp-mappings.md)
> illustrate the shared capture/result, early-return, sink, and lifecycle rules.
> No new syntax or lifetime policy for `for`, `map`, `reduce`, or `mesh` is
> introduced by these conditional agreements.

## Excerpt 16

> Both language backends now accept the smallest value-producing form: a
> temporal Boolean condition, an explicit block `else`, no scalar captures,
> or branch `return`, and one compatible tail value from each branch. They also
> accept outputless temporal conditionals, with or without an explicit block
> `else`, and lower them through the native `switch_sink_` operator. A conditional
> statement may instead assign one predeclared temporal variable in both explicit
> branches; the switch result remaps that binding for later statements. Several
> escaping variables share one compiler-generated structural TSB and are remapped
> from its fields. HGraph IR performs capture/effect/escape and common result-slot
> analysis once; the direct path builds
> context-backed branch callables, while `emit-cpp` writes ordinary named graph
> structs and native switch calls. Scripted and generated behavior are covered by
> compiler tests and executable examples. Expression results can share the
> generated structure with escaping assignments. Existing connections can be
> forwarded independently by reference and are adapted back to each result
> slot's declared schema at the branch boundary. A value-producing conditional
> without `else` supplies a type-resolved `nothing` source for the absent false
> branch, so it emits no default value and no tick while false. Shared HGraph IR
> continuation planning is implemented, including path-sensitive fallthrough,
> capture analysis, a distinct enclosing-function return result, and ordered
> lexical suffix segments for nested paths. Both execution backends consume the
> multi-segment plan for nested direct temporal conditional statements and block
> tails. A temporal conditional embedded in another expression is implemented
> in both backends and pinned by the parity fixture. Temporal `else if` remains
> staged.

## Excerpt 17

> The parser, typed uninitialized `var`, and path-sensitive definite assignment
> support are broader than this first backend slice. The early-return and
> omitted-`else` value cases have graduated to the executable corpus as
> `conditional-early-return.hgl` and `conditional-omitted-else.hgl`.
