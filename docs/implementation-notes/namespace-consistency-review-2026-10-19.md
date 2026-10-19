# Namespace consistency review, 19 October 2026

The review checked the specification's core/std policy, module discovery,
public imports, native bindings, examples and documentation links. The user
guide now states that a candidate supplied by `std` retains its `core` operator
identity and import path. Prelude and diagnostic wording follow that model;
required descriptor compatibility refers to the target runtime.

The project owner clarified that core helpers belong in `core.native` and
additional standard-library helpers in `std.native`. Analytics placement is
deferred, so the existing example name is explicitly provisional. The core
helper guide links to shared contracts rather than an implementation inventory.

Expected traces, executable example files and measured results are unchanged.
Prior wording is preserved below, with source hashes and locations in the
[provenance manifest](namespace-consistency-review-2026-10-19.provenance.json).

## README.md

[Source, line 23](https://github.com/hhenson/hgraph_spec/blob/d1dadc731f4b2f6799f890ba4d3bb0e7aea3a814/README.md#L23).

> - [Library contracts](https://github.com/hhenson/hgraph_spec/blob/d1dadc731f4b2f6799f890ba4d3bb0e7aea3a814/library/README.md): what standard library operators publish

## language/docs/design/decisions/0008-temporal-contracts-and-target-mappings.md

[Source, line 136](https://github.com/hhenson/hgraph_spec/blob/d1dadc731f4b2f6799f890ba4d3bb0e7aea3a814/language/docs/design/decisions/0008-temporal-contracts-and-target-mappings.md#L136).

> an overload on each tick. The existing hgraph resolver remains the owner of
> temporal candidate matching/ranking. Extending the model to value candidates

## language/docs/design/modules.md

[Source, line 7](https://github.com/hhenson/hgraph_spec/blob/d1dadc731f4b2f6799f890ba4d3bb0e7aea3a814/language/docs/design/modules.md#L7).

> Hgraph and its native extensions provide the capabilities from which language

[Source, line 25](https://github.com/hhenson/hgraph_spec/blob/d1dadc731f4b2f6799f890ba4d3bb0e7aea3a814/language/docs/design/modules.md#L25).

> - compatible hgraph SDK and descriptor-format versions;

## language/docs/design/native-interface.md

[Source, line 247](https://github.com/hhenson/hgraph_spec/blob/d1dadc731f4b2f6799f890ba4d3bb0e7aea3a814/language/docs/design/native-interface.md#L247).

> its runtime implementation:

[Source, line 250](https://github.com/hhenson/hgraph_spec/blob/d1dadc731f4b2f6799f890ba4d3bb0e7aea3a814/language/docs/design/native-interface.md#L250).

> use hgraph.native as native

[Source, line 269](https://github.com/hhenson/hgraph_spec/blob/d1dadc731f4b2f6799f890ba4d3bb0e7aea3a814/language/docs/design/native-interface.md#L269).

> use hgraph.native as native

## language/docs/design/native-interfaces.md

[Source, line 30](https://github.com/hhenson/hgraph_spec/blob/d1dadc731f4b2f6799f890ba4d3bb0e7aea3a814/language/docs/design/native-interfaces.md#L30).

> module hgraph.native

## language/docs/design/native-surface-proposal.md

[Source, line 108](https://github.com/hhenson/hgraph_spec/blob/d1dadc731f4b2f6799f890ba4d3bb0e7aea3a814/language/docs/design/native-surface-proposal.md#L108).

> use hgraph.native as native

## language/docs/design/node-authoring.md

[Source, line 8](https://github.com/hhenson/hgraph_spec/blob/d1dadc731f4b2f6799f890ba4d3bb0e7aea3a814/language/docs/design/node-authoring.md#L8).

> A temporal operator can call a scalar native helper:

## language/docs/developer-guide/syntax-and-semantics.md

[Source, line 2589](https://github.com/hhenson/hgraph_spec/blob/d1dadc731f4b2f6799f890ba4d3bb0e7aea3a814/language/docs/developer-guide/syntax-and-semantics.md#L2589).

> module: 'export impl fn add_' is invalid; the implementation is public through core::add_

## language/docs/user-guide/README.md

[Source, line 6](https://github.com/hhenson/hgraph_spec/blob/d1dadc731f4b2f6799f890ba4d3bb0e7aea3a814/language/docs/user-guide/README.md#L6).

> how source calls reach hgraph.

## language/docs/user-guide/language-tour.md

[Source, line 35](https://github.com/hhenson/hgraph_spec/blob/d1dadc731f4b2f6799f890ba4d3bb0e7aea3a814/language/docs/user-guide/language-tour.md#L35).

> `window` is marked `const`, so it is an ordinary `i64` available while hgraph
> constructs the function. It cannot change from tick to tick.

## language/docs/user-guide/modules-and-tools.md

[Source, line 3](https://github.com/hhenson/hgraph_spec/blob/d1dadc731f4b2f6799f890ba4d3bb0e7aea3a814/language/docs/user-guide/modules-and-tools.md#L3).

> Modules make hgraph and extension capabilities available without exposing a

[Source, line 78](https://github.com/hhenson/hgraph_spec/blob/d1dadc731f4b2f6799f890ba4d3bb0e7aea3a814/language/docs/user-guide/modules-and-tools.md#L78).

> expression operator bindings come from the implicit hgraph prelude. Exported

[Source, line 98](https://github.com/hhenson/hgraph_spec/blob/d1dadc731f4b2f6799f890ba4d3bb0e7aea3a814/language/docs/user-guide/modules-and-tools.md#L98).

> The `hgraph.native` module provides `len` and `is_empty` for `str`,

[Source, line 101](https://github.com/hhenson/hgraph_spec/blob/d1dadc731f4b2f6799f890ba4d3bb0e7aea3a814/language/docs/user-guide/modules-and-tools.md#L101).

> Additional string and window queries live in parts of the same module; see
> the [native inventory](https://github.com/hhenson/hgraph/blob/main/language/stdlib/hgl/hgraph/README.md). Value operations keep

[Source, line 107](https://github.com/hhenson/hgraph_spec/blob/d1dadc731f4b2f6799f890ba4d3bb0e7aea3a814/language/docs/user-guide/modules-and-tools.md#L107).

> use hgraph.native as native

[Source, line 116](https://github.com/hhenson/hgraph_spec/blob/d1dadc731f4b2f6799f890ba4d3bb0e7aea3a814/language/docs/user-guide/modules-and-tools.md#L116).

> The native library must be included in the package that runs the program.
> For build configuration, see the
> [package-authoring guide](https://github.com/hhenson/hgraph/blob/main/language/docs/developer-guide/native-modules-and-packages.md#building-a-package).
> The [module inventory](https://github.com/hhenson/hgraph/blob/main/language/stdlib/hgl/hgraph/README.md) lists available
> functions and current type restrictions.
