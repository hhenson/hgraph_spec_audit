# Relocated notes: runtime/scalar_types.md

Source: [specification before separation](https://github.com/hhenson/hgraph_spec/blob/766033278bef6e9403cc99c0d8f318ba46a03919/runtime/scalar_types.md).

These excerpts preserve earlier implementation notes and their surrounding
context. They were not revalidated during relocation and do not assert current
support or define language behavior. The current specification owns the rules.
HGL source examples remain in the linked specification revision.

## Excerpt 1

> 1. **Arithmetic the language has not settled.** HGL leaves open `i64`
>    overflow, integer division and remainder on negative operands, division by
>    zero at run time, and how `NaN` compares. hgraph's own arithmetic table is
>    the reference until it does. These are operator questions, but the answers
>    fix what `i64` and `f64` *are*.
> 2. **Strings.** Ordering, indexing, length and normalisation of `str` are
>    undefined in HGL.
> 3. **An unknown enum integer.** hgraph's native text form falls back to the
>    number; HGL rejects the value. A runtime that receives one from outside —
>    a recording, another process — needs one answer.
> 4. **Clearing an optional field through a delta.** In a bundle's delta an
>    absent field means "no change", so there is no way to say "this optional
>    field is now unset". HGL rejects the attempt until there is.
> 5. **Field order with several abstract parents.** Field order is part of a
>    struct's identity as data; hgraph and HGL both leave the order across
>    multiple parents undecided.
> 6. **Map equality.** As read from hgraph's type registry, a map has equality
>    when its *key* has equality and hash; the value type is not mentioned. It
>    presumably has to have equality too. The capability table follows the
>    registry and should be checked.
> 7. **Recursive fields across modules.** VAL-18 is settled. HGL ADR 0012 is
>    accepted and implemented for its admitted domain in both backends at the
>    [audited revision](https://github.com/hhenson/hgraph_spec_audit/blob/main/runtime/evidence.md). A recursive edge is optional and an atomic
>    boundary, so temporalization terminates. Direct and mutual recursive edges
>    are supported; recursion through containers remains excluded by that ADR.
>    Importing a struct from another module still waits for general struct
>    imports. The earlier statement that HGL rejects all recursive fields is
>    superseded.

## Excerpt 2

> In hgraph: `docs/source/developer_guide/data_structures/schemas/scalar.rst`
> and `core_concepts.rst`; RFC 0002 (the date and time types), RFC 0028 (shared
> values), RFC 0033 (types as values), RFC 0035 (the type layer without
> Python); the capability rules in `src/hgraph/types/metadata/
> type_registry.cpp`; HGL's `language-model.md` (structs, families, generics,
> enums) and `type-extensions.md`.
