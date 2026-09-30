# Relocated notes: language/docs/design/operators.md

Source: [specification before separation](https://github.com/hhenson/hgraph_spec/blob/766033278bef6e9403cc99c0d8f318ba46a03919/language/docs/design/operators.md).

These excerpts preserve earlier implementation notes and their surrounding
context. They were not revalidated during relocation and do not assert current
support or define language behavior. The current specification owns the rules.
HGL source examples remain in the linked specification revision.

## Excerpt 1

> Status: agreed design; executable declarations, descriptor metadata, and the
> current symbol set, including floor division, are implemented. HGL comments use
> `#` or `/* ... */` (see below).

## Excerpt 2

> `+=`, `-=`, `*=`, and `/=` combine assignment with the corresponding binary
> operation; they do not introduce four more operator identities. Assignment and
> comparison are distinct. Node Boolean expressions retain C++ short-circuit
> evaluation; graph Boolean expressions do not conditionally wire their RHS.

## Excerpt 3

> Status: agreed direction, not implemented. The existing symbol mapping and
> domain-property syntax are unchanged.

## Excerpt 4

> This selects `(i64, i64) -> i64`, not every candidate containing an `i64`.
> It says nothing about `(i64, f64) -> f64`. The domain must satisfy the operator's
> `requires` clause. Unknown properties, repeated properties, repeated domains,
> wrong selector arity, non-concrete types, and incorrectly typed identities are
> errors. The first implementation admits concrete type selectors and scalar
> constant identities; const-generic selectors, partial domains, and value-range
> or numerical-policy predicates are deferred. `ref` and `signal` are not value
> domains for these algebraic declarations.

## Excerpt 5

> The native lifted kernels now publish conservative, specialization-specific
> metadata. Unknown guarantees are false in that API. Known string concatenation,
> Boolean logic, integral bitwise operations, and supported total-order extrema
> retain their applicable guarantees. Closed unsigned arithmetic can use modular
> laws; that does not change HGL `i64` into an unsigned or wrapping type.

## Excerpt 6

> The compiler checks and preserves HGL declarations in HIR, graph IR and JSON
> module descriptors. It does **not** prove arbitrary implementations, copy those
> claims into trusted native kernel flags, or enable new optimizations from them.
> Descriptor loading validates metadata shape and checks identity literals against
> the result type after substituting the declared domain (including the normal
> `i64` to `f64` widening). It does not verify mathematical truth. The
> descriptor import catalog supports operator contracts as well as native
> functions, but rejects operator contracts carrying properties until property
> reconstruction is implemented. Optimizer proof transport is also unimplemented.
