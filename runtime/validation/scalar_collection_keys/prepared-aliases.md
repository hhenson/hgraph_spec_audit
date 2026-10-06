# Prepared immutable key aliases

The [source clarification](https://github.com/hhenson/hgraph_spec/blob/48f72cf/language/docs/design/scalar-collection-keys.md)
admits an immutable ordinary `let` alias initialized from a key constant or
cold recipe. Its value is retained once and reused. A temporal or mutable
binding does not become a sparse constant key under this rule.

This is a source-language classification, not a new runtime key identity.
The [recorded scalar-key graphs](observed.json) already pass preconstructed
ordinary keys into actual set/map replay and record paths. The
[temporal ownership audit](../temporal_scalars/README.md) records ordinary value
retention; the [constructor-order audit](../constructor_order/README.md)
separates expression evaluation from later retention. These are supporting
runtime observations, not direct validation of HGL alias syntax.

Neither oracle accepts HGL source, and passing a preconstructed value to a
Python graph cannot establish whether an HGL compiler reruns a provider recipe.
No such equivalence or new runtime coverage is claimed. Compiler validation
must count cold provider calls with a retained local and alias chain, verify
written evaluation order, and reject wrong-type, temporal and mutable aliases
before graph execution. The shared HGL regression covers alias reuse; an
instrumented provider test proves once-only materialization.
