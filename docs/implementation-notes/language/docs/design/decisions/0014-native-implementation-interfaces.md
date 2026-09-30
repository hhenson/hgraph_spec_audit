# Relocated notes: language/docs/design/decisions/0014-native-implementation-interfaces.md

Source: [specification before separation](https://github.com/hhenson/hgraph_spec/blob/766033278bef6e9403cc99c0d8f318ba46a03919/language/docs/design/decisions/0014-native-implementation-interfaces.md).

These excerpts preserve earlier implementation notes and their surrounding
context. They were not revalidated during relocation and do not assert current
support or define language behavior. The current specification owns the rules.
HGL source examples remain in the linked specification revision.

## Excerpt 1

> Status: accepted authoring model; migration in progress.

## Excerpt 2

> These are language capability types, not payloads to temporalize. Their public
> type spelling and target wrappers remain to be implemented. `out` designates
> the existing result, never an additional output. An outputless function cannot
> request it. For nested collections, its shape is the complete result schema.
> Existing validity, delta and write-order rules still apply.

## Excerpt 3

> Concrete scalar `native const fn` declarations compile through source-owned
> C++ providers, including overload and exception checks. `hgl_add_module` takes
> `NATIVE_PROVIDER_HEADER` and `NATIVE_PROVIDER` once per library; the C++ header
> owns `bind<T>()`, member implementations and its includes. These are library
> entry points, not per-function mappings. Installed sources include the provider.
> The generated public C++ scalar wrappers retain their existing const-reference
> ABI; provider methods use values for bool/i64/f64 and const references for other
> scalars. `const` in that C++ spelling does not change HGL temporal roles.
> Native value calls lift over time-series arguments through the same runtime
> node policy as ordinary `const fn`, including imported calls. Descriptor format
> 8 records `value`, `temporal`, or `legacy-value` plus required capabilities;
> hooks do not determine role. Capabilities propagate transitively through value
> calls and imported native declarations, without duplicate injection requests.
> `legacy-value` is a migration detail, not an agreed language function kind;
> the separate native checking paths must converge on the common contract above.
> Legacy inline `native fn` is rejected inside `const fn`: value helpers must
> state `native const fn`. Calendar/duration helpers now use the scalar provider.
> Scripted `test` accepts the corresponding `--native-provider-header` and
> `--native-provider` options. Its cache is bypassed until provider-header
> transitive dependencies can be fingerprinted.

## Excerpt 4

> The 56 scalar substrate implementations live in `stdlib/cpp/native_scalar.h`.
> `native/scalar_values_i64.hgl` is a shared declaration part used by both target
> implementations. `emit-native-rust <file> --part <implementation> --out <file>` generates a checked Rust
> trait for concrete bool/i64/f64 value declarations, including a call-borrowed
> logger. C++ value providers also admit the evaluation clock. Target-specific requests come from the selected implementation part. Rust overloads, generics, clock injection,
> fallible contracts and other scalar mappings are rejected until implemented.

## Excerpt 5

> New temporal declarations retain their source role but cannot use this scalar
> provider ABI. The temporal provider ABI and explicit collection-borrow spelling
> remain outstanding. Existing inline view helpers retain their legacy behaviour
> while that migration is pending; they are not examples of the new typing rules.
