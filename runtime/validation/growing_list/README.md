# Growing-list publication deltas

The [growing-list contract](https://github.com/hhenson/hgraph_spec/blob/a7f10e522ba0dd18ecc354a3ab22dcadda8fae6e/language/docs/design/growing-list-publications.md)
uses net tail removals plus sparse child publications under existing TS-12 and
TS-32. [reasoned.json](reasoned.json) was written before measurement.

[observed.json](observed.json) contains three identical fresh processes per
engine, five actual eval attempts each (30 total). The native package uses
`TSL[TS[int], Size[-1]]`; historical Python uses its dynamic `Size` marker
(`FIXED_SIZE=False`). Neither is replaced by a fixed list. Provenance includes
package/source/native-library hashes.

Native passes append/update/shrink, equal repeated child writes, and complete
tail removal followed by regrowth. Its actual authoring delta is an index map
with REMOVE markers for every removed tail position. Generic `delta_value`
forwarding preserves that delta on the compute's own output. Truncation to
zero publishes removals and leaves a valid/all-valid empty root; a later
append starts at zero. No held full list is substituted for a delta.

Historical Python can construct the dynamic schema but its replay raises
`Expected 0 elements, got N` on all three nonempty traces before the compute
runs. Its empty and all-silent traces return raw null, as native does.
This is a native behavioral observation with a historical engine failure,
not two-engine growth parity. No fallback resizes the historical list.

The bounded source profile encodes canonical net deltas: contiguous append
with nonempty child publications, a complete removed tail, and no removed/
modified overlap. It does not claim invalid-child growth, transient same-cycle
resize observation, removed-child lifetime, arbitrary recursive shapes,
invalidation or reference coverage.

```sh
python3 runtime/validation/growing_list/observe.py \
  --python /path/to/historical-python/bin/python \
  --cpp /path/to/native/bin/python --output /tmp/growing-list-fresh.json
python3 runtime/validation/growing_list/check.py
python3 -m unittest discover -s runtime/validation/growing_list
```

Five tests reject missing removals, suppressed empty truncation, invented
Python parity and unrelated errors. The full original exception trace remains
in evidence; the checker recognizes its specific replay failure and phase.
