# Remaining implementation references in contract prose: notes relocated on 18 October 2026

Historical implementation material removed from the specification. These excerpts
were not revalidated and do not assert current support or define the standard.
Required behavior and open semantic decisions remain in the specification.

Source revision: `1cfdd23ccadfd3ab7b2248e1e33dbc7d0cb5e511`. The [provenance manifest](final-editorial-cleanup-2026-10-18.provenance.json)
records source hashes, excerpt locations and original text. Relative links in
excerpts resolve to that specification revision.

## language/docs/design/modules.md

### Excerpt 1

[Source, line 267](https://github.com/hhenson/hgraph_spec/blob/1cfdd23ccadfd3ab7b2248e1e33dbc7d0cb5e511/language/docs/design/modules.md#L267).

> universe are then presented to a compiler bridge over hgraph's `TypePattern`,
> `ResolutionMap`, and operator registry. The bridge returns the selected
> candidate, resolved output schema, and rejected-candidate diagnostics.
>
> Generated C++ makes the corresponding public operator wiring call. Both paths
> therefore consume the same registrations and matching rules. A mismatch between
> compiler prediction and generated wiring is a compiler defect and belongs in a
> cross-mode regression test.

## language/docs/user-guide/modules-and-tools.md

### Excerpt 1

[Source, line 221](https://github.com/hhenson/hgraph_spec/blob/1cfdd23ccadfd3ab7b2248e1e33dbc7d0cb5e511/language/docs/user-guide/modules-and-tools.md#L221).

> Current builds require explicit dependencies; automatic discovery and locking
> of a complete transitive package set remain planned.

### Excerpt 2

[Source, line 226](https://github.com/hhenson/hgraph_spec/blob/1cfdd23ccadfd3ab7b2248e1e33dbc7d0cb5e511/language/docs/user-guide/modules-and-tools.md#L226).

> A C++ extension may expose a typed function contract

### Excerpt 3

[Source, line 234](https://github.com/hhenson/hgraph_spec/blob/1cfdd23ccadfd3ab7b2248e1e33dbc7d0cb5e511/language/docs/user-guide/modules-and-tools.md#L234).

> declared by that module. The C++ package remains responsible

### Excerpt 4

[Source, line 238](https://github.com/hhenson/hgraph_spec/blob/1cfdd23ccadfd3ab7b2248e1e33dbc7d0cb5e511/language/docs/user-guide/modules-and-tools.md#L238).

> Language source cannot declare an adaptor. A top-level `native fn` may contain
> local evaluation-time C++, but it does not acquire callback, thread, queue,
> service, module-lifecycle, or external dependency semantics.

## language/docs/design/native-interface.md

### Excerpt 1

[Source, line 206](https://github.com/hhenson/hgraph_spec/blob/1cfdd23ccadfd3ab7b2248e1e33dbc7d0cb5e511/language/docs/design/native-interface.md#L206).

>   receives a common `TSInputView`; it is rejected as a value parameter, nested

### Excerpt 2

[Source, line 215](https://github.com/hhenson/hgraph_spec/blob/1cfdd23ccadfd3ab7b2248e1e33dbc7d0cb5e511/language/docs/design/native-interface.md#L215).

> - raw pointers, lifetimes, callbacks, variadic calls, and open C++ templates are
>   not representable in the HGL signature or descriptor; a local C++ body is
>   still real C++ and remains the author's responsibility;
> - an open C++ template is still exposed only through an explicit specialization
>   or wrapper; generic HGL input-view patterns erase to reviewed non-template C++
>   view types;

## language/docs/developer-guide/syntax-and-semantics.md

### Excerpt 1

[Source, line 988](https://github.com/hhenson/hgraph_spec/blob/1cfdd23ccadfd3ab7b2248e1e33dbc7d0cb5e511/language/docs/developer-guide/syntax-and-semantics.md#L988).

> unresolved dependency or cycle is diagnosed rather than deferred to generated
> C++. Only equalities in a positive conjunction can introduce a binding.

### Excerpt 2

[Source, line 1494](https://github.com/hhenson/hgraph_spec/blob/1cfdd23ccadfd3ab7b2248e1e33dbc7d0cb5e511/language/docs/developer-guide/syntax-and-semantics.md#L1494).

> collisions introduced by automatic numbering; do not rely on C++ emission or
> native registration to enforce this source rule.

### Excerpt 3

[Source, line 2042](https://github.com/hhenson/hgraph_spec/blob/1cfdd23ccadfd3ab7b2248e1e33dbc7d0cb5e511/language/docs/developer-guide/syntax-and-semantics.md#L2042).

> from which imported overload happens to win, inferred from generated C++, or
> changed between scripted and AOT modes.

## language/docs/design/operators.md

### Excerpt 1

[Source, line 146](https://github.com/hhenson/hgraph_spec/blob/1cfdd23ccadfd3ab7b2248e1e33dbc7d0cb5e511/language/docs/design/operators.md#L146).

>   selection are observable. Custom native/Python scalar operators inherit no
>   laws merely because C++ supplies an overloaded operator.

## language/docs/design/native-surface-proposal.md

### Excerpt 1

[Source, line 11](https://github.com/hhenson/hgraph_spec/blob/1cfdd23ccadfd3ab7b2248e1e33dbc7d0cb5e511/language/docs/design/native-surface-proposal.md#L11).

> erased-value accessors, or different spelling based on the C++ representation.

## library/README.md

### Excerpt 1

[Source, line 4](https://github.com/hhenson/hgraph_spec/blob/1cfdd23ccadfd3ab7b2248e1e33dbc7d0cb5e511/library/README.md#L4).

> is its own project; the contracts kept here were derived while triaging
> runtime parity issues and are held until that project exists. Nothing here

## runtime/design_options.md

### Excerpt 1

[Source, line 7](https://github.com/hhenson/hgraph_spec/blob/1cfdd23ccadfd3ab7b2248e1e33dbc7d0cb5e511/runtime/design_options.md#L7).

> reasoning behind hgraph's choices is not lost and so that a new
> implementation can weigh the same trade-offs.

## runtime/overview.md

### Excerpt 1

[Source, line 428](https://github.com/hhenson/hgraph_spec/blob/1cfdd23ccadfd3ab7b2248e1e33dbc7d0cb5e511/runtime/overview.md#L428).

> only as far as working behaviour requires. A facility hgraph has that no
> concept here yet needs — externally driven stepping, observers,

## runtime/boundaries.md

### Excerpt 1

[Source, line 47](https://github.com/hhenson/hgraph_spec/blob/1cfdd23ccadfd3ab7b2248e1e33dbc7d0cb5e511/runtime/boundaries.md#L47).

> C handles, C++ views, Rust borrows and Swift facades may realize these rules.
> An ABI separately fixes widths, versions, contexts, handles, view lifetimes
> and error returns. Package, schema, source and binary compatibility differ.
> Generation, if revisited, must leave handwritten algorithms intact and be
> proved on a small two-backend example. Grammar and tooling remain deferred.
