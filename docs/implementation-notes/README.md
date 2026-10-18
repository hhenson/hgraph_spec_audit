# Implementation notes relocated from the specification

The specification defines portable rules, examples and expected traces. These
notes retain compiler progress reports, source pointers, build recipes and
implementation rationale removed from that specification.

This is a dated documentary record, **not a current support matrix or a new
validation result**. Status claims inside excerpts retain their original
context and may be superseded. Follow the active compiler audits and runtime
evidence for measured results. No observations, expected traces or dependency
pins were changed by this relocation.

Original source revision: [`766033278bef`](https://github.com/hhenson/hgraph_spec/tree/766033278bef6e9403cc99c0d8f318ba46a03919).
[Provenance](provenance.json) records each source file's hash and excerpt count.
Local documentation links in excerpts resolve to that revision. HGL files and
portable examples remain owned by the specification and standard library.

- [language/docs/design/control-flow.md](language/docs/design/control-flow.md)
- [language/docs/design/decisions/0005-inline-cpp-native-functions.md](language/docs/design/decisions/0005-inline-cpp-native-functions.md)
- [language/docs/design/decisions/0006-multi-file-module-parts.md](language/docs/design/decisions/0006-multi-file-module-parts.md)
- [language/docs/design/decisions/0007-parameter-packs.md](language/docs/design/decisions/0007-parameter-packs.md)
- [language/docs/design/decisions/0008-temporal-contracts-and-target-mappings.md](language/docs/design/decisions/0008-temporal-contracts-and-target-mappings.md)
- [language/docs/design/decisions/0009-native-errors-and-the-node-error-model.md](language/docs/design/decisions/0009-native-errors-and-the-node-error-model.md)
- [language/docs/design/decisions/0010-lifecycle-capabilities.md](language/docs/design/decisions/0010-lifecycle-capabilities.md)
- [language/docs/design/decisions/0011-cache-declarations.md](language/docs/design/decisions/0011-cache-declarations.md)
- [language/docs/design/decisions/0012-recursive-struct-fields.md](language/docs/design/decisions/0012-recursive-struct-fields.md)
- [language/docs/design/decisions/0013-struct-imports.md](language/docs/design/decisions/0013-struct-imports.md)
- [language/docs/design/decisions/0014-native-implementation-interfaces.md](language/docs/design/decisions/0014-native-implementation-interfaces.md)
- [language/docs/design/decisions/0015-pull-sources.md](language/docs/design/decisions/0015-pull-sources.md)
- [language/docs/design/decisions/README.md](language/docs/design/decisions/README.md)
- [language/docs/design/documentation.md](language/docs/design/documentation.md)
- [language/docs/design/iteration.md](language/docs/design/iteration.md)
- [language/docs/design/language-model.md](language/docs/design/language-model.md)
- [language/docs/design/migration-requirements.md](language/docs/design/migration-requirements.md)
- [language/docs/design/modules.md](language/docs/design/modules.md)
- [language/docs/design/native-implementation-parts.md](language/docs/design/native-implementation-parts.md)
- [language/docs/design/native-interface.md](language/docs/design/native-interface.md)
- [language/docs/design/native-interfaces.md](language/docs/design/native-interfaces.md)
- [language/docs/design/native-surface-proposal.md](language/docs/design/native-surface-proposal.md)
- [language/docs/design/node-authoring.md](language/docs/design/node-authoring.md)
- [language/docs/design/operators.md](language/docs/design/operators.md)
- [language/docs/design/switch.md](language/docs/design/switch.md)
- [language/docs/design/type-extensions.md](language/docs/design/type-extensions.md)
- [language/docs/developer-guide/syntax-and-semantics.md](language/docs/developer-guide/syntax-and-semantics.md)
- [language/docs/user-guide/README.md](language/docs/user-guide/README.md)
- [language/docs/user-guide/functions.md](language/docs/user-guide/functions.md)
- [language/docs/user-guide/language-tour.md](language/docs/user-guide/language-tour.md)
- [language/docs/user-guide/modules-and-tools.md](language/docs/user-guide/modules-and-tools.md)
- [language/docs/user-guide/testing-and-running.md](language/docs/user-guide/testing-and-running.md)
- [language/docs/user-guide/types-and-expressions.md](language/docs/user-guide/types-and-expressions.md)
- [language/docs/user-guide/value-functions.md](language/docs/user-guide/value-functions.md)
- [library/operator_contracts.md](library/operator_contracts.md)
- [runtime/graph.md](runtime/graph.md)
- [runtime/injectables.md](runtime/injectables.md)
- [runtime/node.md](runtime/node.md)
- [runtime/representations.md](runtime/representations.md)
- [runtime/scalar_types.md](runtime/scalar_types.md)
- [wiring/wiring.md](wiring/wiring.md)

## Later relocations

- [17 October 2026: examples index, injectables and node state](2026-10-17-cleanup.md)
  ([provenance](2026-10-17-cleanup.provenance.json)), from specification revision
  [`95292403cd80`](https://github.com/hhenson/hgraph_spec/tree/95292403cd8066a375b6747609f868402616f123).
- [17 October 2026: library operator contract comparisons](library/operator-contracts-cleanup-2026-10-17.md)
  ([provenance](library/operator-contracts-cleanup-2026-10-17.provenance.json)).
- [18 October 2026: runtime case execution and fixture notes](runtime/case-cleanup-2026-10-18.md)
  ([provenance](runtime/case-cleanup-2026-10-18.provenance.json)).
- [18 October 2026: state/cache storage and lowering notes](language/state-cache-cleanup-2026-10-18.md)
  ([provenance](language/state-cache-cleanup-2026-10-18.provenance.json)).
- [18 October 2026: pull-source and scheduler implementation notes](language/pull-source-cleanup-2026-10-18.md)
  ([provenance](language/pull-source-cleanup-2026-10-18.provenance.json)).
- [18 October 2026: runtime and wiring implementation evidence](runtime-evidence-cleanup-2026-10-18.md)
  ([provenance](runtime-evidence-cleanup-2026-10-18.provenance.json)).
- [18 October 2026: source-language contracts and target mappings](source-contract-cleanup-2026-10-18.md)
  ([provenance](source-contract-cleanup-2026-10-18.provenance.json)).
- [18 October 2026: native-binding contracts and implementation evidence](native-binding-cleanup-2026-10-18.md)
  ([provenance](native-binding-cleanup-2026-10-18.provenance.json)).
- [18 October 2026: expected observations and historical corrections](expectation-history-cleanup-2026-10-18.md)
  ([provenance](expectation-history-cleanup-2026-10-18.provenance.json)).
- [18 October 2026: remaining implementation references in contract prose](final-editorial-cleanup-2026-10-18.md)
  ([provenance](final-editorial-cleanup-2026-10-18.provenance.json)).
- [18 October 2026: specification authority and extraction history](specification-authority-2026-10-18.md)
  ([provenance](specification-authority-2026-10-18.provenance.json)).
