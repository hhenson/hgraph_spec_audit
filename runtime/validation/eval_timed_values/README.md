# Ordinary timed values for scalar eval

Measured 2026-10-03. This extends the earlier
[ordinary value-sequence evidence](../value_sequences/README.md) from one
integer trace to all eight scalar types, with silent and empty inputs. It
tests a proposed source representation, not a new replay-specific capability.

The expectations in [reasoned.json](reasoned.json) were written before the
probe. Each dense input is normalized into an ordinary constant list of
timestamp/payload pairs containing only its present positions. An ordinary
generator receives that list directly, a compute returns its input delta,
and the real eval recorder captures the output. The original input horizon
is retained separately. False, zero and empty text are present payloads;
they are never removed by a truthiness filter.

[observed.json](observed.json) records three identical fresh-process runs
per engine, with package, source and native binary identities. Historical
Python hgraph 0.5.41 and the native development wheel reporting 0.0.0 both
match all 24 prewritten dense results. This is the Python authoring surface
of the native engine; the earlier direct-native integer probe remains its
separate corroboration. No released-version parity claim is added.

The raw eval result is preserved. Horizon materialization is a separately
labelled calculation: it restores trailing silent positions and makes an
all-silent input different from an empty input. It does not claim that the
source, recorder or reference helper produced those padded positions. Empty
timed data produces no publications even when the external horizon is nonzero.

## Consequences for the HGL proposal

This supports using ordinary timed values for replay and recording. A library
may name a timestamp/payload pair with an ordinary generic struct; that is a
source spelling decision, not a new runtime type category. Eval can translate
its harness slots into present timed values and retain the dense horizon
itself. Scalar replay then needs no absent list element and no nullable
storage type. This does not resolve general nullable ordinary values.

The prior ordinary-value audit supplies the independent-retention evidence
and distinguishes Python aliasing from native mutable access. The HGL rules
for retained constructor arguments, list insertion and typed global borrowing
remain language choices; these observations do not establish arbitrary
allocation-failure behavior.

Eval normalization must retain its existing checks for representable slot
times and finite input length. Independently supplied replay entries can use
the existing generator scheduling rules; this evidence does not establish
a stricter timestamp-admission policy. Record can retain an ordinary
timestamp/delta value in its typed global list. This probe used only valid
ordered timestamps and does not establish behavior for malformed or
out-of-order reference inputs. The frozen reasoned file also records an
initial proposal for strict pre-start timestamp admission. That unmeasured
proposal was dropped after checking the existing HGL generator contract; it
is preserved in the pre-measurement record, not adopted as a conclusion.

Structural deltas still need an ordinary storable representation. This audit
does not equate a complete collection value with its publication delta or
claim coverage of signals, references, windows, invalidations or empty
structural publication events. Eval's collision policy for recorder keys also
remains a separate source-contract decision.

## Reproduce

```sh
python3 runtime/validation/eval_timed_values/observe.py \
  --python /path/to/python-hgraph/bin/python \
  --cpp /path/to/cpp-hgraph/bin/python \
  --output /tmp/new-timed-values-observed.json
python3 runtime/validation/eval_timed_values/check.py
```

The runner refuses to overwrite a result and preserves errors. The checker
checks saved evidence and provenance; it does not rerun the engines. No native
performance or allocation benchmark was measured here.
