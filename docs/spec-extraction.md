# Specification extraction

This is the agreed method for extracting rules from existing code. Additional
rules come from the project owner. Record origins and acceptance here; the
[specification](https://github.com/hhenson/hgraph_spec) states the resulting
contract. Conformance runs compare against that contract.

State the expected observations and their rule derivation before execution.
Compare each observation with isolated Python and C++ runs:

- Reasoning matches both: accept.
- Reasoning matches either: accept; retain the other result as a variation.
- Python and C++ agree against reasoning: recheck the derivation and adapter.
  Record why an expectation changed; never regenerate it from actual output.
- No pair agrees: ask the user and preserve all three results. A user ruling
  accepts the contract, not a claim that either implementation conforms.
- An explicit user ruling supersedes an earlier acceptance. Retain the old
  expectation, the ruling and both measured results; do not rewrite history.

Python has the stronger testing history and is the preferred guide where
reasoning leaves an interpretation open. Compare fields separately: one
matching field does not validate the whole trace. An unavailable observation,
crash or harness failure is not a matching value. Record the failed phase.

A variation names the case, rules, exact input and observation point, expected
and actual results, implementation identities, repeats and any remaining
uncertainty about the adapter or native core. Keep it until reviewed.
