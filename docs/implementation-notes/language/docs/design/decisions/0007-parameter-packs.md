# Relocated notes: language/docs/design/decisions/0007-parameter-packs.md

Source: [specification before separation](https://github.com/hhenson/hgraph_spec/blob/766033278bef6e9403cc99c0d8f318ba46a03919/language/docs/design/decisions/0007-parameter-packs.md).

These excerpts preserve earlier implementation notes and their surrounding
context. They were not revalidated during relocation and do not assert current
support or define language behavior. The current specification owns the rules.
HGL source examples remain in the linked specification revision.

## Excerpt 1

> Status: accepted. Implemented for signatures, calls, composition and runtime
> traversal, module descriptors, generated C++ operator contracts, native
> runtime-node aggregate inputs, inclusive cardinality constraints, and the
> `len`/`keys`/`types`/`type_at` constraint intrinsics, quantified `each`
> constraints, and runtime schema views.

## Excerpt 2

> The four reflection intrinsics above are implemented for concrete calls,
> forwarded packs, and positive equality inference such as `N == len(Ts)`.
> Quantified `each` constraints are implemented for concrete and forwarded
> packs. At runtime `schemas(values)` is a compiler-only borrowed view. Generated
> C++ iterates the already-bound `TSLInputView` or `TSBInputView` and passes each
> child's `.schema()` pointer directly. It creates no schema collection, copies
> no metadata, and performs no registry lookup.
