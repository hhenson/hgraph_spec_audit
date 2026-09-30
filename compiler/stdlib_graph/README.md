# Imported const → debug_print: current expectations

All six cases agree with reasoning, released Python hgraph 0.5.42 and the C++
engine. The [contract and literal cases](https://github.com/hhenson/hgraph_spec/tree/codex/stdlib-const-debug/compiler/stdlib_graph)
are owned by hgraph_spec. No observed result rewrites an expectation.

The C++ run uses the macOS stable-ABI wheel from hgraph PR #1669, commit
`540b0976ada30f313975ca90533d6a7bce02b519`, workflow run `36662605112`, artifact
`distribution-wheel-macos-26`. Its package reports `0.0.0`; the recorded binary
hash disambiguates it. Python is the released pure-Python package. Timestamp and
logging prefixes are excluded; label, sampling prefix and integer text remain.

Run in each runtime's isolated environment, supplying the cases from
hgraph_spec commit `3c139f8` or a later compatible revision:

```sh
python compiler/stdlib_graph/replay.py --cases /path/to/hgraph_spec/compiler/stdlib_graph/cases.json --engine python --output python.json
python compiler/stdlib_graph/replay.py --cases /path/to/hgraph_spec/compiler/stdlib_graph/cases.json --engine cpp --output cpp.json
```

The Rust compiler's generated-code tests separately compile the actual pinned
HGL library and assert source value/time, no future alarm, printed lines,
missing/equal ticks, sampling and fresh instances. They also change an HGL body
and rename the constant operator to verify that emitted behaviour follows source.
