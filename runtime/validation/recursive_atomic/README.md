# Finite recursive atomic values

The [recursive atomic admission](https://github.com/hhenson/hgraph_spec/blob/d9303b8248717dd89891f5e5b7e43fc093731ebf/language/docs/design/recursive-atomic-publications.md)
uses existing direct optional recursive edges and complete ordinary values.
[reasoned.json](reasoned.json) preceded the actual graph measurements.

Three identical fresh processes per engine run 54 eval calls in total.
Historical Python 0.5.41 and native 0.0.0 both accept self-recursive and mutually
recursive CompoundScalar declarations through their actual authoring surfaces.
A real TS compute returns `delta_value` into its own output; the actual eval
recorder captures the result. Package/source/native-library hashes identify
what ran.

Both preserve a depth-three chain, equal repeated trees, silence, terminal
unset edges and complete replacement by a leaf. A mutual A/B/A tree preserves
the nominal type at each depth. Empty/all-silent raw self-recursive recordings
remain null. No object identity or flattened leaf list replaces the observed
tree structure.

The ownership control changes a list inside the deepest descendant, then runs
a second eval and changes one first-run capture's deepest list. Native retains
independent trees across all boundaries. Historical Python aliases the source,
sibling captures and second recording. The checker preserves that divergence;
ordinary publication agreement does not establish historical deep-copy parity.

This does not establish arbitrary depth, recursive generic declarations,
abstract recursive families, branching-tree breadth, container recursion,
cyclic-object rejection, structural clearing, imported descriptors or
references. The schema graph and concrete values tested are finite.

```sh
python3 runtime/validation/recursive_atomic/observe.py \
  --python /path/to/historical-python/bin/python \
  --cpp /path/to/native/bin/python --output /tmp/recursive-atomic-fresh.json
python3 runtime/validation/recursive_atomic/check.py
python3 -m unittest discover -s runtime/validation/recursive_atomic
```

Six tests reject dropped repeats, altered deep nominal identity, retained old
subtrees, hidden Python aliases and introduced native aliases.
