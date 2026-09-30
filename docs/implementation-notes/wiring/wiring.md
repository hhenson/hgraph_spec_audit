# Relocated notes: wiring/wiring.md

Source: [specification before separation](https://github.com/hhenson/hgraph_spec/blob/766033278bef6e9403cc99c0d8f318ba46a03919/wiring/wiring.md).

These excerpts preserve earlier implementation notes and their surrounding
context. They were not revalidated during relocation and do not assert current
support or define language behavior. The current specification owns the rules.
HGL source examples remain in the linked specification revision.

## Excerpt 1

> | Rules | Evidence |
> |---|---|
> | WIR-5, WIR-6 to WIR-13 | The wiring cases, run on both implementations and held by their contract tests; the C++ matcher and its static unifier are checked row by row |
> | WIR-14 | The HGL front end was observed to vary and is corrected; the front-end case is replayed in its compiler tests |
> | WIR-15 | The bundle-identity case, run on both implementations |
> | WIR-21 to WIR-24 | The operator-contract case, run on both implementations and the HGL front end, and through native C++ wiring, which also checks the registration check (WIR-24) |
> | WIR-4, WIR-16 to WIR-18 | Wiring cases for selection, ambiguity, no candidate and repeated variables, in both implementations' contract tests |
> | WIR-1 to WIR-3, WIR-19, WIR-20 | Source reading only |

## Excerpt 2

> In hgraph: `docs/source/developer_guide/writing_nodes.rst` (the
> dereferenced binding of a generic parameter; the matcher and unifier
> contract), `operators.rst` (resolution, ranking, reference transparency,
> type arguments), `graph_wiring.rst` and `wiring.rst`; the runtime matcher,
> the static unifier and the dispatcher in `src/hgraph/types/`. WIR-22's
> "arguments the operator does not declare" is Python's `*args, **kwargs`
> convention, which hgraph's operators follow. For HGL:
> `language/docs/design/type-extensions.md` (`ref<T>`) and the compiler's
> generic inference.
