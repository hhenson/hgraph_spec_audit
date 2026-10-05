# Scalar set members and map keys

The [scalar-key extension](https://github.com/hhenson/hgraph_spec/blob/06e576a34a4fa22c0876e5db18335cbbd3075b2f/language/docs/design/scalar-collection-keys.md)
uses exact ordinary equality/hash for temporal set members and map keys.
[reasoned.json](reasoned.json) and [float_reasoned.json](float_reasoned.json)
were written before their respective graph measurements.

The scalar probe runs a real compute returning `delta_value` to its own output
through the actual eval recorder. Nine families agree in historical Python
0.5.41 and native 0.0.0: bool, integer, float, string, date, time, datetime,
duration and a declared enum. Native additionally passes civil datetime,
timezone and zoned datetime, which are unavailable in historical Python.
Zoned time remains unavailable in both canonical authoring surfaces.

Set traces add two values, remain silent, then remove one. Map traces add two
keys, publish an equal value at one key, remain silent, then remove that key.
Zone aliases remain distinct, including zoned datetimes with equal instant and
offset but different exact zone names. Observation tokens `a`/`b` are assigned
only after exact Python type and ordinary scalar equality checks; ordering of
members/keys is ignored. No stringification drives membership.

[float_observed.json](float_observed.json) separately retains IEEE boundaries:

| Boundary | Python | Native |
|---|---|---|
| +0/-0 | Same membership/key; update retains one key | Same |
| +infinity/-infinity | Two distinct keys/members; removal works | Same |
| Two distinct NaN objects, then remove the original first object | Removes one, leaving one | TSS emits no removal tick; TSD raises `REMOVE: key not present in TSD (use REMOVE_IF_EXISTS to remove-if-present)` with no recorded compute calls |

The NaN result is a disagreement, not a selected source policy. No native
exception is repaired or converted into a publication. Python object identity
can affect NaN container behavior despite nonreflexive floating equality.
The specification extension keeps NaN application unresolved and outside its
bounded admission. This does not establish a general NaN-rejection contract.

Each probe ran three identical fresh processes per engine. The scalar matrix
contains 126 eval calls; the IEEE boundary probe adds 36. Both artifacts carry
package/source and loaded native-library digests. These are bounded runtime
observations, not proof of HGL constructors, cold provider validation,
composite keys, atomic sets/maps, invalidations or reference support.

```sh
python3 runtime/validation/scalar_collection_keys/observe.py \
  --python /path/to/historical-python/bin/python \
  --cpp /path/to/native/bin/python --output /tmp/scalar-keys-fresh.json
python3 runtime/validation/scalar_collection_keys/float_observe.py \
  --python /path/to/historical-python/bin/python \
  --cpp /path/to/native/bin/python --output /tmp/float-keys-fresh.json
python3 runtime/validation/scalar_collection_keys/check.py
python3 -m unittest discover -s runtime/validation/scalar_collection_keys
```
