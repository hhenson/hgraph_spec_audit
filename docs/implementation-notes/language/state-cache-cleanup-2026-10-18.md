# State/cache notes relocated on 18 October 2026

Historical native storage mappings, grouping and lowering notes removed from
five language documents. These excerpts were not revalidated and do not assert
current support or define the standard. Initialization, restoration,
reconstruction and lifecycle requirements remain in the specification.

Source revision: `61eb6b8be0a9b989f00b9bace8b12ac74d403506`. The [provenance manifest](state-cache-cleanup-2026-10-18.provenance.json)
records source hashes, excerpt locations and original text. Relative links in
excerpts resolve to that specification revision.

## language/docs/developer-guide/syntax-and-semantics.md

### Excerpt 1

[Source, line 1278](https://github.com/hhenson/hgraph_spec/blob/61eb6b8be0a9b989f00b9bace8b12ac74d403506/language/docs/developer-guide/syntax-and-semantics.md#L1278).

> and one `stop` block. A `cache` is node-local data outside record/replay,
> re-initialized on every start; multiple scalar cache fields share a generated struct in one native
> `State<>` slot. A function may declare both: the two storages are planned
> independently, as native static nodes admit one `State<>` and one
> `RecordableState<>`, and `start` seeds a state field only when it is not
> already valid while assigning every cache field unconditionally -- so a
> restored state survives and its cache is rebuilt from it
> ([ADR 0011](https://github.com/hhenson/hgraph_spec/blob/61eb6b8be0a9b989f00b9bace8b12ac74d403506/language/docs/design/decisions/0011-cache-declarations.md)). It permits multiple function-level `when` blocks and preserves their
> source order; a `when` nested in another block is rejected because it cannot

## language/docs/design/language-model.md

### Excerpt 1

[Source, line 702](https://github.com/hhenson/hgraph_spec/blob/61eb6b8be0a9b989f00b9bace8b12ac74d403506/language/docs/design/language-model.md#L702).

> All state variables aggregate into one typed state value. State initializers
> lower to replay-aware startup initialization and do not overwrite restored
> state. `state` is by definition a time series and is always recordable: the
> language sets as its default the practice hgraph's own library applies only to
> loopback state. Reconstructible node-local data has the separate agreed
> `cache<T>` concept, mapped to native `State<T>` rather than
> `RecordableState<TSchema>`. It need not be global or module-owned. Cache does
> not require recordability, but rebuilding it must preserve observable
> computation; arbitrary resources still need a native ownership/lifecycle
> contract. `cache name[: T] = init` is the declaration
> ([ADR 0011](https://github.com/hhenson/hgraph_spec/blob/61eb6b8be0a9b989f00b9bace8b12ac74d403506/language/docs/design/decisions/0011-cache-declarations.md)): scalar cache fields share one generated native struct, re-initialized on
> every start, and may be declared beside `state`.
> Both cache and state storage/objects must be constructed before `start`,
> separately from logical initialization or restore. See
> [ADR 0008](https://github.com/hhenson/hgraph_spec/blob/61eb6b8be0a9b989f00b9bace8b12ac74d403506/language/docs/design/decisions/0008-temporal-contracts-and-target-mappings.md#cache-versus-recordable-state)
> for the reconstruction contract. Native nodes support both state selectors, and
> a function declaring `state` and `cache` lowers to both: a restored state field
> wins over its initializer, a cache field is rebuilt by every start.

## language/docs/design/decisions/0008-temporal-contracts-and-target-mappings.md

### Excerpt 1

[Source, line 166](https://github.com/hhenson/hgraph_spec/blob/61eb6b8be0a9b989f00b9bace8b12ac74d403506/language/docs/design/decisions/0008-temporal-contracts-and-target-mappings.md#L166).

> | HGL concept | Meaning | Current native counterpart | Record/replay |
> | --- | --- | --- | --- |
> | `state` | Persistent data needed to determine subsequent computation | `RecordableState<TSchema>` | Recorded and restored |
> | `cache<T>` | Node-local data reconstructible independently of missing history | `State<T>` | Excluded; rebuilt after restart |
>
> `cache<T>` names the agreed concept. The scalar declaration and initializer grammar is settled in
> [ADR 0011](https://github.com/hhenson/hgraph_spec/blob/61eb6b8be0a9b989f00b9bace8b12ac74d403506/language/docs/design/decisions/0011-cache-declarations.md). It does not rename C++ `State` or introduce
> a native `Cache` selector.

### Excerpt 2

[Source, line 215](https://github.com/hhenson/hgraph_spec/blob/61eb6b8be0a9b989f00b9bace8b12ac74d403506/language/docs/design/decisions/0008-temporal-contracts-and-target-mappings.md#L215).

> Native static nodes destroy constructed slots after a failed `start`, without
> calling that node's `stop`; partial resource acquisition must use RAII or a
> rollback guard. Generic HGL native construction hooks remain future work.

### Excerpt 3

[Source, line 226](https://github.com/hhenson/hgraph_spec/blob/61eb6b8be0a9b989f00b9bace8b12ac74d403506/language/docs/design/decisions/0008-temporal-contracts-and-target-mappings.md#L226).

> A node may declare both recordable history and a derived cache. Restoration
> precedes `start`; cache rebuilding uses the restored state. Their storage may
> be planned independently, but that choice must not change initialization order
> or observable recovery behavior.

## language/docs/design/decisions/0011-cache-declarations.md

### Excerpt 1

[Source, line 17](https://github.com/hhenson/hgraph_spec/blob/61eb6b8be0a9b989f00b9bace8b12ac74d403506/language/docs/design/decisions/0011-cache-declarations.md#L17).

> across state and cache, so each can read earlier declarations. An implementation
> could group cache fields in one storage object, provided that these rules hold.

## language/docs/design/native-interface.md

### Excerpt 1

[Source, line 175](https://github.com/hhenson/hgraph_spec/blob/61eb6b8be0a9b989f00b9bace8b12ac74d403506/language/docs/design/native-interface.md#L175).

> Reconstructible non-recordable data belongs in HGL cache (native `State<T>`);
> semantic history belongs in HGL `state` (native `RecordableState<TSchema>`) and
> requires recordable types. Native nodes support both selectors with independent
> storage and restore recordable state before `start` rebuilds the cache. Mixed
> HGL lowering and the opaque-type lifecycle bridge remain implementation work.
