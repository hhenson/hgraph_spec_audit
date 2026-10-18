# Runtime case notes relocated on 18 October 2026

Historical execution claims, backend differences and fixture notes removed from
four runtime case pages. These excerpts were not revalidated and do not assert
current support or define the standard. Expected observations and proposal
boundaries remain in the specification.

Source revision: `61eb6b8be0a9b989f00b9bace8b12ac74d403506`. The [provenance manifest](case-cleanup-2026-10-18.provenance.json)
records source hashes, excerpt locations and original text. Relative links in
excerpts resolve to that specification revision.

## runtime/cases_nested.md

### Excerpt 1

[Source, line 3](https://github.com/hhenson/hgraph_spec/blob/61eb6b8be0a9b989f00b9bace8b12ac74d403506/runtime/cases_nested.md#L3).

> Status: validated on Python and C++ hgraph; see [results](https://github.com/hhenson/hgraph_spec_audit/blob/main/runtime/validation.md).

### Excerpt 2

[Source, line 41](https://github.com/hhenson/hgraph_spec/blob/61eb6b8be0a9b989f00b9bace8b12ac74d403506/runtime/cases_nested.md#L41).

> The fixture uses native/Python `STATE` to observe instance lifetime. This does
> not validate recording, recovery or HGL's state/cache lowering.

### Excerpt 3

[Source, line 61](https://github.com/hhenson/hgraph_spec/blob/61eb6b8be0a9b989f00b9bace8b12ac74d403506/runtime/cases_nested.md#L61).

> exclusive run end. These cases validate deadline propagation and cancellation;
> they do not establish memory bounds or absence of physical allocations.

## runtime/cases_references.md

### Excerpt 1

[Source, line 3](https://github.com/hhenson/hgraph_spec/blob/61eb6b8be0a9b989f00b9bace8b12ac74d403506/runtime/cases_references.md#L3).

> Status: validated expectations with recorded variations; see [results](https://github.com/hhenson/hgraph_spec_audit/blob/main/runtime/validation.md).

### Excerpt 2

[Source, line 53](https://github.com/hhenson/hgraph_spec/blob/61eb6b8be0a9b989f00b9bace8b12ac74d403506/runtime/cases_references.md#L53).

> These expectations are accepted observation by observation: Python supports
> the complete removal delta; C++ supports invalidity on withdrawal. Neither
> implementation's complete withdrawal row currently conforms.

### Excerpt 3

[Source, line 67](https://github.com/hhenson/hgraph_spec/blob/61eb6b8be0a9b989f00b9bace8b12ac74d403506/runtime/cases_references.md#L67).

> The expiry rule was confirmed by the user on 2026-09-21. Python raises when
> the expired reference is used; C++ retains 7 at 3 and expires it at 4.
> Both are variations, not alternative permitted results.

### Excerpt 4

[Source, line 71](https://github.com/hhenson/hgraph_spec/blob/61eb6b8be0a9b989f00b9bace8b12ac74d403506/runtime/cases_references.md#L71).

> The saved-reference case does not prove allocator slot reuse or generation
> wrap handling. Those need storage tests when the Rust realization exists.

## runtime/cases_fixed.md

### Excerpt 1

[Source, line 1](https://github.com/hhenson/hgraph_spec/blob/61eb6b8be0a9b989f00b9bace8b12ac74d403506/runtime/cases_fixed.md#L1).

> Fixed collections: validation cases
> ==================================
>
> Status: 44 cases compared with Python and C++; user rulings recorded.
> See the [comparison report](https://github.com/hhenson/hgraph_spec_audit/blob/main/runtime/validation/fixed/README.md).
> The prototype slice covers fixed-size TSL and TSB. Growing TSL is separate.

## runtime/cases_collections.md

### Excerpt 1

[Source, line 3](https://github.com/hhenson/hgraph_spec/blob/61eb6b8be0a9b989f00b9bace8b12ac74d403506/runtime/cases_collections.md#L3).

> Status: mixed. QUOTE-HISTORY, MEMBERSHIP-INDEPENDENT and same-cycle restoration
> have [executed evidence and variations](https://github.com/hhenson/hgraph_spec_audit/blob/main/runtime/validation.md). Other cases remain
> proposed unless separately identified.

### Excerpt 2

[Source, line 68](https://github.com/hhenson/hgraph_spec/blob/61eb6b8be0a9b989f00b9bace8b12ac74d403506/runtime/cases_collections.md#L68).

> [Evidence](https://github.com/hhenson/hgraph_spec_audit/blob/main/runtime/evidence.md) names the C++ surfaces. This case extends beyond
> QUOTE-HISTORY.

### Excerpt 3

[Source, line 77](https://github.com/hhenson/hgraph_spec/blob/61eb6b8be0a9b989f00b9bace8b12ac74d403506/runtime/cases_collections.md#L77).

> this is a new child. See the `restore` input and observations in the evidence.
