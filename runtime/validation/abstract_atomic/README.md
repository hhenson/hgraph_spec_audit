# Complete atomic family values

The [atomic family admission](https://github.com/hhenson/hgraph_spec/blob/dd476790a8374b4f75aba09c6ceed8868be0a633/language/docs/design/abstract-atomic-publications.md)
retains an exact concrete member through an abstract-family endpoint.
[reasoned.json](reasoned.json) was written before measurement.

Three fresh processes per engine use the actual `CompoundScalar` abstract
keyword and actual TS compute/eval recorder. Historical Python 0.5.41 rejects
the declaration keyword, so no graph case is claimed there. The native runtime
runs 24 eval calls in total: alternating equal-layout concrete descendants,
repeated values, silence, empty/all-silent inputs, and mutable-child retention
across source mutation, another eval and mutation of a prior capture. Exact
concrete tags and independent owned contents survive each native boundary.

The native Python authoring surface nevertheless accepts construction of the
abstract dataclass itself. The audit preserves this divergence from HGL's
existing nonconstructible-abstract-parent rule. It does not replace the parent
with a concrete stand-in or claim this construction is a valid HGL operation.
Raw recordings for empty/all-silent input remain null.

Package sources, loaded native libraries and the harness are fingerprinted.
This probe does not establish generic family specialization, import closure,
multiple inheritance, optional fields, recursive families, structural family
roots or references. Those require separate compiler/runtime evidence.

```sh
python3 runtime/validation/abstract_atomic/observe.py \
  --python /path/to/historical-python/bin/python \
  --cpp /path/to/native/bin/python --output /tmp/abstract-atomic-fresh.json
python3 runtime/validation/abstract_atomic/check.py
python3 -m unittest discover -s runtime/validation/abstract_atomic
```

Six checker tests preserve tags, repeated ticks, ownership, authoring absence
and the abstract-construction divergence.
