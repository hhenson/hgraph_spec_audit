# Relocated notes: language/docs/user-guide/functions.md

Source: [specification before separation](https://github.com/hhenson/hgraph_spec/blob/766033278bef6e9403cc99c0d8f318ba46a03919/language/docs/user-guide/functions.md).

These excerpts preserve earlier implementation notes and their surrounding
context. They were not revalidated during relocation and do not assert current
support or define language behavior. The current specification owns the rules.
HGL source examples remain in the linked specification revision.

## Excerpt 1

> Local, non-generic value functions and their default temporal lifting are
> implemented. See [Value functions and lifting](https://github.com/hhenson/hgraph_spec/blob/766033278bef6e9403cc99c0d8f318ba46a03919/language/docs/user-guide/value-functions.md) for selection,
> `const(function)`, testing, and the remaining implementation boundaries.

## Excerpt 2

> > **Implementation status:** Pack signatures, calls, composition and runtime
> > traversal are implemented, including cardinality suffixes. `len`, `keys`,
> > `types`, `type_at`, and the `each` conjunction are implemented in `requires`,
> > as are borrowed runtime schema views for native inspection.

## Excerpt 3

> A `schema` can only be passed to an approved native helper during that
> evaluation. It cannot be stored, returned, captured, compared, or used in
> arithmetic. See [native helper authoring](https://github.com/hhenson/hgraph/blob/main/language/docs/developer-guide/compiler-and-lowering.md#runtime-pack-schema-views)
> for extension integration.

## Excerpt 4

> > **Current compiler boundary:** explicit materialization is implemented for an
> > operator declared locally or selectively imported from a module with a supported
> > contract. See [separate implementations](https://github.com/hhenson/hgraph_spec/blob/766033278bef6e9403cc99c0d8f318ba46a03919/language/docs/user-guide/modules-and-tools.md#compiling-a-separate-implementation).

## Excerpt 5

> Under the [iteration model](https://github.com/hhenson/hgraph_spec/blob/766033278bef6e9403cc99c0d8f318ba46a03919/language/docs/design/iteration.md), `for` follows the
> containing function's phase. During graph construction, fixed temporal lists
> provide their child connections. Independent bodies over dynamic maps and
> unbounded lists apply separately to each live key or index, and may capture
> temporal inputs. During evaluation, traversal reads current children or scalar
> elements. Loop-carried reductions, graph iterator predicates, `const` captures
> in dynamic graph loops, escaping assignments, and loop returns are unsupported.
> Scalar wiring-time iterables are not implemented yet.

## Excerpt 6

> Status: partially implemented. Temporal conditions support branch values,
> outputless branches, early returns, and assignments to variables declared
> before the conditional. Several variables may be assigned together. A branch
> may retain a variable's incoming binding; otherwise every path reaching a later
> read must assign it. A value-producing temporal `if` without `else` produces
> no ticks while its condition is false. Embedded expressions such as
> `(if c { x } else { y }) + 1` are supported. Scalar branch captures and
> temporal `else if` are unsupported.

## Excerpt 7

> This form is implemented in scripted and compiled modes. See the runnable
> [conditional-sinks.hgl](https://github.com/hhenson/hgraph_spec/blob/766033278bef6e9403cc99c0d8f318ba46a03919/language/examples/conditional-sinks.hgl) example.
> The example also returns a value after a discarded sink conditional, showing
> that the conditional does not inherit the enclosing function's result type.
> Temporal `else if` is not supported yet;
> use a block `else` in the current compiler.

## Excerpt 8

> The [paired HGL/C++ scenarios](https://github.com/hhenson/hgraph/blob/main/language/docs/developer-guide/control-flow-cpp-mappings.md)
> show node-style `when` handlers, wiring-time selectors, temporal selectors,
> multiple results, early returns, sinks, and state lifetime.

## Excerpt 9

> All four are implemented: `out` and `logger` since the first runtime slice,
> `clock` and `scheduler` under
> [ADR 0010](https://github.com/hhenson/hgraph_spec/blob/766033278bef6e9403cc99c0d8f318ba46a03919/language/docs/design/decisions/0010-lifecycle-capabilities.md), and a
> fifth, `alarm`, under [ADR 0015](https://github.com/hhenson/hgraph_spec/blob/766033278bef6e9403cc99c0d8f318ba46a03919/language/docs/design/decisions/0015-pull-sources.md);
> see the next section.
