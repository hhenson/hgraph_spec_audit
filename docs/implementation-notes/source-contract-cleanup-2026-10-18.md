# Source-language contracts and target mappings: notes relocated on 18 October 2026

Historical implementation material removed from the specification. These excerpts
were not revalidated and do not assert current support or define the standard.
Required behavior and open semantic decisions remain in the specification.

Source revision: `4f0facee5aaa9e26abfcecefe3f877110211ddad`. The [provenance manifest](source-contract-cleanup-2026-10-18.provenance.json)
records source hashes, excerpt locations and original text. Relative links in
excerpts resolve to that specification revision.

## language/docs/user-guide/types-and-expressions.md

### Excerpt 1

[Source, line 194](https://github.com/hhenson/hgraph_spec/blob/4f0facee5aaa9e26abfcecefe3f877110211ddad/language/docs/user-guide/types-and-expressions.md#L194).

> This is Python-style call spelling, not a blanket agreement on Python's
> formatting, encoding arguments, implicit conversions, or custom `__str__`
> methods. The enum member-name rule is unchanged. Existing reference opacity and
> `signal` payload restrictions also remain: conversion is not an escape from
> them. See the [HGL/C++ mappings](https://github.com/hhenson/hgraph/blob/main/language/docs/developer-guide/enum-cpp-mappings.md#conversion-in-nodes-and-graphs).

### Excerpt 2

[Source, line 1389](https://github.com/hhenson/hgraph_spec/blob/4f0facee5aaa9e26abfcecefe3f877110211ddad/language/docs/user-guide/types-and-expressions.md#L1389).

> error behavior independently of C++ debug or release settings.

### Excerpt 3

[Source, line 202](https://github.com/hhenson/hgraph_spec/blob/4f0facee5aaa9e26abfcecefe3f877110211ddad/language/docs/user-guide/types-and-expressions.md#L202).

> The temporal scalars are hgraph's RFC 0002 core types.

## language/docs/user-guide/functions.md

### Excerpt 1

[Source, line 80](https://github.com/hhenson/hgraph_spec/blob/4f0facee5aaa9e26abfcecefe3f877110211ddad/language/docs/user-guide/functions.md#L80).

> includes an HGL caller and expected C++ lowering.

### Excerpt 2

[Source, line 838](https://github.com/hhenson/hgraph_spec/blob/4f0facee5aaa9e26abfcecefe3f877110211ddad/language/docs/user-guide/functions.md#L838).

> agreed design; compiler implementation remains separate work. See

### Excerpt 3

[Source, line 940](https://github.com/hhenson/hgraph_spec/blob/4f0facee5aaa9e26abfcecefe3f877110211ddad/language/docs/user-guide/functions.md#L940).

> finite-schedule progress must survive recovery; current native parity alone
> does not establish that guarantee.

### Excerpt 4

[Source, line 1163](https://github.com/hhenson/hgraph_spec/blob/4f0facee5aaa9e26abfcecefe3f877110211ddad/language/docs/user-guide/functions.md#L1163).

> responsibility of C++ extensions.

## language/docs/user-guide/README.md

### Excerpt 1

[Source, line 118](https://github.com/hhenson/hgraph_spec/blob/4f0facee5aaa9e26abfcecefe3f877110211ddad/language/docs/user-guide/README.md#L118).

> adaptors remain C++ extension responsibilities.

## language/docs/developer-guide/syntax-and-semantics.md

### Excerpt 1

[Source, line 664](https://github.com/hhenson/hgraph_spec/blob/4f0facee5aaa9e26abfcecefe3f877110211ddad/language/docs/developer-guide/syntax-and-semantics.md#L664).

> `zoned_time` is not part of RFC 0002. It is the language's one hgraph-side
> addition to the temporal types: a core scalar (`CivilTime` plus `ZoneId`,
> registered name `zoned_time`) with the resolution operations listed below, a
> JSON form of the time followed by the bracketed zone, and a Python wrapper.
> It is tracked with the other hgraph-side requirements in the roadmap until an
> RFC promotes it.

### Excerpt 2

[Source, line 746](https://github.com/hhenson/hgraph_spec/blob/4f0facee5aaa9e26abfcecefe3f877110211ddad/language/docs/developer-guide/syntax-and-semantics.md#L746).

>   a value silently read as UTC, and Python's naive-means-UTC convention never

### Excerpt 3

[Source, line 838](https://github.com/hhenson/hgraph_spec/blob/4f0facee5aaa9e26abfcecefe3f877110211ddad/language/docs/developer-guide/syntax-and-semantics.md#L838).

> as Python `date` arithmetic and hgraph's operators do:

### Excerpt 4

[Source, line 1557](https://github.com/hhenson/hgraph_spec/blob/4f0facee5aaa9e26abfcecefe3f877110211ddad/language/docs/developer-guide/syntax-and-semantics.md#L1557).

> This agreement covers the one-value Python-style spelling, not Python's
> additional `str` forms or an unrestricted guarantee of Python formatting.

### Excerpt 5

[Source, line 1562](https://github.com/hhenson/hgraph_spec/blob/4f0facee5aaa9e26abfcecefe3f877110211ddad/language/docs/developer-guide/syntax-and-semantics.md#L1562).

> operation. No compiler or runtime implementation is changed by this record.

### Excerpt 6

[Source, line 1898](https://github.com/hhenson/hgraph_spec/blob/4f0facee5aaa9e26abfcecefe3f877110211ddad/language/docs/developer-guide/syntax-and-semantics.md#L1898).

> The compiler may consume these calls while deriving node input policies, so
> they need not remain as runtime calls in generated C++. `valid(value)` tests

### Excerpt 7

[Source, line 1473](https://github.com/hhenson/hgraph_spec/blob/4f0facee5aaa9e26abfcecefe3f877110211ddad/language/docs/developer-guide/syntax-and-semantics.md#L1473).

> lower to native C++ control flow; temporal graph dispatch uses native `switch_`
> with the same capture, result-schema, REF adaptation, and continuation analysis

### Excerpt 8

[Source, line 876](https://github.com/hhenson/hgraph_spec/blob/4f0facee5aaa9e26abfcecefe3f877110211ddad/language/docs/developer-guide/syntax-and-semantics.md#L876).

> other call, not syntax. The zone operations are hgraph's:

### Excerpt 9

[Source, line 879](https://github.com/hhenson/hgraph_spec/blob/4f0facee5aaa9e26abfcecefe3f877110211ddad/language/docs/developer-guide/syntax-and-semantics.md#L879).

> (hgraph's `resolve_civil`, with the same policy enumerations), and, as a
> roadmap ask, `resolve(date, zoned_time, ambiguous:, nonexistent:)`,

### Excerpt 10

[Source, line 868](https://github.com/hhenson/hgraph_spec/blob/4f0facee5aaa9e26abfcecefe3f877110211ddad/language/docs/developer-guide/syntax-and-semantics.md#L868).

> runtime raises through hgraph's checked temporal arithmetic; the language's
> runtime scalar error behaviour is an open question shared with the numeric

## language/docs/design/type-extensions.md

### Excerpt 1

[Source, line 19](https://github.com/hhenson/hgraph_spec/blob/4f0facee5aaa9e26abfcecefe3f877110211ddad/language/docs/design/type-extensions.md#L19).

> uses the agreed Python-style `str(value)` spelling.

### Excerpt 2

[Source, line 65](https://github.com/hhenson/hgraph_spec/blob/4f0facee5aaa9e26abfcecefe3f877110211ddad/language/docs/design/type-extensions.md#L65).

> The assigned numbers are `-1`, `0`, and `1`. The
> [range and overflow examples](https://github.com/hhenson/hgraph/blob/main/language/docs/developer-guide/enum-cpp-mappings.md#signed-range-and-overflow)
> also cover both endpoints, a reset after the maximum, and rejected values.

### Excerpt 3

[Source, line 70](https://github.com/hhenson/hgraph_spec/blob/4f0facee5aaa9e26abfcecefe3f877110211ddad/language/docs/design/type-extensions.md#L70).

> resolved signed number and each required automatic increment before native
> emission; do not inherit C++ literal or overflow behavior accidentally.

### Excerpt 4

[Source, line 80](https://github.com/hhenson/hgraph_spec/blob/4f0facee5aaa9e26abfcecefe3f877110211ddad/language/docs/design/type-extensions.md#L80).

> that name unambiguous within an enum. The source call uses Python-style
> `str(value)`:

### Excerpt 5

[Source, line 87](https://github.com/hhenson/hgraph_spec/blob/4f0facee5aaa9e26abfcecefe3f877110211ddad/language/docs/design/type-extensions.md#L87).

> This produces the constant string `"first"`. The spelling follows Python;
> it does not change the agreed enum representation to Python's qualified enum
> display or require Python execution. `str` remains the string type name in
> type positions and is the conversion operation in this expression position.

### Excerpt 6

[Source, line 94](https://github.com/hhenson/hgraph_spec/blob/4f0facee5aaa9e26abfcecefe3f877110211ddad/language/docs/design/type-extensions.md#L94).

> [Numbered source examples and C++ mappings](https://github.com/hhenson/hgraph/blob/main/language/docs/developer-guide/enum-cpp-mappings.md)
> show explicit values, automatic values starting at zero, stringification,
> and duplicate-number errors. The positive and intentionally invalid HGL
> declarations are also in the [standard-library design corpus](https://github.com/hhenson/hgraph/blob/main/language/stdlib/README.md#enum-values).

### Excerpt 7

[Source, line 153](https://github.com/hhenson/hgraph_spec/blob/4f0facee5aaa9e26abfcecefe3f877110211ddad/language/docs/design/type-extensions.md#L153).

> already-typed native enum value arriving through an import boundary. The
> [paired HGL/C++ conversion examples](https://github.com/hhenson/hgraph/blob/main/language/docs/developer-guide/enum-cpp-mappings.md#checked-conversion-into-an-enum)
> include successful lookups and rejected constants. Compiler support remains
> separate work.

### Excerpt 8

[Source, line 210](https://github.com/hhenson/hgraph_spec/blob/4f0facee5aaa9e26abfcecefe3f877110211ddad/language/docs/design/type-extensions.md#L210).

> [switch coverage](https://github.com/hhenson/hgraph_spec/blob/4f0facee5aaa9e26abfcecefe3f877110211ddad/language/docs/design/switch.md#duplicate-cases-and-enum-coverage) and the
> [paired HGL/C++ examples](https://github.com/hhenson/hgraph/blob/main/language/docs/developer-guide/enum-switch-cpp-mappings.md).

### Excerpt 9

[Source, line 189](https://github.com/hhenson/hgraph_spec/blob/4f0facee5aaa9e26abfcecefe3f877110211ddad/language/docs/design/type-extensions.md#L189).

> declared member. The [out-of-order numbering example](https://github.com/hhenson/hgraph/blob/main/language/docs/developer-guide/enum-cpp-mappings.md#declaration-order-enumeration)
> makes this distinction explicit.

### Excerpt 10

[Source, line 198](https://github.com/hhenson/hgraph_spec/blob/4f0facee5aaa9e26abfcecefe3f877110211ddad/language/docs/design/type-extensions.md#L198).

> Compiler support for enum enumeration remains separate work.

## language/docs/design/operators.md

### Excerpt 1

[Source, line 33](https://github.com/hhenson/hgraph_spec/blob/4f0facee5aaa9e26abfcecefe3f877110211ddad/language/docs/design/operators.md#L33).

> Floor-based modulo, not C++ truncating remainder.

### Excerpt 2

[Source, line 190](https://github.com/hhenson/hgraph_spec/blob/4f0facee5aaa9e26abfcecefe3f877110211ddad/language/docs/design/operators.md#L190).

> scalar operation. See the [paired HGL/C++ examples](https://github.com/hhenson/hgraph/blob/main/language/docs/developer-guide/operator-cpp-mappings.md).

### Excerpt 3

[Source, line 192](https://github.com/hhenson/hgraph_spec/blob/4f0facee5aaa9e26abfcecefe3f877110211ddad/language/docs/design/operators.md#L192).

> The executable [operator module](https://github.com/hhenson/hgraph_std/blob/main/hgl/hgraph/operators.hgl) declares
> the 16 arithmetic/comparison/Boolean hooks (including floor division),
> delegates implementations to production native candidates, and materializes
> the supported primitive combinations. The native-call requirements therefore
> belong to those delegating `impl fn` candidates, not the public contracts. Its
> `hgraph.operators.*` identities are parallel migration contracts, not
> replacements for the native system identities.

## language/docs/design/iteration.md

### Excerpt 1

[Source, line 20](https://github.com/hhenson/hgraph_spec/blob/4f0facee5aaa9e26abfcecefe3f877110211ddad/language/docs/design/iteration.md#L20).

> Describes one child graph per key or index through native mapping.

### Excerpt 2

[Source, line 40](https://github.com/hhenson/hgraph_spec/blob/4f0facee5aaa9e26abfcecefe3f877110211ddad/language/docs/design/iteration.md#L40).

> descriptor. Runtime-node traversal uses the same source model over hgraph's
> existing `Args<>`/TSL and `Kwargs<>`/TSB input views. Positional `items` converts
> the private one-based field numbering to a zero-based HGL `i64` index.

### Excerpt 3

[Source, line 49](https://github.com/hhenson/hgraph_spec/blob/4f0facee5aaa9e26abfcecefe3f877110211ddad/language/docs/design/iteration.md#L49).

> agreed source behavior awaiting enum/compiler support, not an expansion of
> dynamic graph-loop lowering.

### Excerpt 4

[Source, line 88](https://github.com/hhenson/hgraph_spec/blob/4f0facee5aaa9e26abfcecefe3f877110211ddad/language/docs/design/iteration.md#L88).

> An illustrative native realization is recorded in the audit:
>
> [Native example 1](https://github.com/hhenson/hgraph_spec_audit/blob/main/examples/documentation/language/docs/design/iteration.md#example-1)

### Excerpt 5

[Source, line 126](https://github.com/hhenson/hgraph_spec/blob/4f0facee5aaa9e26abfcecefe3f877110211ddad/language/docs/design/iteration.md#L126).

> An illustrative C++ mapping uses the existing public added-member range:
>
> [Native example 2](https://github.com/hhenson/hgraph_spec_audit/blob/main/examples/documentation/language/docs/design/iteration.md#example-2)

### Excerpt 6

[Source, line 131](https://github.com/hhenson/hgraph_spec/blob/4f0facee5aaa9e26abfcecefe3f877110211ddad/language/docs/design/iteration.md#L131).

> tick produces no output tick. The loop counts scalar members in the native
> delta range, without imposing set order or wiring a child graph per member.
> The count is evaluation-local, not persistent state or a graph reduction.
> These C++ illustrations can be syntax-checked independently of HGL support;
> they are not new native graph execution tests.

### Excerpt 7

[Source, line 141](https://github.com/hhenson/hgraph_spec/blob/4f0facee5aaa9e26abfcecefe3f877110211ddad/language/docs/design/iteration.md#L141).

> initial design lowers the loop through the native map machinery: one child
> graph per map key or dynamic-list index, with membership controlling child

### Excerpt 8

[Source, line 156](https://github.com/hhenson/hgraph_spec/blob/4f0facee5aaa9e26abfcecefe3f877110211ddad/language/docs/design/iteration.md#L156).

> Here the body is outputless, so the lowering uses a sink map. The runnable

### Excerpt 9

[Source, line 168](https://github.com/hhenson/hgraph_spec/blob/4f0facee5aaa9e26abfcecefe3f877110211ddad/language/docs/design/iteration.md#L168).

> the native lifetime protocol. Surviving children retain their own node state.

## language/docs/design/control-flow.md

### Excerpt 1

[Source, line 407](https://github.com/hhenson/hgraph_spec/blob/4f0facee5aaa9e26abfcecefe3f877110211ddad/language/docs/design/control-flow.md#L407).

> The runnable [conditional-sinks.hgl](https://github.com/hhenson/hgraph_spec/blob/4f0facee5aaa9e26abfcecefe3f877110211ddad/language/examples/conditional-sinks.hgl)
> example exercises this wiring model in both compiler backends.

### Excerpt 2

[Source, line 487](https://github.com/hhenson/hgraph_spec/blob/4f0facee5aaa9e26abfcecefe3f877110211ddad/language/docs/design/control-flow.md#L487).

> agreement does not require new source-level closure syntax. The initial
> implementation gives both generated branches one consistent explicit temporal
> signature formed from the stable first-use union. Unused branch parameters are
> marked in generated C++, and hgraph's switch boundary binds the same slots to
> both branches. Scalar specialization and the more selective native
> capture-boundary form remain later work.

## language/docs/design/switch.md

### Excerpt 1

[Source, line 8](https://github.com/hhenson/hgraph_spec/blob/4f0facee5aaa9e26abfcecefe3f877110211ddad/language/docs/design/switch.md#L8).

> Compiler implementation remains separate work.

### Excerpt 2

[Source, line 10](https://github.com/hhenson/hgraph_spec/blob/4f0facee5aaa9e26abfcecefe3f877110211ddad/language/docs/design/switch.md#L10).

> [Paired HGL and C++ examples](https://github.com/hhenson/hgraph/blob/main/language/docs/developer-guide/control-flow-cpp-mappings.md)
> describe node and graph scenarios, captures and results, defaults and failures,
> sinks, early returns, and state lifetime. The source examples also live in the
> [standard-library design corpus](https://github.com/hhenson/hgraph_spec/blob/4f0facee5aaa9e26abfcecefe3f877110211ddad/language/stdlib/examples/switch-scenarios.hgl).

### Excerpt 3

[Source, line 112](https://github.com/hhenson/hgraph_spec/blob/4f0facee5aaa9e26abfcecefe3f877110211ddad/language/docs/design/switch.md#L112).

> [Paired enum-switch HGL/C++ examples](https://github.com/hhenson/hgraph/blob/main/language/docs/developer-guide/enum-switch-cpp-mappings.md)
> cover exhaustive and partial dispatch, a supplied default, and intentional
> duplicate/type errors. No new source syntax or compiler implementation is
> introduced by these checks.

### Excerpt 4

[Source, line 127](https://github.com/hhenson/hgraph_spec/blob/4f0facee5aaa9e26abfcecefe3f877110211ddad/language/docs/design/switch.md#L127).

> Wire native `switch_` with generated branch callables and boundary signatures.

### Excerpt 5

[Source, line 142](https://github.com/hhenson/hgraph_spec/blob/4f0facee5aaa9e26abfcecefe3f877110211ddad/language/docs/design/switch.md#L142).

> For a temporal graph switch, the selector must bind to the native `switch_`
> scalar-key input, and the case values must be compatible with the selected key
> contract. The native input is `TS<ScalarVar<K>>`; source compatibility and any
> REF binding adaptation must use the existing type and wiring rules.

### Excerpt 6

[Source, line 154](https://github.com/hhenson/hgraph_spec/blob/4f0facee5aaa9e26abfcecefe3f877110211ddad/language/docs/design/switch.md#L154).

> is not fixed here. A backend's ability to emit a particular C++ statement is
> not by itself evidence that every source type has a valid switch-key contract.

### Excerpt 7

[Source, line 157](https://github.com/hhenson/hgraph_spec/blob/4f0facee5aaa9e26abfcecefe3f877110211ddad/language/docs/design/switch.md#L157).

> ## Node-style lowering to C++
>
> A node-style switch must lower to native C++ dispatch within the generated
> node's evaluation code. It must not require Python execution or create a
> graph-level `switch_` merely to implement local control flow.
>
> The generated C++ may use a C++ `switch` where the admitted selector and case
> types permit that statement. For other admitted types, equivalent native C++
> comparison-based dispatch may be needed. This is a code-generation distinction,
> not an agreement to admit additional selector types or new source syntax.

### Excerpt 8

[Source, line 187](https://github.com/hhenson/hgraph_spec/blob/4f0facee5aaa9e26abfcecefe3f877110211ddad/language/docs/design/switch.md#L187).

>    escaping assignments. Zero results use the native outputless switch path;

### Excerpt 9

[Source, line 196](https://github.com/hhenson/hgraph_spec/blob/4f0facee5aaa9e26abfcecefe3f877110211ddad/language/docs/design/switch.md#L196).

> also apply. Underlying type compatibility must not hide mismatched native
> bundle fields. If the public native API cannot express a required adaptation,
> the compiler must reject that lowering until the support exists.

## language/docs/design/decisions/0006-multi-file-module-parts.md

### Excerpt 1

[Source, line 42](https://github.com/hhenson/hgraph_spec/blob/4f0facee5aaa9e26abfcecefe3f877110211ddad/language/docs/design/decisions/0006-multi-file-module-parts.md#L42).

> The command line names additional files explicitly with repeatable `--part`
> options. `hgl_add_module()` exposes the same contract with one anchor in `HGL`
> and the remaining files in `PARTS`. The anchor filename determines generated
> artifact names; it does not receive special source visibility or affect the
> module identity.

### Excerpt 2

[Source, line 53](https://github.com/hhenson/hgraph_spec/blob/4f0facee5aaa9e26abfcecefe3f877110211ddad/language/docs/design/decisions/0006-multi-file-module-parts.md#L53).

> - A large library can have one module descriptor, generated C++ namespace,

## language/docs/design/decisions/0007-parameter-packs.md

### Excerpt 1

[Source, line 45](https://github.com/hhenson/hgraph_spec/blob/4f0facee5aaa9e26abfcecefe3f877110211ddad/language/docs/design/decisions/0007-parameter-packs.md#L45).

> specificity is fixed arity before a homogeneous pack before a heterogeneous
> positional pack. HGL emits `In`/`VarIn`/`VarKwIn` selectors and does not
> reimplement native overload ranking.

### Excerpt 2

[Source, line 51](https://github.com/hhenson/hgraph_spec/blob/4f0facee5aaa9e26abfcecefe3f877110211ddad/language/docs/design/decisions/0007-parameter-packs.md#L51).

> The positional heterogeneous view behaves as `tuple<...>` even if generated
> C++ uses a private bundle representation:

### Excerpt 3

[Source, line 74](https://github.com/hhenson/hgraph_spec/blob/4f0facee5aaa9e26abfcecefe3f877110211ddad/language/docs/design/decisions/0007-parameter-packs.md#L74).

> Runtime packs use hgraph's existing structural node inputs; HGL does not define
> a second aggregate ABI:
>
> | HGL parameter | Generated C++ node input | HGL source view |
> | --- | --- | --- |
> | `values: ...T` | `In<"values", Args<S>>` where `S` is the temporal schema for `T` | fixed homogeneous list |
> | `values: ...Ts` | `In<"values", Kwargs<...>>` with private `_1`, `_2`, ... fields | heterogeneous tuple |
> | `values: ...{Fields}` | `In<"values", Kwargs<...>>` with the supplied field names | heterogeneous bundle |
>
> `Args` is resolved by hgraph as a fixed `TSL` and `Kwargs` as an unnamed TSB.
> The existing `TSLInputView` and `TSBInputView` own runtime traversal, child
> validity and modification metadata, and evaluation-local borrowing. The HGL
> compiler is responsible only for lowering to those selectors and preserving the
> source abstraction. In particular, positional `items(values)` returns a
> zero-based `i64` index even though its private C++ field is numbered from `_1`.

### Excerpt 4

[Source, line 92](https://github.com/hhenson/hgraph_spec/blob/4f0facee5aaa9e26abfcecefe3f877110211ddad/language/docs/design/decisions/0007-parameter-packs.md#L92).

> runtime function is diagnosed before C++ emission until the native static-node
> ABI can bind two independent aggregate inputs.

### Excerpt 5

[Source, line 97](https://github.com/hhenson/hgraph_spec/blob/4f0facee5aaa9e26abfcecefe3f877110211ddad/language/docs/design/decisions/0007-parameter-packs.md#L97).

> This requires the core runtime to represent a fixed-empty `TSL` separately from
> an unbounded `TSL`: the unbounded extent uses hgraph's original `-1` sentinel,
> leaving zero as an ordinary fixed extent. Runtime-node pack lowering is
> available because the core contract preserves this distinction.

### Excerpt 6

[Source, line 158](https://github.com/hhenson/hgraph_spec/blob/4f0facee5aaa9e26abfcecefe3f877110211ddad/language/docs/design/decisions/0007-parameter-packs.md#L158).

> immutable borrowed handle which lowers directly to each existing C++ child
> endpoint's `TSValueTypeMetaData`. The view preserves the pack's tuple or bundle

## language/docs/design/decisions/0008-temporal-contracts-and-target-mappings.md

### Excerpt 1

[Source, line 68](https://github.com/hhenson/hgraph_spec/blob/4f0facee5aaa9e26abfcecefe3f877110211ddad/language/docs/design/decisions/0008-temporal-contracts-and-target-mappings.md#L68).

> ### HGL example and C++ expectation

### Excerpt 2

[Source, line 83](https://github.com/hhenson/hgraph_spec/blob/4f0facee5aaa9e26abfcecefe3f877110211ddad/language/docs/design/decisions/0008-temporal-contracts-and-target-mappings.md#L83).

> The expected C++ shape is a plain value helper called by the containing node's
> evaluation hook, not another node. Illustrative lowering, not current emitter
> output:
>
> [Native example 1](https://github.com/hhenson/hgraph_spec_audit/blob/main/examples/documentation/language/docs/design/decisions/0008-temporal-contracts-and-target-mappings.md#example-1)

## language/docs/design/decisions/0012-recursive-struct-fields.md

### Excerpt 1

[Source, line 136](https://github.com/hhenson/hgraph_spec/blob/4f0facee5aaa9e26abfcecefe3f877110211ddad/language/docs/design/decisions/0012-recursive-struct-fields.md#L136).

>   the graph in the parity corpus, observed through scalar `eval` results,
>   with identical ticks from direct wiring and generated C++;
