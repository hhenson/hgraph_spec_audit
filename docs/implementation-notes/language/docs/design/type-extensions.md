# Relocated notes: language/docs/design/type-extensions.md

Source: [specification before separation](https://github.com/hhenson/hgraph_spec/blob/766033278bef6e9403cc99c0d8f318ba46a03919/language/docs/design/type-extensions.md).

These excerpts preserve earlier implementation notes and their surrounding
context. They were not revalidated during relocation and do not assert current
support or define language behavior. The current specification owns the rules.
HGL source examples remain in the linked specification revision.

## Excerpt 1

> Status: agreed source semantics, 2026-09-05; explicit `ref<T>` parsing, type
> checking, metadata, descriptors, and generated reference-routing nodes are
> implemented. The lowercase `signal` input marker is also implemented through
> parsing, semantic checking, descriptor validation, direct-wiring type
> materialization, generated C++, and scripted runtime behavior tests.
> Wiring-time access through a reference and imported native types remain
> compiler work. A map of references, `map<K, ref<V>>`, is settled and
> implemented (below). This record introduces no native declaration syntax.

## Excerpt 2

> Status: enum declarations, qualified member references, explicit/automatic
> numbering within the signed `i64` range with compile-time overflow errors,
> member-name stringification, rejection of duplicate numbers,
> distinct enum identity, explicit integer conversion, checked construction from
> integers or strings through the enum type name, and the `keys`, `values`, and
> `elements` calls on enum types returning immutable fixed-size scalar lists
> are agreed, 2026-09-06. Members are
> constant switch case values. Duplicate resolved switch cases are rejected;
> covering all declared members establishes exhaustiveness, while partial
> switches remain permitted with the existing no-match failure. String conversion
> uses the agreed Python-style `str(value)` spelling. Remaining conversion details and native
> mapping are still open; compiler support is not implemented.

## Excerpt 3

> The existing native [enum registration contract](https://github.com/hhenson/hgraph/blob/main/include/hgraph/types/metadata/type_registry.h)
> accepts an ordered member-name/assigned-integer table. Its
> [enum value operations](https://github.com/hhenson/hgraph/blob/main/src/hgraph/types/metadata/type_registry.cpp)
> currently stringify a known number using its member name, and fall back to
> numeric text for an unknown number. This is native implementation context,
> not an agreement that HGL admits unknown enum values or must use that fallback.
> HGL must reject duplicate member numbers before registering the table; native
> registration is not a substitute for that source check.

## Excerpt 4

> No implicit integer conversion, flag-enum behaviour, or exemption from
> no-match failure is introduced by this agreement. Enum declarations and these
> design fixtures remain outside the implemented compiler surface.

## Excerpt 5

> A generic therefore sees a reference only where its signature writes `ref`.
> The compiler's inference is `GenericSubstitution::infer_from_argument` and
> `infer_from_result`; exact comparison is `unify`.

## Excerpt 6

> This is not implemented in composition bodies yet. The compiler currently
> rejects field or index access through `ref<T>` in every phase rather than
> silently reading a value. Simple reference forwarding and normal hgraph
> endpoint adaptation are supported.

## Excerpt 7

> The source spelling is lowercase `signal`. It is a contextual type marker that
> is legal only as the complete type of a non-`const` function or operator
> parameter. It cannot be nested, used as a field or result, declared `const`, or
> given a default value. Uppercase `SIGNAL` remains unknown in HGL. The generated
> C++ schema spelling is `hgraph::SIGNAL`.

## Excerpt 8

> The compiler still rejects a nested `ref<ref<T>>` boundary instead of
> relying on native REF normalization; that is a fail-closed implementation
> boundary, not a source-level decision.

## Excerpt 9

> This record does not settle native declaration syntax, reference construction
> or mutation operations, or additional restrictions on reference placement.
> Those remain separate discussion items. Implemented
> reference forms are exercised by `examples/reference-routing.hgl`; unresolved
> forms continue to fail closed.
