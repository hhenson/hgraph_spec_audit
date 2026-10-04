# Retained-candidate specialization: evidence boundary

Status: reasoned HGL compiler rule; no fresh compiler measurement in this record.

The [source extension](https://github.com/hhenson/hgraph_spec/commit/22766590fa984dfd2536a17460c00a8568e2237b)
separates compile-time substitution from reading a generic parameter as a value.
The prior language rules already distinguished concrete-required body/storage
types, resolver markers and reification. The ordinary-delta proposal also
required substitution before formation and prohibited unresolved types in an
instantiated value or graph. Neither statement previously specified how a
retained candidate obtains its concrete body/storage specialization. The new
rule closes that gap; it is not a claim that the earlier text already required it.

The [compiler cases](https://github.com/hhenson/hgraph_spec/blob/22766590fa984dfd2536a17460c00a8568e2237b/compiler/cases_retained_specialization.md)
state the reasoned admission, substitution, identity and rejection expectations.
They do not introduce runtime reflection, body-visible generic values, residual
constraints or new storage shapes.

## What the references establish

| Question | Evidence and limit |
|---|---|
| Can ordinary containers retain sparse delta data independently? | The [owned-delta audit](https://github.com/hhenson/hgraph_spec_audit/blob/cf431ec659442a0a30d30be4bde443b3d8a8d320/runtime/validation/owned_deltas/README.md) records six structural shapes through direct native ordinary storage and independent Python/native graph probes. Native traces and the historical Python copied-payload control match the prewritten expectations. Reused Python payloads diverge; naive copying loses removal-marker identity in map cases. |
| Does that establish HGL retained body specialization or exact delta identity? | No. The audit explicitly excludes HGL nominal/fixed-size identity and type inference. Its successful retention paths support the storage premise only. |
| Is there a Python/C++ runtime analogue of `instantiate op<_>`? | Not in these probes. It is an HGL source-compiler admission rule, so neither runtime observation is a pass or failure for that syntax. The new compiler cases remain unmeasured here. |
| Is generic value reification now supported? | No. The extension preserves that separate boundary. The [historical compiler notes](../../docs/implementation-notes/language/docs/design/language-model.md) describe the earlier retained-marker limitation; they are historical implementation evidence, not authority for the new rule. |

A fresh compiler campaign must identify its source and shared-input revisions,
run the shared cases without deriving expectations from either implementation,
and preserve rejection diagnostics and missing coverage. Agreement on runtime
retention does not substitute for those compiler checks. This note adds no
measurement, changes no archived observation, and claims no whole-library parity.
