# Contextual local bindings: C++ baseline evidence

The [shared rule](../../spec/language/docs/design/contextual-local-bindings.md)
fixes each local's canonical type and ordinary/connection category at
initialization. `let` forbids reassignment; `var` permits compatible replacement
in the same category. Connection rebinding preserves earlier uses and aliases.
Node execution locals are ordinary values. These expectations come from the
owner's language decision, not from the compiler's current behavior.

The [shared cases](../../spec/compiler/contextual_bindings/cases.json) own all
HGL inputs and expectations, pinned at spec commit
`d72e0c4e0abbdda49e1a7682dc98c09703993d8e`. The focused C++ run on
2026-10-04 records 20 cases in [cpp.json](cpp.json), with eight mismatches:

| Cases | Expected | Observed |
|---|---|---|
| `scalar_to_port`, `port_to_scalar` | Type rejection | Accepted |
| `uninitialized_scalar_to_port` | Type rejection after the first ordinary assignment | Accepted |
| `conditional_initial_scalar_change`, `conditional_initial_port_change` | Type rejection | Accepted |
| `node_atomic_composite` | Type rejection for an atomic composite ordinary local annotation | Accepted |
| `unused_category_change`, `conditional_unused_scalar_write` | Type rejection even if the assignment is unused | Backend rejection because the local is never read; does not establish the required type check |
| `let_scalar_reassign`, `let_port_reassign` | Reject reassignment | Rejected as immutable |
| `scalar_type_change`, `port_type_change` | Reject incompatible replacement | Rejected: `str`, expected `i64` |
| `graph_scalar_local`, `node_scalar_local` | Accept; trace `[4, 5]` | Both tests passed |
| `wire_rebind` | Accept; earlier alias preserved; trace `[13, 24]` | Test passed |
| `graph_compound`, `ordinary_widening` | Accept and run their shared assertions | Both tests passed |
| `uninitialized_scalar` | Accept ordinary definite assignment and run its shared assertion | Test passed |
| `conditional_uninitialized_result`, `conditional_repeated_result` | Accept the existing conditional-result construction | Accepted; no runtime assertion in these cases |

The node-local IR is retained in the report: references to `local` have
`phase=runtime kind=runtime-value`, with canonical scalar `i64`. The six
executed tests passed. The other observations are compiler admission and
diagnostic checks, not runtime measurements. No compiler was changed.

## Reference boundary

Python authoring uses Python name binding while constructing graphs; Python's
ability to bind a name first to a scalar and then to a port cannot establish an
HGL static type rule. Python-authored runtime observations may establish value
or wiring behavior, but do not test HGL `let`, `var`, canonical type fixation,
or compiler rejection. This campaign makes no Python or Rust conformance claim.

The existing C++ executable reports
`hgl 0.8.31-36-gdb55ea2c2 (hgraph api 0.8.0)` and has SHA256
`4328aee54fcde8b6a65ec42b03657e1ec912fcdd628e7f2271887fcc0010923e`.
It was reused without rebuilding. The associated source archive manifest was
independently checked against hgraph commit
`52c343031bef46035b4e8cbfbfe4b64ed8a427d3`, including pinned recursive
submodules: all 3,132 file hashes matched. The manifest SHA256 is
`a6606b6939fc6421d98fec283fa1ad128c18cfd438bb0bfd8b9ad2fce7614e93`;
the source archive SHA256 is
`0306a9338824572133620930f4955f91309d8fb2ec0a1198cb80fbcc5b49ff61`.
The embedded version comes from the earlier configure step. The runner records
the executable fingerprint; it does not independently certify the binary's
build chain or rebuild that source revision.

## Reproduce

```sh
git submodule update --init --recursive
python3 compiler/contextual_bindings/observe.py --hgl <cpp-hgl-executable> \
  --output results/local-contextual-bindings.json
python3 compiler/contextual_bindings/check.py
```

The observation command writes all results and exits 1 on any mismatch. An
expected rejection must exit 1 and contain the shared diagnostic marker when
specified; crashes and incidental backend errors do not count as type-rule
conformance. The recorded check verifies unchanged shared inputs and harness,
the eight documented variations, and successful assertions. It makes no fresh
compiler measurement. This bounded audit is not whole-language conformance.
