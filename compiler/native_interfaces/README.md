# Native-interface compatibility and source migration

This audit separates historical native-interface evidence from current HGL
source identity. `contracts.json` keeps the original `hgraph_revision`,
`upstream_files` and `historical_interface_files` ABI fingerprints immutable.
The public compiler check builds that pinned compiler and runs its original
source inputs through `emit-native-rust`, then compares the formatted output
with the historical ABI baseline. It does not compile the current source
spelling.

The current specification uses receiver-first capability functions. Its
`const-debug.hgl` and `native-provider.hgl` examples therefore differ from the
original upstream files. `shared_files` and `hgl_files` record the current
source bytes, while `source_migrations` links each changed source to an
archived original in [historical_sources](historical_sources/). Those originals
must match the immutable `upstream_files` hashes.

The checker reconstructs the current bytes using exactly three approved
call-spelling substitutions across the two files: scheduler scheduling,
logger information logging and evaluation-clock access. Every other byte
must remain identical. This checks native declarations, annotations and the
rest of the bodies as well as the changed calls; refreshing a current hash
cannot hide an unrelated change. The scalar source and implementation-part
fingerprints remain unchanged. Current Rust interface fingerprints must
still equal the historical ABI fingerprints.

This is a bounded owner-directed source migration and an unchanged ABI
baseline. It is **not evidence that the historical compiler accepts the new
receiver-first syntax**, nor a fresh compilation of those current sources.
Current compiler acceptance belongs to HGL's own checks. The audit retains
its original upstream revision rather than relabelling old compilation
results as measurements of new source text.

HGL keeps its Rust interfaces and implementation parts. Its CI checks their
bytes and current shared source bytes against this manifest; it does not
build C++ hgraph. The public audit does not check out the private HGL
repository.

```sh
# Historical compiler/source check, using the pinned upstream revision.
python compiler/native_interfaces/check.py --upstream <hgraph> --compiler <hgl>
# Current HGL source/interface fingerprint check; no compilation.
python compiler/native_interfaces/check.py --hgl <hgl-checkout>
# Shared current source, archived-original and exact migration checks only.
python compiler/native_interfaces/check.py
```

The Rust formatter version remains pinned. A future declaration or ABI change
requires separate evidence and an explicit update; it cannot use this scoped
spelling migration. The current C++ and Rust implementation-part fingerprints
retain the original scalar signatures and logger injection, with no claim
that a hash check alone validates their runtime behavior.
