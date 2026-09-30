# Native-interface compatibility

This audit owns the C++ compiler to Rust native-interface check. CI builds the
pinned public hgraph compiler and compares its formatted `emit-native-rust`
output with the fingerprints in `contracts.json`. Scalar and logger-capability
contracts are covered, together with bootstrap source identity.

HGL keeps its Rust interfaces and implementation parts. Its CI checks their
bytes against the pinned audit fingerprints; it does not build C++ hgraph.
The public audit never checks out the private HGL repository. HGL sources stay
in the specification, standard library and implementation repositories.

```sh
# Public audit: use a compiler built from the pinned upstream revision.
python compiler/native_interfaces/check.py --upstream <hgraph> --compiler <hgl>
# Offline HGL check; no compiler is needed.
python compiler/native_interfaces/check.py --hgl <hgl-checkout>
```

With no arguments, the checker verifies only the pinned shared inputs. This is
part of recorded-evidence validation and is not a fresh compiler measurement.

When contracts change, update the public source revision and fingerprints,
run the compiler audit, then update HGL's interfaces and audit pin together.
The Rust formatter version is pinned so formatting does not drift between jobs.
The C++ target parts used by this audit have the same scalar signatures and
logger injection as HGL's Rust target parts; the generated interface fingerprint
must agree for both implementations.
