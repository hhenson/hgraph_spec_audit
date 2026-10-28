# Operator review clarifications, 19 October 2026

Review found two inconsistencies in the specification: the temporal-function
summary still called `abs` a standard-library function, and the `std` extension
wording could imply an override of an equally ranked core baseline. The text
now identifies `core.abs` and retains ordinary candidate selection: provider
membership adds no priority; equal-ranked applicable candidates are ambiguous.

The audit spelling comment compares an archived, removed `core::add_`
diagnostic with the corrected `core.add_` identity. The earlier review archive
pins the removed text to its own source revision. The placement manifest now
pins the revision against which its `current_replacement` fields were checked.
Neither archived source text nor its source hashes have been rewritten.

The [provenance manifest](operator-review-clarifications-2026-10-19.provenance.json)
preserves the superseded specification passages below. Expected traces and
recorded runtime results are unchanged.

## language/docs/design/operators.md

[Source, line 43](https://github.com/hhenson/hgraph_spec/blob/fb36dfe67ac39425120e2393435c44a8cfb05f8a/language/docs/design/operators.md#L43).

> `core` identity and applicable contract. They may extend supported domains or
> provide optimizations without redeclaring the operator in `std`.
> Candidate selection follows the ordinary resolution rules.

## language/docs/developer-guide/syntax-and-semantics.md

[Source, line 868](https://github.com/hhenson/hgraph_spec/blob/fb36dfe67ac39425120e2393435c44a8cfb05f8a/language/docs/developer-guide/syntax-and-semantics.md#L868).

> Field accessors (`year`, `month`, `day`, `weekday`, `hour`, `minute`,
> `second`, `microsecond`, `days`, `seconds`, `total_seconds`), `abs`, the
