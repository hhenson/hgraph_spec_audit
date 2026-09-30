# Relocated notes: language/docs/design/native-implementation-parts.md

Source: [specification before separation](https://github.com/hhenson/hgraph_spec/blob/766033278bef6e9403cc99c0d8f318ba46a03919/language/docs/design/native-implementation-parts.md).

These excerpts preserve earlier implementation notes and their surrounding
context. They were not revalidated during relocation and do not assert current
support or define language behavior. The current specification owns the rules.
HGL source examples remain in the linked specification revision.

## Excerpt 1

> The shared declaration owns the callable signature. A selected implementation
> part supplies execution shape, injectables and lifecycle requirements.
> Shared HGL contracts cross repositories; implementations belong to their runtime.
> `hgraph` owns C++ parts and providers; `hgl` owns Rust parts and providers.
> A library selects one implementation, never both.

## Excerpt 2

> The compiler checks and carries graph/node contracts. Existing value adapters
> consume selected implementation requirements. Temporal graph/node provider
> execution and borrowed-TS helper binding are not implemented by this change;
> backends must diagnose them rather than emit a value ABI.
