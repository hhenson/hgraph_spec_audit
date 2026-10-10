# Remaining scalar reference observations

Frozen bytes and object-bridge probes ran against both installed reference
engines in three fresh processes each. The identities fingerprint installed
packages and native binaries; they do not establish a release or Git build
identity. [Reasoning](reasoned.json) precedes [observations](observed.json).

Both engines publish present empty bytes and equal byte repeats, preserve
silence, and forward complete byte deltas. Raw no-output results are `null`;
the independently derived dense horizon remains separate. Constructor range,
equality and unsigned-order checks use Python's `bytes` in each interpreter;
they are not direct native constructor or native hashing measurements.

Both public object-typed bridges preserve mixed payload types. After mutating
a replay source list, Python's earlier raw capture changes; the native C++
capture remains independent. This Python ownership disagreement is retained,
not made a new language rule. These observations do not define HGL `any`
boxing, a present empty `any`, or native atomic provider conformance. Python
class/object bridge support is not a registered native C++ atomic fixture.

```sh
python3 runtime/validation/last_scalar_types/observe.py \
  --python <python-reference> --cpp <native-reference> --output <new-result.json>
python3 runtime/validation/last_scalar_types/check.py
```

The separately fingerprinted [native probe](native.cpp) links an installed SDK
and registers two distinct nominal atomic types plus a type lacking optional
capabilities. Three fresh runs validate owning native copies and real graph
pass-through for native atomic values and heterogeneous `Any` boxes. Empty
boxes, false/zero/empty payloads and equal repeats publish independently of
silent positions. [Native reasoning](native_reasoned.json) precedes the
[record](native_observed.json); installed SDK headers, archives and compiler
identity are fingerprinted without claiming a Git build identity.

Explicit `AnyView` assignment nests an already boxed value; erased assignment
flattens it. Both observations are retained. Equality and ordering of boxed
values lacking those capabilities return false/unordered; hash fails. The
first two disagree with VAL-11 and are not adopted as language rules.

```sh
cmake -S runtime/validation/last_scalar_types -B <build> -DCMAKE_PREFIX_PATH=<sdk>
cmake --build <build>
python3 runtime/validation/last_scalar_types/native_observe.py \
  --executable <native-probe> --sdk <installed-sdk> --build-dir <build> \
  --output <new-native-result.json>
python3 -m unittest discover -s runtime/validation/last_scalar_types
```
