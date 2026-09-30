# Relocated notes: language/docs/design/decisions/0010-lifecycle-capabilities.md

Source: [specification before separation](https://github.com/hhenson/hgraph_spec/blob/766033278bef6e9403cc99c0d8f318ba46a03919/language/docs/design/decisions/0010-lifecycle-capabilities.md).

These excerpts preserve earlier implementation notes and their surrounding
context. They were not revalidated during relocation and do not assert current
support or define language behavior. The current specification owns the rules.
HGL source examples remain in the linked specification revision.

## Excerpt 1

> Status: accepted. Implemented for `inject clock`, `inject scheduler`, the
> `scheduled()` handler selector, scheduler-driven sources, and the
> `passivate`/`activate` input-activity statements.

## Excerpt 2

> 1. **`inject clock`** binds `hgraph::EvaluationClockView` as `clock` in every
>    hook. `clock.evaluation_time()`, `clock.now()` (wall clock) and
>    `clock.next_cycle_evaluation_time()` return `datetime`.

## Excerpt 3

> 2. **`inject scheduler`** binds `hgraph::NodeScheduler` as `scheduler` in
>    every hook. `scheduler.schedule(delay)` and
>    `scheduler.schedule(delay, on_wall_clock)` take a `duration`;
>    `scheduler.schedule_at(time)` and `scheduler.schedule_at(time, on_wall_clock)`
>    take a `datetime`; `scheduler.is_scheduled()` returns `bool`;
>    `scheduler.next_scheduled_time()` returns `datetime`. Wall-clock alarms
>    follow hgraph's rule: only a real-time executor accepts them, and a due
>    alarm fires on the next evaluatable cycle. Tags are not exposed.
