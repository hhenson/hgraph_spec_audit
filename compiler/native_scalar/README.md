# Native scalar operator traces

All six [reasoned cases](../../spec/compiler/native_scalar/cases.json) match
Python 0.5.42 and C++ 0.8.30 in three fresh-process runs each. No variation.
These are reference runtime observations; native-requirement admission and
specialization are checked by the HGL compiler suite. The matching HGL tests
are in `hgraph_std/hgl/hgraph/tests/operators.hgl`.

Reproduce with each pinned environment, choosing a new output file:

```sh
.venv-python/bin/python tools/native_scalar_cases.py --engine python --output results/scalar-python.json
.venv-cpp/bin/python tools/native_scalar_cases.py --engine cpp --output results/scalar-cpp.json
```
