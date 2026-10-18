# Library contract notes relocated on 17 October 2026

Historical implementation comparisons and their surrounding wording, removed
from [library/operator_contracts.md](https://github.com/hhenson/hgraph_spec/blob/990261ff840014f7eb1ef221a6f8d843152908da/library/operator_contracts.md). These excerpts were not
revalidated and do not assert current support or define the standard.

Source revision: `990261ff840014f7eb1ef221a6f8d843152908da`. The [provenance manifest](operator-contracts-cleanup-2026-10-17.provenance.json)
records the original file hash, excerpt locations and original excerpt text.
Relative links below resolve to the recorded specification revision. Existing
operator validity exceptions were not settled by this cleanup.

## Excerpt 1

[Source, line 6](https://github.com/hhenson/hgraph_spec/blob/990261ff840014f7eb1ef221a6f8d843152908da/library/operator_contracts.md#L6).

> Derived while triaging the open
> parity issues; covers the operator families those issues exercised. The
> rest of the library remains open

## Excerpt 2

[Source, line 10](https://github.com/hhenson/hgraph_spec/blob/990261ff840014f7eb1ef221a6f8d843152908da/library/operator_contracts.md#L10).

> [Parity validation](https://github.com/hhenson/hgraph_spec_audit/blob/main/runtime/validation/parity/README.md) records each derivation
> against the Python 0.5.41 and C++ observations.

## Excerpt 3

[Source, line 37](https://github.com/hhenson/hgraph_spec/blob/990261ff840014f7eb1ef221a6f8d843152908da/library/operator_contracts.md#L37).

> names its arguments. `mean` over a dictionary names its whole input: Python
> 0.5.41 defines it as `default(div_(sum_, len_), NaN)`, so a dictionary that
> has never ticked has a NaN mean. Its `sum_`, `min_` and `max_` name nothing
> and publish nothing.

## Excerpt 4

[Source, line 44](https://github.com/hhenson/hgraph_spec/blob/990261ff840014f7eb1ef221a6f8d843152908da/library/operator_contracts.md#L44).

> the valid elements only (the accepted valid-subset reduce, issue #95).

## Excerpt 5

[Source, line 53](https://github.com/hhenson/hgraph_spec/blob/990261ff840014f7eb1ef221a6f8d843152908da/library/operator_contracts.md#L53).

> (ruling 2026-07-17, enforced 2026-09-15; `roadmap.rst`).

## Excerpt 6

[Source, line 72](https://github.com/hhenson/hgraph_spec/blob/990261ff840014f7eb1ef221a6f8d843152908da/library/operator_contracts.md#L72).

> tick. Both runtimes already do this for sets. Python 0.5.41 does it for
> `difference` and `intersection` of dictionaries, but not for their `^` and
> `|`, which it builds on `map_`.

## Excerpt 7

[Source, line 82](https://github.com/hhenson/hgraph_spec/blob/990261ff840014f7eb1ef221a6f8d843152908da/library/operator_contracts.md#L82).

> number of operands; `difference` takes exactly two. Python 0.5.41 cannot
> fold intersection or symmetric difference: it has no zero for the fold. It
> rejects three TSS operands at wiring, and three TSD operands to symmetric
> difference never publish. The fold is an accepted superset
> (`parity_matrix.rst`). Over dictionaries a fold whose intermediate result is
> empty also depends on point to settle 1.

## Excerpt 8

[Source, line 140](https://github.com/hhenson/hgraph_spec/blob/990261ff840014f7eb1ef221a6f8d843152908da/library/operator_contracts.md#L140).

> `str_` gives Python's `str` of the value. A string at the top level is its
> own text. Inside a container a string is written as Python's `repr` writes
> it: quoted as Python chooses, with the backslash, quote and every character
> that Python's `str.isprintable` rejects escaped. `\t`, `\n` and `\r` are
> named; other characters below U+0100 are `\xNN`; others below U+10000 are
> `\uNNNN`, and the rest `\UNNNNNNNN`. A map or a set is unordered, so its
> text lists its members in no specified order: Python writes insertion order,
> the C++ runtime storage order (ruling 2026-09-24). Printability follows the Unicode version
> the implementation records; a character whose category differs
> between Unicode versions may render differently under another Python.

## Excerpt 9

[Source, line 156](https://github.com/hhenson/hgraph_spec/blob/990261ff840014f7eb1ef221a6f8d843152908da/library/operator_contracts.md#L156).

> results. Python 0.5.41 raises `ValueError` from `math.log`. Accepted
> deviation (`parity_matrix.rst`).

## Excerpt 10

[Source, line 175](https://github.com/hhenson/hgraph_spec/blob/990261ff840014f7eb1ef221a6f8d843152908da/library/operator_contracts.md#L175).

> - Removing a partition costs the keys that partition owns, never the size of
>   the output (guardrail iv, `CLAUDE.md`).

## Excerpt 11

[Source, line 178](https://github.com/hhenson/hgraph_spec/blob/990261ff840014f7eb1ef221a6f8d843152908da/library/operator_contracts.md#L178).

> Python 0.5.41 keeps a removed partition's keys. Each holds a reference that
> designates nothing from the next engine cycle (TS-23), so a consumer bound
> through it unbinds without a tick (TS-15) while the key stays in the
> dictionary; a nested dictionary child reports its elements removed instead of
> its key. Accepted deviation (`parity_matrix.rst`).

## Excerpt 12

[Source, line 239](https://github.com/hhenson/hgraph_spec/blob/990261ff840014f7eb1ef221a6f8d843152908da/library/operator_contracts.md#L239).

> - **OP-9** `str_` of a container renders each string as Python's `repr`,
>   escaping every character `str.isprintable` rejects. The members of a map or
>   a set appear in no specified order.

## Excerpt 13

[Source, line 275](https://github.com/hhenson/hgraph_spec/blob/990261ff840014f7eb1ef221a6f8d843152908da/library/operator_contracts.md#L275).

>    although its value is well defined (#978). Both runtimes already
>    publish the empty first result for sets.

## Excerpt 14

[Source, line 279](https://github.com/hhenson/hgraph_spec/blob/990261ff840014f7eb1ef221a6f8d843152908da/library/operator_contracts.md#L279).

>    text is unspecified (Scalar types, Text; OP-9). Python writes insertion
>    order and the C++ runtime storage order; both conform. A set has no order
>    either (VAL-8) and is treated the same way.

## Excerpt 15

[Source, line 282](https://github.com/hhenson/hgraph_spec/blob/990261ff840014f7eb1ef221a6f8d843152908da/library/operator_contracts.md#L282).

> 3. **The emptiness of an invalid set.** `is_empty` of a never-ticked set is
>    `True` in both runtimes. OP-1 would publish nothing. Both runtimes agree,
>    no parity issue depends on it, and nothing here changes it.
