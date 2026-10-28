# Map call order correction, 19 October 2026

The project owner corrected the proposed form to `map(fn(p) => body, c)`:
the callable precedes the collection. MAP-1 and the related anonymous-function
examples now use that order. The illustrative named-function and multi-collection
spellings follow the same order; their support remains open under point 8.
No collection membership, lifetime, delta or capture rule changed.

The [provenance manifest](map-call-order-2026-10-19.provenance.json) retains the
superseded collection-first examples and their pinned source locations.
