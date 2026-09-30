# Relocated notes: runtime/graph.md

Source: [specification before separation](https://github.com/hhenson/hgraph_spec/blob/766033278bef6e9403cc99c0d8f318ba46a03919/runtime/graph.md).

These excerpts preserve earlier implementation notes and their surrounding
context. They were not revalidated during relocation and do not assert current
support or define language behavior. The current specification owns the rules.
HGL source examples remain in the linked specification revision.

## Excerpt 1

> In hgraph: `docs/source/developer_guide/architecture.rst` (rank, the graph
> schedule, the cycle, start and stop order) and `nested_graphs.rst` (boundary
> binding, scheduling delegation — for the components, not the nodes built on
> them); `include/hgraph/runtime/graph.h` (the graph builder, edges);
> `runtime/node.h` (node builder, node type, node type descriptor);
> `types/time_series/endpoint_schema.h` (peered, non-peered, local);
> `runtime/nested_graph_node.h` and `runtime/child_graph_inspection.h` (child
> graphs and their bindings); RFC 0022 (the manifest). The original Python
> builder was not available to check against.
