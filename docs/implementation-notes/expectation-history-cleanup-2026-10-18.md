# Expected observations and historical corrections: notes relocated on 18 October 2026

Historical implementation material removed from the specification. These excerpts
were not revalidated and do not assert current support or define the standard.
Required behavior and open semantic decisions remain in the specification.

Source revision: `b295f39c94403dc4093a1d8c009cdcc6f2549a24`. The [provenance manifest](expectation-history-cleanup-2026-10-18.provenance.json)
records source hashes, excerpt locations and original text. Relative links in
excerpts resolve to that specification revision.

## runtime/validation/fixed/reasoned.json

### Excerpt 1

[Source, line 2](https://github.com/hhenson/hgraph_spec/blob/b295f39c94403dc4093a1d8c009cdcc6f2549a24/runtime/validation/fixed/reasoned.json#L2).

>   "status": "Each case's initial expectations were written before its first execution. Snapshot helpers only expand explicitly listed values and timestamps; no runtime output is imported.",

### Excerpt 2

[Source, line 51](https://github.com/hhenson/hgraph_spec/blob/b295f39c94403dc4093a1d8c009cdcc6f2549a24/runtime/validation/fixed/reasoned.json#L51).

>         {"valid": true, "all_valid": false, "modified": true, "last": 4, "value": [null, 9], "delta": {}, "peer": false, "children": {"0": {"valid": false, "modified": false, "last": "never", "value": null, "delta": null}, "1": {"valid": true, "modified": false, "last": 2, "value": 9, "delta": null}}},

### Excerpt 3

[Source, line 72](https://github.com/hhenson/hgraph_spec/blob/b295f39c94403dc4093a1d8c009cdcc6f2549a24/runtime/validation/fixed/reasoned.json#L72).

>       "reason": "TS-1, TS-4, TS-7: partial publication, invalidation and revalidation preserve fixed positions. Non-peered validity is derived from children; the current prose assigns notification time to its parent.",
>       "expected": [
>         {"valid": false, "all_valid": false, "modified": false, "last": "never", "value": null, "delta": null, "peer": true, "children": {"left": {"valid": false, "modified": false, "last": "never", "value": null, "delta": null}, "right": {"valid": false, "modified": false, "last": "never", "value": null, "delta": null}}},
>         {"valid": true, "all_valid": false, "modified": true, "last": 1, "value": {"left": 7}, "delta": {"left": 7}, "peer": true, "children": {"left": {"valid": true, "modified": true, "last": 1, "value": 7, "delta": 7}, "right": {"valid": false, "modified": false, "last": "never", "value": null, "delta": null}}},

### Excerpt 4

[Source, line 78](https://github.com/hhenson/hgraph_spec/blob/b295f39c94403dc4093a1d8c009cdcc6f2549a24/runtime/validation/fixed/reasoned.json#L78).

>         {"valid": true, "all_valid": false, "modified": true, "last": 4, "value": {"right": 9}, "delta": {}, "peer": true, "children": {"left": {"valid": false, "modified": false, "last": "never", "value": null, "delta": null}, "right": {"valid": true, "modified": false, "last": 2, "value": 9, "delta": null}}},
>         {"valid": true, "all_valid": false, "modified": true, "last": 5, "value": {}, "delta": {}, "peer": true, "children": {"left": {"valid": false, "modified": false, "last": "never", "value": null, "delta": null}, "right": {"valid": false, "modified": false, "last": "never", "value": null, "delta": null}}},
>         {"valid": true, "all_valid": false, "modified": true, "last": 6, "value": {"left": 7}, "delta": {"left": 7}, "peer": true, "children": {"left": {"valid": true, "modified": true, "last": 6, "value": 7, "delta": 7}, "right": {"valid": false, "modified": false, "last": "never", "value": null, "delta": null}}},

### Excerpt 5

[Source, line 82](https://github.com/hhenson/hgraph_spec/blob/b295f39c94403dc4093a1d8c009cdcc6f2549a24/runtime/validation/fixed/reasoned.json#L82).

>         {"valid": true, "all_valid": false, "modified": true, "last": 8, "value": {"right": 11}, "delta": {"right": 11}, "peer": true, "children": {"left": {"valid": false, "modified": false, "last": "never", "value": null, "delta": null}, "right": {"valid": true, "modified": true, "last": 8, "value": 11, "delta": 11}}},
>         {"valid": true, "all_valid": false, "modified": false, "last": 8, "value": {"right": 11}, "delta": null, "peer": true, "children": {"left": {"valid": false, "modified": false, "last": "never", "value": null, "delta": null}, "right": {"valid": true, "modified": false, "last": 8, "value": 11, "delta": null}}}

### Excerpt 6

[Source, line 99](https://github.com/hhenson/hgraph_spec/blob/b295f39c94403dc4093a1d8c009cdcc6f2549a24/runtime/validation/fixed/reasoned.json#L99).

>       "reason": "TS-1, TS-4, TS-7: partial publication, invalidation and revalidation preserve fixed positions. Non-peered validity is derived from children; the current prose assigns notification time to its parent.",
>       "expected": [
>         {"valid": false, "all_valid": false, "modified": false, "last": "never", "value": null, "delta": null, "peer": false, "children": {"left": {"valid": false, "modified": false, "last": "never", "value": null, "delta": null}, "right": {"valid": false, "modified": false, "last": "never", "value": null, "delta": null}}},
>         {"valid": true, "all_valid": false, "modified": true, "last": 1, "value": {"left": 7}, "delta": {"left": 7}, "peer": false, "children": {"left": {"valid": true, "modified": true, "last": 1, "value": 7, "delta": 7}, "right": {"valid": false, "modified": false, "last": "never", "value": null, "delta": null}}},

### Excerpt 7

[Source, line 105](https://github.com/hhenson/hgraph_spec/blob/b295f39c94403dc4093a1d8c009cdcc6f2549a24/runtime/validation/fixed/reasoned.json#L105).

>         {"valid": true, "all_valid": false, "modified": true, "last": 4, "value": {"right": 9}, "delta": {}, "peer": false, "children": {"left": {"valid": false, "modified": false, "last": "never", "value": null, "delta": null}, "right": {"valid": true, "modified": false, "last": 2, "value": 9, "delta": null}}},

### Excerpt 8

[Source, line 107](https://github.com/hhenson/hgraph_spec/blob/b295f39c94403dc4093a1d8c009cdcc6f2549a24/runtime/validation/fixed/reasoned.json#L107).

>         {"valid": true, "all_valid": false, "modified": true, "last": 6, "value": {"left": 7}, "delta": {"left": 7}, "peer": false, "children": {"left": {"valid": true, "modified": true, "last": 6, "value": 7, "delta": 7}, "right": {"valid": false, "modified": false, "last": "never", "value": null, "delta": null}}},

### Excerpt 9

[Source, line 109](https://github.com/hhenson/hgraph_spec/blob/b295f39c94403dc4093a1d8c009cdcc6f2549a24/runtime/validation/fixed/reasoned.json#L109).

>         {"valid": true, "all_valid": false, "modified": true, "last": 8, "value": {"right": 11}, "delta": {"right": 11}, "peer": false, "children": {"left": {"valid": false, "modified": false, "last": "never", "value": null, "delta": null}, "right": {"valid": true, "modified": true, "last": 8, "value": 11, "delta": 11}}},
>         {"valid": true, "all_valid": false, "modified": false, "last": 8, "value": {"right": 11}, "delta": null, "peer": false, "children": {"left": {"valid": false, "modified": false, "last": "never", "value": null, "delta": null}, "right": {"valid": true, "modified": false, "last": 8, "value": 11, "delta": null}}}

### Excerpt 10

[Source, line 173](https://github.com/hhenson/hgraph_spec/blob/b295f39c94403dc4093a1d8c009cdcc6f2549a24/runtime/validation/fixed/reasoned.json#L173).

>         {"valid": true, "all_valid": false, "modified": true, "last": 1, "value": [{"left": 7}, null], "delta": {"0": {"left": 7}}, "peer": true, "children": {"0": {"valid": true, "all_valid": false, "modified": true, "last": 1, "value": {"left": 7}, "delta": {"left": 7}, "peer": true, "children": {"left": {"valid": true, "modified": true, "last": 1, "value": 7, "delta": 7}, "right": {"valid": false, "modified": false, "last": "never", "value": null, "delta": null}}}, "1": {"valid": false, "all_valid": false, "modified": false, "last": "never", "value": null, "delta": null, "peer": true, "children": {"left": {"valid": false, "modified": false, "last": "never", "value": null, "delta": null}, "right": {"valid": false, "modified": false, "last": "never", "value": null, "delta": null}}}}},
>         {"valid": true, "all_valid": true, "modified": true, "last": 2, "value": [{"left": 7}, {"left": 9}], "delta": {"1": {"left": 9}}, "peer": true, "children": {"0": {"valid": true, "all_valid": false, "modified": false, "last": 1, "value": {"left": 7}, "delta": null, "peer": true, "children": {"left": {"valid": true, "modified": false, "last": 1, "value": 7, "delta": null}, "right": {"valid": false, "modified": false, "last": "never", "value": null, "delta": null}}}, "1": {"valid": true, "all_valid": false, "modified": true, "last": 2, "value": {"left": 9}, "delta": {"left": 9}, "peer": true, "children": {"left": {"valid": true, "modified": true, "last": 2, "value": 9, "delta": 9}, "right": {"valid": false, "modified": false, "last": "never", "value": null, "delta": null}}}}},
>         {"valid": true, "all_valid": true, "modified": true, "last": 3, "value": [{"left": 7, "right": 8}, {"left": 9}], "delta": {"0": {"right": 8}}, "peer": true, "children": {"0": {"valid": true, "all_valid": true, "modified": true, "last": 3, "value": {"left": 7, "right": 8}, "delta": {"right": 8}, "peer": true, "children": {"left": {"valid": true, "modified": false, "last": 1, "value": 7, "delta": null}, "right": {"valid": true, "modified": true, "last": 3, "value": 8, "delta": 8}}}, "1": {"valid": true, "all_valid": false, "modified": false, "last": 2, "value": {"left": 9}, "delta": null, "peer": true, "children": {"left": {"valid": true, "modified": false, "last": 2, "value": 9, "delta": null}, "right": {"valid": false, "modified": false, "last": "never", "value": null, "delta": null}}}}},
>         {"valid": true, "all_valid": true, "modified": false, "last": 3, "value": [{"left": 7, "right": 8}, {"left": 9}], "delta": null, "peer": true, "children": {"0": {"valid": true, "all_valid": true, "modified": false, "last": 3, "value": {"left": 7, "right": 8}, "delta": null, "peer": true, "children": {"left": {"valid": true, "modified": false, "last": 1, "value": 7, "delta": null}, "right": {"valid": true, "modified": false, "last": 3, "value": 8, "delta": null}}}, "1": {"valid": true, "all_valid": false, "modified": false, "last": 2, "value": {"left": 9}, "delta": null, "peer": true, "children": {"left": {"valid": true, "modified": false, "last": 2, "value": 9, "delta": null}, "right": {"valid": false, "modified": false, "last": "never", "value": null, "delta": null}}}}},

### Excerpt 11

[Source, line 196](https://github.com/hhenson/hgraph_spec/blob/b295f39c94403dc4093a1d8c009cdcc6f2549a24/runtime/validation/fixed/reasoned.json#L196).

>         {"valid": true, "all_valid": false, "modified": true, "last": 1, "value": [{"left": 7}, null], "delta": {"0": {"left": 7}}, "peer": false, "children": {"0": {"valid": true, "all_valid": false, "modified": true, "last": 1, "value": {"left": 7}, "delta": {"left": 7}, "peer": false, "children": {"left": {"valid": true, "modified": true, "last": 1, "value": 7, "delta": 7}, "right": {"valid": false, "modified": false, "last": "never", "value": null, "delta": null}}}, "1": {"valid": false, "all_valid": false, "modified": false, "last": "never", "value": null, "delta": null, "peer": false, "children": {"left": {"valid": false, "modified": false, "last": "never", "value": null, "delta": null}, "right": {"valid": false, "modified": false, "last": "never", "value": null, "delta": null}}}}},
>         {"valid": true, "all_valid": true, "modified": true, "last": 2, "value": [{"left": 7}, {"left": 9}], "delta": {"1": {"left": 9}}, "peer": false, "children": {"0": {"valid": true, "all_valid": false, "modified": false, "last": 1, "value": {"left": 7}, "delta": null, "peer": false, "children": {"left": {"valid": true, "modified": false, "last": 1, "value": 7, "delta": null}, "right": {"valid": false, "modified": false, "last": "never", "value": null, "delta": null}}}, "1": {"valid": true, "all_valid": false, "modified": true, "last": 2, "value": {"left": 9}, "delta": {"left": 9}, "peer": false, "children": {"left": {"valid": true, "modified": true, "last": 2, "value": 9, "delta": 9}, "right": {"valid": false, "modified": false, "last": "never", "value": null, "delta": null}}}}},
>         {"valid": true, "all_valid": true, "modified": true, "last": 3, "value": [{"left": 7, "right": 8}, {"left": 9}], "delta": {"0": {"right": 8}}, "peer": false, "children": {"0": {"valid": true, "all_valid": true, "modified": true, "last": 3, "value": {"left": 7, "right": 8}, "delta": {"right": 8}, "peer": false, "children": {"left": {"valid": true, "modified": false, "last": 1, "value": 7, "delta": null}, "right": {"valid": true, "modified": true, "last": 3, "value": 8, "delta": 8}}}, "1": {"valid": true, "all_valid": false, "modified": false, "last": 2, "value": {"left": 9}, "delta": null, "peer": false, "children": {"left": {"valid": true, "modified": false, "last": 2, "value": 9, "delta": null}, "right": {"valid": false, "modified": false, "last": "never", "value": null, "delta": null}}}}},
>         {"valid": true, "all_valid": true, "modified": false, "last": 3, "value": [{"left": 7, "right": 8}, {"left": 9}], "delta": null, "peer": false, "children": {"0": {"valid": true, "all_valid": true, "modified": false, "last": 3, "value": {"left": 7, "right": 8}, "delta": null, "peer": false, "children": {"left": {"valid": true, "modified": false, "last": 1, "value": 7, "delta": null}, "right": {"valid": true, "modified": false, "last": 3, "value": 8, "delta": null}}}, "1": {"valid": true, "all_valid": false, "modified": false, "last": 2, "value": {"left": 9}, "delta": null, "peer": false, "children": {"left": {"valid": true, "modified": false, "last": 2, "value": 9, "delta": null}, "right": {"valid": false, "modified": false, "last": "never", "value": null, "delta": null}}}}},

### Excerpt 12

[Source, line 219](https://github.com/hhenson/hgraph_spec/blob/b295f39c94403dc4093a1d8c009cdcc6f2549a24/runtime/validation/fixed/reasoned.json#L219).

>         {"valid": true, "all_valid": false, "modified": true, "last": 1, "value": {"left": [7, null]}, "delta": {"left": {"0": 7}}, "peer": true, "children": {"left": {"valid": true, "all_valid": false, "modified": true, "last": 1, "value": [7, null], "delta": {"0": 7}, "peer": true, "children": {"0": {"valid": true, "modified": true, "last": 1, "value": 7, "delta": 7}, "1": {"valid": false, "modified": false, "last": "never", "value": null, "delta": null}}}, "right": {"valid": false, "all_valid": false, "modified": false, "last": "never", "value": null, "delta": null, "peer": true, "children": {"0": {"valid": false, "modified": false, "last": "never", "value": null, "delta": null}, "1": {"valid": false, "modified": false, "last": "never", "value": null, "delta": null}}}}},

### Excerpt 13

[Source, line 242](https://github.com/hhenson/hgraph_spec/blob/b295f39c94403dc4093a1d8c009cdcc6f2549a24/runtime/validation/fixed/reasoned.json#L242).

>         {"valid": true, "all_valid": false, "modified": true, "last": 1, "value": {"left": [7, null]}, "delta": {"left": {"0": 7}}, "peer": false, "children": {"left": {"valid": true, "all_valid": false, "modified": true, "last": 1, "value": [7, null], "delta": {"0": 7}, "peer": false, "children": {"0": {"valid": true, "modified": true, "last": 1, "value": 7, "delta": 7}, "1": {"valid": false, "modified": false, "last": "never", "value": null, "delta": null}}}, "right": {"valid": false, "all_valid": false, "modified": false, "last": "never", "value": null, "delta": null, "peer": false, "children": {"0": {"valid": false, "modified": false, "last": "never", "value": null, "delta": null}, "1": {"valid": false, "modified": false, "last": "never", "value": null, "delta": null}}}}},

### Excerpt 14

[Source, line 265](https://github.com/hhenson/hgraph_spec/blob/b295f39c94403dc4093a1d8c009cdcc6f2549a24/runtime/validation/fixed/reasoned.json#L265).

>         {"valid": true, "all_valid": false, "modified": true, "last": 1, "value": {"left": {"left": 7}}, "delta": {"left": {"left": 7}}, "peer": true, "children": {"left": {"valid": true, "all_valid": false, "modified": true, "last": 1, "value": {"left": 7}, "delta": {"left": 7}, "peer": true, "children": {"left": {"valid": true, "modified": true, "last": 1, "value": 7, "delta": 7}, "right": {"valid": false, "modified": false, "last": "never", "value": null, "delta": null}}}, "right": {"valid": false, "all_valid": false, "modified": false, "last": "never", "value": null, "delta": null, "peer": true, "children": {"left": {"valid": false, "modified": false, "last": "never", "value": null, "delta": null}, "right": {"valid": false, "modified": false, "last": "never", "value": null, "delta": null}}}}},
>         {"valid": true, "all_valid": true, "modified": true, "last": 2, "value": {"left": {"left": 7}, "right": {"left": 9}}, "delta": {"right": {"left": 9}}, "peer": true, "children": {"left": {"valid": true, "all_valid": false, "modified": false, "last": 1, "value": {"left": 7}, "delta": null, "peer": true, "children": {"left": {"valid": true, "modified": false, "last": 1, "value": 7, "delta": null}, "right": {"valid": false, "modified": false, "last": "never", "value": null, "delta": null}}}, "right": {"valid": true, "all_valid": false, "modified": true, "last": 2, "value": {"left": 9}, "delta": {"left": 9}, "peer": true, "children": {"left": {"valid": true, "modified": true, "last": 2, "value": 9, "delta": 9}, "right": {"valid": false, "modified": false, "last": "never", "value": null, "delta": null}}}}},
>         {"valid": true, "all_valid": true, "modified": true, "last": 3, "value": {"left": {"left": 7, "right": 8}, "right": {"left": 9}}, "delta": {"left": {"right": 8}}, "peer": true, "children": {"left": {"valid": true, "all_valid": true, "modified": true, "last": 3, "value": {"left": 7, "right": 8}, "delta": {"right": 8}, "peer": true, "children": {"left": {"valid": true, "modified": false, "last": 1, "value": 7, "delta": null}, "right": {"valid": true, "modified": true, "last": 3, "value": 8, "delta": 8}}}, "right": {"valid": true, "all_valid": false, "modified": false, "last": 2, "value": {"left": 9}, "delta": null, "peer": true, "children": {"left": {"valid": true, "modified": false, "last": 2, "value": 9, "delta": null}, "right": {"valid": false, "modified": false, "last": "never", "value": null, "delta": null}}}}},
>         {"valid": true, "all_valid": true, "modified": false, "last": 3, "value": {"left": {"left": 7, "right": 8}, "right": {"left": 9}}, "delta": null, "peer": true, "children": {"left": {"valid": true, "all_valid": true, "modified": false, "last": 3, "value": {"left": 7, "right": 8}, "delta": null, "peer": true, "children": {"left": {"valid": true, "modified": false, "last": 1, "value": 7, "delta": null}, "right": {"valid": true, "modified": false, "last": 3, "value": 8, "delta": null}}}, "right": {"valid": true, "all_valid": false, "modified": false, "last": 2, "value": {"left": 9}, "delta": null, "peer": true, "children": {"left": {"valid": true, "modified": false, "last": 2, "value": 9, "delta": null}, "right": {"valid": false, "modified": false, "last": "never", "value": null, "delta": null}}}}},

### Excerpt 15

[Source, line 288](https://github.com/hhenson/hgraph_spec/blob/b295f39c94403dc4093a1d8c009cdcc6f2549a24/runtime/validation/fixed/reasoned.json#L288).

>         {"valid": true, "all_valid": false, "modified": true, "last": 1, "value": {"left": {"left": 7}}, "delta": {"left": {"left": 7}}, "peer": false, "children": {"left": {"valid": true, "all_valid": false, "modified": true, "last": 1, "value": {"left": 7}, "delta": {"left": 7}, "peer": false, "children": {"left": {"valid": true, "modified": true, "last": 1, "value": 7, "delta": 7}, "right": {"valid": false, "modified": false, "last": "never", "value": null, "delta": null}}}, "right": {"valid": false, "all_valid": false, "modified": false, "last": "never", "value": null, "delta": null, "peer": false, "children": {"left": {"valid": false, "modified": false, "last": "never", "value": null, "delta": null}, "right": {"valid": false, "modified": false, "last": "never", "value": null, "delta": null}}}}},
>         {"valid": true, "all_valid": true, "modified": true, "last": 2, "value": {"left": {"left": 7}, "right": {"left": 9}}, "delta": {"right": {"left": 9}}, "peer": false, "children": {"left": {"valid": true, "all_valid": false, "modified": false, "last": 1, "value": {"left": 7}, "delta": null, "peer": false, "children": {"left": {"valid": true, "modified": false, "last": 1, "value": 7, "delta": null}, "right": {"valid": false, "modified": false, "last": "never", "value": null, "delta": null}}}, "right": {"valid": true, "all_valid": false, "modified": true, "last": 2, "value": {"left": 9}, "delta": {"left": 9}, "peer": false, "children": {"left": {"valid": true, "modified": true, "last": 2, "value": 9, "delta": 9}, "right": {"valid": false, "modified": false, "last": "never", "value": null, "delta": null}}}}},
>         {"valid": true, "all_valid": true, "modified": true, "last": 3, "value": {"left": {"left": 7, "right": 8}, "right": {"left": 9}}, "delta": {"left": {"right": 8}}, "peer": false, "children": {"left": {"valid": true, "all_valid": true, "modified": true, "last": 3, "value": {"left": 7, "right": 8}, "delta": {"right": 8}, "peer": false, "children": {"left": {"valid": true, "modified": false, "last": 1, "value": 7, "delta": null}, "right": {"valid": true, "modified": true, "last": 3, "value": 8, "delta": 8}}}, "right": {"valid": true, "all_valid": false, "modified": false, "last": 2, "value": {"left": 9}, "delta": null, "peer": false, "children": {"left": {"valid": true, "modified": false, "last": 2, "value": 9, "delta": null}, "right": {"valid": false, "modified": false, "last": "never", "value": null, "delta": null}}}}},
>         {"valid": true, "all_valid": true, "modified": false, "last": 3, "value": {"left": {"left": 7, "right": 8}, "right": {"left": 9}}, "delta": null, "peer": false, "children": {"left": {"valid": true, "all_valid": true, "modified": false, "last": 3, "value": {"left": 7, "right": 8}, "delta": null, "peer": false, "children": {"left": {"valid": true, "modified": false, "last": 1, "value": 7, "delta": null}, "right": {"valid": true, "modified": false, "last": 3, "value": 8, "delta": null}}}, "right": {"valid": true, "all_valid": false, "modified": false, "last": 2, "value": {"left": 9}, "delta": null, "peer": false, "children": {"left": {"valid": true, "modified": false, "last": 2, "value": 9, "delta": null}, "right": {"valid": false, "modified": false, "last": "never", "value": null, "delta": null}}}}},

### Excerpt 16

[Source, line 311](https://github.com/hhenson/hgraph_spec/blob/b295f39c94403dc4093a1d8c009cdcc6f2549a24/runtime/validation/fixed/reasoned.json#L311).

>         {"valid": true, "all_valid": false, "modified": true, "last": 1, "value": [{"left": 7}, null], "delta": {"0": {"left": 7}}, "peer": false, "children": {"0": {"valid": true, "all_valid": false, "modified": true, "last": 1, "value": {"left": 7}, "delta": {"left": 7}, "peer": true, "children": {"left": {"valid": true, "modified": true, "last": 1, "value": 7, "delta": 7}, "right": {"valid": false, "modified": false, "last": "never", "value": null, "delta": null}}}, "1": {"valid": false, "all_valid": false, "modified": false, "last": "never", "value": null, "delta": null, "peer": false, "children": {"left": {"valid": false, "modified": false, "last": "never", "value": null, "delta": null}, "right": {"valid": false, "modified": false, "last": "never", "value": null, "delta": null}}}}},
>         {"valid": true, "all_valid": true, "modified": true, "last": 2, "value": [{"left": 7}, {"left": 9}], "delta": {"1": {"left": 9}}, "peer": false, "children": {"0": {"valid": true, "all_valid": false, "modified": false, "last": 1, "value": {"left": 7}, "delta": null, "peer": true, "children": {"left": {"valid": true, "modified": false, "last": 1, "value": 7, "delta": null}, "right": {"valid": false, "modified": false, "last": "never", "value": null, "delta": null}}}, "1": {"valid": true, "all_valid": false, "modified": true, "last": 2, "value": {"left": 9}, "delta": {"left": 9}, "peer": false, "children": {"left": {"valid": true, "modified": true, "last": 2, "value": 9, "delta": 9}, "right": {"valid": false, "modified": false, "last": "never", "value": null, "delta": null}}}}},
>         {"valid": true, "all_valid": true, "modified": true, "last": 3, "value": [{"left": 7, "right": 8}, {"left": 9}], "delta": {"0": {"right": 8}}, "peer": false, "children": {"0": {"valid": true, "all_valid": true, "modified": true, "last": 3, "value": {"left": 7, "right": 8}, "delta": {"right": 8}, "peer": true, "children": {"left": {"valid": true, "modified": false, "last": 1, "value": 7, "delta": null}, "right": {"valid": true, "modified": true, "last": 3, "value": 8, "delta": 8}}}, "1": {"valid": true, "all_valid": false, "modified": false, "last": 2, "value": {"left": 9}, "delta": null, "peer": false, "children": {"left": {"valid": true, "modified": false, "last": 2, "value": 9, "delta": null}, "right": {"valid": false, "modified": false, "last": "never", "value": null, "delta": null}}}}},
>         {"valid": true, "all_valid": true, "modified": false, "last": 3, "value": [{"left": 7, "right": 8}, {"left": 9}], "delta": null, "peer": false, "children": {"0": {"valid": true, "all_valid": true, "modified": false, "last": 3, "value": {"left": 7, "right": 8}, "delta": null, "peer": true, "children": {"left": {"valid": true, "modified": false, "last": 1, "value": 7, "delta": null}, "right": {"valid": true, "modified": false, "last": 3, "value": 8, "delta": null}}}, "1": {"valid": true, "all_valid": false, "modified": false, "last": 2, "value": {"left": 9}, "delta": null, "peer": false, "children": {"left": {"valid": true, "modified": false, "last": 2, "value": 9, "delta": null}, "right": {"valid": false, "modified": false, "last": "never", "value": null, "delta": null}}}}},

### Excerpt 17

[Source, line 334](https://github.com/hhenson/hgraph_spec/blob/b295f39c94403dc4093a1d8c009cdcc6f2549a24/runtime/validation/fixed/reasoned.json#L334).

>         {"valid": true, "all_valid": false, "modified": true, "last": 1, "value": {"left": [7, null]}, "delta": {"left": {"0": 7}}, "peer": false, "children": {"left": {"valid": true, "all_valid": false, "modified": true, "last": 1, "value": [7, null], "delta": {"0": 7}, "peer": true, "children": {"0": {"valid": true, "modified": true, "last": 1, "value": 7, "delta": 7}, "1": {"valid": false, "modified": false, "last": "never", "value": null, "delta": null}}}, "right": {"valid": false, "all_valid": false, "modified": false, "last": "never", "value": null, "delta": null, "peer": false, "children": {"0": {"valid": false, "modified": false, "last": "never", "value": null, "delta": null}, "1": {"valid": false, "modified": false, "last": "never", "value": null, "delta": null}}}}},

### Excerpt 18

[Source, line 351](https://github.com/hhenson/hgraph_spec/blob/b295f39c94403dc4093a1d8c009cdcc6f2549a24/runtime/validation/fixed/reasoned.json#L351).

>         "empty",
>         "select A",
>         "idle"
>       ],
>       "reason": "TS-14\u2013TS-16: changed binding samples newly selected children; repeated designation does not resample, reference ticks are separate from target ticks. Whole selection samples all children; vector retains unchanged child bindings.",
>       "expected": [
>         {"data": {"valid": false, "all_valid": false, "modified": false, "last": "never", "value": null, "delta": null, "peer": false, "children": {"0": {"valid": false, "modified": false, "last": "never", "value": null, "delta": null}, "1": {"valid": false, "modified": false, "last": "never", "value": null, "delta": null}}}, "a": {"valid": true, "all_valid": true, "modified": true, "last": 0, "value": [7, 9], "delta": {"0": 7, "1": 9}, "peer": true, "children": {"0": {"valid": true, "modified": true, "last": 0, "value": 7, "delta": 7}, "1": {"valid": true, "modified": true, "last": 0, "value": 9, "delta": 9}}}, "b": {"valid": true, "all_valid": true, "modified": true, "last": 0, "value": [20, 30], "delta": {"0": 20, "1": 30}, "peer": true, "children": {"0": {"valid": true, "modified": true, "last": 0, "value": 20, "delta": 20}, "1": {"valid": true, "modified": true, "last": 0, "value": 30, "delta": 30}}}, "ref_valid": true, "ref_modified": true},
>         {"data": {"valid": true, "all_valid": true, "modified": true, "last": 1, "value": [7, 9], "delta": {"0": 7, "1": 9}, "peer": true, "children": {"0": {"valid": true, "modified": true, "last": 1, "value": 7, "delta": 7}, "1": {"valid": true, "modified": true, "last": 1, "value": 9, "delta": 9}}}, "a": {"valid": true, "all_valid": true, "modified": false, "last": 0, "value": [7, 9], "delta": null, "peer": true, "children": {"0": {"valid": true, "modified": false, "last": 0, "value": 7, "delta": null}, "1": {"valid": true, "modified": false, "last": 0, "value": 9, "delta": null}}}, "b": {"valid": true, "all_valid": true, "modified": false, "last": 0, "value": [20, 30], "delta": null, "peer": true, "children": {"0": {"valid": true, "modified": false, "last": 0, "value": 20, "delta": null}, "1": {"valid": true, "modified": false, "last": 0, "value": 30, "delta": null}}}, "ref_valid": true, "ref_modified": true},
>         {"data": {"valid": true, "all_valid": true, "modified": false, "last": 1, "value": [7, 9], "delta": null, "peer": true, "children": {"0": {"valid": true, "modified": false, "last": 1, "value": 7, "delta": null}, "1": {"valid": true, "modified": false, "last": 1, "value": 9, "delta": null}}}, "a": {"valid": true, "all_valid": true, "modified": false, "last": 0, "value": [7, 9], "delta": null, "peer": true, "children": {"0": {"valid": true, "modified": false, "last": 0, "value": 7, "delta": null}, "1": {"valid": true, "modified": false, "last": 0, "value": 9, "delta": null}}}, "b": {"valid": true, "all_valid": true, "modified": false, "last": 0, "value": [20, 30], "delta": null, "peer": true, "children": {"0": {"valid": true, "modified": false, "last": 0, "value": 20, "delta": null}, "1": {"valid": true, "modified": false, "last": 0, "value": 30, "delta": null}}}, "ref_valid": true, "ref_modified": true},

### Excerpt 19

[Source, line 376](https://github.com/hhenson/hgraph_spec/blob/b295f39c94403dc4093a1d8c009cdcc6f2549a24/runtime/validation/fixed/reasoned.json#L376).

>         "select [empty,B.right]",
>         "select A",
>         "idle"
>       ],
>       "reason": "TS-14\u2013TS-16: changed binding samples newly selected children; repeated designation does not resample, reference ticks are separate from target ticks. Whole selection samples all children; vector retains unchanged child bindings.",
>       "expected": [
>         {"data": {"valid": false, "all_valid": false, "modified": false, "last": "never", "value": null, "delta": null, "peer": false, "children": {"0": {"valid": false, "modified": false, "last": "never", "value": null, "delta": null}, "1": {"valid": false, "modified": false, "last": "never", "value": null, "delta": null}}}, "a": {"valid": true, "all_valid": true, "modified": true, "last": 0, "value": [7, 9], "delta": {"0": 7, "1": 9}, "peer": true, "children": {"0": {"valid": true, "modified": true, "last": 0, "value": 7, "delta": 7}, "1": {"valid": true, "modified": true, "last": 0, "value": 9, "delta": 9}}}, "b": {"valid": true, "all_valid": true, "modified": true, "last": 0, "value": [20, 30], "delta": {"0": 20, "1": 30}, "peer": true, "children": {"0": {"valid": true, "modified": true, "last": 0, "value": 20, "delta": 20}, "1": {"valid": true, "modified": true, "last": 0, "value": 30, "delta": 30}}}, "ref_valid": true, "ref_modified": true},
>         {"data": {"valid": true, "all_valid": true, "modified": true, "last": 1, "value": [7, 9], "delta": {"0": 7, "1": 9}, "peer": true, "children": {"0": {"valid": true, "modified": true, "last": 1, "value": 7, "delta": 7}, "1": {"valid": true, "modified": true, "last": 1, "value": 9, "delta": 9}}}, "a": {"valid": true, "all_valid": true, "modified": false, "last": 0, "value": [7, 9], "delta": null, "peer": true, "children": {"0": {"valid": true, "modified": false, "last": 0, "value": 7, "delta": null}, "1": {"valid": true, "modified": false, "last": 0, "value": 9, "delta": null}}}, "b": {"valid": true, "all_valid": true, "modified": false, "last": 0, "value": [20, 30], "delta": null, "peer": true, "children": {"0": {"valid": true, "modified": false, "last": 0, "value": 20, "delta": null}, "1": {"valid": true, "modified": false, "last": 0, "value": 30, "delta": null}}}, "ref_valid": true, "ref_modified": true},
>         {"data": {"valid": true, "all_valid": true, "modified": false, "last": 1, "value": [7, 9], "delta": null, "peer": true, "children": {"0": {"valid": true, "modified": false, "last": 1, "value": 7, "delta": null}, "1": {"valid": true, "modified": false, "last": 1, "value": 9, "delta": null}}}, "a": {"valid": true, "all_valid": true, "modified": false, "last": 0, "value": [7, 9], "delta": null, "peer": true, "children": {"0": {"valid": true, "modified": false, "last": 0, "value": 7, "delta": null}, "1": {"valid": true, "modified": false, "last": 0, "value": 9, "delta": null}}}, "b": {"valid": true, "all_valid": true, "modified": false, "last": 0, "value": [20, 30], "delta": null, "peer": true, "children": {"0": {"valid": true, "modified": false, "last": 0, "value": 20, "delta": null}, "1": {"valid": true, "modified": false, "last": 0, "value": 30, "delta": null}}}, "ref_valid": true, "ref_modified": true},

### Excerpt 20

[Source, line 388](https://github.com/hhenson/hgraph_spec/blob/b295f39c94403dc4093a1d8c009cdcc6f2549a24/runtime/validation/fixed/reasoned.json#L388).

>         {"data": {"valid": true, "all_valid": false, "modified": true, "last": 6, "value": [null, 31], "delta": {}, "peer": false, "children": {"0": {"valid": false, "modified": false, "last": "never", "value": null, "delta": null}, "1": {"valid": true, "modified": false, "last": 5, "value": 31, "delta": null}}}, "a": {"valid": true, "all_valid": true, "modified": false, "last": 3, "value": [8, 9], "delta": null, "peer": true, "children": {"0": {"valid": true, "modified": false, "last": 3, "value": 8, "delta": null}, "1": {"valid": true, "modified": false, "last": 0, "value": 9, "delta": null}}}, "b": {"valid": true, "all_valid": true, "modified": false, "last": 5, "value": [20, 31], "delta": null, "peer": true, "children": {"0": {"valid": true, "modified": false, "last": 0, "value": 20, "delta": null}, "1": {"valid": true, "modified": false, "last": 5, "value": 31, "delta": null}}}, "ref_valid": true, "ref_modified": true},

### Excerpt 21

[Source, line 401](https://github.com/hhenson/hgraph_spec/blob/b295f39c94403dc4093a1d8c009cdcc6f2549a24/runtime/validation/fixed/reasoned.json#L401).

>         "empty",
>         "select A",
>         "idle"
>       ],
>       "reason": "TS-14\u2013TS-16: changed binding samples newly selected children; repeated designation does not resample, reference ticks are separate from target ticks. Whole selection samples all children; vector retains unchanged child bindings.",
>       "expected": [
>         {"data": {"valid": false, "all_valid": false, "modified": false, "last": "never", "value": null, "delta": null, "peer": false, "children": {"left": {"valid": false, "modified": false, "last": "never", "value": null, "delta": null}, "right": {"valid": false, "modified": false, "last": "never", "value": null, "delta": null}}}, "a": {"valid": true, "all_valid": true, "modified": true, "last": 0, "value": {"left": 7, "right": 9}, "delta": {"left": 7, "right": 9}, "peer": true, "children": {"left": {"valid": true, "modified": true, "last": 0, "value": 7, "delta": 7}, "right": {"valid": true, "modified": true, "last": 0, "value": 9, "delta": 9}}}, "b": {"valid": true, "all_valid": true, "modified": true, "last": 0, "value": {"left": 20, "right": 30}, "delta": {"left": 20, "right": 30}, "peer": true, "children": {"left": {"valid": true, "modified": true, "last": 0, "value": 20, "delta": 20}, "right": {"valid": true, "modified": true, "last": 0, "value": 30, "delta": 30}}}, "ref_valid": true, "ref_modified": true},
>         {"data": {"valid": true, "all_valid": true, "modified": true, "last": 1, "value": {"left": 7, "right": 9}, "delta": {"left": 7, "right": 9}, "peer": true, "children": {"left": {"valid": true, "modified": true, "last": 1, "value": 7, "delta": 7}, "right": {"valid": true, "modified": true, "last": 1, "value": 9, "delta": 9}}}, "a": {"valid": true, "all_valid": true, "modified": false, "last": 0, "value": {"left": 7, "right": 9}, "delta": null, "peer": true, "children": {"left": {"valid": true, "modified": false, "last": 0, "value": 7, "delta": null}, "right": {"valid": true, "modified": false, "last": 0, "value": 9, "delta": null}}}, "b": {"valid": true, "all_valid": true, "modified": false, "last": 0, "value": {"left": 20, "right": 30}, "delta": null, "peer": true, "children": {"left": {"valid": true, "modified": false, "last": 0, "value": 20, "delta": null}, "right": {"valid": true, "modified": false, "last": 0, "value": 30, "delta": null}}}, "ref_valid": true, "ref_modified": true},
>         {"data": {"valid": true, "all_valid": true, "modified": false, "last": 1, "value": {"left": 7, "right": 9}, "delta": null, "peer": true, "children": {"left": {"valid": true, "modified": false, "last": 1, "value": 7, "delta": null}, "right": {"valid": true, "modified": false, "last": 1, "value": 9, "delta": null}}}, "a": {"valid": true, "all_valid": true, "modified": false, "last": 0, "value": {"left": 7, "right": 9}, "delta": null, "peer": true, "children": {"left": {"valid": true, "modified": false, "last": 0, "value": 7, "delta": null}, "right": {"valid": true, "modified": false, "last": 0, "value": 9, "delta": null}}}, "b": {"valid": true, "all_valid": true, "modified": false, "last": 0, "value": {"left": 20, "right": 30}, "delta": null, "peer": true, "children": {"left": {"valid": true, "modified": false, "last": 0, "value": 20, "delta": null}, "right": {"valid": true, "modified": false, "last": 0, "value": 30, "delta": null}}}, "ref_valid": true, "ref_modified": true},

### Excerpt 22

[Source, line 426](https://github.com/hhenson/hgraph_spec/blob/b295f39c94403dc4093a1d8c009cdcc6f2549a24/runtime/validation/fixed/reasoned.json#L426).

>         "select [empty,B.right]",
>         "select A",
>         "idle"
>       ],
>       "reason": "TS-14\u2013TS-16: changed binding samples newly selected children; repeated designation does not resample, reference ticks are separate from target ticks. Whole selection samples all children; vector retains unchanged child bindings.",
>       "expected": [
>         {"data": {"valid": false, "all_valid": false, "modified": false, "last": "never", "value": null, "delta": null, "peer": false, "children": {"left": {"valid": false, "modified": false, "last": "never", "value": null, "delta": null}, "right": {"valid": false, "modified": false, "last": "never", "value": null, "delta": null}}}, "a": {"valid": true, "all_valid": true, "modified": true, "last": 0, "value": {"left": 7, "right": 9}, "delta": {"left": 7, "right": 9}, "peer": true, "children": {"left": {"valid": true, "modified": true, "last": 0, "value": 7, "delta": 7}, "right": {"valid": true, "modified": true, "last": 0, "value": 9, "delta": 9}}}, "b": {"valid": true, "all_valid": true, "modified": true, "last": 0, "value": {"left": 20, "right": 30}, "delta": {"left": 20, "right": 30}, "peer": true, "children": {"left": {"valid": true, "modified": true, "last": 0, "value": 20, "delta": 20}, "right": {"valid": true, "modified": true, "last": 0, "value": 30, "delta": 30}}}, "ref_valid": true, "ref_modified": true},
>         {"data": {"valid": true, "all_valid": true, "modified": true, "last": 1, "value": {"left": 7, "right": 9}, "delta": {"left": 7, "right": 9}, "peer": true, "children": {"left": {"valid": true, "modified": true, "last": 1, "value": 7, "delta": 7}, "right": {"valid": true, "modified": true, "last": 1, "value": 9, "delta": 9}}}, "a": {"valid": true, "all_valid": true, "modified": false, "last": 0, "value": {"left": 7, "right": 9}, "delta": null, "peer": true, "children": {"left": {"valid": true, "modified": false, "last": 0, "value": 7, "delta": null}, "right": {"valid": true, "modified": false, "last": 0, "value": 9, "delta": null}}}, "b": {"valid": true, "all_valid": true, "modified": false, "last": 0, "value": {"left": 20, "right": 30}, "delta": null, "peer": true, "children": {"left": {"valid": true, "modified": false, "last": 0, "value": 20, "delta": null}, "right": {"valid": true, "modified": false, "last": 0, "value": 30, "delta": null}}}, "ref_valid": true, "ref_modified": true},
>         {"data": {"valid": true, "all_valid": true, "modified": false, "last": 1, "value": {"left": 7, "right": 9}, "delta": null, "peer": true, "children": {"left": {"valid": true, "modified": false, "last": 1, "value": 7, "delta": null}, "right": {"valid": true, "modified": false, "last": 1, "value": 9, "delta": null}}}, "a": {"valid": true, "all_valid": true, "modified": false, "last": 0, "value": {"left": 7, "right": 9}, "delta": null, "peer": true, "children": {"left": {"valid": true, "modified": false, "last": 0, "value": 7, "delta": null}, "right": {"valid": true, "modified": false, "last": 0, "value": 9, "delta": null}}}, "b": {"valid": true, "all_valid": true, "modified": false, "last": 0, "value": {"left": 20, "right": 30}, "delta": null, "peer": true, "children": {"left": {"valid": true, "modified": false, "last": 0, "value": 20, "delta": null}, "right": {"valid": true, "modified": false, "last": 0, "value": 30, "delta": null}}}, "ref_valid": true, "ref_modified": true},

### Excerpt 23

[Source, line 438](https://github.com/hhenson/hgraph_spec/blob/b295f39c94403dc4093a1d8c009cdcc6f2549a24/runtime/validation/fixed/reasoned.json#L438).

>         {"data": {"valid": true, "all_valid": false, "modified": true, "last": 6, "value": {"right": 31}, "delta": {}, "peer": false, "children": {"left": {"valid": false, "modified": false, "last": "never", "value": null, "delta": null}, "right": {"valid": true, "modified": false, "last": 5, "value": 31, "delta": null}}}, "a": {"valid": true, "all_valid": true, "modified": false, "last": 3, "value": {"left": 8, "right": 9}, "delta": null, "peer": true, "children": {"left": {"valid": true, "modified": false, "last": 3, "value": 8, "delta": null}, "right": {"valid": true, "modified": false, "last": 0, "value": 9, "delta": null}}}, "b": {"valid": true, "all_valid": true, "modified": false, "last": 5, "value": {"left": 20, "right": 31}, "delta": null, "peer": true, "children": {"left": {"valid": true, "modified": false, "last": 0, "value": 20, "delta": null}, "right": {"valid": true, "modified": false, "last": 5, "value": 31, "delta": null}}}, "ref_valid": true, "ref_modified": true},

### Excerpt 24

[Source, line 476](https://github.com/hhenson/hgraph_spec/blob/b295f39c94403dc4093a1d8c009cdcc6f2549a24/runtime/validation/fixed/reasoned.json#L476).

>         null,
>         {"valid": true, "all_valid": false, "modified": true, "last": 1, "value": {"left": 7}, "delta": {"left": 7}, "peer": false, "children": {"left": {"valid": true, "modified": true, "last": 1, "value": 7, "delta": 7}, "right": {"valid": false, "modified": false, "last": "never", "value": null, "delta": null}}},

### Excerpt 25

[Source, line 499](https://github.com/hhenson/hgraph_spec/blob/b295f39c94403dc4093a1d8c009cdcc6f2549a24/runtime/validation/fixed/reasoned.json#L499).

>         {"valid": true, "all_valid": true, "modified": true, "last": 1, "value": [{"left": 7}, {"left": 9}], "delta": {"0": {"left": 7}, "1": {"left": 9}}, "peer": true, "children": {"0": {"valid": true, "all_valid": false, "modified": true, "last": 1, "value": {"left": 7}, "delta": {"left": 7}, "peer": true, "children": {"left": {"valid": true, "modified": true, "last": 1, "value": 7, "delta": 7}, "right": {"valid": false, "modified": false, "last": "never", "value": null, "delta": null}}}, "1": {"valid": true, "all_valid": false, "modified": true, "last": 1, "value": {"left": 9}, "delta": {"left": 9}, "peer": true, "children": {"left": {"valid": true, "modified": true, "last": 1, "value": 9, "delta": 9}, "right": {"valid": false, "modified": false, "last": "never", "value": null, "delta": null}}}}},
>         {"valid": true, "all_valid": true, "modified": false, "last": 1, "value": [{"left": 7}, {"left": 9}], "delta": null, "peer": true, "children": {"0": {"valid": true, "all_valid": false, "modified": false, "last": 1, "value": {"left": 7}, "delta": null, "peer": true, "children": {"left": {"valid": true, "modified": false, "last": 1, "value": 7, "delta": null}, "right": {"valid": false, "modified": false, "last": "never", "value": null, "delta": null}}}, "1": {"valid": true, "all_valid": false, "modified": false, "last": 1, "value": {"left": 9}, "delta": null, "peer": true, "children": {"left": {"valid": true, "modified": false, "last": 1, "value": 9, "delta": null}, "right": {"valid": false, "modified": false, "last": "never", "value": null, "delta": null}}}}},
>         {"valid": true, "all_valid": true, "modified": true, "last": 3, "value": [{"left": 7, "right": 8}, {"left": 9}], "delta": {"0": {"right": 8}}, "peer": true, "children": {"0": {"valid": true, "all_valid": true, "modified": true, "last": 3, "value": {"left": 7, "right": 8}, "delta": {"right": 8}, "peer": true, "children": {"left": {"valid": true, "modified": false, "last": 1, "value": 7, "delta": null}, "right": {"valid": true, "modified": true, "last": 3, "value": 8, "delta": 8}}}, "1": {"valid": true, "all_valid": false, "modified": false, "last": 1, "value": {"left": 9}, "delta": null, "peer": true, "children": {"left": {"valid": true, "modified": false, "last": 1, "value": 9, "delta": null}, "right": {"valid": false, "modified": false, "last": "never", "value": null, "delta": null}}}}},

### Excerpt 26

[Source, line 503](https://github.com/hhenson/hgraph_spec/blob/b295f39c94403dc4093a1d8c009cdcc6f2549a24/runtime/validation/fixed/reasoned.json#L503).

>         {"valid": true, "all_valid": true, "modified": true, "last": 5, "value": [{"left": 20, "right": 21}, {"left": 30}], "delta": {"1": {"left": 30}}, "peer": true, "children": {"0": {"valid": true, "all_valid": true, "modified": false, "last": 4, "value": {"left": 20, "right": 21}, "delta": null, "peer": true, "children": {"left": {"valid": true, "modified": false, "last": 4, "value": 20, "delta": null}, "right": {"valid": true, "modified": false, "last": 4, "value": 21, "delta": null}}}, "1": {"valid": true, "all_valid": false, "modified": true, "last": 5, "value": {"left": 30}, "delta": {"left": 30}, "peer": true, "children": {"left": {"valid": true, "modified": true, "last": 5, "value": 30, "delta": 30}, "right": {"valid": false, "modified": false, "last": "never", "value": null, "delta": null}}}}},

### Excerpt 27

[Source, line 505](https://github.com/hhenson/hgraph_spec/blob/b295f39c94403dc4093a1d8c009cdcc6f2549a24/runtime/validation/fixed/reasoned.json#L505).

>         {"valid": true, "all_valid": true, "modified": true, "last": 7, "value": [{"left": 7, "right": 8}, {"left": 9}], "delta": {"0": {"left": 7, "right": 8}, "1": {"left": 9}}, "peer": true, "children": {"0": {"valid": true, "all_valid": true, "modified": true, "last": 7, "value": {"left": 7, "right": 8}, "delta": {"left": 7, "right": 8}, "peer": true, "children": {"left": {"valid": true, "modified": true, "last": 7, "value": 7, "delta": 7}, "right": {"valid": true, "modified": true, "last": 7, "value": 8, "delta": 8}}}, "1": {"valid": true, "all_valid": false, "modified": true, "last": 7, "value": {"left": 9}, "delta": {"left": 9}, "peer": true, "children": {"left": {"valid": true, "modified": true, "last": 7, "value": 9, "delta": 9}, "right": {"valid": false, "modified": false, "last": "never", "value": null, "delta": null}}}}},
>         {"valid": true, "all_valid": true, "modified": false, "last": 7, "value": [{"left": 7, "right": 8}, {"left": 9}], "delta": null, "peer": true, "children": {"0": {"valid": true, "all_valid": true, "modified": false, "last": 7, "value": {"left": 7, "right": 8}, "delta": null, "peer": true, "children": {"left": {"valid": true, "modified": false, "last": 7, "value": 7, "delta": null}, "right": {"valid": true, "modified": false, "last": 7, "value": 8, "delta": null}}}, "1": {"valid": true, "all_valid": false, "modified": false, "last": 7, "value": {"left": 9}, "delta": null, "peer": true, "children": {"left": {"valid": true, "modified": false, "last": 7, "value": 9, "delta": null}, "right": {"valid": false, "modified": false, "last": "never", "value": null, "delta": null}}}}}

### Excerpt 28

[Source, line 527](https://github.com/hhenson/hgraph_spec/blob/b295f39c94403dc4093a1d8c009cdcc6f2549a24/runtime/validation/fixed/reasoned.json#L527).

>         {"valid": true, "all_valid": false, "modified": true, "last": 4, "value": {"left": [20, 21]}, "delta": {"left": {"0": 20, "1": 21}}, "peer": true, "children": {"left": {"valid": true, "all_valid": true, "modified": true, "last": 4, "value": [20, 21], "delta": {"0": 20, "1": 21}, "peer": true, "children": {"0": {"valid": true, "modified": true, "last": 4, "value": 20, "delta": 20}, "1": {"valid": true, "modified": true, "last": 4, "value": 21, "delta": 21}}}, "right": {"valid": false, "all_valid": false, "modified": false, "last": "never", "value": null, "delta": null, "peer": true, "children": {"0": {"valid": false, "modified": false, "last": "never", "value": null, "delta": null}, "1": {"valid": false, "modified": false, "last": "never", "value": null, "delta": null}}}}},

### Excerpt 29

[Source, line 543](https://github.com/hhenson/hgraph_spec/blob/b295f39c94403dc4093a1d8c009cdcc6f2549a24/runtime/validation/fixed/reasoned.json#L543).

>       ],
>       "expected": [
>         {"valid": false, "all_valid": false, "modified": false, "last": "never", "value": null, "delta": null, "peer": true, "children": {"left": {"valid": false, "modified": false, "last": "never", "value": null, "delta": null}, "right": {"valid": false, "modified": false, "last": "never", "value": null, "delta": null}}},
>         {"valid": true, "all_valid": false, "modified": true, "last": 1, "value": {"left": 7}, "delta": {"left": 7}, "peer": true, "children": {"left": {"valid": true, "modified": true, "last": 1, "value": 7, "delta": 7}, "right": {"valid": false, "modified": false, "last": "never", "value": null, "delta": null}}},

### Excerpt 30

[Source, line 562](https://github.com/hhenson/hgraph_spec/blob/b295f39c94403dc4093a1d8c009cdcc6f2549a24/runtime/validation/fixed/reasoned.json#L562).

>       ],
>       "expected": [
>         {"valid": false, "all_valid": false, "modified": false, "last": "never", "value": null, "delta": null, "peer": false, "children": {"left": {"valid": false, "modified": false, "last": "never", "value": null, "delta": null}, "right": {"valid": false, "modified": false, "last": "never", "value": null, "delta": null}}},
>         {"valid": true, "all_valid": false, "modified": true, "last": 1, "value": {"left": 7}, "delta": {"left": 7}, "peer": false, "children": {"left": {"valid": true, "modified": true, "last": 1, "value": 7, "delta": 7}, "right": {"valid": false, "modified": false, "last": "never", "value": null, "delta": null}}},

### Excerpt 31

[Source, line 583](https://github.com/hhenson/hgraph_spec/blob/b295f39c94403dc4093a1d8c009cdcc6f2549a24/runtime/validation/fixed/reasoned.json#L583).

>         {"valid": true, "all_valid": true, "modified": true, "last": 0, "keys": ["X"], "added": ["X"], "removed": [], "children": {"X": {"valid": true, "all_valid": false, "modified": true, "last": 0, "value": [{"left": 7}, null], "delta": {"0": {"left": 7}}, "children": {"0": {"valid": true, "all_valid": false, "modified": true, "last": 0, "value": {"left": 7}, "delta": {"left": 7}, "children": {"left": {"valid": true, "modified": true, "last": 0, "value": 7, "delta": 7}, "right": {"valid": false, "modified": false, "last": "never", "value": null, "delta": null}}}, "1": {"valid": false, "all_valid": false, "modified": false, "last": "never", "value": null, "delta": null, "children": {"left": {"valid": false, "modified": false, "last": "never", "value": null, "delta": null}, "right": {"valid": false, "modified": false, "last": "never", "value": null, "delta": null}}}}}}, "retired": {}, "delta": {"X": {"0": {"left": 7}}}},
>         {"valid": true, "all_valid": true, "modified": true, "last": 1, "keys": ["X"], "added": [], "removed": [], "children": {"X": {"valid": true, "all_valid": true, "modified": true, "last": 1, "value": [{"left": 7}, {"left": 9}], "delta": {"1": {"left": 9}}, "children": {"0": {"valid": true, "all_valid": false, "modified": false, "last": 0, "value": {"left": 7}, "delta": null, "children": {"left": {"valid": true, "modified": false, "last": 0, "value": 7, "delta": null}, "right": {"valid": false, "modified": false, "last": "never", "value": null, "delta": null}}}, "1": {"valid": true, "all_valid": false, "modified": true, "last": 1, "value": {"left": 9}, "delta": {"left": 9}, "children": {"left": {"valid": true, "modified": true, "last": 1, "value": 9, "delta": 9}, "right": {"valid": false, "modified": false, "last": "never", "value": null, "delta": null}}}}}}, "retired": {}, "delta": {"X": {"1": {"left": 9}}}},
>         {"valid": true, "all_valid": true, "modified": true, "last": 2, "keys": [], "added": [], "removed": ["X"], "children": {}, "retired": {"X": {"valid": true, "all_valid": true, "modified": false, "last": 1, "value": [{"left": 7}, {"left": 9}], "delta": null, "children": {"0": {"valid": true, "all_valid": false, "modified": false, "last": 0, "value": {"left": 7}, "delta": null, "children": {"left": {"valid": true, "modified": false, "last": 0, "value": 7, "delta": null}, "right": {"valid": false, "modified": false, "last": "never", "value": null, "delta": null}}}, "1": {"valid": true, "all_valid": false, "modified": false, "last": 1, "value": {"left": 9}, "delta": null, "children": {"left": {"valid": true, "modified": false, "last": 1, "value": 9, "delta": null}, "right": {"valid": false, "modified": false, "last": "never", "value": null, "delta": null}}}}}}, "delta": {"X": {"$remove": true}}},

### Excerpt 32

[Source, line 587](https://github.com/hhenson/hgraph_spec/blob/b295f39c94403dc4093a1d8c009cdcc6f2549a24/runtime/validation/fixed/reasoned.json#L587).

>         {"valid": true, "all_valid": true, "modified": true, "last": 4, "keys": ["X"], "added": ["X"], "removed": [], "children": {"X": {"valid": true, "all_valid": false, "modified": true, "last": 4, "value": [{"left": 11}, null], "delta": {"0": {"left": 11}}, "children": {"0": {"valid": true, "all_valid": false, "modified": true, "last": 4, "value": {"left": 11}, "delta": {"left": 11}, "children": {"left": {"valid": true, "modified": true, "last": 4, "value": 11, "delta": 11}, "right": {"valid": false, "modified": false, "last": "never", "value": null, "delta": null}}}, "1": {"valid": false, "all_valid": false, "modified": false, "last": "never", "value": null, "delta": null, "children": {"left": {"valid": false, "modified": false, "last": "never", "value": null, "delta": null}, "right": {"valid": false, "modified": false, "last": "never", "value": null, "delta": null}}}}}}, "retired": {}, "delta": {"X": {"0": {"left": 11}}}},
>         {"valid": true, "all_valid": true, "modified": false, "last": 4, "keys": ["X"], "added": [], "removed": [], "children": {"X": {"valid": true, "all_valid": false, "modified": false, "last": 4, "value": [{"left": 11}, null], "delta": null, "children": {"0": {"valid": true, "all_valid": false, "modified": false, "last": 4, "value": {"left": 11}, "delta": null, "children": {"left": {"valid": true, "modified": false, "last": 4, "value": 11, "delta": null}, "right": {"valid": false, "modified": false, "last": "never", "value": null, "delta": null}}}, "1": {"valid": false, "all_valid": false, "modified": false, "last": "never", "value": null, "delta": null, "children": {"left": {"valid": false, "modified": false, "last": "never", "value": null, "delta": null}, "right": {"valid": false, "modified": false, "last": "never", "value": null, "delta": null}}}}}}, "retired": {}, "delta": null}

### Excerpt 33

[Source, line 602](https://github.com/hhenson/hgraph_spec/blob/b295f39c94403dc4093a1d8c009cdcc6f2549a24/runtime/validation/fixed/reasoned.json#L602).

>         {"valid": true, "all_valid": true, "modified": true, "last": 0, "keys": ["X"], "added": ["X"], "removed": [], "children": {"X": {"valid": true, "all_valid": false, "modified": true, "last": 0, "value": {"left": [7, null]}, "delta": {"left": {"0": 7}}, "children": {"left": {"valid": true, "all_valid": false, "modified": true, "last": 0, "value": [7, null], "delta": {"0": 7}, "children": {"0": {"valid": true, "modified": true, "last": 0, "value": 7, "delta": 7}, "1": {"valid": false, "modified": false, "last": "never", "value": null, "delta": null}}}, "right": {"valid": false, "all_valid": false, "modified": false, "last": "never", "value": null, "delta": null, "children": {"0": {"valid": false, "modified": false, "last": "never", "value": null, "delta": null}, "1": {"valid": false, "modified": false, "last": "never", "value": null, "delta": null}}}}}}, "retired": {}, "delta": {"X": {"left": {"0": 7}}}},

### Excerpt 34

[Source, line 606](https://github.com/hhenson/hgraph_spec/blob/b295f39c94403dc4093a1d8c009cdcc6f2549a24/runtime/validation/fixed/reasoned.json#L606).

>         {"valid": true, "all_valid": true, "modified": true, "last": 4, "keys": ["X"], "added": ["X"], "removed": [], "children": {"X": {"valid": true, "all_valid": false, "modified": true, "last": 4, "value": {"left": [11, null]}, "delta": {"left": {"0": 11}}, "children": {"left": {"valid": true, "all_valid": false, "modified": true, "last": 4, "value": [11, null], "delta": {"0": 11}, "children": {"0": {"valid": true, "modified": true, "last": 4, "value": 11, "delta": 11}, "1": {"valid": false, "modified": false, "last": "never", "value": null, "delta": null}}}, "right": {"valid": false, "all_valid": false, "modified": false, "last": "never", "value": null, "delta": null, "children": {"0": {"valid": false, "modified": false, "last": "never", "value": null, "delta": null}, "1": {"valid": false, "modified": false, "last": "never", "value": null, "delta": null}}}}}}, "retired": {}, "delta": {"X": {"left": {"0": 11}}}},
>         {"valid": true, "all_valid": true, "modified": false, "last": 4, "keys": ["X"], "added": [], "removed": [], "children": {"X": {"valid": true, "all_valid": false, "modified": false, "last": 4, "value": {"left": [11, null]}, "delta": null, "children": {"left": {"valid": true, "all_valid": false, "modified": false, "last": 4, "value": [11, null], "delta": null, "children": {"0": {"valid": true, "modified": false, "last": 4, "value": 11, "delta": null}, "1": {"valid": false, "modified": false, "last": "never", "value": null, "delta": null}}}, "right": {"valid": false, "all_valid": false, "modified": false, "last": "never", "value": null, "delta": null, "children": {"0": {"valid": false, "modified": false, "last": "never", "value": null, "delta": null}, "1": {"valid": false, "modified": false, "last": "never", "value": null, "delta": null}}}}}}, "retired": {}, "delta": null}

### Excerpt 35

[Source, line 763](https://github.com/hhenson/hgraph_spec/blob/b295f39c94403dc4093a1d8c009cdcc6f2549a24/runtime/validation/fixed/reasoned.json#L763).

>         {"valid": true, "all_valid": false, "modified": false, "last": 0, "value": [7, null], "delta": null, "peer": false, "children": {"0": {"valid": true, "modified": false, "last": 0, "value": 7, "delta": null}, "1": {"valid": false, "modified": false, "last": "never", "value": null, "delta": null}}},
>         {"valid": true, "all_valid": false, "modified": false, "last": 0, "value": [7, null], "delta": null, "peer": false, "children": {"0": {"valid": true, "modified": false, "last": 0, "value": 7, "delta": null}, "1": {"valid": false, "modified": false, "last": "never", "value": null, "delta": null}}},

### Excerpt 36

[Source, line 818](https://github.com/hhenson/hgraph_spec/blob/b295f39c94403dc4093a1d8c009cdcc6f2549a24/runtime/validation/fixed/reasoned.json#L818).

>         {"valid": true, "all_valid": false, "modified": true, "last": 0, "value": {"left": 7}, "delta": {"left": 7}, "peer": false, "children": {"left": {"valid": true, "modified": true, "last": 0, "value": 7, "delta": 7}, "right": {"valid": false, "modified": false, "last": "never", "value": null, "delta": null}}},

### Excerpt 37

[Source, line 820](https://github.com/hhenson/hgraph_spec/blob/b295f39c94403dc4093a1d8c009cdcc6f2549a24/runtime/validation/fixed/reasoned.json#L820).

>         {"valid": true, "all_valid": false, "modified": false, "last": 0, "value": {"left": 7}, "delta": null, "peer": false, "children": {"left": {"valid": true, "modified": false, "last": 0, "value": 7, "delta": null}, "right": {"valid": false, "modified": false, "last": "never", "value": null, "delta": null}}},
>         {"valid": true, "all_valid": false, "modified": false, "last": 0, "value": {"left": 7}, "delta": null, "peer": false, "children": {"left": {"valid": true, "modified": false, "last": 0, "value": 7, "delta": null}, "right": {"valid": false, "modified": false, "last": "never", "value": null, "delta": null}}},

### Excerpt 38

[Source, line 837](https://github.com/hhenson/hgraph_spec/blob/b295f39c94403dc4093a1d8c009cdcc6f2549a24/runtime/validation/fixed/reasoned.json#L837).

>         {"valid": true, "all_valid": false, "modified": true, "last": 0, "value": {"left": {"X": 7}}, "delta": {"left": {"X": 7}}, "peer": true, "children": {"left": {"valid": true, "all_valid": true, "modified": true, "last": 0, "value": {"X": 7}, "delta": {"X": 7}, "peer": true, "children": {"X": {"valid": true, "modified": true, "last": 0, "value": 7, "delta": 7}}}, "right": {"valid": false, "all_valid": false, "modified": false, "last": "never", "value": null, "delta": null, "peer": true, "children": {}}}},

### Excerpt 39

[Source, line 856](https://github.com/hhenson/hgraph_spec/blob/b295f39c94403dc4093a1d8c009cdcc6f2549a24/runtime/validation/fixed/reasoned.json#L856).

>         {"valid": true, "all_valid": false, "modified": true, "last": 0, "value": {"left": {"X": 7}}, "delta": {"left": {"X": 7}}, "peer": false, "children": {"left": {"valid": true, "all_valid": true, "modified": true, "last": 0, "value": {"X": 7}, "delta": {"X": 7}, "peer": true, "children": {"X": {"valid": true, "modified": true, "last": 0, "value": 7, "delta": 7}}}, "right": {"valid": false, "all_valid": false, "modified": false, "last": "never", "value": null, "delta": null, "peer": true, "children": {}}}},

## runtime/validation/fixed/decisions.json

### Excerpt 1

[Source, line 12](https://github.com/hhenson/hgraph_spec/blob/b295f39c94403dc4093a1d8c009cdcc6f2549a24/runtime/validation/fixed/decisions.json#L12).

>       {"case": "tsb_owned", "path": "/ticks/1/value", "previous_expected": {"left": 7}, "expected": {"left": 7, "right": null}},
>       {"case": "tsb_owned", "path": "/ticks/4/value", "previous_expected": {"right": 9}, "expected": {"left": null, "right": 9}},
>       {"case": "tsb_owned", "path": "/ticks/5/value", "previous_expected": {}, "expected": {"left": null, "right": null}},
>       {"case": "tsb_owned", "path": "/ticks/6/value", "previous_expected": {"left": 7}, "expected": {"left": 7, "right": null}},
>       {"case": "tsb_owned", "path": "/ticks/8/value", "previous_expected": {"right": 11}, "expected": {"left": null, "right": 11}},
>       {"case": "tsb_owned", "path": "/ticks/9/value", "previous_expected": {"right": 11}, "expected": {"left": null, "right": 11}},
>       {"case": "tsb_assembled", "path": "/ticks/1/value", "previous_expected": {"left": 7}, "expected": {"left": 7, "right": null}},
>       {"case": "tsb_assembled", "path": "/ticks/4/value", "previous_expected": {"right": 9}, "expected": {"left": null, "right": 9}},
>       {"case": "tsb_assembled", "path": "/ticks/6/value", "previous_expected": {"left": 7}, "expected": {"left": 7, "right": null}},
>       {"case": "tsb_assembled", "path": "/ticks/8/value", "previous_expected": {"right": 11}, "expected": {"left": null, "right": 11}},
>       {"case": "tsb_assembled", "path": "/ticks/9/value", "previous_expected": {"right": 11}, "expected": {"left": null, "right": 11}},
>       {"case": "tsl_tsb_owned", "path": "/ticks/1/children/0/value", "previous_expected": {"left": 7}, "expected": {"left": 7, "right": null}},
>       {"case": "tsl_tsb_owned", "path": "/ticks/1/value", "previous_expected": [{"left": 7}, null], "expected": [{"left": 7, "right": null}, null]},
>       {"case": "tsl_tsb_owned", "path": "/ticks/2/children/0/value", "previous_expected": {"left": 7}, "expected": {"left": 7, "right": null}},
>       {"case": "tsl_tsb_owned", "path": "/ticks/2/children/1/value", "previous_expected": {"left": 9}, "expected": {"left": 9, "right": null}},
>       {"case": "tsl_tsb_owned", "path": "/ticks/2/value", "previous_expected": [{"left": 7}, {"left": 9}], "expected": [{"left": 7, "right": null}, {"left": 9, "right": null}]},
>       {"case": "tsl_tsb_owned", "path": "/ticks/3/children/1/value", "previous_expected": {"left": 9}, "expected": {"left": 9, "right": null}},
>       {"case": "tsl_tsb_owned", "path": "/ticks/3/value", "previous_expected": [{"left": 7, "right": 8}, {"left": 9}], "expected": [{"left": 7, "right": 8}, {"left": 9, "right": null}]},
>       {"case": "tsl_tsb_owned", "path": "/ticks/4/children/1/value", "previous_expected": {"left": 9}, "expected": {"left": 9, "right": null}},
>       {"case": "tsl_tsb_owned", "path": "/ticks/4/value", "previous_expected": [{"left": 7, "right": 8}, {"left": 9}], "expected": [{"left": 7, "right": 8}, {"left": 9, "right": null}]},
>       {"case": "tsl_tsb_assembled", "path": "/ticks/1/children/0/value", "previous_expected": {"left": 7}, "expected": {"left": 7, "right": null}},
>       {"case": "tsl_tsb_assembled", "path": "/ticks/1/value", "previous_expected": [{"left": 7}, null], "expected": [{"left": 7, "right": null}, null]},
>       {"case": "tsl_tsb_assembled", "path": "/ticks/2/children/0/value", "previous_expected": {"left": 7}, "expected": {"left": 7, "right": null}},
>       {"case": "tsl_tsb_assembled", "path": "/ticks/2/children/1/value", "previous_expected": {"left": 9}, "expected": {"left": 9, "right": null}},
>       {"case": "tsl_tsb_assembled", "path": "/ticks/2/value", "previous_expected": [{"left": 7}, {"left": 9}], "expected": [{"left": 7, "right": null}, {"left": 9, "right": null}]},
>       {"case": "tsl_tsb_assembled", "path": "/ticks/3/children/1/value", "previous_expected": {"left": 9}, "expected": {"left": 9, "right": null}},
>       {"case": "tsl_tsb_assembled", "path": "/ticks/3/value", "previous_expected": [{"left": 7, "right": 8}, {"left": 9}], "expected": [{"left": 7, "right": 8}, {"left": 9, "right": null}]},
>       {"case": "tsl_tsb_assembled", "path": "/ticks/4/children/1/value", "previous_expected": {"left": 9}, "expected": {"left": 9, "right": null}},
>       {"case": "tsl_tsb_assembled", "path": "/ticks/4/value", "previous_expected": [{"left": 7, "right": 8}, {"left": 9}], "expected": [{"left": 7, "right": 8}, {"left": 9, "right": null}]},
>       {"case": "tsb_tsl_owned", "path": "/ticks/1/value", "previous_expected": {"left": [7, null]}, "expected": {"left": [7, null], "right": null}},
>       {"case": "tsb_tsl_assembled", "path": "/ticks/1/value", "previous_expected": {"left": [7, null]}, "expected": {"left": [7, null], "right": null}},
>       {"case": "tsb_tsb_owned", "path": "/ticks/1/children/left/value", "previous_expected": {"left": 7}, "expected": {"left": 7, "right": null}},
>       {"case": "tsb_tsb_owned", "path": "/ticks/1/value", "previous_expected": {"left": {"left": 7}}, "expected": {"left": {"left": 7, "right": null}, "right": null}},
>       {"case": "tsb_tsb_owned", "path": "/ticks/2/children/left/value", "previous_expected": {"left": 7}, "expected": {"left": 7, "right": null}},
>       {"case": "tsb_tsb_owned", "path": "/ticks/2/children/right/value", "previous_expected": {"left": 9}, "expected": {"left": 9, "right": null}},
>       {"case": "tsb_tsb_owned", "path": "/ticks/2/value", "previous_expected": {"left": {"left": 7}, "right": {"left": 9}}, "expected": {"left": {"left": 7, "right": null}, "right": {"left": 9, "right": null}}},
>       {"case": "tsb_tsb_owned", "path": "/ticks/3/children/right/value", "previous_expected": {"left": 9}, "expected": {"left": 9, "right": null}},
>       {"case": "tsb_tsb_owned", "path": "/ticks/3/value", "previous_expected": {"left": {"left": 7, "right": 8}, "right": {"left": 9}}, "expected": {"left": {"left": 7, "right": 8}, "right": {"left": 9, "right": null}}},
>       {"case": "tsb_tsb_owned", "path": "/ticks/4/children/right/value", "previous_expected": {"left": 9}, "expected": {"left": 9, "right": null}},
>       {"case": "tsb_tsb_owned", "path": "/ticks/4/value", "previous_expected": {"left": {"left": 7, "right": 8}, "right": {"left": 9}}, "expected": {"left": {"left": 7, "right": 8}, "right": {"left": 9, "right": null}}},
>       {"case": "tsb_tsb_assembled", "path": "/ticks/1/children/left/value", "previous_expected": {"left": 7}, "expected": {"left": 7, "right": null}},
>       {"case": "tsb_tsb_assembled", "path": "/ticks/1/value", "previous_expected": {"left": {"left": 7}}, "expected": {"left": {"left": 7, "right": null}, "right": null}},
>       {"case": "tsb_tsb_assembled", "path": "/ticks/2/children/left/value", "previous_expected": {"left": 7}, "expected": {"left": 7, "right": null}},
>       {"case": "tsb_tsb_assembled", "path": "/ticks/2/children/right/value", "previous_expected": {"left": 9}, "expected": {"left": 9, "right": null}},
>       {"case": "tsb_tsb_assembled", "path": "/ticks/2/value", "previous_expected": {"left": {"left": 7}, "right": {"left": 9}}, "expected": {"left": {"left": 7, "right": null}, "right": {"left": 9, "right": null}}},
>       {"case": "tsb_tsb_assembled", "path": "/ticks/3/children/right/value", "previous_expected": {"left": 9}, "expected": {"left": 9, "right": null}},
>       {"case": "tsb_tsb_assembled", "path": "/ticks/3/value", "previous_expected": {"left": {"left": 7, "right": 8}, "right": {"left": 9}}, "expected": {"left": {"left": 7, "right": 8}, "right": {"left": 9, "right": null}}},
>       {"case": "tsb_tsb_assembled", "path": "/ticks/4/children/right/value", "previous_expected": {"left": 9}, "expected": {"left": 9, "right": null}},
>       {"case": "tsb_tsb_assembled", "path": "/ticks/4/value", "previous_expected": {"left": {"left": 7, "right": 8}, "right": {"left": 9}}, "expected": {"left": {"left": 7, "right": 8}, "right": {"left": 9, "right": null}}},
>       {"case": "tsl_tsb_mixed", "path": "/ticks/1/children/0/value", "previous_expected": {"left": 7}, "expected": {"left": 7, "right": null}},
>       {"case": "tsl_tsb_mixed", "path": "/ticks/1/value", "previous_expected": [{"left": 7}, null], "expected": [{"left": 7, "right": null}, null]},
>       {"case": "tsl_tsb_mixed", "path": "/ticks/2/children/0/value", "previous_expected": {"left": 7}, "expected": {"left": 7, "right": null}},
>       {"case": "tsl_tsb_mixed", "path": "/ticks/2/children/1/value", "previous_expected": {"left": 9}, "expected": {"left": 9, "right": null}},
>       {"case": "tsl_tsb_mixed", "path": "/ticks/2/value", "previous_expected": [{"left": 7}, {"left": 9}], "expected": [{"left": 7, "right": null}, {"left": 9, "right": null}]},
>       {"case": "tsl_tsb_mixed", "path": "/ticks/3/children/1/value", "previous_expected": {"left": 9}, "expected": {"left": 9, "right": null}},
>       {"case": "tsl_tsb_mixed", "path": "/ticks/3/value", "previous_expected": [{"left": 7, "right": 8}, {"left": 9}], "expected": [{"left": 7, "right": 8}, {"left": 9, "right": null}]},
>       {"case": "tsl_tsb_mixed", "path": "/ticks/4/children/1/value", "previous_expected": {"left": 9}, "expected": {"left": 9, "right": null}},
>       {"case": "tsl_tsb_mixed", "path": "/ticks/4/value", "previous_expected": [{"left": 7, "right": 8}, {"left": 9}], "expected": [{"left": 7, "right": 8}, {"left": 9, "right": null}]},
>       {"case": "tsb_tsl_mixed", "path": "/ticks/1/value", "previous_expected": {"left": [7, null]}, "expected": {"left": [7, null], "right": null}},
>       {"case": "tsb_ref_items", "path": "/ticks/6/data/value", "previous_expected": {"right": 31}, "expected": {"left": null, "right": 31}},
>       {"case": "tsb_passive", "path": "/ticks/1/value", "previous_expected": {"left": 7}, "expected": {"left": 7, "right": null}},
>       {"case": "tsl_tsb_ref", "path": "/ticks/1/children/0/value", "previous_expected": {"left": 7}, "expected": {"left": 7, "right": null}},
>       {"case": "tsl_tsb_ref", "path": "/ticks/1/children/1/value", "previous_expected": {"left": 9}, "expected": {"left": 9, "right": null}},
>       {"case": "tsl_tsb_ref", "path": "/ticks/1/value", "previous_expected": [{"left": 7}, {"left": 9}], "expected": [{"left": 7, "right": null}, {"left": 9, "right": null}]},
>       {"case": "tsl_tsb_ref", "path": "/ticks/2/children/0/value", "previous_expected": {"left": 7}, "expected": {"left": 7, "right": null}},
>       {"case": "tsl_tsb_ref", "path": "/ticks/2/children/1/value", "previous_expected": {"left": 9}, "expected": {"left": 9, "right": null}},
>       {"case": "tsl_tsb_ref", "path": "/ticks/2/value", "previous_expected": [{"left": 7}, {"left": 9}], "expected": [{"left": 7, "right": null}, {"left": 9, "right": null}]},
>       {"case": "tsl_tsb_ref", "path": "/ticks/3/children/1/value", "previous_expected": {"left": 9}, "expected": {"left": 9, "right": null}},
>       {"case": "tsl_tsb_ref", "path": "/ticks/3/value", "previous_expected": [{"left": 7, "right": 8}, {"left": 9}], "expected": [{"left": 7, "right": 8}, {"left": 9, "right": null}]},
>       {"case": "tsl_tsb_ref", "path": "/ticks/5/children/1/value", "previous_expected": {"left": 30}, "expected": {"left": 30, "right": null}},
>       {"case": "tsl_tsb_ref", "path": "/ticks/5/value", "previous_expected": [{"left": 20, "right": 21}, {"left": 30}], "expected": [{"left": 20, "right": 21}, {"left": 30, "right": null}]},
>       {"case": "tsl_tsb_ref", "path": "/ticks/7/children/1/value", "previous_expected": {"left": 9}, "expected": {"left": 9, "right": null}},
>       {"case": "tsl_tsb_ref", "path": "/ticks/7/value", "previous_expected": [{"left": 7, "right": 8}, {"left": 9}], "expected": [{"left": 7, "right": 8}, {"left": 9, "right": null}]},
>       {"case": "tsl_tsb_ref", "path": "/ticks/8/children/1/value", "previous_expected": {"left": 9}, "expected": {"left": 9, "right": null}},
>       {"case": "tsl_tsb_ref", "path": "/ticks/8/value", "previous_expected": [{"left": 7, "right": 8}, {"left": 9}], "expected": [{"left": 7, "right": 8}, {"left": 9, "right": null}]},
>       {"case": "tsb_tsl_ref", "path": "/ticks/4/value", "previous_expected": {"left": [20, 21]}, "expected": {"left": [20, 21], "right": null}},
>       {"case": "tsb_heterogeneous_owned", "path": "/ticks/1/value", "previous_expected": {"left": 7}, "expected": {"left": 7, "right": null}},
>       {"case": "tsb_heterogeneous_assembled", "path": "/ticks/1/value", "previous_expected": {"left": 7}, "expected": {"left": 7, "right": null}},
>       {"case": "tsd_tsl_tsb", "path": "/ticks/0/children/X/children/0/value", "previous_expected": {"left": 7}, "expected": {"left": 7, "right": null}},
>       {"case": "tsd_tsl_tsb", "path": "/ticks/0/children/X/value", "previous_expected": [{"left": 7}, null], "expected": [{"left": 7, "right": null}, null]},
>       {"case": "tsd_tsl_tsb", "path": "/ticks/1/children/X/children/0/value", "previous_expected": {"left": 7}, "expected": {"left": 7, "right": null}},
>       {"case": "tsd_tsl_tsb", "path": "/ticks/1/children/X/children/1/value", "previous_expected": {"left": 9}, "expected": {"left": 9, "right": null}},
>       {"case": "tsd_tsl_tsb", "path": "/ticks/1/children/X/value", "previous_expected": [{"left": 7}, {"left": 9}], "expected": [{"left": 7, "right": null}, {"left": 9, "right": null}]},
>       {"case": "tsd_tsl_tsb", "path": "/ticks/2/retired/X/children/0/value", "previous_expected": {"left": 7}, "expected": {"left": 7, "right": null}},
>       {"case": "tsd_tsl_tsb", "path": "/ticks/2/retired/X/children/1/value", "previous_expected": {"left": 9}, "expected": {"left": 9, "right": null}},
>       {"case": "tsd_tsl_tsb", "path": "/ticks/2/retired/X/value", "previous_expected": [{"left": 7}, {"left": 9}], "expected": [{"left": 7, "right": null}, {"left": 9, "right": null}]},
>       {"case": "tsd_tsl_tsb", "path": "/ticks/4/children/X/children/0/value", "previous_expected": {"left": 11}, "expected": {"left": 11, "right": null}},
>       {"case": "tsd_tsl_tsb", "path": "/ticks/4/children/X/value", "previous_expected": [{"left": 11}, null], "expected": [{"left": 11, "right": null}, null]},
>       {"case": "tsd_tsl_tsb", "path": "/ticks/5/children/X/children/0/value", "previous_expected": {"left": 11}, "expected": {"left": 11, "right": null}},
>       {"case": "tsd_tsl_tsb", "path": "/ticks/5/children/X/value", "previous_expected": [{"left": 11}, null], "expected": [{"left": 11, "right": null}, null]},
>       {"case": "tsd_tsb_tsl", "path": "/ticks/0/children/X/value", "previous_expected": {"left": [7, null]}, "expected": {"left": [7, null], "right": null}},
>       {"case": "tsd_tsb_tsl", "path": "/ticks/4/children/X/value", "previous_expected": {"left": [11, null]}, "expected": {"left": [11, null], "right": null}},
>       {"case": "tsd_tsb_tsl", "path": "/ticks/5/children/X/value", "previous_expected": {"left": [11, null]}, "expected": {"left": [11, null], "right": null}},
>       {"case": "tsb_latest_invalid", "path": "/ticks/0/value", "previous_expected": {"left": 7}, "expected": {"left": 7, "right": null}},
>       {"case": "tsb_latest_invalid", "path": "/ticks/2/value", "previous_expected": {"left": 7}, "expected": {"left": 7, "right": null}},
>       {"case": "tsb_latest_invalid", "path": "/ticks/3/value", "previous_expected": {"left": 7}, "expected": {"left": 7, "right": null}},
>       {"case": "tsb_dictionary_owned", "path": "/ticks/0/value", "previous_expected": {"left": {"X": 7}}, "expected": {"left": {"X": 7}, "right": null}},
>       {"case": "tsb_dictionary_assembled", "path": "/ticks/0/value", "previous_expected": {"left": {"X": 7}}, "expected": {"left": {"X": 7}, "right": null}}

### Excerpt 2

[Source, line 121](https://github.com/hhenson/hgraph_spec/blob/b295f39c94403dc4093a1d8c009cdcc6f2549a24/runtime/validation/fixed/decisions.json#L121).

>       {"case": "tsl_ref_whole", "path": "/ticks/2/ref_modified", "previous_expected": true, "expected": false},
>       {"case": "tsb_ref_whole", "path": "/ticks/2/ref_modified", "previous_expected": true, "expected": false},
>       {"case": "tsl_ref_items", "path": "/ticks/2/ref_modified", "previous_expected": true, "expected": false},
>       {"case": "tsb_ref_items", "path": "/ticks/2/ref_modified", "previous_expected": true, "expected": false}

### Excerpt 3

[Source, line 137](https://github.com/hhenson/hgraph_spec/blob/b295f39c94403dc4093a1d8c009cdcc6f2549a24/runtime/validation/fixed/decisions.json#L137).

>       {"case": "tsl_owned", "path": "/ticks/7/valid", "previous_expected": false, "expected": false},
>       {"case": "tsl_owned", "path": "/ticks/7/all_valid", "previous_expected": false, "expected": false},
>       {"case": "tsl_owned", "path": "/ticks/7/modified", "previous_expected": false, "expected": false},
>       {"case": "tsl_owned", "path": "/ticks/7/last", "previous_expected": "never", "expected": "never"},
>       {"case": "tsl_owned", "path": "/ticks/7/value", "previous_expected": null, "expected": null},
>       {"case": "tsl_owned", "path": "/ticks/7/delta", "previous_expected": null, "expected": null},
>       {"case": "tsl_owned", "path": "/ticks/7/peer", "previous_expected": true, "expected": true},
>       {"case": "tsl_owned", "path": "/ticks/7/children", "previous_expected": ["0", "1"], "expected": ["0", "1"]},
>       {"case": "tsl_owned", "path": "/ticks/7/children/0/valid", "previous_expected": false, "expected": false},
>       {"case": "tsl_owned", "path": "/ticks/7/children/0/modified", "previous_expected": false, "expected": false},
>       {"case": "tsl_owned", "path": "/ticks/7/children/0/last", "previous_expected": "never", "expected": "never"},
>       {"case": "tsl_owned", "path": "/ticks/7/children/0/value", "previous_expected": null, "expected": null},
>       {"case": "tsl_owned", "path": "/ticks/7/children/0/delta", "previous_expected": null, "expected": null},
>       {"case": "tsl_owned", "path": "/ticks/7/children/1/valid", "previous_expected": false, "expected": false},
>       {"case": "tsl_owned", "path": "/ticks/7/children/1/modified", "previous_expected": false, "expected": false},
>       {"case": "tsl_owned", "path": "/ticks/7/children/1/last", "previous_expected": "never", "expected": "never"},
>       {"case": "tsl_owned", "path": "/ticks/7/children/1/value", "previous_expected": null, "expected": null},
>       {"case": "tsl_owned", "path": "/ticks/7/children/1/delta", "previous_expected": null, "expected": null},
>       {"case": "tsb_owned", "path": "/ticks/7/valid", "previous_expected": false, "expected": false},
>       {"case": "tsb_owned", "path": "/ticks/7/all_valid", "previous_expected": false, "expected": false},
>       {"case": "tsb_owned", "path": "/ticks/7/modified", "previous_expected": false, "expected": false},
>       {"case": "tsb_owned", "path": "/ticks/7/last", "previous_expected": "never", "expected": "never"},
>       {"case": "tsb_owned", "path": "/ticks/7/value", "previous_expected": null, "expected": null},
>       {"case": "tsb_owned", "path": "/ticks/7/delta", "previous_expected": null, "expected": null},
>       {"case": "tsb_owned", "path": "/ticks/7/peer", "previous_expected": true, "expected": true},
>       {"case": "tsb_owned", "path": "/ticks/7/children", "previous_expected": ["left", "right"], "expected": ["left", "right"]},
>       {"case": "tsb_owned", "path": "/ticks/7/children/left/valid", "previous_expected": false, "expected": false},
>       {"case": "tsb_owned", "path": "/ticks/7/children/left/modified", "previous_expected": false, "expected": false},
>       {"case": "tsb_owned", "path": "/ticks/7/children/left/last", "previous_expected": "never", "expected": "never"},
>       {"case": "tsb_owned", "path": "/ticks/7/children/left/value", "previous_expected": null, "expected": null},
>       {"case": "tsb_owned", "path": "/ticks/7/children/left/delta", "previous_expected": null, "expected": null},
>       {"case": "tsb_owned", "path": "/ticks/7/children/right/valid", "previous_expected": false, "expected": false},
>       {"case": "tsb_owned", "path": "/ticks/7/children/right/modified", "previous_expected": false, "expected": false},
>       {"case": "tsb_owned", "path": "/ticks/7/children/right/last", "previous_expected": "never", "expected": "never"},
>       {"case": "tsb_owned", "path": "/ticks/7/children/right/value", "previous_expected": null, "expected": null},
>       {"case": "tsb_owned", "path": "/ticks/7/children/right/delta", "previous_expected": null, "expected": null},
>       {"case": "tsl_tsl_owned_invalidate", "path": "/ticks/7/valid", "previous_expected": false, "expected": false},
>       {"case": "tsl_tsl_owned_invalidate", "path": "/ticks/7/all_valid", "previous_expected": false, "expected": false},
>       {"case": "tsl_tsl_owned_invalidate", "path": "/ticks/7/modified", "previous_expected": false, "expected": false},
>       {"case": "tsl_tsl_owned_invalidate", "path": "/ticks/7/last", "previous_expected": "never", "expected": "never"},
>       {"case": "tsl_tsl_owned_invalidate", "path": "/ticks/7/value", "previous_expected": null, "expected": null},
>       {"case": "tsl_tsl_owned_invalidate", "path": "/ticks/7/delta", "previous_expected": null, "expected": null},
>       {"case": "tsl_tsl_owned_invalidate", "path": "/ticks/7/peer", "previous_expected": true, "expected": true},
>       {"case": "tsl_tsl_owned_invalidate", "path": "/ticks/7/children", "previous_expected": ["0", "1"], "expected": ["0", "1"]},
>       {"case": "tsl_tsl_owned_invalidate", "path": "/ticks/7/children/0/valid", "previous_expected": false, "expected": false},
>       {"case": "tsl_tsl_owned_invalidate", "path": "/ticks/7/children/0/all_valid", "previous_expected": false, "expected": false},
>       {"case": "tsl_tsl_owned_invalidate", "path": "/ticks/7/children/0/modified", "previous_expected": false, "expected": false},
>       {"case": "tsl_tsl_owned_invalidate", "path": "/ticks/7/children/0/last", "previous_expected": "never", "expected": "never"},
>       {"case": "tsl_tsl_owned_invalidate", "path": "/ticks/7/children/0/value", "previous_expected": null, "expected": null},
>       {"case": "tsl_tsl_owned_invalidate", "path": "/ticks/7/children/0/delta", "previous_expected": null, "expected": null},
>       {"case": "tsl_tsl_owned_invalidate", "path": "/ticks/7/children/0/peer", "previous_expected": true, "expected": true},
>       {"case": "tsl_tsl_owned_invalidate", "path": "/ticks/7/children/0/children", "previous_expected": ["0", "1"], "expected": ["0", "1"]},
>       {"case": "tsl_tsl_owned_invalidate", "path": "/ticks/7/children/0/children/0/valid", "previous_expected": false, "expected": false},
>       {"case": "tsl_tsl_owned_invalidate", "path": "/ticks/7/children/0/children/0/modified", "previous_expected": false, "expected": false},
>       {"case": "tsl_tsl_owned_invalidate", "path": "/ticks/7/children/0/children/0/last", "previous_expected": "never", "expected": "never"},
>       {"case": "tsl_tsl_owned_invalidate", "path": "/ticks/7/children/0/children/0/value", "previous_expected": null, "expected": null},
>       {"case": "tsl_tsl_owned_invalidate", "path": "/ticks/7/children/0/children/0/delta", "previous_expected": null, "expected": null},
>       {"case": "tsl_tsl_owned_invalidate", "path": "/ticks/7/children/0/children/1/valid", "previous_expected": false, "expected": false},
>       {"case": "tsl_tsl_owned_invalidate", "path": "/ticks/7/children/0/children/1/modified", "previous_expected": false, "expected": false},
>       {"case": "tsl_tsl_owned_invalidate", "path": "/ticks/7/children/0/children/1/last", "previous_expected": "never", "expected": "never"},
>       {"case": "tsl_tsl_owned_invalidate", "path": "/ticks/7/children/0/children/1/value", "previous_expected": null, "expected": null},
>       {"case": "tsl_tsl_owned_invalidate", "path": "/ticks/7/children/0/children/1/delta", "previous_expected": null, "expected": null},
>       {"case": "tsl_tsl_owned_invalidate", "path": "/ticks/7/children/1/valid", "previous_expected": false, "expected": false},
>       {"case": "tsl_tsl_owned_invalidate", "path": "/ticks/7/children/1/all_valid", "previous_expected": false, "expected": false},
>       {"case": "tsl_tsl_owned_invalidate", "path": "/ticks/7/children/1/modified", "previous_expected": false, "expected": false},
>       {"case": "tsl_tsl_owned_invalidate", "path": "/ticks/7/children/1/last", "previous_expected": "never", "expected": "never"},
>       {"case": "tsl_tsl_owned_invalidate", "path": "/ticks/7/children/1/value", "previous_expected": null, "expected": null},
>       {"case": "tsl_tsl_owned_invalidate", "path": "/ticks/7/children/1/delta", "previous_expected": null, "expected": null},
>       {"case": "tsl_tsl_owned_invalidate", "path": "/ticks/7/children/1/peer", "previous_expected": true, "expected": true},
>       {"case": "tsl_tsl_owned_invalidate", "path": "/ticks/7/children/1/children", "previous_expected": ["0", "1"], "expected": ["0", "1"]},
>       {"case": "tsl_tsl_owned_invalidate", "path": "/ticks/7/children/1/children/0/valid", "previous_expected": false, "expected": false},
>       {"case": "tsl_tsl_owned_invalidate", "path": "/ticks/7/children/1/children/0/modified", "previous_expected": false, "expected": false},
>       {"case": "tsl_tsl_owned_invalidate", "path": "/ticks/7/children/1/children/0/last", "previous_expected": "never", "expected": "never"},
>       {"case": "tsl_tsl_owned_invalidate", "path": "/ticks/7/children/1/children/0/value", "previous_expected": null, "expected": null},
>       {"case": "tsl_tsl_owned_invalidate", "path": "/ticks/7/children/1/children/0/delta", "previous_expected": null, "expected": null},
>       {"case": "tsl_tsl_owned_invalidate", "path": "/ticks/7/children/1/children/1/valid", "previous_expected": false, "expected": false},
>       {"case": "tsl_tsl_owned_invalidate", "path": "/ticks/7/children/1/children/1/modified", "previous_expected": false, "expected": false},
>       {"case": "tsl_tsl_owned_invalidate", "path": "/ticks/7/children/1/children/1/last", "previous_expected": "never", "expected": "never"},
>       {"case": "tsl_tsl_owned_invalidate", "path": "/ticks/7/children/1/children/1/value", "previous_expected": null, "expected": null},
>       {"case": "tsl_tsl_owned_invalidate", "path": "/ticks/7/children/1/children/1/delta", "previous_expected": null, "expected": null},
>       {"case": "tsl_tsl_owned_invalidate", "path": "/ticks/8/valid", "previous_expected": false, "expected": false},
>       {"case": "tsl_tsl_owned_invalidate", "path": "/ticks/8/all_valid", "previous_expected": false, "expected": false},
>       {"case": "tsl_tsl_owned_invalidate", "path": "/ticks/8/modified", "previous_expected": false, "expected": false},
>       {"case": "tsl_tsl_owned_invalidate", "path": "/ticks/8/last", "previous_expected": "never", "expected": "never"},
>       {"case": "tsl_tsl_owned_invalidate", "path": "/ticks/8/value", "previous_expected": null, "expected": null},
>       {"case": "tsl_tsl_owned_invalidate", "path": "/ticks/8/delta", "previous_expected": null, "expected": null},
>       {"case": "tsl_tsl_owned_invalidate", "path": "/ticks/8/peer", "previous_expected": true, "expected": true},
>       {"case": "tsl_tsl_owned_invalidate", "path": "/ticks/8/children", "previous_expected": ["0", "1"], "expected": ["0", "1"]},
>       {"case": "tsl_tsl_owned_invalidate", "path": "/ticks/8/children/0/valid", "previous_expected": false, "expected": false},
>       {"case": "tsl_tsl_owned_invalidate", "path": "/ticks/8/children/0/all_valid", "previous_expected": false, "expected": false},
>       {"case": "tsl_tsl_owned_invalidate", "path": "/ticks/8/children/0/modified", "previous_expected": false, "expected": false},
>       {"case": "tsl_tsl_owned_invalidate", "path": "/ticks/8/children/0/last", "previous_expected": "never", "expected": "never"},
>       {"case": "tsl_tsl_owned_invalidate", "path": "/ticks/8/children/0/value", "previous_expected": null, "expected": null},
>       {"case": "tsl_tsl_owned_invalidate", "path": "/ticks/8/children/0/delta", "previous_expected": null, "expected": null},
>       {"case": "tsl_tsl_owned_invalidate", "path": "/ticks/8/children/0/peer", "previous_expected": true, "expected": true},
>       {"case": "tsl_tsl_owned_invalidate", "path": "/ticks/8/children/0/children", "previous_expected": ["0", "1"], "expected": ["0", "1"]},
>       {"case": "tsl_tsl_owned_invalidate", "path": "/ticks/8/children/0/children/0/valid", "previous_expected": false, "expected": false},
>       {"case": "tsl_tsl_owned_invalidate", "path": "/ticks/8/children/0/children/0/modified", "previous_expected": false, "expected": false},
>       {"case": "tsl_tsl_owned_invalidate", "path": "/ticks/8/children/0/children/0/last", "previous_expected": "never", "expected": "never"},
>       {"case": "tsl_tsl_owned_invalidate", "path": "/ticks/8/children/0/children/0/value", "previous_expected": null, "expected": null},
>       {"case": "tsl_tsl_owned_invalidate", "path": "/ticks/8/children/0/children/0/delta", "previous_expected": null, "expected": null},
>       {"case": "tsl_tsl_owned_invalidate", "path": "/ticks/8/children/0/children/1/valid", "previous_expected": false, "expected": false},
>       {"case": "tsl_tsl_owned_invalidate", "path": "/ticks/8/children/0/children/1/modified", "previous_expected": false, "expected": false},
>       {"case": "tsl_tsl_owned_invalidate", "path": "/ticks/8/children/0/children/1/last", "previous_expected": "never", "expected": "never"},
>       {"case": "tsl_tsl_owned_invalidate", "path": "/ticks/8/children/0/children/1/value", "previous_expected": null, "expected": null},
>       {"case": "tsl_tsl_owned_invalidate", "path": "/ticks/8/children/0/children/1/delta", "previous_expected": null, "expected": null},
>       {"case": "tsl_tsl_owned_invalidate", "path": "/ticks/8/children/1/valid", "previous_expected": false, "expected": false},
>       {"case": "tsl_tsl_owned_invalidate", "path": "/ticks/8/children/1/all_valid", "previous_expected": false, "expected": false},
>       {"case": "tsl_tsl_owned_invalidate", "path": "/ticks/8/children/1/modified", "previous_expected": false, "expected": false},
>       {"case": "tsl_tsl_owned_invalidate", "path": "/ticks/8/children/1/last", "previous_expected": "never", "expected": "never"},
>       {"case": "tsl_tsl_owned_invalidate", "path": "/ticks/8/children/1/value", "previous_expected": null, "expected": null},
>       {"case": "tsl_tsl_owned_invalidate", "path": "/ticks/8/children/1/delta", "previous_expected": null, "expected": null},
>       {"case": "tsl_tsl_owned_invalidate", "path": "/ticks/8/children/1/peer", "previous_expected": true, "expected": true},
>       {"case": "tsl_tsl_owned_invalidate", "path": "/ticks/8/children/1/children", "previous_expected": ["0", "1"], "expected": ["0", "1"]},
>       {"case": "tsl_tsl_owned_invalidate", "path": "/ticks/8/children/1/children/0/valid", "previous_expected": false, "expected": false},
>       {"case": "tsl_tsl_owned_invalidate", "path": "/ticks/8/children/1/children/0/modified", "previous_expected": false, "expected": false},
>       {"case": "tsl_tsl_owned_invalidate", "path": "/ticks/8/children/1/children/0/last", "previous_expected": "never", "expected": "never"},
>       {"case": "tsl_tsl_owned_invalidate", "path": "/ticks/8/children/1/children/0/value", "previous_expected": null, "expected": null},
>       {"case": "tsl_tsl_owned_invalidate", "path": "/ticks/8/children/1/children/0/delta", "previous_expected": null, "expected": null},
>       {"case": "tsl_tsl_owned_invalidate", "path": "/ticks/8/children/1/children/1/valid", "previous_expected": false, "expected": false},
>       {"case": "tsl_tsl_owned_invalidate", "path": "/ticks/8/children/1/children/1/modified", "previous_expected": false, "expected": false},
>       {"case": "tsl_tsl_owned_invalidate", "path": "/ticks/8/children/1/children/1/last", "previous_expected": "never", "expected": "never"},
>       {"case": "tsl_tsl_owned_invalidate", "path": "/ticks/8/children/1/children/1/value", "previous_expected": null, "expected": null},
>       {"case": "tsl_tsl_owned_invalidate", "path": "/ticks/8/children/1/children/1/delta", "previous_expected": null, "expected": null},
>       {"case": "tsl_tsl_assembled_invalidate", "path": "/ticks/7/valid", "previous_expected": false, "expected": false},
>       {"case": "tsl_tsl_assembled_invalidate", "path": "/ticks/7/all_valid", "previous_expected": false, "expected": false},
>       {"case": "tsl_tsl_assembled_invalidate", "path": "/ticks/7/modified", "previous_expected": false, "expected": false},
>       {"case": "tsl_tsl_assembled_invalidate", "path": "/ticks/7/last", "previous_expected": "never", "expected": "never"},
>       {"case": "tsl_tsl_assembled_invalidate", "path": "/ticks/7/value", "previous_expected": null, "expected": null},
>       {"case": "tsl_tsl_assembled_invalidate", "path": "/ticks/7/delta", "previous_expected": null, "expected": null},
>       {"case": "tsl_tsl_assembled_invalidate", "path": "/ticks/7/peer", "previous_expected": false, "expected": false},
>       {"case": "tsl_tsl_assembled_invalidate", "path": "/ticks/7/children", "previous_expected": ["0", "1"], "expected": ["0", "1"]},
>       {"case": "tsl_tsl_assembled_invalidate", "path": "/ticks/7/children/0/valid", "previous_expected": false, "expected": false},
>       {"case": "tsl_tsl_assembled_invalidate", "path": "/ticks/7/children/0/all_valid", "previous_expected": false, "expected": false},
>       {"case": "tsl_tsl_assembled_invalidate", "path": "/ticks/7/children/0/modified", "previous_expected": false, "expected": false},
>       {"case": "tsl_tsl_assembled_invalidate", "path": "/ticks/7/children/0/last", "previous_expected": "never", "expected": "never"},
>       {"case": "tsl_tsl_assembled_invalidate", "path": "/ticks/7/children/0/value", "previous_expected": null, "expected": null},
>       {"case": "tsl_tsl_assembled_invalidate", "path": "/ticks/7/children/0/delta", "previous_expected": null, "expected": null},
>       {"case": "tsl_tsl_assembled_invalidate", "path": "/ticks/7/children/0/peer", "previous_expected": false, "expected": false},
>       {"case": "tsl_tsl_assembled_invalidate", "path": "/ticks/7/children/0/children", "previous_expected": ["0", "1"], "expected": ["0", "1"]},
>       {"case": "tsl_tsl_assembled_invalidate", "path": "/ticks/7/children/0/children/0/valid", "previous_expected": false, "expected": false},
>       {"case": "tsl_tsl_assembled_invalidate", "path": "/ticks/7/children/0/children/0/modified", "previous_expected": false, "expected": false},
>       {"case": "tsl_tsl_assembled_invalidate", "path": "/ticks/7/children/0/children/0/last", "previous_expected": "never", "expected": "never"},
>       {"case": "tsl_tsl_assembled_invalidate", "path": "/ticks/7/children/0/children/0/value", "previous_expected": null, "expected": null},
>       {"case": "tsl_tsl_assembled_invalidate", "path": "/ticks/7/children/0/children/0/delta", "previous_expected": null, "expected": null},
>       {"case": "tsl_tsl_assembled_invalidate", "path": "/ticks/7/children/0/children/1/valid", "previous_expected": false, "expected": false},
>       {"case": "tsl_tsl_assembled_invalidate", "path": "/ticks/7/children/0/children/1/modified", "previous_expected": false, "expected": false},
>       {"case": "tsl_tsl_assembled_invalidate", "path": "/ticks/7/children/0/children/1/last", "previous_expected": "never", "expected": "never"},
>       {"case": "tsl_tsl_assembled_invalidate", "path": "/ticks/7/children/0/children/1/value", "previous_expected": null, "expected": null},
>       {"case": "tsl_tsl_assembled_invalidate", "path": "/ticks/7/children/0/children/1/delta", "previous_expected": null, "expected": null},
>       {"case": "tsl_tsl_assembled_invalidate", "path": "/ticks/7/children/1/valid", "previous_expected": false, "expected": false},
>       {"case": "tsl_tsl_assembled_invalidate", "path": "/ticks/7/children/1/all_valid", "previous_expected": false, "expected": false},
>       {"case": "tsl_tsl_assembled_invalidate", "path": "/ticks/7/children/1/modified", "previous_expected": false, "expected": false},
>       {"case": "tsl_tsl_assembled_invalidate", "path": "/ticks/7/children/1/last", "previous_expected": "never", "expected": "never"},
>       {"case": "tsl_tsl_assembled_invalidate", "path": "/ticks/7/children/1/value", "previous_expected": null, "expected": null},
>       {"case": "tsl_tsl_assembled_invalidate", "path": "/ticks/7/children/1/delta", "previous_expected": null, "expected": null},
>       {"case": "tsl_tsl_assembled_invalidate", "path": "/ticks/7/children/1/peer", "previous_expected": false, "expected": false},
>       {"case": "tsl_tsl_assembled_invalidate", "path": "/ticks/7/children/1/children", "previous_expected": ["0", "1"], "expected": ["0", "1"]},
>       {"case": "tsl_tsl_assembled_invalidate", "path": "/ticks/7/children/1/children/0/valid", "previous_expected": false, "expected": false},
>       {"case": "tsl_tsl_assembled_invalidate", "path": "/ticks/7/children/1/children/0/modified", "previous_expected": false, "expected": false},
>       {"case": "tsl_tsl_assembled_invalidate", "path": "/ticks/7/children/1/children/0/last", "previous_expected": "never", "expected": "never"},
>       {"case": "tsl_tsl_assembled_invalidate", "path": "/ticks/7/children/1/children/0/value", "previous_expected": null, "expected": null},
>       {"case": "tsl_tsl_assembled_invalidate", "path": "/ticks/7/children/1/children/0/delta", "previous_expected": null, "expected": null},
>       {"case": "tsl_tsl_assembled_invalidate", "path": "/ticks/7/children/1/children/1/valid", "previous_expected": false, "expected": false},
>       {"case": "tsl_tsl_assembled_invalidate", "path": "/ticks/7/children/1/children/1/modified", "previous_expected": false, "expected": false},
>       {"case": "tsl_tsl_assembled_invalidate", "path": "/ticks/7/children/1/children/1/last", "previous_expected": "never", "expected": "never"},
>       {"case": "tsl_tsl_assembled_invalidate", "path": "/ticks/7/children/1/children/1/value", "previous_expected": null, "expected": null},
>       {"case": "tsl_tsl_assembled_invalidate", "path": "/ticks/7/children/1/children/1/delta", "previous_expected": null, "expected": null},
>       {"case": "tsl_tsl_assembled_invalidate", "path": "/ticks/8/valid", "previous_expected": false, "expected": false},
>       {"case": "tsl_tsl_assembled_invalidate", "path": "/ticks/8/all_valid", "previous_expected": false, "expected": false},
>       {"case": "tsl_tsl_assembled_invalidate", "path": "/ticks/8/modified", "previous_expected": false, "expected": false},
>       {"case": "tsl_tsl_assembled_invalidate", "path": "/ticks/8/last", "previous_expected": "never", "expected": "never"},
>       {"case": "tsl_tsl_assembled_invalidate", "path": "/ticks/8/value", "previous_expected": null, "expected": null},
>       {"case": "tsl_tsl_assembled_invalidate", "path": "/ticks/8/delta", "previous_expected": null, "expected": null},
>       {"case": "tsl_tsl_assembled_invalidate", "path": "/ticks/8/peer", "previous_expected": false, "expected": false},
>       {"case": "tsl_tsl_assembled_invalidate", "path": "/ticks/8/children", "previous_expected": ["0", "1"], "expected": ["0", "1"]},
>       {"case": "tsl_tsl_assembled_invalidate", "path": "/ticks/8/children/0/valid", "previous_expected": false, "expected": false},
>       {"case": "tsl_tsl_assembled_invalidate", "path": "/ticks/8/children/0/all_valid", "previous_expected": false, "expected": false},
>       {"case": "tsl_tsl_assembled_invalidate", "path": "/ticks/8/children/0/modified", "previous_expected": false, "expected": false},
>       {"case": "tsl_tsl_assembled_invalidate", "path": "/ticks/8/children/0/last", "previous_expected": "never", "expected": "never"},
>       {"case": "tsl_tsl_assembled_invalidate", "path": "/ticks/8/children/0/value", "previous_expected": null, "expected": null},
>       {"case": "tsl_tsl_assembled_invalidate", "path": "/ticks/8/children/0/delta", "previous_expected": null, "expected": null},
>       {"case": "tsl_tsl_assembled_invalidate", "path": "/ticks/8/children/0/peer", "previous_expected": false, "expected": false},
>       {"case": "tsl_tsl_assembled_invalidate", "path": "/ticks/8/children/0/children", "previous_expected": ["0", "1"], "expected": ["0", "1"]},
>       {"case": "tsl_tsl_assembled_invalidate", "path": "/ticks/8/children/0/children/0/valid", "previous_expected": false, "expected": false},
>       {"case": "tsl_tsl_assembled_invalidate", "path": "/ticks/8/children/0/children/0/modified", "previous_expected": false, "expected": false},
>       {"case": "tsl_tsl_assembled_invalidate", "path": "/ticks/8/children/0/children/0/last", "previous_expected": "never", "expected": "never"},
>       {"case": "tsl_tsl_assembled_invalidate", "path": "/ticks/8/children/0/children/0/value", "previous_expected": null, "expected": null},
>       {"case": "tsl_tsl_assembled_invalidate", "path": "/ticks/8/children/0/children/0/delta", "previous_expected": null, "expected": null},
>       {"case": "tsl_tsl_assembled_invalidate", "path": "/ticks/8/children/0/children/1/valid", "previous_expected": false, "expected": false},
>       {"case": "tsl_tsl_assembled_invalidate", "path": "/ticks/8/children/0/children/1/modified", "previous_expected": false, "expected": false},
>       {"case": "tsl_tsl_assembled_invalidate", "path": "/ticks/8/children/0/children/1/last", "previous_expected": "never", "expected": "never"},
>       {"case": "tsl_tsl_assembled_invalidate", "path": "/ticks/8/children/0/children/1/value", "previous_expected": null, "expected": null},
>       {"case": "tsl_tsl_assembled_invalidate", "path": "/ticks/8/children/0/children/1/delta", "previous_expected": null, "expected": null},
>       {"case": "tsl_tsl_assembled_invalidate", "path": "/ticks/8/children/1/valid", "previous_expected": false, "expected": false},
>       {"case": "tsl_tsl_assembled_invalidate", "path": "/ticks/8/children/1/all_valid", "previous_expected": false, "expected": false},
>       {"case": "tsl_tsl_assembled_invalidate", "path": "/ticks/8/children/1/modified", "previous_expected": false, "expected": false},
>       {"case": "tsl_tsl_assembled_invalidate", "path": "/ticks/8/children/1/last", "previous_expected": "never", "expected": "never"},
>       {"case": "tsl_tsl_assembled_invalidate", "path": "/ticks/8/children/1/value", "previous_expected": null, "expected": null},
>       {"case": "tsl_tsl_assembled_invalidate", "path": "/ticks/8/children/1/delta", "previous_expected": null, "expected": null},
>       {"case": "tsl_tsl_assembled_invalidate", "path": "/ticks/8/children/1/peer", "previous_expected": false, "expected": false},
>       {"case": "tsl_tsl_assembled_invalidate", "path": "/ticks/8/children/1/children", "previous_expected": ["0", "1"], "expected": ["0", "1"]},
>       {"case": "tsl_tsl_assembled_invalidate", "path": "/ticks/8/children/1/children/0/valid", "previous_expected": false, "expected": false},
>       {"case": "tsl_tsl_assembled_invalidate", "path": "/ticks/8/children/1/children/0/modified", "previous_expected": false, "expected": false},
>       {"case": "tsl_tsl_assembled_invalidate", "path": "/ticks/8/children/1/children/0/last", "previous_expected": "never", "expected": "never"},
>       {"case": "tsl_tsl_assembled_invalidate", "path": "/ticks/8/children/1/children/0/value", "previous_expected": null, "expected": null},
>       {"case": "tsl_tsl_assembled_invalidate", "path": "/ticks/8/children/1/children/0/delta", "previous_expected": null, "expected": null},
>       {"case": "tsl_tsl_assembled_invalidate", "path": "/ticks/8/children/1/children/1/valid", "previous_expected": false, "expected": false},
>       {"case": "tsl_tsl_assembled_invalidate", "path": "/ticks/8/children/1/children/1/modified", "previous_expected": false, "expected": false},
>       {"case": "tsl_tsl_assembled_invalidate", "path": "/ticks/8/children/1/children/1/last", "previous_expected": "never", "expected": "never"},
>       {"case": "tsl_tsl_assembled_invalidate", "path": "/ticks/8/children/1/children/1/value", "previous_expected": null, "expected": null},
>       {"case": "tsl_tsl_assembled_invalidate", "path": "/ticks/8/children/1/children/1/delta", "previous_expected": null, "expected": null},
>       {"case": "tsl_tsb_owned_invalidate", "path": "/ticks/7/valid", "previous_expected": false, "expected": false},
>       {"case": "tsl_tsb_owned_invalidate", "path": "/ticks/7/all_valid", "previous_expected": false, "expected": false},
>       {"case": "tsl_tsb_owned_invalidate", "path": "/ticks/7/modified", "previous_expected": false, "expected": false},
>       {"case": "tsl_tsb_owned_invalidate", "path": "/ticks/7/last", "previous_expected": "never", "expected": "never"},
>       {"case": "tsl_tsb_owned_invalidate", "path": "/ticks/7/value", "previous_expected": null, "expected": null},
>       {"case": "tsl_tsb_owned_invalidate", "path": "/ticks/7/delta", "previous_expected": null, "expected": null},
>       {"case": "tsl_tsb_owned_invalidate", "path": "/ticks/7/peer", "previous_expected": true, "expected": true},
>       {"case": "tsl_tsb_owned_invalidate", "path": "/ticks/7/children", "previous_expected": ["0", "1"], "expected": ["0", "1"]},
>       {"case": "tsl_tsb_owned_invalidate", "path": "/ticks/7/children/0/valid", "previous_expected": false, "expected": false},
>       {"case": "tsl_tsb_owned_invalidate", "path": "/ticks/7/children/0/all_valid", "previous_expected": false, "expected": false},
>       {"case": "tsl_tsb_owned_invalidate", "path": "/ticks/7/children/0/modified", "previous_expected": false, "expected": false},
>       {"case": "tsl_tsb_owned_invalidate", "path": "/ticks/7/children/0/last", "previous_expected": "never", "expected": "never"},
>       {"case": "tsl_tsb_owned_invalidate", "path": "/ticks/7/children/0/value", "previous_expected": null, "expected": null},
>       {"case": "tsl_tsb_owned_invalidate", "path": "/ticks/7/children/0/delta", "previous_expected": null, "expected": null},
>       {"case": "tsl_tsb_owned_invalidate", "path": "/ticks/7/children/0/peer", "previous_expected": true, "expected": true},
>       {"case": "tsl_tsb_owned_invalidate", "path": "/ticks/7/children/0/children", "previous_expected": ["left", "right"], "expected": ["left", "right"]},
>       {"case": "tsl_tsb_owned_invalidate", "path": "/ticks/7/children/0/children/left/valid", "previous_expected": false, "expected": false},
>       {"case": "tsl_tsb_owned_invalidate", "path": "/ticks/7/children/0/children/left/modified", "previous_expected": false, "expected": false},
>       {"case": "tsl_tsb_owned_invalidate", "path": "/ticks/7/children/0/children/left/last", "previous_expected": "never", "expected": "never"},
>       {"case": "tsl_tsb_owned_invalidate", "path": "/ticks/7/children/0/children/left/value", "previous_expected": null, "expected": null},
>       {"case": "tsl_tsb_owned_invalidate", "path": "/ticks/7/children/0/children/left/delta", "previous_expected": null, "expected": null},
>       {"case": "tsl_tsb_owned_invalidate", "path": "/ticks/7/children/0/children/right/valid", "previous_expected": false, "expected": false},
>       {"case": "tsl_tsb_owned_invalidate", "path": "/ticks/7/children/0/children/right/modified", "previous_expected": false, "expected": false},
>       {"case": "tsl_tsb_owned_invalidate", "path": "/ticks/7/children/0/children/right/last", "previous_expected": "never", "expected": "never"},
>       {"case": "tsl_tsb_owned_invalidate", "path": "/ticks/7/children/0/children/right/value", "previous_expected": null, "expected": null},
>       {"case": "tsl_tsb_owned_invalidate", "path": "/ticks/7/children/0/children/right/delta", "previous_expected": null, "expected": null},
>       {"case": "tsl_tsb_owned_invalidate", "path": "/ticks/7/children/1/valid", "previous_expected": false, "expected": false},
>       {"case": "tsl_tsb_owned_invalidate", "path": "/ticks/7/children/1/all_valid", "previous_expected": false, "expected": false},
>       {"case": "tsl_tsb_owned_invalidate", "path": "/ticks/7/children/1/modified", "previous_expected": false, "expected": false},
>       {"case": "tsl_tsb_owned_invalidate", "path": "/ticks/7/children/1/last", "previous_expected": "never", "expected": "never"},
>       {"case": "tsl_tsb_owned_invalidate", "path": "/ticks/7/children/1/value", "previous_expected": null, "expected": null},
>       {"case": "tsl_tsb_owned_invalidate", "path": "/ticks/7/children/1/delta", "previous_expected": null, "expected": null},
>       {"case": "tsl_tsb_owned_invalidate", "path": "/ticks/7/children/1/peer", "previous_expected": true, "expected": true},
>       {"case": "tsl_tsb_owned_invalidate", "path": "/ticks/7/children/1/children", "previous_expected": ["left", "right"], "expected": ["left", "right"]},
>       {"case": "tsl_tsb_owned_invalidate", "path": "/ticks/7/children/1/children/left/valid", "previous_expected": false, "expected": false},
>       {"case": "tsl_tsb_owned_invalidate", "path": "/ticks/7/children/1/children/left/modified", "previous_expected": false, "expected": false},
>       {"case": "tsl_tsb_owned_invalidate", "path": "/ticks/7/children/1/children/left/last", "previous_expected": "never", "expected": "never"},
>       {"case": "tsl_tsb_owned_invalidate", "path": "/ticks/7/children/1/children/left/value", "previous_expected": null, "expected": null},
>       {"case": "tsl_tsb_owned_invalidate", "path": "/ticks/7/children/1/children/left/delta", "previous_expected": null, "expected": null},
>       {"case": "tsl_tsb_owned_invalidate", "path": "/ticks/7/children/1/children/right/valid", "previous_expected": false, "expected": false},
>       {"case": "tsl_tsb_owned_invalidate", "path": "/ticks/7/children/1/children/right/modified", "previous_expected": false, "expected": false},
>       {"case": "tsl_tsb_owned_invalidate", "path": "/ticks/7/children/1/children/right/last", "previous_expected": "never", "expected": "never"},
>       {"case": "tsl_tsb_owned_invalidate", "path": "/ticks/7/children/1/children/right/value", "previous_expected": null, "expected": null},
>       {"case": "tsl_tsb_owned_invalidate", "path": "/ticks/7/children/1/children/right/delta", "previous_expected": null, "expected": null},
>       {"case": "tsl_tsb_owned_invalidate", "path": "/ticks/8/valid", "previous_expected": false, "expected": false},
>       {"case": "tsl_tsb_owned_invalidate", "path": "/ticks/8/all_valid", "previous_expected": false, "expected": false},
>       {"case": "tsl_tsb_owned_invalidate", "path": "/ticks/8/modified", "previous_expected": false, "expected": false},
>       {"case": "tsl_tsb_owned_invalidate", "path": "/ticks/8/last", "previous_expected": "never", "expected": "never"},
>       {"case": "tsl_tsb_owned_invalidate", "path": "/ticks/8/value", "previous_expected": null, "expected": null},
>       {"case": "tsl_tsb_owned_invalidate", "path": "/ticks/8/delta", "previous_expected": null, "expected": null},
>       {"case": "tsl_tsb_owned_invalidate", "path": "/ticks/8/peer", "previous_expected": true, "expected": true},
>       {"case": "tsl_tsb_owned_invalidate", "path": "/ticks/8/children", "previous_expected": ["0", "1"], "expected": ["0", "1"]},
>       {"case": "tsl_tsb_owned_invalidate", "path": "/ticks/8/children/0/valid", "previous_expected": false, "expected": false},
>       {"case": "tsl_tsb_owned_invalidate", "path": "/ticks/8/children/0/all_valid", "previous_expected": false, "expected": false},
>       {"case": "tsl_tsb_owned_invalidate", "path": "/ticks/8/children/0/modified", "previous_expected": false, "expected": false},
>       {"case": "tsl_tsb_owned_invalidate", "path": "/ticks/8/children/0/last", "previous_expected": "never", "expected": "never"},
>       {"case": "tsl_tsb_owned_invalidate", "path": "/ticks/8/children/0/value", "previous_expected": null, "expected": null},
>       {"case": "tsl_tsb_owned_invalidate", "path": "/ticks/8/children/0/delta", "previous_expected": null, "expected": null},
>       {"case": "tsl_tsb_owned_invalidate", "path": "/ticks/8/children/0/peer", "previous_expected": true, "expected": true},
>       {"case": "tsl_tsb_owned_invalidate", "path": "/ticks/8/children/0/children", "previous_expected": ["left", "right"], "expected": ["left", "right"]},
>       {"case": "tsl_tsb_owned_invalidate", "path": "/ticks/8/children/0/children/left/valid", "previous_expected": false, "expected": false},
>       {"case": "tsl_tsb_owned_invalidate", "path": "/ticks/8/children/0/children/left/modified", "previous_expected": false, "expected": false},
>       {"case": "tsl_tsb_owned_invalidate", "path": "/ticks/8/children/0/children/left/last", "previous_expected": "never", "expected": "never"},
>       {"case": "tsl_tsb_owned_invalidate", "path": "/ticks/8/children/0/children/left/value", "previous_expected": null, "expected": null},
>       {"case": "tsl_tsb_owned_invalidate", "path": "/ticks/8/children/0/children/left/delta", "previous_expected": null, "expected": null},
>       {"case": "tsl_tsb_owned_invalidate", "path": "/ticks/8/children/0/children/right/valid", "previous_expected": false, "expected": false},
>       {"case": "tsl_tsb_owned_invalidate", "path": "/ticks/8/children/0/children/right/modified", "previous_expected": false, "expected": false},
>       {"case": "tsl_tsb_owned_invalidate", "path": "/ticks/8/children/0/children/right/last", "previous_expected": "never", "expected": "never"},
>       {"case": "tsl_tsb_owned_invalidate", "path": "/ticks/8/children/0/children/right/value", "previous_expected": null, "expected": null},
>       {"case": "tsl_tsb_owned_invalidate", "path": "/ticks/8/children/0/children/right/delta", "previous_expected": null, "expected": null},
>       {"case": "tsl_tsb_owned_invalidate", "path": "/ticks/8/children/1/valid", "previous_expected": false, "expected": false},
>       {"case": "tsl_tsb_owned_invalidate", "path": "/ticks/8/children/1/all_valid", "previous_expected": false, "expected": false},
>       {"case": "tsl_tsb_owned_invalidate", "path": "/ticks/8/children/1/modified", "previous_expected": false, "expected": false},
>       {"case": "tsl_tsb_owned_invalidate", "path": "/ticks/8/children/1/last", "previous_expected": "never", "expected": "never"},
>       {"case": "tsl_tsb_owned_invalidate", "path": "/ticks/8/children/1/value", "previous_expected": null, "expected": null},
>       {"case": "tsl_tsb_owned_invalidate", "path": "/ticks/8/children/1/delta", "previous_expected": null, "expected": null},
>       {"case": "tsl_tsb_owned_invalidate", "path": "/ticks/8/children/1/peer", "previous_expected": true, "expected": true},
>       {"case": "tsl_tsb_owned_invalidate", "path": "/ticks/8/children/1/children", "previous_expected": ["left", "right"], "expected": ["left", "right"]},
>       {"case": "tsl_tsb_owned_invalidate", "path": "/ticks/8/children/1/children/left/valid", "previous_expected": false, "expected": false},
>       {"case": "tsl_tsb_owned_invalidate", "path": "/ticks/8/children/1/children/left/modified", "previous_expected": false, "expected": false},
>       {"case": "tsl_tsb_owned_invalidate", "path": "/ticks/8/children/1/children/left/last", "previous_expected": "never", "expected": "never"},
>       {"case": "tsl_tsb_owned_invalidate", "path": "/ticks/8/children/1/children/left/value", "previous_expected": null, "expected": null},
>       {"case": "tsl_tsb_owned_invalidate", "path": "/ticks/8/children/1/children/left/delta", "previous_expected": null, "expected": null},
>       {"case": "tsl_tsb_owned_invalidate", "path": "/ticks/8/children/1/children/right/valid", "previous_expected": false, "expected": false},
>       {"case": "tsl_tsb_owned_invalidate", "path": "/ticks/8/children/1/children/right/modified", "previous_expected": false, "expected": false},
>       {"case": "tsl_tsb_owned_invalidate", "path": "/ticks/8/children/1/children/right/last", "previous_expected": "never", "expected": "never"},
>       {"case": "tsl_tsb_owned_invalidate", "path": "/ticks/8/children/1/children/right/value", "previous_expected": null, "expected": null},
>       {"case": "tsl_tsb_owned_invalidate", "path": "/ticks/8/children/1/children/right/delta", "previous_expected": null, "expected": null},
>       {"case": "tsl_tsb_assembled_invalidate", "path": "/ticks/7/valid", "previous_expected": false, "expected": false},
>       {"case": "tsl_tsb_assembled_invalidate", "path": "/ticks/7/all_valid", "previous_expected": false, "expected": false},
>       {"case": "tsl_tsb_assembled_invalidate", "path": "/ticks/7/modified", "previous_expected": false, "expected": false},
>       {"case": "tsl_tsb_assembled_invalidate", "path": "/ticks/7/last", "previous_expected": "never", "expected": "never"},
>       {"case": "tsl_tsb_assembled_invalidate", "path": "/ticks/7/value", "previous_expected": null, "expected": null},
>       {"case": "tsl_tsb_assembled_invalidate", "path": "/ticks/7/delta", "previous_expected": null, "expected": null},
>       {"case": "tsl_tsb_assembled_invalidate", "path": "/ticks/7/peer", "previous_expected": false, "expected": false},
>       {"case": "tsl_tsb_assembled_invalidate", "path": "/ticks/7/children", "previous_expected": ["0", "1"], "expected": ["0", "1"]},
>       {"case": "tsl_tsb_assembled_invalidate", "path": "/ticks/7/children/0/valid", "previous_expected": false, "expected": false},
>       {"case": "tsl_tsb_assembled_invalidate", "path": "/ticks/7/children/0/all_valid", "previous_expected": false, "expected": false},
>       {"case": "tsl_tsb_assembled_invalidate", "path": "/ticks/7/children/0/modified", "previous_expected": false, "expected": false},
>       {"case": "tsl_tsb_assembled_invalidate", "path": "/ticks/7/children/0/last", "previous_expected": "never", "expected": "never"},
>       {"case": "tsl_tsb_assembled_invalidate", "path": "/ticks/7/children/0/value", "previous_expected": null, "expected": null},
>       {"case": "tsl_tsb_assembled_invalidate", "path": "/ticks/7/children/0/delta", "previous_expected": null, "expected": null},
>       {"case": "tsl_tsb_assembled_invalidate", "path": "/ticks/7/children/0/peer", "previous_expected": false, "expected": false},
>       {"case": "tsl_tsb_assembled_invalidate", "path": "/ticks/7/children/0/children", "previous_expected": ["left", "right"], "expected": ["left", "right"]},
>       {"case": "tsl_tsb_assembled_invalidate", "path": "/ticks/7/children/0/children/left/valid", "previous_expected": false, "expected": false},
>       {"case": "tsl_tsb_assembled_invalidate", "path": "/ticks/7/children/0/children/left/modified", "previous_expected": false, "expected": false},
>       {"case": "tsl_tsb_assembled_invalidate", "path": "/ticks/7/children/0/children/left/last", "previous_expected": "never", "expected": "never"},
>       {"case": "tsl_tsb_assembled_invalidate", "path": "/ticks/7/children/0/children/left/value", "previous_expected": null, "expected": null},
>       {"case": "tsl_tsb_assembled_invalidate", "path": "/ticks/7/children/0/children/left/delta", "previous_expected": null, "expected": null},
>       {"case": "tsl_tsb_assembled_invalidate", "path": "/ticks/7/children/0/children/right/valid", "previous_expected": false, "expected": false},
>       {"case": "tsl_tsb_assembled_invalidate", "path": "/ticks/7/children/0/children/right/modified", "previous_expected": false, "expected": false},
>       {"case": "tsl_tsb_assembled_invalidate", "path": "/ticks/7/children/0/children/right/last", "previous_expected": "never", "expected": "never"},
>       {"case": "tsl_tsb_assembled_invalidate", "path": "/ticks/7/children/0/children/right/value", "previous_expected": null, "expected": null},
>       {"case": "tsl_tsb_assembled_invalidate", "path": "/ticks/7/children/0/children/right/delta", "previous_expected": null, "expected": null},
>       {"case": "tsl_tsb_assembled_invalidate", "path": "/ticks/7/children/1/valid", "previous_expected": false, "expected": false},
>       {"case": "tsl_tsb_assembled_invalidate", "path": "/ticks/7/children/1/all_valid", "previous_expected": false, "expected": false},
>       {"case": "tsl_tsb_assembled_invalidate", "path": "/ticks/7/children/1/modified", "previous_expected": false, "expected": false},
>       {"case": "tsl_tsb_assembled_invalidate", "path": "/ticks/7/children/1/last", "previous_expected": "never", "expected": "never"},
>       {"case": "tsl_tsb_assembled_invalidate", "path": "/ticks/7/children/1/value", "previous_expected": null, "expected": null},
>       {"case": "tsl_tsb_assembled_invalidate", "path": "/ticks/7/children/1/delta", "previous_expected": null, "expected": null},
>       {"case": "tsl_tsb_assembled_invalidate", "path": "/ticks/7/children/1/peer", "previous_expected": false, "expected": false},
>       {"case": "tsl_tsb_assembled_invalidate", "path": "/ticks/7/children/1/children", "previous_expected": ["left", "right"], "expected": ["left", "right"]},
>       {"case": "tsl_tsb_assembled_invalidate", "path": "/ticks/7/children/1/children/left/valid", "previous_expected": false, "expected": false},
>       {"case": "tsl_tsb_assembled_invalidate", "path": "/ticks/7/children/1/children/left/modified", "previous_expected": false, "expected": false},
>       {"case": "tsl_tsb_assembled_invalidate", "path": "/ticks/7/children/1/children/left/last", "previous_expected": "never", "expected": "never"},
>       {"case": "tsl_tsb_assembled_invalidate", "path": "/ticks/7/children/1/children/left/value", "previous_expected": null, "expected": null},
>       {"case": "tsl_tsb_assembled_invalidate", "path": "/ticks/7/children/1/children/left/delta", "previous_expected": null, "expected": null},
>       {"case": "tsl_tsb_assembled_invalidate", "path": "/ticks/7/children/1/children/right/valid", "previous_expected": false, "expected": false},
>       {"case": "tsl_tsb_assembled_invalidate", "path": "/ticks/7/children/1/children/right/modified", "previous_expected": false, "expected": false},
>       {"case": "tsl_tsb_assembled_invalidate", "path": "/ticks/7/children/1/children/right/last", "previous_expected": "never", "expected": "never"},
>       {"case": "tsl_tsb_assembled_invalidate", "path": "/ticks/7/children/1/children/right/value", "previous_expected": null, "expected": null},
>       {"case": "tsl_tsb_assembled_invalidate", "path": "/ticks/7/children/1/children/right/delta", "previous_expected": null, "expected": null},
>       {"case": "tsl_tsb_assembled_invalidate", "path": "/ticks/8/valid", "previous_expected": false, "expected": false},
>       {"case": "tsl_tsb_assembled_invalidate", "path": "/ticks/8/all_valid", "previous_expected": false, "expected": false},
>       {"case": "tsl_tsb_assembled_invalidate", "path": "/ticks/8/modified", "previous_expected": false, "expected": false},
>       {"case": "tsl_tsb_assembled_invalidate", "path": "/ticks/8/last", "previous_expected": "never", "expected": "never"},
>       {"case": "tsl_tsb_assembled_invalidate", "path": "/ticks/8/value", "previous_expected": null, "expected": null},
>       {"case": "tsl_tsb_assembled_invalidate", "path": "/ticks/8/delta", "previous_expected": null, "expected": null},
>       {"case": "tsl_tsb_assembled_invalidate", "path": "/ticks/8/peer", "previous_expected": false, "expected": false},
>       {"case": "tsl_tsb_assembled_invalidate", "path": "/ticks/8/children", "previous_expected": ["0", "1"], "expected": ["0", "1"]},
>       {"case": "tsl_tsb_assembled_invalidate", "path": "/ticks/8/children/0/valid", "previous_expected": false, "expected": false},
>       {"case": "tsl_tsb_assembled_invalidate", "path": "/ticks/8/children/0/all_valid", "previous_expected": false, "expected": false},
>       {"case": "tsl_tsb_assembled_invalidate", "path": "/ticks/8/children/0/modified", "previous_expected": false, "expected": false},
>       {"case": "tsl_tsb_assembled_invalidate", "path": "/ticks/8/children/0/last", "previous_expected": "never", "expected": "never"},
>       {"case": "tsl_tsb_assembled_invalidate", "path": "/ticks/8/children/0/value", "previous_expected": null, "expected": null},
>       {"case": "tsl_tsb_assembled_invalidate", "path": "/ticks/8/children/0/delta", "previous_expected": null, "expected": null},
>       {"case": "tsl_tsb_assembled_invalidate", "path": "/ticks/8/children/0/peer", "previous_expected": false, "expected": false},
>       {"case": "tsl_tsb_assembled_invalidate", "path": "/ticks/8/children/0/children", "previous_expected": ["left", "right"], "expected": ["left", "right"]},
>       {"case": "tsl_tsb_assembled_invalidate", "path": "/ticks/8/children/0/children/left/valid", "previous_expected": false, "expected": false},
>       {"case": "tsl_tsb_assembled_invalidate", "path": "/ticks/8/children/0/children/left/modified", "previous_expected": false, "expected": false},
>       {"case": "tsl_tsb_assembled_invalidate", "path": "/ticks/8/children/0/children/left/last", "previous_expected": "never", "expected": "never"},
>       {"case": "tsl_tsb_assembled_invalidate", "path": "/ticks/8/children/0/children/left/value", "previous_expected": null, "expected": null},
>       {"case": "tsl_tsb_assembled_invalidate", "path": "/ticks/8/children/0/children/left/delta", "previous_expected": null, "expected": null},
>       {"case": "tsl_tsb_assembled_invalidate", "path": "/ticks/8/children/0/children/right/valid", "previous_expected": false, "expected": false},
>       {"case": "tsl_tsb_assembled_invalidate", "path": "/ticks/8/children/0/children/right/modified", "previous_expected": false, "expected": false},
>       {"case": "tsl_tsb_assembled_invalidate", "path": "/ticks/8/children/0/children/right/last", "previous_expected": "never", "expected": "never"},
>       {"case": "tsl_tsb_assembled_invalidate", "path": "/ticks/8/children/0/children/right/value", "previous_expected": null, "expected": null},
>       {"case": "tsl_tsb_assembled_invalidate", "path": "/ticks/8/children/0/children/right/delta", "previous_expected": null, "expected": null},
>       {"case": "tsl_tsb_assembled_invalidate", "path": "/ticks/8/children/1/valid", "previous_expected": false, "expected": false},
>       {"case": "tsl_tsb_assembled_invalidate", "path": "/ticks/8/children/1/all_valid", "previous_expected": false, "expected": false},
>       {"case": "tsl_tsb_assembled_invalidate", "path": "/ticks/8/children/1/modified", "previous_expected": false, "expected": false},
>       {"case": "tsl_tsb_assembled_invalidate", "path": "/ticks/8/children/1/last", "previous_expected": "never", "expected": "never"},
>       {"case": "tsl_tsb_assembled_invalidate", "path": "/ticks/8/children/1/value", "previous_expected": null, "expected": null},
>       {"case": "tsl_tsb_assembled_invalidate", "path": "/ticks/8/children/1/delta", "previous_expected": null, "expected": null},
>       {"case": "tsl_tsb_assembled_invalidate", "path": "/ticks/8/children/1/peer", "previous_expected": false, "expected": false},
>       {"case": "tsl_tsb_assembled_invalidate", "path": "/ticks/8/children/1/children", "previous_expected": ["left", "right"], "expected": ["left", "right"]},
>       {"case": "tsl_tsb_assembled_invalidate", "path": "/ticks/8/children/1/children/left/valid", "previous_expected": false, "expected": false},
>       {"case": "tsl_tsb_assembled_invalidate", "path": "/ticks/8/children/1/children/left/modified", "previous_expected": false, "expected": false},
>       {"case": "tsl_tsb_assembled_invalidate", "path": "/ticks/8/children/1/children/left/last", "previous_expected": "never", "expected": "never"},
>       {"case": "tsl_tsb_assembled_invalidate", "path": "/ticks/8/children/1/children/left/value", "previous_expected": null, "expected": null},
>       {"case": "tsl_tsb_assembled_invalidate", "path": "/ticks/8/children/1/children/left/delta", "previous_expected": null, "expected": null},
>       {"case": "tsl_tsb_assembled_invalidate", "path": "/ticks/8/children/1/children/right/valid", "previous_expected": false, "expected": false},
>       {"case": "tsl_tsb_assembled_invalidate", "path": "/ticks/8/children/1/children/right/modified", "previous_expected": false, "expected": false},
>       {"case": "tsl_tsb_assembled_invalidate", "path": "/ticks/8/children/1/children/right/last", "previous_expected": "never", "expected": "never"},
>       {"case": "tsl_tsb_assembled_invalidate", "path": "/ticks/8/children/1/children/right/value", "previous_expected": null, "expected": null},
>       {"case": "tsl_tsb_assembled_invalidate", "path": "/ticks/8/children/1/children/right/delta", "previous_expected": null, "expected": null},
>       {"case": "tsb_tsl_owned_invalidate", "path": "/ticks/7/valid", "previous_expected": false, "expected": false},
>       {"case": "tsb_tsl_owned_invalidate", "path": "/ticks/7/all_valid", "previous_expected": false, "expected": false},
>       {"case": "tsb_tsl_owned_invalidate", "path": "/ticks/7/modified", "previous_expected": false, "expected": false},
>       {"case": "tsb_tsl_owned_invalidate", "path": "/ticks/7/last", "previous_expected": "never", "expected": "never"},
>       {"case": "tsb_tsl_owned_invalidate", "path": "/ticks/7/value", "previous_expected": null, "expected": null},
>       {"case": "tsb_tsl_owned_invalidate", "path": "/ticks/7/delta", "previous_expected": null, "expected": null},
>       {"case": "tsb_tsl_owned_invalidate", "path": "/ticks/7/peer", "previous_expected": true, "expected": true},
>       {"case": "tsb_tsl_owned_invalidate", "path": "/ticks/7/children", "previous_expected": ["left", "right"], "expected": ["left", "right"]},
>       {"case": "tsb_tsl_owned_invalidate", "path": "/ticks/7/children/left/valid", "previous_expected": false, "expected": false},
>       {"case": "tsb_tsl_owned_invalidate", "path": "/ticks/7/children/left/all_valid", "previous_expected": false, "expected": false},
>       {"case": "tsb_tsl_owned_invalidate", "path": "/ticks/7/children/left/modified", "previous_expected": false, "expected": false},
>       {"case": "tsb_tsl_owned_invalidate", "path": "/ticks/7/children/left/last", "previous_expected": "never", "expected": "never"},
>       {"case": "tsb_tsl_owned_invalidate", "path": "/ticks/7/children/left/value", "previous_expected": null, "expected": null},
>       {"case": "tsb_tsl_owned_invalidate", "path": "/ticks/7/children/left/delta", "previous_expected": null, "expected": null},
>       {"case": "tsb_tsl_owned_invalidate", "path": "/ticks/7/children/left/peer", "previous_expected": true, "expected": true},
>       {"case": "tsb_tsl_owned_invalidate", "path": "/ticks/7/children/left/children", "previous_expected": ["0", "1"], "expected": ["0", "1"]},
>       {"case": "tsb_tsl_owned_invalidate", "path": "/ticks/7/children/left/children/0/valid", "previous_expected": false, "expected": false},
>       {"case": "tsb_tsl_owned_invalidate", "path": "/ticks/7/children/left/children/0/modified", "previous_expected": false, "expected": false},
>       {"case": "tsb_tsl_owned_invalidate", "path": "/ticks/7/children/left/children/0/last", "previous_expected": "never", "expected": "never"},
>       {"case": "tsb_tsl_owned_invalidate", "path": "/ticks/7/children/left/children/0/value", "previous_expected": null, "expected": null},
>       {"case": "tsb_tsl_owned_invalidate", "path": "/ticks/7/children/left/children/0/delta", "previous_expected": null, "expected": null},
>       {"case": "tsb_tsl_owned_invalidate", "path": "/ticks/7/children/left/children/1/valid", "previous_expected": false, "expected": false},
>       {"case": "tsb_tsl_owned_invalidate", "path": "/ticks/7/children/left/children/1/modified", "previous_expected": false, "expected": false},
>       {"case": "tsb_tsl_owned_invalidate", "path": "/ticks/7/children/left/children/1/last", "previous_expected": "never", "expected": "never"},
>       {"case": "tsb_tsl_owned_invalidate", "path": "/ticks/7/children/left/children/1/value", "previous_expected": null, "expected": null},
>       {"case": "tsb_tsl_owned_invalidate", "path": "/ticks/7/children/left/children/1/delta", "previous_expected": null, "expected": null},
>       {"case": "tsb_tsl_owned_invalidate", "path": "/ticks/7/children/right/valid", "previous_expected": false, "expected": false},
>       {"case": "tsb_tsl_owned_invalidate", "path": "/ticks/7/children/right/all_valid", "previous_expected": false, "expected": false},
>       {"case": "tsb_tsl_owned_invalidate", "path": "/ticks/7/children/right/modified", "previous_expected": false, "expected": false},
>       {"case": "tsb_tsl_owned_invalidate", "path": "/ticks/7/children/right/last", "previous_expected": "never", "expected": "never"},
>       {"case": "tsb_tsl_owned_invalidate", "path": "/ticks/7/children/right/value", "previous_expected": null, "expected": null},
>       {"case": "tsb_tsl_owned_invalidate", "path": "/ticks/7/children/right/delta", "previous_expected": null, "expected": null},
>       {"case": "tsb_tsl_owned_invalidate", "path": "/ticks/7/children/right/peer", "previous_expected": true, "expected": true},
>       {"case": "tsb_tsl_owned_invalidate", "path": "/ticks/7/children/right/children", "previous_expected": ["0", "1"], "expected": ["0", "1"]},
>       {"case": "tsb_tsl_owned_invalidate", "path": "/ticks/7/children/right/children/0/valid", "previous_expected": false, "expected": false},
>       {"case": "tsb_tsl_owned_invalidate", "path": "/ticks/7/children/right/children/0/modified", "previous_expected": false, "expected": false},
>       {"case": "tsb_tsl_owned_invalidate", "path": "/ticks/7/children/right/children/0/last", "previous_expected": "never", "expected": "never"},
>       {"case": "tsb_tsl_owned_invalidate", "path": "/ticks/7/children/right/children/0/value", "previous_expected": null, "expected": null},
>       {"case": "tsb_tsl_owned_invalidate", "path": "/ticks/7/children/right/children/0/delta", "previous_expected": null, "expected": null},
>       {"case": "tsb_tsl_owned_invalidate", "path": "/ticks/7/children/right/children/1/valid", "previous_expected": false, "expected": false},
>       {"case": "tsb_tsl_owned_invalidate", "path": "/ticks/7/children/right/children/1/modified", "previous_expected": false, "expected": false},
>       {"case": "tsb_tsl_owned_invalidate", "path": "/ticks/7/children/right/children/1/last", "previous_expected": "never", "expected": "never"},
>       {"case": "tsb_tsl_owned_invalidate", "path": "/ticks/7/children/right/children/1/value", "previous_expected": null, "expected": null},
>       {"case": "tsb_tsl_owned_invalidate", "path": "/ticks/7/children/right/children/1/delta", "previous_expected": null, "expected": null},
>       {"case": "tsb_tsl_owned_invalidate", "path": "/ticks/8/valid", "previous_expected": false, "expected": false},
>       {"case": "tsb_tsl_owned_invalidate", "path": "/ticks/8/all_valid", "previous_expected": false, "expected": false},
>       {"case": "tsb_tsl_owned_invalidate", "path": "/ticks/8/modified", "previous_expected": false, "expected": false},
>       {"case": "tsb_tsl_owned_invalidate", "path": "/ticks/8/last", "previous_expected": "never", "expected": "never"},
>       {"case": "tsb_tsl_owned_invalidate", "path": "/ticks/8/value", "previous_expected": null, "expected": null},
>       {"case": "tsb_tsl_owned_invalidate", "path": "/ticks/8/delta", "previous_expected": null, "expected": null},
>       {"case": "tsb_tsl_owned_invalidate", "path": "/ticks/8/peer", "previous_expected": true, "expected": true},
>       {"case": "tsb_tsl_owned_invalidate", "path": "/ticks/8/children", "previous_expected": ["left", "right"], "expected": ["left", "right"]},
>       {"case": "tsb_tsl_owned_invalidate", "path": "/ticks/8/children/left/valid", "previous_expected": false, "expected": false},
>       {"case": "tsb_tsl_owned_invalidate", "path": "/ticks/8/children/left/all_valid", "previous_expected": false, "expected": false},
>       {"case": "tsb_tsl_owned_invalidate", "path": "/ticks/8/children/left/modified", "previous_expected": false, "expected": false},
>       {"case": "tsb_tsl_owned_invalidate", "path": "/ticks/8/children/left/last", "previous_expected": "never", "expected": "never"},
>       {"case": "tsb_tsl_owned_invalidate", "path": "/ticks/8/children/left/value", "previous_expected": null, "expected": null},
>       {"case": "tsb_tsl_owned_invalidate", "path": "/ticks/8/children/left/delta", "previous_expected": null, "expected": null},
>       {"case": "tsb_tsl_owned_invalidate", "path": "/ticks/8/children/left/peer", "previous_expected": true, "expected": true},
>       {"case": "tsb_tsl_owned_invalidate", "path": "/ticks/8/children/left/children", "previous_expected": ["0", "1"], "expected": ["0", "1"]},
>       {"case": "tsb_tsl_owned_invalidate", "path": "/ticks/8/children/left/children/0/valid", "previous_expected": false, "expected": false},
>       {"case": "tsb_tsl_owned_invalidate", "path": "/ticks/8/children/left/children/0/modified", "previous_expected": false, "expected": false},
>       {"case": "tsb_tsl_owned_invalidate", "path": "/ticks/8/children/left/children/0/last", "previous_expected": "never", "expected": "never"},
>       {"case": "tsb_tsl_owned_invalidate", "path": "/ticks/8/children/left/children/0/value", "previous_expected": null, "expected": null},
>       {"case": "tsb_tsl_owned_invalidate", "path": "/ticks/8/children/left/children/0/delta", "previous_expected": null, "expected": null},
>       {"case": "tsb_tsl_owned_invalidate", "path": "/ticks/8/children/left/children/1/valid", "previous_expected": false, "expected": false},
>       {"case": "tsb_tsl_owned_invalidate", "path": "/ticks/8/children/left/children/1/modified", "previous_expected": false, "expected": false},
>       {"case": "tsb_tsl_owned_invalidate", "path": "/ticks/8/children/left/children/1/last", "previous_expected": "never", "expected": "never"},
>       {"case": "tsb_tsl_owned_invalidate", "path": "/ticks/8/children/left/children/1/value", "previous_expected": null, "expected": null},
>       {"case": "tsb_tsl_owned_invalidate", "path": "/ticks/8/children/left/children/1/delta", "previous_expected": null, "expected": null},
>       {"case": "tsb_tsl_owned_invalidate", "path": "/ticks/8/children/right/valid", "previous_expected": false, "expected": false},
>       {"case": "tsb_tsl_owned_invalidate", "path": "/ticks/8/children/right/all_valid", "previous_expected": false, "expected": false},
>       {"case": "tsb_tsl_owned_invalidate", "path": "/ticks/8/children/right/modified", "previous_expected": false, "expected": false},
>       {"case": "tsb_tsl_owned_invalidate", "path": "/ticks/8/children/right/last", "previous_expected": "never", "expected": "never"},
>       {"case": "tsb_tsl_owned_invalidate", "path": "/ticks/8/children/right/value", "previous_expected": null, "expected": null},
>       {"case": "tsb_tsl_owned_invalidate", "path": "/ticks/8/children/right/delta", "previous_expected": null, "expected": null},
>       {"case": "tsb_tsl_owned_invalidate", "path": "/ticks/8/children/right/peer", "previous_expected": true, "expected": true},
>       {"case": "tsb_tsl_owned_invalidate", "path": "/ticks/8/children/right/children", "previous_expected": ["0", "1"], "expected": ["0", "1"]},
>       {"case": "tsb_tsl_owned_invalidate", "path": "/ticks/8/children/right/children/0/valid", "previous_expected": false, "expected": false},
>       {"case": "tsb_tsl_owned_invalidate", "path": "/ticks/8/children/right/children/0/modified", "previous_expected": false, "expected": false},
>       {"case": "tsb_tsl_owned_invalidate", "path": "/ticks/8/children/right/children/0/last", "previous_expected": "never", "expected": "never"},
>       {"case": "tsb_tsl_owned_invalidate", "path": "/ticks/8/children/right/children/0/value", "previous_expected": null, "expected": null},
>       {"case": "tsb_tsl_owned_invalidate", "path": "/ticks/8/children/right/children/0/delta", "previous_expected": null, "expected": null},
>       {"case": "tsb_tsl_owned_invalidate", "path": "/ticks/8/children/right/children/1/valid", "previous_expected": false, "expected": false},
>       {"case": "tsb_tsl_owned_invalidate", "path": "/ticks/8/children/right/children/1/modified", "previous_expected": false, "expected": false},
>       {"case": "tsb_tsl_owned_invalidate", "path": "/ticks/8/children/right/children/1/last", "previous_expected": "never", "expected": "never"},
>       {"case": "tsb_tsl_owned_invalidate", "path": "/ticks/8/children/right/children/1/value", "previous_expected": null, "expected": null},
>       {"case": "tsb_tsl_owned_invalidate", "path": "/ticks/8/children/right/children/1/delta", "previous_expected": null, "expected": null},
>       {"case": "tsb_tsl_assembled_invalidate", "path": "/ticks/7/valid", "previous_expected": false, "expected": false},
>       {"case": "tsb_tsl_assembled_invalidate", "path": "/ticks/7/all_valid", "previous_expected": false, "expected": false},
>       {"case": "tsb_tsl_assembled_invalidate", "path": "/ticks/7/modified", "previous_expected": false, "expected": false},
>       {"case": "tsb_tsl_assembled_invalidate", "path": "/ticks/7/last", "previous_expected": "never", "expected": "never"},
>       {"case": "tsb_tsl_assembled_invalidate", "path": "/ticks/7/value", "previous_expected": null, "expected": null},
>       {"case": "tsb_tsl_assembled_invalidate", "path": "/ticks/7/delta", "previous_expected": null, "expected": null},
>       {"case": "tsb_tsl_assembled_invalidate", "path": "/ticks/7/peer", "previous_expected": false, "expected": false},
>       {"case": "tsb_tsl_assembled_invalidate", "path": "/ticks/7/children", "previous_expected": ["left", "right"], "expected": ["left", "right"]},
>       {"case": "tsb_tsl_assembled_invalidate", "path": "/ticks/7/children/left/valid", "previous_expected": false, "expected": false},
>       {"case": "tsb_tsl_assembled_invalidate", "path": "/ticks/7/children/left/all_valid", "previous_expected": false, "expected": false},
>       {"case": "tsb_tsl_assembled_invalidate", "path": "/ticks/7/children/left/modified", "previous_expected": false, "expected": false},
>       {"case": "tsb_tsl_assembled_invalidate", "path": "/ticks/7/children/left/last", "previous_expected": "never", "expected": "never"},
>       {"case": "tsb_tsl_assembled_invalidate", "path": "/ticks/7/children/left/value", "previous_expected": null, "expected": null},
>       {"case": "tsb_tsl_assembled_invalidate", "path": "/ticks/7/children/left/delta", "previous_expected": null, "expected": null},
>       {"case": "tsb_tsl_assembled_invalidate", "path": "/ticks/7/children/left/peer", "previous_expected": false, "expected": false},
>       {"case": "tsb_tsl_assembled_invalidate", "path": "/ticks/7/children/left/children", "previous_expected": ["0", "1"], "expected": ["0", "1"]},
>       {"case": "tsb_tsl_assembled_invalidate", "path": "/ticks/7/children/left/children/0/valid", "previous_expected": false, "expected": false},
>       {"case": "tsb_tsl_assembled_invalidate", "path": "/ticks/7/children/left/children/0/modified", "previous_expected": false, "expected": false},
>       {"case": "tsb_tsl_assembled_invalidate", "path": "/ticks/7/children/left/children/0/last", "previous_expected": "never", "expected": "never"},
>       {"case": "tsb_tsl_assembled_invalidate", "path": "/ticks/7/children/left/children/0/value", "previous_expected": null, "expected": null},
>       {"case": "tsb_tsl_assembled_invalidate", "path": "/ticks/7/children/left/children/0/delta", "previous_expected": null, "expected": null},
>       {"case": "tsb_tsl_assembled_invalidate", "path": "/ticks/7/children/left/children/1/valid", "previous_expected": false, "expected": false},
>       {"case": "tsb_tsl_assembled_invalidate", "path": "/ticks/7/children/left/children/1/modified", "previous_expected": false, "expected": false},
>       {"case": "tsb_tsl_assembled_invalidate", "path": "/ticks/7/children/left/children/1/last", "previous_expected": "never", "expected": "never"},
>       {"case": "tsb_tsl_assembled_invalidate", "path": "/ticks/7/children/left/children/1/value", "previous_expected": null, "expected": null},
>       {"case": "tsb_tsl_assembled_invalidate", "path": "/ticks/7/children/left/children/1/delta", "previous_expected": null, "expected": null},
>       {"case": "tsb_tsl_assembled_invalidate", "path": "/ticks/7/children/right/valid", "previous_expected": false, "expected": false},
>       {"case": "tsb_tsl_assembled_invalidate", "path": "/ticks/7/children/right/all_valid", "previous_expected": false, "expected": false},
>       {"case": "tsb_tsl_assembled_invalidate", "path": "/ticks/7/children/right/modified", "previous_expected": false, "expected": false},
>       {"case": "tsb_tsl_assembled_invalidate", "path": "/ticks/7/children/right/last", "previous_expected": "never", "expected": "never"},
>       {"case": "tsb_tsl_assembled_invalidate", "path": "/ticks/7/children/right/value", "previous_expected": null, "expected": null},
>       {"case": "tsb_tsl_assembled_invalidate", "path": "/ticks/7/children/right/delta", "previous_expected": null, "expected": null},
>       {"case": "tsb_tsl_assembled_invalidate", "path": "/ticks/7/children/right/peer", "previous_expected": false, "expected": false},
>       {"case": "tsb_tsl_assembled_invalidate", "path": "/ticks/7/children/right/children", "previous_expected": ["0", "1"], "expected": ["0", "1"]},
>       {"case": "tsb_tsl_assembled_invalidate", "path": "/ticks/7/children/right/children/0/valid", "previous_expected": false, "expected": false},
>       {"case": "tsb_tsl_assembled_invalidate", "path": "/ticks/7/children/right/children/0/modified", "previous_expected": false, "expected": false},
>       {"case": "tsb_tsl_assembled_invalidate", "path": "/ticks/7/children/right/children/0/last", "previous_expected": "never", "expected": "never"},
>       {"case": "tsb_tsl_assembled_invalidate", "path": "/ticks/7/children/right/children/0/value", "previous_expected": null, "expected": null},
>       {"case": "tsb_tsl_assembled_invalidate", "path": "/ticks/7/children/right/children/0/delta", "previous_expected": null, "expected": null},
>       {"case": "tsb_tsl_assembled_invalidate", "path": "/ticks/7/children/right/children/1/valid", "previous_expected": false, "expected": false},
>       {"case": "tsb_tsl_assembled_invalidate", "path": "/ticks/7/children/right/children/1/modified", "previous_expected": false, "expected": false},
>       {"case": "tsb_tsl_assembled_invalidate", "path": "/ticks/7/children/right/children/1/last", "previous_expected": "never", "expected": "never"},
>       {"case": "tsb_tsl_assembled_invalidate", "path": "/ticks/7/children/right/children/1/value", "previous_expected": null, "expected": null},
>       {"case": "tsb_tsl_assembled_invalidate", "path": "/ticks/7/children/right/children/1/delta", "previous_expected": null, "expected": null},
>       {"case": "tsb_tsl_assembled_invalidate", "path": "/ticks/8/valid", "previous_expected": false, "expected": false},
>       {"case": "tsb_tsl_assembled_invalidate", "path": "/ticks/8/all_valid", "previous_expected": false, "expected": false},
>       {"case": "tsb_tsl_assembled_invalidate", "path": "/ticks/8/modified", "previous_expected": false, "expected": false},
>       {"case": "tsb_tsl_assembled_invalidate", "path": "/ticks/8/last", "previous_expected": "never", "expected": "never"},
>       {"case": "tsb_tsl_assembled_invalidate", "path": "/ticks/8/value", "previous_expected": null, "expected": null},
>       {"case": "tsb_tsl_assembled_invalidate", "path": "/ticks/8/delta", "previous_expected": null, "expected": null},
>       {"case": "tsb_tsl_assembled_invalidate", "path": "/ticks/8/peer", "previous_expected": false, "expected": false},
>       {"case": "tsb_tsl_assembled_invalidate", "path": "/ticks/8/children", "previous_expected": ["left", "right"], "expected": ["left", "right"]},
>       {"case": "tsb_tsl_assembled_invalidate", "path": "/ticks/8/children/left/valid", "previous_expected": false, "expected": false},
>       {"case": "tsb_tsl_assembled_invalidate", "path": "/ticks/8/children/left/all_valid", "previous_expected": false, "expected": false},
>       {"case": "tsb_tsl_assembled_invalidate", "path": "/ticks/8/children/left/modified", "previous_expected": false, "expected": false},
>       {"case": "tsb_tsl_assembled_invalidate", "path": "/ticks/8/children/left/last", "previous_expected": "never", "expected": "never"},
>       {"case": "tsb_tsl_assembled_invalidate", "path": "/ticks/8/children/left/value", "previous_expected": null, "expected": null},
>       {"case": "tsb_tsl_assembled_invalidate", "path": "/ticks/8/children/left/delta", "previous_expected": null, "expected": null},
>       {"case": "tsb_tsl_assembled_invalidate", "path": "/ticks/8/children/left/peer", "previous_expected": false, "expected": false},
>       {"case": "tsb_tsl_assembled_invalidate", "path": "/ticks/8/children/left/children", "previous_expected": ["0", "1"], "expected": ["0", "1"]},
>       {"case": "tsb_tsl_assembled_invalidate", "path": "/ticks/8/children/left/children/0/valid", "previous_expected": false, "expected": false},
>       {"case": "tsb_tsl_assembled_invalidate", "path": "/ticks/8/children/left/children/0/modified", "previous_expected": false, "expected": false},
>       {"case": "tsb_tsl_assembled_invalidate", "path": "/ticks/8/children/left/children/0/last", "previous_expected": "never", "expected": "never"},
>       {"case": "tsb_tsl_assembled_invalidate", "path": "/ticks/8/children/left/children/0/value", "previous_expected": null, "expected": null},
>       {"case": "tsb_tsl_assembled_invalidate", "path": "/ticks/8/children/left/children/0/delta", "previous_expected": null, "expected": null},
>       {"case": "tsb_tsl_assembled_invalidate", "path": "/ticks/8/children/left/children/1/valid", "previous_expected": false, "expected": false},
>       {"case": "tsb_tsl_assembled_invalidate", "path": "/ticks/8/children/left/children/1/modified", "previous_expected": false, "expected": false},
>       {"case": "tsb_tsl_assembled_invalidate", "path": "/ticks/8/children/left/children/1/last", "previous_expected": "never", "expected": "never"},
>       {"case": "tsb_tsl_assembled_invalidate", "path": "/ticks/8/children/left/children/1/value", "previous_expected": null, "expected": null},
>       {"case": "tsb_tsl_assembled_invalidate", "path": "/ticks/8/children/left/children/1/delta", "previous_expected": null, "expected": null},
>       {"case": "tsb_tsl_assembled_invalidate", "path": "/ticks/8/children/right/valid", "previous_expected": false, "expected": false},
>       {"case": "tsb_tsl_assembled_invalidate", "path": "/ticks/8/children/right/all_valid", "previous_expected": false, "expected": false},
>       {"case": "tsb_tsl_assembled_invalidate", "path": "/ticks/8/children/right/modified", "previous_expected": false, "expected": false},
>       {"case": "tsb_tsl_assembled_invalidate", "path": "/ticks/8/children/right/last", "previous_expected": "never", "expected": "never"},
>       {"case": "tsb_tsl_assembled_invalidate", "path": "/ticks/8/children/right/value", "previous_expected": null, "expected": null},
>       {"case": "tsb_tsl_assembled_invalidate", "path": "/ticks/8/children/right/delta", "previous_expected": null, "expected": null},
>       {"case": "tsb_tsl_assembled_invalidate", "path": "/ticks/8/children/right/peer", "previous_expected": false, "expected": false},
>       {"case": "tsb_tsl_assembled_invalidate", "path": "/ticks/8/children/right/children", "previous_expected": ["0", "1"], "expected": ["0", "1"]},
>       {"case": "tsb_tsl_assembled_invalidate", "path": "/ticks/8/children/right/children/0/valid", "previous_expected": false, "expected": false},
>       {"case": "tsb_tsl_assembled_invalidate", "path": "/ticks/8/children/right/children/0/modified", "previous_expected": false, "expected": false},
>       {"case": "tsb_tsl_assembled_invalidate", "path": "/ticks/8/children/right/children/0/last", "previous_expected": "never", "expected": "never"},
>       {"case": "tsb_tsl_assembled_invalidate", "path": "/ticks/8/children/right/children/0/value", "previous_expected": null, "expected": null},
>       {"case": "tsb_tsl_assembled_invalidate", "path": "/ticks/8/children/right/children/0/delta", "previous_expected": null, "expected": null},
>       {"case": "tsb_tsl_assembled_invalidate", "path": "/ticks/8/children/right/children/1/valid", "previous_expected": false, "expected": false},
>       {"case": "tsb_tsl_assembled_invalidate", "path": "/ticks/8/children/right/children/1/modified", "previous_expected": false, "expected": false},
>       {"case": "tsb_tsl_assembled_invalidate", "path": "/ticks/8/children/right/children/1/last", "previous_expected": "never", "expected": "never"},
>       {"case": "tsb_tsl_assembled_invalidate", "path": "/ticks/8/children/right/children/1/value", "previous_expected": null, "expected": null},
>       {"case": "tsb_tsl_assembled_invalidate", "path": "/ticks/8/children/right/children/1/delta", "previous_expected": null, "expected": null},
>       {"case": "tsb_tsb_owned_invalidate", "path": "/ticks/7/valid", "previous_expected": false, "expected": false},
>       {"case": "tsb_tsb_owned_invalidate", "path": "/ticks/7/all_valid", "previous_expected": false, "expected": false},
>       {"case": "tsb_tsb_owned_invalidate", "path": "/ticks/7/modified", "previous_expected": false, "expected": false},
>       {"case": "tsb_tsb_owned_invalidate", "path": "/ticks/7/last", "previous_expected": "never", "expected": "never"},
>       {"case": "tsb_tsb_owned_invalidate", "path": "/ticks/7/value", "previous_expected": null, "expected": null},
>       {"case": "tsb_tsb_owned_invalidate", "path": "/ticks/7/delta", "previous_expected": null, "expected": null},
>       {"case": "tsb_tsb_owned_invalidate", "path": "/ticks/7/peer", "previous_expected": true, "expected": true},
>       {"case": "tsb_tsb_owned_invalidate", "path": "/ticks/7/children", "previous_expected": ["left", "right"], "expected": ["left", "right"]},
>       {"case": "tsb_tsb_owned_invalidate", "path": "/ticks/7/children/left/valid", "previous_expected": false, "expected": false},
>       {"case": "tsb_tsb_owned_invalidate", "path": "/ticks/7/children/left/all_valid", "previous_expected": false, "expected": false},
>       {"case": "tsb_tsb_owned_invalidate", "path": "/ticks/7/children/left/modified", "previous_expected": false, "expected": false},
>       {"case": "tsb_tsb_owned_invalidate", "path": "/ticks/7/children/left/last", "previous_expected": "never", "expected": "never"},
>       {"case": "tsb_tsb_owned_invalidate", "path": "/ticks/7/children/left/value", "previous_expected": null, "expected": null},
>       {"case": "tsb_tsb_owned_invalidate", "path": "/ticks/7/children/left/delta", "previous_expected": null, "expected": null},
>       {"case": "tsb_tsb_owned_invalidate", "path": "/ticks/7/children/left/peer", "previous_expected": true, "expected": true},
>       {"case": "tsb_tsb_owned_invalidate", "path": "/ticks/7/children/left/children", "previous_expected": ["left", "right"], "expected": ["left", "right"]},
>       {"case": "tsb_tsb_owned_invalidate", "path": "/ticks/7/children/left/children/left/valid", "previous_expected": false, "expected": false},
>       {"case": "tsb_tsb_owned_invalidate", "path": "/ticks/7/children/left/children/left/modified", "previous_expected": false, "expected": false},
>       {"case": "tsb_tsb_owned_invalidate", "path": "/ticks/7/children/left/children/left/last", "previous_expected": "never", "expected": "never"},
>       {"case": "tsb_tsb_owned_invalidate", "path": "/ticks/7/children/left/children/left/value", "previous_expected": null, "expected": null},
>       {"case": "tsb_tsb_owned_invalidate", "path": "/ticks/7/children/left/children/left/delta", "previous_expected": null, "expected": null},
>       {"case": "tsb_tsb_owned_invalidate", "path": "/ticks/7/children/left/children/right/valid", "previous_expected": false, "expected": false},
>       {"case": "tsb_tsb_owned_invalidate", "path": "/ticks/7/children/left/children/right/modified", "previous_expected": false, "expected": false},
>       {"case": "tsb_tsb_owned_invalidate", "path": "/ticks/7/children/left/children/right/last", "previous_expected": "never", "expected": "never"},
>       {"case": "tsb_tsb_owned_invalidate", "path": "/ticks/7/children/left/children/right/value", "previous_expected": null, "expected": null},
>       {"case": "tsb_tsb_owned_invalidate", "path": "/ticks/7/children/left/children/right/delta", "previous_expected": null, "expected": null},
>       {"case": "tsb_tsb_owned_invalidate", "path": "/ticks/7/children/right/valid", "previous_expected": false, "expected": false},
>       {"case": "tsb_tsb_owned_invalidate", "path": "/ticks/7/children/right/all_valid", "previous_expected": false, "expected": false},
>       {"case": "tsb_tsb_owned_invalidate", "path": "/ticks/7/children/right/modified", "previous_expected": false, "expected": false},
>       {"case": "tsb_tsb_owned_invalidate", "path": "/ticks/7/children/right/last", "previous_expected": "never", "expected": "never"},
>       {"case": "tsb_tsb_owned_invalidate", "path": "/ticks/7/children/right/value", "previous_expected": null, "expected": null},
>       {"case": "tsb_tsb_owned_invalidate", "path": "/ticks/7/children/right/delta", "previous_expected": null, "expected": null},
>       {"case": "tsb_tsb_owned_invalidate", "path": "/ticks/7/children/right/peer", "previous_expected": true, "expected": true},
>       {"case": "tsb_tsb_owned_invalidate", "path": "/ticks/7/children/right/children", "previous_expected": ["left", "right"], "expected": ["left", "right"]},
>       {"case": "tsb_tsb_owned_invalidate", "path": "/ticks/7/children/right/children/left/valid", "previous_expected": false, "expected": false},
>       {"case": "tsb_tsb_owned_invalidate", "path": "/ticks/7/children/right/children/left/modified", "previous_expected": false, "expected": false},
>       {"case": "tsb_tsb_owned_invalidate", "path": "/ticks/7/children/right/children/left/last", "previous_expected": "never", "expected": "never"},
>       {"case": "tsb_tsb_owned_invalidate", "path": "/ticks/7/children/right/children/left/value", "previous_expected": null, "expected": null},
>       {"case": "tsb_tsb_owned_invalidate", "path": "/ticks/7/children/right/children/left/delta", "previous_expected": null, "expected": null},
>       {"case": "tsb_tsb_owned_invalidate", "path": "/ticks/7/children/right/children/right/valid", "previous_expected": false, "expected": false},
>       {"case": "tsb_tsb_owned_invalidate", "path": "/ticks/7/children/right/children/right/modified", "previous_expected": false, "expected": false},
>       {"case": "tsb_tsb_owned_invalidate", "path": "/ticks/7/children/right/children/right/last", "previous_expected": "never", "expected": "never"},
>       {"case": "tsb_tsb_owned_invalidate", "path": "/ticks/7/children/right/children/right/value", "previous_expected": null, "expected": null},
>       {"case": "tsb_tsb_owned_invalidate", "path": "/ticks/7/children/right/children/right/delta", "previous_expected": null, "expected": null},
>       {"case": "tsb_tsb_owned_invalidate", "path": "/ticks/8/valid", "previous_expected": false, "expected": false},
>       {"case": "tsb_tsb_owned_invalidate", "path": "/ticks/8/all_valid", "previous_expected": false, "expected": false},
>       {"case": "tsb_tsb_owned_invalidate", "path": "/ticks/8/modified", "previous_expected": false, "expected": false},
>       {"case": "tsb_tsb_owned_invalidate", "path": "/ticks/8/last", "previous_expected": "never", "expected": "never"},
>       {"case": "tsb_tsb_owned_invalidate", "path": "/ticks/8/value", "previous_expected": null, "expected": null},
>       {"case": "tsb_tsb_owned_invalidate", "path": "/ticks/8/delta", "previous_expected": null, "expected": null},
>       {"case": "tsb_tsb_owned_invalidate", "path": "/ticks/8/peer", "previous_expected": true, "expected": true},
>       {"case": "tsb_tsb_owned_invalidate", "path": "/ticks/8/children", "previous_expected": ["left", "right"], "expected": ["left", "right"]},
>       {"case": "tsb_tsb_owned_invalidate", "path": "/ticks/8/children/left/valid", "previous_expected": false, "expected": false},
>       {"case": "tsb_tsb_owned_invalidate", "path": "/ticks/8/children/left/all_valid", "previous_expected": false, "expected": false},
>       {"case": "tsb_tsb_owned_invalidate", "path": "/ticks/8/children/left/modified", "previous_expected": false, "expected": false},
>       {"case": "tsb_tsb_owned_invalidate", "path": "/ticks/8/children/left/last", "previous_expected": "never", "expected": "never"},
>       {"case": "tsb_tsb_owned_invalidate", "path": "/ticks/8/children/left/value", "previous_expected": null, "expected": null},
>       {"case": "tsb_tsb_owned_invalidate", "path": "/ticks/8/children/left/delta", "previous_expected": null, "expected": null},
>       {"case": "tsb_tsb_owned_invalidate", "path": "/ticks/8/children/left/peer", "previous_expected": true, "expected": true},
>       {"case": "tsb_tsb_owned_invalidate", "path": "/ticks/8/children/left/children", "previous_expected": ["left", "right"], "expected": ["left", "right"]},
>       {"case": "tsb_tsb_owned_invalidate", "path": "/ticks/8/children/left/children/left/valid", "previous_expected": false, "expected": false},
>       {"case": "tsb_tsb_owned_invalidate", "path": "/ticks/8/children/left/children/left/modified", "previous_expected": false, "expected": false},
>       {"case": "tsb_tsb_owned_invalidate", "path": "/ticks/8/children/left/children/left/last", "previous_expected": "never", "expected": "never"},
>       {"case": "tsb_tsb_owned_invalidate", "path": "/ticks/8/children/left/children/left/value", "previous_expected": null, "expected": null},
>       {"case": "tsb_tsb_owned_invalidate", "path": "/ticks/8/children/left/children/left/delta", "previous_expected": null, "expected": null},
>       {"case": "tsb_tsb_owned_invalidate", "path": "/ticks/8/children/left/children/right/valid", "previous_expected": false, "expected": false},
>       {"case": "tsb_tsb_owned_invalidate", "path": "/ticks/8/children/left/children/right/modified", "previous_expected": false, "expected": false},
>       {"case": "tsb_tsb_owned_invalidate", "path": "/ticks/8/children/left/children/right/last", "previous_expected": "never", "expected": "never"},
>       {"case": "tsb_tsb_owned_invalidate", "path": "/ticks/8/children/left/children/right/value", "previous_expected": null, "expected": null},
>       {"case": "tsb_tsb_owned_invalidate", "path": "/ticks/8/children/left/children/right/delta", "previous_expected": null, "expected": null},
>       {"case": "tsb_tsb_owned_invalidate", "path": "/ticks/8/children/right/valid", "previous_expected": false, "expected": false},
>       {"case": "tsb_tsb_owned_invalidate", "path": "/ticks/8/children/right/all_valid", "previous_expected": false, "expected": false},
>       {"case": "tsb_tsb_owned_invalidate", "path": "/ticks/8/children/right/modified", "previous_expected": false, "expected": false},
>       {"case": "tsb_tsb_owned_invalidate", "path": "/ticks/8/children/right/last", "previous_expected": "never", "expected": "never"},
>       {"case": "tsb_tsb_owned_invalidate", "path": "/ticks/8/children/right/value", "previous_expected": null, "expected": null},
>       {"case": "tsb_tsb_owned_invalidate", "path": "/ticks/8/children/right/delta", "previous_expected": null, "expected": null},
>       {"case": "tsb_tsb_owned_invalidate", "path": "/ticks/8/children/right/peer", "previous_expected": true, "expected": true},
>       {"case": "tsb_tsb_owned_invalidate", "path": "/ticks/8/children/right/children", "previous_expected": ["left", "right"], "expected": ["left", "right"]},
>       {"case": "tsb_tsb_owned_invalidate", "path": "/ticks/8/children/right/children/left/valid", "previous_expected": false, "expected": false},
>       {"case": "tsb_tsb_owned_invalidate", "path": "/ticks/8/children/right/children/left/modified", "previous_expected": false, "expected": false},
>       {"case": "tsb_tsb_owned_invalidate", "path": "/ticks/8/children/right/children/left/last", "previous_expected": "never", "expected": "never"},
>       {"case": "tsb_tsb_owned_invalidate", "path": "/ticks/8/children/right/children/left/value", "previous_expected": null, "expected": null},
>       {"case": "tsb_tsb_owned_invalidate", "path": "/ticks/8/children/right/children/left/delta", "previous_expected": null, "expected": null},
>       {"case": "tsb_tsb_owned_invalidate", "path": "/ticks/8/children/right/children/right/valid", "previous_expected": false, "expected": false},
>       {"case": "tsb_tsb_owned_invalidate", "path": "/ticks/8/children/right/children/right/modified", "previous_expected": false, "expected": false},
>       {"case": "tsb_tsb_owned_invalidate", "path": "/ticks/8/children/right/children/right/last", "previous_expected": "never", "expected": "never"},
>       {"case": "tsb_tsb_owned_invalidate", "path": "/ticks/8/children/right/children/right/value", "previous_expected": null, "expected": null},
>       {"case": "tsb_tsb_owned_invalidate", "path": "/ticks/8/children/right/children/right/delta", "previous_expected": null, "expected": null},
>       {"case": "tsb_tsb_assembled_invalidate", "path": "/ticks/7/valid", "previous_expected": false, "expected": false},
>       {"case": "tsb_tsb_assembled_invalidate", "path": "/ticks/7/all_valid", "previous_expected": false, "expected": false},
>       {"case": "tsb_tsb_assembled_invalidate", "path": "/ticks/7/modified", "previous_expected": false, "expected": false},
>       {"case": "tsb_tsb_assembled_invalidate", "path": "/ticks/7/last", "previous_expected": "never", "expected": "never"},
>       {"case": "tsb_tsb_assembled_invalidate", "path": "/ticks/7/value", "previous_expected": null, "expected": null},
>       {"case": "tsb_tsb_assembled_invalidate", "path": "/ticks/7/delta", "previous_expected": null, "expected": null},
>       {"case": "tsb_tsb_assembled_invalidate", "path": "/ticks/7/peer", "previous_expected": false, "expected": false},
>       {"case": "tsb_tsb_assembled_invalidate", "path": "/ticks/7/children", "previous_expected": ["left", "right"], "expected": ["left", "right"]},
>       {"case": "tsb_tsb_assembled_invalidate", "path": "/ticks/7/children/left/valid", "previous_expected": false, "expected": false},
>       {"case": "tsb_tsb_assembled_invalidate", "path": "/ticks/7/children/left/all_valid", "previous_expected": false, "expected": false},
>       {"case": "tsb_tsb_assembled_invalidate", "path": "/ticks/7/children/left/modified", "previous_expected": false, "expected": false},
>       {"case": "tsb_tsb_assembled_invalidate", "path": "/ticks/7/children/left/last", "previous_expected": "never", "expected": "never"},
>       {"case": "tsb_tsb_assembled_invalidate", "path": "/ticks/7/children/left/value", "previous_expected": null, "expected": null},
>       {"case": "tsb_tsb_assembled_invalidate", "path": "/ticks/7/children/left/delta", "previous_expected": null, "expected": null},
>       {"case": "tsb_tsb_assembled_invalidate", "path": "/ticks/7/children/left/peer", "previous_expected": false, "expected": false},
>       {"case": "tsb_tsb_assembled_invalidate", "path": "/ticks/7/children/left/children", "previous_expected": ["left", "right"], "expected": ["left", "right"]},
>       {"case": "tsb_tsb_assembled_invalidate", "path": "/ticks/7/children/left/children/left/valid", "previous_expected": false, "expected": false},
>       {"case": "tsb_tsb_assembled_invalidate", "path": "/ticks/7/children/left/children/left/modified", "previous_expected": false, "expected": false},
>       {"case": "tsb_tsb_assembled_invalidate", "path": "/ticks/7/children/left/children/left/last", "previous_expected": "never", "expected": "never"},
>       {"case": "tsb_tsb_assembled_invalidate", "path": "/ticks/7/children/left/children/left/value", "previous_expected": null, "expected": null},
>       {"case": "tsb_tsb_assembled_invalidate", "path": "/ticks/7/children/left/children/left/delta", "previous_expected": null, "expected": null},
>       {"case": "tsb_tsb_assembled_invalidate", "path": "/ticks/7/children/left/children/right/valid", "previous_expected": false, "expected": false},
>       {"case": "tsb_tsb_assembled_invalidate", "path": "/ticks/7/children/left/children/right/modified", "previous_expected": false, "expected": false},
>       {"case": "tsb_tsb_assembled_invalidate", "path": "/ticks/7/children/left/children/right/last", "previous_expected": "never", "expected": "never"},
>       {"case": "tsb_tsb_assembled_invalidate", "path": "/ticks/7/children/left/children/right/value", "previous_expected": null, "expected": null},
>       {"case": "tsb_tsb_assembled_invalidate", "path": "/ticks/7/children/left/children/right/delta", "previous_expected": null, "expected": null},
>       {"case": "tsb_tsb_assembled_invalidate", "path": "/ticks/7/children/right/valid", "previous_expected": false, "expected": false},
>       {"case": "tsb_tsb_assembled_invalidate", "path": "/ticks/7/children/right/all_valid", "previous_expected": false, "expected": false},
>       {"case": "tsb_tsb_assembled_invalidate", "path": "/ticks/7/children/right/modified", "previous_expected": false, "expected": false},
>       {"case": "tsb_tsb_assembled_invalidate", "path": "/ticks/7/children/right/last", "previous_expected": "never", "expected": "never"},
>       {"case": "tsb_tsb_assembled_invalidate", "path": "/ticks/7/children/right/value", "previous_expected": null, "expected": null},
>       {"case": "tsb_tsb_assembled_invalidate", "path": "/ticks/7/children/right/delta", "previous_expected": null, "expected": null},
>       {"case": "tsb_tsb_assembled_invalidate", "path": "/ticks/7/children/right/peer", "previous_expected": false, "expected": false},
>       {"case": "tsb_tsb_assembled_invalidate", "path": "/ticks/7/children/right/children", "previous_expected": ["left", "right"], "expected": ["left", "right"]},
>       {"case": "tsb_tsb_assembled_invalidate", "path": "/ticks/7/children/right/children/left/valid", "previous_expected": false, "expected": false},
>       {"case": "tsb_tsb_assembled_invalidate", "path": "/ticks/7/children/right/children/left/modified", "previous_expected": false, "expected": false},
>       {"case": "tsb_tsb_assembled_invalidate", "path": "/ticks/7/children/right/children/left/last", "previous_expected": "never", "expected": "never"},
>       {"case": "tsb_tsb_assembled_invalidate", "path": "/ticks/7/children/right/children/left/value", "previous_expected": null, "expected": null},
>       {"case": "tsb_tsb_assembled_invalidate", "path": "/ticks/7/children/right/children/left/delta", "previous_expected": null, "expected": null},
>       {"case": "tsb_tsb_assembled_invalidate", "path": "/ticks/7/children/right/children/right/valid", "previous_expected": false, "expected": false},
>       {"case": "tsb_tsb_assembled_invalidate", "path": "/ticks/7/children/right/children/right/modified", "previous_expected": false, "expected": false},
>       {"case": "tsb_tsb_assembled_invalidate", "path": "/ticks/7/children/right/children/right/last", "previous_expected": "never", "expected": "never"},
>       {"case": "tsb_tsb_assembled_invalidate", "path": "/ticks/7/children/right/children/right/value", "previous_expected": null, "expected": null},
>       {"case": "tsb_tsb_assembled_invalidate", "path": "/ticks/7/children/right/children/right/delta", "previous_expected": null, "expected": null},
>       {"case": "tsb_tsb_assembled_invalidate", "path": "/ticks/8/valid", "previous_expected": false, "expected": false},
>       {"case": "tsb_tsb_assembled_invalidate", "path": "/ticks/8/all_valid", "previous_expected": false, "expected": false},
>       {"case": "tsb_tsb_assembled_invalidate", "path": "/ticks/8/modified", "previous_expected": false, "expected": false},
>       {"case": "tsb_tsb_assembled_invalidate", "path": "/ticks/8/last", "previous_expected": "never", "expected": "never"},
>       {"case": "tsb_tsb_assembled_invalidate", "path": "/ticks/8/value", "previous_expected": null, "expected": null},
>       {"case": "tsb_tsb_assembled_invalidate", "path": "/ticks/8/delta", "previous_expected": null, "expected": null},
>       {"case": "tsb_tsb_assembled_invalidate", "path": "/ticks/8/peer", "previous_expected": false, "expected": false},
>       {"case": "tsb_tsb_assembled_invalidate", "path": "/ticks/8/children", "previous_expected": ["left", "right"], "expected": ["left", "right"]},
>       {"case": "tsb_tsb_assembled_invalidate", "path": "/ticks/8/children/left/valid", "previous_expected": false, "expected": false},
>       {"case": "tsb_tsb_assembled_invalidate", "path": "/ticks/8/children/left/all_valid", "previous_expected": false, "expected": false},
>       {"case": "tsb_tsb_assembled_invalidate", "path": "/ticks/8/children/left/modified", "previous_expected": false, "expected": false},
>       {"case": "tsb_tsb_assembled_invalidate", "path": "/ticks/8/children/left/last", "previous_expected": "never", "expected": "never"},
>       {"case": "tsb_tsb_assembled_invalidate", "path": "/ticks/8/children/left/value", "previous_expected": null, "expected": null},
>       {"case": "tsb_tsb_assembled_invalidate", "path": "/ticks/8/children/left/delta", "previous_expected": null, "expected": null},
>       {"case": "tsb_tsb_assembled_invalidate", "path": "/ticks/8/children/left/peer", "previous_expected": false, "expected": false},
>       {"case": "tsb_tsb_assembled_invalidate", "path": "/ticks/8/children/left/children", "previous_expected": ["left", "right"], "expected": ["left", "right"]},
>       {"case": "tsb_tsb_assembled_invalidate", "path": "/ticks/8/children/left/children/left/valid", "previous_expected": false, "expected": false},
>       {"case": "tsb_tsb_assembled_invalidate", "path": "/ticks/8/children/left/children/left/modified", "previous_expected": false, "expected": false},
>       {"case": "tsb_tsb_assembled_invalidate", "path": "/ticks/8/children/left/children/left/last", "previous_expected": "never", "expected": "never"},
>       {"case": "tsb_tsb_assembled_invalidate", "path": "/ticks/8/children/left/children/left/value", "previous_expected": null, "expected": null},
>       {"case": "tsb_tsb_assembled_invalidate", "path": "/ticks/8/children/left/children/left/delta", "previous_expected": null, "expected": null},
>       {"case": "tsb_tsb_assembled_invalidate", "path": "/ticks/8/children/left/children/right/valid", "previous_expected": false, "expected": false},
>       {"case": "tsb_tsb_assembled_invalidate", "path": "/ticks/8/children/left/children/right/modified", "previous_expected": false, "expected": false},
>       {"case": "tsb_tsb_assembled_invalidate", "path": "/ticks/8/children/left/children/right/last", "previous_expected": "never", "expected": "never"},
>       {"case": "tsb_tsb_assembled_invalidate", "path": "/ticks/8/children/left/children/right/value", "previous_expected": null, "expected": null},
>       {"case": "tsb_tsb_assembled_invalidate", "path": "/ticks/8/children/left/children/right/delta", "previous_expected": null, "expected": null},
>       {"case": "tsb_tsb_assembled_invalidate", "path": "/ticks/8/children/right/valid", "previous_expected": false, "expected": false},
>       {"case": "tsb_tsb_assembled_invalidate", "path": "/ticks/8/children/right/all_valid", "previous_expected": false, "expected": false},
>       {"case": "tsb_tsb_assembled_invalidate", "path": "/ticks/8/children/right/modified", "previous_expected": false, "expected": false},
>       {"case": "tsb_tsb_assembled_invalidate", "path": "/ticks/8/children/right/last", "previous_expected": "never", "expected": "never"},
>       {"case": "tsb_tsb_assembled_invalidate", "path": "/ticks/8/children/right/value", "previous_expected": null, "expected": null},
>       {"case": "tsb_tsb_assembled_invalidate", "path": "/ticks/8/children/right/delta", "previous_expected": null, "expected": null},
>       {"case": "tsb_tsb_assembled_invalidate", "path": "/ticks/8/children/right/peer", "previous_expected": false, "expected": false},
>       {"case": "tsb_tsb_assembled_invalidate", "path": "/ticks/8/children/right/children", "previous_expected": ["left", "right"], "expected": ["left", "right"]},
>       {"case": "tsb_tsb_assembled_invalidate", "path": "/ticks/8/children/right/children/left/valid", "previous_expected": false, "expected": false},
>       {"case": "tsb_tsb_assembled_invalidate", "path": "/ticks/8/children/right/children/left/modified", "previous_expected": false, "expected": false},
>       {"case": "tsb_tsb_assembled_invalidate", "path": "/ticks/8/children/right/children/left/last", "previous_expected": "never", "expected": "never"},
>       {"case": "tsb_tsb_assembled_invalidate", "path": "/ticks/8/children/right/children/left/value", "previous_expected": null, "expected": null},
>       {"case": "tsb_tsb_assembled_invalidate", "path": "/ticks/8/children/right/children/left/delta", "previous_expected": null, "expected": null},
>       {"case": "tsb_tsb_assembled_invalidate", "path": "/ticks/8/children/right/children/right/valid", "previous_expected": false, "expected": false},
>       {"case": "tsb_tsb_assembled_invalidate", "path": "/ticks/8/children/right/children/right/modified", "previous_expected": false, "expected": false},
>       {"case": "tsb_tsb_assembled_invalidate", "path": "/ticks/8/children/right/children/right/last", "previous_expected": "never", "expected": "never"},
>       {"case": "tsb_tsb_assembled_invalidate", "path": "/ticks/8/children/right/children/right/value", "previous_expected": null, "expected": null},
>       {"case": "tsb_tsb_assembled_invalidate", "path": "/ticks/8/children/right/children/right/delta", "previous_expected": null, "expected": null}

### Excerpt 4

[Source, line 889](https://github.com/hhenson/hgraph_spec/blob/b295f39c94403dc4093a1d8c009cdcc6f2549a24/runtime/validation/fixed/decisions.json#L889).

>       {"case": "tsl_ref_items", "path": "/ticks/4/data/delta", "previous_expected": {"1": 30}, "expected": {"1": 30}},
>       {"case": "tsl_ref_items", "path": "/ticks/4/data/children/0/valid", "previous_expected": true, "expected": true},
>       {"case": "tsl_ref_items", "path": "/ticks/4/data/children/0/modified", "previous_expected": false, "expected": false},
>       {"case": "tsl_ref_items", "path": "/ticks/4/data/children/0/last", "previous_expected": 3, "expected": 3},
>       {"case": "tsl_ref_items", "path": "/ticks/4/data/children/0/value", "previous_expected": 8, "expected": 8},
>       {"case": "tsl_ref_items", "path": "/ticks/4/data/children/0/delta", "previous_expected": null, "expected": null},
>       {"case": "tsb_ref_items", "path": "/ticks/4/data/delta", "previous_expected": {"right": 30}, "expected": {"right": 30}},
>       {"case": "tsb_ref_items", "path": "/ticks/4/data/children/left/valid", "previous_expected": true, "expected": true},
>       {"case": "tsb_ref_items", "path": "/ticks/4/data/children/left/modified", "previous_expected": false, "expected": false},
>       {"case": "tsb_ref_items", "path": "/ticks/4/data/children/left/last", "previous_expected": 3, "expected": 3},
>       {"case": "tsb_ref_items", "path": "/ticks/4/data/children/left/value", "previous_expected": 8, "expected": 8},
>       {"case": "tsb_ref_items", "path": "/ticks/4/data/children/left/delta", "previous_expected": null, "expected": null}

### Excerpt 5

[Source, line 913](https://github.com/hhenson/hgraph_spec/blob/b295f39c94403dc4093a1d8c009cdcc6f2549a24/runtime/validation/fixed/decisions.json#L913).

>       {"case": "tsl_tsb_ref", "path": "/ticks/4/delta", "previous_expected": {"0": {"left": 20, "right": 21}}, "expected": {"0": {"left": 20, "right": 21}}},
>       {"case": "tsl_tsb_ref", "path": "/ticks/4/children/1/valid", "previous_expected": false, "expected": false},
>       {"case": "tsl_tsb_ref", "path": "/ticks/4/children/1/all_valid", "previous_expected": false, "expected": false},
>       {"case": "tsl_tsb_ref", "path": "/ticks/4/children/1/modified", "previous_expected": false, "expected": false},
>       {"case": "tsl_tsb_ref", "path": "/ticks/4/children/1/last", "previous_expected": "never", "expected": "never"},
>       {"case": "tsl_tsb_ref", "path": "/ticks/4/children/1/value", "previous_expected": null, "expected": null},
>       {"case": "tsl_tsb_ref", "path": "/ticks/4/children/1/delta", "previous_expected": null, "expected": null},
>       {"case": "tsl_tsb_ref", "path": "/ticks/4/children/1/peer", "previous_expected": true, "expected": true},
>       {"case": "tsl_tsb_ref", "path": "/ticks/4/children/1/children", "previous_expected": ["left", "right"], "expected": ["left", "right"]},
>       {"case": "tsl_tsb_ref", "path": "/ticks/4/children/1/children/left/valid", "previous_expected": false, "expected": false},
>       {"case": "tsl_tsb_ref", "path": "/ticks/4/children/1/children/left/modified", "previous_expected": false, "expected": false},
>       {"case": "tsl_tsb_ref", "path": "/ticks/4/children/1/children/left/last", "previous_expected": "never", "expected": "never"},
>       {"case": "tsl_tsb_ref", "path": "/ticks/4/children/1/children/left/value", "previous_expected": null, "expected": null},
>       {"case": "tsl_tsb_ref", "path": "/ticks/4/children/1/children/left/delta", "previous_expected": null, "expected": null},
>       {"case": "tsl_tsb_ref", "path": "/ticks/4/children/1/children/right/valid", "previous_expected": false, "expected": false},
>       {"case": "tsl_tsb_ref", "path": "/ticks/4/children/1/children/right/modified", "previous_expected": false, "expected": false},
>       {"case": "tsl_tsb_ref", "path": "/ticks/4/children/1/children/right/last", "previous_expected": "never", "expected": "never"},
>       {"case": "tsl_tsb_ref", "path": "/ticks/4/children/1/children/right/value", "previous_expected": null, "expected": null},
>       {"case": "tsl_tsb_ref", "path": "/ticks/4/children/1/children/right/delta", "previous_expected": null, "expected": null},
>       {"case": "tsb_tsl_ref", "path": "/ticks/4/delta", "previous_expected": {"left": {"0": 20, "1": 21}}, "expected": {"left": {"0": 20, "1": 21}}},
>       {"case": "tsb_tsl_ref", "path": "/ticks/4/children/right/valid", "previous_expected": false, "expected": false},
>       {"case": "tsb_tsl_ref", "path": "/ticks/4/children/right/all_valid", "previous_expected": false, "expected": false},
>       {"case": "tsb_tsl_ref", "path": "/ticks/4/children/right/modified", "previous_expected": false, "expected": false},
>       {"case": "tsb_tsl_ref", "path": "/ticks/4/children/right/last", "previous_expected": "never", "expected": "never"},
>       {"case": "tsb_tsl_ref", "path": "/ticks/4/children/right/value", "previous_expected": null, "expected": null},
>       {"case": "tsb_tsl_ref", "path": "/ticks/4/children/right/delta", "previous_expected": null, "expected": null},
>       {"case": "tsb_tsl_ref", "path": "/ticks/4/children/right/peer", "previous_expected": true, "expected": true},
>       {"case": "tsb_tsl_ref", "path": "/ticks/4/children/right/children", "previous_expected": ["0", "1"], "expected": ["0", "1"]},
>       {"case": "tsb_tsl_ref", "path": "/ticks/4/children/right/children/0/valid", "previous_expected": false, "expected": false},
>       {"case": "tsb_tsl_ref", "path": "/ticks/4/children/right/children/0/modified", "previous_expected": false, "expected": false},
>       {"case": "tsb_tsl_ref", "path": "/ticks/4/children/right/children/0/last", "previous_expected": "never", "expected": "never"},
>       {"case": "tsb_tsl_ref", "path": "/ticks/4/children/right/children/0/value", "previous_expected": null, "expected": null},
>       {"case": "tsb_tsl_ref", "path": "/ticks/4/children/right/children/0/delta", "previous_expected": null, "expected": null},
>       {"case": "tsb_tsl_ref", "path": "/ticks/4/children/right/children/1/valid", "previous_expected": false, "expected": false},
>       {"case": "tsb_tsl_ref", "path": "/ticks/4/children/right/children/1/modified", "previous_expected": false, "expected": false},
>       {"case": "tsb_tsl_ref", "path": "/ticks/4/children/right/children/1/last", "previous_expected": "never", "expected": "never"},
>       {"case": "tsb_tsl_ref", "path": "/ticks/4/children/right/children/1/value", "previous_expected": null, "expected": null},
>       {"case": "tsb_tsl_ref", "path": "/ticks/4/children/right/children/1/delta", "previous_expected": null, "expected": null}

### Excerpt 6

[Source, line 966](https://github.com/hhenson/hgraph_spec/blob/b295f39c94403dc4093a1d8c009cdcc6f2549a24/runtime/validation/fixed/decisions.json#L966).

>       {"case": "tsl_assembled", "path": "/ticks/4/modified", "previous_expected": false, "expected": true},
>       {"case": "tsl_assembled", "path": "/ticks/4/last", "previous_expected": 2, "expected": 4},
>       {"case": "tsl_assembled", "path": "/ticks/4/delta", "previous_expected": null, "expected": {}},
>       {"case": "tsl_assembled", "path": "/ticks/4/children/0/modified", "previous_expected": false, "expected": true},
>       {"case": "tsl_assembled", "path": "/ticks/4/children/0/last", "previous_expected": "never", "expected": 4},
>       {"case": "tsl_assembled", "path": "/ticks/5/modified", "previous_expected": false, "expected": false},
>       {"case": "tsl_assembled", "path": "/ticks/5/last", "previous_expected": "never", "expected": "never"},
>       {"case": "tsl_assembled", "path": "/ticks/5/delta", "previous_expected": null, "expected": null},
>       {"case": "tsl_assembled", "path": "/ticks/5/children/0/modified", "previous_expected": false, "expected": false},
>       {"case": "tsl_assembled", "path": "/ticks/5/children/0/last", "previous_expected": "never", "expected": "never"},
>       {"case": "tsl_assembled", "path": "/ticks/5/children/0/delta", "previous_expected": null, "expected": null},
>       {"case": "tsl_assembled", "path": "/ticks/5/children/1/modified", "previous_expected": false, "expected": false},
>       {"case": "tsl_assembled", "path": "/ticks/5/children/1/last", "previous_expected": "never", "expected": "never"},
>       {"case": "tsl_assembled", "path": "/ticks/5/children/1/delta", "previous_expected": null, "expected": null},
>       {"case": "tsl_assembled", "path": "/ticks/7/modified", "previous_expected": false, "expected": false},
>       {"case": "tsl_assembled", "path": "/ticks/7/last", "previous_expected": "never", "expected": "never"},
>       {"case": "tsl_assembled", "path": "/ticks/7/delta", "previous_expected": null, "expected": null},
>       {"case": "tsl_assembled", "path": "/ticks/7/children/0/modified", "previous_expected": false, "expected": false},
>       {"case": "tsl_assembled", "path": "/ticks/7/children/0/last", "previous_expected": "never", "expected": "never"},
>       {"case": "tsl_assembled", "path": "/ticks/7/children/0/delta", "previous_expected": null, "expected": null},
>       {"case": "tsl_assembled", "path": "/ticks/7/children/1/modified", "previous_expected": false, "expected": false},
>       {"case": "tsl_assembled", "path": "/ticks/7/children/1/last", "previous_expected": "never", "expected": "never"},
>       {"case": "tsl_assembled", "path": "/ticks/7/children/1/delta", "previous_expected": null, "expected": null},
>       {"case": "tsl_assembled", "path": "/ticks/6/children/1/last", "previous_expected": "never", "expected": "never"},
>       {"case": "tsb_assembled", "path": "/ticks/4/modified", "previous_expected": false, "expected": true},
>       {"case": "tsb_assembled", "path": "/ticks/4/last", "previous_expected": 2, "expected": 4},
>       {"case": "tsb_assembled", "path": "/ticks/4/delta", "previous_expected": null, "expected": {}},
>       {"case": "tsb_assembled", "path": "/ticks/4/children/left/modified", "previous_expected": false, "expected": true},
>       {"case": "tsb_assembled", "path": "/ticks/4/children/left/last", "previous_expected": "never", "expected": 4},
>       {"case": "tsb_assembled", "path": "/ticks/5/modified", "previous_expected": false, "expected": false},
>       {"case": "tsb_assembled", "path": "/ticks/5/last", "previous_expected": "never", "expected": "never"},
>       {"case": "tsb_assembled", "path": "/ticks/5/delta", "previous_expected": null, "expected": null},
>       {"case": "tsb_assembled", "path": "/ticks/5/children/left/modified", "previous_expected": false, "expected": false},
>       {"case": "tsb_assembled", "path": "/ticks/5/children/left/last", "previous_expected": "never", "expected": "never"},
>       {"case": "tsb_assembled", "path": "/ticks/5/children/left/delta", "previous_expected": null, "expected": null},
>       {"case": "tsb_assembled", "path": "/ticks/5/children/right/modified", "previous_expected": false, "expected": false},
>       {"case": "tsb_assembled", "path": "/ticks/5/children/right/last", "previous_expected": "never", "expected": "never"},
>       {"case": "tsb_assembled", "path": "/ticks/5/children/right/delta", "previous_expected": null, "expected": null},
>       {"case": "tsb_assembled", "path": "/ticks/7/modified", "previous_expected": false, "expected": false},
>       {"case": "tsb_assembled", "path": "/ticks/7/last", "previous_expected": "never", "expected": "never"},
>       {"case": "tsb_assembled", "path": "/ticks/7/delta", "previous_expected": null, "expected": null},
>       {"case": "tsb_assembled", "path": "/ticks/7/children/left/modified", "previous_expected": false, "expected": false},
>       {"case": "tsb_assembled", "path": "/ticks/7/children/left/last", "previous_expected": "never", "expected": "never"},
>       {"case": "tsb_assembled", "path": "/ticks/7/children/left/delta", "previous_expected": null, "expected": null},
>       {"case": "tsb_assembled", "path": "/ticks/7/children/right/modified", "previous_expected": false, "expected": false},
>       {"case": "tsb_assembled", "path": "/ticks/7/children/right/last", "previous_expected": "never", "expected": "never"},
>       {"case": "tsb_assembled", "path": "/ticks/7/children/right/delta", "previous_expected": null, "expected": null},
>       {"case": "tsb_assembled", "path": "/ticks/6/children/right/last", "previous_expected": "never", "expected": "never"},
>       {"case": "tsl_latest_invalid", "path": "/ticks/2/modified", "previous_expected": false, "expected": true},
>       {"case": "tsl_latest_invalid", "path": "/ticks/2/last", "previous_expected": 0, "expected": 2},
>       {"case": "tsl_latest_invalid", "path": "/ticks/2/delta", "previous_expected": null, "expected": {}},
>       {"case": "tsl_latest_invalid", "path": "/ticks/2/children/1/modified", "previous_expected": false, "expected": true},
>       {"case": "tsl_latest_invalid", "path": "/ticks/2/children/1/last", "previous_expected": "never", "expected": 2},
>       {"case": "tsl_latest_invalid", "path": "/ticks/3/last", "previous_expected": 0, "expected": 2},
>       {"case": "tsl_latest_invalid", "path": "/ticks/3/children/1/last", "previous_expected": "never", "expected": 2},
>       {"case": "tsb_latest_invalid", "path": "/ticks/2/modified", "previous_expected": false, "expected": true},
>       {"case": "tsb_latest_invalid", "path": "/ticks/2/last", "previous_expected": 0, "expected": 2},
>       {"case": "tsb_latest_invalid", "path": "/ticks/2/delta", "previous_expected": null, "expected": {}},
>       {"case": "tsb_latest_invalid", "path": "/ticks/2/children/right/modified", "previous_expected": false, "expected": true},
>       {"case": "tsb_latest_invalid", "path": "/ticks/2/children/right/last", "previous_expected": "never", "expected": 2},
>       {"case": "tsb_latest_invalid", "path": "/ticks/3/last", "previous_expected": 0, "expected": 2},
>       {"case": "tsb_latest_invalid", "path": "/ticks/3/children/right/last", "previous_expected": "never", "expected": 2}

### Excerpt 7

[Source, line 964](https://github.com/hhenson/hgraph_spec/blob/b295f39c94403dc4093a1d8c009cdcc6f2549a24/runtime/validation/fixed/decisions.json#L964).

> retain the C++ child-change time and modification observation

## runtime/validation/fixed/reasoning_corrections.json

### Excerpt 1

[Source, line 1](https://github.com/hhenson/hgraph_spec/blob/b295f39c94403dc4093a1d8c009cdcc6f2549a24/runtime/validation/fixed/reasoning_corrections.json#L1).

> [
>   {"cases": ["tsl_ref_items", "tsb_ref_items"], "path": "/ticks/6/data/modified", "initial": true, "expected": false, "reason": "Both runtimes agree. Removing one child binding is not a child tick. An assembled parent is modified only when a remaining child is modified."},
>   {"cases": ["tsl_ref_items", "tsb_ref_items"], "path": "/ticks/6/data/last", "initial": 6, "expected": 5, "reason": "Both runtimes agree. The remaining child's observed time is 5. A binding notification is not itself a child modification time."},
>   {"cases": ["tsl_ref_items", "tsb_ref_items"], "path": "/ticks/6/data/delta", "initial": {}, "expected": null, "reason": "Both runtimes agree. The assembled parent is unmodified, so its delta is nil."},
>   {"cases": ["tsl_assembled", "tsb_assembled"], "path": "/ticks/4/modified", "initial": true, "expected": false, "reason": "The corrected assembled-input rule also applies to child invalidation. The invalid child is unmodified; the remaining child did not tick. Python agrees; C++ varies."},
>   {"cases": ["tsl_assembled", "tsb_assembled"], "path": "/ticks/4/last", "initial": 4, "expected": 2, "reason": "The corrected assembled-input rule derives time from current children. The valid sibling last ticked at 2. Python agrees; C++ varies."},
>   {"cases": ["tsl_assembled", "tsb_assembled"], "path": "/ticks/4/delta", "initial": {}, "expected": null, "reason": "The corrected assembled-input rule leaves this parent unmodified. Python agrees; C++ varies."}
> ]

## runtime/validation/descriptions/reasoned.json

### Excerpt 1

[Source, line 1](https://github.com/hhenson/hgraph_spec/blob/b295f39c94403dc4093a1d8c009cdcc6f2549a24/runtime/validation/descriptions/reasoned.json#L1).

> {
>   "status": "Reasoned before reference execution; previously accepted rules apply.",
>   "cases": {
>     "owned": {
>       "ticks": [
>         {
>           "a": {
>             "valid": true,
>             "modified": true,
>             "last": 0,
>             "value": {
>               "left": [
>                 2,
>                 null
>               ],
>               "right": null
>             },
>             "delta": {
>               "left": {
>                 "0": 2
>               }
>             },
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": true,
>                 "last": 0,
>                 "value": [
>                   2,
>                   null
>                 ],
>                 "delta": {
>                   "0": 2
>                 },
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": true,
>                     "last": 0,
>                     "value": 2,
>                     "delta": 2
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": true
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": true
>               }
>             },
>             "peer": true
>           },
>           "b": {
>             "valid": true,
>             "modified": true,
>             "last": 0,
>             "value": {
>               "left": [
>                 10,
>                 null
>               ],
>               "right": null
>             },
>             "delta": {
>               "left": {
>                 "0": 10
>               }
>             },
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": true,
>                 "last": 0,
>                 "value": [
>                   10,
>                   null
>                 ],
>                 "delta": {
>                   "0": 10
>                 },
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": true,
>                     "last": 0,
>                     "value": 10,
>                     "delta": 10
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": true
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": true
>               }
>             },
>             "peer": true
>           },
>           "keys": [
>             0
>           ],
>           "added": [
>             0
>           ],
>           "removed": [],
>           "rows": {
>             "0": {
>               "valid": true,
>               "modified": true,
>               "last": 0,
>               "value": {
>                 "left": [
>                   2,
>                   null
>                 ],
>                 "right": null
>               },
>               "delta": {
>                 "left": {
>                   "0": 2
>                 }
>               },
>               "all_valid": false,
>               "children": {
>                 "left": {
>                   "valid": true,
>                   "modified": true,
>                   "last": 0,
>                   "value": [
>                     2,
>                     null
>                   ],
>                   "delta": {
>                     "0": 2
>                   },
>                   "all_valid": false,
>                   "children": {
>                     "0": {
>                       "valid": true,
>                       "modified": true,
>                       "last": 0,
>                       "value": 2,
>                       "delta": 2
>                     },
>                     "1": {
>                       "valid": false,
>                       "modified": false,
>                       "last": "never",
>                       "value": null,
>                       "delta": null
>                     }
>                   },
>                   "peer": true
>                 },
>                 "right": {
>                   "valid": false,
>                   "modified": false,
>                   "last": "never",
>                   "value": null,
>                   "delta": null,
>                   "all_valid": false,
>                   "children": {
>                     "0": {
>                       "valid": false,
>                       "modified": false,
>                       "last": "never",
>                       "value": null,
>                       "delta": null
>                     },
>                     "1": {
>                       "valid": false,
>                       "modified": false,
>                       "last": "never",
>                       "value": null,
>                       "delta": null
>                     }
>                   },
>                   "peer": true
>                 }
>               },
>               "peer": true
>             }
>           },
>           "retired": {}
>         },
>         {
>           "a": {
>             "valid": true,
>             "modified": true,
>             "last": 1,
>             "value": {
>               "left": [
>                 3,
>                 null
>               ],
>               "right": null
>             },
>             "delta": {
>               "left": {
>                 "0": 3
>               }
>             },
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": true,
>                 "last": 1,
>                 "value": [
>                   3,
>                   null
>                 ],
>                 "delta": {
>                   "0": 3
>                 },
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": true,
>                     "last": 1,
>                     "value": 3,
>                     "delta": 3
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": true
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": true
>               }
>             },
>             "peer": true
>           },
>           "b": {
>             "valid": true,
>             "modified": false,
>             "last": 0,
>             "value": {
>               "left": [
>                 10,
>                 null
>               ],
>               "right": null
>             },
>             "delta": null,
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": false,
>                 "last": 0,
>                 "value": [
>                   10,
>                   null
>                 ],
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": false,
>                     "last": 0,
>                     "value": 10,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": true
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": true
>               }
>             },
>             "peer": true
>           },
>           "keys": [
>             0
>           ],
>           "added": [],
>           "removed": [],
>           "rows": {
>             "0": {
>               "valid": true,
>               "modified": true,
>               "last": 1,
>               "value": {
>                 "left": [
>                   5,
>                   null
>                 ],
>                 "right": null
>               },
>               "delta": {
>                 "left": {
>                   "0": 5
>                 }
>               },
>               "all_valid": false,
>               "children": {
>                 "left": {
>                   "valid": true,
>                   "modified": true,
>                   "last": 1,
>                   "value": [
>                     5,
>                     null
>                   ],
>                   "delta": {
>                     "0": 5
>                   },
>                   "all_valid": false,
>                   "children": {
>                     "0": {
>                       "valid": true,
>                       "modified": true,
>                       "last": 1,
>                       "value": 5,
>                       "delta": 5
>                     },
>                     "1": {
>                       "valid": false,
>                       "modified": false,
>                       "last": "never",
>                       "value": null,
>                       "delta": null
>                     }
>                   },
>                   "peer": true
>                 },
>                 "right": {
>                   "valid": false,
>                   "modified": false,
>                   "last": "never",
>                   "value": null,
>                   "delta": null,
>                   "all_valid": false,
>                   "children": {
>                     "0": {
>                       "valid": false,
>                       "modified": false,
>                       "last": "never",
>                       "value": null,
>                       "delta": null
>                     },
>                     "1": {
>                       "valid": false,
>                       "modified": false,
>                       "last": "never",
>                       "value": null,
>                       "delta": null
>                     }
>                   },
>                   "peer": true
>                 }
>               },
>               "peer": true
>             }
>           },
>           "retired": {}
>         },
>         {
>           "a": {
>             "valid": true,
>             "modified": false,
>             "last": 1,
>             "value": {
>               "left": [
>                 3,
>                 null
>               ],
>               "right": null
>             },
>             "delta": null,
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": false,
>                 "last": 1,
>                 "value": [
>                   3,
>                   null
>                 ],
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": false,
>                     "last": 1,
>                     "value": 3,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": true
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": true
>               }
>             },
>             "peer": true
>           },
>           "b": {
>             "valid": true,
>             "modified": false,
>             "last": 0,
>             "value": {
>               "left": [
>                 10,
>                 null
>               ],
>               "right": null
>             },
>             "delta": null,
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": false,
>                 "last": 0,
>                 "value": [
>                   10,
>                   null
>                 ],
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": false,
>                     "last": 0,
>                     "value": 10,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": true
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": true
>               }
>             },
>             "peer": true
>           },
>           "keys": [
>             0
>           ],
>           "added": [],
>           "removed": [],
>           "rows": {
>             "0": {
>               "valid": true,
>               "modified": true,
>               "last": 2,
>               "value": {
>                 "left": [
>                   15,
>                   null
>                 ],
>                 "right": null
>               },
>               "delta": {
>                 "left": {
>                   "0": 15
>                 }
>               },
>               "all_valid": false,
>               "children": {
>                 "left": {
>                   "valid": true,
>                   "modified": true,
>                   "last": 2,
>                   "value": [
>                     15,
>                     null
>                   ],
>                   "delta": {
>                     "0": 15
>                   },
>                   "all_valid": false,
>                   "children": {
>                     "0": {
>                       "valid": true,
>                       "modified": true,
>                       "last": 2,
>                       "value": 15,
>                       "delta": 15
>                     },
>                     "1": {
>                       "valid": false,
>                       "modified": false,
>                       "last": "never",
>                       "value": null,
>                       "delta": null
>                     }
>                   },
>                   "peer": true
>                 },
>                 "right": {
>                   "valid": false,
>                   "modified": false,
>                   "last": "never",
>                   "value": null,
>                   "delta": null,
>                   "all_valid": false,
>                   "children": {
>                     "0": {
>                       "valid": false,
>                       "modified": false,
>                       "last": "never",
>                       "value": null,
>                       "delta": null
>                     },
>                     "1": {
>                       "valid": false,
>                       "modified": false,
>                       "last": "never",
>                       "value": null,
>                       "delta": null
>                     }
>                   },
>                   "peer": true
>                 }
>               },
>               "peer": true
>             }
>           },
>           "retired": {}
>         },
>         {
>           "a": {
>             "valid": true,
>             "modified": true,
>             "last": 3,
>             "value": {
>               "left": [
>                 4,
>                 null
>               ],
>               "right": null
>             },
>             "delta": {
>               "left": {
>                 "0": 4
>               }
>             },
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": true,
>                 "last": 3,
>                 "value": [
>                   4,
>                   null
>                 ],
>                 "delta": {
>                   "0": 4
>                 },
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": true,
>                     "last": 3,
>                     "value": 4,
>                     "delta": 4
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": true
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": true
>               }
>             },
>             "peer": true
>           },
>           "b": {
>             "valid": true,
>             "modified": false,
>             "last": 0,
>             "value": {
>               "left": [
>                 10,
>                 null
>               ],
>               "right": null
>             },
>             "delta": null,
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": false,
>                 "last": 0,
>                 "value": [
>                   10,
>                   null
>                 ],
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": false,
>                     "last": 0,
>                     "value": 10,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": true
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": true
>               }
>             },
>             "peer": true
>           },
>           "keys": [
>             0
>           ],
>           "added": [],
>           "removed": [],
>           "rows": {
>             "0": {
>               "valid": true,
>               "modified": false,
>               "last": 2,
>               "value": {
>                 "left": [
>                   15,
>                   null
>                 ],
>                 "right": null
>               },
>               "delta": null,
>               "all_valid": false,
>               "children": {
>                 "left": {
>                   "valid": true,
>                   "modified": false,
>                   "last": 2,
>                   "value": [
>                     15,
>                     null
>                   ],
>                   "delta": null,
>                   "all_valid": false,
>                   "children": {
>                     "0": {
>                       "valid": true,
>                       "modified": false,
>                       "last": 2,
>                       "value": 15,
>                       "delta": null
>                     },
>                     "1": {
>                       "valid": false,
>                       "modified": false,
>                       "last": "never",
>                       "value": null,
>                       "delta": null
>                     }
>                   },
>                   "peer": true
>                 },
>                 "right": {
>                   "valid": false,
>                   "modified": false,
>                   "last": "never",
>                   "value": null,
>                   "delta": null,
>                   "all_valid": false,
>                   "children": {
>                     "0": {
>                       "valid": false,
>                       "modified": false,
>                       "last": "never",
>                       "value": null,
>                       "delta": null
>                     },
>                     "1": {
>                       "valid": false,
>                       "modified": false,
>                       "last": "never",
>                       "value": null,
>                       "delta": null
>                     }
>                   },
>                   "peer": true
>                 }
>               },
>               "peer": true
>             }
>           },
>           "retired": {}
>         },
>         {
>           "a": {
>             "valid": true,
>             "modified": false,
>             "last": 3,
>             "value": {
>               "left": [
>                 4,
>                 null
>               ],
>               "right": null
>             },
>             "delta": null,
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": false,
>                 "last": 3,
>                 "value": [
>                   4,
>                   null
>                 ],
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": false,
>                     "last": 3,
>                     "value": 4,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": true
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": true
>               }
>             },
>             "peer": true
>           },
>           "b": {
>             "valid": true,
>             "modified": false,
>             "last": 0,
>             "value": {
>               "left": [
>                 10,
>                 null
>               ],
>               "right": null
>             },
>             "delta": null,
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": false,
>                 "last": 0,
>                 "value": [
>                   10,
>                   null
>                 ],
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": false,
>                     "last": 0,
>                     "value": 10,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": true
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": true
>               }
>             },
>             "peer": true
>           },
>           "keys": [
>             0
>           ],
>           "added": [],
>           "removed": [],
>           "rows": {
>             "0": {
>               "valid": true,
>               "modified": true,
>               "last": 4,
>               "value": {
>                 "left": [
>                   -15,
>                   null
>                 ],
>                 "right": null
>               },
>               "delta": {
>                 "left": {
>                   "0": -15
>                 }
>               },
>               "all_valid": false,
>               "children": {
>                 "left": {
>                   "valid": true,
>                   "modified": true,
>                   "last": 4,
>                   "value": [
>                     -15,
>                     null
>                   ],
>                   "delta": {
>                     "0": -15
>                   },
>                   "all_valid": false,
>                   "children": {
>                     "0": {
>                       "valid": true,
>                       "modified": true,
>                       "last": 4,
>                       "value": -15,
>                       "delta": -15
>                     },
>                     "1": {
>                       "valid": false,
>                       "modified": false,
>                       "last": "never",
>                       "value": null,
>                       "delta": null
>                     }
>                   },
>                   "peer": true
>                 },
>                 "right": {
>                   "valid": false,
>                   "modified": false,
>                   "last": "never",
>                   "value": null,
>                   "delta": null,
>                   "all_valid": false,
>                   "children": {
>                     "0": {
>                       "valid": false,
>                       "modified": false,
>                       "last": "never",
>                       "value": null,
>                       "delta": null
>                     },
>                     "1": {
>                       "valid": false,
>                       "modified": false,
>                       "last": "never",
>                       "value": null,
>                       "delta": null
>                     }
>                   },
>                   "peer": true
>                 }
>               },
>               "peer": true
>             }
>           },
>           "retired": {}
>         },
>         {
>           "a": {
>             "valid": true,
>             "modified": false,
>             "last": 3,
>             "value": {
>               "left": [
>                 4,
>                 null
>               ],
>               "right": null
>             },
>             "delta": null,
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": false,
>                 "last": 3,
>                 "value": [
>                   4,
>                   null
>                 ],
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": false,
>                     "last": 3,
>                     "value": 4,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": true
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": true
>               }
>             },
>             "peer": true
>           },
>           "b": {
>             "valid": true,
>             "modified": false,
>             "last": 0,
>             "value": {
>               "left": [
>                 10,
>                 null
>               ],
>               "right": null
>             },
>             "delta": null,
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": false,
>                 "last": 0,
>                 "value": [
>                   10,
>                   null
>                 ],
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": false,
>                     "last": 0,
>                     "value": 10,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": true
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": true
>               }
>             },
>             "peer": true
>           },
>           "keys": [],
>           "added": [],
>           "removed": [
>             0
>           ],
>           "rows": {},
>           "retired": {
>             "0": {
>               "valid": true,
>               "modified": false,
>               "last": 4,
>               "value": {
>                 "left": [
>                   -15,
>                   null
>                 ],
>                 "right": null
>               },
>               "delta": null,
>               "all_valid": false,
>               "children": {
>                 "left": {
>                   "valid": true,
>                   "modified": false,
>                   "last": 4,
>                   "value": [
>                     -15,
>                     null
>                   ],
>                   "delta": null,
>                   "all_valid": false,
>                   "children": {
>                     "0": {
>                       "valid": true,
>                       "modified": false,
>                       "last": 4,
>                       "value": -15,
>                       "delta": null
>                     },
>                     "1": {
>                       "valid": false,
>                       "modified": false,
>                       "last": "never",
>                       "value": null,
>                       "delta": null
>                     }
>                   },
>                   "peer": true
>                 },
>                 "right": {
>                   "valid": false,
>                   "modified": false,
>                   "last": "never",
>                   "value": null,
>                   "delta": null,
>                   "all_valid": false,
>                   "children": {
>                     "0": {
>                       "valid": false,
>                       "modified": false,
>                       "last": "never",
>                       "value": null,
>                       "delta": null
>                     },
>                     "1": {
>                       "valid": false,
>                       "modified": false,
>                       "last": "never",
>                       "value": null,
>                       "delta": null
>                     }
>                   },
>                   "peer": true
>                 }
>               },
>               "peer": true
>             }
>           }
>         },
>         {
>           "a": {
>             "valid": true,
>             "modified": true,
>             "last": 6,
>             "value": {
>               "left": [
>                 5,
>                 null
>               ],
>               "right": null
>             },
>             "delta": {
>               "left": {
>                 "0": 5
>               }
>             },
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": true,
>                 "last": 6,
>                 "value": [
>                   5,
>                   null
>                 ],
>                 "delta": {
>                   "0": 5
>                 },
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": true,
>                     "last": 6,
>                     "value": 5,
>                     "delta": 5
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": true
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": true
>               }
>             },
>             "peer": true
>           },
>           "b": {
>             "valid": true,
>             "modified": false,
>             "last": 0,
>             "value": {
>               "left": [
>                 10,
>                 null
>               ],
>               "right": null
>             },
>             "delta": null,
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": false,
>                 "last": 0,
>                 "value": [
>                   10,
>                   null
>                 ],
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": false,
>                     "last": 0,
>                     "value": 10,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": true
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": true
>               }
>             },
>             "peer": true
>           },
>           "keys": [],
>           "added": [],
>           "removed": [],
>           "rows": {},
>           "retired": {}
>         },
>         {
>           "a": {
>             "valid": true,
>             "modified": false,
>             "last": 6,
>             "value": {
>               "left": [
>                 5,
>                 null
>               ],
>               "right": null
>             },
>             "delta": null,
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": false,
>                 "last": 6,
>                 "value": [
>                   5,
>                   null
>                 ],
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": false,
>                     "last": 6,
>                     "value": 5,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": true
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": true
>               }
>             },
>             "peer": true
>           },
>           "b": {
>             "valid": true,
>             "modified": false,
>             "last": 0,
>             "value": {
>               "left": [
>                 10,
>                 null
>               ],
>               "right": null
>             },
>             "delta": null,
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": false,
>                 "last": 0,
>                 "value": [
>                   10,
>                   null
>                 ],
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": false,
>                     "last": 0,
>                     "value": 10,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": true
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": true
>               }
>             },
>             "peer": true
>           },
>           "keys": [
>             0
>           ],
>           "added": [
>             0
>           ],
>           "removed": [],
>           "rows": {
>             "0": {
>               "valid": true,
>               "modified": true,
>               "last": 7,
>               "value": {
>                 "left": [
>                   5,
>                   null
>                 ],
>                 "right": null
>               },
>               "delta": {
>                 "left": {
>                   "0": 5
>                 }
>               },
>               "all_valid": false,
>               "children": {
>                 "left": {
>                   "valid": true,
>                   "modified": true,
>                   "last": 7,
>                   "value": [
>                     5,
>                     null
>                   ],
>                   "delta": {
>                     "0": 5
>                   },
>                   "all_valid": false,
>                   "children": {
>                     "0": {
>                       "valid": true,
>                       "modified": true,
>                       "last": 7,
>                       "value": 5,
>                       "delta": 5
>                     },
>                     "1": {
>                       "valid": false,
>                       "modified": false,
>                       "last": "never",
>                       "value": null,
>                       "delta": null
>                     }
>                   },
>                   "peer": true
>                 },
>                 "right": {
>                   "valid": false,
>                   "modified": false,
>                   "last": "never",
>                   "value": null,
>                   "delta": null,
>                   "all_valid": false,
>                   "children": {
>                     "0": {
>                       "valid": false,
>                       "modified": false,
>                       "last": "never",
>                       "value": null,
>                       "delta": null
>                     },
>                     "1": {
>                       "valid": false,
>                       "modified": false,
>                       "last": "never",
>                       "value": null,
>                       "delta": null
>                     }
>                   },
>                   "peer": true
>                 }
>               },
>               "peer": true
>             }
>           },
>           "retired": {}
>         },
>         {
>           "a": {
>             "valid": true,
>             "modified": false,
>             "last": 6,
>             "value": {
>               "left": [
>                 5,
>                 null
>               ],
>               "right": null
>             },
>             "delta": null,
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": false,
>                 "last": 6,
>                 "value": [
>                   5,
>                   null
>                 ],
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": false,
>                     "last": 6,
>                     "value": 5,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": true
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": true
>               }
>             },
>             "peer": true
>           },
>           "b": {
>             "valid": true,
>             "modified": false,
>             "last": 0,
>             "value": {
>               "left": [
>                 10,
>                 null
>               ],
>               "right": null
>             },
>             "delta": null,
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": false,
>                 "last": 0,
>                 "value": [
>                   10,
>                   null
>                 ],
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": false,
>                     "last": 0,
>                     "value": 10,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": true
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": true
>               }
>             },
>             "peer": true
>           },
>           "keys": [
>             0
>           ],
>           "added": [],
>           "removed": [],
>           "rows": {
>             "0": {
>               "valid": true,
>               "modified": false,
>               "last": 7,
>               "value": {
>                 "left": [
>                   5,
>                   null
>                 ],
>                 "right": null
>               },
>               "delta": null,
>               "all_valid": false,
>               "children": {
>                 "left": {
>                   "valid": true,
>                   "modified": false,
>                   "last": 7,
>                   "value": [
>                     5,
>                     null
>                   ],
>                   "delta": null,
>                   "all_valid": false,
>                   "children": {
>                     "0": {
>                       "valid": true,
>                       "modified": false,
>                       "last": 7,
>                       "value": 5,
>                       "delta": null
>                     },
>                     "1": {
>                       "valid": false,
>                       "modified": false,
>                       "last": "never",
>                       "value": null,
>                       "delta": null
>                     }
>                   },
>                   "peer": true
>                 },
>                 "right": {
>                   "valid": false,
>                   "modified": false,
>                   "last": "never",
>                   "value": null,
>                   "delta": null,
>                   "all_valid": false,
>                   "children": {
>                     "0": {
>                       "valid": false,
>                       "modified": false,
>                       "last": "never",
>                       "value": null,
>                       "delta": null
>                     },
>                     "1": {
>                       "valid": false,
>                       "modified": false,
>                       "last": "never",
>                       "value": null,
>                       "delta": null
>                     }
>                   },
>                   "peer": true
>                 }
>               },
>               "peer": true
>             }
>           },
>           "retired": {}
>         },
>         {
>           "a": {
>             "valid": true,
>             "modified": false,
>             "last": 6,
>             "value": {
>               "left": [
>                 5,
>                 null
>               ],
>               "right": null
>             },
>             "delta": null,
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": false,
>                 "last": 6,
>                 "value": [
>                   5,
>                   null
>                 ],
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": false,
>                     "last": 6,
>                     "value": 5,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": true
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": true
>               }
>             },
>             "peer": true
>           },
>           "b": {
>             "valid": true,
>             "modified": false,
>             "last": 0,
>             "value": {
>               "left": [
>                 10,
>                 null
>               ],
>               "right": null
>             },
>             "delta": null,
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": false,
>                 "last": 0,
>                 "value": [
>                   10,
>                   null
>                 ],
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": false,
>                     "last": 0,
>                     "value": 10,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": true
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": true
>               }
>             },
>             "peer": true
>           },
>           "keys": [
>             0
>           ],
>           "added": [],
>           "removed": [],
>           "rows": {
>             "0": {
>               "valid": true,
>               "modified": true,
>               "last": 9,
>               "value": {
>                 "left": [
>                   -5,
>                   null
>                 ],
>                 "right": null
>               },
>               "delta": {
>                 "left": {
>                   "0": -5
>                 }
>               },
>               "all_valid": false,
>               "children": {
>                 "left": {
>                   "valid": true,
>                   "modified": true,
>                   "last": 9,
>                   "value": [
>                     -5,
>                     null
>                   ],
>                   "delta": {
>                     "0": -5
>                   },
>                   "all_valid": false,
>                   "children": {
>                     "0": {
>                       "valid": true,
>                       "modified": true,
>                       "last": 9,
>                       "value": -5,
>                       "delta": -5
>                     },
>                     "1": {
>                       "valid": false,
>                       "modified": false,
>                       "last": "never",
>                       "value": null,
>                       "delta": null
>                     }
>                   },
>                   "peer": true
>                 },
>                 "right": {
>                   "valid": false,
>                   "modified": false,
>                   "last": "never",
>                   "value": null,
>                   "delta": null,
>                   "all_valid": false,
>                   "children": {
>                     "0": {
>                       "valid": false,
>                       "modified": false,
>                       "last": "never",
>                       "value": null,
>                       "delta": null
>                     },
>                     "1": {
>                       "valid": false,
>                       "modified": false,
>                       "last": "never",
>                       "value": null,
>                       "delta": null
>                     }
>                   },
>                   "peer": true
>                 }
>               },
>               "peer": true
>             }
>           },
>           "retired": {}
>         },
>         {
>           "a": {
>             "valid": true,
>             "modified": false,
>             "last": 6,
>             "value": {
>               "left": [
>                 5,
>                 null
>               ],
>               "right": null
>             },
>             "delta": null,
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": false,
>                 "last": 6,
>                 "value": [
>                   5,
>                   null
>                 ],
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": false,
>                     "last": 6,
>                     "value": 5,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": true
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": true
>               }
>             },
>             "peer": true
>           },
>           "b": {
>             "valid": true,
>             "modified": false,
>             "last": 0,
>             "value": {
>               "left": [
>                 10,
>                 null
>               ],
>               "right": null
>             },
>             "delta": null,
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": false,
>                 "last": 0,
>                 "value": [
>                   10,
>                   null
>                 ],
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": false,
>                     "last": 0,
>                     "value": 10,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": true
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": true
>               }
>             },
>             "peer": true
>           },
>           "keys": [
>             0
>           ],
>           "added": [],
>           "removed": [],
>           "rows": {
>             "0": {
>               "valid": true,
>               "modified": false,
>               "last": 9,
>               "value": {
>                 "left": [
>                   -5,
>                   null
>                 ],
>                 "right": null
>               },
>               "delta": null,
>               "all_valid": false,
>               "children": {
>                 "left": {
>                   "valid": true,
>                   "modified": false,
>                   "last": 9,
>                   "value": [
>                     -5,
>                     null
>                   ],
>                   "delta": null,
>                   "all_valid": false,
>                   "children": {
>                     "0": {
>                       "valid": true,
>                       "modified": false,
>                       "last": 9,
>                       "value": -5,
>                       "delta": null
>                     },
>                     "1": {
>                       "valid": false,
>                       "modified": false,
>                       "last": "never",
>                       "value": null,
>                       "delta": null
>                     }
>                   },
>                   "peer": true
>                 },
>                 "right": {
>                   "valid": false,
>                   "modified": false,
>                   "last": "never",
>                   "value": null,
>                   "delta": null,
>                   "all_valid": false,
>                   "children": {
>                     "0": {
>                       "valid": false,
>                       "modified": false,
>                       "last": "never",
>                       "value": null,
>                       "delta": null
>                     },
>                     "1": {
>                       "valid": false,
>                       "modified": false,
>                       "last": "never",
>                       "value": null,
>                       "delta": null
>                     }
>                   },
>                   "peer": true
>                 }
>               },
>               "peer": true
>             }
>           },
>           "retired": {}
>         }
>       ],
>       "child_ticks": [
>         {
>           "time": 0,
>           "input": {
>             "valid": true,
>             "modified": true,
>             "last": 0,
>             "value": {
>               "left": [
>                 2,
>                 null
>               ],
>               "right": null
>             },
>             "delta": {
>               "left": {
>                 "0": 2
>               }
>             },
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": true,
>                 "last": 0,
>                 "value": [
>                   2,
>                   null
>                 ],
>                 "delta": {
>                   "0": 2
>                 },
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": true,
>                     "last": 0,
>                     "value": 2,
>                     "delta": 2
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": true
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": true
>               }
>             },
>             "peer": true
>           },
>           "output": {
>             "valid": true,
>             "modified": true,
>             "last": 0,
>             "value": {
>               "left": [
>                 2,
>                 null
>               ],
>               "right": null
>             },
>             "delta": {
>               "left": {
>                 "0": 2
>               }
>             },
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": true,
>                 "last": 0,
>                 "value": [
>                   2,
>                   null
>                 ],
>                 "delta": {
>                   "0": 2
>                 },
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": true,
>                     "last": 0,
>                     "value": 2,
>                     "delta": 2
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 }
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 }
>               }
>             }
>           }
>         },
>         {
>           "time": 1,
>           "input": {
>             "valid": true,
>             "modified": true,
>             "last": 1,
>             "value": {
>               "left": [
>                 3,
>                 null
>               ],
>               "right": null
>             },
>             "delta": {
>               "left": {
>                 "0": 3
>               }
>             },
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": true,
>                 "last": 1,
>                 "value": [
>                   3,
>                   null
>                 ],
>                 "delta": {
>                   "0": 3
>                 },
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": true,
>                     "last": 1,
>                     "value": 3,
>                     "delta": 3
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": true
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": true
>               }
>             },
>             "peer": true
>           },
>           "output": {
>             "valid": true,
>             "modified": true,
>             "last": 1,
>             "value": {
>               "left": [
>                 5,
>                 null
>               ],
>               "right": null
>             },
>             "delta": {
>               "left": {
>                 "0": 5
>               }
>             },
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": true,
>                 "last": 1,
>                 "value": [
>                   5,
>                   null
>                 ],
>                 "delta": {
>                   "0": 5
>                 },
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": true,
>                     "last": 1,
>                     "value": 5,
>                     "delta": 5
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 }
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 }
>               }
>             }
>           }
>         },
>         {
>           "time": 2,
>           "input": {
>             "valid": true,
>             "modified": true,
>             "last": 2,
>             "value": {
>               "left": [
>                 10,
>                 null
>               ],
>               "right": null
>             },
>             "delta": {
>               "left": {
>                 "0": 10
>               }
>             },
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": true,
>                 "last": 2,
>                 "value": [
>                   10,
>                   null
>                 ],
>                 "delta": {
>                   "0": 10
>                 },
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": true,
>                     "last": 2,
>                     "value": 10,
>                     "delta": 10
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": true
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": true
>               }
>             },
>             "peer": true
>           },
>           "output": {
>             "valid": true,
>             "modified": true,
>             "last": 2,
>             "value": {
>               "left": [
>                 15,
>                 null
>               ],
>               "right": null
>             },
>             "delta": {
>               "left": {
>                 "0": 15
>               }
>             },
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": true,
>                 "last": 2,
>                 "value": [
>                   15,
>                   null
>                 ],
>                 "delta": {
>                   "0": 15
>                 },
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": true,
>                     "last": 2,
>                     "value": 15,
>                     "delta": 15
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 }
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 }
>               }
>             }
>           }
>         },
>         {
>           "time": 4,
>           "input": {
>             "valid": true,
>             "modified": false,
>             "last": 2,
>             "value": {
>               "left": [
>                 10,
>                 null
>               ],
>               "right": null
>             },
>             "delta": null,
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": false,
>                 "last": 2,
>                 "value": [
>                   10,
>                   null
>                 ],
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": false,
>                     "last": 2,
>                     "value": 10,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": true
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": true
>               }
>             },
>             "peer": true
>           },
>           "output": {
>             "valid": true,
>             "modified": true,
>             "last": 4,
>             "value": {
>               "left": [
>                 -15,
>                 null
>               ],
>               "right": null
>             },
>             "delta": {
>               "left": {
>                 "0": -15
>               }
>             },
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": true,
>                 "last": 4,
>                 "value": [
>                   -15,
>                   null
>                 ],
>                 "delta": {
>                   "0": -15
>                 },
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": true,
>                     "last": 4,
>                     "value": -15,
>                     "delta": -15
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 }
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 }
>               }
>             }
>           }
>         },
>         {
>           "time": 7,
>           "input": {
>             "valid": true,
>             "modified": true,
>             "last": 7,
>             "value": {
>               "left": [
>                 5,
>                 null
>               ],
>               "right": null
>             },
>             "delta": {
>               "left": {
>                 "0": 5
>               }
>             },
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": true,
>                 "last": 7,
>                 "value": [
>                   5,
>                   null
>                 ],
>                 "delta": {
>                   "0": 5
>                 },
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": true,
>                     "last": 7,
>                     "value": 5,
>                     "delta": 5
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": true
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": true
>               }
>             },
>             "peer": true
>           },
>           "output": {
>             "valid": true,
>             "modified": true,
>             "last": 7,
>             "value": {
>               "left": [
>                 5,
>                 null
>               ],
>               "right": null
>             },
>             "delta": {
>               "left": {
>                 "0": 5
>               }
>             },
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": true,
>                 "last": 7,
>                 "value": [
>                   5,
>                   null
>                 ],
>                 "delta": {
>                   "0": 5
>                 },
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": true,
>                     "last": 7,
>                     "value": 5,
>                     "delta": 5
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 }
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 }
>               }
>             }
>           }
>         },
>         {
>           "time": 9,
>           "input": {
>             "valid": true,
>             "modified": false,
>             "last": 7,
>             "value": {
>               "left": [
>                 5,
>                 null
>               ],
>               "right": null
>             },
>             "delta": null,
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": false,
>                 "last": 7,
>                 "value": [
>                   5,
>                   null
>                 ],
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": false,
>                     "last": 7,
>                     "value": 5,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": true
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": true
>               }
>             },
>             "peer": true
>           },
>           "output": {
>             "valid": true,
>             "modified": true,
>             "last": 9,
>             "value": {
>               "left": [
>                 -5,
>                 null
>               ],
>               "right": null
>             },
>             "delta": {
>               "left": {
>                 "0": -5
>               }
>             },
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": true,
>                 "last": 9,
>                 "value": [
>                   -5,
>                   null
>                 ],
>                 "delta": {
>                   "0": -5
>                 },
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": true,
>                     "last": 9,
>                     "value": -5,
>                     "delta": -5
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 }
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 }
>               }
>             }
>           }
>         }
>       ],
>       "events": [
>         "start",
>         "stop",
>         "start",
>         "stop"
>       ]
>     },
>     "assembled": {
>       "ticks": [
>         {
>           "a": {
>             "valid": true,
>             "modified": true,
>             "last": 0,
>             "value": {
>               "left": [
>                 2,
>                 null
>               ],
>               "right": null
>             },
>             "delta": {
>               "left": {
>                 "0": 2
>               }
>             },
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": true,
>                 "last": 0,
>                 "value": [
>                   2,
>                   null
>                 ],
>                 "delta": {
>                   "0": 2
>                 },
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": true,
>                     "last": 0,
>                     "value": 2,
>                     "delta": 2
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": false
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": false
>               }
>             },
>             "peer": false
>           },
>           "b": {
>             "valid": true,
>             "modified": true,
>             "last": 0,
>             "value": {
>               "left": [
>                 10,
>                 null
>               ],
>               "right": null
>             },
>             "delta": {
>               "left": {
>                 "0": 10
>               }
>             },
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": true,
>                 "last": 0,
>                 "value": [
>                   10,
>                   null
>                 ],
>                 "delta": {
>                   "0": 10
>                 },
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": true,
>                     "last": 0,
>                     "value": 10,
>                     "delta": 10
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": false
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": false
>               }
>             },
>             "peer": false
>           },
>           "keys": [
>             0
>           ],
>           "added": [
>             0
>           ],
>           "removed": [],
>           "rows": {
>             "0": {
>               "valid": true,
>               "modified": true,
>               "last": 0,
>               "value": {
>                 "left": [
>                   2,
>                   null
>                 ],
>                 "right": null
>               },
>               "delta": {
>                 "left": {
>                   "0": 2
>                 }
>               },
>               "all_valid": false,
>               "children": {
>                 "left": {
>                   "valid": true,
>                   "modified": true,
>                   "last": 0,
>                   "value": [
>                     2,
>                     null
>                   ],
>                   "delta": {
>                     "0": 2
>                   },
>                   "all_valid": false,
>                   "children": {
>                     "0": {
>                       "valid": true,
>                       "modified": true,
>                       "last": 0,
>                       "value": 2,
>                       "delta": 2
>                     },
>                     "1": {
>                       "valid": false,
>                       "modified": false,
>                       "last": "never",
>                       "value": null,
>                       "delta": null
>                     }
>                   },
>                   "peer": true
>                 },
>                 "right": {
>                   "valid": false,
>                   "modified": false,
>                   "last": "never",
>                   "value": null,
>                   "delta": null,
>                   "all_valid": false,
>                   "children": {
>                     "0": {
>                       "valid": false,
>                       "modified": false,
>                       "last": "never",
>                       "value": null,
>                       "delta": null
>                     },
>                     "1": {
>                       "valid": false,
>                       "modified": false,
>                       "last": "never",
>                       "value": null,
>                       "delta": null
>                     }
>                   },
>                   "peer": true
>                 }
>               },
>               "peer": true
>             }
>           },
>           "retired": {}
>         },
>         {
>           "a": {
>             "valid": true,
>             "modified": true,
>             "last": 1,
>             "value": {
>               "left": [
>                 3,
>                 null
>               ],
>               "right": null
>             },
>             "delta": {
>               "left": {
>                 "0": 3
>               }
>             },
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": true,
>                 "last": 1,
>                 "value": [
>                   3,
>                   null
>                 ],
>                 "delta": {
>                   "0": 3
>                 },
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": true,
>                     "last": 1,
>                     "value": 3,
>                     "delta": 3
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": false
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": false
>               }
>             },
>             "peer": false
>           },
>           "b": {
>             "valid": true,
>             "modified": false,
>             "last": 0,
>             "value": {
>               "left": [
>                 10,
>                 null
>               ],
>               "right": null
>             },
>             "delta": null,
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": false,
>                 "last": 0,
>                 "value": [
>                   10,
>                   null
>                 ],
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": false,
>                     "last": 0,
>                     "value": 10,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": false
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": false
>               }
>             },
>             "peer": false
>           },
>           "keys": [
>             0
>           ],
>           "added": [],
>           "removed": [],
>           "rows": {
>             "0": {
>               "valid": true,
>               "modified": true,
>               "last": 1,
>               "value": {
>                 "left": [
>                   5,
>                   null
>                 ],
>                 "right": null
>               },
>               "delta": {
>                 "left": {
>                   "0": 5
>                 }
>               },
>               "all_valid": false,
>               "children": {
>                 "left": {
>                   "valid": true,
>                   "modified": true,
>                   "last": 1,
>                   "value": [
>                     5,
>                     null
>                   ],
>                   "delta": {
>                     "0": 5
>                   },
>                   "all_valid": false,
>                   "children": {
>                     "0": {
>                       "valid": true,
>                       "modified": true,
>                       "last": 1,
>                       "value": 5,
>                       "delta": 5
>                     },
>                     "1": {
>                       "valid": false,
>                       "modified": false,
>                       "last": "never",
>                       "value": null,
>                       "delta": null
>                     }
>                   },
>                   "peer": true
>                 },
>                 "right": {
>                   "valid": false,
>                   "modified": false,
>                   "last": "never",
>                   "value": null,
>                   "delta": null,
>                   "all_valid": false,
>                   "children": {
>                     "0": {
>                       "valid": false,
>                       "modified": false,
>                       "last": "never",
>                       "value": null,
>                       "delta": null
>                     },
>                     "1": {
>                       "valid": false,
>                       "modified": false,
>                       "last": "never",
>                       "value": null,
>                       "delta": null
>                     }
>                   },
>                   "peer": true
>                 }
>               },
>               "peer": true
>             }
>           },
>           "retired": {}
>         },
>         {
>           "a": {
>             "valid": true,
>             "modified": false,
>             "last": 1,
>             "value": {
>               "left": [
>                 3,
>                 null
>               ],
>               "right": null
>             },
>             "delta": null,
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": false,
>                 "last": 1,
>                 "value": [
>                   3,
>                   null
>                 ],
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": false,
>                     "last": 1,
>                     "value": 3,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": false
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": false
>               }
>             },
>             "peer": false
>           },
>           "b": {
>             "valid": true,
>             "modified": false,
>             "last": 0,
>             "value": {
>               "left": [
>                 10,
>                 null
>               ],
>               "right": null
>             },
>             "delta": null,
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": false,
>                 "last": 0,
>                 "value": [
>                   10,
>                   null
>                 ],
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": false,
>                     "last": 0,
>                     "value": 10,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": false
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": false
>               }
>             },
>             "peer": false
>           },
>           "keys": [
>             0
>           ],
>           "added": [],
>           "removed": [],
>           "rows": {
>             "0": {
>               "valid": true,
>               "modified": true,
>               "last": 2,
>               "value": {
>                 "left": [
>                   15,
>                   null
>                 ],
>                 "right": null
>               },
>               "delta": {
>                 "left": {
>                   "0": 15
>                 }
>               },
>               "all_valid": false,
>               "children": {
>                 "left": {
>                   "valid": true,
>                   "modified": true,
>                   "last": 2,
>                   "value": [
>                     15,
>                     null
>                   ],
>                   "delta": {
>                     "0": 15
>                   },
>                   "all_valid": false,
>                   "children": {
>                     "0": {
>                       "valid": true,
>                       "modified": true,
>                       "last": 2,
>                       "value": 15,
>                       "delta": 15
>                     },
>                     "1": {
>                       "valid": false,
>                       "modified": false,
>                       "last": "never",
>                       "value": null,
>                       "delta": null
>                     }
>                   },
>                   "peer": true
>                 },
>                 "right": {
>                   "valid": false,
>                   "modified": false,
>                   "last": "never",
>                   "value": null,
>                   "delta": null,
>                   "all_valid": false,
>                   "children": {
>                     "0": {
>                       "valid": false,
>                       "modified": false,
>                       "last": "never",
>                       "value": null,
>                       "delta": null
>                     },
>                     "1": {
>                       "valid": false,
>                       "modified": false,
>                       "last": "never",
>                       "value": null,
>                       "delta": null
>                     }
>                   },
>                   "peer": true
>                 }
>               },
>               "peer": true
>             }
>           },
>           "retired": {}
>         },
>         {
>           "a": {
>             "valid": true,
>             "modified": true,
>             "last": 3,
>             "value": {
>               "left": [
>                 4,
>                 null
>               ],
>               "right": null
>             },
>             "delta": {
>               "left": {
>                 "0": 4
>               }
>             },
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": true,
>                 "last": 3,
>                 "value": [
>                   4,
>                   null
>                 ],
>                 "delta": {
>                   "0": 4
>                 },
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": true,
>                     "last": 3,
>                     "value": 4,
>                     "delta": 4
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": false
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": false
>               }
>             },
>             "peer": false
>           },
>           "b": {
>             "valid": true,
>             "modified": false,
>             "last": 0,
>             "value": {
>               "left": [
>                 10,
>                 null
>               ],
>               "right": null
>             },
>             "delta": null,
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": false,
>                 "last": 0,
>                 "value": [
>                   10,
>                   null
>                 ],
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": false,
>                     "last": 0,
>                     "value": 10,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": false
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": false
>               }
>             },
>             "peer": false
>           },
>           "keys": [
>             0
>           ],
>           "added": [],
>           "removed": [],
>           "rows": {
>             "0": {
>               "valid": true,
>               "modified": false,
>               "last": 2,
>               "value": {
>                 "left": [
>                   15,
>                   null
>                 ],
>                 "right": null
>               },
>               "delta": null,
>               "all_valid": false,
>               "children": {
>                 "left": {
>                   "valid": true,
>                   "modified": false,
>                   "last": 2,
>                   "value": [
>                     15,
>                     null
>                   ],
>                   "delta": null,
>                   "all_valid": false,
>                   "children": {
>                     "0": {
>                       "valid": true,
>                       "modified": false,
>                       "last": 2,
>                       "value": 15,
>                       "delta": null
>                     },
>                     "1": {
>                       "valid": false,
>                       "modified": false,
>                       "last": "never",
>                       "value": null,
>                       "delta": null
>                     }
>                   },
>                   "peer": true
>                 },
>                 "right": {
>                   "valid": false,
>                   "modified": false,
>                   "last": "never",
>                   "value": null,
>                   "delta": null,
>                   "all_valid": false,
>                   "children": {
>                     "0": {
>                       "valid": false,
>                       "modified": false,
>                       "last": "never",
>                       "value": null,
>                       "delta": null
>                     },
>                     "1": {
>                       "valid": false,
>                       "modified": false,
>                       "last": "never",
>                       "value": null,
>                       "delta": null
>                     }
>                   },
>                   "peer": true
>                 }
>               },
>               "peer": true
>             }
>           },
>           "retired": {}
>         },
>         {
>           "a": {
>             "valid": true,
>             "modified": false,
>             "last": 3,
>             "value": {
>               "left": [
>                 4,
>                 null
>               ],
>               "right": null
>             },
>             "delta": null,
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": false,
>                 "last": 3,
>                 "value": [
>                   4,
>                   null
>                 ],
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": false,
>                     "last": 3,
>                     "value": 4,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": false
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": false
>               }
>             },
>             "peer": false
>           },
>           "b": {
>             "valid": true,
>             "modified": false,
>             "last": 0,
>             "value": {
>               "left": [
>                 10,
>                 null
>               ],
>               "right": null
>             },
>             "delta": null,
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": false,
>                 "last": 0,
>                 "value": [
>                   10,
>                   null
>                 ],
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": false,
>                     "last": 0,
>                     "value": 10,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": false
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": false
>               }
>             },
>             "peer": false
>           },
>           "keys": [
>             0
>           ],
>           "added": [],
>           "removed": [],
>           "rows": {
>             "0": {
>               "valid": true,
>               "modified": true,
>               "last": 4,
>               "value": {
>                 "left": [
>                   -15,
>                   null
>                 ],
>                 "right": null
>               },
>               "delta": {
>                 "left": {
>                   "0": -15
>                 }
>               },
>               "all_valid": false,
>               "children": {
>                 "left": {
>                   "valid": true,
>                   "modified": true,
>                   "last": 4,
>                   "value": [
>                     -15,
>                     null
>                   ],
>                   "delta": {
>                     "0": -15
>                   },
>                   "all_valid": false,
>                   "children": {
>                     "0": {
>                       "valid": true,
>                       "modified": true,
>                       "last": 4,
>                       "value": -15,
>                       "delta": -15
>                     },
>                     "1": {
>                       "valid": false,
>                       "modified": false,
>                       "last": "never",
>                       "value": null,
>                       "delta": null
>                     }
>                   },
>                   "peer": true
>                 },
>                 "right": {
>                   "valid": false,
>                   "modified": false,
>                   "last": "never",
>                   "value": null,
>                   "delta": null,
>                   "all_valid": false,
>                   "children": {
>                     "0": {
>                       "valid": false,
>                       "modified": false,
>                       "last": "never",
>                       "value": null,
>                       "delta": null
>                     },
>                     "1": {
>                       "valid": false,
>                       "modified": false,
>                       "last": "never",
>                       "value": null,
>                       "delta": null
>                     }
>                   },
>                   "peer": true
>                 }
>               },
>               "peer": true
>             }
>           },
>           "retired": {}
>         },
>         {
>           "a": {
>             "valid": true,
>             "modified": false,
>             "last": 3,
>             "value": {
>               "left": [
>                 4,
>                 null
>               ],
>               "right": null
>             },
>             "delta": null,
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": false,
>                 "last": 3,
>                 "value": [
>                   4,
>                   null
>                 ],
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": false,
>                     "last": 3,
>                     "value": 4,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": false
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": false
>               }
>             },
>             "peer": false
>           },
>           "b": {
>             "valid": true,
>             "modified": false,
>             "last": 0,
>             "value": {
>               "left": [
>                 10,
>                 null
>               ],
>               "right": null
>             },
>             "delta": null,
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": false,
>                 "last": 0,
>                 "value": [
>                   10,
>                   null
>                 ],
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": false,
>                     "last": 0,
>                     "value": 10,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": false
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": false
>               }
>             },
>             "peer": false
>           },
>           "keys": [],
>           "added": [],
>           "removed": [
>             0
>           ],
>           "rows": {},
>           "retired": {
>             "0": {
>               "valid": true,
>               "modified": false,
>               "last": 4,
>               "value": {
>                 "left": [
>                   -15,
>                   null
>                 ],
>                 "right": null
>               },
>               "delta": null,
>               "all_valid": false,
>               "children": {
>                 "left": {
>                   "valid": true,
>                   "modified": false,
>                   "last": 4,
>                   "value": [
>                     -15,
>                     null
>                   ],
>                   "delta": null,
>                   "all_valid": false,
>                   "children": {
>                     "0": {
>                       "valid": true,
>                       "modified": false,
>                       "last": 4,
>                       "value": -15,
>                       "delta": null
>                     },
>                     "1": {
>                       "valid": false,
>                       "modified": false,
>                       "last": "never",
>                       "value": null,
>                       "delta": null
>                     }
>                   },
>                   "peer": true
>                 },
>                 "right": {
>                   "valid": false,
>                   "modified": false,
>                   "last": "never",
>                   "value": null,
>                   "delta": null,
>                   "all_valid": false,
>                   "children": {
>                     "0": {
>                       "valid": false,
>                       "modified": false,
>                       "last": "never",
>                       "value": null,
>                       "delta": null
>                     },
>                     "1": {
>                       "valid": false,
>                       "modified": false,
>                       "last": "never",
>                       "value": null,
>                       "delta": null
>                     }
>                   },
>                   "peer": true
>                 }
>               },
>               "peer": true
>             }
>           }
>         },
>         {
>           "a": {
>             "valid": true,
>             "modified": true,
>             "last": 6,
>             "value": {
>               "left": [
>                 5,
>                 null
>               ],
>               "right": null
>             },
>             "delta": {
>               "left": {
>                 "0": 5
>               }
>             },
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": true,
>                 "last": 6,
>                 "value": [
>                   5,
>                   null
>                 ],
>                 "delta": {
>                   "0": 5
>                 },
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": true,
>                     "last": 6,
>                     "value": 5,
>                     "delta": 5
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": false
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": false
>               }
>             },
>             "peer": false
>           },
>           "b": {
>             "valid": true,
>             "modified": false,
>             "last": 0,
>             "value": {
>               "left": [
>                 10,
>                 null
>               ],
>               "right": null
>             },
>             "delta": null,
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": false,
>                 "last": 0,
>                 "value": [
>                   10,
>                   null
>                 ],
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": false,
>                     "last": 0,
>                     "value": 10,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": false
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": false
>               }
>             },
>             "peer": false
>           },
>           "keys": [],
>           "added": [],
>           "removed": [],
>           "rows": {},
>           "retired": {}
>         },
>         {
>           "a": {
>             "valid": true,
>             "modified": false,
>             "last": 6,
>             "value": {
>               "left": [
>                 5,
>                 null
>               ],
>               "right": null
>             },
>             "delta": null,
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": false,
>                 "last": 6,
>                 "value": [
>                   5,
>                   null
>                 ],
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": false,
>                     "last": 6,
>                     "value": 5,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": false
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": false
>               }
>             },
>             "peer": false
>           },
>           "b": {
>             "valid": true,
>             "modified": false,
>             "last": 0,
>             "value": {
>               "left": [
>                 10,
>                 null
>               ],
>               "right": null
>             },
>             "delta": null,
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": false,
>                 "last": 0,
>                 "value": [
>                   10,
>                   null
>                 ],
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": false,
>                     "last": 0,
>                     "value": 10,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": false
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": false
>               }
>             },
>             "peer": false
>           },
>           "keys": [
>             0
>           ],
>           "added": [
>             0
>           ],
>           "removed": [],
>           "rows": {
>             "0": {
>               "valid": true,
>               "modified": true,
>               "last": 7,
>               "value": {
>                 "left": [
>                   5,
>                   null
>                 ],
>                 "right": null
>               },
>               "delta": {
>                 "left": {
>                   "0": 5
>                 }
>               },
>               "all_valid": false,
>               "children": {
>                 "left": {
>                   "valid": true,
>                   "modified": true,
>                   "last": 7,
>                   "value": [
>                     5,
>                     null
>                   ],
>                   "delta": {
>                     "0": 5
>                   },
>                   "all_valid": false,
>                   "children": {
>                     "0": {
>                       "valid": true,
>                       "modified": true,
>                       "last": 7,
>                       "value": 5,
>                       "delta": 5
>                     },
>                     "1": {
>                       "valid": false,
>                       "modified": false,
>                       "last": "never",
>                       "value": null,
>                       "delta": null
>                     }
>                   },
>                   "peer": true
>                 },
>                 "right": {
>                   "valid": false,
>                   "modified": false,
>                   "last": "never",
>                   "value": null,
>                   "delta": null,
>                   "all_valid": false,
>                   "children": {
>                     "0": {
>                       "valid": false,
>                       "modified": false,
>                       "last": "never",
>                       "value": null,
>                       "delta": null
>                     },
>                     "1": {
>                       "valid": false,
>                       "modified": false,
>                       "last": "never",
>                       "value": null,
>                       "delta": null
>                     }
>                   },
>                   "peer": true
>                 }
>               },
>               "peer": true
>             }
>           },
>           "retired": {}
>         },
>         {
>           "a": {
>             "valid": true,
>             "modified": false,
>             "last": 6,
>             "value": {
>               "left": [
>                 5,
>                 null
>               ],
>               "right": null
>             },
>             "delta": null,
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": false,
>                 "last": 6,
>                 "value": [
>                   5,
>                   null
>                 ],
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": false,
>                     "last": 6,
>                     "value": 5,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": false
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": false
>               }
>             },
>             "peer": false
>           },
>           "b": {
>             "valid": true,
>             "modified": false,
>             "last": 0,
>             "value": {
>               "left": [
>                 10,
>                 null
>               ],
>               "right": null
>             },
>             "delta": null,
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": false,
>                 "last": 0,
>                 "value": [
>                   10,
>                   null
>                 ],
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": false,
>                     "last": 0,
>                     "value": 10,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": false
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": false
>               }
>             },
>             "peer": false
>           },
>           "keys": [
>             0
>           ],
>           "added": [],
>           "removed": [],
>           "rows": {
>             "0": {
>               "valid": true,
>               "modified": false,
>               "last": 7,
>               "value": {
>                 "left": [
>                   5,
>                   null
>                 ],
>                 "right": null
>               },
>               "delta": null,
>               "all_valid": false,
>               "children": {
>                 "left": {
>                   "valid": true,
>                   "modified": false,
>                   "last": 7,
>                   "value": [
>                     5,
>                     null
>                   ],
>                   "delta": null,
>                   "all_valid": false,
>                   "children": {
>                     "0": {
>                       "valid": true,
>                       "modified": false,
>                       "last": 7,
>                       "value": 5,
>                       "delta": null
>                     },
>                     "1": {
>                       "valid": false,
>                       "modified": false,
>                       "last": "never",
>                       "value": null,
>                       "delta": null
>                     }
>                   },
>                   "peer": true
>                 },
>                 "right": {
>                   "valid": false,
>                   "modified": false,
>                   "last": "never",
>                   "value": null,
>                   "delta": null,
>                   "all_valid": false,
>                   "children": {
>                     "0": {
>                       "valid": false,
>                       "modified": false,
>                       "last": "never",
>                       "value": null,
>                       "delta": null
>                     },
>                     "1": {
>                       "valid": false,
>                       "modified": false,
>                       "last": "never",
>                       "value": null,
>                       "delta": null
>                     }
>                   },
>                   "peer": true
>                 }
>               },
>               "peer": true
>             }
>           },
>           "retired": {}
>         },
>         {
>           "a": {
>             "valid": true,
>             "modified": false,
>             "last": 6,
>             "value": {
>               "left": [
>                 5,
>                 null
>               ],
>               "right": null
>             },
>             "delta": null,
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": false,
>                 "last": 6,
>                 "value": [
>                   5,
>                   null
>                 ],
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": false,
>                     "last": 6,
>                     "value": 5,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": false
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": false
>               }
>             },
>             "peer": false
>           },
>           "b": {
>             "valid": true,
>             "modified": false,
>             "last": 0,
>             "value": {
>               "left": [
>                 10,
>                 null
>               ],
>               "right": null
>             },
>             "delta": null,
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": false,
>                 "last": 0,
>                 "value": [
>                   10,
>                   null
>                 ],
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": false,
>                     "last": 0,
>                     "value": 10,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": false
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": false
>               }
>             },
>             "peer": false
>           },
>           "keys": [
>             0
>           ],
>           "added": [],
>           "removed": [],
>           "rows": {
>             "0": {
>               "valid": true,
>               "modified": true,
>               "last": 9,
>               "value": {
>                 "left": [
>                   -5,
>                   null
>                 ],
>                 "right": null
>               },
>               "delta": {
>                 "left": {
>                   "0": -5
>                 }
>               },
>               "all_valid": false,
>               "children": {
>                 "left": {
>                   "valid": true,
>                   "modified": true,
>                   "last": 9,
>                   "value": [
>                     -5,
>                     null
>                   ],
>                   "delta": {
>                     "0": -5
>                   },
>                   "all_valid": false,
>                   "children": {
>                     "0": {
>                       "valid": true,
>                       "modified": true,
>                       "last": 9,
>                       "value": -5,
>                       "delta": -5
>                     },
>                     "1": {
>                       "valid": false,
>                       "modified": false,
>                       "last": "never",
>                       "value": null,
>                       "delta": null
>                     }
>                   },
>                   "peer": true
>                 },
>                 "right": {
>                   "valid": false,
>                   "modified": false,
>                   "last": "never",
>                   "value": null,
>                   "delta": null,
>                   "all_valid": false,
>                   "children": {
>                     "0": {
>                       "valid": false,
>                       "modified": false,
>                       "last": "never",
>                       "value": null,
>                       "delta": null
>                     },
>                     "1": {
>                       "valid": false,
>                       "modified": false,
>                       "last": "never",
>                       "value": null,
>                       "delta": null
>                     }
>                   },
>                   "peer": true
>                 }
>               },
>               "peer": true
>             }
>           },
>           "retired": {}
>         },
>         {
>           "a": {
>             "valid": true,
>             "modified": false,
>             "last": 6,
>             "value": {
>               "left": [
>                 5,
>                 null
>               ],
>               "right": null
>             },
>             "delta": null,
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": false,
>                 "last": 6,
>                 "value": [
>                   5,
>                   null
>                 ],
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": false,
>                     "last": 6,
>                     "value": 5,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": false
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": false
>               }
>             },
>             "peer": false
>           },
>           "b": {
>             "valid": true,
>             "modified": false,
>             "last": 0,
>             "value": {
>               "left": [
>                 10,
>                 null
>               ],
>               "right": null
>             },
>             "delta": null,
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": false,
>                 "last": 0,
>                 "value": [
>                   10,
>                   null
>                 ],
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": false,
>                     "last": 0,
>                     "value": 10,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": false
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": false
>               }
>             },
>             "peer": false
>           },
>           "keys": [
>             0
>           ],
>           "added": [],
>           "removed": [],
>           "rows": {
>             "0": {
>               "valid": true,
>               "modified": false,
>               "last": 9,
>               "value": {
>                 "left": [
>                   -5,
>                   null
>                 ],
>                 "right": null
>               },
>               "delta": null,
>               "all_valid": false,
>               "children": {
>                 "left": {
>                   "valid": true,
>                   "modified": false,
>                   "last": 9,
>                   "value": [
>                     -5,
>                     null
>                   ],
>                   "delta": null,
>                   "all_valid": false,
>                   "children": {
>                     "0": {
>                       "valid": true,
>                       "modified": false,
>                       "last": 9,
>                       "value": -5,
>                       "delta": null
>                     },
>                     "1": {
>                       "valid": false,
>                       "modified": false,
>                       "last": "never",
>                       "value": null,
>                       "delta": null
>                     }
>                   },
>                   "peer": true
>                 },
>                 "right": {
>                   "valid": false,
>                   "modified": false,
>                   "last": "never",
>                   "value": null,
>                   "delta": null,
>                   "all_valid": false,
>                   "children": {
>                     "0": {
>                       "valid": false,
>                       "modified": false,
>                       "last": "never",
>                       "value": null,
>                       "delta": null
>                     },
>                     "1": {
>                       "valid": false,
>                       "modified": false,
>                       "last": "never",
>                       "value": null,
>                       "delta": null
>                     }
>                   },
>                   "peer": true
>                 }
>               },
>               "peer": true
>             }
>           },
>           "retired": {}
>         }
>       ],
>       "child_ticks": [
>         {
>           "time": 0,
>           "input": {
>             "valid": true,
>             "modified": true,
>             "last": 0,
>             "value": {
>               "left": [
>                 2,
>                 null
>               ],
>               "right": null
>             },
>             "delta": {
>               "left": {
>                 "0": 2
>               }
>             },
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": true,
>                 "last": 0,
>                 "value": [
>                   2,
>                   null
>                 ],
>                 "delta": {
>                   "0": 2
>                 },
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": true,
>                     "last": 0,
>                     "value": 2,
>                     "delta": 2
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": false
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": false
>               }
>             },
>             "peer": false
>           },
>           "output": {
>             "valid": true,
>             "modified": true,
>             "last": 0,
>             "value": {
>               "left": [
>                 2,
>                 null
>               ],
>               "right": null
>             },
>             "delta": {
>               "left": {
>                 "0": 2
>               }
>             },
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": true,
>                 "last": 0,
>                 "value": [
>                   2,
>                   null
>                 ],
>                 "delta": {
>                   "0": 2
>                 },
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": true,
>                     "last": 0,
>                     "value": 2,
>                     "delta": 2
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 }
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 }
>               }
>             }
>           }
>         },
>         {
>           "time": 1,
>           "input": {
>             "valid": true,
>             "modified": true,
>             "last": 1,
>             "value": {
>               "left": [
>                 3,
>                 null
>               ],
>               "right": null
>             },
>             "delta": {
>               "left": {
>                 "0": 3
>               }
>             },
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": true,
>                 "last": 1,
>                 "value": [
>                   3,
>                   null
>                 ],
>                 "delta": {
>                   "0": 3
>                 },
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": true,
>                     "last": 1,
>                     "value": 3,
>                     "delta": 3
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": false
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": false
>               }
>             },
>             "peer": false
>           },
>           "output": {
>             "valid": true,
>             "modified": true,
>             "last": 1,
>             "value": {
>               "left": [
>                 5,
>                 null
>               ],
>               "right": null
>             },
>             "delta": {
>               "left": {
>                 "0": 5
>               }
>             },
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": true,
>                 "last": 1,
>                 "value": [
>                   5,
>                   null
>                 ],
>                 "delta": {
>                   "0": 5
>                 },
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": true,
>                     "last": 1,
>                     "value": 5,
>                     "delta": 5
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 }
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 }
>               }
>             }
>           }
>         },
>         {
>           "time": 2,
>           "input": {
>             "valid": true,
>             "modified": true,
>             "last": 2,
>             "value": {
>               "left": [
>                 10,
>                 null
>               ],
>               "right": null
>             },
>             "delta": {
>               "left": {
>                 "0": 10
>               }
>             },
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": true,
>                 "last": 2,
>                 "value": [
>                   10,
>                   null
>                 ],
>                 "delta": {
>                   "0": 10
>                 },
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": true,
>                     "last": 2,
>                     "value": 10,
>                     "delta": 10
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": false
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": false
>               }
>             },
>             "peer": false
>           },
>           "output": {
>             "valid": true,
>             "modified": true,
>             "last": 2,
>             "value": {
>               "left": [
>                 15,
>                 null
>               ],
>               "right": null
>             },
>             "delta": {
>               "left": {
>                 "0": 15
>               }
>             },
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": true,
>                 "last": 2,
>                 "value": [
>                   15,
>                   null
>                 ],
>                 "delta": {
>                   "0": 15
>                 },
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": true,
>                     "last": 2,
>                     "value": 15,
>                     "delta": 15
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 }
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 }
>               }
>             }
>           }
>         },
>         {
>           "time": 4,
>           "input": {
>             "valid": true,
>             "modified": false,
>             "last": 2,
>             "value": {
>               "left": [
>                 10,
>                 null
>               ],
>               "right": null
>             },
>             "delta": null,
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": false,
>                 "last": 2,
>                 "value": [
>                   10,
>                   null
>                 ],
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": false,
>                     "last": 2,
>                     "value": 10,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": false
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": false
>               }
>             },
>             "peer": false
>           },
>           "output": {
>             "valid": true,
>             "modified": true,
>             "last": 4,
>             "value": {
>               "left": [
>                 -15,
>                 null
>               ],
>               "right": null
>             },
>             "delta": {
>               "left": {
>                 "0": -15
>               }
>             },
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": true,
>                 "last": 4,
>                 "value": [
>                   -15,
>                   null
>                 ],
>                 "delta": {
>                   "0": -15
>                 },
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": true,
>                     "last": 4,
>                     "value": -15,
>                     "delta": -15
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 }
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 }
>               }
>             }
>           }
>         },
>         {
>           "time": 7,
>           "input": {
>             "valid": true,
>             "modified": true,
>             "last": 7,
>             "value": {
>               "left": [
>                 5,
>                 null
>               ],
>               "right": null
>             },
>             "delta": {
>               "left": {
>                 "0": 5
>               }
>             },
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": true,
>                 "last": 7,
>                 "value": [
>                   5,
>                   null
>                 ],
>                 "delta": {
>                   "0": 5
>                 },
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": true,
>                     "last": 7,
>                     "value": 5,
>                     "delta": 5
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": false
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": false
>               }
>             },
>             "peer": false
>           },
>           "output": {
>             "valid": true,
>             "modified": true,
>             "last": 7,
>             "value": {
>               "left": [
>                 5,
>                 null
>               ],
>               "right": null
>             },
>             "delta": {
>               "left": {
>                 "0": 5
>               }
>             },
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": true,
>                 "last": 7,
>                 "value": [
>                   5,
>                   null
>                 ],
>                 "delta": {
>                   "0": 5
>                 },
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": true,
>                     "last": 7,
>                     "value": 5,
>                     "delta": 5
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 }
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 }
>               }
>             }
>           }
>         },
>         {
>           "time": 9,
>           "input": {
>             "valid": true,
>             "modified": false,
>             "last": 7,
>             "value": {
>               "left": [
>                 5,
>                 null
>               ],
>               "right": null
>             },
>             "delta": null,
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": false,
>                 "last": 7,
>                 "value": [
>                   5,
>                   null
>                 ],
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": false,
>                     "last": 7,
>                     "value": 5,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": false
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": false
>               }
>             },
>             "peer": false
>           },
>           "output": {
>             "valid": true,
>             "modified": true,
>             "last": 9,
>             "value": {
>               "left": [
>                 -5,
>                 null
>               ],
>               "right": null
>             },
>             "delta": {
>               "left": {
>                 "0": -5
>               }
>             },
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": true,
>                 "last": 9,
>                 "value": [
>                   -5,
>                   null
>                 ],
>                 "delta": {
>                   "0": -5
>                 },
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": true,
>                     "last": 9,
>                     "value": -5,
>                     "delta": -5
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 }
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 }
>               }
>             }
>           }
>         }
>       ],
>       "events": [
>         "start",
>         "stop",
>         "start",
>         "stop"
>       ]
>     },
>     "mixed": {
>       "ticks": [
>         {
>           "a": {
>             "valid": true,
>             "modified": true,
>             "last": 0,
>             "value": {
>               "left": [
>                 2,
>                 null
>               ],
>               "right": null
>             },
>             "delta": {
>               "left": {
>                 "0": 2
>               }
>             },
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": true,
>                 "last": 0,
>                 "value": [
>                   2,
>                   null
>                 ],
>                 "delta": {
>                   "0": 2
>                 },
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": true,
>                     "last": 0,
>                     "value": 2,
>                     "delta": 2
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": true
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": false
>               }
>             },
>             "peer": false
>           },
>           "b": {
>             "valid": true,
>             "modified": true,
>             "last": 0,
>             "value": {
>               "left": [
>                 10,
>                 null
>               ],
>               "right": null
>             },
>             "delta": {
>               "left": {
>                 "0": 10
>               }
>             },
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": true,
>                 "last": 0,
>                 "value": [
>                   10,
>                   null
>                 ],
>                 "delta": {
>                   "0": 10
>                 },
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": true,
>                     "last": 0,
>                     "value": 10,
>                     "delta": 10
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": true
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": false
>               }
>             },
>             "peer": false
>           },
>           "keys": [
>             0
>           ],
>           "added": [
>             0
>           ],
>           "removed": [],
>           "rows": {
>             "0": {
>               "valid": true,
>               "modified": true,
>               "last": 0,
>               "value": {
>                 "left": [
>                   2,
>                   null
>                 ],
>                 "right": null
>               },
>               "delta": {
>                 "left": {
>                   "0": 2
>                 }
>               },
>               "all_valid": false,
>               "children": {
>                 "left": {
>                   "valid": true,
>                   "modified": true,
>                   "last": 0,
>                   "value": [
>                     2,
>                     null
>                   ],
>                   "delta": {
>                     "0": 2
>                   },
>                   "all_valid": false,
>                   "children": {
>                     "0": {
>                       "valid": true,
>                       "modified": true,
>                       "last": 0,
>                       "value": 2,
>                       "delta": 2
>                     },
>                     "1": {
>                       "valid": false,
>                       "modified": false,
>                       "last": "never",
>                       "value": null,
>                       "delta": null
>                     }
>                   },
>                   "peer": true
>                 },
>                 "right": {
>                   "valid": false,
>                   "modified": false,
>                   "last": "never",
>                   "value": null,
>                   "delta": null,
>                   "all_valid": false,
>                   "children": {
>                     "0": {
>                       "valid": false,
>                       "modified": false,
>                       "last": "never",
>                       "value": null,
>                       "delta": null
>                     },
>                     "1": {
>                       "valid": false,
>                       "modified": false,
>                       "last": "never",
>                       "value": null,
>                       "delta": null
>                     }
>                   },
>                   "peer": true
>                 }
>               },
>               "peer": true
>             }
>           },
>           "retired": {}
>         },
>         {
>           "a": {
>             "valid": true,
>             "modified": true,
>             "last": 1,
>             "value": {
>               "left": [
>                 3,
>                 null
>               ],
>               "right": null
>             },
>             "delta": {
>               "left": {
>                 "0": 3
>               }
>             },
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": true,
>                 "last": 1,
>                 "value": [
>                   3,
>                   null
>                 ],
>                 "delta": {
>                   "0": 3
>                 },
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": true,
>                     "last": 1,
>                     "value": 3,
>                     "delta": 3
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": true
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": false
>               }
>             },
>             "peer": false
>           },
>           "b": {
>             "valid": true,
>             "modified": false,
>             "last": 0,
>             "value": {
>               "left": [
>                 10,
>                 null
>               ],
>               "right": null
>             },
>             "delta": null,
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": false,
>                 "last": 0,
>                 "value": [
>                   10,
>                   null
>                 ],
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": false,
>                     "last": 0,
>                     "value": 10,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": true
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": false
>               }
>             },
>             "peer": false
>           },
>           "keys": [
>             0
>           ],
>           "added": [],
>           "removed": [],
>           "rows": {
>             "0": {
>               "valid": true,
>               "modified": true,
>               "last": 1,
>               "value": {
>                 "left": [
>                   5,
>                   null
>                 ],
>                 "right": null
>               },
>               "delta": {
>                 "left": {
>                   "0": 5
>                 }
>               },
>               "all_valid": false,
>               "children": {
>                 "left": {
>                   "valid": true,
>                   "modified": true,
>                   "last": 1,
>                   "value": [
>                     5,
>                     null
>                   ],
>                   "delta": {
>                     "0": 5
>                   },
>                   "all_valid": false,
>                   "children": {
>                     "0": {
>                       "valid": true,
>                       "modified": true,
>                       "last": 1,
>                       "value": 5,
>                       "delta": 5
>                     },
>                     "1": {
>                       "valid": false,
>                       "modified": false,
>                       "last": "never",
>                       "value": null,
>                       "delta": null
>                     }
>                   },
>                   "peer": true
>                 },
>                 "right": {
>                   "valid": false,
>                   "modified": false,
>                   "last": "never",
>                   "value": null,
>                   "delta": null,
>                   "all_valid": false,
>                   "children": {
>                     "0": {
>                       "valid": false,
>                       "modified": false,
>                       "last": "never",
>                       "value": null,
>                       "delta": null
>                     },
>                     "1": {
>                       "valid": false,
>                       "modified": false,
>                       "last": "never",
>                       "value": null,
>                       "delta": null
>                     }
>                   },
>                   "peer": true
>                 }
>               },
>               "peer": true
>             }
>           },
>           "retired": {}
>         },
>         {
>           "a": {
>             "valid": true,
>             "modified": false,
>             "last": 1,
>             "value": {
>               "left": [
>                 3,
>                 null
>               ],
>               "right": null
>             },
>             "delta": null,
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": false,
>                 "last": 1,
>                 "value": [
>                   3,
>                   null
>                 ],
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": false,
>                     "last": 1,
>                     "value": 3,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": true
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": false
>               }
>             },
>             "peer": false
>           },
>           "b": {
>             "valid": true,
>             "modified": false,
>             "last": 0,
>             "value": {
>               "left": [
>                 10,
>                 null
>               ],
>               "right": null
>             },
>             "delta": null,
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": false,
>                 "last": 0,
>                 "value": [
>                   10,
>                   null
>                 ],
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": false,
>                     "last": 0,
>                     "value": 10,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": true
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": false
>               }
>             },
>             "peer": false
>           },
>           "keys": [
>             0
>           ],
>           "added": [],
>           "removed": [],
>           "rows": {
>             "0": {
>               "valid": true,
>               "modified": true,
>               "last": 2,
>               "value": {
>                 "left": [
>                   15,
>                   null
>                 ],
>                 "right": null
>               },
>               "delta": {
>                 "left": {
>                   "0": 15
>                 }
>               },
>               "all_valid": false,
>               "children": {
>                 "left": {
>                   "valid": true,
>                   "modified": true,
>                   "last": 2,
>                   "value": [
>                     15,
>                     null
>                   ],
>                   "delta": {
>                     "0": 15
>                   },
>                   "all_valid": false,
>                   "children": {
>                     "0": {
>                       "valid": true,
>                       "modified": true,
>                       "last": 2,
>                       "value": 15,
>                       "delta": 15
>                     },
>                     "1": {
>                       "valid": false,
>                       "modified": false,
>                       "last": "never",
>                       "value": null,
>                       "delta": null
>                     }
>                   },
>                   "peer": true
>                 },
>                 "right": {
>                   "valid": false,
>                   "modified": false,
>                   "last": "never",
>                   "value": null,
>                   "delta": null,
>                   "all_valid": false,
>                   "children": {
>                     "0": {
>                       "valid": false,
>                       "modified": false,
>                       "last": "never",
>                       "value": null,
>                       "delta": null
>                     },
>                     "1": {
>                       "valid": false,
>                       "modified": false,
>                       "last": "never",
>                       "value": null,
>                       "delta": null
>                     }
>                   },
>                   "peer": true
>                 }
>               },
>               "peer": true
>             }
>           },
>           "retired": {}
>         },
>         {
>           "a": {
>             "valid": true,
>             "modified": true,
>             "last": 3,
>             "value": {
>               "left": [
>                 4,
>                 null
>               ],
>               "right": null
>             },
>             "delta": {
>               "left": {
>                 "0": 4
>               }
>             },
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": true,
>                 "last": 3,
>                 "value": [
>                   4,
>                   null
>                 ],
>                 "delta": {
>                   "0": 4
>                 },
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": true,
>                     "last": 3,
>                     "value": 4,
>                     "delta": 4
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": true
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": false
>               }
>             },
>             "peer": false
>           },
>           "b": {
>             "valid": true,
>             "modified": false,
>             "last": 0,
>             "value": {
>               "left": [
>                 10,
>                 null
>               ],
>               "right": null
>             },
>             "delta": null,
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": false,
>                 "last": 0,
>                 "value": [
>                   10,
>                   null
>                 ],
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": false,
>                     "last": 0,
>                     "value": 10,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": true
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": false
>               }
>             },
>             "peer": false
>           },
>           "keys": [
>             0
>           ],
>           "added": [],
>           "removed": [],
>           "rows": {
>             "0": {
>               "valid": true,
>               "modified": false,
>               "last": 2,
>               "value": {
>                 "left": [
>                   15,
>                   null
>                 ],
>                 "right": null
>               },
>               "delta": null,
>               "all_valid": false,
>               "children": {
>                 "left": {
>                   "valid": true,
>                   "modified": false,
>                   "last": 2,
>                   "value": [
>                     15,
>                     null
>                   ],
>                   "delta": null,
>                   "all_valid": false,
>                   "children": {
>                     "0": {
>                       "valid": true,
>                       "modified": false,
>                       "last": 2,
>                       "value": 15,
>                       "delta": null
>                     },
>                     "1": {
>                       "valid": false,
>                       "modified": false,
>                       "last": "never",
>                       "value": null,
>                       "delta": null
>                     }
>                   },
>                   "peer": true
>                 },
>                 "right": {
>                   "valid": false,
>                   "modified": false,
>                   "last": "never",
>                   "value": null,
>                   "delta": null,
>                   "all_valid": false,
>                   "children": {
>                     "0": {
>                       "valid": false,
>                       "modified": false,
>                       "last": "never",
>                       "value": null,
>                       "delta": null
>                     },
>                     "1": {
>                       "valid": false,
>                       "modified": false,
>                       "last": "never",
>                       "value": null,
>                       "delta": null
>                     }
>                   },
>                   "peer": true
>                 }
>               },
>               "peer": true
>             }
>           },
>           "retired": {}
>         },
>         {
>           "a": {
>             "valid": true,
>             "modified": false,
>             "last": 3,
>             "value": {
>               "left": [
>                 4,
>                 null
>               ],
>               "right": null
>             },
>             "delta": null,
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": false,
>                 "last": 3,
>                 "value": [
>                   4,
>                   null
>                 ],
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": false,
>                     "last": 3,
>                     "value": 4,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": true
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": false
>               }
>             },
>             "peer": false
>           },
>           "b": {
>             "valid": true,
>             "modified": false,
>             "last": 0,
>             "value": {
>               "left": [
>                 10,
>                 null
>               ],
>               "right": null
>             },
>             "delta": null,
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": false,
>                 "last": 0,
>                 "value": [
>                   10,
>                   null
>                 ],
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": false,
>                     "last": 0,
>                     "value": 10,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": true
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": false
>               }
>             },
>             "peer": false
>           },
>           "keys": [
>             0
>           ],
>           "added": [],
>           "removed": [],
>           "rows": {
>             "0": {
>               "valid": true,
>               "modified": true,
>               "last": 4,
>               "value": {
>                 "left": [
>                   -15,
>                   null
>                 ],
>                 "right": null
>               },
>               "delta": {
>                 "left": {
>                   "0": -15
>                 }
>               },
>               "all_valid": false,
>               "children": {
>                 "left": {
>                   "valid": true,
>                   "modified": true,
>                   "last": 4,
>                   "value": [
>                     -15,
>                     null
>                   ],
>                   "delta": {
>                     "0": -15
>                   },
>                   "all_valid": false,
>                   "children": {
>                     "0": {
>                       "valid": true,
>                       "modified": true,
>                       "last": 4,
>                       "value": -15,
>                       "delta": -15
>                     },
>                     "1": {
>                       "valid": false,
>                       "modified": false,
>                       "last": "never",
>                       "value": null,
>                       "delta": null
>                     }
>                   },
>                   "peer": true
>                 },
>                 "right": {
>                   "valid": false,
>                   "modified": false,
>                   "last": "never",
>                   "value": null,
>                   "delta": null,
>                   "all_valid": false,
>                   "children": {
>                     "0": {
>                       "valid": false,
>                       "modified": false,
>                       "last": "never",
>                       "value": null,
>                       "delta": null
>                     },
>                     "1": {
>                       "valid": false,
>                       "modified": false,
>                       "last": "never",
>                       "value": null,
>                       "delta": null
>                     }
>                   },
>                   "peer": true
>                 }
>               },
>               "peer": true
>             }
>           },
>           "retired": {}
>         },
>         {
>           "a": {
>             "valid": true,
>             "modified": false,
>             "last": 3,
>             "value": {
>               "left": [
>                 4,
>                 null
>               ],
>               "right": null
>             },
>             "delta": null,
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": false,
>                 "last": 3,
>                 "value": [
>                   4,
>                   null
>                 ],
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": false,
>                     "last": 3,
>                     "value": 4,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": true
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": false
>               }
>             },
>             "peer": false
>           },
>           "b": {
>             "valid": true,
>             "modified": false,
>             "last": 0,
>             "value": {
>               "left": [
>                 10,
>                 null
>               ],
>               "right": null
>             },
>             "delta": null,
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": false,
>                 "last": 0,
>                 "value": [
>                   10,
>                   null
>                 ],
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": false,
>                     "last": 0,
>                     "value": 10,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": true
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": false
>               }
>             },
>             "peer": false
>           },
>           "keys": [],
>           "added": [],
>           "removed": [
>             0
>           ],
>           "rows": {},
>           "retired": {
>             "0": {
>               "valid": true,
>               "modified": false,
>               "last": 4,
>               "value": {
>                 "left": [
>                   -15,
>                   null
>                 ],
>                 "right": null
>               },
>               "delta": null,
>               "all_valid": false,
>               "children": {
>                 "left": {
>                   "valid": true,
>                   "modified": false,
>                   "last": 4,
>                   "value": [
>                     -15,
>                     null
>                   ],
>                   "delta": null,
>                   "all_valid": false,
>                   "children": {
>                     "0": {
>                       "valid": true,
>                       "modified": false,
>                       "last": 4,
>                       "value": -15,
>                       "delta": null
>                     },
>                     "1": {
>                       "valid": false,
>                       "modified": false,
>                       "last": "never",
>                       "value": null,
>                       "delta": null
>                     }
>                   },
>                   "peer": true
>                 },
>                 "right": {
>                   "valid": false,
>                   "modified": false,
>                   "last": "never",
>                   "value": null,
>                   "delta": null,
>                   "all_valid": false,
>                   "children": {
>                     "0": {
>                       "valid": false,
>                       "modified": false,
>                       "last": "never",
>                       "value": null,
>                       "delta": null
>                     },
>                     "1": {
>                       "valid": false,
>                       "modified": false,
>                       "last": "never",
>                       "value": null,
>                       "delta": null
>                     }
>                   },
>                   "peer": true
>                 }
>               },
>               "peer": true
>             }
>           }
>         },
>         {
>           "a": {
>             "valid": true,
>             "modified": true,
>             "last": 6,
>             "value": {
>               "left": [
>                 5,
>                 null
>               ],
>               "right": null
>             },
>             "delta": {
>               "left": {
>                 "0": 5
>               }
>             },
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": true,
>                 "last": 6,
>                 "value": [
>                   5,
>                   null
>                 ],
>                 "delta": {
>                   "0": 5
>                 },
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": true,
>                     "last": 6,
>                     "value": 5,
>                     "delta": 5
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": true
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": false
>               }
>             },
>             "peer": false
>           },
>           "b": {
>             "valid": true,
>             "modified": false,
>             "last": 0,
>             "value": {
>               "left": [
>                 10,
>                 null
>               ],
>               "right": null
>             },
>             "delta": null,
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": false,
>                 "last": 0,
>                 "value": [
>                   10,
>                   null
>                 ],
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": false,
>                     "last": 0,
>                     "value": 10,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": true
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": false
>               }
>             },
>             "peer": false
>           },
>           "keys": [],
>           "added": [],
>           "removed": [],
>           "rows": {},
>           "retired": {}
>         },
>         {
>           "a": {
>             "valid": true,
>             "modified": false,
>             "last": 6,
>             "value": {
>               "left": [
>                 5,
>                 null
>               ],
>               "right": null
>             },
>             "delta": null,
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": false,
>                 "last": 6,
>                 "value": [
>                   5,
>                   null
>                 ],
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": false,
>                     "last": 6,
>                     "value": 5,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": true
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": false
>               }
>             },
>             "peer": false
>           },
>           "b": {
>             "valid": true,
>             "modified": false,
>             "last": 0,
>             "value": {
>               "left": [
>                 10,
>                 null
>               ],
>               "right": null
>             },
>             "delta": null,
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": false,
>                 "last": 0,
>                 "value": [
>                   10,
>                   null
>                 ],
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": false,
>                     "last": 0,
>                     "value": 10,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": true
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": false
>               }
>             },
>             "peer": false
>           },
>           "keys": [
>             0
>           ],
>           "added": [
>             0
>           ],
>           "removed": [],
>           "rows": {
>             "0": {
>               "valid": true,
>               "modified": true,
>               "last": 7,
>               "value": {
>                 "left": [
>                   5,
>                   null
>                 ],
>                 "right": null
>               },
>               "delta": {
>                 "left": {
>                   "0": 5
>                 }
>               },
>               "all_valid": false,
>               "children": {
>                 "left": {
>                   "valid": true,
>                   "modified": true,
>                   "last": 7,
>                   "value": [
>                     5,
>                     null
>                   ],
>                   "delta": {
>                     "0": 5
>                   },
>                   "all_valid": false,
>                   "children": {
>                     "0": {
>                       "valid": true,
>                       "modified": true,
>                       "last": 7,
>                       "value": 5,
>                       "delta": 5
>                     },
>                     "1": {
>                       "valid": false,
>                       "modified": false,
>                       "last": "never",
>                       "value": null,
>                       "delta": null
>                     }
>                   },
>                   "peer": true
>                 },
>                 "right": {
>                   "valid": false,
>                   "modified": false,
>                   "last": "never",
>                   "value": null,
>                   "delta": null,
>                   "all_valid": false,
>                   "children": {
>                     "0": {
>                       "valid": false,
>                       "modified": false,
>                       "last": "never",
>                       "value": null,
>                       "delta": null
>                     },
>                     "1": {
>                       "valid": false,
>                       "modified": false,
>                       "last": "never",
>                       "value": null,
>                       "delta": null
>                     }
>                   },
>                   "peer": true
>                 }
>               },
>               "peer": true
>             }
>           },
>           "retired": {}
>         },
>         {
>           "a": {
>             "valid": true,
>             "modified": false,
>             "last": 6,
>             "value": {
>               "left": [
>                 5,
>                 null
>               ],
>               "right": null
>             },
>             "delta": null,
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": false,
>                 "last": 6,
>                 "value": [
>                   5,
>                   null
>                 ],
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": false,
>                     "last": 6,
>                     "value": 5,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": true
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": false
>               }
>             },
>             "peer": false
>           },
>           "b": {
>             "valid": true,
>             "modified": false,
>             "last": 0,
>             "value": {
>               "left": [
>                 10,
>                 null
>               ],
>               "right": null
>             },
>             "delta": null,
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": false,
>                 "last": 0,
>                 "value": [
>                   10,
>                   null
>                 ],
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": false,
>                     "last": 0,
>                     "value": 10,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": true
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": false
>               }
>             },
>             "peer": false
>           },
>           "keys": [
>             0
>           ],
>           "added": [],
>           "removed": [],
>           "rows": {
>             "0": {
>               "valid": true,
>               "modified": false,
>               "last": 7,
>               "value": {
>                 "left": [
>                   5,
>                   null
>                 ],
>                 "right": null
>               },
>               "delta": null,
>               "all_valid": false,
>               "children": {
>                 "left": {
>                   "valid": true,
>                   "modified": false,
>                   "last": 7,
>                   "value": [
>                     5,
>                     null
>                   ],
>                   "delta": null,
>                   "all_valid": false,
>                   "children": {
>                     "0": {
>                       "valid": true,
>                       "modified": false,
>                       "last": 7,
>                       "value": 5,
>                       "delta": null
>                     },
>                     "1": {
>                       "valid": false,
>                       "modified": false,
>                       "last": "never",
>                       "value": null,
>                       "delta": null
>                     }
>                   },
>                   "peer": true
>                 },
>                 "right": {
>                   "valid": false,
>                   "modified": false,
>                   "last": "never",
>                   "value": null,
>                   "delta": null,
>                   "all_valid": false,
>                   "children": {
>                     "0": {
>                       "valid": false,
>                       "modified": false,
>                       "last": "never",
>                       "value": null,
>                       "delta": null
>                     },
>                     "1": {
>                       "valid": false,
>                       "modified": false,
>                       "last": "never",
>                       "value": null,
>                       "delta": null
>                     }
>                   },
>                   "peer": true
>                 }
>               },
>               "peer": true
>             }
>           },
>           "retired": {}
>         },
>         {
>           "a": {
>             "valid": true,
>             "modified": false,
>             "last": 6,
>             "value": {
>               "left": [
>                 5,
>                 null
>               ],
>               "right": null
>             },
>             "delta": null,
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": false,
>                 "last": 6,
>                 "value": [
>                   5,
>                   null
>                 ],
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": false,
>                     "last": 6,
>                     "value": 5,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": true
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": false
>               }
>             },
>             "peer": false
>           },
>           "b": {
>             "valid": true,
>             "modified": false,
>             "last": 0,
>             "value": {
>               "left": [
>                 10,
>                 null
>               ],
>               "right": null
>             },
>             "delta": null,
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": false,
>                 "last": 0,
>                 "value": [
>                   10,
>                   null
>                 ],
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": false,
>                     "last": 0,
>                     "value": 10,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": true
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": false
>               }
>             },
>             "peer": false
>           },
>           "keys": [
>             0
>           ],
>           "added": [],
>           "removed": [],
>           "rows": {
>             "0": {
>               "valid": true,
>               "modified": true,
>               "last": 9,
>               "value": {
>                 "left": [
>                   -5,
>                   null
>                 ],
>                 "right": null
>               },
>               "delta": {
>                 "left": {
>                   "0": -5
>                 }
>               },
>               "all_valid": false,
>               "children": {
>                 "left": {
>                   "valid": true,
>                   "modified": true,
>                   "last": 9,
>                   "value": [
>                     -5,
>                     null
>                   ],
>                   "delta": {
>                     "0": -5
>                   },
>                   "all_valid": false,
>                   "children": {
>                     "0": {
>                       "valid": true,
>                       "modified": true,
>                       "last": 9,
>                       "value": -5,
>                       "delta": -5
>                     },
>                     "1": {
>                       "valid": false,
>                       "modified": false,
>                       "last": "never",
>                       "value": null,
>                       "delta": null
>                     }
>                   },
>                   "peer": true
>                 },
>                 "right": {
>                   "valid": false,
>                   "modified": false,
>                   "last": "never",
>                   "value": null,
>                   "delta": null,
>                   "all_valid": false,
>                   "children": {
>                     "0": {
>                       "valid": false,
>                       "modified": false,
>                       "last": "never",
>                       "value": null,
>                       "delta": null
>                     },
>                     "1": {
>                       "valid": false,
>                       "modified": false,
>                       "last": "never",
>                       "value": null,
>                       "delta": null
>                     }
>                   },
>                   "peer": true
>                 }
>               },
>               "peer": true
>             }
>           },
>           "retired": {}
>         },
>         {
>           "a": {
>             "valid": true,
>             "modified": false,
>             "last": 6,
>             "value": {
>               "left": [
>                 5,
>                 null
>               ],
>               "right": null
>             },
>             "delta": null,
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": false,
>                 "last": 6,
>                 "value": [
>                   5,
>                   null
>                 ],
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": false,
>                     "last": 6,
>                     "value": 5,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": true
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": false
>               }
>             },
>             "peer": false
>           },
>           "b": {
>             "valid": true,
>             "modified": false,
>             "last": 0,
>             "value": {
>               "left": [
>                 10,
>                 null
>               ],
>               "right": null
>             },
>             "delta": null,
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": false,
>                 "last": 0,
>                 "value": [
>                   10,
>                   null
>                 ],
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": false,
>                     "last": 0,
>                     "value": 10,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": true
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": false
>               }
>             },
>             "peer": false
>           },
>           "keys": [
>             0
>           ],
>           "added": [],
>           "removed": [],
>           "rows": {
>             "0": {
>               "valid": true,
>               "modified": false,
>               "last": 9,
>               "value": {
>                 "left": [
>                   -5,
>                   null
>                 ],
>                 "right": null
>               },
>               "delta": null,
>               "all_valid": false,
>               "children": {
>                 "left": {
>                   "valid": true,
>                   "modified": false,
>                   "last": 9,
>                   "value": [
>                     -5,
>                     null
>                   ],
>                   "delta": null,
>                   "all_valid": false,
>                   "children": {
>                     "0": {
>                       "valid": true,
>                       "modified": false,
>                       "last": 9,
>                       "value": -5,
>                       "delta": null
>                     },
>                     "1": {
>                       "valid": false,
>                       "modified": false,
>                       "last": "never",
>                       "value": null,
>                       "delta": null
>                     }
>                   },
>                   "peer": true
>                 },
>                 "right": {
>                   "valid": false,
>                   "modified": false,
>                   "last": "never",
>                   "value": null,
>                   "delta": null,
>                   "all_valid": false,
>                   "children": {
>                     "0": {
>                       "valid": false,
>                       "modified": false,
>                       "last": "never",
>                       "value": null,
>                       "delta": null
>                     },
>                     "1": {
>                       "valid": false,
>                       "modified": false,
>                       "last": "never",
>                       "value": null,
>                       "delta": null
>                     }
>                   },
>                   "peer": true
>                 }
>               },
>               "peer": true
>             }
>           },
>           "retired": {}
>         }
>       ],
>       "child_ticks": [
>         {
>           "time": 0,
>           "input": {
>             "valid": true,
>             "modified": true,
>             "last": 0,
>             "value": {
>               "left": [
>                 2,
>                 null
>               ],
>               "right": null
>             },
>             "delta": {
>               "left": {
>                 "0": 2
>               }
>             },
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": true,
>                 "last": 0,
>                 "value": [
>                   2,
>                   null
>                 ],
>                 "delta": {
>                   "0": 2
>                 },
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": true,
>                     "last": 0,
>                     "value": 2,
>                     "delta": 2
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": true
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": false
>               }
>             },
>             "peer": false
>           },
>           "output": {
>             "valid": true,
>             "modified": true,
>             "last": 0,
>             "value": {
>               "left": [
>                 2,
>                 null
>               ],
>               "right": null
>             },
>             "delta": {
>               "left": {
>                 "0": 2
>               }
>             },
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": true,
>                 "last": 0,
>                 "value": [
>                   2,
>                   null
>                 ],
>                 "delta": {
>                   "0": 2
>                 },
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": true,
>                     "last": 0,
>                     "value": 2,
>                     "delta": 2
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 }
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 }
>               }
>             }
>           }
>         },
>         {
>           "time": 1,
>           "input": {
>             "valid": true,
>             "modified": true,
>             "last": 1,
>             "value": {
>               "left": [
>                 3,
>                 null
>               ],
>               "right": null
>             },
>             "delta": {
>               "left": {
>                 "0": 3
>               }
>             },
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": true,
>                 "last": 1,
>                 "value": [
>                   3,
>                   null
>                 ],
>                 "delta": {
>                   "0": 3
>                 },
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": true,
>                     "last": 1,
>                     "value": 3,
>                     "delta": 3
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": true
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": false
>               }
>             },
>             "peer": false
>           },
>           "output": {
>             "valid": true,
>             "modified": true,
>             "last": 1,
>             "value": {
>               "left": [
>                 5,
>                 null
>               ],
>               "right": null
>             },
>             "delta": {
>               "left": {
>                 "0": 5
>               }
>             },
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": true,
>                 "last": 1,
>                 "value": [
>                   5,
>                   null
>                 ],
>                 "delta": {
>                   "0": 5
>                 },
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": true,
>                     "last": 1,
>                     "value": 5,
>                     "delta": 5
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 }
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 }
>               }
>             }
>           }
>         },
>         {
>           "time": 2,
>           "input": {
>             "valid": true,
>             "modified": true,
>             "last": 2,
>             "value": {
>               "left": [
>                 10,
>                 null
>               ],
>               "right": null
>             },
>             "delta": {
>               "left": {
>                 "0": 10
>               }
>             },
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": true,
>                 "last": 2,
>                 "value": [
>                   10,
>                   null
>                 ],
>                 "delta": {
>                   "0": 10
>                 },
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": true,
>                     "last": 2,
>                     "value": 10,
>                     "delta": 10
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": true
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": false
>               }
>             },
>             "peer": false
>           },
>           "output": {
>             "valid": true,
>             "modified": true,
>             "last": 2,
>             "value": {
>               "left": [
>                 15,
>                 null
>               ],
>               "right": null
>             },
>             "delta": {
>               "left": {
>                 "0": 15
>               }
>             },
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": true,
>                 "last": 2,
>                 "value": [
>                   15,
>                   null
>                 ],
>                 "delta": {
>                   "0": 15
>                 },
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": true,
>                     "last": 2,
>                     "value": 15,
>                     "delta": 15
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 }
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 }
>               }
>             }
>           }
>         },
>         {
>           "time": 4,
>           "input": {
>             "valid": true,
>             "modified": false,
>             "last": 2,
>             "value": {
>               "left": [
>                 10,
>                 null
>               ],
>               "right": null
>             },
>             "delta": null,
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": false,
>                 "last": 2,
>                 "value": [
>                   10,
>                   null
>                 ],
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": false,
>                     "last": 2,
>                     "value": 10,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": true
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": false
>               }
>             },
>             "peer": false
>           },
>           "output": {
>             "valid": true,
>             "modified": true,
>             "last": 4,
>             "value": {
>               "left": [
>                 -15,
>                 null
>               ],
>               "right": null
>             },
>             "delta": {
>               "left": {
>                 "0": -15
>               }
>             },
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": true,
>                 "last": 4,
>                 "value": [
>                   -15,
>                   null
>                 ],
>                 "delta": {
>                   "0": -15
>                 },
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": true,
>                     "last": 4,
>                     "value": -15,
>                     "delta": -15
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 }
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 }
>               }
>             }
>           }
>         },
>         {
>           "time": 7,
>           "input": {
>             "valid": true,
>             "modified": true,
>             "last": 7,
>             "value": {
>               "left": [
>                 5,
>                 null
>               ],
>               "right": null
>             },
>             "delta": {
>               "left": {
>                 "0": 5
>               }
>             },
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": true,
>                 "last": 7,
>                 "value": [
>                   5,
>                   null
>                 ],
>                 "delta": {
>                   "0": 5
>                 },
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": true,
>                     "last": 7,
>                     "value": 5,
>                     "delta": 5
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": true
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": false
>               }
>             },
>             "peer": false
>           },
>           "output": {
>             "valid": true,
>             "modified": true,
>             "last": 7,
>             "value": {
>               "left": [
>                 5,
>                 null
>               ],
>               "right": null
>             },
>             "delta": {
>               "left": {
>                 "0": 5
>               }
>             },
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": true,
>                 "last": 7,
>                 "value": [
>                   5,
>                   null
>                 ],
>                 "delta": {
>                   "0": 5
>                 },
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": true,
>                     "last": 7,
>                     "value": 5,
>                     "delta": 5
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 }
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 }
>               }
>             }
>           }
>         },
>         {
>           "time": 9,
>           "input": {
>             "valid": true,
>             "modified": false,
>             "last": 7,
>             "value": {
>               "left": [
>                 5,
>                 null
>               ],
>               "right": null
>             },
>             "delta": null,
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": false,
>                 "last": 7,
>                 "value": [
>                   5,
>                   null
>                 ],
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": false,
>                     "last": 7,
>                     "value": 5,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": true
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": false
>               }
>             },
>             "peer": false
>           },
>           "output": {
>             "valid": true,
>             "modified": true,
>             "last": 9,
>             "value": {
>               "left": [
>                 -5,
>                 null
>               ],
>               "right": null
>             },
>             "delta": {
>               "left": {
>                 "0": -5
>               }
>             },
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": true,
>                 "last": 9,
>                 "value": [
>                   -5,
>                   null
>                 ],
>                 "delta": {
>                   "0": -5
>                 },
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": true,
>                     "last": 9,
>                     "value": -5,
>                     "delta": -5
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 }
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 }
>               }
>             }
>           }
>         }
>       ],
>       "events": [
>         "start",
>         "stop",
>         "start",
>         "stop"
>       ]
>     },
>     "owned_capture": {
>       "ticks": [
>         {
>           "a": {
>             "valid": true,
>             "modified": true,
>             "last": 0,
>             "value": {
>               "left": [
>                 2,
>                 null
>               ],
>               "right": null
>             },
>             "delta": {
>               "left": {
>                 "0": 2
>               }
>             },
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": true,
>                 "last": 0,
>                 "value": [
>                   2,
>                   null
>                 ],
>                 "delta": {
>                   "0": 2
>                 },
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": true,
>                     "last": 0,
>                     "value": 2,
>                     "delta": 2
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": true
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": true
>               }
>             },
>             "peer": true
>           },
>           "b": {
>             "valid": true,
>             "modified": true,
>             "last": 0,
>             "value": {
>               "left": [
>                 10,
>                 null
>               ],
>               "right": null
>             },
>             "delta": {
>               "left": {
>                 "0": 10
>               }
>             },
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": true,
>                 "last": 0,
>                 "value": [
>                   10,
>                   null
>                 ],
>                 "delta": {
>                   "0": 10
>                 },
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": true,
>                     "last": 0,
>                     "value": 10,
>                     "delta": 10
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": true
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": true
>               }
>             },
>             "peer": true
>           },
>           "keys": [
>             0
>           ],
>           "added": [
>             0
>           ],
>           "removed": [],
>           "rows": {
>             "0": {
>               "valid": true,
>               "modified": true,
>               "last": 0,
>               "value": {
>                 "left": [
>                   2,
>                   null
>                 ],
>                 "right": null
>               },
>               "delta": {
>                 "left": {
>                   "0": 2
>                 }
>               },
>               "all_valid": false,
>               "children": {
>                 "left": {
>                   "valid": true,
>                   "modified": true,
>                   "last": 0,
>                   "value": [
>                     2,
>                     null
>                   ],
>                   "delta": {
>                     "0": 2
>                   },
>                   "all_valid": false,
>                   "children": {
>                     "0": {
>                       "valid": true,
>                       "modified": true,
>                       "last": 0,
>                       "value": 2,
>                       "delta": 2
>                     },
>                     "1": {
>                       "valid": false,
>                       "modified": false,
>                       "last": "never",
>                       "value": null,
>                       "delta": null
>                     }
>                   },
>                   "peer": true
>                 },
>                 "right": {
>                   "valid": false,
>                   "modified": false,
>                   "last": "never",
>                   "value": null,
>                   "delta": null,
>                   "all_valid": false,
>                   "children": {
>                     "0": {
>                       "valid": false,
>                       "modified": false,
>                       "last": "never",
>                       "value": null,
>                       "delta": null
>                     },
>                     "1": {
>                       "valid": false,
>                       "modified": false,
>                       "last": "never",
>                       "value": null,
>                       "delta": null
>                     }
>                   },
>                   "peer": true
>                 }
>               },
>               "peer": true
>             }
>           },
>           "retired": {}
>         },
>         {
>           "a": {
>             "valid": true,
>             "modified": true,
>             "last": 1,
>             "value": {
>               "left": [
>                 3,
>                 null
>               ],
>               "right": null
>             },
>             "delta": {
>               "left": {
>                 "0": 3
>               }
>             },
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": true,
>                 "last": 1,
>                 "value": [
>                   3,
>                   null
>                 ],
>                 "delta": {
>                   "0": 3
>                 },
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": true,
>                     "last": 1,
>                     "value": 3,
>                     "delta": 3
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": true
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": true
>               }
>             },
>             "peer": true
>           },
>           "b": {
>             "valid": true,
>             "modified": false,
>             "last": 0,
>             "value": {
>               "left": [
>                 10,
>                 null
>               ],
>               "right": null
>             },
>             "delta": null,
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": false,
>                 "last": 0,
>                 "value": [
>                   10,
>                   null
>                 ],
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": false,
>                     "last": 0,
>                     "value": 10,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": true
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": true
>               }
>             },
>             "peer": true
>           },
>           "keys": [
>             0
>           ],
>           "added": [],
>           "removed": [],
>           "rows": {
>             "0": {
>               "valid": true,
>               "modified": true,
>               "last": 1,
>               "value": {
>                 "left": [
>                   5,
>                   null
>                 ],
>                 "right": null
>               },
>               "delta": {
>                 "left": {
>                   "0": 5
>                 }
>               },
>               "all_valid": false,
>               "children": {
>                 "left": {
>                   "valid": true,
>                   "modified": true,
>                   "last": 1,
>                   "value": [
>                     5,
>                     null
>                   ],
>                   "delta": {
>                     "0": 5
>                   },
>                   "all_valid": false,
>                   "children": {
>                     "0": {
>                       "valid": true,
>                       "modified": true,
>                       "last": 1,
>                       "value": 5,
>                       "delta": 5
>                     },
>                     "1": {
>                       "valid": false,
>                       "modified": false,
>                       "last": "never",
>                       "value": null,
>                       "delta": null
>                     }
>                   },
>                   "peer": true
>                 },
>                 "right": {
>                   "valid": false,
>                   "modified": false,
>                   "last": "never",
>                   "value": null,
>                   "delta": null,
>                   "all_valid": false,
>                   "children": {
>                     "0": {
>                       "valid": false,
>                       "modified": false,
>                       "last": "never",
>                       "value": null,
>                       "delta": null
>                     },
>                     "1": {
>                       "valid": false,
>                       "modified": false,
>                       "last": "never",
>                       "value": null,
>                       "delta": null
>                     }
>                   },
>                   "peer": true
>                 }
>               },
>               "peer": true
>             }
>           },
>           "retired": {}
>         },
>         {
>           "a": {
>             "valid": true,
>             "modified": true,
>             "last": 2,
>             "value": {
>               "left": [
>                 10,
>                 null
>               ],
>               "right": null
>             },
>             "delta": {
>               "left": {
>                 "0": 10
>               }
>             },
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": true,
>                 "last": 2,
>                 "value": [
>                   10,
>                   null
>                 ],
>                 "delta": {
>                   "0": 10
>                 },
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": true,
>                     "last": 2,
>                     "value": 10,
>                     "delta": 10
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": true
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": true
>               }
>             },
>             "peer": true
>           },
>           "b": {
>             "valid": true,
>             "modified": false,
>             "last": 0,
>             "value": {
>               "left": [
>                 10,
>                 null
>               ],
>               "right": null
>             },
>             "delta": null,
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": false,
>                 "last": 0,
>                 "value": [
>                   10,
>                   null
>                 ],
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": false,
>                     "last": 0,
>                     "value": 10,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": true
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": true
>               }
>             },
>             "peer": true
>           },
>           "keys": [
>             0
>           ],
>           "added": [],
>           "removed": [],
>           "rows": {
>             "0": {
>               "valid": true,
>               "modified": true,
>               "last": 2,
>               "value": {
>                 "left": [
>                   15,
>                   null
>                 ],
>                 "right": null
>               },
>               "delta": {
>                 "left": {
>                   "0": 15
>                 }
>               },
>               "all_valid": false,
>               "children": {
>                 "left": {
>                   "valid": true,
>                   "modified": true,
>                   "last": 2,
>                   "value": [
>                     15,
>                     null
>                   ],
>                   "delta": {
>                     "0": 15
>                   },
>                   "all_valid": false,
>                   "children": {
>                     "0": {
>                       "valid": true,
>                       "modified": true,
>                       "last": 2,
>                       "value": 15,
>                       "delta": 15
>                     },
>                     "1": {
>                       "valid": false,
>                       "modified": false,
>                       "last": "never",
>                       "value": null,
>                       "delta": null
>                     }
>                   },
>                   "peer": true
>                 },
>                 "right": {
>                   "valid": false,
>                   "modified": false,
>                   "last": "never",
>                   "value": null,
>                   "delta": null,
>                   "all_valid": false,
>                   "children": {
>                     "0": {
>                       "valid": false,
>                       "modified": false,
>                       "last": "never",
>                       "value": null,
>                       "delta": null
>                     },
>                     "1": {
>                       "valid": false,
>                       "modified": false,
>                       "last": "never",
>                       "value": null,
>                       "delta": null
>                     }
>                   },
>                   "peer": true
>                 }
>               },
>               "peer": true
>             }
>           },
>           "retired": {}
>         },
>         {
>           "a": {
>             "valid": true,
>             "modified": false,
>             "last": 2,
>             "value": {
>               "left": [
>                 10,
>                 null
>               ],
>               "right": null
>             },
>             "delta": null,
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": false,
>                 "last": 2,
>                 "value": [
>                   10,
>                   null
>                 ],
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": false,
>                     "last": 2,
>                     "value": 10,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": true
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": true
>               }
>             },
>             "peer": true
>           },
>           "b": {
>             "valid": true,
>             "modified": false,
>             "last": 0,
>             "value": {
>               "left": [
>                 10,
>                 null
>               ],
>               "right": null
>             },
>             "delta": null,
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": false,
>                 "last": 0,
>                 "value": [
>                   10,
>                   null
>                 ],
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": false,
>                     "last": 0,
>                     "value": 10,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": true
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": true
>               }
>             },
>             "peer": true
>           },
>           "keys": [
>             0
>           ],
>           "added": [],
>           "removed": [],
>           "rows": {
>             "0": {
>               "valid": true,
>               "modified": false,
>               "last": 2,
>               "value": {
>                 "left": [
>                   15,
>                   null
>                 ],
>                 "right": null
>               },
>               "delta": null,
>               "all_valid": false,
>               "children": {
>                 "left": {
>                   "valid": true,
>                   "modified": false,
>                   "last": 2,
>                   "value": [
>                     15,
>                     null
>                   ],
>                   "delta": null,
>                   "all_valid": false,
>                   "children": {
>                     "0": {
>                       "valid": true,
>                       "modified": false,
>                       "last": 2,
>                       "value": 15,
>                       "delta": null
>                     },
>                     "1": {
>                       "valid": false,
>                       "modified": false,
>                       "last": "never",
>                       "value": null,
>                       "delta": null
>                     }
>                   },
>                   "peer": true
>                 },
>                 "right": {
>                   "valid": false,
>                   "modified": false,
>                   "last": "never",
>                   "value": null,
>                   "delta": null,
>                   "all_valid": false,
>                   "children": {
>                     "0": {
>                       "valid": false,
>                       "modified": false,
>                       "last": "never",
>                       "value": null,
>                       "delta": null
>                     },
>                     "1": {
>                       "valid": false,
>                       "modified": false,
>                       "last": "never",
>                       "value": null,
>                       "delta": null
>                     }
>                   },
>                   "peer": true
>                 }
>               },
>               "peer": true
>             }
>           },
>           "retired": {}
>         },
>         {
>           "a": {
>             "valid": true,
>             "modified": false,
>             "last": 2,
>             "value": {
>               "left": [
>                 10,
>                 null
>               ],
>               "right": null
>             },
>             "delta": null,
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": false,
>                 "last": 2,
>                 "value": [
>                   10,
>                   null
>                 ],
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": false,
>                     "last": 2,
>                     "value": 10,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": true
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": true
>               }
>             },
>             "peer": true
>           },
>           "b": {
>             "valid": true,
>             "modified": false,
>             "last": 0,
>             "value": {
>               "left": [
>                 10,
>                 null
>               ],
>               "right": null
>             },
>             "delta": null,
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": false,
>                 "last": 0,
>                 "value": [
>                   10,
>                   null
>                 ],
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": false,
>                     "last": 0,
>                     "value": 10,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": true
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": true
>               }
>             },
>             "peer": true
>           },
>           "keys": [
>             0
>           ],
>           "added": [],
>           "removed": [],
>           "rows": {
>             "0": {
>               "valid": true,
>               "modified": true,
>               "last": 4,
>               "value": {
>                 "left": [
>                   -15,
>                   null
>                 ],
>                 "right": null
>               },
>               "delta": {
>                 "left": {
>                   "0": -15
>                 }
>               },
>               "all_valid": false,
>               "children": {
>                 "left": {
>                   "valid": true,
>                   "modified": true,
>                   "last": 4,
>                   "value": [
>                     -15,
>                     null
>                   ],
>                   "delta": {
>                     "0": -15
>                   },
>                   "all_valid": false,
>                   "children": {
>                     "0": {
>                       "valid": true,
>                       "modified": true,
>                       "last": 4,
>                       "value": -15,
>                       "delta": -15
>                     },
>                     "1": {
>                       "valid": false,
>                       "modified": false,
>                       "last": "never",
>                       "value": null,
>                       "delta": null
>                     }
>                   },
>                   "peer": true
>                 },
>                 "right": {
>                   "valid": false,
>                   "modified": false,
>                   "last": "never",
>                   "value": null,
>                   "delta": null,
>                   "all_valid": false,
>                   "children": {
>                     "0": {
>                       "valid": false,
>                       "modified": false,
>                       "last": "never",
>                       "value": null,
>                       "delta": null
>                     },
>                     "1": {
>                       "valid": false,
>                       "modified": false,
>                       "last": "never",
>                       "value": null,
>                       "delta": null
>                     }
>                   },
>                   "peer": true
>                 }
>               },
>               "peer": true
>             }
>           },
>           "retired": {}
>         },
>         {
>           "a": {
>             "valid": true,
>             "modified": false,
>             "last": 2,
>             "value": {
>               "left": [
>                 10,
>                 null
>               ],
>               "right": null
>             },
>             "delta": null,
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": false,
>                 "last": 2,
>                 "value": [
>                   10,
>                   null
>                 ],
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": false,
>                     "last": 2,
>                     "value": 10,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": true
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": true
>               }
>             },
>             "peer": true
>           },
>           "b": {
>             "valid": true,
>             "modified": false,
>             "last": 0,
>             "value": {
>               "left": [
>                 10,
>                 null
>               ],
>               "right": null
>             },
>             "delta": null,
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": false,
>                 "last": 0,
>                 "value": [
>                   10,
>                   null
>                 ],
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": false,
>                     "last": 0,
>                     "value": 10,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": true
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": true
>               }
>             },
>             "peer": true
>           },
>           "keys": [],
>           "added": [],
>           "removed": [
>             0
>           ],
>           "rows": {},
>           "retired": {
>             "0": {
>               "valid": true,
>               "modified": false,
>               "last": 4,
>               "value": {
>                 "left": [
>                   -15,
>                   null
>                 ],
>                 "right": null
>               },
>               "delta": null,
>               "all_valid": false,
>               "children": {
>                 "left": {
>                   "valid": true,
>                   "modified": false,
>                   "last": 4,
>                   "value": [
>                     -15,
>                     null
>                   ],
>                   "delta": null,
>                   "all_valid": false,
>                   "children": {
>                     "0": {
>                       "valid": true,
>                       "modified": false,
>                       "last": 4,
>                       "value": -15,
>                       "delta": null
>                     },
>                     "1": {
>                       "valid": false,
>                       "modified": false,
>                       "last": "never",
>                       "value": null,
>                       "delta": null
>                     }
>                   },
>                   "peer": true
>                 },
>                 "right": {
>                   "valid": false,
>                   "modified": false,
>                   "last": "never",
>                   "value": null,
>                   "delta": null,
>                   "all_valid": false,
>                   "children": {
>                     "0": {
>                       "valid": false,
>                       "modified": false,
>                       "last": "never",
>                       "value": null,
>                       "delta": null
>                     },
>                     "1": {
>                       "valid": false,
>                       "modified": false,
>                       "last": "never",
>                       "value": null,
>                       "delta": null
>                     }
>                   },
>                   "peer": true
>                 }
>               },
>               "peer": true
>             }
>           }
>         },
>         {
>           "a": {
>             "valid": true,
>             "modified": false,
>             "last": 2,
>             "value": {
>               "left": [
>                 10,
>                 null
>               ],
>               "right": null
>             },
>             "delta": null,
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": false,
>                 "last": 2,
>                 "value": [
>                   10,
>                   null
>                 ],
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": false,
>                     "last": 2,
>                     "value": 10,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": true
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": true
>               }
>             },
>             "peer": true
>           },
>           "b": {
>             "valid": true,
>             "modified": false,
>             "last": 0,
>             "value": {
>               "left": [
>                 10,
>                 null
>               ],
>               "right": null
>             },
>             "delta": null,
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": false,
>                 "last": 0,
>                 "value": [
>                   10,
>                   null
>                 ],
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": false,
>                     "last": 0,
>                     "value": 10,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": true
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": true
>               }
>             },
>             "peer": true
>           },
>           "keys": [],
>           "added": [],
>           "removed": [],
>           "rows": {},
>           "retired": {}
>         },
>         {
>           "a": {
>             "valid": true,
>             "modified": true,
>             "last": 7,
>             "value": {
>               "left": [
>                 5,
>                 null
>               ],
>               "right": null
>             },
>             "delta": {
>               "left": {
>                 "0": 5
>               }
>             },
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": true,
>                 "last": 7,
>                 "value": [
>                   5,
>                   null
>                 ],
>                 "delta": {
>                   "0": 5
>                 },
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": true,
>                     "last": 7,
>                     "value": 5,
>                     "delta": 5
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": true
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": true
>               }
>             },
>             "peer": true
>           },
>           "b": {
>             "valid": true,
>             "modified": false,
>             "last": 0,
>             "value": {
>               "left": [
>                 10,
>                 null
>               ],
>               "right": null
>             },
>             "delta": null,
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": false,
>                 "last": 0,
>                 "value": [
>                   10,
>                   null
>                 ],
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": false,
>                     "last": 0,
>                     "value": 10,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": true
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": true
>               }
>             },
>             "peer": true
>           },
>           "keys": [
>             0
>           ],
>           "added": [
>             0
>           ],
>           "removed": [],
>           "rows": {
>             "0": {
>               "valid": true,
>               "modified": true,
>               "last": 7,
>               "value": {
>                 "left": [
>                   5,
>                   null
>                 ],
>                 "right": null
>               },
>               "delta": {
>                 "left": {
>                   "0": 5
>                 }
>               },
>               "all_valid": false,
>               "children": {
>                 "left": {
>                   "valid": true,
>                   "modified": true,
>                   "last": 7,
>                   "value": [
>                     5,
>                     null
>                   ],
>                   "delta": {
>                     "0": 5
>                   },
>                   "all_valid": false,
>                   "children": {
>                     "0": {
>                       "valid": true,
>                       "modified": true,
>                       "last": 7,
>                       "value": 5,
>                       "delta": 5
>                     },
>                     "1": {
>                       "valid": false,
>                       "modified": false,
>                       "last": "never",
>                       "value": null,
>                       "delta": null
>                     }
>                   },
>                   "peer": true
>                 },
>                 "right": {
>                   "valid": false,
>                   "modified": false,
>                   "last": "never",
>                   "value": null,
>                   "delta": null,
>                   "all_valid": false,
>                   "children": {
>                     "0": {
>                       "valid": false,
>                       "modified": false,
>                       "last": "never",
>                       "value": null,
>                       "delta": null
>                     },
>                     "1": {
>                       "valid": false,
>                       "modified": false,
>                       "last": "never",
>                       "value": null,
>                       "delta": null
>                     }
>                   },
>                   "peer": true
>                 }
>               },
>               "peer": true
>             }
>           },
>           "retired": {}
>         },
>         {
>           "a": {
>             "valid": true,
>             "modified": false,
>             "last": 7,
>             "value": {
>               "left": [
>                 5,
>                 null
>               ],
>               "right": null
>             },
>             "delta": null,
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": false,
>                 "last": 7,
>                 "value": [
>                   5,
>                   null
>                 ],
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": false,
>                     "last": 7,
>                     "value": 5,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": true
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": true
>               }
>             },
>             "peer": true
>           },
>           "b": {
>             "valid": true,
>             "modified": false,
>             "last": 0,
>             "value": {
>               "left": [
>                 10,
>                 null
>               ],
>               "right": null
>             },
>             "delta": null,
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": false,
>                 "last": 0,
>                 "value": [
>                   10,
>                   null
>                 ],
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": false,
>                     "last": 0,
>                     "value": 10,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": true
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": true
>               }
>             },
>             "peer": true
>           },
>           "keys": [
>             0
>           ],
>           "added": [],
>           "removed": [],
>           "rows": {
>             "0": {
>               "valid": true,
>               "modified": false,
>               "last": 7,
>               "value": {
>                 "left": [
>                   5,
>                   null
>                 ],
>                 "right": null
>               },
>               "delta": null,
>               "all_valid": false,
>               "children": {
>                 "left": {
>                   "valid": true,
>                   "modified": false,
>                   "last": 7,
>                   "value": [
>                     5,
>                     null
>                   ],
>                   "delta": null,
>                   "all_valid": false,
>                   "children": {
>                     "0": {
>                       "valid": true,
>                       "modified": false,
>                       "last": 7,
>                       "value": 5,
>                       "delta": null
>                     },
>                     "1": {
>                       "valid": false,
>                       "modified": false,
>                       "last": "never",
>                       "value": null,
>                       "delta": null
>                     }
>                   },
>                   "peer": true
>                 },
>                 "right": {
>                   "valid": false,
>                   "modified": false,
>                   "last": "never",
>                   "value": null,
>                   "delta": null,
>                   "all_valid": false,
>                   "children": {
>                     "0": {
>                       "valid": false,
>                       "modified": false,
>                       "last": "never",
>                       "value": null,
>                       "delta": null
>                     },
>                     "1": {
>                       "valid": false,
>                       "modified": false,
>                       "last": "never",
>                       "value": null,
>                       "delta": null
>                     }
>                   },
>                   "peer": true
>                 }
>               },
>               "peer": true
>             }
>           },
>           "retired": {}
>         },
>         {
>           "a": {
>             "valid": true,
>             "modified": false,
>             "last": 7,
>             "value": {
>               "left": [
>                 5,
>                 null
>               ],
>               "right": null
>             },
>             "delta": null,
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": false,
>                 "last": 7,
>                 "value": [
>                   5,
>                   null
>                 ],
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": false,
>                     "last": 7,
>                     "value": 5,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": true
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": true
>               }
>             },
>             "peer": true
>           },
>           "b": {
>             "valid": true,
>             "modified": false,
>             "last": 0,
>             "value": {
>               "left": [
>                 10,
>                 null
>               ],
>               "right": null
>             },
>             "delta": null,
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": false,
>                 "last": 0,
>                 "value": [
>                   10,
>                   null
>                 ],
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": false,
>                     "last": 0,
>                     "value": 10,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": true
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": true
>               }
>             },
>             "peer": true
>           },
>           "keys": [
>             0
>           ],
>           "added": [],
>           "removed": [],
>           "rows": {
>             "0": {
>               "valid": true,
>               "modified": true,
>               "last": 9,
>               "value": {
>                 "left": [
>                   -5,
>                   null
>                 ],
>                 "right": null
>               },
>               "delta": {
>                 "left": {
>                   "0": -5
>                 }
>               },
>               "all_valid": false,
>               "children": {
>                 "left": {
>                   "valid": true,
>                   "modified": true,
>                   "last": 9,
>                   "value": [
>                     -5,
>                     null
>                   ],
>                   "delta": {
>                     "0": -5
>                   },
>                   "all_valid": false,
>                   "children": {
>                     "0": {
>                       "valid": true,
>                       "modified": true,
>                       "last": 9,
>                       "value": -5,
>                       "delta": -5
>                     },
>                     "1": {
>                       "valid": false,
>                       "modified": false,
>                       "last": "never",
>                       "value": null,
>                       "delta": null
>                     }
>                   },
>                   "peer": true
>                 },
>                 "right": {
>                   "valid": false,
>                   "modified": false,
>                   "last": "never",
>                   "value": null,
>                   "delta": null,
>                   "all_valid": false,
>                   "children": {
>                     "0": {
>                       "valid": false,
>                       "modified": false,
>                       "last": "never",
>                       "value": null,
>                       "delta": null
>                     },
>                     "1": {
>                       "valid": false,
>                       "modified": false,
>                       "last": "never",
>                       "value": null,
>                       "delta": null
>                     }
>                   },
>                   "peer": true
>                 }
>               },
>               "peer": true
>             }
>           },
>           "retired": {}
>         },
>         {
>           "a": {
>             "valid": true,
>             "modified": false,
>             "last": 7,
>             "value": {
>               "left": [
>                 5,
>                 null
>               ],
>               "right": null
>             },
>             "delta": null,
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": false,
>                 "last": 7,
>                 "value": [
>                   5,
>                   null
>                 ],
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": false,
>                     "last": 7,
>                     "value": 5,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": true
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": true
>               }
>             },
>             "peer": true
>           },
>           "b": {
>             "valid": true,
>             "modified": false,
>             "last": 0,
>             "value": {
>               "left": [
>                 10,
>                 null
>               ],
>               "right": null
>             },
>             "delta": null,
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": false,
>                 "last": 0,
>                 "value": [
>                   10,
>                   null
>                 ],
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": false,
>                     "last": 0,
>                     "value": 10,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": true
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": true
>               }
>             },
>             "peer": true
>           },
>           "keys": [
>             0
>           ],
>           "added": [],
>           "removed": [],
>           "rows": {
>             "0": {
>               "valid": true,
>               "modified": false,
>               "last": 9,
>               "value": {
>                 "left": [
>                   -5,
>                   null
>                 ],
>                 "right": null
>               },
>               "delta": null,
>               "all_valid": false,
>               "children": {
>                 "left": {
>                   "valid": true,
>                   "modified": false,
>                   "last": 9,
>                   "value": [
>                     -5,
>                     null
>                   ],
>                   "delta": null,
>                   "all_valid": false,
>                   "children": {
>                     "0": {
>                       "valid": true,
>                       "modified": false,
>                       "last": 9,
>                       "value": -5,
>                       "delta": null
>                     },
>                     "1": {
>                       "valid": false,
>                       "modified": false,
>                       "last": "never",
>                       "value": null,
>                       "delta": null
>                     }
>                   },
>                   "peer": true
>                 },
>                 "right": {
>                   "valid": false,
>                   "modified": false,
>                   "last": "never",
>                   "value": null,
>                   "delta": null,
>                   "all_valid": false,
>                   "children": {
>                     "0": {
>                       "valid": false,
>                       "modified": false,
>                       "last": "never",
>                       "value": null,
>                       "delta": null
>                     },
>                     "1": {
>                       "valid": false,
>                       "modified": false,
>                       "last": "never",
>                       "value": null,
>                       "delta": null
>                     }
>                   },
>                   "peer": true
>                 }
>               },
>               "peer": true
>             }
>           },
>           "retired": {}
>         }
>       ],
>       "child_ticks": [
>         {
>           "time": 0,
>           "input": {
>             "valid": true,
>             "modified": true,
>             "last": 0,
>             "value": {
>               "left": [
>                 2,
>                 null
>               ],
>               "right": null
>             },
>             "delta": {
>               "left": {
>                 "0": 2
>               }
>             },
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": true,
>                 "last": 0,
>                 "value": [
>                   2,
>                   null
>                 ],
>                 "delta": {
>                   "0": 2
>                 },
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": true,
>                     "last": 0,
>                     "value": 2,
>                     "delta": 2
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": true
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": true
>               }
>             },
>             "peer": true
>           },
>           "output": {
>             "valid": true,
>             "modified": true,
>             "last": 0,
>             "value": {
>               "left": [
>                 2,
>                 null
>               ],
>               "right": null
>             },
>             "delta": {
>               "left": {
>                 "0": 2
>               }
>             },
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": true,
>                 "last": 0,
>                 "value": [
>                   2,
>                   null
>                 ],
>                 "delta": {
>                   "0": 2
>                 },
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": true,
>                     "last": 0,
>                     "value": 2,
>                     "delta": 2
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 }
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 }
>               }
>             }
>           }
>         },
>         {
>           "time": 1,
>           "input": {
>             "valid": true,
>             "modified": true,
>             "last": 1,
>             "value": {
>               "left": [
>                 3,
>                 null
>               ],
>               "right": null
>             },
>             "delta": {
>               "left": {
>                 "0": 3
>               }
>             },
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": true,
>                 "last": 1,
>                 "value": [
>                   3,
>                   null
>                 ],
>                 "delta": {
>                   "0": 3
>                 },
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": true,
>                     "last": 1,
>                     "value": 3,
>                     "delta": 3
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": true
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": true
>               }
>             },
>             "peer": true
>           },
>           "output": {
>             "valid": true,
>             "modified": true,
>             "last": 1,
>             "value": {
>               "left": [
>                 5,
>                 null
>               ],
>               "right": null
>             },
>             "delta": {
>               "left": {
>                 "0": 5
>               }
>             },
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": true,
>                 "last": 1,
>                 "value": [
>                   5,
>                   null
>                 ],
>                 "delta": {
>                   "0": 5
>                 },
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": true,
>                     "last": 1,
>                     "value": 5,
>                     "delta": 5
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 }
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 }
>               }
>             }
>           }
>         },
>         {
>           "time": 2,
>           "input": {
>             "valid": true,
>             "modified": true,
>             "last": 2,
>             "value": {
>               "left": [
>                 10,
>                 null
>               ],
>               "right": null
>             },
>             "delta": {
>               "left": {
>                 "0": 10
>               }
>             },
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": true,
>                 "last": 2,
>                 "value": [
>                   10,
>                   null
>                 ],
>                 "delta": {
>                   "0": 10
>                 },
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": true,
>                     "last": 2,
>                     "value": 10,
>                     "delta": 10
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": true
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": true
>               }
>             },
>             "peer": true
>           },
>           "output": {
>             "valid": true,
>             "modified": true,
>             "last": 2,
>             "value": {
>               "left": [
>                 15,
>                 null
>               ],
>               "right": null
>             },
>             "delta": {
>               "left": {
>                 "0": 15
>               }
>             },
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": true,
>                 "last": 2,
>                 "value": [
>                   15,
>                   null
>                 ],
>                 "delta": {
>                   "0": 15
>                 },
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": true,
>                     "last": 2,
>                     "value": 15,
>                     "delta": 15
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 }
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 }
>               }
>             }
>           }
>         },
>         {
>           "time": 4,
>           "input": {
>             "valid": true,
>             "modified": false,
>             "last": 2,
>             "value": {
>               "left": [
>                 10,
>                 null
>               ],
>               "right": null
>             },
>             "delta": null,
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": false,
>                 "last": 2,
>                 "value": [
>                   10,
>                   null
>                 ],
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": false,
>                     "last": 2,
>                     "value": 10,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": true
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": true
>               }
>             },
>             "peer": true
>           },
>           "output": {
>             "valid": true,
>             "modified": true,
>             "last": 4,
>             "value": {
>               "left": [
>                 -15,
>                 null
>               ],
>               "right": null
>             },
>             "delta": {
>               "left": {
>                 "0": -15
>               }
>             },
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": true,
>                 "last": 4,
>                 "value": [
>                   -15,
>                   null
>                 ],
>                 "delta": {
>                   "0": -15
>                 },
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": true,
>                     "last": 4,
>                     "value": -15,
>                     "delta": -15
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 }
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 }
>               }
>             }
>           }
>         },
>         {
>           "time": 7,
>           "input": {
>             "valid": true,
>             "modified": true,
>             "last": 7,
>             "value": {
>               "left": [
>                 5,
>                 null
>               ],
>               "right": null
>             },
>             "delta": {
>               "left": {
>                 "0": 5
>               }
>             },
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": true,
>                 "last": 7,
>                 "value": [
>                   5,
>                   null
>                 ],
>                 "delta": {
>                   "0": 5
>                 },
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": true,
>                     "last": 7,
>                     "value": 5,
>                     "delta": 5
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": true
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": true
>               }
>             },
>             "peer": true
>           },
>           "output": {
>             "valid": true,
>             "modified": true,
>             "last": 7,
>             "value": {
>               "left": [
>                 5,
>                 null
>               ],
>               "right": null
>             },
>             "delta": {
>               "left": {
>                 "0": 5
>               }
>             },
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": true,
>                 "last": 7,
>                 "value": [
>                   5,
>                   null
>                 ],
>                 "delta": {
>                   "0": 5
>                 },
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": true,
>                     "last": 7,
>                     "value": 5,
>                     "delta": 5
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 }
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 }
>               }
>             }
>           }
>         },
>         {
>           "time": 9,
>           "input": {
>             "valid": true,
>             "modified": false,
>             "last": 7,
>             "value": {
>               "left": [
>                 5,
>                 null
>               ],
>               "right": null
>             },
>             "delta": null,
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": false,
>                 "last": 7,
>                 "value": [
>                   5,
>                   null
>                 ],
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": false,
>                     "last": 7,
>                     "value": 5,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": true
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": true
>               }
>             },
>             "peer": true
>           },
>           "output": {
>             "valid": true,
>             "modified": true,
>             "last": 9,
>             "value": {
>               "left": [
>                 -5,
>                 null
>               ],
>               "right": null
>             },
>             "delta": {
>               "left": {
>                 "0": -5
>               }
>             },
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": true,
>                 "last": 9,
>                 "value": [
>                   -5,
>                   null
>                 ],
>                 "delta": {
>                   "0": -5
>                 },
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": true,
>                     "last": 9,
>                     "value": -5,
>                     "delta": -5
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 }
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 }
>               }
>             }
>           }
>         }
>       ],
>       "events": [
>         "start",
>         "stop",
>         "start",
>         "stop"
>       ]
>     },
>     "mixed_capture": {
>       "ticks": [
>         {
>           "a": {
>             "valid": true,
>             "modified": true,
>             "last": 0,
>             "value": {
>               "left": [
>                 2,
>                 null
>               ],
>               "right": null
>             },
>             "delta": {
>               "left": {
>                 "0": 2
>               }
>             },
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": true,
>                 "last": 0,
>                 "value": [
>                   2,
>                   null
>                 ],
>                 "delta": {
>                   "0": 2
>                 },
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": true,
>                     "last": 0,
>                     "value": 2,
>                     "delta": 2
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": true
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": false
>               }
>             },
>             "peer": false
>           },
>           "b": {
>             "valid": true,
>             "modified": true,
>             "last": 0,
>             "value": {
>               "left": [
>                 10,
>                 null
>               ],
>               "right": null
>             },
>             "delta": {
>               "left": {
>                 "0": 10
>               }
>             },
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": true,
>                 "last": 0,
>                 "value": [
>                   10,
>                   null
>                 ],
>                 "delta": {
>                   "0": 10
>                 },
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": true,
>                     "last": 0,
>                     "value": 10,
>                     "delta": 10
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": true
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": false
>               }
>             },
>             "peer": false
>           },
>           "keys": [
>             0
>           ],
>           "added": [
>             0
>           ],
>           "removed": [],
>           "rows": {
>             "0": {
>               "valid": true,
>               "modified": true,
>               "last": 0,
>               "value": {
>                 "left": [
>                   2,
>                   null
>                 ],
>                 "right": null
>               },
>               "delta": {
>                 "left": {
>                   "0": 2
>                 }
>               },
>               "all_valid": false,
>               "children": {
>                 "left": {
>                   "valid": true,
>                   "modified": true,
>                   "last": 0,
>                   "value": [
>                     2,
>                     null
>                   ],
>                   "delta": {
>                     "0": 2
>                   },
>                   "all_valid": false,
>                   "children": {
>                     "0": {
>                       "valid": true,
>                       "modified": true,
>                       "last": 0,
>                       "value": 2,
>                       "delta": 2
>                     },
>                     "1": {
>                       "valid": false,
>                       "modified": false,
>                       "last": "never",
>                       "value": null,
>                       "delta": null
>                     }
>                   },
>                   "peer": true
>                 },
>                 "right": {
>                   "valid": false,
>                   "modified": false,
>                   "last": "never",
>                   "value": null,
>                   "delta": null,
>                   "all_valid": false,
>                   "children": {
>                     "0": {
>                       "valid": false,
>                       "modified": false,
>                       "last": "never",
>                       "value": null,
>                       "delta": null
>                     },
>                     "1": {
>                       "valid": false,
>                       "modified": false,
>                       "last": "never",
>                       "value": null,
>                       "delta": null
>                     }
>                   },
>                   "peer": true
>                 }
>               },
>               "peer": true
>             }
>           },
>           "retired": {}
>         },
>         {
>           "a": {
>             "valid": true,
>             "modified": true,
>             "last": 1,
>             "value": {
>               "left": [
>                 3,
>                 null
>               ],
>               "right": null
>             },
>             "delta": {
>               "left": {
>                 "0": 3
>               }
>             },
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": true,
>                 "last": 1,
>                 "value": [
>                   3,
>                   null
>                 ],
>                 "delta": {
>                   "0": 3
>                 },
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": true,
>                     "last": 1,
>                     "value": 3,
>                     "delta": 3
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": true
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": false
>               }
>             },
>             "peer": false
>           },
>           "b": {
>             "valid": true,
>             "modified": false,
>             "last": 0,
>             "value": {
>               "left": [
>                 10,
>                 null
>               ],
>               "right": null
>             },
>             "delta": null,
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": false,
>                 "last": 0,
>                 "value": [
>                   10,
>                   null
>                 ],
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": false,
>                     "last": 0,
>                     "value": 10,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": true
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": false
>               }
>             },
>             "peer": false
>           },
>           "keys": [
>             0
>           ],
>           "added": [],
>           "removed": [],
>           "rows": {
>             "0": {
>               "valid": true,
>               "modified": true,
>               "last": 1,
>               "value": {
>                 "left": [
>                   5,
>                   null
>                 ],
>                 "right": null
>               },
>               "delta": {
>                 "left": {
>                   "0": 5
>                 }
>               },
>               "all_valid": false,
>               "children": {
>                 "left": {
>                   "valid": true,
>                   "modified": true,
>                   "last": 1,
>                   "value": [
>                     5,
>                     null
>                   ],
>                   "delta": {
>                     "0": 5
>                   },
>                   "all_valid": false,
>                   "children": {
>                     "0": {
>                       "valid": true,
>                       "modified": true,
>                       "last": 1,
>                       "value": 5,
>                       "delta": 5
>                     },
>                     "1": {
>                       "valid": false,
>                       "modified": false,
>                       "last": "never",
>                       "value": null,
>                       "delta": null
>                     }
>                   },
>                   "peer": true
>                 },
>                 "right": {
>                   "valid": false,
>                   "modified": false,
>                   "last": "never",
>                   "value": null,
>                   "delta": null,
>                   "all_valid": false,
>                   "children": {
>                     "0": {
>                       "valid": false,
>                       "modified": false,
>                       "last": "never",
>                       "value": null,
>                       "delta": null
>                     },
>                     "1": {
>                       "valid": false,
>                       "modified": false,
>                       "last": "never",
>                       "value": null,
>                       "delta": null
>                     }
>                   },
>                   "peer": true
>                 }
>               },
>               "peer": true
>             }
>           },
>           "retired": {}
>         },
>         {
>           "a": {
>             "valid": true,
>             "modified": true,
>             "last": 2,
>             "value": {
>               "left": [
>                 10,
>                 null
>               ],
>               "right": null
>             },
>             "delta": {
>               "left": {
>                 "0": 10
>               }
>             },
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": true,
>                 "last": 2,
>                 "value": [
>                   10,
>                   null
>                 ],
>                 "delta": {
>                   "0": 10
>                 },
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": true,
>                     "last": 2,
>                     "value": 10,
>                     "delta": 10
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": true
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": false
>               }
>             },
>             "peer": false
>           },
>           "b": {
>             "valid": true,
>             "modified": false,
>             "last": 0,
>             "value": {
>               "left": [
>                 10,
>                 null
>               ],
>               "right": null
>             },
>             "delta": null,
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": false,
>                 "last": 0,
>                 "value": [
>                   10,
>                   null
>                 ],
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": false,
>                     "last": 0,
>                     "value": 10,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": true
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": false
>               }
>             },
>             "peer": false
>           },
>           "keys": [
>             0
>           ],
>           "added": [],
>           "removed": [],
>           "rows": {
>             "0": {
>               "valid": true,
>               "modified": true,
>               "last": 2,
>               "value": {
>                 "left": [
>                   15,
>                   null
>                 ],
>                 "right": null
>               },
>               "delta": {
>                 "left": {
>                   "0": 15
>                 }
>               },
>               "all_valid": false,
>               "children": {
>                 "left": {
>                   "valid": true,
>                   "modified": true,
>                   "last": 2,
>                   "value": [
>                     15,
>                     null
>                   ],
>                   "delta": {
>                     "0": 15
>                   },
>                   "all_valid": false,
>                   "children": {
>                     "0": {
>                       "valid": true,
>                       "modified": true,
>                       "last": 2,
>                       "value": 15,
>                       "delta": 15
>                     },
>                     "1": {
>                       "valid": false,
>                       "modified": false,
>                       "last": "never",
>                       "value": null,
>                       "delta": null
>                     }
>                   },
>                   "peer": true
>                 },
>                 "right": {
>                   "valid": false,
>                   "modified": false,
>                   "last": "never",
>                   "value": null,
>                   "delta": null,
>                   "all_valid": false,
>                   "children": {
>                     "0": {
>                       "valid": false,
>                       "modified": false,
>                       "last": "never",
>                       "value": null,
>                       "delta": null
>                     },
>                     "1": {
>                       "valid": false,
>                       "modified": false,
>                       "last": "never",
>                       "value": null,
>                       "delta": null
>                     }
>                   },
>                   "peer": true
>                 }
>               },
>               "peer": true
>             }
>           },
>           "retired": {}
>         },
>         {
>           "a": {
>             "valid": true,
>             "modified": false,
>             "last": 2,
>             "value": {
>               "left": [
>                 10,
>                 null
>               ],
>               "right": null
>             },
>             "delta": null,
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": false,
>                 "last": 2,
>                 "value": [
>                   10,
>                   null
>                 ],
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": false,
>                     "last": 2,
>                     "value": 10,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": true
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": false
>               }
>             },
>             "peer": false
>           },
>           "b": {
>             "valid": true,
>             "modified": false,
>             "last": 0,
>             "value": {
>               "left": [
>                 10,
>                 null
>               ],
>               "right": null
>             },
>             "delta": null,
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": false,
>                 "last": 0,
>                 "value": [
>                   10,
>                   null
>                 ],
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": false,
>                     "last": 0,
>                     "value": 10,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": true
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": false
>               }
>             },
>             "peer": false
>           },
>           "keys": [
>             0
>           ],
>           "added": [],
>           "removed": [],
>           "rows": {
>             "0": {
>               "valid": true,
>               "modified": false,
>               "last": 2,
>               "value": {
>                 "left": [
>                   15,
>                   null
>                 ],
>                 "right": null
>               },
>               "delta": null,
>               "all_valid": false,
>               "children": {
>                 "left": {
>                   "valid": true,
>                   "modified": false,
>                   "last": 2,
>                   "value": [
>                     15,
>                     null
>                   ],
>                   "delta": null,
>                   "all_valid": false,
>                   "children": {
>                     "0": {
>                       "valid": true,
>                       "modified": false,
>                       "last": 2,
>                       "value": 15,
>                       "delta": null
>                     },
>                     "1": {
>                       "valid": false,
>                       "modified": false,
>                       "last": "never",
>                       "value": null,
>                       "delta": null
>                     }
>                   },
>                   "peer": true
>                 },
>                 "right": {
>                   "valid": false,
>                   "modified": false,
>                   "last": "never",
>                   "value": null,
>                   "delta": null,
>                   "all_valid": false,
>                   "children": {
>                     "0": {
>                       "valid": false,
>                       "modified": false,
>                       "last": "never",
>                       "value": null,
>                       "delta": null
>                     },
>                     "1": {
>                       "valid": false,
>                       "modified": false,
>                       "last": "never",
>                       "value": null,
>                       "delta": null
>                     }
>                   },
>                   "peer": true
>                 }
>               },
>               "peer": true
>             }
>           },
>           "retired": {}
>         },
>         {
>           "a": {
>             "valid": true,
>             "modified": false,
>             "last": 2,
>             "value": {
>               "left": [
>                 10,
>                 null
>               ],
>               "right": null
>             },
>             "delta": null,
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": false,
>                 "last": 2,
>                 "value": [
>                   10,
>                   null
>                 ],
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": false,
>                     "last": 2,
>                     "value": 10,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": true
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": false
>               }
>             },
>             "peer": false
>           },
>           "b": {
>             "valid": true,
>             "modified": false,
>             "last": 0,
>             "value": {
>               "left": [
>                 10,
>                 null
>               ],
>               "right": null
>             },
>             "delta": null,
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": false,
>                 "last": 0,
>                 "value": [
>                   10,
>                   null
>                 ],
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": false,
>                     "last": 0,
>                     "value": 10,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": true
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": false
>               }
>             },
>             "peer": false
>           },
>           "keys": [
>             0
>           ],
>           "added": [],
>           "removed": [],
>           "rows": {
>             "0": {
>               "valid": true,
>               "modified": true,
>               "last": 4,
>               "value": {
>                 "left": [
>                   -15,
>                   null
>                 ],
>                 "right": null
>               },
>               "delta": {
>                 "left": {
>                   "0": -15
>                 }
>               },
>               "all_valid": false,
>               "children": {
>                 "left": {
>                   "valid": true,
>                   "modified": true,
>                   "last": 4,
>                   "value": [
>                     -15,
>                     null
>                   ],
>                   "delta": {
>                     "0": -15
>                   },
>                   "all_valid": false,
>                   "children": {
>                     "0": {
>                       "valid": true,
>                       "modified": true,
>                       "last": 4,
>                       "value": -15,
>                       "delta": -15
>                     },
>                     "1": {
>                       "valid": false,
>                       "modified": false,
>                       "last": "never",
>                       "value": null,
>                       "delta": null
>                     }
>                   },
>                   "peer": true
>                 },
>                 "right": {
>                   "valid": false,
>                   "modified": false,
>                   "last": "never",
>                   "value": null,
>                   "delta": null,
>                   "all_valid": false,
>                   "children": {
>                     "0": {
>                       "valid": false,
>                       "modified": false,
>                       "last": "never",
>                       "value": null,
>                       "delta": null
>                     },
>                     "1": {
>                       "valid": false,
>                       "modified": false,
>                       "last": "never",
>                       "value": null,
>                       "delta": null
>                     }
>                   },
>                   "peer": true
>                 }
>               },
>               "peer": true
>             }
>           },
>           "retired": {}
>         },
>         {
>           "a": {
>             "valid": true,
>             "modified": false,
>             "last": 2,
>             "value": {
>               "left": [
>                 10,
>                 null
>               ],
>               "right": null
>             },
>             "delta": null,
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": false,
>                 "last": 2,
>                 "value": [
>                   10,
>                   null
>                 ],
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": false,
>                     "last": 2,
>                     "value": 10,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": true
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": false
>               }
>             },
>             "peer": false
>           },
>           "b": {
>             "valid": true,
>             "modified": false,
>             "last": 0,
>             "value": {
>               "left": [
>                 10,
>                 null
>               ],
>               "right": null
>             },
>             "delta": null,
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": false,
>                 "last": 0,
>                 "value": [
>                   10,
>                   null
>                 ],
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": false,
>                     "last": 0,
>                     "value": 10,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": true
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": false
>               }
>             },
>             "peer": false
>           },
>           "keys": [],
>           "added": [],
>           "removed": [
>             0
>           ],
>           "rows": {},
>           "retired": {
>             "0": {
>               "valid": true,
>               "modified": false,
>               "last": 4,
>               "value": {
>                 "left": [
>                   -15,
>                   null
>                 ],
>                 "right": null
>               },
>               "delta": null,
>               "all_valid": false,
>               "children": {
>                 "left": {
>                   "valid": true,
>                   "modified": false,
>                   "last": 4,
>                   "value": [
>                     -15,
>                     null
>                   ],
>                   "delta": null,
>                   "all_valid": false,
>                   "children": {
>                     "0": {
>                       "valid": true,
>                       "modified": false,
>                       "last": 4,
>                       "value": -15,
>                       "delta": null
>                     },
>                     "1": {
>                       "valid": false,
>                       "modified": false,
>                       "last": "never",
>                       "value": null,
>                       "delta": null
>                     }
>                   },
>                   "peer": true
>                 },
>                 "right": {
>                   "valid": false,
>                   "modified": false,
>                   "last": "never",
>                   "value": null,
>                   "delta": null,
>                   "all_valid": false,
>                   "children": {
>                     "0": {
>                       "valid": false,
>                       "modified": false,
>                       "last": "never",
>                       "value": null,
>                       "delta": null
>                     },
>                     "1": {
>                       "valid": false,
>                       "modified": false,
>                       "last": "never",
>                       "value": null,
>                       "delta": null
>                     }
>                   },
>                   "peer": true
>                 }
>               },
>               "peer": true
>             }
>           }
>         },
>         {
>           "a": {
>             "valid": true,
>             "modified": false,
>             "last": 2,
>             "value": {
>               "left": [
>                 10,
>                 null
>               ],
>               "right": null
>             },
>             "delta": null,
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": false,
>                 "last": 2,
>                 "value": [
>                   10,
>                   null
>                 ],
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": false,
>                     "last": 2,
>                     "value": 10,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": true
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": false
>               }
>             },
>             "peer": false
>           },
>           "b": {
>             "valid": true,
>             "modified": false,
>             "last": 0,
>             "value": {
>               "left": [
>                 10,
>                 null
>               ],
>               "right": null
>             },
>             "delta": null,
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": false,
>                 "last": 0,
>                 "value": [
>                   10,
>                   null
>                 ],
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": false,
>                     "last": 0,
>                     "value": 10,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": true
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": false
>               }
>             },
>             "peer": false
>           },
>           "keys": [],
>           "added": [],
>           "removed": [],
>           "rows": {},
>           "retired": {}
>         },
>         {
>           "a": {
>             "valid": true,
>             "modified": true,
>             "last": 7,
>             "value": {
>               "left": [
>                 5,
>                 null
>               ],
>               "right": null
>             },
>             "delta": {
>               "left": {
>                 "0": 5
>               }
>             },
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": true,
>                 "last": 7,
>                 "value": [
>                   5,
>                   null
>                 ],
>                 "delta": {
>                   "0": 5
>                 },
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": true,
>                     "last": 7,
>                     "value": 5,
>                     "delta": 5
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": true
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": false
>               }
>             },
>             "peer": false
>           },
>           "b": {
>             "valid": true,
>             "modified": false,
>             "last": 0,
>             "value": {
>               "left": [
>                 10,
>                 null
>               ],
>               "right": null
>             },
>             "delta": null,
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": false,
>                 "last": 0,
>                 "value": [
>                   10,
>                   null
>                 ],
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": false,
>                     "last": 0,
>                     "value": 10,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": true
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": false
>               }
>             },
>             "peer": false
>           },
>           "keys": [
>             0
>           ],
>           "added": [
>             0
>           ],
>           "removed": [],
>           "rows": {
>             "0": {
>               "valid": true,
>               "modified": true,
>               "last": 7,
>               "value": {
>                 "left": [
>                   5,
>                   null
>                 ],
>                 "right": null
>               },
>               "delta": {
>                 "left": {
>                   "0": 5
>                 }
>               },
>               "all_valid": false,
>               "children": {
>                 "left": {
>                   "valid": true,
>                   "modified": true,
>                   "last": 7,
>                   "value": [
>                     5,
>                     null
>                   ],
>                   "delta": {
>                     "0": 5
>                   },
>                   "all_valid": false,
>                   "children": {
>                     "0": {
>                       "valid": true,
>                       "modified": true,
>                       "last": 7,
>                       "value": 5,
>                       "delta": 5
>                     },
>                     "1": {
>                       "valid": false,
>                       "modified": false,
>                       "last": "never",
>                       "value": null,
>                       "delta": null
>                     }
>                   },
>                   "peer": true
>                 },
>                 "right": {
>                   "valid": false,
>                   "modified": false,
>                   "last": "never",
>                   "value": null,
>                   "delta": null,
>                   "all_valid": false,
>                   "children": {
>                     "0": {
>                       "valid": false,
>                       "modified": false,
>                       "last": "never",
>                       "value": null,
>                       "delta": null
>                     },
>                     "1": {
>                       "valid": false,
>                       "modified": false,
>                       "last": "never",
>                       "value": null,
>                       "delta": null
>                     }
>                   },
>                   "peer": true
>                 }
>               },
>               "peer": true
>             }
>           },
>           "retired": {}
>         },
>         {
>           "a": {
>             "valid": true,
>             "modified": false,
>             "last": 7,
>             "value": {
>               "left": [
>                 5,
>                 null
>               ],
>               "right": null
>             },
>             "delta": null,
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": false,
>                 "last": 7,
>                 "value": [
>                   5,
>                   null
>                 ],
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": false,
>                     "last": 7,
>                     "value": 5,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": true
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": false
>               }
>             },
>             "peer": false
>           },
>           "b": {
>             "valid": true,
>             "modified": false,
>             "last": 0,
>             "value": {
>               "left": [
>                 10,
>                 null
>               ],
>               "right": null
>             },
>             "delta": null,
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": false,
>                 "last": 0,
>                 "value": [
>                   10,
>                   null
>                 ],
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": false,
>                     "last": 0,
>                     "value": 10,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": true
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": false
>               }
>             },
>             "peer": false
>           },
>           "keys": [
>             0
>           ],
>           "added": [],
>           "removed": [],
>           "rows": {
>             "0": {
>               "valid": true,
>               "modified": false,
>               "last": 7,
>               "value": {
>                 "left": [
>                   5,
>                   null
>                 ],
>                 "right": null
>               },
>               "delta": null,
>               "all_valid": false,
>               "children": {
>                 "left": {
>                   "valid": true,
>                   "modified": false,
>                   "last": 7,
>                   "value": [
>                     5,
>                     null
>                   ],
>                   "delta": null,
>                   "all_valid": false,
>                   "children": {
>                     "0": {
>                       "valid": true,
>                       "modified": false,
>                       "last": 7,
>                       "value": 5,
>                       "delta": null
>                     },
>                     "1": {
>                       "valid": false,
>                       "modified": false,
>                       "last": "never",
>                       "value": null,
>                       "delta": null
>                     }
>                   },
>                   "peer": true
>                 },
>                 "right": {
>                   "valid": false,
>                   "modified": false,
>                   "last": "never",
>                   "value": null,
>                   "delta": null,
>                   "all_valid": false,
>                   "children": {
>                     "0": {
>                       "valid": false,
>                       "modified": false,
>                       "last": "never",
>                       "value": null,
>                       "delta": null
>                     },
>                     "1": {
>                       "valid": false,
>                       "modified": false,
>                       "last": "never",
>                       "value": null,
>                       "delta": null
>                     }
>                   },
>                   "peer": true
>                 }
>               },
>               "peer": true
>             }
>           },
>           "retired": {}
>         },
>         {
>           "a": {
>             "valid": true,
>             "modified": false,
>             "last": 7,
>             "value": {
>               "left": [
>                 5,
>                 null
>               ],
>               "right": null
>             },
>             "delta": null,
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": false,
>                 "last": 7,
>                 "value": [
>                   5,
>                   null
>                 ],
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": false,
>                     "last": 7,
>                     "value": 5,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": true
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": false
>               }
>             },
>             "peer": false
>           },
>           "b": {
>             "valid": true,
>             "modified": false,
>             "last": 0,
>             "value": {
>               "left": [
>                 10,
>                 null
>               ],
>               "right": null
>             },
>             "delta": null,
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": false,
>                 "last": 0,
>                 "value": [
>                   10,
>                   null
>                 ],
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": false,
>                     "last": 0,
>                     "value": 10,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": true
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": false
>               }
>             },
>             "peer": false
>           },
>           "keys": [
>             0
>           ],
>           "added": [],
>           "removed": [],
>           "rows": {
>             "0": {
>               "valid": true,
>               "modified": true,
>               "last": 9,
>               "value": {
>                 "left": [
>                   -5,
>                   null
>                 ],
>                 "right": null
>               },
>               "delta": {
>                 "left": {
>                   "0": -5
>                 }
>               },
>               "all_valid": false,
>               "children": {
>                 "left": {
>                   "valid": true,
>                   "modified": true,
>                   "last": 9,
>                   "value": [
>                     -5,
>                     null
>                   ],
>                   "delta": {
>                     "0": -5
>                   },
>                   "all_valid": false,
>                   "children": {
>                     "0": {
>                       "valid": true,
>                       "modified": true,
>                       "last": 9,
>                       "value": -5,
>                       "delta": -5
>                     },
>                     "1": {
>                       "valid": false,
>                       "modified": false,
>                       "last": "never",
>                       "value": null,
>                       "delta": null
>                     }
>                   },
>                   "peer": true
>                 },
>                 "right": {
>                   "valid": false,
>                   "modified": false,
>                   "last": "never",
>                   "value": null,
>                   "delta": null,
>                   "all_valid": false,
>                   "children": {
>                     "0": {
>                       "valid": false,
>                       "modified": false,
>                       "last": "never",
>                       "value": null,
>                       "delta": null
>                     },
>                     "1": {
>                       "valid": false,
>                       "modified": false,
>                       "last": "never",
>                       "value": null,
>                       "delta": null
>                     }
>                   },
>                   "peer": true
>                 }
>               },
>               "peer": true
>             }
>           },
>           "retired": {}
>         },
>         {
>           "a": {
>             "valid": true,
>             "modified": false,
>             "last": 7,
>             "value": {
>               "left": [
>                 5,
>                 null
>               ],
>               "right": null
>             },
>             "delta": null,
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": false,
>                 "last": 7,
>                 "value": [
>                   5,
>                   null
>                 ],
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": false,
>                     "last": 7,
>                     "value": 5,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": true
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": false
>               }
>             },
>             "peer": false
>           },
>           "b": {
>             "valid": true,
>             "modified": false,
>             "last": 0,
>             "value": {
>               "left": [
>                 10,
>                 null
>               ],
>               "right": null
>             },
>             "delta": null,
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": false,
>                 "last": 0,
>                 "value": [
>                   10,
>                   null
>                 ],
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": false,
>                     "last": 0,
>                     "value": 10,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": true
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": false
>               }
>             },
>             "peer": false
>           },
>           "keys": [
>             0
>           ],
>           "added": [],
>           "removed": [],
>           "rows": {
>             "0": {
>               "valid": true,
>               "modified": false,
>               "last": 9,
>               "value": {
>                 "left": [
>                   -5,
>                   null
>                 ],
>                 "right": null
>               },
>               "delta": null,
>               "all_valid": false,
>               "children": {
>                 "left": {
>                   "valid": true,
>                   "modified": false,
>                   "last": 9,
>                   "value": [
>                     -5,
>                     null
>                   ],
>                   "delta": null,
>                   "all_valid": false,
>                   "children": {
>                     "0": {
>                       "valid": true,
>                       "modified": false,
>                       "last": 9,
>                       "value": -5,
>                       "delta": null
>                     },
>                     "1": {
>                       "valid": false,
>                       "modified": false,
>                       "last": "never",
>                       "value": null,
>                       "delta": null
>                     }
>                   },
>                   "peer": true
>                 },
>                 "right": {
>                   "valid": false,
>                   "modified": false,
>                   "last": "never",
>                   "value": null,
>                   "delta": null,
>                   "all_valid": false,
>                   "children": {
>                     "0": {
>                       "valid": false,
>                       "modified": false,
>                       "last": "never",
>                       "value": null,
>                       "delta": null
>                     },
>                     "1": {
>                       "valid": false,
>                       "modified": false,
>                       "last": "never",
>                       "value": null,
>                       "delta": null
>                     }
>                   },
>                   "peer": true
>                 }
>               },
>               "peer": true
>             }
>           },
>           "retired": {}
>         }
>       ],
>       "child_ticks": [
>         {
>           "time": 0,
>           "input": {
>             "valid": true,
>             "modified": true,
>             "last": 0,
>             "value": {
>               "left": [
>                 2,
>                 null
>               ],
>               "right": null
>             },
>             "delta": {
>               "left": {
>                 "0": 2
>               }
>             },
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": true,
>                 "last": 0,
>                 "value": [
>                   2,
>                   null
>                 ],
>                 "delta": {
>                   "0": 2
>                 },
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": true,
>                     "last": 0,
>                     "value": 2,
>                     "delta": 2
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": true
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": false
>               }
>             },
>             "peer": false
>           },
>           "output": {
>             "valid": true,
>             "modified": true,
>             "last": 0,
>             "value": {
>               "left": [
>                 2,
>                 null
>               ],
>               "right": null
>             },
>             "delta": {
>               "left": {
>                 "0": 2
>               }
>             },
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": true,
>                 "last": 0,
>                 "value": [
>                   2,
>                   null
>                 ],
>                 "delta": {
>                   "0": 2
>                 },
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": true,
>                     "last": 0,
>                     "value": 2,
>                     "delta": 2
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 }
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 }
>               }
>             }
>           }
>         },
>         {
>           "time": 1,
>           "input": {
>             "valid": true,
>             "modified": true,
>             "last": 1,
>             "value": {
>               "left": [
>                 3,
>                 null
>               ],
>               "right": null
>             },
>             "delta": {
>               "left": {
>                 "0": 3
>               }
>             },
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": true,
>                 "last": 1,
>                 "value": [
>                   3,
>                   null
>                 ],
>                 "delta": {
>                   "0": 3
>                 },
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": true,
>                     "last": 1,
>                     "value": 3,
>                     "delta": 3
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": true
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": false
>               }
>             },
>             "peer": false
>           },
>           "output": {
>             "valid": true,
>             "modified": true,
>             "last": 1,
>             "value": {
>               "left": [
>                 5,
>                 null
>               ],
>               "right": null
>             },
>             "delta": {
>               "left": {
>                 "0": 5
>               }
>             },
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": true,
>                 "last": 1,
>                 "value": [
>                   5,
>                   null
>                 ],
>                 "delta": {
>                   "0": 5
>                 },
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": true,
>                     "last": 1,
>                     "value": 5,
>                     "delta": 5
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 }
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 }
>               }
>             }
>           }
>         },
>         {
>           "time": 2,
>           "input": {
>             "valid": true,
>             "modified": true,
>             "last": 2,
>             "value": {
>               "left": [
>                 10,
>                 null
>               ],
>               "right": null
>             },
>             "delta": {
>               "left": {
>                 "0": 10
>               }
>             },
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": true,
>                 "last": 2,
>                 "value": [
>                   10,
>                   null
>                 ],
>                 "delta": {
>                   "0": 10
>                 },
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": true,
>                     "last": 2,
>                     "value": 10,
>                     "delta": 10
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": true
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": false
>               }
>             },
>             "peer": false
>           },
>           "output": {
>             "valid": true,
>             "modified": true,
>             "last": 2,
>             "value": {
>               "left": [
>                 15,
>                 null
>               ],
>               "right": null
>             },
>             "delta": {
>               "left": {
>                 "0": 15
>               }
>             },
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": true,
>                 "last": 2,
>                 "value": [
>                   15,
>                   null
>                 ],
>                 "delta": {
>                   "0": 15
>                 },
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": true,
>                     "last": 2,
>                     "value": 15,
>                     "delta": 15
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 }
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 }
>               }
>             }
>           }
>         },
>         {
>           "time": 4,
>           "input": {
>             "valid": true,
>             "modified": false,
>             "last": 2,
>             "value": {
>               "left": [
>                 10,
>                 null
>               ],
>               "right": null
>             },
>             "delta": null,
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": false,
>                 "last": 2,
>                 "value": [
>                   10,
>                   null
>                 ],
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": false,
>                     "last": 2,
>                     "value": 10,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": true
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": false
>               }
>             },
>             "peer": false
>           },
>           "output": {
>             "valid": true,
>             "modified": true,
>             "last": 4,
>             "value": {
>               "left": [
>                 -15,
>                 null
>               ],
>               "right": null
>             },
>             "delta": {
>               "left": {
>                 "0": -15
>               }
>             },
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": true,
>                 "last": 4,
>                 "value": [
>                   -15,
>                   null
>                 ],
>                 "delta": {
>                   "0": -15
>                 },
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": true,
>                     "last": 4,
>                     "value": -15,
>                     "delta": -15
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 }
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 }
>               }
>             }
>           }
>         },
>         {
>           "time": 7,
>           "input": {
>             "valid": true,
>             "modified": true,
>             "last": 7,
>             "value": {
>               "left": [
>                 5,
>                 null
>               ],
>               "right": null
>             },
>             "delta": {
>               "left": {
>                 "0": 5
>               }
>             },
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": true,
>                 "last": 7,
>                 "value": [
>                   5,
>                   null
>                 ],
>                 "delta": {
>                   "0": 5
>                 },
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": true,
>                     "last": 7,
>                     "value": 5,
>                     "delta": 5
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": true
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": false
>               }
>             },
>             "peer": false
>           },
>           "output": {
>             "valid": true,
>             "modified": true,
>             "last": 7,
>             "value": {
>               "left": [
>                 5,
>                 null
>               ],
>               "right": null
>             },
>             "delta": {
>               "left": {
>                 "0": 5
>               }
>             },
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": true,
>                 "last": 7,
>                 "value": [
>                   5,
>                   null
>                 ],
>                 "delta": {
>                   "0": 5
>                 },
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": true,
>                     "last": 7,
>                     "value": 5,
>                     "delta": 5
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 }
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 }
>               }
>             }
>           }
>         },
>         {
>           "time": 9,
>           "input": {
>             "valid": true,
>             "modified": false,
>             "last": 7,
>             "value": {
>               "left": [
>                 5,
>                 null
>               ],
>               "right": null
>             },
>             "delta": null,
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": false,
>                 "last": 7,
>                 "value": [
>                   5,
>                   null
>                 ],
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": false,
>                     "last": 7,
>                     "value": 5,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": true
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 },
>                 "peer": false
>               }
>             },
>             "peer": false
>           },
>           "output": {
>             "valid": true,
>             "modified": true,
>             "last": 9,
>             "value": {
>               "left": [
>                 -5,
>                 null
>               ],
>               "right": null
>             },
>             "delta": {
>               "left": {
>                 "0": -5
>               }
>             },
>             "all_valid": false,
>             "children": {
>               "left": {
>                 "valid": true,
>                 "modified": true,
>                 "last": 9,
>                 "value": [
>                   -5,
>                   null
>                 ],
>                 "delta": {
>                   "0": -5
>                 },
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": true,
>                     "modified": true,
>                     "last": 9,
>                     "value": -5,
>                     "delta": -5
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 }
>               },
>               "right": {
>                 "valid": false,
>                 "modified": false,
>                 "last": "never",
>                 "value": null,
>                 "delta": null,
>                 "all_valid": false,
>                 "children": {
>                   "0": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   },
>                   "1": {
>                     "valid": false,
>                     "modified": false,
>                     "last": "never",
>                     "value": null,
>                     "delta": null
>                   }
>                 }
>               }
>             }
>           }
>         }
>       ],
>       "events": [
>         "start",
>         "stop",
>         "start",
>         "stop"
>       ]
>     }
>   }
> }

## runtime/validation/descriptions/corrections.json

### Excerpt 1

[Source, line 1](https://github.com/hhenson/hgraph_spec/blob/b295f39c94403dc4093a1d8c009cdcc6f2549a24/runtime/validation/descriptions/corrections.json#L1).

> [
>   {
>     "case": "owned",
>     "path": "/ticks/5/retired/0/peer",
>     "previous": true,
>     "expected": false,
>     "reason": "A removed input is detached. Retained data does not imply a current peer; both root observations and Python child observations confirm detachment."
>   },
>   {
>     "case": "owned",
>     "path": "/ticks/5/retired/0/children/left/peer",
>     "previous": true,
>     "expected": false,
>     "reason": "A removed input is detached. Retained data does not imply a current peer; both root observations and Python child observations confirm detachment."
>   },
>   {
>     "case": "owned",
>     "path": "/ticks/5/retired/0/children/right/peer",
>     "previous": true,
>     "expected": false,
>     "reason": "A removed input is detached. Retained data does not imply a current peer; both root observations and Python child observations confirm detachment."
>   },
>   {
>     "case": "assembled",
>     "path": "/ticks/5/retired/0/peer",
>     "previous": true,
>     "expected": false,
>     "reason": "A removed input is detached. Retained data does not imply a current peer; both root observations and Python child observations confirm detachment."
>   },
>   {
>     "case": "assembled",
>     "path": "/ticks/5/retired/0/children/left/peer",
>     "previous": true,
>     "expected": false,
>     "reason": "A removed input is detached. Retained data does not imply a current peer; both root observations and Python child observations confirm detachment."
>   },
>   {
>     "case": "assembled",
>     "path": "/ticks/5/retired/0/children/right/peer",
>     "previous": true,
>     "expected": false,
>     "reason": "A removed input is detached. Retained data does not imply a current peer; both root observations and Python child observations confirm detachment."
>   },
>   {
>     "case": "mixed",
>     "path": "/ticks/5/retired/0/peer",
>     "previous": true,
>     "expected": false,
>     "reason": "A removed input is detached. Retained data does not imply a current peer; both root observations and Python child observations confirm detachment."
>   },
>   {
>     "case": "mixed",
>     "path": "/ticks/5/retired/0/children/left/peer",
>     "previous": true,
>     "expected": false,
>     "reason": "A removed input is detached. Retained data does not imply a current peer; both root observations and Python child observations confirm detachment."
>   },
>   {
>     "case": "mixed",
>     "path": "/ticks/5/retired/0/children/right/peer",
>     "previous": true,
>     "expected": false,
>     "reason": "A removed input is detached. Retained data does not imply a current peer; both root observations and Python child observations confirm detachment."
>   },
>   {
>     "case": "owned_capture",
>     "path": "/ticks/5/retired/0/peer",
>     "previous": true,
>     "expected": false,
>     "reason": "A removed input is detached. Retained data does not imply a current peer; both root observations and Python child observations confirm detachment."
>   },
>   {
>     "case": "owned_capture",
>     "path": "/ticks/5/retired/0/children/left/peer",
>     "previous": true,
>     "expected": false,
>     "reason": "A removed input is detached. Retained data does not imply a current peer; both root observations and Python child observations confirm detachment."
>   },
>   {
>     "case": "owned_capture",
>     "path": "/ticks/5/retired/0/children/right/peer",
>     "previous": true,
>     "expected": false,
>     "reason": "A removed input is detached. Retained data does not imply a current peer; both root observations and Python child observations confirm detachment."
>   },
>   {
>     "case": "mixed_capture",
>     "path": "/ticks/5/retired/0/peer",
>     "previous": true,
>     "expected": false,
>     "reason": "A removed input is detached. Retained data does not imply a current peer; both root observations and Python child observations confirm detachment."
>   },
>   {
>     "case": "mixed_capture",
>     "path": "/ticks/5/retired/0/children/left/peer",
>     "previous": true,
>     "expected": false,
>     "reason": "A removed input is detached. Retained data does not imply a current peer; both root observations and Python child observations confirm detachment."
>   },
>   {
>     "case": "mixed_capture",
>     "path": "/ticks/5/retired/0/children/right/peer",
>     "previous": true,
>     "expected": false,
>     "reason": "A removed input is detached. Retained data does not imply a current peer; both root observations and Python child observations confirm detachment."
>   }
> ]

## runtime/validation/parity/reasoned.json

### Excerpt 1

[Source, line 847](https://github.com/hhenson/hgraph_spec/blob/b295f39c94403dc4093a1d8c009cdcc6f2549a24/runtime/validation/parity/reasoned.json#L847).

>   "1062": {
>    "derivation": "str_ of a tuple is Python's str: each string element in Python's repr, escaping what str.isprintable rejects.",
>    "expected": [
>     "('\\x87', '\\x0b\\U0008ca7d')"
>    ],
>    "family": "python-repr-escaping",
>    "mode": "trace",
>    "rules": [
>     "OP-9"
>    ]
>   },

### Excerpt 2

[Source, line 1498](https://github.com/hhenson/hgraph_spec/blob/b295f39c94403dc4093a1d8c009cdcc6f2549a24/runtime/validation/parity/reasoned.json#L1498).

>   "960": {
>    "derivation": "str_ of a tuple is Python's str: each string element in Python's repr, escaping what str.isprintable rejects.",
>    "expected": [
>     "('\u00c1\\U00063bba\u00de\u00c6',)"
>    ],
>    "family": "python-repr-escaping",
>    "mode": "trace",
>    "rules": [
>     "OP-9"
>    ]
>   },

### Excerpt 3

[Source, line 1898](https://github.com/hhenson/hgraph_spec/blob/b295f39c94403dc4093a1d8c009cdcc6f2549a24/runtime/validation/parity/reasoned.json#L1898).

>  "note": "Expectations derived from operators.md and the core chapters. The parity issues had already been observed; each derivation was written from the rules and then scored unchanged. Mismatches with both runtimes were not fitted away (open_point)."

### Excerpt 4

[Source, line 3](https://github.com/hhenson/hgraph_spec/blob/b295f39c94403dc4093a1d8c009cdcc6f2549a24/runtime/validation/parity/reasoned.json#L3).

> "1002": {
>    "derivation": "tsd_set_model.py: members by OP-5, admission by OP-6, children forwarded (OP-4) from the operand OP-5 names; the first admitted evaluation publishes (validity), later empty deltas do not.",
>    "expected": [
>     null,
>     null,
>     {
>      "$map": [
>       [
>        "a",
>        -19
>       ]
>      ]
>     },
>     {
>      "$map": [
>       [
>        "a",
>        -19
>       ]
>      ]
>     }
>    ],
>    "family": "tsd-set-operators",
>    "mode": "trace",
>    "rules": [
>     "OP-4",
>     "OP-5",
>     "OP-6",
>     "OP-7"
>    ]
>   }

### Excerpt 5

[Source, line 34](https://github.com/hhenson/hgraph_spec/blob/b295f39c94403dc4093a1d8c009cdcc6f2549a24/runtime/validation/parity/reasoned.json#L34).

> "1003": {
>    "derivation": "tsd_set_model.py: members by OP-5, admission by OP-6, children forwarded (OP-4) from the operand OP-5 names; the first admitted evaluation publishes (validity), later empty deltas do not.",
>    "expected": null,
>    "family": "tsd-set-operators",
>    "mode": "trace",
>    "rules": [
>     "OP-4",
>     "OP-5",
>     "OP-6",
>     "OP-7"
>    ]
>   }

### Excerpt 6

[Source, line 46](https://github.com/hhenson/hgraph_spec/blob/b295f39c94403dc4093a1d8c009cdcc6f2549a24/runtime/validation/parity/reasoned.json#L46).

> "1004": {
>    "derivation": "tsd_set_model.py: members by OP-5, admission by OP-6, children forwarded (OP-4) from the operand OP-5 names; the first admitted evaluation publishes (validity), later empty deltas do not.",
>    "expected": [
>     {
>      "$map": []
>     },
>     {
>      "$map": [
>       [
>        "a",
>        -18
>       ],
>       [
>        "c",
>        -19
>       ]
>      ]
>     },
>     {
>      "$map": [
>       [
>        "c",
>        -19
>       ]
>      ]
>     }
>    ],
>    "family": "tsd-set-operators",
>    "mode": "trace",
>    "rules": [
>     "OP-4",
>     "OP-5",
>     "OP-6",
>     "OP-7"
>    ],
>    "ruling": "first-empty-set-result"
>   }

### Excerpt 7

[Source, line 83](https://github.com/hhenson/hgraph_spec/blob/b295f39c94403dc4093a1d8c009cdcc6f2549a24/runtime/validation/parity/reasoned.json#L83).

> "1005": {
>    "derivation": "tsd_set_model.py: members by OP-5, admission by OP-6, children forwarded (OP-4) from the operand OP-5 names; the first admitted evaluation publishes (validity), later empty deltas do not.",
>    "expected": null,
>    "family": "tsd-set-operators",
>    "mode": "trace",
>    "rules": [
>     "OP-4",
>     "OP-5",
>     "OP-6",
>     "OP-7"
>    ]
>   }

### Excerpt 8

[Source, line 95](https://github.com/hhenson/hgraph_spec/blob/b295f39c94403dc4093a1d8c009cdcc6f2549a24/runtime/validation/parity/reasoned.json#L95).

> "1006": {
>    "derivation": "tsd_set_model.py: members by OP-5, admission by OP-6, children forwarded (OP-4) from the operand OP-5 names; the first admitted evaluation publishes (validity), later empty deltas do not.",
>    "expected": null,
>    "family": "tsd-set-operators",
>    "mode": "trace",
>    "rules": [
>     "OP-4",
>     "OP-5",
>     "OP-6",
>     "OP-7"
>    ]
>   }

### Excerpt 9

[Source, line 107](https://github.com/hhenson/hgraph_spec/blob/b295f39c94403dc4093a1d8c009cdcc6f2549a24/runtime/validation/parity/reasoned.json#L107).

> "1007": {
>    "derivation": "tsd_set_model.py: members by OP-5, admission by OP-6, children forwarded (OP-4) from the operand OP-5 names; the first admitted evaluation publishes (validity), later empty deltas do not.",
>    "expected": [
>     {
>      "$map": [
>       [
>        "a",
>        -19
>       ]
>      ]
>     },
>     {
>      "$map": [
>       [
>        "a",
>        -19
>       ]
>      ]
>     }
>    ],
>    "family": "tsd-set-operators",
>    "mode": "trace",
>    "rules": [
>     "OP-4",
>     "OP-5",
>     "OP-6",
>     "OP-7"
>    ]
>   }

### Excerpt 10

[Source, line 136](https://github.com/hhenson/hgraph_spec/blob/b295f39c94403dc4093a1d8c009cdcc6f2549a24/runtime/validation/parity/reasoned.json#L136).

> "1008": {
>    "derivation": "tsd_set_model.py: members by OP-5, admission by OP-6, children forwarded (OP-4) from the operand OP-5 names; the first admitted evaluation publishes (validity), later empty deltas do not.",
>    "expected": [
>     {
>      "$map": []
>     },
>     null,
>     {
>      "$map": [
>       [
>        "a",
>        -19
>       ]
>      ]
>     },
>     {
>      "$map": [
>       [
>        "a",
>        -19
>       ]
>      ]
>     }
>    ],
>    "family": "tsd-set-operators",
>    "mode": "trace",
>    "rules": [
>     "OP-4",
>     "OP-5",
>     "OP-6",
>     "OP-7"
>    ],
>    "ruling": "first-empty-set-result"
>   }

### Excerpt 11

[Source, line 170](https://github.com/hhenson/hgraph_spec/blob/b295f39c94403dc4093a1d8c009cdcc6f2549a24/runtime/validation/parity/reasoned.json#L170).

> "1009": {
>    "derivation": "tsd_set_model.py: members by OP-5, admission by OP-6, children forwarded (OP-4) from the operand OP-5 names; the first admitted evaluation publishes (validity), later empty deltas do not.",
>    "expected": null,
>    "family": "tsd-set-operators",
>    "mode": "trace",
>    "rules": [
>     "OP-4",
>     "OP-5",
>     "OP-6",
>     "OP-7"
>    ]
>   }

### Excerpt 12

[Source, line 182](https://github.com/hhenson/hgraph_spec/blob/b295f39c94403dc4093a1d8c009cdcc6f2549a24/runtime/validation/parity/reasoned.json#L182).

> "1010": {
>    "derivation": "tsd_set_model.py: members by OP-5, admission by OP-6, children forwarded (OP-4) from the operand OP-5 names; the first admitted evaluation publishes (validity), later empty deltas do not.",
>    "expected": [
>     {
>      "$map": [
>       [
>        "a",
>        -5
>       ]
>      ]
>     },
>     {
>      "$map": [
>       [
>        "a",
>        -5
>       ]
>      ]
>     }
>    ],
>    "family": "tsd-set-operators",
>    "mode": "trace",
>    "rules": [
>     "OP-4",
>     "OP-5",
>     "OP-6",
>     "OP-7"
>    ]
>   }

### Excerpt 13

[Source, line 211](https://github.com/hhenson/hgraph_spec/blob/b295f39c94403dc4093a1d8c009cdcc6f2549a24/runtime/validation/parity/reasoned.json#L211).

> "1028": {
>    "derivation": "tsd_set_model.py: members by OP-5, admission by OP-6, children forwarded (OP-4) from the operand OP-5 names; the first admitted evaluation publishes (validity), later empty deltas do not.",
>    "expected": [
>     null,
>     {
>      "$map": [
>       [
>        "b",
>        -19
>       ],
>       [
>        "c",
>        -19
>       ]
>      ]
>     },
>     {
>      "$map": [
>       [
>        "b",
>        -17
>       ]
>      ]
>     },
>     null,
>     null
>    ],
>    "family": "tsd-set-operators",
>    "mode": "trace",
>    "rules": [
>     "OP-4",
>     "OP-5",
>     "OP-6",
>     "OP-7"
>    ]
>   }

### Excerpt 14

[Source, line 247](https://github.com/hhenson/hgraph_spec/blob/b295f39c94403dc4093a1d8c009cdcc6f2549a24/runtime/validation/parity/reasoned.json#L247).

> "1029": {
>    "derivation": "tsd_set_model.py: members by OP-5, admission by OP-6, children forwarded (OP-4) from the operand OP-5 names; the first admitted evaluation publishes (validity), later empty deltas do not.",
>    "expected": null,
>    "family": "tsd-set-operators",
>    "mode": "trace",
>    "rules": [
>     "OP-4",
>     "OP-5",
>     "OP-6",
>     "OP-7"
>    ]
>   }

### Excerpt 15

[Source, line 259](https://github.com/hhenson/hgraph_spec/blob/b295f39c94403dc4093a1d8c009cdcc6f2549a24/runtime/validation/parity/reasoned.json#L259).

> "1030": {
>    "derivation": "tsd_set_model.py: members by OP-5, admission by OP-6, children forwarded (OP-4) from the operand OP-5 names; the first admitted evaluation publishes (validity), later empty deltas do not.",
>    "expected": [
>     {
>      "$map": [
>       [
>        "a",
>        2
>       ]
>      ]
>     },
>     null,
>     {
>      "$map": [
>       [
>        "a",
>        2
>       ]
>      ]
>     }
>    ],
>    "family": "tsd-set-operators",
>    "mode": "trace",
>    "rules": [
>     "OP-4",
>     "OP-5",
>     "OP-6",
>     "OP-7"
>    ]
>   }

### Excerpt 16

[Source, line 289](https://github.com/hhenson/hgraph_spec/blob/b295f39c94403dc4093a1d8c009cdcc6f2549a24/runtime/validation/parity/reasoned.json#L289).

> "1031": {
>    "derivation": "tsd_set_model.py: members by OP-5, admission by OP-6, children forwarded (OP-4) from the operand OP-5 names; the first admitted evaluation publishes (validity), later empty deltas do not.",
>    "expected": [
>     {
>      "$map": [
>       [
>        "a",
>        -7
>       ],
>       [
>        "c",
>        2
>       ]
>      ]
>     },
>     {
>      "$map": [
>       [
>        "a",
>        -19
>       ]
>      ]
>     },
>     {
>      "$map": [
>       [
>        "a",
>        -19
>       ]
>      ]
>     }
>    ],
>    "family": "tsd-set-operators",
>    "mode": "trace",
>    "rules": [
>     "OP-4",
>     "OP-5",
>     "OP-6",
>     "OP-7"
>    ]
>   }

### Excerpt 17

[Source, line 330](https://github.com/hhenson/hgraph_spec/blob/b295f39c94403dc4093a1d8c009cdcc6f2549a24/runtime/validation/parity/reasoned.json#L330).

> "1032": {
>    "derivation": "tsd_set_model.py: members by OP-5, admission by OP-6, children forwarded (OP-4) from the operand OP-5 names; the first admitted evaluation publishes (validity), later empty deltas do not.",
>    "expected": [
>     {
>      "$map": [
>       [
>        "b",
>        -19
>       ]
>      ]
>     },
>     null,
>     {
>      "$map": [
>       [
>        "b",
>        -19
>       ]
>      ]
>     }
>    ],
>    "family": "tsd-set-operators",
>    "mode": "trace",
>    "rules": [
>     "OP-4",
>     "OP-5",
>     "OP-6",
>     "OP-7"
>    ]
>   }

### Excerpt 18

[Source, line 360](https://github.com/hhenson/hgraph_spec/blob/b295f39c94403dc4093a1d8c009cdcc6f2549a24/runtime/validation/parity/reasoned.json#L360).

> "1033": {
>    "derivation": "tsd_set_model.py: members by OP-5, admission by OP-6, children forwarded (OP-4) from the operand OP-5 names; the first admitted evaluation publishes (validity), later empty deltas do not.",
>    "expected": [
>     {
>      "$map": [
>       [
>        "a",
>        -19
>       ]
>      ]
>     },
>     null,
>     {
>      "$map": [
>       [
>        "a",
>        -19
>       ]
>      ]
>     },
>     null
>    ],
>    "family": "tsd-set-operators",
>    "mode": "trace",
>    "rules": [
>     "OP-4",
>     "OP-5",
>     "OP-6",
>     "OP-7"
>    ]
>   }

### Excerpt 19

[Source, line 391](https://github.com/hhenson/hgraph_spec/blob/b295f39c94403dc4093a1d8c009cdcc6f2549a24/runtime/validation/parity/reasoned.json#L391).

> "1034": {
>    "derivation": "tsd_set_model.py: members by OP-5, admission by OP-6, children forwarded (OP-4) from the operand OP-5 names; the first admitted evaluation publishes (validity), later empty deltas do not.",
>    "expected": [
>     {
>      "$map": [
>       [
>        "a",
>        -19
>       ]
>      ]
>     },
>     {
>      "$map": [
>       [
>        "a",
>        -19
>       ]
>      ]
>     }
>    ],
>    "family": "tsd-set-operators",
>    "mode": "trace",
>    "rules": [
>     "OP-4",
>     "OP-5",
>     "OP-6",
>     "OP-7"
>    ]
>   }

### Excerpt 20

[Source, line 420](https://github.com/hhenson/hgraph_spec/blob/b295f39c94403dc4093a1d8c009cdcc6f2549a24/runtime/validation/parity/reasoned.json#L420).

> "1035": {
>    "derivation": "tsd_set_model.py: members by OP-5, admission by OP-6, children forwarded (OP-4) from the operand OP-5 names; the first admitted evaluation publishes (validity), later empty deltas do not.",
>    "expected": null,
>    "family": "tsd-set-operators",
>    "mode": "trace",
>    "rules": [
>     "OP-4",
>     "OP-5",
>     "OP-6",
>     "OP-7"
>    ]
>   }

### Excerpt 21

[Source, line 432](https://github.com/hhenson/hgraph_spec/blob/b295f39c94403dc4093a1d8c009cdcc6f2549a24/runtime/validation/parity/reasoned.json#L432).

> "1036": {
>    "derivation": "tsd_set_model.py: members by OP-5, admission by OP-6, children forwarded (OP-4) from the operand OP-5 names; the first admitted evaluation publishes (validity), later empty deltas do not.",
>    "expected": [
>     {
>      "$map": [
>       [
>        "a",
>        -19
>       ]
>      ]
>     },
>     {
>      "$map": [
>       [
>        "a",
>        -19
>       ]
>      ]
>     }
>    ],
>    "family": "tsd-set-operators",
>    "mode": "trace",
>    "rules": [
>     "OP-4",
>     "OP-5",
>     "OP-6",
>     "OP-7"
>    ]
>   }

### Excerpt 22

[Source, line 461](https://github.com/hhenson/hgraph_spec/blob/b295f39c94403dc4093a1d8c009cdcc6f2549a24/runtime/validation/parity/reasoned.json#L461).

> "1037": {
>    "derivation": "tsd_set_model.py: members by OP-5, admission by OP-6, children forwarded (OP-4) from the operand OP-5 names; the first admitted evaluation publishes (validity), later empty deltas do not.",
>    "expected": null,
>    "family": "tsd-set-operators",
>    "mode": "trace",
>    "rules": [
>     "OP-4",
>     "OP-5",
>     "OP-6",
>     "OP-7"
>    ]
>   }

### Excerpt 23

[Source, line 473](https://github.com/hhenson/hgraph_spec/blob/b295f39c94403dc4093a1d8c009cdcc6f2549a24/runtime/validation/parity/reasoned.json#L473).

> "1038": {
>    "derivation": "tsd_set_model.py: members by OP-5, admission by OP-6, children forwarded (OP-4) from the operand OP-5 names; the first admitted evaluation publishes (validity), later empty deltas do not.",
>    "expected": [
>     {
>      "$map": [
>       [
>        "a",
>        -19
>       ]
>      ]
>     },
>     {
>      "$map": [
>       [
>        "a",
>        -19
>       ]
>      ]
>     }
>    ],
>    "family": "tsd-set-operators",
>    "mode": "trace",
>    "rules": [
>     "OP-4",
>     "OP-5",
>     "OP-6",
>     "OP-7"
>    ]
>   }

### Excerpt 24

[Source, line 502](https://github.com/hhenson/hgraph_spec/blob/b295f39c94403dc4093a1d8c009cdcc6f2549a24/runtime/validation/parity/reasoned.json#L502).

> "1039": {
>    "derivation": "tsd_set_model.py: members by OP-5, admission by OP-6, children forwarded (OP-4) from the operand OP-5 names; the first admitted evaluation publishes (validity), later empty deltas do not.",
>    "expected": null,
>    "family": "tsd-set-operators",
>    "mode": "trace",
>    "rules": [
>     "OP-4",
>     "OP-5",
>     "OP-6",
>     "OP-7"
>    ]
>   }

### Excerpt 25

[Source, line 514](https://github.com/hhenson/hgraph_spec/blob/b295f39c94403dc4093a1d8c009cdcc6f2549a24/runtime/validation/parity/reasoned.json#L514).

> "1040": {
>    "derivation": "tsd_set_model.py: members by OP-5, admission by OP-6, children forwarded (OP-4) from the operand OP-5 names; the first admitted evaluation publishes (validity), later empty deltas do not.",
>    "expected": [
>     {
>      "$map": [
>       [
>        "a",
>        -19
>       ],
>       [
>        "b",
>        -13
>       ]
>      ]
>     },
>     {
>      "$map": [
>       [
>        "b",
>        {
>         "$remove": true
>        }
>       ]
>      ]
>     },
>     {
>      "$map": [
>       [
>        "a",
>        {
>         "$remove": true
>        }
>       ]
>      ]
>     },
>     {
>      "$map": [
>       [
>        "a",
>        -19
>       ]
>      ]
>     },
>     {
>      "$map": [
>       [
>        "a",
>        -19
>       ]
>      ]
>     }
>    ],
>    "family": "tsd-set-operators",
>    "mode": "trace",
>    "rules": [
>     "OP-4",
>     "OP-5",
>     "OP-6",
>     "OP-7"
>    ]
>   }

### Excerpt 26

[Source, line 575](https://github.com/hhenson/hgraph_spec/blob/b295f39c94403dc4093a1d8c009cdcc6f2549a24/runtime/validation/parity/reasoned.json#L575).

> "1041": {
>    "derivation": "tsd_set_model.py: members by OP-5, admission by OP-6, children forwarded (OP-4) from the operand OP-5 names; the first admitted evaluation publishes (validity), later empty deltas do not.",
>    "expected": [
>     {
>      "$map": [
>       [
>        "b",
>        10
>       ]
>      ]
>     },
>     null,
>     {
>      "$map": [
>       [
>        "b",
>        10
>       ]
>      ]
>     }
>    ],
>    "family": "tsd-set-operators",
>    "mode": "trace",
>    "rules": [
>     "OP-4",
>     "OP-5",
>     "OP-6",
>     "OP-7"
>    ]
>   }

### Excerpt 27

[Source, line 605](https://github.com/hhenson/hgraph_spec/blob/b295f39c94403dc4093a1d8c009cdcc6f2549a24/runtime/validation/parity/reasoned.json#L605).

> "1042": {
>    "derivation": "tsd_set_model.py: members by OP-5, admission by OP-6, children forwarded (OP-4) from the operand OP-5 names; the first admitted evaluation publishes (validity), later empty deltas do not.",
>    "expected": [
>     null,
>     null,
>     {
>      "$map": [
>       [
>        "b",
>        6
>       ]
>      ]
>     },
>     {
>      "$map": [
>       [
>        "a",
>        -19
>       ]
>      ]
>     },
>     {
>      "$map": [
>       [
>        "a",
>        -19
>       ]
>      ]
>     }
>    ],
>    "family": "tsd-set-operators",
>    "mode": "trace",
>    "rules": [
>     "OP-4",
>     "OP-5",
>     "OP-6",
>     "OP-7"
>    ]
>   }

### Excerpt 28

[Source, line 644](https://github.com/hhenson/hgraph_spec/blob/b295f39c94403dc4093a1d8c009cdcc6f2549a24/runtime/validation/parity/reasoned.json#L644).

> "1043": {
>    "derivation": "tsd_set_model.py: members by OP-5, admission by OP-6, children forwarded (OP-4) from the operand OP-5 names; the first admitted evaluation publishes (validity), later empty deltas do not.",
>    "expected": [
>     {
>      "$map": [
>       [
>        "b",
>        -10
>       ],
>       [
>        "c",
>        -19
>       ]
>      ]
>     },
>     {
>      "$map": [
>       [
>        "c",
>        -19
>       ]
>      ]
>     }
>    ],
>    "family": "tsd-set-operators",
>    "mode": "trace",
>    "rules": [
>     "OP-4",
>     "OP-5",
>     "OP-6",
>     "OP-7"
>    ]
>   }

### Excerpt 29

[Source, line 677](https://github.com/hhenson/hgraph_spec/blob/b295f39c94403dc4093a1d8c009cdcc6f2549a24/runtime/validation/parity/reasoned.json#L677).

> "1044": {
>    "derivation": "tsd_set_model.py: members by OP-5, admission by OP-6, children forwarded (OP-4) from the operand OP-5 names; the first admitted evaluation publishes (validity), later empty deltas do not.",
>    "expected": [
>     {
>      "$map": [
>       [
>        "a",
>        -19
>       ]
>      ]
>     },
>     null,
>     null,
>     null,
>     {
>      "$map": [
>       [
>        "a",
>        -19
>       ]
>      ]
>     },
>     null
>    ],
>    "family": "tsd-set-operators",
>    "mode": "trace",
>    "rules": [
>     "OP-4",
>     "OP-5",
>     "OP-6",
>     "OP-7"
>    ]
>   }

### Excerpt 30

[Source, line 710](https://github.com/hhenson/hgraph_spec/blob/b295f39c94403dc4093a1d8c009cdcc6f2549a24/runtime/validation/parity/reasoned.json#L710).

> "1045": {
>    "derivation": "tsd_set_model.py: members by OP-5, admission by OP-6, children forwarded (OP-4) from the operand OP-5 names; the first admitted evaluation publishes (validity), later empty deltas do not.",
>    "expected": [
>     null,
>     {
>      "$map": [
>       [
>        "a",
>        -19
>       ]
>      ]
>     },
>     {
>      "$map": [
>       [
>        "a",
>        -11
>       ],
>       [
>        "c",
>        -20
>       ]
>      ]
>     },
>     {
>      "$map": [
>       [
>        "a",
>        -17
>       ]
>      ]
>     },
>     null
>    ],
>    "family": "tsd-set-operators",
>    "mode": "trace",
>    "rules": [
>     "OP-4",
>     "OP-5",
>     "OP-6",
>     "OP-7"
>    ]
>   }

### Excerpt 31

[Source, line 753](https://github.com/hhenson/hgraph_spec/blob/b295f39c94403dc4093a1d8c009cdcc6f2549a24/runtime/validation/parity/reasoned.json#L753).

> "1046": {
>    "derivation": "tsd_set_model.py: members by OP-5, admission by OP-6, children forwarded (OP-4) from the operand OP-5 names; the first admitted evaluation publishes (validity), later empty deltas do not.",
>    "expected": null,
>    "family": "tsd-set-operators",
>    "mode": "trace",
>    "rules": [
>     "OP-4",
>     "OP-5",
>     "OP-6",
>     "OP-7"
>    ]
>   }

### Excerpt 32

[Source, line 765](https://github.com/hhenson/hgraph_spec/blob/b295f39c94403dc4093a1d8c009cdcc6f2549a24/runtime/validation/parity/reasoned.json#L765).

> "1047": {
>    "derivation": "tsd_set_model.py: members by OP-5, admission by OP-6, children forwarded (OP-4) from the operand OP-5 names; the first admitted evaluation publishes (validity), later empty deltas do not.",
>    "expected": null,
>    "family": "tsd-set-operators",
>    "mode": "trace",
>    "rules": [
>     "OP-4",
>     "OP-5",
>     "OP-6",
>     "OP-7"
>    ]
>   }

### Excerpt 33

[Source, line 777](https://github.com/hhenson/hgraph_spec/blob/b295f39c94403dc4093a1d8c009cdcc6f2549a24/runtime/validation/parity/reasoned.json#L777).

> "1048": {
>    "derivation": "tsd_set_model.py: members by OP-5, admission by OP-6, children forwarded (OP-4) from the operand OP-5 names; the first admitted evaluation publishes (validity), later empty deltas do not.",
>    "expected": [
>     {
>      "$map": [
>       [
>        "c",
>        -11
>       ]
>      ]
>     },
>     {
>      "$map": [
>       [
>        "c",
>        -11
>       ]
>      ]
>     }
>    ],
>    "family": "tsd-set-operators",
>    "mode": "trace",
>    "rules": [
>     "OP-4",
>     "OP-5",
>     "OP-6",
>     "OP-7"
>    ]
>   }

### Excerpt 34

[Source, line 806](https://github.com/hhenson/hgraph_spec/blob/b295f39c94403dc4093a1d8c009cdcc6f2549a24/runtime/validation/parity/reasoned.json#L806).

> "1049": {
>    "derivation": "tsd_set_model.py: members by OP-5, admission by OP-6, children forwarded (OP-4) from the operand OP-5 names; the first admitted evaluation publishes (validity), later empty deltas do not.",
>    "expected": [
>     {
>      "$map": [
>       [
>        "a",
>        -19
>       ]
>      ]
>     },
>     {
>      "$map": [
>       [
>        "a",
>        -19
>       ]
>      ]
>     }
>    ],
>    "family": "tsd-set-operators",
>    "mode": "trace",
>    "rules": [
>     "OP-4",
>     "OP-5",
>     "OP-6",
>     "OP-7"
>    ]
>   }

### Excerpt 35

[Source, line 835](https://github.com/hhenson/hgraph_spec/blob/b295f39c94403dc4093a1d8c009cdcc6f2549a24/runtime/validation/parity/reasoned.json#L835).

> "1061": {
>    "derivation": "tsd_set_model.py: members by OP-5, admission by OP-6, children forwarded (OP-4) from the operand OP-5 names; the first admitted evaluation publishes (validity), later empty deltas do not.",
>    "expected": null,
>    "family": "tsd-set-operators",
>    "mode": "trace",
>    "rules": [
>     "OP-4",
>     "OP-5",
>     "OP-6",
>     "OP-7"
>    ]
>   }

### Excerpt 36

[Source, line 858](https://github.com/hhenson/hgraph_spec/blob/b295f39c94403dc4093a1d8c009cdcc6f2549a24/runtime/validation/parity/reasoned.json#L858).

> "1063": {
>    "derivation": "tsd_set_model.py: members by OP-5, admission by OP-6, children forwarded (OP-4) from the operand OP-5 names; the first admitted evaluation publishes (validity), later empty deltas do not.",
>    "expected": [
>     {
>      "$map": [
>       [
>        "a",
>        -19
>       ]
>      ]
>     },
>     {
>      "$map": [
>       [
>        "a",
>        -19
>       ]
>      ]
>     },
>     null
>    ],
>    "family": "tsd-set-operators",
>    "mode": "trace",
>    "rules": [
>     "OP-4",
>     "OP-5",
>     "OP-6",
>     "OP-7"
>    ]
>   }

### Excerpt 37

[Source, line 888](https://github.com/hhenson/hgraph_spec/blob/b295f39c94403dc4093a1d8c009cdcc6f2549a24/runtime/validation/parity/reasoned.json#L888).

> "1064": {
>    "derivation": "tsd_set_model.py: members by OP-5, admission by OP-6, children forwarded (OP-4) from the operand OP-5 names; the first admitted evaluation publishes (validity), later empty deltas do not.",
>    "expected": null,
>    "family": "tsd-set-operators",
>    "mode": "trace",
>    "rules": [
>     "OP-4",
>     "OP-5",
>     "OP-6",
>     "OP-7"
>    ]
>   }

### Excerpt 38

[Source, line 900](https://github.com/hhenson/hgraph_spec/blob/b295f39c94403dc4093a1d8c009cdcc6f2549a24/runtime/validation/parity/reasoned.json#L900).

> "1065": {
>    "derivation": "tsd_set_model.py: members by OP-5, admission by OP-6, children forwarded (OP-4) from the operand OP-5 names; the first admitted evaluation publishes (validity), later empty deltas do not.",
>    "expected": [
>     null,
>     null,
>     {
>      "$map": [
>       [
>        "a",
>        -1
>       ]
>      ]
>     },
>     {
>      "$map": [
>       [
>        "c",
>        -19
>       ]
>      ]
>     },
>     {
>      "$map": [
>       [
>        "c",
>        -19
>       ]
>      ]
>     }
>    ],
>    "family": "tsd-set-operators",
>    "mode": "trace",
>    "rules": [
>     "OP-4",
>     "OP-5",
>     "OP-6",
>     "OP-7"
>    ]
>   }

### Excerpt 39

[Source, line 939](https://github.com/hhenson/hgraph_spec/blob/b295f39c94403dc4093a1d8c009cdcc6f2549a24/runtime/validation/parity/reasoned.json#L939).

> "1066": {
>    "derivation": "tsd_set_model.py: members by OP-5, admission by OP-6, children forwarded (OP-4) from the operand OP-5 names; the first admitted evaluation publishes (validity), later empty deltas do not.",
>    "expected": [
>     {
>      "$map": [
>       [
>        "a",
>        -19
>       ]
>      ]
>     },
>     {
>      "$map": [
>       [
>        "a",
>        -19
>       ]
>      ]
>     }
>    ],
>    "family": "tsd-set-operators",
>    "mode": "trace",
>    "rules": [
>     "OP-4",
>     "OP-5",
>     "OP-6",
>     "OP-7"
>    ]
>   }

### Excerpt 40

[Source, line 968](https://github.com/hhenson/hgraph_spec/blob/b295f39c94403dc4093a1d8c009cdcc6f2549a24/runtime/validation/parity/reasoned.json#L968).

> "1067": {
>    "derivation": "tsd_set_model.py: members by OP-5, admission by OP-6, children forwarded (OP-4) from the operand OP-5 names; the first admitted evaluation publishes (validity), later empty deltas do not.",
>    "expected": [
>     {
>      "$map": [
>       [
>        "b",
>        -20
>       ]
>      ]
>     },
>     {
>      "$map": [
>       [
>        "b",
>        7
>       ]
>      ]
>     }
>    ],
>    "family": "tsd-set-operators",
>    "mode": "trace",
>    "rules": [
>     "OP-4",
>     "OP-5",
>     "OP-6",
>     "OP-7"
>    ]
>   }

### Excerpt 41

[Source, line 997](https://github.com/hhenson/hgraph_spec/blob/b295f39c94403dc4093a1d8c009cdcc6f2549a24/runtime/validation/parity/reasoned.json#L997).

> "1068": {
>    "derivation": "tsd_set_model.py: members by OP-5, admission by OP-6, children forwarded (OP-4) from the operand OP-5 names; the first admitted evaluation publishes (validity), later empty deltas do not.",
>    "expected": [
>     null,
>     {
>      "$map": [
>       [
>        "c",
>        -3
>       ]
>      ]
>     },
>     {
>      "$map": [
>       [
>        "c",
>        -3
>       ]
>      ]
>     }
>    ],
>    "family": "tsd-set-operators",
>    "mode": "trace",
>    "rules": [
>     "OP-4",
>     "OP-5",
>     "OP-6",
>     "OP-7"
>    ]
>   }

### Excerpt 42

[Source, line 1027](https://github.com/hhenson/hgraph_spec/blob/b295f39c94403dc4093a1d8c009cdcc6f2549a24/runtime/validation/parity/reasoned.json#L1027).

> "1069": {
>    "derivation": "tsd_set_model.py: members by OP-5, admission by OP-6, children forwarded (OP-4) from the operand OP-5 names; the first admitted evaluation publishes (validity), later empty deltas do not.",
>    "expected": [
>     {
>      "$map": [
>       [
>        "a",
>        -17
>       ]
>      ]
>     },
>     null,
>     {
>      "$map": [
>       [
>        "a",
>        -13
>       ]
>      ]
>     }
>    ],
>    "family": "tsd-set-operators",
>    "mode": "trace",
>    "rules": [
>     "OP-4",
>     "OP-5",
>     "OP-6",
>     "OP-7"
>    ]
>   }

### Excerpt 43

[Source, line 1100](https://github.com/hhenson/hgraph_spec/blob/b295f39c94403dc4093a1d8c009cdcc6f2549a24/runtime/validation/parity/reasoned.json#L1100).

> "1084": {
>    "derivation": "tsd_set_model.py: members by OP-5, admission by OP-6, children forwarded (OP-4) from the operand OP-5 names; the first admitted evaluation publishes (validity), later empty deltas do not.",
>    "expected": null,
>    "family": "tsd-set-operators",
>    "mode": "trace",
>    "rules": [
>     "OP-4",
>     "OP-5",
>     "OP-6",
>     "OP-7"
>    ]
>   }

### Excerpt 44

[Source, line 1112](https://github.com/hhenson/hgraph_spec/blob/b295f39c94403dc4093a1d8c009cdcc6f2549a24/runtime/validation/parity/reasoned.json#L1112).

> "1085": {
>    "derivation": "tsd_set_model.py: members by OP-5, admission by OP-6, children forwarded (OP-4) from the operand OP-5 names; the first admitted evaluation publishes (validity), later empty deltas do not.",
>    "expected": null,
>    "family": "tsd-set-operators",
>    "mode": "trace",
>    "rules": [
>     "OP-4",
>     "OP-5",
>     "OP-6",
>     "OP-7"
>    ]
>   }

### Excerpt 45

[Source, line 1145](https://github.com/hhenson/hgraph_spec/blob/b295f39c94403dc4093a1d8c009cdcc6f2549a24/runtime/validation/parity/reasoned.json#L1145).

> "1087": {
>    "derivation": "tsd_set_model.py: members by OP-5, admission by OP-6, children forwarded (OP-4) from the operand OP-5 names; the first admitted evaluation publishes (validity), later empty deltas do not.",
>    "expected": null,
>    "family": "tsd-set-operators",
>    "mode": "trace",
>    "rules": [
>     "OP-4",
>     "OP-5",
>     "OP-6",
>     "OP-7"
>    ]
>   }

### Excerpt 46

[Source, line 1486](https://github.com/hhenson/hgraph_spec/blob/b295f39c94403dc4093a1d8c009cdcc6f2549a24/runtime/validation/parity/reasoned.json#L1486).

> "959": {
>    "derivation": "tsd_set_model.py: members by OP-5, admission by OP-6, children forwarded (OP-4) from the operand OP-5 names; the first admitted evaluation publishes (validity), later empty deltas do not.",
>    "expected": null,
>    "family": "tsd-set-operators",
>    "mode": "trace",
>    "rules": [
>     "OP-4",
>     "OP-5",
>     "OP-6",
>     "OP-7"
>    ]
>   }

### Excerpt 47

[Source, line 1509](https://github.com/hhenson/hgraph_spec/blob/b295f39c94403dc4093a1d8c009cdcc6f2549a24/runtime/validation/parity/reasoned.json#L1509).

> "961": {
>    "derivation": "tsd_set_model.py: members by OP-5, admission by OP-6, children forwarded (OP-4) from the operand OP-5 names; the first admitted evaluation publishes (validity), later empty deltas do not.",
>    "expected": [
>     {
>      "$map": []
>     }
>    ],
>    "family": "tsd-set-operators",
>    "mode": "trace",
>    "rules": [
>     "OP-4",
>     "OP-5",
>     "OP-6",
>     "OP-7"
>    ]
>   }

### Excerpt 48

[Source, line 1525](https://github.com/hhenson/hgraph_spec/blob/b295f39c94403dc4093a1d8c009cdcc6f2549a24/runtime/validation/parity/reasoned.json#L1525).

> "962": {
>    "derivation": "tsd_set_model.py: members by OP-5, admission by OP-6, children forwarded (OP-4) from the operand OP-5 names; the first admitted evaluation publishes (validity), later empty deltas do not.",
>    "expected": [
>     null,
>     {
>      "$map": [
>       [
>        "b",
>        -18
>       ]
>      ]
>     },
>     {
>      "$map": [
>       [
>        "b",
>        -18
>       ]
>      ]
>     }
>    ],
>    "family": "tsd-set-operators",
>    "mode": "trace",
>    "rules": [
>     "OP-4",
>     "OP-5",
>     "OP-6",
>     "OP-7"
>    ]
>   }

### Excerpt 49

[Source, line 1618](https://github.com/hhenson/hgraph_spec/blob/b295f39c94403dc4093a1d8c009cdcc6f2549a24/runtime/validation/parity/reasoned.json#L1618).

> "966": {
>    "derivation": "tsd_set_model.py: members by OP-5, admission by OP-6, children forwarded (OP-4) from the operand OP-5 names; the first admitted evaluation publishes (validity), later empty deltas do not.",
>    "expected": null,
>    "family": "tsd-set-operators",
>    "mode": "trace",
>    "rules": [
>     "OP-4",
>     "OP-5",
>     "OP-6",
>     "OP-7"
>    ]
>   }

### Excerpt 50

[Source, line 1630](https://github.com/hhenson/hgraph_spec/blob/b295f39c94403dc4093a1d8c009cdcc6f2549a24/runtime/validation/parity/reasoned.json#L1630).

> "967": {
>    "derivation": "tsd_set_model.py: members by OP-5, admission by OP-6, children forwarded (OP-4) from the operand OP-5 names; the first admitted evaluation publishes (validity), later empty deltas do not.",
>    "expected": [
>     null,
>     {
>      "$map": [
>       [
>        "a",
>        -19
>       ]
>      ]
>     },
>     {
>      "$map": [
>       [
>        "a",
>        -19
>       ]
>      ]
>     }
>    ],
>    "family": "tsd-set-operators",
>    "mode": "trace",
>    "rules": [
>     "OP-4",
>     "OP-5",
>     "OP-6",
>     "OP-7"
>    ]
>   }

### Excerpt 51

[Source, line 1660](https://github.com/hhenson/hgraph_spec/blob/b295f39c94403dc4093a1d8c009cdcc6f2549a24/runtime/validation/parity/reasoned.json#L1660).

> "968": {
>    "derivation": "tsd_set_model.py: members by OP-5, admission by OP-6, children forwarded (OP-4) from the operand OP-5 names; the first admitted evaluation publishes (validity), later empty deltas do not.",
>    "expected": [
>     null,
>     null,
>     {
>      "$map": [
>       [
>        "a",
>        -19
>       ]
>      ]
>     },
>     {
>      "$map": [
>       [
>        "a",
>        -19
>       ]
>      ]
>     }
>    ],
>    "family": "tsd-set-operators",
>    "mode": "trace",
>    "rules": [
>     "OP-4",
>     "OP-5",
>     "OP-6",
>     "OP-7"
>    ]
>   }

### Excerpt 52

[Source, line 1691](https://github.com/hhenson/hgraph_spec/blob/b295f39c94403dc4093a1d8c009cdcc6f2549a24/runtime/validation/parity/reasoned.json#L1691).

> "969": {
>    "derivation": "tsd_set_model.py: members by OP-5, admission by OP-6, children forwarded (OP-4) from the operand OP-5 names; the first admitted evaluation publishes (validity), later empty deltas do not.",
>    "expected": null,
>    "family": "tsd-set-operators",
>    "mode": "trace",
>    "rules": [
>     "OP-4",
>     "OP-5",
>     "OP-6",
>     "OP-7"
>    ]
>   }

### Excerpt 53

[Source, line 1703](https://github.com/hhenson/hgraph_spec/blob/b295f39c94403dc4093a1d8c009cdcc6f2549a24/runtime/validation/parity/reasoned.json#L1703).

> "978": {
>    "derivation": "tsd_set_model.py: members by OP-5, admission by OP-6, children forwarded (OP-4) from the operand OP-5 names; the first admitted evaluation publishes (validity), later empty deltas do not. Three operands fold pairwise through the empty intermediate a^b; that intermediate publishes (and so the fold does) only if the first empty result validates, which is point to settle 1.",
>    "expected": [
>     {
>      "$map": [
>       [
>        "a",
>        -19
>       ]
>      ]
>     }
>    ],
>    "family": "tsd-set-operators",
>    "mode": "trace",
>    "rules": [
>     "OP-4",
>     "OP-5",
>     "OP-6",
>     "OP-7"
>    ],
>    "ruling": "first-empty-set-result"
>   }

### Excerpt 54

[Source, line 1725](https://github.com/hhenson/hgraph_spec/blob/b295f39c94403dc4093a1d8c009cdcc6f2549a24/runtime/validation/parity/reasoned.json#L1725).

> "979": {
>    "derivation": "tsd_set_model.py: members by OP-5, admission by OP-6, children forwarded (OP-4) from the operand OP-5 names; the first admitted evaluation publishes (validity), later empty deltas do not.",
>    "expected": [
>     {
>      "$map": [
>       [
>        "b",
>        15
>       ]
>      ]
>     },
>     {
>      "$map": [
>       [
>        "b",
>        15
>       ]
>      ]
>     }
>    ],
>    "family": "tsd-set-operators",
>    "mode": "trace",
>    "rules": [
>     "OP-4",
>     "OP-5",
>     "OP-6",
>     "OP-7"
>    ]
>   }

### Excerpt 55

[Source, line 1754](https://github.com/hhenson/hgraph_spec/blob/b295f39c94403dc4093a1d8c009cdcc6f2549a24/runtime/validation/parity/reasoned.json#L1754).

> "980": {
>    "derivation": "tsd_set_model.py: members by OP-5, admission by OP-6, children forwarded (OP-4) from the operand OP-5 names; the first admitted evaluation publishes (validity), later empty deltas do not.",
>    "expected": [
>     {
>      "$map": [
>       [
>        "c",
>        12
>       ]
>      ]
>     },
>     {
>      "$map": [
>       [
>        "c",
>        12
>       ]
>      ]
>     }
>    ],
>    "family": "tsd-set-operators",
>    "mode": "trace",
>    "rules": [
>     "OP-4",
>     "OP-5",
>     "OP-6",
>     "OP-7"
>    ]
>   }

### Excerpt 56

[Source, line 1783](https://github.com/hhenson/hgraph_spec/blob/b295f39c94403dc4093a1d8c009cdcc6f2549a24/runtime/validation/parity/reasoned.json#L1783).

> "981": {
>    "derivation": "tsd_set_model.py: members by OP-5, admission by OP-6, children forwarded (OP-4) from the operand OP-5 names; the first admitted evaluation publishes (validity), later empty deltas do not.",
>    "expected": null,
>    "family": "tsd-set-operators",
>    "mode": "trace",
>    "rules": [
>     "OP-4",
>     "OP-5",
>     "OP-6",
>     "OP-7"
>    ]
>   }

### Excerpt 57

[Source, line 1795](https://github.com/hhenson/hgraph_spec/blob/b295f39c94403dc4093a1d8c009cdcc6f2549a24/runtime/validation/parity/reasoned.json#L1795).

> "982": {
>    "derivation": "tsd_set_model.py: members by OP-5, admission by OP-6, children forwarded (OP-4) from the operand OP-5 names; the first admitted evaluation publishes (validity), later empty deltas do not.",
>    "expected": [
>     null,
>     null,
>     {
>      "$map": [
>       [
>        "c",
>        -19
>       ]
>      ]
>     },
>     {
>      "$map": [
>       [
>        "c",
>        -19
>       ]
>      ]
>     }
>    ],
>    "family": "tsd-set-operators",
>    "mode": "trace",
>    "rules": [
>     "OP-4",
>     "OP-5",
>     "OP-6",
>     "OP-7"
>    ]
>   }

### Excerpt 58

[Source, line 1826](https://github.com/hhenson/hgraph_spec/blob/b295f39c94403dc4093a1d8c009cdcc6f2549a24/runtime/validation/parity/reasoned.json#L1826).

> "983": {
>    "derivation": "tsd_set_model.py: members by OP-5, admission by OP-6, children forwarded (OP-4) from the operand OP-5 names; the first admitted evaluation publishes (validity), later empty deltas do not.",
>    "expected": [
>     {
>      "$map": []
>     },
>     {
>      "$map": [
>       [
>        "a",
>        -19
>       ]
>      ]
>     },
>     {
>      "$map": [
>       [
>        "a",
>        -19
>       ]
>      ]
>     }
>    ],
>    "family": "tsd-set-operators",
>    "mode": "trace",
>    "rules": [
>     "OP-4",
>     "OP-5",
>     "OP-6",
>     "OP-7"
>    ],
>    "ruling": "first-empty-set-result"
>   }

### Excerpt 59

[Source, line 1859](https://github.com/hhenson/hgraph_spec/blob/b295f39c94403dc4093a1d8c009cdcc6f2549a24/runtime/validation/parity/reasoned.json#L1859).

> "984": {
>    "derivation": "tsd_set_model.py: members by OP-5, admission by OP-6, children forwarded (OP-4) from the operand OP-5 names; the first admitted evaluation publishes (validity), later empty deltas do not.",
>    "expected": [
>     {
>      "$map": []
>     },
>     {
>      "$map": [
>       [
>        "a",
>        -19
>       ],
>       [
>        "b",
>        -19
>       ]
>      ]
>     },
>     {
>      "$map": [
>       [
>        "a",
>        -19
>       ]
>      ]
>     }
>    ],
>    "family": "tsd-set-operators",
>    "mode": "trace",
>    "rules": [
>     "OP-4",
>     "OP-5",
>     "OP-6",
>     "OP-7"
>    ],
>    "ruling": "first-empty-set-result"
>   }

## language/examples/struct-imports/instrument-book.hgl

### Excerpt 1

[Source, line 6](https://github.com/hhenson/hgraph_spec/blob/b295f39c94403dc4093a1d8c009cdcc6f2549a24/language/examples/struct-imports/instrument-book.hgl#L6).

> # Generated C++ refers to that module's own definition and includes its
> # header rather than re-declaring the struct.

## language/stdlib/examples/elements-iteration.hgl

### Excerpt 1

[Source, line 2](https://github.com/hhenson/hgraph_spec/blob/b295f39c94403dc4093a1d8c009cdcc6f2549a24/language/stdlib/examples/elements-iteration.hgl#L2).

> # See language/docs/design/iteration.md for paired HGL/C++ mappings.

## language/stdlib/examples/switch-scenarios.hgl

### Excerpt 1

[Source, line 2](https://github.com/hhenson/hgraph_spec/blob/b295f39c94403dc4093a1d8c009cdcc6f2549a24/language/stdlib/examples/switch-scenarios.hgl#L2).

> # Paired source and C++ mappings: language/docs/developer-guide/control-flow-cpp-mappings.md.

## language/stdlib/examples/invalid/conditional-unassigned-result.hgl

### Excerpt 1

[Source, line 2](https://github.com/hhenson/hgraph_spec/blob/b295f39c94403dc4093a1d8c009cdcc6f2549a24/language/stdlib/examples/invalid/conditional-unassigned-result.hgl#L2).

> # Intentionally invalid under the agreed design; CTest runs it through hgl check.

## runtime/cases_fixed.md

### Excerpt 1

[Source, line 11](https://github.com/hhenson/hgraph_spec/blob/b295f39c94403dc4093a1d8c009cdcc6f2549a24/runtime/cases_fixed.md#L11).

> The initial expectations are in [reasoned.json](https://github.com/hhenson/hgraph_spec/blob/b295f39c94403dc4093a1d8c009cdcc6f2549a24/runtime/validation/fixed/reasoned.json).

## runtime/overview.md

### Excerpt 1

[Source, line 372](https://github.com/hhenson/hgraph_spec/blob/b295f39c94403dc4093a1d8c009cdcc6f2549a24/runtime/overview.md#L372).

> | Wiring | [../wiring/wiring.md](https://github.com/hhenson/hgraph_spec/blob/b295f39c94403dc4093a1d8c009cdcc6f2549a24/wiring/wiring.md) | first draft; type resolution validated |

### Excerpt 2

[Source, line 373](https://github.com/hhenson/hgraph_spec/blob/b295f39c94403dc4093a1d8c009cdcc6f2549a24/runtime/overview.md#L373).

> draft, parity-derived families; a provisional home

## language/docs/user-guide/language-tour.md

### Excerpt 1

[Source, line 151](https://github.com/hhenson/hgraph_spec/blob/b295f39c94403dc4093a1d8c009cdcc6f2549a24/language/docs/user-guide/language-tour.md#L151).

> ranking remain explicitly deferred or fail closed as described in the roadmap.

## compiler/stdlib_graph/README.md

### Excerpt 1

[Source, line 16](https://github.com/hhenson/hgraph_spec/blob/b295f39c94403dc4093a1d8c009cdcc6f2549a24/compiler/stdlib_graph/README.md#L16).

> 42 in `[_, 42, _, 42, -7]`. Backend timestamp prefixes are excluded from the
> comparison; the label, sampling prefix and scalar text are retained.

## runtime/validation/parity/decisions.json

### Excerpt 1

[Source, line 10](https://github.com/hhenson/hgraph_spec/blob/b295f39c94403dc4093a1d8c009cdcc6f2549a24/runtime/validation/parity/decisions.json#L10).

> Point to settle 2: Python writes a dictionary's text in insertion order; the C++ runtime writes storage order, which reuses a removed key's slot. Which order is the contract?

### Excerpt 2

[Source, line 12](https://github.com/hhenson/hgraph_spec/blob/b295f39c94403dc4093a1d8c009cdcc6f2549a24/runtime/validation/parity/decisions.json#L12).

> A map has no order, so the order of the members in its text is unspecified and both runtimes conform. Sets have no order either (VAL-8) and are treated the same way.

### Excerpt 3

[Source, line 29](https://github.com/hhenson/hgraph_spec/blob/b295f39c94403dc4093a1d8c009cdcc6f2549a24/runtime/validation/parity/decisions.json#L29).

> Point to settle 1: should a set operator's first admitted evaluation publish an empty dictionary? Python 0.5.41 does for difference and intersection but not for ^ and |; the C++ runtime did only for intersection.

### Excerpt 4

[Source, line 31](https://github.com/hhenson/hgraph_spec/blob/b295f39c94403dc4093a1d8c009cdcc6f2549a24/runtime/validation/parity/decisions.json#L31).

> An admitted result is a value even when empty (valid does not mean non-empty); one rule across the four operators, as both runtimes already have for sets; and without it a three-operand symmetric difference whose first two operands cancel never publishes (#978).

### Excerpt 5

[Source, line 40](https://github.com/hhenson/hgraph_spec/blob/b295f39c94403dc4093a1d8c009cdcc6f2549a24/runtime/validation/parity/decisions.json#L40).

> tsd_set_model.py unchanged: the first admitted evaluation publishes, empty or not

## runtime/validation/wiring/decisions.json

### Excerpt 1

[Source, line 96](https://github.com/hhenson/hgraph_spec/blob/b295f39c94403dc4093a1d8c009cdcc6f2549a24/runtime/validation/wiring/decisions.json#L96).

> Settles point 6. Both runtimes register a wider candidate (WV-6); expectations follow this ruling.

### Excerpt 2

[Source, line 106](https://github.com/hhenson/hgraph_spec/blob/b295f39c94403dc4093a1d8c009cdcc6f2549a24/runtime/validation/wiring/decisions.json#L106).

> A declared optional parameter may be absent from a candidate. The C++ declaration cleanup and the registration check follow (WV-6).
