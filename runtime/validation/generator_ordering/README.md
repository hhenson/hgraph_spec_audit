# Strict ordering across every yielded target

HGL requires each successfully resolved yield target to be strictly greater
than the previous yielded target, across resumptions and including targets
that were skipped because they were already in the past. The first target
has no predecessor. An equal or decreasing subsequent target raises an
exception after successful time and payload operand evaluation; it cannot
be silently skipped merely because it is past.

The negative-duration rule remains separate: after both operands succeed,
a negative relative duration raises before implicit addition. For other
yields, target resolution and the strict-order check precede past/due/future
classification. A valid increasing past target advances the yield history
and is then skipped. A zero relative duration is admissible only when the
resolved target satisfies strict ordering and the other publication rules.
An initial zero has no earlier target and remains allowed.

This is a deliberate HGL contract. Reference measurements below do not prove
that either reference implements every part of that contract. The earlier
[negative-duration audit](../generator_negative/README.md) remains intact.
Its pre-ordering `past_absolute_later` expectation is superseded: after a
future target, an absolute target earlier than that previous target must now
raise, even though it is also past relative to the running body. The
[supersession record](../generator_negative/supersession.json) identifies the
unchanged earlier corpus and the affected expected case.

## Measured reference outcomes

Measured 2026-10-03 with eight cases written in [reasoned.json](reasoned.json)
before measurement, each run in three fresh processes per engine: 48 processes.
[observed.json](observed.json) retains raw results, all operand/resume effects,
downstream compute captures, actual exception messages and full provenance.
The engines are historical Python hgraph 0.5.41 and the native development
wheel reporting 0.0.0, both exercised through Python authoring. Native C++
expression order and released-version parity are not claimed.

Each source yields payloads 1, 2 and 3. The table's target lists are absolute
offsets in microseconds from `MIN_ST` (Unix epoch plus `1us`). Thus `-1` is
exactly the Unix epoch; `-2` and `-3` are pre-epoch. These times are
representable and do not involve arithmetic underflow. Raw results below
include only what the real eval recorder returns; there is no padding.

| Absolute target offsets from MIN_ST | HGL rule | Historical Python | Native development |
|---|---|---|---|
| `[-1,-1,2]` repeated epoch | Reject second target | Skips both past entries; raw `[null,null,3]` | Returns `None` after first operands; no resume |
| `[-3,-3,2]` repeated pre-epoch | Reject second target | Skips both; raw `[null,null,3]` | Same first-yield halt |
| `[-2,-3,2]` decreasing pre-epoch | Reject second target | Skips both; raw `[null,null,3]` | Same first-yield halt |
| `[-3,-2,2]` increasing pre-epoch | Skip first two, publish third | Raw `[null,null,3]` | Same first-yield halt |
| `[-2,-1,2]` increasing across epoch | Skip first two, publish third | Raw `[null,null,3]` | Same first-yield halt |
| `[1,2,3]` increasing future | Publish all three | Raw `[null,1,2,3]` | Same |
| `[2,2,3]` repeated future | Reject second target | Raw `[null,null,2,3]`; first payload is absent downstream | Order exception after second operands; no downstream capture |
| `[2,1,3]` decreasing future | Reject second target | Skips second payload; raw `[null,null,1,3]` | Order exception after second operands; no downstream capture |

All Python cases resume beyond all three yields. The increasing-future native
control does too. On native past-target cases only `time1,value1` occur:
there is no `after1`, second-operand evaluation or order error. That early
termination is not evidence that repeated/decreasing skipped targets were
checked. On native future violations the exact trace is
`time1,value1,after1,time2,value2`, followed by the diagnostic
`Python generator output times must be strictly increasing`.

The separately retained [zero-after-future control](../generator_negative/README.md)
shows the same native order error after both operands. Historical Python
accepts that case and delivers `[1,2]`, losing the earlier prelude payload 10.
The initial-zero control succeeds on both engines. Negative relative
admission, zero admission, target-order rejection and past-target skipping
must therefore remain distinct rules and observations.

These captures report downstream observations. Empty downstream captures on
errors do not establish absence of internal generator output writes, atomic
rollback or allocation behavior. The checker requires exact traces, outputs
and native order diagnostics; it never converts Python skips or native early
termination into HGL order rejection.

## Reproduce

```sh
python3 runtime/validation/generator_ordering/observe.py \
  --python /path/to/historical-python/bin/python \
  --cpp /path/to/native/bin/python \
  --output /tmp/new-ordering-observed.json
python3 runtime/validation/generator_ordering/check.py
```

The runner requires a new output path and verifies identity and repetition
stability. `tools/check_recorded.py` validates the saved corpus, harness,
provenance and observations and runs the negative checker tests without
executing either engine.
