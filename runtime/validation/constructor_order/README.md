# Named constructor argument order

Measured 2026-10-03. A Python-authored `@dataclass` Pair derived from
`CompoundScalar`, with fields declared left then right, evaluates
`Pair(right=mark(2), left=mark(1))` in written argument order. Both independent
packages produce trace `[2, 1]`, with left equal to 1 and right equal to 2.
When the first supplied argument raises, the trace is `[2]`: the later
argument does not execute and construction does not succeed.

`reasoned.json` was written before measurement. `observed.json` records three
identical fresh-process runs for each package, the harness and expectation
hashes, CompoundScalar source hashes, package manifests and loaded native
library hashes. The packages are pure Python hgraph 0.5.41 and a C++ development
wheel reporting 0.0.0, both under Python 3.14. This is not a released-version
parity claim. These observations test Python authoring order on both packages;
they do not test native C++ argument-expression evaluation order.

The proposed HGL rule independently chooses written argument order and named
field association. An argument failure stops later argument evaluation and
does not produce a constructed value; prior argument effects remain. The
observations support that choice for scalar arguments. They do not measure
aggregate capture timing, arbitrary copy failures or transactional rollback.

Separate native source inspection at
[`8e899e600089902f9b755f67d9998292fcc03e84`](https://github.com/hhenson/hgraph/blob/8e899e600089902f9b755f67d9998292fcc03e84/include/hgraph/types/value/value_builder.h#L1075-L1180)
shows BundleBuilder's named/indexed setters copy a supplied value immediately;
build materializes the completed bundle. A caller can sequence setters. This
does not establish an evaluation order for argument expressions at arbitrary
C++ call sites or impose field-declaration order on HGL.

Reproduce with independent interpreters and a new output destination:

```sh
python3 runtime/validation/constructor_order/observe.py \
  --python /path/to/python-hgraph/bin/python \
  --cpp /path/to/cpp-hgraph/bin/python \
  --output /tmp/new-constructor-order.json
python3 runtime/validation/constructor_order/check.py
```

The checker verifies saved evidence only; it does not rerun engines.
