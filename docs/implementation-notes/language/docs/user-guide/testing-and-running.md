# Relocated notes: language/docs/user-guide/testing-and-running.md

Source: [specification before separation](https://github.com/hhenson/hgraph_spec/blob/766033278bef6e9403cc99c0d8f318ba46a03919/language/docs/user-guide/testing-and-running.md).

These excerpts preserve earlier implementation notes and their surrounding
context. They were not revalidated during relocation and do not assert current
support or define language behavior. The current specification owns the rules.
HGL source examples remain in the linked specification revision.

## Excerpt 1

> Status: `test`, `assert`, and `eval` over dense sequences, `hgl run` from the
> command line, and the REPL are implemented; every example on this page runs
> as written unless it is labelled provisional. Timed sequences and the TOML
> run configuration are provisional: their agreed form is shown in labelled
> snippets that the current `hgl` rejects. The specification is
> [Tests and the evaluation harness](https://github.com/hhenson/hgraph_spec/blob/766033278bef6e9403cc99c0d8f318ba46a03919/language/docs/developer-guide/syntax-and-semantics.md#tests-and-the-evaluation-harness)
> and [Running a module](https://github.com/hhenson/hgraph_spec/blob/766033278bef6e9403cc99c0d8f318ba46a03919/language/docs/developer-guide/syntax-and-semantics.md#running-a-module);
> the [roadmap status matrix](https://github.com/hhenson/hgraph/blob/main/language/docs/design/roadmap.md#feature-status-matrix-2026-09-07)
> records the status of each form.

## Excerpt 2

> The implemented context contains private `fn` and `const fn` declarations and
> named `test` cases. Put assertions inside a named case, not directly in the
> context. Nested contexts, test-local types, imports, native declarations, and
> operator implementations are not supported in this first slice.

## Excerpt 3

> > **Provisional.** Timed sequences parse, but the harness does not run them
> > (`timed sequences are not supported by the first pass; write one value per
> > cycle`), and `eval` does not yet accept a `rolling` parameter. The agreed
> > form is recorded here so that dense tests are not written in a shape that
> > will change.

## Excerpt 4

> > **Provisional: configuration file.** The agreed `--config run.toml` form
> > mirrors the command line, with command-line options overriding the file.
> > The current `hgl run` does not read it, so this is not runnable today:
> >
> > ```toml
> > [run]
> > entry = "heartbeat"
> > mode = "realtime"
> > start = 2026-09-03T08:00:00Z
> > end = "1d"
> >
> > [run.params]
> > every = "1500ms"
> > ```
> >
> > TOML values would bind by their type: integer to `i64`, float to `f64`,
> > string to `str` or, for a temporal parameter, the HGL literal spelling such
> > as `"1d"`, offset date-time to `datetime`, local date to `date`, array to
> > `list`.

## Excerpt 5

> The current `hgl` runs every example on this page that is not labelled
> provisional. The limits, each reported by name:

## Excerpt 6

> - `eval` drives scalar and `atomic` parameters; a structural tuple, list,
>   set, map, or rolling parameter is reported as unsupported;
> - timed sequences are reported as unsupported; write one value per cycle;
> - `eval` takes a module `fn`; wrap an operator in a `fn` to evaluate it;
> - `hgl run` takes its configuration from the command line only; the
>   `--config` file is not read;
> - file-based `test` and `run`, and the REPL, compile supported runtime
>   functions and generic `impl fn` candidates on Unix only; an unresolved
>   generic composition call is still outside the direct-wiring path, while the
>   generated backend supports the concrete generic operator and window forms
>   used by the examples;
> - complete scalar struct values, type-only generic struct specializations,
>   `atomic<S>` harness values, and simple field-wise temporal struct
>   construction run; generic constructor inference, `const` generic struct
>   identity, multiple inheritance, temporal structured deltas, and explicit
>   optional-field clearing are reported as unsupported;
> - a `for` statement inside a `test` body is reported as unavailable;
> - types in diagnostics are printed with hgraph's names (`float`,
>   `TS[float]`, `Tuple[float,float]`).

## Excerpt 7

> The [roadmap status matrix](https://github.com/hhenson/hgraph/blob/main/language/docs/design/roadmap.md#feature-status-matrix-2026-09-07)
> is the complete list.

## Excerpt 8

> Composition-only programs can run directly. Programs with runtime functions,
> value functions, or operator implementations need a native toolchain for
> scripted execution, which is currently supported on Unix. Windows supports
> building such programs as native packages. The test-context example above
> contains a runtime helper and therefore needs that toolchain.

## Excerpt 9

> A failed native build reports a directory containing its diagnostics. The REPL
> keeps the previous working declarations if a replacement fails. See
> [Execution requirements](https://github.com/hhenson/hgraph_spec/blob/766033278bef6e9403cc99c0d8f318ba46a03919/language/docs/user-guide/modules-and-tools.md#execution-requirements) for tool
> and cache settings, and the [developer guide](https://github.com/hhenson/hgraph/blob/main/language/docs/developer-guide/native-modules-and-packages.md#one-execution-model)
> for compiler and loader internals.
