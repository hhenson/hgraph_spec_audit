# Relocated notes: language/docs/developer-guide/syntax-and-semantics.md

Source: [specification before separation](https://github.com/hhenson/hgraph_spec/blob/766033278bef6e9403cc99c0d8f318ba46a03919/language/docs/developer-guide/syntax-and-semantics.md).

These excerpts preserve earlier implementation notes and their surrounding
context. They were not revalidated during relocation and do not assert current
support or define language behavior. The current specification owns the rules.
HGL source examples remain in the linked specification revision.

## Excerpt 1

> Status: the grammar, generic constraints, structured-value syntax, and the
> phase-neutral iteration rule below are implemented through the parser, typed
> HIR, and both backends for the forms the
> [roadmap status matrix](https://github.com/hhenson/hgraph/blob/main/language/docs/design/roadmap.md#feature-status-matrix-2026-09-07)
> marks implemented; runtime-function semantics are partial; the `enum`,
> `switch`, and `str(value)` extensions are provisional and not parsed. The EBNF
> is descriptive: where it admits a form the compiler rejects,
> the surrounding prose names the boundary.

## Excerpt 2

> `const fn` identifies non-temporal value functions; parameter-level `const`
> retains its wiring-time meaning. Local fixed-arity functions and
> [role selection/lifting](https://github.com/hhenson/hgraph_spec/blob/766033278bef6e9403cc99c0d8f318ba46a03919/language/docs/user-guide/value-functions.md) are implemented.
> Generic/pack value-function lowering is not implemented. Scalar `cache`
> declarations are implemented, including beside `state`.
> Native type lifecycle forms and target-mapping declarations remain outside
> the implemented grammar. Their agreed semantics and open syntax are recorded
> in [ADR 0008](https://github.com/hhenson/hgraph_spec/blob/766033278bef6e9403cc99c0d8f318ba46a03919/language/docs/design/decisions/0008-temporal-contracts-and-target-mappings.md).

## Excerpt 3

> A `string_character` is any UTF-8 character other than `"`, `\`, and a line
> break; an unterminated string and an unknown escape are `parse` diagnostics.
> An integer literal must fit `i64` and a float literal `f64`; otherwise the
> lexer reports the literal as out of range. There is no signed literal token
> (`-1` is unary minus applied to `1`) and no source spelling for a non-finite
> float, although a folded wiring-time `f64` product may overflow to one
> (`tests/codegen/parity.hgl` does this deliberately; the descriptor format
> tags such payloads, see ADR 0004). An exponent belongs to the number only
> when no unit follows it, so `1e5` is a float literal and `1e5m` an invalid
> duration run. `temporal_literal` and `duration_literal` are defined under
> "Temporal scalar types".

## Excerpt 4

> The hard reserved words are those in the keyword table of
> `src/syntax/token.cpp`:

## Excerpt 5

> Parameter packs have three explicit forms. `values: ...T` is a homogeneous
> positional pack and unifies every captured value with `T`; `values: ...Ts`
> with `...Ts` declared in the generic list is a heterogeneous positional pack;
> and `values: ...{Fields}` with `...Fields` declared is a heterogeneous named
> pack. A type-pack generic is not a singular source type. Packs cannot be
> `const`, have defaults, or be followed by fixed parameters in the implemented
> slice. `{n}`, `{n:*}`, and `{n:m}` respectively enforce exact, minimum, and
> inclusive bounded arity during call normalization and native candidate
> registration. `requires each T in types(Ts) { ... }` introduces a lexical type
> binding and evaluates its body as a compile-time conjunction over the selected
> type sequence; an empty sequence is true, and forwarded premises compare
> modulo the local binding name. The syntax, binding rules, traversal views,
> native selector mapping, and remaining reflection boundary are fixed by
> [ADR 0007](https://github.com/hhenson/hgraph_spec/blob/766033278bef6e9403cc99c0d8f318ba46a03919/language/docs/design/decisions/0007-parameter-packs.md).

## Excerpt 6

> A `native fn` is automatically public and contains exactly one C++ projection.
> Its HGL signature uses the ordinary grammar, but its parameters cannot have
> defaults. An optional `throws` after the signature declares that the body may
> raise; the generated function then has no `noexcept` and the descriptor
> records the `translated` policy. `throws` is a contextual keyword, like
> `native`, and cannot be used as a name. A raise ends the evaluation under
> hgraph's node error model
> ([ADR 0009](https://github.com/hhenson/hgraph_spec/blob/766033278bef6e9403cc99c0d8f318ba46a03919/language/docs/design/decisions/0009-native-errors-and-the-node-error-model.md)). The grammar recognizes an optional `requires` clause so the syntax
> tree remains future-compatible; semantic analysis currently rejects it because
> descriptor constraints cannot yet be reconstructed on import. The lexer
> retains the balanced C++ parameter list and compound statement verbatim,
> accounting for C++ comments, quoted literals, and raw strings. HGL does not
> parse their contents. The form is top-level; a value native is callable in
> `start`, `when`, and `stop`, a view native only in `when`; it cannot
> appear inside another function body.

## Excerpt 7

> A `cpp include` is module-level build metadata for source-defined C++ only.
> The header must be a literal `<...>` or `"..."` name; macro, computed, and
> conditional preprocessor forms are rejected. Delimiter form and first
> declaration order are retained, duplicate declarations are removed, and the
> include is emitted before generated native declarations. It is not exported or
> propagated by an HGL `use`. Header search paths and linked libraries remain
> properties of the surrounding CMake target.

## Excerpt 8

> A cycle that also runs through inheritance, such as a parent's field that
> names its own descendant, is rejected too: hgraph declares a parent before its
> children, so such a cycle cannot be registered. A struct type may name another
> module's struct (ADR 0013), but a recursive EDGE may not: rule 5 keeps an edge
> inside the module that owns it, and module imports are acyclic, so no cycle
> crosses a module. The resolver marks each admitted edge on the struct's effective
> fields, and typed HIR and hgraph IR carry the mark with the edge's target
> named by struct identity (compiler and lowering guide, "Recursive struct
> edges"). Both backends realize an edge as an owner of its target, and module
> descriptor format 6 marks each edge in an exported struct's layout (roadmap,
> "Feature status matrix").

## Excerpt 9

> `signal` is a contextual, payload-erased input marker. It is legal only as the
> complete type of a non-`const` function or operator parameter; results,
> structure fields, nested uses, `const` parameters, and defaults are rejected
> semantically. It accepts any concrete temporal input, materializes as the
> native `hgraph::SIGNAL` schema, and has no scalar value type. The spelling is
> lowercase in HGL; uppercase `SIGNAL` is not an HGL type.

## Excerpt 10

> The compiler infers the use from the typed body; `instantiate` does not add a
> second annotation for it. Marker-only fixed-list sizes lower directly to
> `hgraph::SIZE<"name">` and have no runtime field. Reading a retained generic as
> a value requires an explicit reification mechanism and currently fails with a
> targeted `emit-cpp` diagnostic. Binding that same generic concretely remains
> valid. This prevents an implementation detail such as per-tick schema
> inspection from being introduced as an accidental language rule.

## Excerpt 11

> The current implementation accepts only a locally declared operator contract.
> Although ordinary `impl fn` binding also admits a selectively imported
> operator, materializing that case requires descriptor-backed external contract
> metadata and currently produces a module diagnostic. This is a staged compiler
> boundary, not a different long-term visibility rule.

## Excerpt 12

> A `let` or `var` binding that nothing reads is a diagnostic: it is dead code,
> and the generated C++ must not carry a variable the language did not need
> (`hgraph_ir::binding_uses` decides; a compound assignment reads its target, a
> plain `=` does not).

## Excerpt 13

> The agreed
> [conditional-result design](https://github.com/hhenson/hgraph_spec/blob/766033278bef6e9403cc99c0d8f318ba46a03919/language/docs/design/control-flow.md#results-used-after-the-conditional)
> uses typed, uninitialized declarations such as
> `var r: i64`. The declaration introduces the enclosing variable; branch
> assignments supply its output connection, and lowering remaps the binding
> after the switch. Count any used expression result alongside the escaping
> bindings: one result is returned directly; several are returned through a
> compiler-generated bundle. The grammar and semantic passes implement the
> declaration and definite-assignment portions. Both backends implement the
> single-result case and the structural-bundle multiple-result case. Expression
> and assignment results may share that bundle, and a branch may forward an
> existing binding through a reference-qualified generated input. No default
> value or runtime state cell is implied.

## Excerpt 14

> The final statement of a block is its tail expression when it is an
> expression. `if` is a primary expression, so it is an operand only when
> parenthesized (`(if c { 1 } else { 2 }) + 1`); as a statement its value is
> discarded. A bare `{ ... }` in expression position is a block expression.
> The parser accepts `if` uniformly. Its meaning depends on context: a
> wiring-time Boolean chooses composition, a temporal Boolean in composition
> uses the agreed native switch strategy, and a runtime-node condition is an
> ordinary current-value conditional. See
> [Conditional control flow](https://github.com/hhenson/hgraph_spec/blob/766033278bef6e9403cc99c0d8f318ba46a03919/language/docs/design/control-flow.md). The temporal composition
> case is implemented in both backends for a two-branch value result and for an
> outputless sink switch with an optional block `else`. A discarded conditional
> is checked without the enclosing function's expected result, so sink operators
> remain outputless inside a value-producing graph. A consumed temporal
> conditional without `else` instead gets a typed native `nothing` false branch.
> The `"else", if_expression` alternative of the grammar is the `else if`
> chain. It is implemented for a wiring-time condition (`else if mode == 1 {
> ... }` in a `const`-driven conditional). Temporal `else if` is retained in
> the IR but rejected by both backends until nested branch lowering exists
> (`backend: temporal 'else if' is not supported in this compiler stage; use a
> block 'else'`); it is never rewritten as an omitted false branch.
> Continuation forms remain implementation limits rather than unresolved
> choices of strategy.

## Excerpt 15

> Under the agreed temporal composition design, `return` targets the enclosing
> HGL function, not a compiler-generated branch lambda. Lowering must identify
> early-return paths and place the remaining function body in the non-returning
> path's continuation before deriving branch captures and result signatures.
> The continuation's computations share that branch's lifetime. Definite
> assignment considers only paths reaching a use, excluding paths that return
> before it. See [Early returns](https://github.com/hhenson/hgraph_spec/blob/766033278bef6e9403cc99c0d8f318ba46a03919/language/docs/design/control-flow.md#early-returns-and-continuations).
> Shared HGraph IR plans this behavior as ordered lexical continuation segments.
> Both backends execute those paths for top-level and nested direct temporal
> conditional statements and block tails. A temporal conditional embedded in
> another expression form remains staged.

## Excerpt 16

> An outputless temporal conditional uses the native sink-switch path without a
> synthetic output. Sinks inside the branch are wired through the switch; sinks
> outside it remain unconditionally wired. The graph body still describes
> wiring, and the sink nodes perform runtime effects. Result and escape analysis
> determines whether a switch is outputless, independently of the enclosing
> function's return annotation. See
> [Outputless conditionals](https://github.com/hhenson/hgraph_spec/blob/766033278bef6e9403cc99c0d8f318ba46a03919/language/docs/design/control-flow.md#outputless-conditionals).
> Both compiler backends implement this form, including a synthetic empty false
> branch when `else` is omitted.

## Excerpt 17

> The agreed source form is `switch selector { case value: ... default: ... }`.
> This is a target extension to `statement`, not an implemented production in
> the parser described above. Each label ends with `:` and its body continues
> until the next case/default label or closing switch brace. Statements retain
> their existing newline rules. The [worked examples](https://github.com/hhenson/hgraph/blob/main/language/docs/developer-guide/control-flow-cpp-mappings.md)
> show complete HGL functions before their C++ mappings.

## Excerpt 18

> An enum is a distinct atomic scalar type, not an integer alias. Preserve that
> identity in equality and switch checking; an assigned number or a member of
> another enum is not an interchangeable case label. Integer conversion is
> explicit and uses a type-name call like string conversion; its exact source
> spelling remains to be confirmed. Enumeration exposes member-name strings
> through `keys`, assigned integers through `values`, and typed enum instances
> through `elements`. All three views iterate in declaration order, never
> numeric or alphabetical order. The enum-type calls are `keys(Mode)`,
> `values(Mode)`, and `elements(Mode)`. For an enum with `N` members they return
> immutable scalar `list<str, N>`, `list<i64, N>`, and `list<Mode, N>` values,
> respectively. Resolve the argument as an enum type and preserve its nominal
> identity and declared member count. These are ordinary constant values that
> may be bound, indexed, reused, or iterated during wiring, not temporal ports
> or `RuntimeIterator` values. Their meaning does not become a borrowed runtime
> traversal inside a node. This does not introduce a general type-constructor
> surface or new dynamic-loop lowering.
> [Paired HGL/C++ examples](https://github.com/hhenson/hgraph/blob/main/language/docs/developer-guide/enum-cpp-mappings.md) cover declarations, numbering,
> string conversion, checked construction through `Mode(...)`, and
> declaration-order scalar-list enumeration. Enum declarations remain a target
> grammar extension, not implemented parser support.

## Excerpt 19

> `default:` catches unmatched selector values; an explicitly empty body is
> allowed. No match without a default must fail, including for outputless
> switches; do not manufacture an empty branch. Case bodies do not implicitly
> fall through to each other and require no source `break`. For an enum selector,
> covering all declared members establishes exhaustiveness without requiring a
> default. Partial coverage is permitted and retains the same no-match rule.
> Even exhaustive dispatch must retain its failure path. Coverage does not replace
> definite-assignment checks on branches reaching a later use. Apply these checks
> in node and graph forms; see [enum switch examples](https://github.com/hhenson/hgraph/blob/main/language/docs/developer-guide/enum-switch-cpp-mappings.md).
> Exact selector-type admission, native enum mapping, and an expression-value
> surface remain separate design work. No parser or backend support is implemented by this
> design update. Recognition of the new `switch`, `case`, and `default` tokens
> must be added to the parser alongside the statement extension.

## Excerpt 20

> A call whose callee resolves to an enum type is a checked conversion from one
> integer or string operand, such as `Mode(10)` or `Mode("first")`. Resolve the
> callee to the nominal enum identity, then look up an assigned number or exact
> case-sensitive member name. Do not apply struct named-field construction rules
> or erase the result to its backing integer. Unknown numbers and names are
> errors: constants during checking, scalar configuration during wiring, and
> runtime values during evaluation. A temporal graph operand requires a wired
> checked conversion, not a wiring-time payload read. The existing validity,
> REF, and SIGNAL restrictions apply. A conversion error is not a no-match
> switch key and does not activate `default`. This is agreed target behavior,
> not implemented compiler support; see
> [enum conversion](https://github.com/hhenson/hgraph_spec/blob/766033278bef6e9403cc99c0d8f318ba46a03919/language/docs/design/type-extensions.md#constructing-an-enum-from-a-number-or-name).

## Excerpt 21

> The calls are parsed as ordinary call expressions. The grammar above records
> their checked intrinsic shapes rather than adding special parser nodes.
> Under the agreed phase-dependent design, these calls no longer force the
> containing function to be a `RuntimeFn`. This section describes their runtime
> interpretation: the iterator must be consumed directly by `for`; it is neither
> a canonical value nor a temporal port and cannot escape the current
> evaluation. In graph composition, a supported wiring-time iterable provides
> scalar values and a fixed temporal structure provides child connections. The
> compiler implements `elements` and `items` over a fixed TSL by statically
> unrolling the body and projecting children through hgraph's public
> `tsl_element` contract. Independent `values`/`items` bodies over a TSD and
> `elements`/`items` bodies over an unbounded TSL lower through hgraph's
> per-key/per-index sink mapping in both backends; temporal captures become
> explicit broadcast child inputs. The
> current subset rejects predicates, graph-phase `keys`, scalar captures,
> assignments to enclosing variables, and loop returns. Unordered map reduction
> and ordered, linear list reduction are deferred options, not initial lowering
> support. See
> [Iteration](https://github.com/hhenson/hgraph_spec/blob/766033278bef6e9403cc99c0d8f318ba46a03919/language/docs/design/iteration.md) for the target design and current boundary.

## Excerpt 22

> The implemented classifier (`src/semantics/resolve.cpp`, `classify`) applies
> these rules to temporal `fn` bodies. A `const fn` remains value-level when it
> injects an admitted service; required capabilities also propagate through calls:

## Excerpt 23

> This section describes implemented HGL. The agreed
> [native capability contract](https://github.com/hhenson/hgraph_spec/blob/766033278bef6e9403cc99c0d8f318ba46a03919/language/docs/design/decisions/0014-native-implementation-interfaces.md#outputs-and-capabilities)
> also supports `logger` and `clock` on value functions and native value
> declarations. Calls silently upgrade their callers' injection lists. Injection
> alone does not classify a `const fn` as a node. Temporal native provider
> bindings remain pending.

## Excerpt 24

> An `inject` declaration requests compiler-approved runtime selectors without
> adding parameters to the callable contract: `out`, `logger`, `clock`,
> `scheduler` and, once ADR 0015 is implemented, `alarm`. Each generated hook
> requests only the selectors it uses. Unknown capabilities and use from an
> unsupported phase are diagnostics. `out` is a
> special injectable inferred from the result type; it is invalid on an
> outputless function and is initially available only during evaluation, not in
> `start` or `stop`. The clock and scheduler methods, the `scheduled()` handler
> selector, and the `passivate`/`activate` statements are fixed by
> [ADR 0010](https://github.com/hhenson/hgraph_spec/blob/766033278bef6e9403cc99c0d8f318ba46a03919/language/docs/design/decisions/0010-lifecycle-capabilities.md); `scheduled`,
> `passivate` and `activate` are intrinsic names. A runtime function without
> temporal parameters must inject `scheduler` or `alarm`, or be a generator
> (`yield`). `alarm` is the stateless one-shot scheduler
> ([ADR 0015](https://github.com/hhenson/hgraph_spec/blob/766033278bef6e9403cc99c0d8f318ba46a03919/language/docs/design/decisions/0015-pull-sources.md)): `alarm.schedule(delay)`
> and `alarm.schedule_at(time)`, earliest request wins, nothing recorded or
> recovered, admitted in sources only.

## Excerpt 25

> `test`, `assert`, and `eval` are hard reserved words. `_` on its own is the
> placeholder token rather than an identifier; identifiers may still begin
> with an underscore. A `test` block sees its module's scope, including
> unexported functions, so tests live beside the code they cover; a test in
> another module sees only that module's public interface. Test names are
> unique within a module. A `test` body is a composition-phase block plus
> `assert` statements: `state`, `inject`, lifecycle, and `when` forms are
> `phase` diagnostics there, and so, in the current compiler, is `for`
> (`'for' is not available in a test body`), although the classifier treats
> iteration as phase-neutral. Test declarations never lower into the module's
> artifact; `hgl test` discovers and runs them, and `hgl emit-cpp` omits them
> from the generated package (there is no `hgl build`; a package is built by
> `hgl_add_module()`).

## Excerpt 26

> TOML integers, floats, strings, booleans, offset date-times, local dates,
> local times, local date-times, and arrays bind to `i64`, `f64`, `str`,
> `bool`, `datetime`, `date`, `time`, `civil_datetime`, and `list` parameters;
> a string binds to any temporal parameter type through the HGL literal
> spelling (`"1d"`, `"09:30[America/New_York]"`). Defaults are hgraph's
> `run_graph` defaults: a simulation starts at the engine origin and ends when
> nothing remains scheduled; a real-time run starts now and ends at `--end` or
> on interruption. Each tick of the entry's output is written as a `time value`
> line, the time in the canonical `datetime` spelling without its `@`. The
> configuration file is provisional: its format is versioned with the command,
> but the current `hgl run` implements the command line only and does not read
> `--config`.

## Excerpt 27

> The typed HIR records whether a named `fn` is an exact ordinary function or,
> through its `impl` modifier, an implementation of a canonical operator
> identity. Import changes only make an `impl fn` resolve or fail to resolve;
> they never reinterpret an ordinary function as a candidate.

## Excerpt 28

> There is no source grammar for top-level `init`, `deinit`, or disposal blocks.
> The scripted module compiler synthesizes lifecycle entry points and a
> registration handle from the module's exports, operator candidates, types, and
> dependencies. AOT output currently emits an explicit registration function but
> does not yet synthesize the dynamic query ABI or application bootstrap.

## Excerpt 29

> The current compiler's observed behavior for several of these, stated as
> observation rather than rule, is collected under
> [Open decisions](https://github.com/hhenson/hgraph_spec/blob/766033278bef6e9403cc99c0d8f318ba46a03919/language/docs/design/language-model.md#open-decisions-2026-09-07)
> (#767 item 6). Before code generation, an RFC must also define:

## Excerpt 30

> - `i64` overflow and conversion behavior;
> - division by zero and NaN comparison;
> - complete string escape and Unicode normalization rules;
> - destructuring and copy-with-update syntax; recursive struct fields are
>   agreed in [ADR 0012](https://github.com/hhenson/hgraph_spec/blob/766033278bef6e9403cc99c0d8f318ba46a03919/language/docs/design/decisions/0012-recursive-struct-fields.md)
>   and not yet implemented;
> - explicit generic arguments on function and operator calls, generic parameter
>   defaults, partial generic type application, and specialization relationships
>   beyond invariant applied types and the defined pattern ranking and ambiguity
>   rule;
> - general anonymous capture and type inference beyond inline iterator
>   predicates;
> - remaining phase/effect rules and modifier combinations for the agreed
>   value-level `const fn` extension;
> - collection delta constructors and a first-class public native encoding for
>   explicitly clearing an optional TSB field;
> - rolling-window iteration over hgraph's window view (`values`,
>   `time_values`, `value_times`, `removed_value`), which both window kinds
>   share, and a parameter spelling that accepts either kind (hgraph's
>   `TSWAny`);
> - non-scalar reconstructible caches, native type lifecycle and mapping
>   contracts, lifecycle output access, and runtime sinks;
> - runtime scalar error behavior;
> - an explicit end bound and approximate comparison for `eval`, delta
>   spellings for set, map, and list harness elements, and tuple construction
>   from temporal values.
