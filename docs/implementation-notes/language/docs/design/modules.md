# Relocated notes: language/docs/design/modules.md

Source: [specification before separation](https://github.com/hhenson/hgraph_spec/blob/766033278bef6e9403cc99c0d8f318ba46a03919/language/docs/design/modules.md).

These excerpts preserve earlier implementation notes and their surrounding
context. They were not revalidated during relocation and do not assert current
support or define language behavior. The current specification owns the rules.
HGL source examples remain in the linked specification revision.

## Excerpt 1

> Status: accepted module boundary; canonical versioned JSON descriptor implemented

## Excerpt 2

> - canonical language module name and version;
> - compatible hgraph SDK and descriptor-format versions;
> - automatically public nominal operator contracts, explicitly exported exact
>   functions, and exported concrete and abstract struct declarations;
> - operator implementation candidates, including explicit generic
>   materializations with any retained resolver parameters, indexed by canonical operator identity,
>   provider module, implementation kind, and generic signature;
> - canonical types, schema declarations, generic struct-family parameters and
>   constraints, and abstract-family relationships;
> - the C++ headers required by generated code;
> - CMake package names and imported targets;
> - explicit module initialization, registry installation, deinitialization, and
>   registration-removal entry points;
> - optional documentation and source links for diagnostics and tooling.

## Excerpt 3

> The descriptor contains declarations and build metadata, not executable user
> code. Its serialization is canonical, versioned JSON with descriptor-local
> type, constant-expression, and constraint arenas. It is reviewable and can be
> validated before native code is loaded; see
> [ADR 0004](https://github.com/hhenson/hgraph/blob/main/language/docs/design/decisions/0004-json-module-descriptors.md).

## Excerpt 4

> Scalar-dependent `requires` predicates are serialized as declarative constraint
> records rather than hidden callbacks. Imported operator checking must pass
> those records to hgraph's shared resolver without approximation. Imported operators with supported signatures can be implemented and
> materialized across modules. Reconstructing imported contract constraints is
> still unsupported and diagnosed by the catalog; arbitrary resolver helpers
> running outside the compiler process are not an escape hatch.

## Excerpt 5

> Every file in an assembled set names the same module and a unique part. The
> part name is file-local ownership metadata used for deterministic compilation;
> it is not a namespace, export, provider, or registration identity. All files
> share one declaration and import scope, one descriptor, and one generated C++
> namespace. Private declarations may be referenced across parts, and duplicate
> declarations are checked across the set. Imports still precede ordinary
> declarations within each physical file and never become re-exports.

## Excerpt 6

> The CLI and CMake target list parts explicitly. The compiler neither scans a
> directory nor infers a missing file. The complete decision, including source
> mapping and artifact naming, is [ADR 0006](https://github.com/hhenson/hgraph_spec/blob/766033278bef6e9403cc99c0d8f318ba46a03919/language/docs/design/decisions/0006-multi-file-module-parts.md).

## Excerpt 7

> Explicit materialization supports local and selectively imported contracts.
> The descriptor carries the external C++ marker, nominal identity, and signature;
> those identities survive HIR and hgraph IR into generated registration.
> Unsupported imported constraints, properties, generic packs, and type shapes
> fail during checking. `tests/codegen/imported-operators/` covers concrete and
> generic providers compiled separately from their contract module.

## Excerpt 8

> The semantic IR records the canonical operator identity on every implementation
> candidate and operator call. It never reconstructs that identity later from a
> short string. A descriptor for a native package maps the canonical language
> identity to its public C++ contract alias and registration hook. Source-defined
> operators receive deterministic generated contract identities.

## Excerpt 9

> Explicit load and unload logic is in scope from the first native slice rather
> than deferred to REPL work. hgraph already relies on module load and unload
> logic to expose native modules to Python, operator-overload registration has to
> be evaluated for hand-written C++ modules as well as generated ones, and
> deterministic teardown is needed for orderly process shutdown and for unit
> tests that install and remove modules within one process. Running scripts in a
> child process does not cover any of those.

## Excerpt 10

> Scripted native-module compilation emits a module descriptor and the
> version-one, C-compatible lifecycle ABI specified by
> `hgl/native_module_abi.h`. Its fixed query function returns a module-owned
> context and `init`, `deinit`, and `is_active` callbacks. The AOT
> `hgl emit-cpp` / `hgl_add_module()` path currently emits the descriptor and an
> explicit `register_operators()` entry point, but not this dynamic lifecycle
> query ABI; the linked application owns that registration lifetime. Extending
> the same generated lifecycle boundary to AOT packages remains compiler work.
> The scripted lifecycle has three separate responsibilities:

## Excerpt 11

> `init` and `deinit` are compiler-generated for scripted HGL modules, not
> source-level blocks. A native extension may provide reviewed resource hooks
> through the same ABI. Registry installation remains replayable after reset and
> must not repeat unrelated one-time initialization side effects.

## Excerpt 12

> Deactivation, deinitialization, and native-library unloading are distinct. A
> wired graph or cached plan that selects module code holds a provider lease.
> Deinitialization must wait or fail while such a lease is live, and unloading is
> permitted only after all code and metadata references are gone. The initial
> implementation may perform logical registration removal while retaining the
> library image for process lifetime.

## Excerpt 13

> The hgraph operator registry now supports keyed replayable installers,
> provider-scoped candidate and installer removal, failed-installer rollback, and
> leases retained by graph plans and instances. Generated operator-only modules
> now return that provider handle, and the scripted/REPL loader uses it for
> logical deactivation and transactional replacement while retaining native
> images for process lifetime. The language still requires a first-class
> module-registration transaction spanning the other owned surfaces (types,
> exact functions, associations, and native resources); it must not erase
> registry internals or privately compose several unrelated handles itself.

## Excerpt 14

> Push adaptors, services, and external-resource sinks are implemented in C++.
> Their module declarations expose typed function contracts, but language source
> cannot provide callbacks, queue storage, thread ownership, or arbitrary
> lifecycle hooks to them.

## Excerpt 15

> The C++ compiler is built in hgraph; the Rust compiler is built in hgl.
> This repository contains their shared contracts and examples, not a build
> project. See [hgraph build setup](https://github.com/hhenson/hgraph/blob/main/language/docs/developer-guide/shared-sources.md)
> for the pinned source dependencies and compiler build context.
