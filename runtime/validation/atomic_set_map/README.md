# Complete ordinary set/map publications

The [atomic set/map extension](https://github.com/hhenson/hgraph_spec/blob/75b15822b691c13765241647fa831e8d125b882e/language/docs/design/atomic-set-map-publications.md)
admits finite ordinary set/map payloads with complete replacement and existing
owning capture rules. [reasoned.json](reasoned.json) was written before graph
measurement; ordinary source construction is a specification decision, not an
API inferred from these Python authoring tests.

[observed.json](observed.json) records three identical fresh runs per engine,
48 eval calls. Historical Python 0.5.41 and native 0.0.0 both run real
`TS[set[int]]`, `TS[dict[str,int]]` and `TS[dict[str,list[int]]]` computes that
return `delta_value` into their own output, captured by the actual eval
recorder. These are complete TS payloads, not TSS/TSD sparse patches.
Package/source/native-library hashes identify the measured runtimes.

Both engines preserve full/empty/silent/empty/replacement traces. Repeated empty
containers publish, and a complete map replaces omitted keys. Native map/list
recordings survive source changes, another eval and mutation of one recorded
nested list without altering other captures. Historical Python aliases source
containers and nested values: each mutation changes earlier recordings,
sibling captures and the second run. This divergence remains explicit.

Native sets are exported as immutable frozensets. They retain original
snapshots across mutation of the mutable input set and another eval. Attempting
`add` on a native recorded set raises `AttributeError`; the audit preserves
that failure and does not claim writable capture support. The observer retains
all pre-mutation measurements even when this bounded mutation probe fails.
HGL's ordinary writable-owner behavior still requires its specified ownership
and mutation contracts; the authoring representation does not redefine them.

This does not prove HGL constructor parsing, duplicate failure phases, arbitrary
scalar key families, unknown native enums, NaN, optional/recursive payloads,
invalidations or references.

```sh
python3 runtime/validation/atomic_set_map/observe.py \
  --python /path/to/historical-python/bin/python \
  --cpp /path/to/native/bin/python --output /tmp/atomic-set-map-fresh.json
python3 runtime/validation/atomic_set_map/check.py
python3 -m unittest discover -s runtime/validation/atomic_set_map
```

The checker and six tests preserve complete empty ticks, replacement, both
engines' exact ownership observations and the native immutable-set failure.
