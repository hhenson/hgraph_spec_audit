# Relocated notes: language/docs/design/native-interfaces.md

Source: [specification before separation](https://github.com/hhenson/hgraph_spec/blob/766033278bef6e9403cc99c0d8f318ba46a03919/language/docs/design/native-interfaces.md).

These excerpts preserve earlier implementation notes and their surrounding
context. They were not revalidated during relocation and do not assert current
support or define language behavior. The current specification owns the rules.
HGL source examples remain in the linked specification revision.

## Excerpt 1

> Status: agreed model; scalar bindings implemented with upstream ADR 0014.

## Excerpt 2

> The HGL declaration owns typing, temporal role, borrowing, effects and errors.
> hgraph owns C++ implementation parts and providers; hgl owns Rust parts and
> providers. Share HGL contracts across repositories and select one implementation.
> Implementations live in ordinary native source. Generate a C++
> `bind<Implementation>()` adapter and a Rust implementation trait from that
> contract. Native-library builds own dependency configuration; do not author a
> second per-function symbol manifest.

## Excerpt 3

> C++ implements the generated interface with a static member and `bind<T>()`;
> Rust implements its generated trait. Both implement `lhs & rhs`. The temporal
> `hgraph.operators.bit_and` node retains its input handles, activation and output
> publication and calls this value helper during evaluation.

## Excerpt 4

> C++ value adapters support logger/clock; generated Rust traits support logger.
> The compiler preserves temporal graph/node shape and hooks. Their execution ABI
> and explicit borrowed-TS helper spelling remain pending; backends reject those
> contracts instead of emitting scalar calls.

## Excerpt 5

> The upstream [implementation-part rules and acceptance cases](https://github.com/hhenson/hgraph/blob/codex/native-implementation-parts/language/docs/design/native-implementation-parts.md)
> cover matching, selection, ownership and lifecycle diagnostics. Existing
> [value-helper traces](https://github.com/hhenson/hgraph_spec_audit/blob/main/compiler/capabilities/README.md) remain the reasoned/Python/C++
> oracle. Rust generated-trait tests prove binding shape and borrowing, not
> compiler-generated node-context execution.

## Excerpt 6

> The upstream compiler's `emit-native-rust` command generates
> `crates/hgl-native/src/scalar_interface.rs` from the shared
> `crates/hgl-native/interfaces/scalar.hgl` declaration and selected
> `scalar-impl.hgl` requirements. Only the shared declaration tracks upstream;
> the Rust implementation part is maintained here.
> `StandardNative` implements that trait; the existing node calls it through `bit_and_i64`. No symbol manifest or
> third-party dependency is introduced.

## Excerpt 7

> ```sh
> python tools/native_bindings.py --compiler <hgl> --interface <upstream-interface> --implementation crates/hgl-native/interfaces/scalar-impl.hgl
> python tools/native_bindings.py --compiler <hgl> --check
> cargo xtask ci
> ```

## Excerpt 8

> CI builds the upstream compiler at the revision pinned in `ci.yml` and checks
> the vendored declaration against upstream and generates the Rust trait using
> the local implementation part. Supply interface and implementation paths together;
> they need not share a repository. Update the pin and regenerate together when
> changing the shared contract.

## Excerpt 9

> C++ supports concrete scalar value interfaces, overloads and `throws`; 56 core
> scalar helpers now use the generated adapter. Rust trait emission currently
> supports concrete bool/i64/f64 declarations without overloads or `throws` and
> rejects unsupported contracts. Temporal native interfaces are recognized but
> cannot use this scalar ABI; their provider ABI and the collection-view
> migration remain outstanding. Existing inline view helpers retain their legacy
> behaviour until that migration is settled.
