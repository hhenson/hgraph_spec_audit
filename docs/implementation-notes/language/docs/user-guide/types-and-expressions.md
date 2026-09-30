# Relocated notes: language/docs/user-guide/types-and-expressions.md

Source: [specification before separation](https://github.com/hhenson/hgraph_spec/blob/766033278bef6e9403cc99c0d8f318ba46a03919/language/docs/user-guide/types-and-expressions.md).

These excerpts preserve earlier implementation notes and their surrounding
context. They were not revalidated during relocation and do not assert current
support or define language behavior. The current specification owns the rules.
HGL source examples remain in the linked specification revision.

## Excerpt 1

> Native C++/Python mapping remains open. Enums are agreed design, not implemented
> compiler support; see the
> [paired examples](https://github.com/hhenson/hgraph/blob/main/language/docs/developer-guide/enum-cpp-mappings.md)
> and [Enum types](https://github.com/hhenson/hgraph_spec/blob/766033278bef6e9403cc99c0d8f318ba46a03919/language/docs/design/type-extensions.md#enum-types).

## Excerpt 2

> Status: `str(value)` is the agreed source spelling; these examples describe
> the target language contract, not implemented compiler support.

## Excerpt 3

> Status: partially implemented. Explicit `ref<T>` signatures, transparent
> underlying-type compatibility, opaque node access, forwarding, and fixed-list
> reference selection are available. Wiring-time access through a reference and
> imported native types remain compiler work. See
> [Type extensions](https://github.com/hhenson/hgraph_spec/blob/766033278bef6e9403cc99c0d8f318ba46a03919/language/docs/design/type-extensions.md) for the complete agreement.

## Excerpt 4

> Status: implemented for function and operator inputs. See
> [`signal` inputs](https://github.com/hhenson/hgraph_spec/blob/766033278bef6e9403cc99c0d8f318ba46a03919/language/docs/design/type-extensions.md#signal-inputs).

## Excerpt 5

> > **Implementation status:** declarations, type-generic applications,
> > abstract-only single inheritance, construction, optional fields, and sparse
> > delta syntax are implemented. Constructor inference, typed `const` generic
> > metadata, explicit optional-field clearing, and the remaining nested/runtime
> > forms are rejected as listed in the roadmap.

## Excerpt 6

> A value built here crosses back to `market.data` without conversion and both
> modules see one schema. The importing module never re-declares the struct:
> generated C++ refers to the exporter's own definition and includes its header.

## Excerpt 7

> An importing module needs the exporting module's descriptor, which the build
> supplies (`hgl check --module-descriptor`, or the `LINK_LIBRARIES` of
> `hgl_add_module`).

## Excerpt 8

> **What cannot be imported yet.** A struct an importer cannot rebuild whole is
> refused by name rather than rebuilt short, and today that includes any struct
> with a **field default other than `null`** — the descriptor records the
> default, but the catalog cannot yet reconstruct its value, so `Quote` above,
> with `currency: str = "USD"`, is not importable.

## Excerpt 9

> `= null` does cross, because it says the field is optional and carries no
> value to rebuild — and that is what lets a recursive struct import, since its
> edge must be declared `= null`. It crosses on the struct that **declares** the
> field, and on a child that merely inherits it. What does not cross is a child
> **overriding** an inherited default: the child's copy of the field is rebuilt
> from the parent's record, so an override would be lost rather than rebuilt
> short.

## Excerpt 10

> When multiple abstract parents contribute the same field name, its type and
> optionality must agree. Equal defaults merge. Different defaults, or a default
> from only one of otherwise compatible parents, require the child to choose an
> explicit default. A type or optionality conflict is always an error. The exact
> stable ordering rule for fields contributed by multiple parents will be fixed
> before this syntax is implemented.

## Excerpt 11

> Status: constructor inference is provisional. The rule below is agreed but
> not implemented: the compiler rejects a generic constructor without its
> explicit type arguments, so write `Box<f64>(value: 1.5)` today. The snippets
> in the rest of this subsection that omit the arguments are design fixtures,
> not accepted programs.

## Excerpt 12

> Status: `elements` is the element-iteration spelling for lists and sets. Like
> `for`, `keys`, `values`, and `items`, it follows the containing phase rather
> than itself forcing a runtime node. The compiler implements graph-phase
> `elements` and `items` over fixed temporal lists by expanding the body once per
> child connection; `items` also supplies its wiring-time `i64` index. Scalar
> wiring-time iterables and bundles remain future compiler work. Independent
> `values`/`items` bodies over maps and `elements`/`items` bodies over unbounded
> lists apply independently to each live key or index. Captured temporal
> inputs are available to every iteration.
> Graph-phase predicates, graph-phase `keys`, and `const` captures remain
> unsupported.
> Loop-carried reductions are initially unsupported; future map reductions are
> unordered, while lists may require the linear reduction option to preserve
> index order. See
> [Iteration](https://github.com/hhenson/hgraph_spec/blob/766033278bef6e9403cc99c0d8f318ba46a03919/language/docs/design/iteration.md) for examples, restrictions, and the
> deferred reduction option.

## Excerpt 13

> These calls currently take positional arguments. Indices are zero-based;
> window samples are ordered oldest to newest, including after wraparound.
> Missing keys, invalid child value reads, empty `front`/`back`, and out-of-range
> indices are errors. They do not fabricate default values. `contains` checks
> membership, not child validity. Atomic collection values still require further
> compiler support; this implemented slice uses structural time-series inputs.

## Excerpt 14

> The safe counterpart `get(value, key_or_index, default=null)` is accepted but
> not implemented yet. The nullable result and the treatment of a present
> but invalid child remain outstanding; see the
> [surface completion record](https://github.com/hhenson/hgraph_spec/blob/766033278bef6e9403cc99c0d8f318ba46a03919/language/docs/design/native-surface-proposal.md).
