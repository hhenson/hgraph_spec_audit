# Retained ordinary structural deltas

Measured 2026-10-03 against prewritten expectations, with three identical
fresh-process runs for each probe. This adds six sparse shapes: integer set,
fixed integer list, named bundle, integer map, nested map, and list of maps.
The traces include partial updates and removals; missing children are never
filled from held values.

## Ordinary native storage

The direct native probe constructs canonical delta Values, retains each in
an ordinary timestamp/payload tuple, appends it to an ordinary mutable list,
sets that list in GlobalState and extracts an owning recording. It then
replaces the original payload, tuple, list element and global entry and
destroys their owners. The retained recording still contains exactly the
original timestamp and sparse delta and differs from the replacement.
All six cases match. The executable, source, installed SDK headers and
loaded native libraries are hashed; native library hashes match the
Python-authored native measurements below.

This measures independent value retention through ordinary containers, not
HGL nominal identity, fixed-size delta identity or type-expression inference.
It does not add a native replay overload, inspect a stale borrowed view or
claim allocation-failure behavior. The tested delta payloads are immutable
native values; replacing owners and mutating the containing list are the
operations exercised.

## Actual source, compute and record

Each Python-authored graph has a generator source, a compute returning its
input delta, and the actual eval recorder. Historical Python hgraph 0.5.41
and the native development engine are measured independently.

| Authored input ownership | Historical Python | Native development |
| --- | --- | --- |
| Reuse and mutate one generator payload container | All six traces diverge: the intermediate update is lost/replaced in the observed trace | All six match |
| Independently copied payloads, preserving the REMOVE singleton | All six match | All six match |
| Naive `deepcopy`, including REMOVE | Three map-containing cases fail because the copied sentinel loses removal identity; other cases match | All six match |

The original, copied control and naive-copy control are saved separately.
The errors are not converted into removal success. Naive-copy diagnostic
object IDs are normalized solely for stable diagnostic comparison; result
payloads are untouched. Both successful controls retain their returned
captures after the reused producer container is cleared and garbage
collection runs. Historical aliasing is not presented as independent-copy
semantics, and arbitrary `deepcopy` is not treated as a universal delta-copy
operation.

## Consequences for the HGL extension

The observations support using independently retained sparse delta data as
ordinary list/struct/global payloads. The proposed `delta_of(T)` source type,
exact originating-shape identity, generic matching and ordinary ownership
boundaries remain deliberate HGL rules. Copying must preserve semantic marker
identity as well as children and omissions. A complete endpoint snapshot
must not replace a sparse delta merely to make storage convenient.

This does not settle empty-event application, invalidation, invalid-child
membership, references, signals, windows or atomic boundaries. It also does
not measure the entire proposed HGL replay/record body, constructor effect
order or arbitrary allocation failures. Those limits remain separate from
the observed successful retention paths.

## Reproduce

Run `observe.py`, `control.py`, and `control_deepcopy.py` with independent
`--python` and `--cpp` interpreters and a fresh `--output` for each. Build
`native.cpp` with this directory's CMake project against the installed native
SDK; that SDK requires its declared matching nanobind version and a compiler
runtime compatible with its shared libraries. Run `native_observe.py` with
`--executable`, `--sdk-include` and a new `--output`.

`python3 runtime/validation/owned_deltas/check.py` validates saved evidence
and reproduces all matches, divergences and errors without executing engines.
