# Runtime and wiring implementation evidence: notes relocated on 18 October 2026

Historical implementation material removed from the specification. These excerpts
were not revalidated and do not assert current support or define the standard.
Required behavior and open semantic decisions remain in the specification.

Source revision: `5d27402d0992873e9fa1d4eacfdcb7d79ebe6aa5`. The [provenance manifest](runtime-evidence-cleanup-2026-10-18.provenance.json)
records source hashes, excerpt locations and original text. Relative links in
excerpts resolve to that specification revision.

## wiring/wiring.md

### Excerpt 1

[Source, line 6](https://github.com/hhenson/hgraph_spec/blob/5d27402d0992873e9fa1d4eacfdcb7d79ebe6aa5/wiring/wiring.md#L6).

> resolution (Part 2), projections (WIR-5) and candidate selection (WIR-16 to
> WIR-18) are validated against two independent implementations
> ([wiring validation](https://github.com/hhenson/hgraph_spec_audit/blob/main/runtime/validation/wiring/README.md)); the Evidence table
> says which rules rest on cases and which on source reading only.

### Excerpt 2

[Source, line 408](https://github.com/hhenson/hgraph_spec/blob/5d27402d0992873e9fa1d4eacfdcb7d79ebe6aa5/wiring/wiring.md#L408).

> Parts of wiring that hgraph provides and the rules above do not yet cover.
> The first four are next: code generated for HGL calls operators that rely
> on them, so they need rules and cases as type resolution has.

### Excerpt 3

[Source, line 451](https://github.com/hhenson/hgraph_spec/blob/5d27402d0992873e9fa1d4eacfdcb7d79ebe6aa5/wiring/wiring.md#L451).

> [Wiring cases](https://github.com/hhenson/hgraph_spec/blob/5d27402d0992873e9fa1d4eacfdcb7d79ebe6aa5/wiring/cases_wiring.md) derive each decision from the rules; the
> [wiring validation](https://github.com/hhenson/hgraph_spec_audit/blob/main/runtime/validation/wiring/README.md) records the observations
> on hgraph's Python implementation (0.5.41) and its C++ implementation, and
> on the HGL front end.
>
> Implementation comparisons and test coverage are maintained in the
> [audit evidence](https://github.com/hhenson/hgraph_spec_audit/blob/main/runtime/validation/wiring/README.md).

## wiring/cases_wiring.md

### Excerpt 1

[Source, line 3](https://github.com/hhenson/hgraph_spec/blob/5d27402d0992873e9fa1d4eacfdcb7d79ebe6aa5/wiring/cases_wiring.md#L3).

> Status: validated expectations with recorded variations; rewritten for
> clarity on 2026-09-30 with the case names, rule references and expected
> decisions unchanged. The observations are in the
> [wiring validation](https://github.com/hhenson/hgraph_spec_audit/blob/main/runtime/validation/wiring/README.md).

### Excerpt 2

[Source, line 19](https://github.com/hhenson/hgraph_spec/blob/5d27402d0992873e9fa1d4eacfdcb7d79ebe6aa5/wiring/cases_wiring.md#L19).

> reference to a time-series of type `X`, and `T` a type variable. In the
> recorded runs these are hgraph's Python spellings (`TS[int]`,
> `TSD[str, REF[TS[int]]]`); the correspondence is one to one.

## runtime/injectables.md

### Excerpt 1

[Source, line 210](https://github.com/hhenson/hgraph_spec/blob/5d27402d0992873e9fa1d4eacfdcb7d79ebe6aa5/runtime/injectables.md#L210).

> **Logger.** Follows the shape common to logging interfaces — Python's
> `logging`, spdlog — and no more than that:

### Excerpt 2

[Source, line 313](https://github.com/hhenson/hgraph_spec/blob/5d27402d0992873e9fa1d4eacfdcb7d79ebe6aa5/runtime/injectables.md#L313).

> 1. **Writing the output in start.** Reading is settled (INJ-8). Writing in
>    start is possible in principle, and hgraph does not do it:
>
>    - Of the node implementations in hgraph's C++ standard library, 59 have a
>      start that is handed the output. Every one of them only *reads its
>      type* — to work out, once, how values of that type are built or
>      converted, and keep the answer in state. None writes a value.
>    - No stop is handed the output at all.
>    - What a write in start would mean is clear enough:

### Excerpt 3

[Source, line 339](https://github.com/hhenson/hgraph_spec/blob/5d27402d0992873e9fa1d4eacfdcb7d79ebe6aa5/runtime/injectables.md#L339).

>    extension, so it lands in hgraph first.

## runtime/open_points.md

### Excerpt 1

[Source, line 44](https://github.com/hhenson/hgraph_spec/blob/5d27402d0992873e9fa1d4eacfdcb7d79ebe6aa5/runtime/open_points.md#L44).

> | 16 | `lag` on HGL's clock | Injectables 2 | A language extension; lands in hgraph first |

## runtime/node.md

### Excerpt 1

[Source, line 499](https://github.com/hhenson/hgraph_spec/blob/5d27402d0992873e9fa1d4eacfdcb7d79ebe6aa5/runtime/node.md#L499).

> 2. **The output on a cycle that fails.** hgraph says what was written before
>    the failure stands, and calls the result "unspecified" in places. NOD-19
>    says it stands. Should a failing eval instead leave no tick on the main
>    output at all?
> 3. **A request for the past** is quietly ignored by hgraph's scheduler but is
>    an error in hgraph's graph schedule (see Graph, point 7).

### Excerpt 2

[Source, line 511](https://github.com/hhenson/hgraph_spec/blob/5d27402d0992873e9fa1d4eacfdcb7d79ebe6aa5/runtime/node.md#L511).

> 5. **Structural inputs.** Settled 2026-09-30: defined above and in NOD-28,
>    from hgraph's third input activity.

### Excerpt 3

[Source, line 515](https://github.com/hhenson/hgraph_spec/blob/5d27402d0992873e9fa1d4eacfdcb7d79ebe6aa5/runtime/node.md#L515).

> 6. **Error capture for nested nodes.** Settled 2026-09-30 from hgraph's
>    `try_except` and keyed `map_` capture: NOD-29. hgraph does not yet capture
>    for switch and mesh; that is an implementation gap, not a rule.

## runtime/graph.md

### Excerpt 1

[Source, line 566](https://github.com/hhenson/hgraph_spec/blob/5d27402d0992873e9fa1d4eacfdcb7d79ebe6aa5/runtime/graph.md#L566).

>    description and of the builder boundary (Overview, point 3). In hgraph today a node's behaviour is held as function
>    pointers and a process-local token; the builder can also retain opaque
>    extension state. None of that can be written out, which is why hgraph's
>    RFC 0022 manifest can identify a wired graph but not rebuild one. A stable
>    identity needs

### Excerpt 2

[Source, line 580](https://github.com/hhenson/hgraph_spec/blob/5d27402d0992873e9fa1d4eacfdcb7d79ebe6aa5/runtime/graph.md#L580).

> 3. **How types appear.** hgraph refers to types by interned address. A
>    storable description must carry them — by value, as a table of the types
>    it uses, or by canonical name. It must also carry, for each abstract
>    struct family, the closed set of concrete members wiring knew about:
>    hgraph freezes that set when wiring finishes, and a graph ignores members
>    registered later.

### Excerpt 3

[Source, line 588](https://github.com/hhenson/hgraph_spec/blob/5d27402d0992873e9fa1d4eacfdcb7d79ebe6aa5/runtime/graph.md#L588).

>    position is a non-peered parent. hgraph stores the peering explicitly;
>    what cannot be derived from edges is a **local** input,

### Excerpt 4

[Source, line 591](https://github.com/hhenson/hgraph_spec/blob/5d27402d0992873e9fa1d4eacfdcb7d79ebe6aa5/runtime/graph.md#L591).

> 5. **Structural inputs** are listed because hgraph's node type has them. They
>    need a definition in Time-series types before they can stay.

### Excerpt 5

[Source, line 596](https://github.com/hhenson/hgraph_spec/blob/5d27402d0992873e9fa1d4eacfdcb7d79ebe6aa5/runtime/graph.md#L596).

> 7. **Scheduling in the past.** hgraph's graph treats it as an error; hgraph's
>    node scheduler quietly ignores a request for a time that is not in the
>    future. GRF-12 takes the first. Should a node's scheduler be as strict?

### Excerpt 6

[Source, line 601](https://github.com/hhenson/hgraph_spec/blob/5d27402d0992873e9fa1d4eacfdcb7d79ebe6aa5/runtime/graph.md#L601).

>    considered once with nothing due. hgraph accepts this. It is harmless but
>    observable: the node's evaluation runs.

### Excerpt 7

[Source, line 612](https://github.com/hhenson/hgraph_spec/blob/5d27402d0992873e9fa1d4eacfdcb7d79ebe6aa5/runtime/graph.md#L612).

>     reclaimable from the start of the next. hgraph keeping a switch's old
>     branch until the next switch, or holding two address spaces for a switch,
>     is a design option ([Design options](https://github.com/hhenson/hgraph_spec/blob/5d27402d0992873e9fa1d4eacfdcb7d79ebe6aa5/runtime/design_options.md)).

## runtime/time_series.md

### Excerpt 1

[Source, line 576](https://github.com/hhenson/hgraph_spec/blob/5d27402d0992873e9fa1d4eacfdcb7d79ebe6aa5/runtime/time_series.md#L576).

> - **How the two directions of reference binding are carried out.** hgraph
>   has the *output* own a converted view of itself for each kind of input that
>   asks; that is a mechanism, and only what an input sees is specified here.

### Excerpt 2

[Source, line 586](https://github.com/hhenson/hgraph_spec/blob/5d27402d0992873e9fa1d4eacfdcb7d79ebe6aa5/runtime/time_series.md#L586).

>    ticked, and in hgraph stays valid even if its only valid field is later

### Excerpt 3

[Source, line 617](https://github.com/hhenson/hgraph_spec/blob/5d27402d0992873e9fa1d4eacfdcb7d79ebe6aa5/runtime/time_series.md#L617).

> In hgraph: `docs/source/developer_guide/data_structures/schemas/
> time_series.rst` (tick semantics, value and delta by kind);
> `data_structures/plans_and_ops/time_series.rst` and `linking_strategies.rst`
> (binding, sampling, keyed unbinds, delta visibility);
> `developer_guide/binding_vocabulary.rst`; RFC 0031 (growing lists), RFC 0036
> (references); the ruling of 2026-09-19 on `all_valid`; HGL's
> `language-model.md` (canonical temporal types, temporal metadata, collection
> traversal).

## runtime/scalar_types.md

### Excerpt 1

[Source, line 290](https://github.com/hhenson/hgraph_spec/blob/5d27402d0992873e9fa1d4eacfdcb7d79ebe6aa5/runtime/scalar_types.md#L290).

> - **Serial forms.** hgraph has a binary form and a JSON form, registered per
>   atomic type. They are needed for recording, replay and distribution, and
>   go with those.

### Excerpt 2

[Source, line 297](https://github.com/hhenson/hgraph_spec/blob/5d27402d0992873e9fa1d4eacfdcb7d79ebe6aa5/runtime/scalar_types.md#L297).

> - **Cyclic buffer and queue.** hgraph has both as value kinds. They exist to
>   implement windows (TSW) — they are the changing store behind one, not
>   values a graph passes around — and so are an implementation's concern.
> - **Shared and owned handles** to struct values. hgraph uses a shared handle
>   to avoid copying large values, and an owned one-pointer handle as the way a
>   struct holds a field of its own type. Both are mechanisms: VAL-18 is the
>   concept the second one serves.

## runtime/representations.md

### Excerpt 1

[Source, line 75](https://github.com/hhenson/hgraph_spec/blob/5d27402d0992873e9fa1d4eacfdcb7d79ebe6aa5/runtime/representations.md#L75).

> | AtomicCell | ATOMIC-RETENTION, ATOMIC-ZERO | [AtomicStorage](https://github.com/hhenson/hgraph_spec/blob/5d27402d0992873e9fa1d4eacfdcb7d79ebe6aa5/runtime/layout_example.md) | proposed; no native implementation |
> | MapQuote | QUOTE-HISTORY | NodeMap | proposed; no native implementation |
> | PivotQuote | QUOTE-HISTORY | FlatPivot | proposed; no native implementation |

## runtime/overview.md

### Excerpt 1

[Source, line 280](https://github.com/hhenson/hgraph_spec/blob/5d27402d0992873e9fa1d4eacfdcb7d79ebe6aa5/runtime/overview.md#L280).

> process-local. hgraph does not do this today; it is a goal the description is
> specified to allow.

### Excerpt 2

[Source, line 514](https://github.com/hhenson/hgraph_spec/blob/5d27402d0992873e9fa1d4eacfdcb7d79ebe6aa5/runtime/overview.md#L514).

>    instantiated on demand. A first pass at its contents, taken from hgraph's
>    graph builder, is in [Graph](https://github.com/hhenson/hgraph_spec/blob/5d27402d0992873e9fa1d4eacfdcb7d79ebe6aa5/runtime/graph.md). The hard part it leaves open is
>    how a description names what implements a node: hgraph holds behaviour as
>    process-local function pointers, which is why its RFC 0022 manifest can
>    *identify* a wired program but not rebuild one.

### Excerpt 3

[Source, line 526](https://github.com/hhenson/hgraph_spec/blob/5d27402d0992873e9fa1d4eacfdcb7d79ebe6aa5/runtime/overview.md#L526).

>    - *The compiler emits code that does the wiring when run* — what has been
>      done so far.

### Excerpt 4

[Source, line 564](https://github.com/hhenson/hgraph_spec/blob/5d27402d0992873e9fa1d4eacfdcb7d79ebe6aa5/runtime/overview.md#L564).

>   buffer and queue are not: hgraph has them to implement windows, and they
>   are an implementation's concern.

### Excerpt 5

[Source, line 577](https://github.com/hhenson/hgraph_spec/blob/5d27402d0992873e9fa1d4eacfdcb7d79ebe6aa5/runtime/overview.md#L577).

> In hgraph: `docs/source/developer_guide/architecture.rst` (the engine, the
> cycle, lifecycle); `developer_guide/data_structures/` and
> `binding_vocabulary.rst` (time-series and values); `developer_guide/
> nested_graphs.rst` (for the components nested nodes rely on, not the nodes);
> the RFCs, notably 0002 (temporal types), 0022 (serialisable graph manifest),
> 0027 (push queues), 0031 (unbounded lists), 0036 (reference transparency); the Python implementation for design
> intent; the older `docs/source/specification/` chapters for framing;
> `language/docs/design/` for the names HGL gives these concepts; and the
> `.hgspec` runtime-contract draft (PR #796).
>
> [Dynamic-case validation](https://github.com/hhenson/hgraph_spec_audit/blob/main/runtime/validation.md) records the TSD, REF and nested-graph
> expectations, executed traces and implementation variations.
>
> [Fixed collection cases](https://github.com/hhenson/hgraph_spec/blob/5d27402d0992873e9fa1d4eacfdcb7d79ebe6aa5/runtime/cases_fixed.md) validate the next TSL/TSB slice,
> including nesting and whole-output versus child bindings. User rulings
> and recorded variations are in its [comparison report](https://github.com/hhenson/hgraph_spec_audit/blob/main/runtime/validation/fixed/README.md).

## runtime/design_options.md

### Excerpt 1

[Source, line 20](https://github.com/hhenson/hgraph_spec/blob/5d27402d0992873e9fa1d4eacfdcb7d79ebe6aa5/runtime/design_options.md#L20).

> and is reclaimed no earlier than the start of the next. hgraph goes further
> and reclaims lazily:

### Excerpt 2

[Source, line 41](https://github.com/hhenson/hgraph_spec/blob/5d27402d0992873e9fa1d4eacfdcb7d79ebe6aa5/runtime/design_options.md#L41).

> hgraph keeps the old branch until the next switch, and an implementation may
> go further and hold two fully built address spaces, A and B, alternating

### Excerpt 3

[Source, line 61](https://github.com/hhenson/hgraph_spec/blob/5d27402d0992873e9fa1d4eacfdcb7d79ebe6aa5/runtime/design_options.md#L61).

> from child events. hgraph maintains them: a child notification updates the
> parent's change time, and a read costs nothing beyond a field.

### Excerpt 4

[Source, line 76](https://github.com/hhenson/hgraph_spec/blob/5d27402d0992873e9fa1d4eacfdcb7d79ebe6aa5/runtime/design_options.md#L76).

> collection and owns an output, to which every consumer binds. hgraph folds
> the assembly into the consumer when there is one consumer, and may share a
> node when there are several.

### Excerpt 5

[Source, line 92](https://github.com/hhenson/hgraph_spec/blob/5d27402d0992873e9fa1d4eacfdcb7d79ebe6aa5/runtime/design_options.md#L92).

> hgraph gives such a node no scheduler storage at all: the alarm is a view
> over the graph's schedule, constructed on demand, and the node's memory
> holds no request.

### Excerpt 6

[Source, line 105](https://github.com/hhenson/hgraph_spec/blob/5d27402d0992873e9fa1d4eacfdcb7d79ebe6aa5/runtime/design_options.md#L105).

> owner's inputs are bound to, with nothing in between. hgraph compiles the
> child against placeholders for those inputs and binds them at instantiation,
> rather than inserting a forwarding node.

### Excerpt 7

[Source, line 120](https://github.com/hhenson/hgraph_spec/blob/5d27402d0992873e9fa1d4eacfdcb7d79ebe6aa5/runtime/design_options.md#L120).

> find the newcomer. hgraph guards reuse with an invalidation subscription;
> the Rust store stamps each slot with a generation that a reference carries
> and checks.

## runtime/execution_engine.md

### Excerpt 1

[Source, line 397](https://github.com/hhenson/hgraph_spec/blob/5d27402d0992873e9fa1d4eacfdcb7d79ebe6aa5/runtime/execution_engine.md#L397).

> values and the schedule as they were when the node failed. In Python the
>      failed run is kept alive by the raised exception and torn down when the
>      exception is released.

### Excerpt 2

[Source, line 352](https://github.com/hhenson/hgraph_spec/blob/5d27402d0992873e9fa1d4eacfdcb7d79ebe6aa5/runtime/execution_engine.md#L352).

> Facilities hgraph's engine has that no concept above needs yet. Each is
> specified when an implementation requires it,

### Excerpt 3

[Source, line 364](https://github.com/hhenson/hgraph_spec/blob/5d27402d0992873e9fa1d4eacfdcb7d79ebe6aa5/runtime/execution_engine.md#L364).

> profiling and diagnostics are built on them. hgraph pairs every *before*
>   with an *after* for evaluation and stop even on failure, but not for start.

### Excerpt 4

[Source, line 374](https://github.com/hhenson/hgraph_spec/blob/5d27402d0992873e9fa1d4eacfdcb7d79ebe6aa5/runtime/execution_engine.md#L374).

> - **Pausing a cycle.** hgraph lets a node pause the cycle it is in and have
>   it resumed at the same evaluation time (mesh uses this while waiting on a
>   dependency). ENG-2 assumes no such thing exists.

### Excerpt 5

[Source, line 384](https://github.com/hhenson/hgraph_spec/blob/5d27402d0992873e9fa1d4eacfdcb7d79ebe6aa5/runtime/execution_engine.md#L384).

> 1. **Failure handling: is *report, then stop* a concept?** What hgraph does:

### Excerpt 6

[Source, line 389](https://github.com/hhenson/hgraph_spec/blob/5d27402d0992873e9fa1d4eacfdcb7d79ebe6aa5/runtime/execution_engine.md#L389).

>    - hgraph's `cleanup_on_error` option chooses the **order**. *True* (the
>      default): stop first, then report — by the time the caller sees the
>      failure, every stop hook has run. *False*: report first — the caller
>      receives the failure together with the failed run, still started, and
>      the stop happens when the caller lets go of it.

### Excerpt 7

[Source, line 403](https://github.com/hhenson/hgraph_spec/blob/5d27402d0992873e9fa1d4eacfdcb7d79ebe6aa5/runtime/execution_engine.md#L403).

>    - hgraph has a second, separate setting alongside it: how much context the
>      report of an escaped failure carries — how far upstream of the failing
>      node to walk, and whether to include the input values found there. That
>      is the content of a node error and belongs in Node.

### Excerpt 8

[Source, line 412](https://github.com/hhenson/hgraph_spec/blob/5d27402d0992873e9fa1d4eacfdcb7d79ebe6aa5/runtime/execution_engine.md#L412).

> 2. **Pausing a cycle, for mesh.** hgraph's mesh pauses the cycle while a
>    dependency is resolved. Either pausing becomes an optional engine facility

## runtime/conformance.md

### Excerpt 1

[Source, line 3](https://github.com/hhenson/hgraph_spec/blob/5d27402d0992873e9fa1d4eacfdcb7d79ebe6aa5/runtime/conformance.md#L3).

> Status: proposed methodology; the bounded [dynamic cases](https://github.com/hhenson/hgraph_spec_audit/blob/main/runtime/validation.md) have
> recorded Python/C++ runs. Other cases retain their stated evidence limits.

### Excerpt 2

[Source, line 127](https://github.com/hhenson/hgraph_spec/blob/5d27402d0992873e9fa1d4eacfdcb7d79ebe6aa5/runtime/conformance.md#L127).

> Core integration then needs public C++/Python coverage and the full acceptance
> gates.
