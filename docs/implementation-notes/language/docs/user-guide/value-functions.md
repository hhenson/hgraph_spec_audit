# Relocated notes: language/docs/user-guide/value-functions.md

Source: [specification before separation](https://github.com/hhenson/hgraph_spec/blob/766033278bef6e9403cc99c0d8f318ba46a03919/language/docs/user-guide/value-functions.md).

These excerpts preserve earlier implementation notes and their surrounding
context. They were not revalidated during relocation and do not assert current
support or define language behavior. The current specification owns the rules.
HGL source examples remain in the linked specification revision.

## Excerpt 1

> `eval(scale, ...)` tests the temporal definition when present. For a name with
> only a `const fn`, the wrapper is unnecessary. At least one argument must be a
> tick sequence when evaluating a value function; use a direct call/assertion to
> test an all-scalar invocation. The current harness recognizes sequence literals
> as temporal inputs and scalar expressions as configuration; its existing
> structural replay limitations remain in force.

## Excerpt 2

> Local, non-generic, fixed-arity `const fn` declarations, positional/named calls,
> scalar defaults, direct value calls, same-name role selection, automatic lifting,
> and `const(function)` selection are implemented for compiled packages and scripted execution on Unix. The executable fixture is
> [`value-functions.hgl`](https://github.com/hhenson/hgraph/blob/main/language/tests/codegen/value-functions.hgl), with matching
> public C++ wiring tests.

## Excerpt 3

> Value-function signatures currently accept scalar value types, with `void`
> also allowed as a result. Structural parameters and results, including tuples,
> collections, and structs, are rejected
> during checking. This restriction also applies to explicitly `const` parameters.
> Value helpers may call later declarations, but recursive calls are not supported.

## Excerpt 4

> Value bodies use the supported value expressions and runtime statements.
> Tuple/list literals, constant field access, and `if` used as a runtime value
> remain restricted.

## Excerpt 5

> Generic and parameter-pack value functions are explicitly diagnosed, not
> silently emitted as incomplete templates. Exported HGL value-function descriptors
> and `impl const fn` still need separate integration. `native const fn` value
> contracts, including imported overloads, follow the same value-call rules.
> Legacy inline native declarations still require explicit migration.
