# Relocated notes: language/docs/design/decisions/0015-pull-sources.md

Source: [specification before separation](https://github.com/hhenson/hgraph_spec/blob/766033278bef6e9403cc99c0d8f318ba46a03919/language/docs/design/decisions/0015-pull-sources.md).

These excerpts preserve earlier implementation notes and their surrounding
context. They were not revalidated during relocation and do not assert current
support or define language behavior. The current specification owns the rules.
HGL source examples remain in the linked specification revision.

## Excerpt 1

> Status: proposed. The spelling was agreed with the project owner on
> 2026-09-28. The C++ compiler implements decisions 1 to 5 in hgraph PR
> [#1670](https://github.com/hhenson/hgraph/pull/1670) (open); the Rust
> compiler has not started. The standard-library re-expression and the
> `const` spelling (consequences) are follow-ups.

## Excerpt 2

> hgraph has two schedulers. `NodeScheduler` is the reliable one: tagged
> alarms, cancellation, `is_scheduled`, wall-clock alarms, checkpoint capture
> and restore. `SingleShotScheduler` is the stateless one: it marks the node
> to evaluate now, after a delay or at a time, keeps the earliest request,
> holds no state and is neither stored nor recovered (ADR 0011). It exists
> only for C++ nodes today.

## Excerpt 3

> hgraph's own pull sources (`const`, `nothing`, `replay`, `replay_const`) are
> Python generators: a function yields `(time, value)` pairs and the runtime
> publishes each pair at its time. Nothing in HGL expresses that shape.

## Excerpt 4

> `yield` and `while` join the hard reserved words in the keyword table of
> `token.cpp` and in the developer guide. Neither is used as an identifier in
> the standard library, the examples or the compiler tests. `alarm` is an
> injectable name and, like `out`, `clock` and `scheduler`, stays contextual.

## Excerpt 5

> - `nothing` in the standard library is re-expressed on `alarm` (hgraph_std
>   PR [#5](https://github.com/hhenson/hgraph_std/pull/5)), and its catalogue
>   entry moves from native-provider to implemented.
> - hgraph's `const` reduces to the alarm shape above, but its library
>   spelling is `const`, never `const_` (project owner, 2026-09-29: a
>   function is not the `const` modifier, and the replacement of a native
>   identity keeps its name), and its contract keeps
>   [MIG-009](https://github.com/hhenson/hgraph_spec/blob/766033278bef6e9403cc99c0d8f318ba46a03919/language/docs/design/migration-requirements.md#mig-009-source-names-versus-native-identities):
>   an independent scalar `T` and output shape `S`, with `delay` after them.
>   hgraph PR [#1671](https://github.com/hhenson/hgraph/pull/1671) supplies
>   the mapping: `const` is admitted as an operator, function, instantiation
>   and imported name, a `const(f)` call whose one argument names a function
>   stays the value-role selector of ADR 0008, and any other `const(...)`
>   call goes to the operator in scope. hgraph_std PR #5 then declares
>   `const` on the alarm; no `const_` is added.
> - The evaluation harness needs an end for a source: today `eval` requires a
>   time-series input to bound the run, and that stays the rule. A generator
>   that reaches the end of its body finishes, but decision 4 admits
>   `while { yield ... }`, which never does, so `eval` cannot run a source to
>   completion as its bound. A harness spelling for an explicit end remains
>   open in "Tests and the evaluation harness"; the example pairs each source
>   with a sink on a ticking input.
> - Compiler work: the `alarm` injectable (hgraph already has an argument
>   provider for `SingleShotScheduler`), the `while` statement in runtime
>   bodies, the generator classification and lowering, and the two keywords.
>   The Rust compiler mirrors the same source. Editor tooling adds the two
>   keywords.

## Excerpt 6

> `yield` is a lowering, not a runtime feature. A generator becomes the same
> static node a `when scheduled()` source is today: node-local storage, an
> `eval` hook and a wake-up. hgraph already has every runtime piece: the
> argument provider for `SingleShotScheduler` in `eval`, the
> `schedule_on_start` node attribute, and the generated cache struct in one
> `State<>` slot (ADR 0011). The runtime does not change; the compiler does.

## Excerpt 7

> 1. **Syntax.** `yield` and `while` in the keyword table, two productions in
>    the declarative grammar, and two typed-HIR statements beside `when` and
>    `for`: a yield with a time and a value, and a while with an optional
>    condition.
> 2. **Classification.** A body containing `yield` is a runtime function of a
>    new kind, generator. The checker enforces decision 3: no temporal
>    parameters, a result type, the time typed `duration` or `datetime`, the
>    value typed as the result, and none of `state`, `cache`, `out`,
>    `scheduler`, `alarm`, `when`, `start` or `stop`. `while` is admitted in
>    runtime bodies only.
> 3. **IR.** hgraph IR keeps `yield` and `while` as statements and marks the
>    callable a generator. It has no labels or jumps, so the state machine is
>    not an IR rewrite: each backend lowers the generator in its own emitter,
>    where the target language's control flow is available.
> 4. **C++ emission.** The emitter numbers the yield points in body order,
>    with `-1` meaning finished. One cache struct (the ADR 0011 slot) holds
>    the resume index, a parked flag, the parked value and every local of the
>    body, hoisted so that no C++ local with an initializer sits in the
>    `eval` body: a `let` or `var` becomes an assignment to its field and
>    every read goes through the slot. The node carries `schedule_on_start`,
>    `start` rebuilds the struct, and `eval` takes the slot, the
>    `SingleShotScheduler` and the output. `eval` first publishes a parked
>    value, then dispatches: a `switch` on the resume index jumps to the label
>    after the last yield. At a yield the instant is `alarm.now()` plus the
>    duration, or the datetime itself; earlier than now is skipped; equal to
>    now publishes, after a duplicate-time check against the output's
>    modified flag, and the body continues; later parks the value, stores the
>    resume index, schedules the alarm at the instant and returns. Falling
>    off the end, or a bare `return`, stores `-1`. Jumping into a `while` or
>    `if` block is legal C++ because hoisting leaves no initialization to
>    bypass, the technique of C# iterators and stackless coroutine libraries.
>    The Rust emitter, having no `goto`, lowers the same IR to a loop over a
>    `match` on the resume index.
> 5. **Order.** Keywords, parser and HIR with parser tests; `alarm` end to
>    end, which lets `nothing` and a constant source drop the state slot;
>    `while` in runtime bodies; the generator classification and the C++
>    state machine with tests for a constant, a counting loop, a single parked
>    value, an absolute time, a skipped past time, a same-time publication,
>    a bare return and a yield inside `if`, and the duplicate-time error;
>    then the standard-library re-expression and the editor keywords. The
>    C++ compiler implements all of this except the last two.

## Excerpt 8

> Why not C++20 coroutines: the frame is heap-allocated at start, suspension
> and exceptions are their own model, there is no Rust mirror, and hgraph
> has one runtime model with no second node kind. The per-tick cost of the
> state machine is a switch, a publication and one `schedule_node` call, with
> no allocation and no scheduler state slot.

## Excerpt 9

> ADR 0011 refuses sources with caches under the component checkpoint
> contract, so a generator inside a checkpointed component is refused until
> that contract admits reconstructible storage on sources.
