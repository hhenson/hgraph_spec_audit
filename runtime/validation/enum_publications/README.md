# Declared enum publications

The [enum publication admission](https://github.com/hhenson/hgraph_spec/blob/c40b3ef73c5e9a22e63077c60fe74e08239fe015/language/docs/design/enum-publications.md)
uses the existing nominal enum scalar identity. [reasoned.json](reasoned.json)
was written before these graph measurements: the delta is the complete enum
member, equal repeats publish, and silence does not substitute a held value.

[observed.json](observed.json) records three identical fresh-process runs per
engine, 48 eval calls in total. Historical Python 0.5.41 and native 0.0.0
both run a real `TS[Mode]` compute returning `delta_value` into its own output,
recorded by the actual eval recorder. Package/source/native-library hashes
identify each runtime.

Four traces cover repeated and distinct members, leading/interior/trailing
silence, all-silent input, and empty input. Member numbers include -7, 11 and
the signed `i64` maximum. Received value and delta retain `Mode`, member name
and number. Ordinary controls distinguish another enum with the same name and
number, and distinguish the integer itself. A second eval preserves the first
recording. Raw all-silent/empty output is null on both engines; it is not
fabricated into a dense recording by this audit.

This is bounded two-engine publication agreement through the Python authoring
surface. It does not prove HGL compilation, native imported-unknown handling,
physical enum ABI, set/map admission or composite ownership. Enum objects are
immutable; retained recordings do not establish mutable-container isolation.
References remain excluded.

```sh
python3 runtime/validation/enum_publications/observe.py \
  --python /path/to/historical-python/bin/python \
  --cpp /path/to/native/bin/python \
  --output /tmp/enum-publications-fresh.json
python3 runtime/validation/enum_publications/check.py
python3 -m unittest discover -s runtime/validation/enum_publications
```

The checker fixes independent expected patterns and verifies exact observations
and provenance. Six tests reject lost identity, narrowed numbers, dropped
repeats, altered retained recordings and invented raw all-silent output.
