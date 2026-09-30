# Relocated notes: language/docs/user-guide/modules-and-tools.md

Source: [specification before separation](https://github.com/hhenson/hgraph_spec/blob/766033278bef6e9403cc99c0d8f318ba46a03919/language/docs/user-guide/modules-and-tools.md).

These excerpts preserve earlier implementation notes and their surrounding
context. They were not revalidated during relocation and do not assert current
support or define language behavior. The current specification owns the rules.
HGL source examples remain in the linked specification revision.

## Excerpt 1

> Writing a `native fn` with a C++ body is extension-authoring work. See
> [Native modules and packages](https://github.com/hhenson/hgraph/blob/main/language/docs/developer-guide/native-modules-and-packages.md#writing-a-small-native-c-helper).

## Excerpt 2

> Descriptor-backed imported implementations work for the catalog's supported
> scalar, collection and signal signatures, including ordinary type and constant
> generics. Contract constraints, properties, defaults, packs and unsupported
> nominal shapes currently produce an explicit import diagnostic. Constraints on
> the implementation itself still use the ordinary `requires` rules.

## Excerpt 3

> The implemented command surface is:

## Excerpt 4

> ```text
> hgl check path/to/program.hgl [--module-descriptor <file>]...
>         [--part <file>]...
>         [--dump-tokens] [--dump-ast] [--dump-hir] [--dump-hgraph-ir]
> hgl test path/to/program.hgl [--part <file>]...
>         [--module-descriptor <file>]... [test-name]...
> hgl run path/to/program.hgl [--part <file>]... [--entry name] [--mode sim|realtime]
>         [--start <datetime>] [--end <datetime|duration>]
>         [--set name=<constant expression>]...
>         [--module-descriptor <file>]...
> hgl emit-cpp path/to/program.hgl [--part <file>]...
>         [--out-dir <dir> | --include-dir <dir> --src-dir <dir>]
>         [--python <file.py> --python-native <module>] [--print]
>         [--print-namespace]
>         [--module-descriptor <file>]...
> hgl repl [--module-descriptor <file>]...
> ```

## Excerpt 5

> | Command | Behavior |
> | --- | --- |
> | `check` | Check syntax, names, types, and supported semantic rules without executing the program |
> | `test` | Run the module's `test` declarations and report failing assertions |
> | `run` | Bind an entry to a mode, clock, and parameters, then execute it |
> | `emit-cpp` | Write `program.h`, `program.cpp`, and `program.hgl-module.json` in the module's namespace |
> | `repl` | Accumulate declarations, run tests and `eval` forms interactively |

## Excerpt 6

> [Testing and running](https://github.com/hhenson/hgraph_spec/blob/766033278bef6e9403cc99c0d8f318ba46a03919/language/docs/user-guide/testing-and-running.md) shows `test`, `run`, and the
> run configuration file from the author's side.

## Excerpt 7

> The current `hgl` implements `--help`, `--version`, `check`, `test`, `run`
> (without `--config`), `emit-cpp`, and `repl` over the `hgraph.std` and
> `hgraph.analytics` kernels. File-based `test` and `run` compile/load the
> supported scalar runtime-node subset through a native cache on Unix; the REPL
> uses the same route when its session contains runtime declarations. `test`
> accepts test names after the file to run a selection.
> Compiler debugging flags are described in the
> [developer guide](https://github.com/hhenson/hgraph/blob/main/language/docs/developer-guide/compiler-and-lowering.md).
> The first-pass limits are listed in
> [Testing and running](https://github.com/hhenson/hgraph_spec/blob/766033278bef6e9403cc99c0d8f318ba46a03919/language/docs/user-guide/testing-and-running.md#first-pass-limits); the
> constructs `emit-cpp` does not yet lower are listed under
> [Building a package](https://github.com/hhenson/hgraph_spec/blob/766033278bef6e9403cc99c0d8f318ba46a03919/language/docs/user-guide/modules-and-tools.md#building-a-package).

## Excerpt 8

> Use `hgl emit-cpp prices.hgl --out-dir build/generated` to generate a module
> for a native build. The build needs the hgraph SDK, a C++ compiler, and
> `clang-format`. Configure `HGL_CLANG_FORMAT` if the formatter is not on `PATH`.

## Excerpt 9

> For reusable libraries or Python packages, use `hgl_add_module()` in CMake.
> The [package-authoring guide](https://github.com/hhenson/hgraph/blob/main/language/docs/developer-guide/native-modules-and-packages.md#building-a-package)
> covers dependencies, public exports, installation, and Python wrappers. There
> is no separate `hgl build` command.

## Excerpt 10

> Composition-only programs can run directly with `hgl test`, `hgl run`, and the
> REPL. Programs containing runtime functions, value functions, or operator
> implementations also need a C++ toolchain and `clang-format`. Scripted native
> execution is supported on Unix; on Windows, build a native package instead.

## Excerpt 11

> The same language rules apply to scripted and packaged programs. Some imported
> native dependencies need an explicit package build; supplying a descriptor
> alone does not install or load an external dependency. See the
> [package-authoring guide](https://github.com/hhenson/hgraph/blob/main/language/docs/developer-guide/native-modules-and-packages.md).

## Excerpt 12

> The REPL keeps the last working session if a new declaration fails to check,
> compile, or activate. A failed native build reports the directory containing
> its diagnostics. Useful environment settings are:

## Excerpt 13

> | Variable | Purpose |
> | --- | --- |
> | `HGL_CXX` | Select the native compiler |
> | `HGL_CLANG_FORMAT` | Select the required formatter |
> | `HGL_ARTIFACT_DIR` | Choose where failed and temporary builds are retained |
> | `HGL_CACHE_DIR` | Choose the compilation cache directory |
> | `HGL_DISABLE_CACHE=1` | Compile without reusing the cache |
> | `HGL_CACHE_TRACE=1` | Report cache decisions for troubleshooting |

## Excerpt 14

> External input comes from imported facilities or test sequences. The REPL does
> not provide a separate adaptor language.
