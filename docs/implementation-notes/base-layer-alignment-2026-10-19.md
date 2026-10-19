# Base-layer proposal alignment, 19 October 2026

The base-layer proposal in [spec PR #126](https://github.com/hhenson/hgraph_spec/pull/126)
predated the agreed `core`/`std` model. It now follows those module names,
uses `core.native` and `std.native` for their helper roles, and names its test-only
modules `conformance` and `conformance.rejections`, as clarified by the owner.
Core helper providers belong to core's implementation dependency closure; they
do not introduce a standard-library dependency into conformance.

The logger review finding is valid: capability receiver dispatch must include
`logger` and precede ordinary name shadowing. Related proposal text now retains
ordinary candidate ambiguity, keeps `abs` in core, and tests projections through
named calls only where a public declaration exists. Detailed `abs` roles and
domains remain an open proposal question. The other unresolved semantic choices
remain proposed.

The specification retains agreed/proposed labels. Rule origins, including the
original owner/date annotations, are preserved here rather than asserted as a
second authority in the specification. The [provenance manifest](base-layer-alignment-2026-10-19.provenance.json)
records removed passages and source locations from revision `ddb8a31e5a83d9950144f547fc9bbb9c997731d2`
of the [original proposal](https://github.com/hhenson/hgraph_spec/blob/ddb8a31e5a83d9950144f547fc9bbb9c997731d2/language/docs/design/base-layer.md).

All BASE-1–BASE-19 and MAP-1–MAP-7 identifiers are retained. The proposed operator
signature block and existing expected traces are unchanged. No executable core
or conformance source files were added by this alignment.
