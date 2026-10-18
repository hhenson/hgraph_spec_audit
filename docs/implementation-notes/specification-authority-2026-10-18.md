# Specification authority and extraction history: notes relocated on 18 October 2026

Historical implementation material removed from the specification. These excerpts
were not revalidated and do not assert current support or define the standard.
Required behavior and open semantic decisions remain in the specification.

Source revision: `cde1c4ea9316cf52a7ac58d4cbb7a28bb81048bd`. The [provenance manifest](specification-authority-2026-10-18.provenance.json)
records source hashes, excerpt locations and original text. Relative links in
excerpts resolve to that specification revision.

## README.md

### Excerpt 1

[Source, line 4](https://github.com/hhenson/hgraph_spec/blob/cde1c4ea9316cf52a7ac58d4cbb7a28bb81048bd/README.md#L4).

> reasoned traces and accepted decisions. No Python, C++ or Rust code lives here.

### Excerpt 2

[Source, line 26](https://github.com/hhenson/hgraph_spec/blob/cde1c4ea9316cf52a7ac58d4cbb7a28bb81048bd/README.md#L26).

> Python/C++ probes, experiments and measured results. Accepted expected traces
> stay here; observations never silently replace them.

### Excerpt 3

[Source, line 36](https://github.com/hhenson/hgraph_spec/blob/cde1c4ea9316cf52a7ac58d4cbb7a28bb81048bd/README.md#L36).

> and test locations belong in

### Excerpt 4

[Source, line 39](https://github.com/hhenson/hgraph_spec/blob/cde1c4ea9316cf52a7ac58d4cbb7a28bb81048bd/README.md#L39).

> [PROVENANCE.json](https://github.com/hhenson/hgraph_spec/blob/cde1c4ea9316cf52a7ac58d4cbb7a28bb81048bd/PROVENANCE.json). This repository is a source/data package;
> it has no importable Python package or native implementation.

## runtime/overview.md

### Excerpt 1

[Source, line 424](https://github.com/hhenson/hgraph_spec/blob/cde1c4ea9316cf52a7ac58d4cbb7a28bb81048bd/runtime/overview.md#L424).

> These are intended rules. Proposals and implementation gaps are marked in
> [Evidence](https://github.com/hhenson/hgraph_spec_audit/blob/main/runtime/evidence.md); the written cases do not certify a runtime.

### Excerpt 2

[Source, line 465](https://github.com/hhenson/hgraph_spec/blob/cde1c4ea9316cf52a7ac58d4cbb7a28bb81048bd/runtime/overview.md#L465).

> **Which hgraph.** The C++ runtime's design rulings win. The Python
> implementation holds the original design intent and is used to disambiguate
> where the C++ documents are silent or unclear. hgraph's older specification
> chapters describe the Python-era runtime and are used for framing only. The
> known disagreements are listed in
> [evidence and compatibility record](https://github.com/hhenson/hgraph_spec_audit/blob/main/runtime/evidence.md).

## runtime/conformance.md

### Excerpt 1

[Source, line 37](https://github.com/hhenson/hgraph_spec/blob/cde1c4ea9316cf52a7ac58d4cbb7a28bb81048bd/runtime/conformance.md#L37).

> **optional** behaviour (owner, 2026-09-30):

### Excerpt 2

[Source, line 100](https://github.com/hhenson/hgraph_spec/blob/cde1c4ea9316cf52a7ac58d4cbb7a28bb81048bd/runtime/conformance.md#L100).

> State the expected observations and their rule derivation before execution.
> Compare each observation with isolated Python and C++ runs:
>
> - Reasoning matches both: accept.
> - Reasoning matches either: accept; retain the other result as a variation.
> - Python and C++ agree against reasoning: recheck the derivation and adapter.
>   Record why an expectation changed; never regenerate it from actual output.
> - No pair agrees: ask the user and preserve all three results. A user ruling
>   accepts the contract, not a claim that either implementation conforms.
> - An explicit user ruling supersedes an earlier acceptance. Retain the old
>   expectation, the ruling and both measured results; do not rewrite history.
>
> Python has the stronger testing history and is the preferred guide where
> reasoning leaves an interpretation open. Compare fields separately: one
> matching field does not validate the whole trace. An unavailable observation,
> crash or harness failure is not a matching value. Record the failed phase.
>
> A variation names the case, rules, exact input and observation point, expected
> and actual results, implementation identities, repeats and any remaining
> uncertainty about the adapter or native core. Keep it until reviewed.

## language/docs/design/decisions/0014-native-implementation-interfaces.md

### Excerpt 1

[Source, line 177](https://github.com/hhenson/hgraph_spec/blob/cde1c4ea9316cf52a7ac58d4cbb7a28bb81048bd/language/docs/design/decisions/0014-native-implementation-interfaces.md#L177).

> [conformance acceptance policy]
