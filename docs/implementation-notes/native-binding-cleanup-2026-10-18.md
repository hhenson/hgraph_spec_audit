# Native-binding contracts and implementation evidence: notes relocated on 18 October 2026

Historical implementation material removed from the specification. These excerpts
were not revalidated and do not assert current support or define the standard.
Required behavior and open semantic decisions remain in the specification.

Source revision: `54e252dfb4d0bfe740349fcca2f8b24753beb01f`. The [provenance manifest](native-binding-cleanup-2026-10-18.provenance.json)
records source hashes, excerpt locations and original text. Relative links in
excerpts resolve to that specification revision.

## language/docs/design/decisions/0014-native-implementation-interfaces.md

### Excerpt 1

[Source, line 8](https://github.com/hhenson/hgraph_spec/blob/54e252dfb4d0bfe740349fcca2f8b24753beb01f/language/docs/design/decisions/0014-native-implementation-interfaces.md#L8).

> body, header, crate path or symbol map. C++ and Rust implement the same contract
> in ordinary source files. Native-library builds own their dependencies.

### Excerpt 2

[Source, line 41](https://github.com/hhenson/hgraph_spec/blob/54e252dfb4d0bfe740349fcca2f8b24753beb01f/language/docs/design/decisions/0014-native-implementation-interfaces.md#L41).

> The compiler generates the implementation interface. A C++ library supplies a
> class with static members and binds it through the generated `bind<T>()`:
>
> [Native example 1](https://github.com/hhenson/hgraph_spec_audit/blob/main/examples/documentation/language/docs/design/decisions/0014-native-implementation-interfaces.md#example-1)
>
> The corresponding Rust library implements the generated trait:
>
> Rust implements the corresponding contract through its native binding interface.
>
> Both may delegate to existing native functions. Generated checks include the
> resolved parameter/result types, temporal role and declared failure contract. C++
> implicit conversions cannot satisfy a mismatched signature.

### Excerpt 3

[Source, line 87](https://github.com/hhenson/hgraph_spec/blob/54e252dfb4d0bfe740349fcca2f8b24753beb01f/language/docs/design/decisions/0014-native-implementation-interfaces.md#L87).

> The compiler checks these contracts; temporal execution still needs its provider
> ABI. Value helpers support logger/clock in C++ and logger in Rust traits.

### Excerpt 4

[Source, line 99](https://github.com/hhenson/hgraph_spec/blob/54e252dfb4d0bfe740349fcca2f8b24753beb01f/language/docs/design/decisions/0014-native-implementation-interfaces.md#L99).

> implementation part owns injectable requests and lifecycle hooks. C++ may
> request `out, logger` while Rust requests only `out`; each generated interface
> uses its selected requirements.

### Excerpt 5

[Source, line 133](https://github.com/hhenson/hgraph_spec/blob/54e252dfb4d0bfe740349fcca2f8b24753beb01f/language/docs/design/decisions/0014-native-implementation-interfaces.md#L133).

> Illustrative target signatures for the declarations above (not existing APIs):
>
> [Native example 3](https://github.com/hhenson/hgraph_spec_audit/blob/main/examples/documentation/language/docs/design/decisions/0014-native-implementation-interfaces.md#example-3)
>
> Rust implements the corresponding contract through its native binding interface.
>
> C++ `bind<Implementation>()` and the Rust trait check their target's generated
> signatures. The examples show implementations requesting both capabilities;
> neither requires all targets to use that same parameter list. The selected
> implementation part supplies the target requirements.
> The first implementation publishes through `out`; its native `void`/unit result
> does not remove the HGL temporal result. The second returns a scalar string.
> The adapter for temporal implementations returning a complete value, and the
> full lifecycle ABI, remain separate implementation work.

### Excerpt 6

[Source, line 171](https://github.com/hhenson/hgraph_spec/blob/54e252dfb4d0bfe740349fcca2f8b24753beb01f/language/docs/design/decisions/0014-native-implementation-interfaces.md#L171).

> Acceptance expectations. Value-helper inference, imports, logger forwarding,
> clock reads and ordinary/native call checks have executable coverage. Temporal
> provider output and borrowed-output cases remain pending. Target-specific
> requests, graph/node shape and lifecycle metadata have compiler coverage.

### Excerpt 7

[Source, line 185](https://github.com/hhenson/hgraph_spec/blob/54e252dfb4d0bfe740349fcca2f8b24753beb01f/language/docs/design/decisions/0014-native-implementation-interfaces.md#L185).

> | C++ uses `out, logger`; Rust uses only `out` |

### Excerpt 8

[Source, line 195](https://github.com/hhenson/hgraph_spec/blob/54e252dfb4d0bfe740349fcca2f8b24753beb01f/language/docs/design/decisions/0014-native-implementation-interfaces.md#L195).

> Language diagnostics have no Python/C++ runtime oracle. For runtime cases,
> record values, ticks, effects and owner identity against reasoned, Python and
> C++ results before implementing bindings. Accept two-way agreement with a
> variation report; if Python and C++ agree against reasoning, revisit reasoning.
> Escalate three-way disagreement. The [helper reference traces](https://github.com/hhenson/hgl/blob/codex/native-interface-bindings/docs/compiler/capabilities/README.md)
> agree across reasoning, Python and C++ for duplicate/idle ticks, helper call
> counts and evaluation-clock reads. Compiler diagnostics are validated separately.

### Excerpt 9

[Source, line 206](https://github.com/hhenson/hgraph_spec/blob/54e252dfb4d0bfe740349fcca2f8b24753beb01f/language/docs/design/decisions/0014-native-implementation-interfaces.md#L206).

> once. Native imports stay in C++/Rust source; dependencies stay in that library's
> ordinary CMake/Cargo build.

### Excerpt 10

[Source, line 218](https://github.com/hhenson/hgraph_spec/blob/54e252dfb4d0bfe740349fcca2f8b24753beb01f/language/docs/design/decisions/0014-native-implementation-interfaces.md#L218).

> | Value `bit_and(6, 3)` | `2` in C++ and Rust |

### Excerpt 11

[Source, line 234](https://github.com/hhenson/hgraph_spec/blob/54e252dfb4d0bfe740349fcca2f8b24753beb01f/language/docs/design/decisions/0014-native-implementation-interfaces.md#L234).

> Record reasoned results before execution. Preserve existing scalar operator
> traces against Python and C++; this migration must not change their ticks.

## language/docs/design/node-authoring.md

### Excerpt 1

[Source, line 25](https://github.com/hhenson/hgraph_spec/blob/54e252dfb4d0bfe740349fcca2f8b24753beb01f/language/docs/design/node-authoring.md#L25).

> - **NAT-2:** Generate the implementation interface from the HGL contract. C++
>   uses a checked `bind<T>()` adapter; Rust implements a generated trait. Keep
>   implementations in native source and dependencies in its normal library build.

## language/docs/design/native-interfaces.md

### Excerpt 1

[Source, line 38](https://github.com/hhenson/hgraph_spec/blob/54e252dfb4d0bfe740349fcca2f8b24753beb01f/language/docs/design/native-interfaces.md#L38).

> Acceptance: preserve the reasoned/Python/C++/Rust bitwise traces in

### Excerpt 2

[Source, line 74](https://github.com/hhenson/hgraph_spec/blob/54e252dfb4d0bfe740349fcca2f8b24753beb01f/language/docs/design/native-interfaces.md#L74).

> C++ and Rust parts may request different services.

### Excerpt 3

[Source, line 82](https://github.com/hhenson/hgraph_spec/blob/54e252dfb4d0bfe740349fcca2f8b24753beb01f/language/docs/design/native-interfaces.md#L82).

> Native constructors/destructors and Rust `Drop` do not replace start/stop.

## language/docs/design/native-implementation-parts.md

### Excerpt 1

[Source, line 50](https://github.com/hhenson/hgraph_spec/blob/54e252dfb4d0bfe740349fcca2f8b24753beb01f/language/docs/design/native-implementation-parts.md#L50).

>   scopes. Hooks are not C++ constructors/destructors or Rust `Drop`.

### Excerpt 2

[Source, line 56](https://github.com/hhenson/hgraph_spec/blob/54e252dfb4d0bfe740349fcca2f8b24753beb01f/language/docs/design/native-implementation-parts.md#L56).

> These are compiler contracts, not new tick semantics. The existing matching
> reasoned/Python/C++ helper and clock traces remain the runtime oracle.

### Excerpt 3

[Source, line 66](https://github.com/hhenson/hgraph_spec/blob/54e252dfb4d0bfe740349fcca2f8b24753beb01f/language/docs/design/native-implementation-parts.md#L66).

> | Select C++ logger part or Rust empty part |

## language/docs/design/native-interface.md

### Excerpt 1

[Source, line 142](https://github.com/hhenson/hgraph_spec/blob/54e252dfb4d0bfe740349fcca2f8b24753beb01f/language/docs/design/native-interface.md#L142).

> candidate before HGraph IR lowering.

### Excerpt 2

[Source, line 146](https://github.com/hhenson/hgraph_spec/blob/54e252dfb4d0bfe740349fcca2f8b24753beb01f/language/docs/design/native-interface.md#L146).

> The generated C++ calls the declared symbol, its package-provided wrapper, or a
> source-native generated function directly. It never subclasses an operator to
> represent an exact helper. The direct-wiring backend does not emulate native
> C++: a runtime-bearing program follows the existing generated, compiled, and
> loaded image path.

### Excerpt 3

[Source, line 231](https://github.com/hhenson/hgraph_spec/blob/54e252dfb4d0bfe740349fcca2f8b24753beb01f/language/docs/design/native-interface.md#L231).

> A small helper owned by an HGL module can be implemented directly. The HGL
> signature remains the public contract and the C++ projection states the exact
> native ABI used by the generated call:
>
> [Native example 3](https://github.com/hhenson/hgraph_spec_audit/blob/main/examples/documentation/language/docs/design/native-interface.md#example-3)
>
> For a separately built native package, an imported descriptor supplies the
> same call-site contract.

### Excerpt 4

[Source, line 269](https://github.com/hhenson/hgraph_spec/blob/54e252dfb4d0bfe740349fcca2f8b24753beb01f/language/docs/design/native-interface.md#L269).

> value: the selected C++ overload reads `value.size()` from the live input view.

## language/docs/design/native-surface-proposal.md

### Excerpt 1

[Source, line 137](https://github.com/hhenson/hgraph_spec/blob/54e252dfb4d0bfe740349fcca2f8b24753beb01f/language/docs/design/native-surface-proposal.md#L137).

>   predicates; preserve existing C++ semantics and flag genuinely undecided
>   names or policies separately.

## language/docs/design/const-debug-bootstrap.md

### Excerpt 1

[Source, line 6](https://github.com/hhenson/hgraph_spec/blob/54e252dfb4d0bfe740349fcca2f8b24753beb01f/language/docs/design/const-debug-bootstrap.md#L6).

> The graph connects `const_(42)` to `debug_print`. `const` is a reserved word, so
> the authored source uses `const_`.

### Excerpt 2

[Source, line 12](https://github.com/hhenson/hgraph_spec/blob/54e252dfb4d0bfe740349fcca2f8b24753beb01f/language/docs/design/const-debug-bootstrap.md#L12).

> `hgraph` supplies the C++ part and provider; `hgl` supplies its own Rust pair.
> Only the shared HGL source is mirrored between them.

### Excerpt 3

[Source, line 26](https://github.com/hhenson/hgraph_spec/blob/54e252dfb4d0bfe740349fcca2f8b24753beb01f/language/docs/design/const-debug-bootstrap.md#L26).

> | Source with bare `when` | No modified inputs, so no publication even if scheduled |

### Excerpt 4

[Source, line 30](https://github.com/hhenson/hgraph_spec/blob/54e252dfb4d0bfe740349fcca2f8b24753beb01f/language/docs/design/const-debug-bootstrap.md#L30).

> Validate the source and generated C++ on hgraph first. Then compile the same
> HGL with the Rust compiler and run emitted nodes and graph construction on the
> Rust engine. Compare ticks and effects, not generated names or output handles.
> Python and C++ operator comparisons cover the source and sink behaviour;
> reference debug-print prefixes are excluded from the integer-payload comparison.
> The bootstrap itself prints only the integer and a newline.
