# Operator namespace migration history

`hgraph.operators` was an implementation migration arrangement, not an
agreed public namespace. The specification removes that arrangement and records
the core operator policy described below. Expected ticks are unchanged.

The existing [conformance adapter](../../compiler/stdlib/nodes.hgl) is retained
here byte for byte for the pinned implementation. Its imports do not define
the standard library namespace. Recorded measurements are unchanged.

Source revision: `00772fa17a63c0befcd6d002611b9405fec71105`. The [provenance manifest](operator-namespace-2026-10-19.provenance.json)
preserves source hashes, removed text and the former adapter metadata.

## Final project owner decision, 19 October 2026

`core` owns both operator declarations and their required baseline
implementations. Every engine must provide that baseline for every core
operator. The core remains small: syntax-required operators and essential named
operations, such as `abs`, whose inclusion justifies the universal obligation.
`std` owns the broader library and may add candidates for operators declared in
`core`, retaining their original operator identities.

Native helpers used by core implementations belong in `core.native`;
additional helpers needed by the standard library belong in `std.native`.
Analytics placement is deferred; its example module name remains provisional.

This explicitly replaces the earlier `hgraph` / `hgraph.kernel` split and the
`hgraph.std` spelling with `core` and `std`. The recorded adapter remains at its
measured namespace arrangement; it is historical evidence, not a new source
example for the current module names.
The [decision provenance](core-std-decision-2026-10-19.provenance.json) records
the superseded policy and source revision.

## Earlier decisions and corrections (superseded)

Core operators are declared directly in `hgraph`; `hgraph.kernel` contains their
implementations and no operator declarations. Every engine must provide a
baseline implementation of every core operator. The core includes operators
required by language syntax and essential named operations, such as `abs`,
whose inclusion justifies that universal obligation. Keep the core small;
other operators belong in `hgraph.std`. This decision does not enumerate the complete
inventory or select new implementation machinery.

Documentation examples import core `add_` from `hgraph`. Standard-library
operators retain `hgraph.std`; the owner's use of “std” was shorthand, not a
namespace rename. The initial top-level `std` edits were an interpretation
error and have been corrected. The [placement provenance](core-operator-placement-2026-10-19.provenance.json)
retains those intermediate edits and their corrections. The recorded audit
adapter remains unchanged at its measured namespace arrangement.

## language/docs/design/operators.md

[Source, line 192](https://github.com/hhenson/hgraph_spec/blob/00772fa17a63c0befcd6d002611b9405fec71105/language/docs/design/operators.md#L192).

> Native-call requirements belong to the delegating `impl fn` candidates,
> not the public operator contracts. The `hgraph.operators.*` identities are
> parallel migration contracts, not replacements for system identities.
> The existing `getitem_`/`getattr_` projections are not redeclared as scalar binary
> arithmetic. Broader temporal, collection, and downstream scalar domains remain
> in the native registry until their HGL materializations are covered.

## language/docs/design/node-authoring.md

[Source, line 21](https://github.com/hhenson/hgraph_spec/blob/00772fa17a63c0befcd6d002611b9405fec71105/language/docs/design/node-authoring.md#L21).

> - **NAT-1:** Select by canonical module/declaration identity, full signature and
>   role. `native const fn hgraph.native.bit_and(i64,i64)->i64` is a value helper;
>   `hgraph.operators.bit_and` is a temporal operator. Neither substitutes for
>   the other. Resolve candidates in the checker, retain the selection in IR.

## compiler/stdlib/nodes.hgl

[Source, line 1](https://github.com/hhenson/hgraph_spec/blob/00772fa17a63c0befcd6d002611b9405fec71105/compiler/stdlib/nodes.hgl#L1).

> module conformance.stdlib
>
> use hgraph.operators as operators
> use hgraph.std as std
>
> export fn bit_and_i64(lhs: i64, rhs: i64) -> i64 => operators::bit_and(lhs, rhs)
> export fn sample_i64(signal: i64, ts: i64) -> i64 => std::sample(signal, ts)
> export fn dedup_i64(ts: i64) -> i64 => std::dedup(ts)
