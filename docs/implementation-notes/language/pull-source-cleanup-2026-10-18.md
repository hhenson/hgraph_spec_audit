# Pull-source and scheduler notes relocated on 18 October 2026

Historical native capability mappings, generator implementation sketches,
backend comparisons and progress notes removed from four language documents.
These excerpts were not revalidated and do not assert current support or define
the standard. Source behavior, checkpoint scope, restrictions and open questions
remain in the specification.

Source revision: `0f3bc6e56cb5f7bebe4ca7d3629aea547a89ecab`. The [provenance manifest](pull-source-cleanup-2026-10-18.provenance.json)
records source hashes, excerpt locations and original text. Relative links in
excerpts resolve to that specification revision.

## language/docs/design/decisions/0015-pull-sources.md

### Excerpt 1

[Source, line 10](https://github.com/hhenson/hgraph_spec/blob/0f3bc6e56cb5f7bebe4ca7d3629aea547a89ecab/language/docs/design/decisions/0015-pull-sources.md#L10).

> to publish one value, and `scheduler` binds hgraph's `NodeScheduler`: a
> per-node state slot of tagged pending events that checkpoints capture and
> restore.

### Excerpt 2

[Source, line 27](https://github.com/hhenson/hgraph_spec/blob/0f3bc6e56cb5f7bebe4ca7d3629aea547a89ecab/language/docs/design/decisions/0015-pull-sources.md#L27).

> `alarm` is an injectable that maps to `SingleShotScheduler`. It offers

### Excerpt 3

[Source, line 57](https://github.com/hhenson/hgraph_spec/blob/0f3bc6e56cb5f7bebe4ca7d3629aea547a89ecab/language/docs/design/decisions/0015-pull-sources.md#L57).

> | Node state | none | pending events (tagged inside hgraph; tags are not exposed, ADR 0010) |

### Excerpt 4

[Source, line 103](https://github.com/hhenson/hgraph_spec/blob/0f3bc6e56cb5f7bebe4ca7d3629aea547a89ecab/language/docs/design/decisions/0015-pull-sources.md#L103).

>   bare `return` finishes the source. `for` is not admitted (see the open
>   questions): its iteration owns the body, so a suspension inside it could
>   not resume.

### Excerpt 5

[Source, line 107](https://github.com/hhenson/hgraph_spec/blob/0f3bc6e56cb5f7bebe4ca7d3629aea547a89ecab/language/docs/design/decisions/0015-pull-sources.md#L107).

>   statement. It cannot sit inside a value (an `if` used as an expression,
>   a lambda), where a backend has no resume point to jump to.

### Excerpt 6

[Source, line 128](https://github.com/hhenson/hgraph_spec/blob/0f3bc6e56cb5f7bebe4ca7d3629aea547a89ecab/language/docs/design/decisions/0015-pull-sources.md#L128).

>   recorded. After a restore the body restarts from its first statement,
>   which is what hgraph's generator does.

### Excerpt 7

[Source, line 159](https://github.com/hhenson/hgraph_spec/blob/0f3bc6e56cb5f7bebe4ca7d3629aea547a89ecab/language/docs/design/decisions/0015-pull-sources.md#L159).

> Audit evidence: [negative durations](https://github.com/hhenson/hgraph_spec_audit/blob/9967125fe6fad385e2d120e40049348402e0c686/runtime/validation/generator_negative/README.md)
> and [target ordering](https://github.com/hhenson/hgraph_spec_audit/blob/9967125fe6fad385e2d120e40049348402e0c686/runtime/validation/generator_ordering/README.md).

### Excerpt 8

[Source, line 176](https://github.com/hhenson/hgraph_spec/blob/0f3bc6e56cb5f7bebe4ca7d3629aea547a89ecab/language/docs/design/decisions/0015-pull-sources.md#L176).

> A generator needs no runtime node kind. The compiler lowers the body to a
> state machine: a resume position and the hoisted locals in node-local
> storage, one parked value, and the stateless scheduler for the wake-up. A
> generator is therefore sugar over decision 1, and the only runtime change
> both decisions need is exposing `SingleShotScheduler` to HGL.

### Excerpt 9

[Source, line 213](https://github.com/hhenson/hgraph_spec/blob/0f3bc6e56cb5f7bebe4ca7d3629aea547a89ecab/language/docs/design/decisions/0015-pull-sources.md#L213).

> ## Possible realization
>
> An implementation could represent a generator by its resume position, live
> locals and a pending publication. At a future yield it saves that state and
> schedules resumption; at a due yield it publishes and continues in source
> order. It must preserve skipped past absolute times, negative-duration and
> duplicate-time errors, loops, conditionals and termination. Native coroutines and explicit state machines
> are possible realizations, not language requirements.

### Excerpt 10

[Source, line 224](https://github.com/hhenson/hgraph_spec/blob/0f3bc6e56cb5f7bebe4ca7d3629aea547a89ecab/language/docs/design/decisions/0015-pull-sources.md#L224).

> - Whether a generator may carry a `stop` block. hgraph's `@generator.stop`
>   exists; the block would run at teardown with the `const` parameters only.
> - Whether an absolute `yield` time in the past should be a diagnostic
>   rather than skipped. hgraph skips silently; this record follows it.
> - `for` inside a generator, which hgraph's replay generators use over a
>   constant collection. It needs the loop index hoisted beside the locals
>   and an index-based loop in each backend; until then the checker rejects
>   it and points to `while`.

## language/docs/design/decisions/0010-lifecycle-capabilities.md

### Excerpt 1

[Source, line 7](https://github.com/hhenson/hgraph_spec/blob/0f3bc6e56cb5f7bebe4ca7d3629aea547a89ecab/language/docs/design/decisions/0010-lifecycle-capabilities.md#L7).

> The language agreed the injectable names `clock` and `scheduler` with no
> surface behind them, and the migration catalogue holds thirty-six core
> operators under blocker B2 (lifecycle and activation). Three things were
> missing, and they are what the native stream nodes actually use:
>
> - an evaluation clock (`EvaluationClockView`: evaluation time, wall-clock
>   time, next cycle);
> - the node scheduler (`NodeScheduler`: schedule after a delay or at a time,
>   on the engine or the wall clock; query the next alarm; know whether the
>   current evaluation is the alarm firing); and
> - input activity: a node that has seen enough ticks stops listening to an
>   input (`make_passive`) and may listen again later (`make_active`).

### Excerpt 2

[Source, line 53](https://github.com/hhenson/hgraph_spec/blob/0f3bc6e56cb5f7bebe4ca7d3629aea547a89ecab/language/docs/design/decisions/0010-lifecycle-capabilities.md#L53).

>    `next_scheduled_time(scheduler)` returns `datetime`. Wall-clock alarms
>    follow hgraph's rule: only a real-time executor accepts them, and a due
>    alarm fires on the next evaluatable cycle. Tags are not exposed.

### Excerpt 3

[Source, line 59](https://github.com/hhenson/hgraph_spec/blob/0f3bc6e56cb5f7bebe4ca7d3629aea547a89ecab/language/docs/design/decisions/0010-lifecycle-capabilities.md#L59).

>    and is true when the current evaluation is the node's alarm firing
>    (`is_scheduled_now`). A source on the stateless `alarm` of

### Excerpt 4

[Source, line 76](https://github.com/hhenson/hgraph_spec/blob/0f3bc6e56cb5f7bebe4ca7d3629aea547a89ecab/language/docs/design/decisions/0010-lifecycle-capabilities.md#L76).

>    for evaluation in the starting cycle, which is how a static node's
>    `schedule_on_start` is spelled. Its default all-input validity requirement

### Excerpt 5

[Source, line 85](https://github.com/hhenson/hgraph_spec/blob/0f3bc6e56cb5f7bebe4ca7d3629aea547a89ecab/language/docs/design/decisions/0010-lifecycle-capabilities.md#L85).

>    evaluation-only: `start` and `stop` have no temporal input access. They
>    lower to the input view's `make_passive()` / `make_active()`. A passive
>    input still holds its value and validity; it just no longer activates the
>    node. The node's static activation policy is unchanged; activity is a
>    per-evaluation effect, exactly as in a hand-written node.

### Excerpt 6

[Source, line 93](https://github.com/hhenson/hgraph_spec/blob/0f3bc6e56cb5f7bebe4ca7d3629aea547a89ecab/language/docs/design/decisions/0010-lifecycle-capabilities.md#L93).

> - `freeze`, `take` and `until_true` become authorable as parallel identities.
>   `schedule` remains blocked: its native counter is non-recordable `State<Int>`,
>   while HGL `state` is checkpointed. The cache declarations in ADR 0008 and
>   positive-delay validation in `start` are still required.
>   Likewise, `throttle`, `batch`, `gate`, `lag` and `window` still
>   need the buffered-delta and queue state contracts (MIG-005) and remain B2.

## language/docs/design/decisions/0011-cache-declarations.md

### Excerpt 1

[Source, line 30](https://github.com/hhenson/hgraph_spec/blob/0f3bc6e56cb5f7bebe4ca7d3629aea547a89ecab/language/docs/design/decisions/0011-cache-declarations.md#L30).

> `SingleShotScheduler` is best effort. Its schedules are neither stored nor
> recovered; its normal `start` behaviour is unchanged.

### Excerpt 2

[Source, line 39](https://github.com/hhenson/hgraph_spec/blob/0f3bc6e56cb5f7bebe4ca7d3629aea547a89ecab/language/docs/design/decisions/0011-cache-declarations.md#L39).

> The native time-series-delay overloads also retain their progress. A fresh
> `start` input still resets their emission budget and re-bases the grid. Scalar configuration participates in
> checkpoint compatibility, so changing a delay or budget requires a new run.

### Excerpt 3

[Source, line 43](https://github.com/hhenson/hgraph_spec/blob/0f3bc6e56cb5f7bebe4ca7d3629aea547a89ecab/language/docs/design/decisions/0011-cache-declarations.md#L43).

> Generated HGL scheduler sources receive an explicit checkpoint contract only
> when their runtime state consists of endpoints and pending alarms. Sources
> with caches, clock injection, or logger injection remain refused. This does
> not implement general native-resource recovery. Wall-clock recovery remains
> outside the simulation-only component contract; `SingleShotScheduler` retains
> its best-effort exception.

## language/docs/design/language-model.md

### Excerpt 1

[Source, line 719](https://github.com/hhenson/hgraph_spec/blob/0f3bc6e56cb5f7bebe4ca7d3629aea547a89ecab/language/docs/design/language-model.md#L719).

> body to inspect or incrementally update its output. Other injectables, such as
> `logger`, `clock`, `scheduler` and `alarm`, map to their hgraph selector
> contracts (`LoggerView`, `EvaluationClockView`, `NodeScheduler`,
> `SingleShotScheduler`; ADR 0010 fixes the clock property and scheduler function
> surfaces, [ADR 0015](https://github.com/hhenson/hgraph_spec/blob/0f3bc6e56cb5f7bebe4ca7d3629aea547a89ecab/language/docs/design/decisions/0015-pull-sources.md) the alarm's).
