# Relocated notes: language/docs/design/language-model.md

Source: [specification before separation](https://github.com/hhenson/hgraph_spec/blob/766033278bef6e9403cc99c0d8f318ba46a03919/language/docs/design/language-model.md).

These excerpts preserve earlier implementation notes and their surrounding
context. They were not revalidated during relocation and do not assert current
support or define language behavior. The current specification owns the rules.
HGL source examples remain in the linked specification revision.

## Excerpt 1

> The [User Guide](https://github.com/hhenson/hgraph_spec/blob/766033278bef6e9403cc99c0d8f318ba46a03919/language/docs/user-guide/README.md) is authoritative for observable
> source behavior. The
> [Developer Guide](https://github.com/hhenson/hgraph_spec/blob/766033278bef6e9403cc99c0d8f318ba46a03919/language/docs/developer-guide/syntax-and-semantics.md) records the
> proposed grammar and compiler boundaries.

## Excerpt 2

> HGL is a temporal programming language: values, change, validity, activation,
> and history form its programming model. The agreed direction for value-level
> functions, reconstructible caches, and native type/target contracts is in
> [ADR 0008](https://github.com/hhenson/hgraph_spec/blob/766033278bef6e9403cc99c0d8f318ba46a03919/language/docs/design/decisions/0008-temporal-contracts-and-target-mappings.md). Its
> unimplemented extensions are distinguished from the current model below.

## Excerpt 3

> The agreed, not-yet-implemented `const fn` extension declares direct
> value-level functions. It does not add `graph` or `node` keywords or alter
> parameter-level `const`. Modifier combinations with `impl`, `native`, and
> `export` remain open; see [value-level functions](https://github.com/hhenson/hgraph_spec/blob/766033278bef6e9403cc99c0d8f318ba46a03919/language/docs/user-guide/functions.md#value-level-functions).

## Excerpt 4

> Ordinary temporal `fn` results are temporal unless the function is outputless.
> The agreed `const fn` extension instead returns a value, which may be computed
> at wiring time or inside a runtime node when the helper's phase contract
> permits. It is not yet implemented.

## Excerpt 5

> One struct declaration supplies the value schema and temporal shape that
> Python currently expresses separately as `CompoundScalar` and
> `TimeSeriesSchema`:

## Excerpt 6

> The runtime already supports sparse TSB delta fields through Bundle validity.
> Explicit optional-field clearing still needs a distinct public native
> operation or delta encoding, because the existing unset delta field means no
> change. The compiler must preserve that distinction through checked HIR and
> reject the clear form until its native contract exists.

## Excerpt 7

> The language preserves this symbolic type information through checked HIR.
> Code generation may use one erased implementation when the body uses only
> operations valid for every admitted substitution, or specialize an
> implementation when representation-specific code is required. This is an
> implementation decision: source generics remain statically substituted in
> both cases.

## Excerpt 8

> Retention does not imply that a resolved generic value is available to the
> body. A retained marker used only in a signature is type-erased after resolver
> matching; a retained generic referenced by the body must be reified through a
> defined read-only contract. The first implemented retained marker is a fixed
> list size, lowered to hgraph's named `SIZE` variable. Generic reification and
> residual constraints are deliberately unresolved rather than simulated by
> runtime schema inspection.

## Excerpt 9

> The compiler implements this rule for local and selectively imported operator
> contracts. Imported contracts retain their external C++ marker and nominal
> identity through both IRs. The import catalog rejects unsupported contract
> constraints, properties, generic packs, and type shapes before registration;
> see `src/descriptor/import_catalog.cpp` and the imported-operator codegen tests.

## Excerpt 10

> The target module model gives every compiled HGL module compiler-generated
> initialization and deinitialization entry points. The current implementation
> provides that versioned lifecycle ABI for dynamically loaded scripted modules;
> AOT output currently provides its descriptor and explicit
> `register_operators()` entry point while the linked application owns its
> lifetime. Completing the AOT lifecycle bootstrap remains compiler work.
> Initialization records a keyed installer for all type and operator
> contributions, including the concrete candidates produced by `instantiate`;
> the installer can be replayed after an hgraph registry reset
> without repeating one-time module initialization. The final application
> explicitly initializes the complete target closure before wiring.

## Excerpt 11

> Selected implementations give wired graphs and cached plans a lease on their
> provider. A module cannot complete deinitialization, and its native image cannot
> be unloaded, while such a lease is live. Logical registration removal and
> physical library unloading are therefore distinct; the first implementation
> may keep removed native images resident for process lifetime.

## Excerpt 12

> Under the agreed [iteration model](https://github.com/hhenson/hgraph_spec/blob/766033278bef6e9403cc99c0d8f318ba46a03919/language/docs/design/iteration.md), `for`, `keys`, `values`,
> `elements`, and `items` follow the containing phase and do not themselves force runtime
> classification. The classifier and typed HIR implement this rule; backend
> support reaches fixed temporal-list traversal and independent map/list bodies
> over dynamic maps and unbounded lists.

## Excerpt 13

> A graph `if` with a temporal Boolean condition uses native switch-style child
> execution, following the Arrow API. It remains graph composition: the graph
> wires the conditional once and the native switch manages branch execution.
> A wiring-time Boolean still selects which branch to wire, and a conditional
> inside node evaluation remains ordinary runtime control flow. See
> [Conditional control flow](https://github.com/hhenson/hgraph_spec/blob/766033278bef6e9403cc99c0d8f318ba46a03919/language/docs/design/control-flow.md) for this agreed strategy and its
> implementation status.

## Excerpt 14

> The agreed [explicit switch model](https://github.com/hhenson/hgraph_spec/blob/766033278bef6e9403cc99c0d8f318ba46a03919/language/docs/design/switch.md) follows the same phase split:
> wiring-time selection during composition, native `switch_` with branch capture
> and result analysis for a temporal graph selector, and local C++ dispatch
> inside a node. Selector suitability is checked before lowering. `default: ...`
> handles unmatched values; no match without a default fails. The agreed form
> is `switch selector { case value: ... default: ... }`, with source-expressible
> constant case values and no implicit fallthrough. Implementation remains
> separate work. [Enum support](https://github.com/hhenson/hgraph_spec/blob/766033278bef6e9403cc99c0d8f318ba46a03919/language/docs/design/type-extensions.md#enum-types), including named
> member constants for cases, uses the agreed `enum Mode { first, second }`
> declaration and `Mode::first` reference form. An explicit `= constant` assigns
> an integer number; otherwise the first member starts at zero and later
> members increment the preceding number. Numbers use the signed `i64` range,
> including negative values; out-of-range explicit numbers and automatic
> successor overflow are compile-time errors without wrapping. An explicit
> assignment may restart numbering after the maximum. Duplicate numbers are
> rejected initially. This source range does not settle the native ABI.
> Stringification returns the member name without a type prefix or
> number, using the agreed `str(value)` call spelling. Constant, node-value, and
> temporal graph conversions follow the existing phase distinction; the call
> does not select the function's phase. Enums remain distinct atomic scalar
> types; integer conversion is explicit rather than implicit. Construction from
> an integer or exact member-name string uses the enum type as the callee, such
> as `Mode(10)` or `Mode("first")`. Unknown numbers and names are conversion
> errors at checking, wiring, or evaluation time as appropriate to the operand;
> they never create unnamed members. Enumeration calls `keys(Mode)`,
> `values(Mode)`, and `elements(Mode)` return immutable fixed-size scalar lists
> of names, assigned integers, and enum instances. All three use declaration
> order and the declared member count. They are constant data that can be bound,
> indexed, reused, and iterated during wiring, not time-series ports or borrowed
> node iterators. Enum switches reject duplicate resolved cases and can establish
> exhaustiveness by covering every declared member. Partial coverage remains
> permitted with default-or-failure semantics; even exhaustive generated dispatch
> retains no-match failure. These checks apply in both phases and do not replace
> definite assignment. Remaining conversion details and native mapping stay open.

## Excerpt 15

> Multiple `when` blocks are independent ordered conditions. The compiler uses
> the union of their activation dependencies and the validity requirements common
> to all handlers as the most permissive safe node-level policy. It lowers each
> remaining predicate to a C++ `if` in source order. Later handlers observe state
> and output changes made by earlier handlers.

## Excerpt 16

> - `i64` overflow, conversion, and division behavior;
> - NaN comparison;
> - destructuring and copy-with-update syntax; recursive struct fields are
>   agreed in [ADR 0012](https://github.com/hhenson/hgraph_spec/blob/766033278bef6e9403cc99c0d8f318ba46a03919/language/docs/design/decisions/0012-recursive-struct-fields.md) and are
>   rejected by the compiler until it is implemented;
> - runtime type tests, concrete downcasts, exhaustive abstract-family matching,
>   the temporal base-projection spelling, and multiple-parent field ordering;
> - explicit generic arguments on function and operator calls, generic parameter
>   defaults, partial generic type application, and any specialization
>   relationship beyond invariant applied types and the defined pattern ranking
>   and ambiguity rule;
> - general anonymous capture beyond inline runtime collection predicates;
> - rolling-window iteration and a parameter spelling that accepts either
>   window kind;
> - an explicit end bound and approximate comparison for `eval`, delta
>   spellings for set, map, and list harness elements, and tuple construction
>   from temporal values;
> - collection delta literals and the native encoding for explicit optional-field
>   clearing;
> - remaining phase/effect and modifier rules for value-level `const fn`,
>   non-scalar cache storage, native type/target mappings, lifecycle
>   output access, and sinks; the agreed direction is in
>   [ADR 0008](https://github.com/hhenson/hgraph_spec/blob/766033278bef6e9403cc99c0d8f318ba46a03919/language/docs/design/decisions/0008-temporal-contracts-and-target-mappings.md).

## Excerpt 17

> [#767](https://github.com/hhenson/hgraph/issues/767) item 6 owns the
> decisions below. Each entry records what the compiler does today as observed
> behavior; none of it is an agreed language rule until its design record
> exists, and a backend description is not a substitute for one.

## Excerpt 18

> - **Error model for runtime nodes.** Decided
>   ([ADR 0009](https://github.com/hhenson/hgraph_spec/blob/766033278bef6e9403cc99c0d8f318ba46a03919/language/docs/design/decisions/0009-native-errors-and-the-node-error-model.md)): a
>   raise, from a `throws` native, a strict intrinsic or a delegated native
>   operator, ends the evaluation under hgraph's node error model. Earlier
>   writes in that evaluation stand; a captured error output ticks a
>   `NodeError`, otherwise the exception propagates. HGL has no exception
>   surface of its own.
> - **Integer division, overflow, and NaN.** `i64 / i64` is typed `f64` by the
>   checker (`src/ir/type_check.cpp`, `arithmetic_result`) and folded as a
>   `Float` division (compiler-and-lowering.md, "Bodies"); the other operators
>   on two `i64` operands stay `i64`. A constant `i64` overflow and a constant
>   zero divisor are diagnostics at fold time; runtime overflow, runtime
>   division by zero, `%` on negative operands, and NaN comparison are
>   undefined.
> - **String operators.** `str + str` is typed `str` and folds to
>   concatenation, and constant `str` comparisons fold. Equality and ordering
>   of temporal strings, indexing, length, and Unicode normalization are
>   undefined.
> - **First-tick validity.** `valid(out)` before the node's first output and
>   `last_modified(x)` before `x` first ticks return whatever hgraph's endpoint
>   returns; the language states nothing.
> - **Descriptor parameter `kind`.** Format v1 writes `"kind": "signal"` for
>   every temporal parameter and `"const"` for a `const` one, so the label
>   collides with the `signal` type. A rename is a format v2 decision with
>   reader compatibility.
> - **`elements` and `values`.** `elements` traverses lists and sets; `values`
>   projects values from keyed or named structures. They are distinct operations,
>   not compatibility aliases ([Iteration](https://github.com/hhenson/hgraph_spec/blob/766033278bef6e9403cc99c0d8f318ba46a03919/language/docs/design/iteration.md)).
> - **Type-keyword callees.** `str(...)` and `Mode(...)` need a grammar rule for
>   a type keyword or type name in callee position; today `str` is not an
>   expression start and `Mode(...)` is an ordinary call to an unknown name.

## Excerpt 19

> Diagnostics should identify the source concept and expanded hgraph shape while
> preserving candidate rejection reasons from hgraph.
