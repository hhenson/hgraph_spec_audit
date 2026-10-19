# Dictionary and mapping names, 19 October 2026

The project owner agreed to `dict<K, V>` for keyed containers and `map(...)`
for the mapping operation. The specification grammar, type constructors,
examples and cases now use `dict` in both ordinary and temporal type positions.
The separate public spelling `map_` is retired. Additional mapping forms,
including key parameters and multi-collection behaviour, remain unresolved;
the naming decision does not settle them.

Container identity, validity, membership, delta and lookup rules are unchanged.
Existing case identifiers and document paths remain stable. Historical wiring
premises now describe keyed outputs without the retired operator spelling.

The [provenance manifest](dictionary-naming-2026-10-19.provenance.json)
preserves the replaced wording at its pinned source revision.
