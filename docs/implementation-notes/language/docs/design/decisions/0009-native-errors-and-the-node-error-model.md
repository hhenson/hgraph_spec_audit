# Relocated notes: language/docs/design/decisions/0009-native-errors-and-the-node-error-model.md

Source: [specification before separation](https://github.com/hhenson/hgraph_spec/blob/766033278bef6e9403cc99c0d8f318ba46a03919/language/docs/design/decisions/0009-native-errors-and-the-node-error-model.md).

These excerpts preserve earlier implementation notes and their surrounding
context. They were not revalidated during relocation and do not assert current
support or define language behavior. The current specification owns the rules.
HGL source examples remain in the linked specification revision.

## Excerpt 1

> Status: accepted. Implemented for source-defined and imported evaluation-time
> native functions (`throws`, descriptor policy `translated`), and used by the
> first checked kernels in `hgraph.native` (power, shifts).
