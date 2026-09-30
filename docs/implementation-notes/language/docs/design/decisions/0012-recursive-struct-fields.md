# Relocated notes: language/docs/design/decisions/0012-recursive-struct-fields.md

Source: [specification before separation](https://github.com/hhenson/hgraph_spec/blob/766033278bef6e9403cc99c0d8f318ba46a03919/language/docs/design/decisions/0012-recursive-struct-fields.md).

These excerpts preserve earlier implementation notes and their surrounding
context. They were not revalidated during relocation and do not assert current
support or define language behavior. The current specification owns the rules.
HGL source examples remain in the linked specification revision.

## Excerpt 1

> Status: accepted (2026-09-19); implemented (2026-09-20), and complete since
> struct imports landed (ADR 0013, 2026-09-21). Implemented
> through the passes the two backends share. `check_recursive_fields` (`src/semantics/resolve.cpp`) finds
> every recursive edge, admits the ones rules 2, 3, 4 and 8 allow and reports
> the rule each other edge breaks (`tests/semantics/resolve_tests.cpp`); typed
> HIR and hgraph IR mark each admitted edge and name its target by identity.
> Both backends realize edges through hgraph's
> `TypeRegistry::recursive_bundle_closure` (hgraph RFC 0041): direct wiring from
> `src/wiring/type_bridge.cpp`, and generated C++ through the static schema's
> `hgraph::Edge<T>` field, with the two agreeing tick for tick
> (`tests/wiring/recursive-structs.hgl`,
> `tests/codegen/generated_recursive_tests.cpp`). Module descriptor format 6
> marks each edge in an exported struct's layout, and `hgl check` validates it
> without loading code (`tests/driver/recursive-export.hgl`).
> `examples/recursive-fields.hgl` and the user guide's "Recursive fields"
> section show the feature. A second module imports a recursive struct and
> rebuilds its edges through ADR 0013's struct imports
> (`examples/struct-imports/`); the edge's mandatory `= null` is the one field
> default the catalog carries, precisely so that case can cross.

## Excerpt 2

> hgraph already supports them natively (developer guide, *Recursive Bundle
> fields*). A recursive field is an `Owned[T]` value schema: one owner pointer
> inline, whatever `T` is; an unset field leaves it null; the pointee is
> allocated on demand and deep-copied. `TypeRegistry::recursive_bundle` declares
> a self-recursive named Bundle, a null field schema standing for `Owned<Self>`;
> `TypeRegistry::recursive_bundles` declares a mutually recursive batch. Python
> recognises a direct self reference, including `Optional[Self]`, on a
> `CompoundScalar` and uses the same path.

## Excerpt 3

> - **Name resolution** (`semantics/resolve`): `check_recursive_fields` is
>   the detector of recursive edges. It follows same-module structs (rule 5),
>   abstract families (rule 6), generic arguments and collection elements,
>   admits the edges the rules above allow and marks them on the struct's
>   fields. (When this record was written the check looked only for the struct
>   itself, so edges through another struct or an abstract parent passed the
>   resolver and crashed direct wiring; that was fixed first, as its own
>   change.)
> - **Every pass that walks struct fields must terminate on a recursive type**:
>   canonical types, capability and recordability checks, temporalization,
>   constraint reflection, substitution, and both backends' type realization.
> - **Typed HIR and hgraph IR** mark a field as a recursive edge and name its
>   target by struct identity, never by expansion.
> - **Direct wiring** (`wiring/type_bridge`) realizes a recursive struct through
>   `recursive_bundle` or `recursive_bundles` instead of `bundle`. Its present
>   field loop would recurse without end.
> - **Generated C++** needs a spelling hgraph does not have. The static schema
>   has `hgraph::Owned<T>`, but a `NominalBundle<...>` alias cannot name itself
>   from inside its own field list, and nothing stands for `Self`. Either the
>   static schema gains a self marker, or the emitter registers a recursive
>   struct through the registry call. This is an hgraph change and lands there
>   first. (Resolved by hgraph RFC 0041: the static schema's `Edge<T>` names a
>   generated struct, which may be incomplete, and a `NominalBundle` with an
>   edge registers through `TypeRegistry::recursive_bundle_closure`, the same
>   operation direct wiring uses.)
> - **Module descriptors** must express an edge to the enclosing struct or to a
>   batch member in a struct layout. That is a format-version change (ADR 0004).
> - **`delta<S>`** needs no new rule: a recursive edge is an atomic field, and
>   an atomic field in a delta is replaced whole or omitted.

## Excerpt 4

> - resolver tests: a direct edge, a same-module mutual pair, an edge through
>   an abstract parent and a generic self edge are accepted; a required edge, a
>   non-atomic edge, a changed generic argument, a container edge and a
>   cross-module cycle are each rejected with a diagnostic that names the rule;
> - the existing rejection test is replaced, not deleted;
> - a temporal use of a recursive struct has the finite bundle shape of rule 3
>   in both backends;
> - construction, equality, hashing and a three-deep value round-trip through
>   `eval` in the parity corpus, with identical ticks from direct wiring and
>   generated C++;
> - a module descriptor carrying a recursive struct is written, validated by
>   `hgl check` without loading code, and imported by a second module
>   (`examples/struct-imports/`, ADR 0013 slice 8: the edge's mandatory
>   `= null` is the one default the catalog carries, precisely so this closes);
> - an example under `examples/` and a user-guide section.
