# Relocated notes: language/docs/user-guide/README.md

Source: [specification before separation](https://github.com/hhenson/hgraph_spec/blob/766033278bef6e9403cc99c0d8f318ba46a03919/language/docs/user-guide/README.md).

These excerpts preserve earlier implementation notes and their surrounding
context. They were not revalidated during relocation and do not assert current
support or define language behavior. The current specification owns the rules.
HGL source examples remain in the linked specification revision.

## Excerpt 1

> > **Design preview:** the current `hgl` command checks the compiler example corpus and
> > runs composition functions directly and, for file-based `hgl test` and
> > `hgl run`, supports the documented runtime-function subset on Unix with a C++
> > toolchain. Failed REPL declarations leave the last working session intact.
> > The remaining limits are listed in
> > [Testing and running](https://github.com/hhenson/hgraph_spec/blob/766033278bef6e9403cc99c0d8f318ba46a03919/language/docs/user-guide/testing-and-running.md#first-pass-limits), and the
> > status of every surface (implemented, partial, provisional, or blocked) in
> > the [roadmap status matrix](https://github.com/hhenson/hgraph/blob/main/language/docs/design/roadmap.md#feature-status-matrix-2026-09-07).
> > The documents record syntax agreed during design discussion, not a source
> > compatibility promise. Sections marked provisional or not implemented are
> > design material, not accepted compiler examples; open syntax is identified
> > separately from agreed syntax.

## Excerpt 2

> Source files are collected under [`language/examples`](https://github.com/hhenson/hgraph/blob/main/language/examples). The
> frontend checks every example; the scripted backends run the supported subset described in
> [Testing and running](https://github.com/hhenson/hgraph_spec/blob/766033278bef6e9403cc99c0d8f318ba46a03919/language/docs/user-guide/testing-and-running.md#first-pass-limits).

## Excerpt 3

> The agreed extension adds [value-level `const fn`](https://github.com/hhenson/hgraph_spec/blob/766033278bef6e9403cc99c0d8f318ba46a03919/language/docs/user-guide/functions.md#value-level-functions)
> for direct computations without independent ticks, and
> [reconstructible caches](https://github.com/hhenson/hgraph_spec/blob/766033278bef6e9403cc99c0d8f318ba46a03919/language/docs/user-guide/functions.md#reconstructible-cache) for node-local
> data excluded from record/replay. Local fixed-arity value functions and
> [default lifting](https://github.com/hhenson/hgraph_spec/blob/766033278bef6e9403cc99c0d8f318ba46a03919/language/docs/user-guide/value-functions.md) are implemented, as are scalar caches,
> including beside `state`. Non-scalar cache storage remains unsupported.
> `const fn` does not mean compile-time-only or pure; its role is distinct from
> parameter-level `const`.
