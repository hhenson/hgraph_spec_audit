# Relocated notes: language/docs/user-guide/language-tour.md

Source: [specification before separation](https://github.com/hhenson/hgraph_spec/blob/766033278bef6e9403cc99c0d8f318ba46a03919/language/docs/user-guide/language-tour.md).

These excerpts preserve earlier implementation notes and their surrounding
context. They were not revalidated during relocation and do not assert current
support or define language behavior. The current specification owns the rules.
HGL source examples remain in the linked specification revision.

## Excerpt 1

> The concise `=> expression` form is useful for a single-expression function.
> A block uses its final expression as its result. Explicit `return` is an early
> exit: in a composition function the rest of the body becomes the continuation
> of the path that did not return, in both backends
> ([Functions](https://github.com/hhenson/hgraph_spec/blob/766033278bef6e9403cc99c0d8f318ba46a03919/language/docs/user-guide/functions.md#conditional-control-flow)).
