# Negative relative yield durations: explicit HGL rejection

**Later ordering extension:** [strict target ordering](../generator_ordering/README.md)
applies across every resolved target, including skipped past entries. The
first target has no predecessor. This page preserves the earlier negative-only
measurement and reasoning; its `past_absolute_later` expected skip is now
superseded by order rejection, as identified in [metadata](supersession.json).
Negative rejection and its operand phase are unchanged.

The current HGL rule rejects every negative relative yield duration after
successful time-expression and payload-expression evaluation, and before
implicit target-time addition or past/due/future classification. Zero remains
admissible, subject to the existing duplicate-publication rule. Past absolute
timestamps retain skip behavior only after strict target-order validation. A failure while evaluating the time
expression prevents payload evaluation; a payload failure prevents admission.

This supersedes the negative-duration skip proposal preserved in the older
[generator operand corpus](../generator_operands/reasoned.json). That original
pre-measurement record and its observations remain unchanged; the linked
[metadata](../generator_operands/supersession.json) identifies the superseded
proposal. The corrected HGL rule is a deliberate language decision, not a
claim that either reference implements a general negative-duration check.

## Measurement

Measured 2026-10-03 from ten cases written in [reasoned.json](reasoned.json)
before the probe. Each case ran in three fresh processes on each engine:
60 processes. [observed.json](observed.json) preserves package/source/native
identities, operand traces, downstream compute captures, raw eval returns and
actual error messages. Only filesystem prefixes are redacted in errors.
Historical Python hgraph 0.5.41 and the native development wheel reporting
0.0.0 were measured through Python authoring; this does not establish native
C++ expression-evaluation order or released-version parity.

The initial evaluation time is `MIN_ST`, one microsecond after the Unix epoch.
The later cases first yield payload 10 at relative `2us`, then resume and
evaluate the tested time and payload 1. A resumed tested yield is followed by
payload 2 at relative `1us`. The initial `-1us` target is the representable
Unix epoch: this case does not involve timestamp arithmetic underflow.

| Case | Historical Python | Native development |
|---|---|---|
| Initial relative `-1us` | Both operands; duplicate-time diagnostic; no downstream capture | Both operands; returns `None`, no downstream capture or resume |
| Relative `-1us` after future prelude | Both operands; resumes; raw `[null,null,1,2]`, downstream `[1,2]` | Both operands; strictly-increasing-time diagnostic; no downstream capture |
| Negative duration with payload exception | Time then payload; payload sentinel exception | Same effects and sentinel |
| Negative duration with time exception | Time effect only; time sentinel exception | Same effects and sentinel |
| Relative `-1000000 days` | Both operands; implicit addition raises datetime range error | Both operands; returns `None`, no downstream capture or resume |
| Explicit `datetime.min - 1us` inside time expression | Time effect only; datetime range error | Same effects and error |
| Initial zero relative duration | Resumes; raw and downstream `[1,2]` | Same |
| Zero relative duration after future prelude | Resumes; raw `[null,null,1,2]`, downstream `[1,2]` | Strictly-increasing-time diagnostic after both operands; no downstream capture |
| Initial past absolute `MIN_ST - 1us` | Skips, resumes; raw `[null,2]`, downstream `[2]` | Returns `None`; no resume or downstream capture |
| Past absolute `MIN_ST + 1us` after future prelude | Skips, resumes; raw `[null,null,10,2]`, downstream `[10,2]` | Strictly-increasing-time diagnostic after both operands; no downstream capture |

The later negative and zero Python cases do not deliver the prelude payload
10 to the downstream compute. This is preserved as observed behavior, not
repaired into a successful prelude recording. On native failures, an empty
downstream capture does not prove that no internal generator output changed;
the probe makes no rollback or hidden-publication claim.

## Failure phases and limits

Historical Python's initial `-1us` error says
`Duplicate time produced by generator: [1970-01-01 00:00:00] - 1`.
Its later negative acceptance proves that this initial error is not a
blanket negative-duration admission rule. The native later error says
`Python generator output times must be strictly increasing`; it also occurs
for the later zero and past-absolute controls. Generic failure agreement
must therefore not be described as matching negative-admission semantics.

The large negative duration is representable as a Python timedelta and as
signed 64-bit microseconds. Adding it to the initial time crosses Python
datetime's year-1 bound. Its Python traceback shows failure in the engine's
`time = et + time`, after both operand effects. This measures Python datetime
range underflow, not signed 64-bit arithmetic underflow or a universal native
timestamp bound. The explicit-underflow control instead fails within the
authored time expression before the payload effect. HGL rejects the negative
duration before its implicit addition; explicit arithmetic performed inside
a time expression can still fail before HGL reaches the admission check.

The checker compares the pre-ordering HGL *effects* separately from actual reference
facts, requires exact diagnostic causes, and preserves every divergence. An
effect labelled `match` does not equate a duplicate/overflow error with HGL's
negative-duration error. Zero after a prelude remains subject to HGL's
one-publication-per-output-per-instant rule; zero admission alone does not
permit duplicate publication. Python's later-zero behavior differs from that
rule, while the initial-zero control confirms the allowed zero case.

## Reproduce

```sh
python3 runtime/validation/generator_negative/observe.py \
  --python /path/to/historical-python/bin/python \
  --cpp /path/to/native/bin/python \
  --output /tmp/new-negative-observed.json
python3 runtime/validation/generator_negative/check.py
```

The recorder refuses to overwrite output and checks identity/repetition
stability. The offline checker validates complete provenance and exact
reference outcomes. `tools/check_recorded.py` includes it and the negative
checker tests; it does not rerun the reference engines.
