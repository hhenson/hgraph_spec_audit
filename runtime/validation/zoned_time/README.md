# Zoned-time publication boundary

The [proposed scalar admission](https://github.com/hhenson/hgraph_spec/blob/3fb31379c1c003985ff85aee6ff4a2ac5129297b/language/docs/design/temporal-scalar-publications.md)
preserves a zoned time as wall-clock microseconds plus the exact zone name.
It has no date, instant or offset. The existing scalar rule supplies repeated
publications, silence, owning capture and recursive leaf admission without
introducing date-dependent resolution.

[reasoned.json](reasoned.json) records the candidate equal/silent trace and
identity controls: equal wall times with alias zone spellings differ, and a
one-microsecond wall-time change differs. Those graph cases remain unmeasured.
This file does not claim the availability result was unknown before inspection.

[observed.json](observed.json) contains three identical fresh-process probes
per engine, with package/source and loaded native-library identities. The
historical Python package reports 0.5.41; the native package reports 0.0.0.
Neither exports `hgraph.ZonedTime`. The native `hgraph.temporal` and `_hgraph`
modules also lack that export; historical Python has neither module.

No eval/pass-through graph was executed for zoned time. A Python datetime,
zoned datetime, or custom struct would change the contract and is not a
substitute oracle. This evidence establishes the measured authoring boundary,
not the absence of every internal native representation, compiler failure,
or Python/C++ publication parity. It is consistent with the earlier
[temporal-scalar availability observation](../temporal_scalars/README.md).
References remain excluded.

Reproduce with actual historical and native interpreter paths:

```sh
python3 runtime/validation/zoned_time/observe.py \
  --python /path/to/historical-python/bin/python \
  --cpp /path/to/native/bin/python \
  --output /tmp/zoned-time-fresh.json
python3 runtime/validation/zoned_time/check.py
python3 -m unittest discover -s runtime/validation/zoned_time
```

The observer refuses overwrite and records exact availability without adapting
missing exports. The checker rejects invented exports, graph execution, wrong
backend identity and changed harness hashes. Once a canonical runtime surface
exists, add graph observations under a new evidence artifact; retain this
unavailable result as the bounded historical observation.
