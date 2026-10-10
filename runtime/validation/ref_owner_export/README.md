# Owned REF export observations

The reasoned corpus was committed before measurement at
`5fd42fd573425186074b4e12fdb2aa8a09b0e5a6`. Its four cases reproduce both
fresh evals of the two [Std50](https://github.com/hhenson/hgraph_std/pull/50)
groups at `11636557ddd228dcbd22a79904d694ec1c4df4ab`. The route contract is
[Spec95](https://github.com/hhenson/hgraph_spec/pull/95) GRF-27/TS-20 at
`4e83fe121bf92293b98fdd1b5e4b1bd362b6450a`, with existing TS-16/17/25.

The probe builds analogous public graphs with ordinary compute producers,
opaque REF relays, and nested switch owners. The pair uses `TSB.from_ts` to
assemble child connections, then emits the exported designation. An ordinary
same-shaped consumer publishes deltas; a `TS[str]` observer captures JSON
instead of recording an Any payload. Each public interpreter runs three fresh
processes, and each process runs both cases twice with fresh graph state.
Loaded package, native-library and source fingerprints identify each artifact.
The raw `eval_node` result remains separate from decoded captures and the view
padded solely to the input horizon. Exceptions retain partial observations.

The scalar requirement is `[7,21,22,73,204,25,13,null]`. For the tree, the inner
switch retargets only right: left remains bound and only right samples 8.
Subsequent shared-left publication produces both 9s. An outer retarget then
samples both new endpoints `(9,40)`, including its equal-valued left child.
The trailing silent horizon is retained. Requirements are never replaced by
observations.

| Case (both fresh evals) | Public Python | Installed C++ interpreter |
|---|---|---|
| Two nested scalar REF output boundaries | Matches the frozen eight-cycle trace | Matches the frozen eight-cycle trace |
| Exported child tree: sparse ticks and retarget samples | Matches all ten cycles | Cycle 4 is silent instead of the required right-only `{"right":8}` sample; all other cycles match |

All three processes agree per interpreter. The selected package, eval helper,
native artifact and loaded-library fingerprints exactly match the respective
Audit58 identities. The C++ bridge expresses both graphs and records the
child-tree retarget divergence; it is not an unavailable native authoring
surface. The evidence-only checker preserves this actual missing sample,
including a corruption test that tries to replace it with the required sample.

This measures public Python and the installed C++ interpreter bridge. It
claims neither direct installed-SDK native C++ execution nor HGL compilation,
execution, lowering or backend conformance. The separate owner-expiry audit
is unchanged.

Run `python check.py` and `python -m unittest discover -s . -p test_check.py`
for recorded-evidence verification. Measurement requires explicit independent
`--python`, `--cpp`, and new `--output` paths; no private host paths are tracked.
