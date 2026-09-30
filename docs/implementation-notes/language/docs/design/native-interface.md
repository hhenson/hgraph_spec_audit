# Relocated notes: language/docs/design/native-interface.md

Source: [specification before separation](https://github.com/hhenson/hgraph_spec/blob/766033278bef6e9403cc99c0d8f318ba46a03919/language/docs/design/native-interface.md).

These excerpts preserve earlier implementation notes and their surrounding
context. They were not revalidated during relocation and do not assert current
support or define language behavior. The current specification owns the rules.
HGL source examples remain in the linked specification revision.

## Excerpt 1

> Status: accepted boundary; descriptor validation, native declaration metadata,
> canonical fingerprints, the lifecycle ABI, explicit descriptor authoring,
> source-defined inline C++ value/view functions, exact canonical-value,
> overloaded collection-input-view, and payload-erased input-view evaluation
> calls in AOT modules implemented; opaque state and external scripted dependency
> loading remain

## Excerpt 2

> The agreed replacement authoring model is [ADR 0014](https://github.com/hhenson/hgraph_spec/blob/766033278bef6e9403cc99c0d8f318ba46a03919/language/docs/design/decisions/0014-native-implementation-interfaces.md):
> shared declarations, generated C++ adapters/Rust traits and implementations in
> native source. `native` preserves ordinary temporal and `const` typing. The
> inline value/view forms below describe the legacy implementation during migration.

## Excerpt 3

> HGL is intentionally not a general-purpose language. Native C++ is nevertheless
> necessary for efficient algorithms, stateful resources, and capabilities that
> cannot be implemented as graph composition. This record defines two deliberate
> boundaries: a small top-level source form for exact C++ value/view functions,
> and versioned descriptors for separately built libraries. C and other
> implementation languages remain future descriptor providers; the implemented
> source escape is C++ only.

## Excerpt 4

> The subsequent agreed direction is recorded in
> [ADR 0008](https://github.com/hhenson/hgraph_spec/blob/766033278bef6e9403cc99c0d8f318ba46a03919/language/docs/design/decisions/0008-temporal-contracts-and-target-mappings.md): value-level
> `const fn`, reconstructible node-local cache, native type lifecycles, and
> semantic contracts separated from target-specific mappings. Those extensions
> are not implemented. The source examples and C++ descriptors below describe
> the existing native-function interface, not a new generalized mapping syntax.

## Excerpt 5

> An HGL module may define a top-level exact native function and name the headers
> required by its C++ projection:

## Excerpt 6

> [Native example 1](https://github.com/hhenson/hgraph_spec_audit/blob/main/examples/documentation/language/docs/design/native-interface.md#example-1)

## Excerpt 7

> The outer HGL signature is authoritative for name resolution, generic
> selection, constraints, parameter access, result type, and the generated module
> descriptor. A temporal collection parameter is passed as its live typed hgraph
> input view; an ordinary scalar temporal parameter is passed as its current C++
> value. The input-only `signal` marker instead passes
> `const hgraph::TSInputView &`. It is a payload-erased endpoint pattern which
> accepts atomic values, structs, collections, windows, references, and
> payload-free signals without exposing their payload type to HGL. The contextual
> `schema` type is narrower still: it may appear only as a non-`const` native
> parameter and projects to `const hgraph::TSValueTypeMetaData *`. Runtime pack
> code obtains such a borrowed handle through `schemas(pack)`. It is the metadata
> already owned by the child endpoint, not a new HGL value, and cannot be returned
> or retained.

## Excerpt 8

> Passing a `signal` native argument is an endpoint inspection, not a payload
> read: it need not be dominated by `valid`. The native helper must tolerate an
> invalid or unbound endpoint, or check it before accessing a payload. Native
> input-view arguments still must be runtime input parameters, not arbitrary
> indexed/field expressions. Ordinary scalar and typed collection native
> arguments retain the existing validity checks. A native call does not itself
> establish HGL flow-sensitive validity for subsequent payload reads.

## Excerpt 9

> The `cpp(...)` list states the exact C++ parameter declarations received by the
> body. The compiler supplies the function name and C++ result type, adds
> `noexcept` unless `throws` is declared, then emits a plain function in the generated module's `native` namespace.
> Same-named HGL candidates use distinct generated symbols: the first keeps the
> short name and later candidates use `__candidate_N`. This is necessary because
> two distinct HGL patterns can intentionally project to the same erased C++
> view type, such as fixed and unbounded lists.

## Excerpt 10

> The source form is deliberately top-level. It cannot occur inside a graph or
> node body, so it cannot introduce new wiring. A call is a direct C++ call on
> current values or views. A native whose parameters are all values is
> available in every node hook (`start`, `when`, `stop`), which is how a node
> validates its configuration in `start` as the native library does; a native
> that takes a live input view is evaluation-only, because lifecycle blocks
> have no inputs. The descriptor records the phases accordingly. A native declaration is automatically public because a
> downstream module must be able to import it, and declarations with the same
> name form one HGL overload family. Source-native `requires` clauses are rejected
> until the version-one descriptor catalog can reconstruct them; the compiler
> must not publish a contract it cannot enforce on import. Parameter defaults are
> rejected because descriptor format v1 has no native-default contract.

## Excerpt 11

> HGL balances the C++ parameter list and compound statement while respecting
> C++ comments, quoted literals, escapes, and raw string literals. It does not
> implement a second C++ parser. The native compiler validates the projected C++
> declarations and body. The generated header and source are run through the same
> embedded `clang-format` policy as all other emitted code, so the escape remains
> readable in review.

## Excerpt 12

> `cpp include <header>` and `cpp include "header"` accept literal system and
> project header names. The compiler retains their delimiter form, deduplicates
> after the first occurrence, and emits them before native declarations in the
> generated header. They are local to the defining source module and do not
> propagate through HGL imports. Macro, computed, and conditional includes are
> rejected; CMake supplies header search paths and linked targets.

## Excerpt 13

> A native function whose body may raise says so with `throws` after its
> signature ([ADR 0009](https://github.com/hhenson/hgraph_spec/blob/766033278bef6e9403cc99c0d8f318ba46a03919/language/docs/design/decisions/0009-native-errors-and-the-node-error-model.md)):

## Excerpt 14

> [Native example 2](https://github.com/hhenson/hgraph_spec_audit/blob/main/examples/documentation/language/docs/design/native-interface.md#example-2)

## Excerpt 15

> The generated function then has no exception specification and the descriptor
> records the `translated` policy. A raise ends the evaluation under hgraph's
> node error model; HGL has no exception surface of its own. Without `throws`
> the function is emitted `noexcept`.

## Excerpt 16

> There is currently no general HGL spelling for a link dependency, effect,
> state type, lifecycle phase, or ownership annotation. The `schema` parameter's
> immutable call-confined borrow is fixed by that type; separately built
> libraries use descriptors for all other ownership concerns. A future source
> feature must define those contracts before widening this form.

## Excerpt 17

> This decision is recorded in
> [ADR 0005](https://github.com/hhenson/hgraph_spec/blob/766033278bef6e9403cc99c0d8f318ba46a03919/language/docs/design/decisions/0005-inline-cpp-native-functions.md) and, for `throws`,
> [ADR 0009](https://github.com/hhenson/hgraph_spec/blob/766033278bef6e9403cc99c0d8f318ba46a03919/language/docs/design/decisions/0009-native-errors-and-the-node-error-model.md).

## Excerpt 18

> The first shipped use of this form is
> [`hgraph.native`](https://github.com/hhenson/hgraph/blob/main/language/stdlib/hgl/hgraph/native.hgl). Its compiled
> `hgl::core_native` target provides `len` and `is_empty` for strings and typed
> collection views, tick-window metadata, and string queries. It also provides
> payload-erased `valid`, `all_valid`, `modified`,
> `last_modified`, `bound`, and `active` functions over every standard time-series
> shape. The module is split into explicit source parts, keeping one import and
> descriptor identity. The parts, generated library, header, and descriptor are
> installed together and exercised by an isolated SDK consumer.

## Excerpt 19

> - canonical HGL module and declaration identity;
> - declaration category: hgraph operator, exact native value function, native
>   constructor, or lifecycle operation;
> - complete HGL parameter and result types, including generic collection-view
>   patterns used only for overload selection and the complete input-only
>   `signal` pattern used for payload-erased endpoint calls;
> - permitted phases: wiring, start, evaluation, or stop;
> - observable effects, including mutation, I/O, blocking, and allocation where
>   relevant;
> - value, owned, shared, or borrowed ownership and any dependent lifetime;
> - whether a parameter receives its current scalar value or its live typed input
>   view;
> - exception and thread-safety policy;
> - canonical C++ symbol or generated wrapper identity;
> - required public headers, CMake packages, imported targets, and runtime image;
> - module lifecycle entry points, provider identity, compatibility versions, and
>   descriptor fingerprint.

## Excerpt 20

> The serialized representation is the canonical, versioned JSON selected in
> [ADR 0004](https://github.com/hhenson/hgraph/blob/main/language/docs/design/decisions/0004-json-module-descriptors.md). The current compiler
> emits its envelope, public/provider inventories, structured HGL signatures,
> struct layouts, defaults, canonical types and constraints, and generated build
> metadata. `hgl check` reads and validates one such descriptor without loading a
> library or consulting a registry. Native declarations now encode exact C++
> symbols, permitted phases, effects, parameter/result ownership and dependent
> lifetimes, exception policy, thread-safety policy, opaque or atomic native type
> associations, runtime images, and lifecycle ABI metadata. The reader enforces
> the non-blocking evaluation envelope, declared exception policy, explicit mutable state,
> borrow rules, and lifecycle consistency. The compiler can build an explicit
> module catalog from one or more descriptors, resolve a selective or aliased
> `use`, select an exact overload from canonical scalar or collection types,
> carry that candidate through HIR and HGraph IR, and emit its reviewed
> `cpp_symbol` as a direct call. A source `native fn` produces the same descriptor
> record using its generated exact symbol. The AOT CMake helper obtains
> descriptors from directly linked targets. Locked transitive dependency closure
> and external-package resolution for the scripted loader remain to be added.
> Native `requires` clauses also remain blocked until the catalog can reconstruct
> their constraint arena.

## Excerpt 21

> An exact native function is callable only in phases allowed by its descriptor.
> A value parameter receives the current canonical scalar payload. A collection
> `input-view` parameter receives the corresponding live `TSL`, `TSS`, `TSD`, or
> rolling input view. A complete `signal` parameter with `input-view` access
> receives the common `TSInputView` base instead. This permits constant-time
> metadata operations and erased current-value behavior without materializing a
> collection or switching on its runtime kind. Construction or cleanup of private
> native state is the next stateful slice.

## Excerpt 22

> The installed `hgraph.native` module exposes this common endpoint surface:

## Excerpt 23

> | Native function | Erased hgraph operation | HGL result |
> | --- | --- | --- |
> | `valid(value)` | `TSInputView::valid()` | `bool` |
> | `all_valid(value)` | `TSInputView::all_valid()` | `bool` |
> | `modified(value)` | `TSInputView::modified()` | `bool` |
> | `last_modified(value)` | `TSInputView::last_modified_time()` | `datetime` |
> | `bound(value)` | `TSInputView::bound()` | `bool` |
> | `active(value)` | `TSInputView::active()` | `bool` |

## Excerpt 24

> The one declaration for each operation covers `TS<T>` for every canonical or
> registered atomic value, nominal `TSB`, fixed and unbounded `TSL`, `TSS`,
> `TSD`, tick- and duration-based `TSW`, `REF`, and `SIGNAL`. That coverage comes
> from hgraph's existing `SIGNAL` input compatibility and common view contract;
> the implementation does not enumerate or branch over those types.

## Excerpt 25

> Representation erasure belongs behind the implementation boundary. HGL uses
> ordinary value expressions and `delta_value` for every supported shape, not
> separate erased-value accessors. The remaining implementation gaps are:

## Excerpt 26

> See the [native surface completion record](https://github.com/hhenson/hgraph_spec/blob/766033278bef6e9403cc99c0d8f318ba46a03919/language/docs/design/native-surface-proposal.md) for
> accepted collection accessors, implemented coverage and remaining decisions. In particular, the existing
> TSL/TSS/TSD input patterns do not imply native access to atomic List/Set/Map
> values; their signature and borrowing contracts must be supported explicitly.

## Excerpt 27

> Runtime pack schema inspection is the deliberately narrow exception. A
> source-native helper accepts one borrowed `schema` parameter, and generated C++
> passes the current child input's existing metadata pointer directly. The
> descriptor records the parameter as runtime metadata with borrowed immutable
> ownership. This does not expose a constructible, storable, or returnable schema
> value through the general native ABI.

## Excerpt 28

> Calls from wiring-time constant evaluation, automatic temporal lifting, and
> general compile-time execution are outside the first interface. Although the
> phase metadata can describe wiring, start, evaluation, and stop, the compiler
> accepts a call only in a phase named by the descriptor and the implemented
> canonical-value and collection-view slices are exercised in evaluation.

## Excerpt 29

> The generated node accepts any standard time-series shape, while the C++ helper
> receives only `const hgraph::TSInputView &`. HGL still cannot inspect the
> payload of `value`; the native declaration exposes one reviewed operation on
> that erased endpoint.

## Excerpt 30

> The installed `hgl::native_package` C++ API is the first producer. A small
> build-time executable owned by the native package fills an
> `hgl::native::Package` and calls `write_descriptor`. The authoring model can
> name canonical scalars, nominal native types declared by that same package,
> generic collection input-view patterns, and a complete payload-erased signal
> input-view pattern. It sorts set-like inventories and
> declarations, creates the shared descriptor schema records, seals the result,
> and runs the same validator used by `hgl check` before writing anything.

## Excerpt 31

> For example, this describes a non-throwing scalar operation:

## Excerpt 32

> [Native example 4](https://github.com/hhenson/hgraph_spec_audit/blob/main/examples/documentation/language/docs/design/native-interface.md#example-4)

## Excerpt 33

> The named `cpp_symbol` must already be an exact directly callable public C++
> symbol. Multiple descriptor declarations may name the same C++ overload family
> and HGL identity when their HGL signatures differ. If a template, throwing
> function, or ownership-heavy API needs normalization, the package supplies a
> small reviewed wrapper and names that wrapper. Automatic wrapper emission is a
> remaining Stage F slice; the authoring API does not parse headers or accept
> arbitrary C++ declarations.

## Excerpt 34

> For example, an erased list-view overload is described as:

## Excerpt 35

> [Native example 5](https://github.com/hhenson/hgraph_spec_audit/blob/main/examples/documentation/language/docs/design/native-interface.md#example-5)

## Excerpt 36

> The named C++ overload accepts `const hgraph::TSLInputView &` (or the view by
> value) and returns `hgraph::Int`. Parallel declarations for `set<T>` and
> `map<K, V>` form the same HGL overload family.

## Excerpt 37

> An erased endpoint declaration uses `ValueType::signal()` and must select
> `ParameterAccess::InputView`:

## Excerpt 38

> [Native example 6](https://github.com/hhenson/hgraph_spec_audit/blob/main/examples/documentation/language/docs/design/native-interface.md#example-6)

## Excerpt 39

> For AOT compilation, place the descriptor path on the native dependency
> target's `HGL_MODULE_DESCRIPTORS` property and link that target from the HGL
> module. `hgl_add_module()` passes those descriptors to every HGL compilation
> and links the target that supplies the public header and symbol:

## Excerpt 40

> ```cmake
> set_property(TARGET acme_stats PROPERTY
>     HGL_MODULE_DESCRIPTORS "${acme_stats_descriptor}")
>
> hgl_add_module(my_hgl_nodes STATIC
>     HGL smooth.hgl
>     LINK_LIBRARIES acme_stats)
> ```

## Excerpt 41

> This bootstrap follows direct CMake target edges only. It does not yet compute
> the locked transitive descriptor closure or teach `hgl test`, `hgl run`, and
> the REPL how to resolve arbitrary external CMake packages and runtime images.

## Excerpt 42

> An optional Clang-based binding generator may later derive the same artifact
> from annotated public headers. Clang is then a descriptor-generation tool, not
> part of HGL parsing or the definition of which arbitrary C++ constructs the
> language accepts. The generated descriptor remains reviewable and versioned.

## Excerpt 43

> The descriptor participates in the existing closed package universe. Its
> provider initializes transactionally, installs all registrations through one
> module-owned handle, and deinitializes in reverse dependency order. Graphs,
> plans, native call targets, and metadata retain provider leases.

## Excerpt 44

> The installed, C-compatible `hgl/native_module_abi.h` defines version one of
> the dynamic lifecycle boundary. A provider exports the fixed
> `hgl_query_native_module_v1` symbol. The host requests ABI version one and
> validates the returned immutable table before activation. The table contains
> its byte size, canonical module identity, descriptor fingerprint, opaque
> module-owned context, and `init`, `deinit`, and `is_active` callbacks. An ABI
> error record is host-allocated and has a fixed capacity; callbacks return a
> status code and must not let exceptions cross the boundary.

## Excerpt 45

> The module, rather than the host loader, owns the hgraph provider handle and
> all registration state behind the opaque context. Initialization and
> deinitialization are idempotent. The scripted compiler bootstrap implements
> this contract and catches registration/removal failures through hgraph's common
> exception-boundary helper. The host validates the ABI version, table size,
> identity, required callbacks, and exact descriptor fingerprint before it
> retains the image and invokes lifecycle callbacks.

## Excerpt 46

> Descriptors are sealed with `sha256:` followed by the lowercase digest of their
> canonical version-one semantic model with the fingerprint field empty. Input
> whitespace and object ordering therefore do not affect identity. Compatible
> unknown version-one members remain outside that projection; a security-relevant
> semantic addition requires a format-version increment. The generated bootstrap
> embeds the fingerprint, and the loader rejects an image whose module identity or
> fingerprint differs before invoking `init`.

## Excerpt 47

> Calls within generated code may still use direct C++ types and functions when
> the descriptor permits them. Logical provider removal and native-image
> unloading are distinct: the first implementation deinitializes registrations
> but deliberately keeps loaded images resident for process lifetime.

## Excerpt 48

> - descriptor-only `hgl check` without loading its library;
> - one canonical scalar value function used inside a runtime node in an AOT
>   module;
> - one owned opaque state value constructed at startup, mutated during
>   evaluation, and destroyed after stop;
> - rejection of the same calls in an unpermitted phase;
> - rejection of a borrowed value that escapes;
> - generated C++ that is a direct, readable call through public headers;
> - a source `native fn` emitted as a formatted plain C++ function, exported in
>   the module descriptor, imported by another HGL module, and executed through
>   generated C++;
> - scripted and ahead-of-time execution with identical ticks once external
>   dependency resolution is implemented;
> - descriptor/provider fingerprint mismatch before graph wiring;
> - failed activation rollback and provider removal without stale registrations;
> - an installed-SDK consumer build, not only an in-tree test.
