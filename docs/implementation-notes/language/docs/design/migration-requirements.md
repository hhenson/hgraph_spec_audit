# Relocated notes: language/docs/design/migration-requirements.md

Source: [specification before separation](https://github.com/hhenson/hgraph_spec/blob/766033278bef6e9403cc99c0d8f318ba46a03919/language/docs/design/migration-requirements.md).

These excerpts preserve earlier implementation notes and their surrounding
context. They were not revalidated during relocation and do not assert current
support or define language behavior. The current specification owns the rules.
HGL source examples remain in the linked specification revision.

## Excerpt 1

> Status: accepted ledger, extracted from PR #801 on 2026-09-17 and verified
> against `main`. It is the definition of the `HGL-MIG-*` and `HGL-LIB-*`
> identifiers that the [implementation catalogue](https://github.com/hhenson/hgraph/blob/main/language/docs/design/migration-catalogue.md),
> source `TODO(HGL-LIB-...)` comments and ADR 0008 cite.

## Excerpt 2

> Status vocabulary: **implemented** means the stated slice is on `main`;
> **partial** names working substrate and a remaining boundary; **open** needs a
> contract before implementation can start. A slice being implemented never
> implies that every operator family using it has migrated.

## Excerpt 3

> | Requirement | Status | Catalogue blocker | Accepted record | Still open |
> | --- | --- | --- | --- | --- |
> | MIG-001 module parts | implemented | — | [ADR 0006](https://github.com/hhenson/hgraph_spec/blob/766033278bef6e9403cc99c0d8f318ba46a03919/language/docs/design/decisions/0006-multi-file-module-parts.md) | Automatic discovery and package manifests are tooling, not language. |
> | MIG-002 parameter packs | implemented | B6 | [ADR 0007](https://github.com/hhenson/hgraph_spec/blob/766033278bef6e9403cc99c0d8f318ba46a03919/language/docs/design/decisions/0007-parameter-packs.md); stack #889–#897 merged 2026-09-11/12 | A runtime function accepts one aggregate pack input. |
> | MIG-003 algebraic properties | implemented, scoped | — | [Operators](https://github.com/hhenson/hgraph_spec/blob/766033278bef6e9403cc99c0d8f318ba46a03919/language/docs/design/operators.md) | Claims are not optimizer permissions; inverse/group/field vocabulary deferred. |
> | MIG-004 scalar/native boundary | partial | B1, B3 | [Native interface](https://github.com/hhenson/hgraph_spec/blob/766033278bef6e9403cc99c0d8f318ba46a03919/language/docs/design/native-interface.md), [ADR 0009](https://github.com/hhenson/hgraph_spec/blob/766033278bef6e9403cc99c0d8f318ba46a03919/language/docs/design/decisions/0009-native-errors-and-the-node-error-model.md), [native surface](https://github.com/hhenson/hgraph_spec/blob/766033278bef6e9403cc99c0d8f318ba46a03919/language/docs/design/native-surface-proposal.md) | Owned non-scalar native results; imported atomic types; typed view shapes. |
> | MIG-005 recordable state | partial | B2, B4 | [ADR 0008](https://github.com/hhenson/hgraph_spec/blob/766033278bef6e9403cc99c0d8f318ba46a03919/language/docs/design/decisions/0008-temporal-contracts-and-target-mappings.md) settles cache vs state | Generic state without a default; sparse state; queues and windows; non-scalar caches; wall-clock schedule recovery; owned native state construction. Scalar caches, HGL mixed recordable-state/cache lowering, native pending alarms, and finite schedule progress in simulation are implemented. |
> | MIG-006 collection mutation | implemented, node scope | B4 | [Language model](https://github.com/hhenson/hgraph_spec/blob/766033278bef6e9403cc99c0d8f318ba46a03919/language/docs/design/language-model.md#function-abstraction), typed C++ wrappers (#881–#885) | Graph-form mutation; live structural-child writes. |
> | MIG-007 delta forwarding | open | B4 | — | Type-preserving delta value versus a dedicated forwarding effect. |
> | MIG-008 output resolution | partial | B3 | Constraint language in [functions](https://github.com/hhenson/hgraph_spec/blob/766033278bef6e9403cc99c0d8f318ba46a03919/language/docs/user-guide/functions.md#requirements-and-type-constraints) | Dependent output schemas and imported resolver metadata. |
> | MIG-009 operator identity | partial | — (LIB-001) | Symbol mapping in [Operators](https://github.com/hhenson/hgraph_spec/blob/766033278bef6e9403cc99c0d8f318ba46a03919/language/docs/design/operators.md#fixed-symbol-to-name-mapping); imported-operator checkpoints 1–3 in the [roadmap](https://github.com/hhenson/hgraph/blob/main/language/docs/design/roadmap.md#imported-operator-migration-checkpoints) | Supported descriptor-backed compiled bodies retain imported identities and keyword-safe native aliases. Remaining: unsupported contract shapes, complete provider closure and production replacement. |
> | MIG-010 implementation arity | partial | B6 | Pack cardinality (#891–#892), ranking in ADR 0007 | Fixed candidates refining a pack contract; implementation-specific scalar parameters. |
> | MIG-011 higher-order forms | partial | B6 | [Switch](https://github.com/hhenson/hgraph_spec/blob/766033278bef6e9403cc99c0d8f318ba46a03919/language/docs/design/switch.md), [Iteration](https://github.com/hhenson/hgraph_spec/blob/766033278bef6e9403cc99c0d8f318ba46a03919/language/docs/design/iteration.md), temporal `if` lowering | Explicit `switch` implementation; general map/reduce/mesh callable contracts. |
> | MIG-012 effects and capabilities | partial | B1, B2, B5 | Descriptor phase/effect/ownership metadata ([native interface](https://github.com/hhenson/hgraph_spec/blob/766033278bef6e9403cc99c0d8f318ba46a03919/language/docs/design/native-interface.md#descriptor-is-the-contract)); throwing evaluation calls ([ADR 0009](https://github.com/hhenson/hgraph_spec/blob/766033278bef6e9403cc99c0d8f318ba46a03919/language/docs/design/decisions/0009-native-errors-and-the-node-error-model.md)); clock and scheduler ([ADR 0010](https://github.com/hhenson/hgraph_spec/blob/766033278bef6e9403cc99c0d8f318ba46a03919/language/docs/design/decisions/0010-lifecycle-capabilities.md)) | Resources, additional approved effects, a closed vocabulary shared with descriptors. |
> | MIG-013 library metadata | partial | — | [Source documentation](https://github.com/hhenson/hgraph_spec/blob/766033278bef6e9403cc99c0d8f318ba46a03919/language/docs/design/documentation.md): Google-style sections, reST content and compiler preservation | Defaults, stability and compatibility metadata on HGL declarations. |
> | MIG-014 empty input policies | partial | B2 (LIB-002) | [ADR 0010](https://github.com/hhenson/hgraph_spec/blob/766033278bef6e9403cc99c0d8f318ba46a03919/language/docs/design/decisions/0010-lifecycle-capabilities.md) admits scheduled handlers with an empty activation set | A source form for an explicitly empty validity set. |
> | MIG-015 generic publication | partial | B3 | `instantiate` with retained `_` slots; typed native views read live metadata | Who materializes open downstream types and how a body reads a resolver-selected generic. |

## Excerpt 4

> | Library blocker | Maps to | What it blocks |
> | --- | --- | --- |
> | LIB-001 parallel identity | MIG-009 | Every compiled `hgraph.std.*` / `hgraph.operators.*` body registers as a parallel identity, never as the production overload. |
> | LIB-002 startup and never-valid inputs | MIG-014, B2 | Startup scheduling is available; observing bound-but-invalid inputs still needs an explicitly empty validity set. |
> | LIB-003 retained rolling extents | MIG-015, B3 | A retained rolling size lowers to an any-window pattern and cannot materialize the concrete input schema. |
> | LIB-004 bundle metadata | MIG-015, B3 | TSB size/emptiness is schema metadata and needs a graph-level metadata operation rather than a live-view projection. |

## Excerpt 5

> `pass_through` for the eight scalar domains is compiled. The general operator
> requires the complete input delta, including structural and collection
> removals, applied to an output of the same temporal schema. `delta(value)` has
> no result type today. The choice is a first-class, type-preserving delta value
> or a dedicated forwarding effect; either must work through the public runtime
> contract and in both backends.

## Excerpt 6

> Whatever expresses dependent outputs for `convert`, `combine`, `collect`,
> `split`, frame joins and higher-order calls must lower to the shared hgraph
> resolver. A second ranking or inference algorithm in the compiler is not
> acceptable, and an unconstrained generic `O` on a contract is not a resolver.

## Excerpt 7

> Two native identities collide with HGL source spellings: `const` is an HGL
> keyword, and `default` is the fallback label of the planned `switch` form. Their
> contracts are fixed by the operator markers in
> `include/hgraph/lib/std/operators/conversion.h` and cannot be spelled as
> declarations today:

## Excerpt 8

> ```text
> native identity "const"   (marker const_):
>     Scalar<"value", ScalarVar<"T">>, TypeArg<"tp", TsVar<"S">, AutoResolve>,
>     Scalar<"delay", TimeDelta>, Out<TsVar<"S">>
> native identity "default" (marker default_):
>     In<"ts", TsVar<"S">>, In<"default_value", TsVar<"S">>, Out<TsVar<"S">>
> ```

## Excerpt 9

> The parameter names and type relationships are part of the contract. `const`
> takes an independent scalar `T`; its output shape `S` is auto-resolved from the
> value or selected explicitly (`const[TS[float]](https://github.com/hhenson/hgraph_spec/blob/766033278bef6e9403cc99c0d8f318ba46a03919/language/docs/design/1)`), and `delay` is an optional
> keyword after `tp`. `default` names its first input `ts`, so named calls such as
> `default(ts=price, default_value=zero)` are established call shapes. The library
> needs a reviewable mapping from a legal source declaration to the stable native
> identity that preserves these names, defaults and type relationships. Renaming a
> source symbol must never create a new overload family. Internal `__`-prefixed
> identities (`__lag_proxy`, `__print_sink`, `__log_sink`, `__assert_fmt`,
> `__apply_value_callable`, `__call_value_callable`, `__json_object`,
> `__json_array`) are compiler-selected kernels; they are never public HGL names,
> whatever their catalogue disposition.

## Excerpt 10

> Decision (project owner, 2026-09-29, on
> [ADR 0015](https://github.com/hhenson/hgraph_spec/blob/766033278bef6e9403cc99c0d8f318ba46a03919/language/docs/design/decisions/0015-pull-sources.md)): the library spelling of the
> constant source is `const`, never `const_`. A function is not the `const`
> modifier, and replacing a native identity keeps its name. The mapping this
> needs: the parser admits `const` as an operator, implementation and
> instantiation name (it already parses it; the projection rejects it), and a
> call `const(...)` whose single argument is not a function name resolves to
> the operator in scope rather than to the `const(function)` selector of
> [ADR 0008](https://github.com/hhenson/hgraph_spec/blob/766033278bef6e9403cc99c0d8f318ba46a03919/language/docs/design/decisions/0008-temporal-contracts-and-target-mappings.md). The
> `const_` of the [bootstrap](https://github.com/hhenson/hgraph_spec/blob/766033278bef6e9403cc99c0d8f318ba46a03919/language/docs/design/const-debug-bootstrap.md) is a private example
> function, not the library name.

## Excerpt 11

> Source-native evaluation functions remain non-blocking. ADR 0009 admits
> `throws` and the descriptor's `translated` policy under hgraph's node error
> model; functions without `throws` remain `noexcept`. Owned scalar results are
> admitted, while owned non-scalar results remain B1. ADR 0010 implements the
> clock and scheduler capabilities, scheduled activation, and evaluation-time
> input activity. Non-recordable storage, input access in lifecycle hooks, and
> external resource ownership remain B2. A C++ body is not permission to publish
> a contract the descriptor cannot enforce: the vocabulary must be closed and
> shared between HGL source, descriptors and the backend-neutral runtime
> specification.

## Excerpt 12

> The nine proposed family files in PR #801 were contract inventories; the
> catalogue now derives that inventory from the C++ headers. These observations
> in them are not derivable from the headers and are kept:

## Excerpt 13

> - `cmp_` needs a nominal result enum; range and civil policy parameters
>   (`month_end_policy`, `ambiguous`, `nonexistent`) should become nominal
>   enums once imported enum mapping exists. `i64` is a placeholder.
> - `join` is one native identity spanning the string and frame families. It is
>   a useful test that a nominal operator family can span candidates with
>   different call shapes without source-order dispatch.
> - Set `union` in HGL needs membership in the *other* input to handle removal,
>   plus a rule for simultaneous deltas. The `contains` intrinsic on set inputs
>   now exists, so this candidate deserves a fresh review under B4.
> - A binary `merge` written as ordered `when` blocks makes the left input win
>   when both tick; that spelling is correct but the native family also carries
>   reference reselection, which is why the catalogue keeps it under B4.
> - Bodies proposed for `sample`, `filter_`, `dedup`, `drop`, `null_sink`,
>   `pass_through`, `min_` and `max_` have graduated into compiled source.
>   `take` now has a scalar slice using evaluation-time passivation (ADR 0010);
>   passivating a restored exhausted counter during `start` remains B2.
>   `debug_print` remains blocked: logger formatting of an arbitrary value is B5.

## Excerpt 14

> The catalogue's *implemented* means authored and parity-tested as a parallel
> identity. Production replacement additionally requires the criteria in the
> roadmap's [core migration programme](https://github.com/hhenson/hgraph/blob/main/language/docs/design/roadmap.md#core-standard-library-migration-programme),
> plus two conditions PR #801 recorded that the roadmap does not:

## Excerpt 15

> - the HGL source contains no provisional syntax or design annotation; and
> - the generated module registers through the same provider transaction and
>   operator registry as the implementation it replaces.

## Excerpt 16

> The historical operator inventory, the recovery manifest, and the
> `.hgl.proposed` contract lists in PR #801 are superseded by the checked
> catalogue and are intentionally not copied. PR #801 is closed; this page is
> the surviving record.
