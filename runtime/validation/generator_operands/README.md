# Generator yield operands and timing boundaries

Measured 2026-10-03, with six prewritten cases and three fresh-process runs
per engine. This exercises the Python authoring surface on historical
Python hgraph 0.5.41 and the native development engine. It does not measure
native C++ expression evaluation order.

The proposed language rule evaluates the time expression and then the payload
expression, each once, before applying the generator's time rule. A failure
in the first prevents the second; failure in either prevents suspension or
publication for that yield. The marked Python expressions establish a
reference authoring trace, while engine behavior determines publication,
resumption and error results. This separation matters: Python evaluates a
yielded tuple before handing it to either engine.

Both engines match the prewritten future-resumption trace, time-operand
failure, past-yield payload failure, and duplicate-due-publication failure.
The duplicate evaluates both operands before failing and does not resume
past its second yield. No runtime payload-retention or allocation-failure
claim is added by these scalar traces.

Two timing cases diverge from the proposed uniform past-target skip:

| Case | Historical Python | Native development engine |
| --- | --- | --- |
| Absolute `MIN_ST - MIN_TD`, followed by a valid future yield | Skips the first, resumes, publishes the second | Returns no recording and never resumes after the first yield |
| Relative `-MIN_TD` at the first body evaluation | Fails after evaluating both operands | Returns no recording and never resumes after the first yield |

These exact boundary cases resolve to the instant immediately before the
minimum start time. They do not establish behavior for every past instant,
negative duration after a later resume, or values outside datetime range.
The observed failures/early termination are retained; they are not normalized
into skip behavior or replaced by expected results.

The HGL specification already requires skipping past absolute times and has
a pre-epoch example. That agreed behavior remains a specification rule even
where this native development observation differs. Clarifying yield operand
order is a separate source-language choice supported by the authoring trace;
clarifying negative durations requires an explicit language decision, not a
claim of existing agreement between these engines.

## Reproduce

```sh
python3 runtime/validation/generator_operands/observe.py \
  --python /path/to/python-hgraph/bin/python \
  --cpp /path/to/native-hgraph/bin/python \
  --output /tmp/generator-operands-observed.json
python3 runtime/validation/generator_operands/check.py
```

The runner refuses to overwrite evidence. The saved report includes corpus,
harness, identity-helper, package and native binary hashes. The checker
recomputes assessments including divergences and does not execute engines.
