# Relocated notes: language/docs/design/decisions/0008-temporal-contracts-and-target-mappings.md

Source: [specification before separation](https://github.com/hhenson/hgraph_spec/blob/766033278bef6e9403cc99c0d8f318ba46a03919/language/docs/design/decisions/0008-temporal-contracts-and-target-mappings.md).

These excerpts preserve earlier implementation notes and their surrounding
context. They were not revalidated during relocation and do not assert current
support or define language behavior. The current specification owns the rules.
HGL source examples remain in the linked specification revision.

## Excerpt 1

> Status: accepted design direction; local fixed-arity `const fn`, role selection,
> and default lifting are implemented. Generic/pack value functions and exported
> value-function descriptors remain follow-up work. The cache concept and lifecycle
> are agreed; its complete declaration syntax, native-type lifecycle syntax, and
> target-mapping syntax remain open. Cache and target examples below remain
> design material; executable value-function examples live in
> [`value-functions.hgl`](https://github.com/hhenson/hgraph/blob/main/language/tests/codegen/value-functions.hgl).

## Excerpt 2

> This is a language design decision, not authorization to implement another
> runtime inside the compiler. The current target remains the public C++ hgraph
> SDK, including its type, operator, lifecycle, and record/replay semantics.

## Excerpt 3

> The following uses the implemented local `const fn` spelling:

## Excerpt 4

> The AST preserves function-level constness separately from parameter constness.
> Typed HIR selects the execution role and records a declaration-order input
> mask only for calls requiring lifting. It also propagates native execution
> phase restrictions through value-call dependencies, independently of source
> order. A value parameter is not permission to read temporal metadata or pass
> an endpoint to a native input-view parameter.

## Excerpt 5

> Hgraph IR owns `ValueFunction` as a distinct callable kind. Lowering interns
> one internal runtime adapter per target/mask, with ordinary parameter bindings,
> an ordinary activation block, and a value-call result. Both the scripted
> harness and AOT emitter consume those same adapters. Neither emitter nor
> runtime performs overload selection per tick. The C++ representation is a
> plain value helper, called by a small generated static node when lifted.

## Excerpt 6

> This implementation supports module-local, fixed-arity, non-generic value
> functions, defaults, named/positional calls, and immediate `const(function)`
> selection with scalar parameter/result types (or a void result). Structural
> value signatures are rejected during checking until their runtime-value and
> ownership conversions are implemented; schema markers are not payload types.
> Generic/pack value functions are diagnosed explicitly. Public
> value-function descriptors, modifier combinations, native-family migration,
> and general first-class callable storage are not implied by this slice.

## Excerpt 7

> A node may need both recordable history and a derived cache. The
> [C++ static-node API](https://github.com/hhenson/hgraph/blob/main/include/hgraph/types/static_node.h) supports one
> `State` and one `RecordableState` together, with independent planned storage.
> Checkpoint restoration precedes `start`, which rebuilds the fresh cache. HGL
> scalar cache declarations, aggregation and mixed state/cache lowering are
> implemented; generic native cache construction remains separate implementation
> work. Shared graph-IR admission no longer rejects the mixed HGL case: a function
> may declare both, and the generated node carries one `RecordableState` and one
> `State` with independent planned storage.

## Excerpt 8

> The existing [descriptor model](https://github.com/hhenson/hgraph/blob/main/language/include/hgl/native_package.h)
> already records native type categories, phase,
> effect, and ownership information, but its `cpp_type`, `cpp_symbol`, headers,
> and build metadata describe the current C++ target. It is a starting point,
> not a completed target-mapping system. The exploratory runtime-contract
> prototype in [PR #796](https://github.com/hhenson/hgraph/pull/796) is related
> design input; this decision neither adopts its entire provisional syntax nor
> claims a specification parser or generator exists.

## Excerpt 9

> Extend the existing typed HIR and hgraph semantic IR boundaries deliberately.
> Represent execution roles and required capabilities before emission; perform
> target-specific realization through an explicit mapping boundary. Emitters
> must not invent language semantics or reimplement resolution. The current
> compiler remains hgraph-specific; another engine or language requires a
> separately validated target integration, not just a different output suffix.

## Excerpt 10

> Suggested bounded implementation order, not additional syntax decisions:

## Excerpt 11

> 1. Define execution-role metadata and `const fn` checking/lowering, including
>    value results and diagnostics for illegal cross-phase calls. Settle modifier
>    combinations and compatibility with existing native declarations.
> 2. Settle cache declarations and native type-construction contracts. Add the
>    public C++ path for a node containing both state categories, with pre-`start`
>    construction and restart/teardown coverage.
> 3. Specify requirements and target mappings with one native cache type and one
>    operator having value-level and temporal implementations. Separate logical
>    identity from target compatibility metadata.
> 4. Probe mapping reuse with an alternative C++ engine and portability with a
>    Rust or Zig realization. Use the same semantic conformance scenarios; do
>    not claim backend support from a specification-only example.

## Excerpt 12

> Acceptance must cover current-value versus wiring-value calls, no accidental
> temporal lifting, domain-specific operator selection, construction before
> `start`, cache reconstruction after restore, partial initialization cleanup,
> borrowed/REF lifetime rejection, and missing-capability diagnostics. Changes
> to runtime behavior require native C++ tests and matching Python coverage
> where exposed. The local value-function slice has HGL execution and public
> C++ wiring tests; the remaining cache and target-mapping extensions are not
> implemented by it.
