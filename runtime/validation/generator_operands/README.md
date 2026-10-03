# Generator yield operands and timing boundaries

**Superseded proposal:** the negative-duration skip proposal preserved in
`reasoned.json` is historical, not current HGL policy. The
[negative-duration correction](../generator_negative/README.md) requires
rejection after both operands succeed and before implicit target addition.
[Supersession metadata](supersession.json) identifies the unchanged original
corpus. Past absolute targets still skip under HGL.

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
past its second yield. The review remeasurement preserves the actual exception
text, including its stack/activation trace, with only filesystem prefixes
redacted as `<audit-root>`, `<environment>` and `<private-home>`. Python reports
`Duplicate time produced by generator: [1970-01-01 00:00:00.000001] - 2`;
the native engine reports `Python generator output times must be strictly increasing`.
The checker requires the exact engine diagnostic line and exception type;
a generic failure after operand evaluation cannot satisfy this case. No runtime payload-retention or allocation-failure
claim is added by these scalar traces.

Two timing cases diverged from the original, now superseded uniform
past-target skip proposal:

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
the later explicit negative-duration rejection decision is documented in the
linked correction, separately from these measured engine behaviors.

## Reproduce

```sh
python3 runtime/validation/generator_operands/observe.py \
  --python /path/to/python-hgraph/bin/python \
  --cpp /path/to/native-hgraph/bin/python \
  --output /tmp/generator-operands-observed.json
python3 runtime/validation/generator_operands/check.py
```

The runner refuses to overwrite evidence. The saved report includes corpus,
harness, assessment-helper, error-contract, identity-helper, package and native
binary hashes. The checker validates the package identity digest, source and
artifact manifests, eval helper source, native artifacts and loaded libraries,
including consistency between the overlapping manifests. This establishes
recorded provenance consistency, not independent authenticity of the wheel.

The original `reasoned.json` remains unchanged. The separately labelled
[error_contract.json](error_contract.json) records the diagnostic spelling
inspected during review before the three fresh-process remeasurement runs.
The new `observed.json` includes those actual error details; its package
identity records the fresh historical-Python installation. The original
observations remain in Git history. The checker reproduces the original
past-target divergences and requires the four claimed agreements. Negative
tests reject unrelated failures, diagnostics appearing only later in a
traceback, missing error details and altered provenance. Checking saved
evidence does not execute engines.
