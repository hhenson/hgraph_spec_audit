# NaN comparison and negative logarithm audit

Measured 2026-10-06 with historical Python hgraph 0.5.41 and the genuine native
development runtime reporting 0.0.0, both under Python 3.14.4. All 28
[candidate expectations](reasoned.json) and [reasoning](reasoning.md) were
committed before execution. Each engine repeated identically in three fresh
processes. No HGL semantics, compiler, standard library, constructors or
reference runtime files are changed.

| Cases | Historical Python | Native runtime |
|---|---|---|
| NaN vs NaN: eq, ne, lt, le, gt, ge | false, true, false, false, false, false | Same |
| NaN vs 1.0, and 1.0 vs NaN | Same six results in both operand orders | Same |
| 1.0 vs 1.0 finite controls | true, false, false, true, false, true | Same |
| ln(1.0) | Present 0.0 | Present 0.0 |
| ln(-1.0) | Raises ValueError through NodeException | Present NaN |
| ln(-1.0) compared with itself: eq/ne | Upstream logarithm raises | false/true |

Thus 24 registered comparison cases match in both engines. The native runtime
matches all 28 cases; Python matches 25 and retains three logarithm errors.
Python's underlying `math.log` reports “expected a positive input, got -1.0”.
The historical error is not converted into a NaN result or comparator success.
Every successful case also preserves its trailing silent slot, and independent
sinks confirm false and zero are present, valid, modified publications.

Neither `is_nan` nor `isnan` is exported by either tested public hgraph facade;
neither name exists in the native registered-operator list. This is a bounded
primitive-availability result, not a claim that no internal C++/Python floating
point classification helper exists. The observation harness uses `math.isnan`
only to classify captured float data externally; that does not add a source
primitive.

## Source assertion consequence, not a semantic selection

If a specification adopts the observed NaN inequality rule, an ordinary
runtime compute returning `value != value` can produce a Boolean assertion
result for NaN. A corresponding native graph `ln(-1.0) != ln(-1.0)` has direct
reference evidence here. Historical Python cannot supply that operand through
its ln implementation; its error remains a divergence from the frozen OP-10
expectation. No NaN equality assertion, bit-pattern identity or NaN constructor
is required. This audit does not choose HGL comparison rules or add source syntax.

Python floating equality has an existing tolerance-based implementation. These
NaN cases and exactly equal finite controls do not settle tolerance for distinct
nearby finite values. There is no signaling/quiet NaN, sign, payload, IEEE
exception flag, or f32 claim.

## Evidence and reproducibility

[observe.py](observe.py) wires each genuine registered `eq_`, `ne_`, `lt_`,
`le_`, `gt_`, `ge_` and `ln` operator through public graph/eval_node. It does
not implement native comparisons using Python `==`. Replay-supplied NaN is a
private reference fixture, not an admitted HGL literal. Separate sinks record
operand and result publication metadata. NaN output uses a JSON classification
object; the file contains no nonstandard JSON numeric NaN token.

[observed.json](observed.json) retains raw eval results, comparison deltas,
input presence, errors, exact corpus/harness hashes, installed package/source
manifests and actual loaded native library hashes. The development version
string is not a published release claim. The identity is checked before and
after each process, with private filesystem paths excluded from provenance and
redacted in diagnostics. No source checkout hash substitutes for binary identity.

```sh
python3 runtime/validation/nan_comparisons/observe.py \
  --python /path/to/historical/bin/python \
  --cpp /path/to/native/bin/python --output /tmp/new-nan-observed.json
python3 runtime/validation/nan_comparisons/check.py
python3 -m unittest discover -s runtime/validation/nan_comparisons -p 'test_*.py'
```

The checker and all 13 regression tests pass, including false-vs-absence,
false-vs-zero, real NaN operands, finite positive controls, retained domain
errors, primitive absence and native identity. `git diff --check` passes.
Checking saved evidence does not execute engines. The checker is registered
with `tools/check_recorded.py`; that full runner has a pre-existing first-check
failure because `runtime/validation/assertions.json` is absent in this checkout.
