# Ordinary tuple construction

Measured 2026-10-08 from expectations written before the probes ran. The HGL
[proposal](https://github.com/hhenson/hgraph_spec/blob/c82b93a2cf377bd8da5f9bbe61234a01fb475ca3/language/docs/design/ordinary-tuple-values.md)
admits runtime ordinary tuple elements and requires evaluation plus
independent retention of each element in written order. This follows the
existing ordinary struct construction rule; reference call conventions do not
choose HGL evaluation order.

[observed.json](observed.json) records three identical fresh-process runs each
under pure Python hgraph 0.5.41 and a C++ development wheel reporting 0.0.0,
both on Python 3.14.4. Source, package, loaded-library and harness hashes identify
the artifacts. This is not a released-version parity claim.

| Surface | Observation | Evidence boundary |
| --- | --- | --- |
| Python tuple expressions on both packages | `(mark(2), mark(1))` logs `[2,1]` once; nested construction logs `[2,1,3]`; a first-element exception prevents the second element. | Python authoring order, including when the imported engine is native. |
| Runtime compute on both engines | `TS[int]` input `[7,None,-1,0]` produces `TS[tuple[int,bool]]` output `[(7,True),None,(-1,False),(0,False)]`. | Complete ordinary atomic tuple payloads, not structural TST or sparse child observations. |
| Python tuple containing mutable lists | Ordinary children alias; later source append changes both. Explicit per-child `deepcopy` preserves both original values. | Ordinary tuple syntax does not itself satisfy HGL independent ownership. |
| Direct C++ `std::tuple<int,int>(mark(2),mark(1))` | GNU C++ evaluates `[1,2]`, while stored positions are `[2,1]`. With `fail(2)` first in source, `mark(1)` executes before the failure. | Constructor-call argument order differs from the proposed HGL rule. No named temporaries or staged evaluation hide the difference. |

The last row is measured by [native_call.cpp](native_call.cpp), with compiler,
flags, executable and source hashes in [native_observed.json](native_observed.json).
It uses the C++ standard library, not an hgraph node or structural tuple. The
observed order is compiler-specific, not a portable reverse-order requirement.

For hgraph native owning-value retention, the directly relevant existing
[value-sequence evidence](../value_sequences/README.md#copy-alias-and-replacement-observations)
records `native_tuple_nested_copy`: a tuple built from a mutable list view
retains `[1,2]` after the source gains another element. Its source, SDK and
binary identities remain in [that saved measurement](../value_sequences/native_observed.json).
This older result was not rerun here and does not establish expression order.
Together these observations support runtime tuple construction and the ability
to retain children independently; sequencing retention before the next element
is an explicit HGL choice. Arbitrary retention/allocation failure and rollback
are unmeasured. This audit makes no structural TST, invalidation or empty-event
claim and does not change nonempty list-literal rules.

Reproduce with independent immutable environments and new output destinations:

```sh
python3 runtime/validation/tuple_construction/observe.py \
  --python /path/to/python-hgraph/bin/python \
  --cpp /path/to/cpp-hgraph/bin/python --output /tmp/tuple-observed.json
python3 runtime/validation/tuple_construction/native_observe.py \
  --cxx g++ --output /tmp/tuple-native-observed.json
python3 runtime/validation/tuple_construction/check.py
```

The checker verifies recorded evidence only. Failed or unsupported observations
remain data; no adapter rewrites them into expected results.
