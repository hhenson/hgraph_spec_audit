# Relocated notes: language/docs/design/native-surface-proposal.md

Source: [specification before separation](https://github.com/hhenson/hgraph_spec/blob/766033278bef6e9403cc99c0d8f318ba46a03919/language/docs/design/native-surface-proposal.md).

These excerpts preserve earlier implementation notes and their surrounding
context. They were not revalidated during relocation and do not assert current
support or define language behavior. The current specification owns the rules.
HGL source examples remain in the linked specification revision.

## Excerpt 1

> Status: accepted names and direction; implemented coverage and remaining work
> are distinguished below. The [module inventory](https://github.com/hhenson/hgraph/blob/main/language/stdlib/hgl/hgraph/README.md)
> records the source-native bindings under the single `hgraph.native` identity.

## Excerpt 2

> | Function | Contract | Implementation in this slice |
> | --- | --- | --- |
> | `key_set(value)` | The live set of map keys | Existing composition path plus runtime map-input projection |
> | `modified(key_set(value))` | Keys were added or removed, not merely child values changed | Runtime membership-delta query; structural activation for a membership-only `when` |
> | `contains(collection, key)` | Membership, independent of a child's validity | Runtime sets/maps/key-set projections; strings also support substring membership |
> | `at(value, key_or_index)` | Strict access; missing key or out-of-range index is an error | Runtime map/list children and tick-window samples |
> | `get(value, key_or_index, default=null)` | Safe lookup with a caller-supplied fallback, defaulting to `null` | Accepted; not implemented yet |

## Excerpt 3

> The `default=null` notation above describes the parameter default. HGL named
> call arguments retain their existing colon syntax: `get(value, key, default: 0)`.
> The new collection access intrinsics currently take positional arguments.

## Excerpt 4

> `key_set` is borrowed within the evaluation; it does not copy keys into a new
> container. Its added/removed ranges use the input's current projected delta,
> not stale storage changes from an earlier evaluation. A local projection must
> use `let`, not mutable `var`. The borrowed view must not escape the evaluation.
> Returning it from a `when`, or assigning it to `out`, synchronously copies its
> current contents into owned output storage. This aligns the whole set, including
> removals; it does not return the borrowed projection itself. Structural children
> read with `at` use the same complete-value copy path when written to an output.
> The existing C++ mutation operation determines the output delta, including empty
> deltas when a complete value is written without changing membership.
> An ordinary child-only tick is rejected by the membership timestamp without
> scanning keys. A sampled reference rebind uses the input's projected key ranges.
> `last_modified` on a runtime key-set projection is deliberately rejected until
> the compiler can retain membership history across rebinds. A composition-level
> `key_set` endpoint already supplies persistent tracking.

## Excerpt 5

> The raw C++ `TSDInputView::structure_modified()` also reports child-only delta
> epochs. It is not the implementation of the HGL membership predicate. Raw C++
> View methods and their spelling remain unchanged.

## Excerpt 6

> Open detail for `get`: whether a present but invalid child returns the fallback
> or remains distinct from an absent key/index. The proposed rule is absent-only,
> preserving removal versus invalidation; this detail still needs agreement.
> The compiler also needs a general nullable-expression/result path: its current
> `null` lowering is limited to optional struct fields and sparse deltas. Neither
> an invented zero value nor an implicit no-output tick implements nullable lookup.

## Excerpt 7

> The accepted initial accessors are `at(window, index)`, `time_at(window, index)`,
> `front(window)`, `back(window)`, and `removed_value(window)`. They now lower for
> tick-count windows and are tested through ring-buffer wraparound. Indices are
> zero-based in oldest-to-newest logical order. Strict bounds errors propagate
> through the generated node; they are not hidden inside a `noexcept` wrapper.
> List `front` and `back` use the same strict bounds policy.
> Strict list/map value access also rejects a present but invalid child instead
> of reading its retained storage. `valid(at(value, key))` can inspect the child
> without reading its payload, but the key/index must still exist.

## Excerpt 8

> The newly implemented collection accessors are compiler intrinsics in runtime
> bodies, not additional descriptor-native overloads. They use the existing C++
> typed input APIs. Only `key_set` also has composition lowering in this slice.
> The source-native ABI still needs standalone generic value arguments,
> dependent/borrowed results, and exception/effect metadata before all these
> functions can move behind ordinary imported native declarations.
