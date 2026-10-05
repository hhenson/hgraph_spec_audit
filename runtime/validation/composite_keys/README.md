# Finite composite collection keys

The [composite key contract](https://github.com/hhenson/hgraph_spec/blob/0f172a3/language/docs/design/composite-collection-keys.md)
admits complete tuple and concrete struct keys. Reasoning was written before
measurement, and actual graph inputs use independently constructed equal keys.

Both historical Python and native runtimes preserve tuple components and
concrete struct fields through actual TSS/TSD delta pass-through and recording.
Adding an equal set member produces no second membership addition; an equal
map child update still publishes. Removal and later reinsertion preserve the
complete key. Empty/all-silent raw recordings remain null. Three fresh
processes per engine run 96 eval calls in total, with matching observations.

This evidence covers two immutable key shapes (`tuple[int,str]` and a frozen
concrete struct with int/string fields). It does not establish mutable-source
key retention, optional fields, provider children, hash-collision behavior,
recursive or abstract keys, collection-containing keys or references. Full
source checking remains a compiler obligation. No composite is converted to a
string or integer in the runtime under test; JSON tags only encode observations.

Package sources, loaded libraries, reasoning and harness are fingerprinted.

```sh
python3 runtime/validation/composite_keys/observe.py \
  --python /path/to/historical-python/bin/python \
  --cpp /path/to/native/bin/python --output /tmp/composite-keys-fresh.json
python3 runtime/validation/composite_keys/check.py
python3 -m unittest discover -s runtime/validation/composite_keys
```

Six checker tests preserve nominal/component identity, canonical membership,
equal child updates and removals.
