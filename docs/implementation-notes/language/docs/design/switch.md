# Relocated notes: language/docs/design/switch.md

Source: [specification before separation](https://github.com/hhenson/hgraph_spec/blob/766033278bef6e9403cc99c0d8f318ba46a03919/language/docs/design/switch.md).

These excerpts preserve earlier implementation notes and their surrounding
context. They were not revalidated during relocation and do not assert current
support or define language behavior. The current specification owns the rules.
HGL source examples remain in the linked specification revision.

## Excerpt 1

> The agreed `default:` body catches selector values that match none of the
> explicit cases. In graph composition it becomes the native `switch_` default
> branch, with the same captures, result checks, and lifecycle as other branches.
> In node-style code it becomes the native C++ dispatch fallback.

## Excerpt 2

> The native [higher-order operator contract](https://github.com/hhenson/hgraph/blob/main/include/hgraph/lib/std/operators/higher_order.h)
> provides the switch key, cases, optional default, and outputless form.
> [Switch execution](https://github.com/hhenson/hgraph/blob/main/src/hgraph/runtime/switch_node.cpp) owns dispatch
> and lifecycle; [public-wiring tests](https://github.com/hhenson/hgraph/blob/main/tests/cpp/test_switch.cpp) cover
> default selection, no-match failure, outputless branches, and fresh branch
> instances on reselection.

## Excerpt 3

> The exact admitted selector types, native enum representation/import rules,
> and any exposure of native reload policy remain to be discussed. Duplicate
> resolved case rejection and declared-member exhaustiveness are agreed source
> checks; their compiler implementation remains pending. The statement form is
> illustrated in `language/stdlib/`; a switch expression-value surface is not added by these
> examples. This record does not add parser, IR, backend, or runtime
> implementation, and leaves the deferred `for` work untouched.
