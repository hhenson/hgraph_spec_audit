# Operator namespace migration history

`hgraph.operators` was an implementation migration arrangement, not an
agreed public namespace. It is removed from the specification without
selecting a replacement. Operator behavior and expected ticks are unchanged.

The existing [conformance adapter](../../compiler/stdlib/nodes.hgl) is retained
here byte for byte for the pinned implementation. Its imports do not define
the standard library namespace. Recorded measurements are unchanged.

Source revision: `00772fa17a63c0befcd6d002611b9405fec71105`. The [provenance manifest](operator-namespace-2026-10-19.provenance.json)
preserves source hashes, removed text and the former adapter metadata.

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
