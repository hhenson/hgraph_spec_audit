# Required reads from retained unset observations

This bounded audit informs the proposed `value.unset_read` contract. Required
scalar or collection operations need a payload; observation and retention can
preserve absence. Expectations in `reasoned.json` precede measurement. Each
source has a valid sibling and an independently unset or present child.
No structural TST, wholly invalid source admission, new invalid map membership,
empty publication, bounds failure or source-HGL implementation is measured.

## Genuine observations

Nine cases ran in three fresh processes per surface against Python hgraph
0.5.41 and the frozen C++ development package (version 0.0.0). Version alone
is not the native identity: records include artifact hashes. All five present
controls agree, including true and false Boolean controls.

The facade probe distinguishes a retained whole bundle's field projection
from a separately retained child `.value`. It never fills absent fields or
converts missing children to defaults:

| Unset case | Python retained whole bundle | Python retained child | C++ facade, both surfaces |
| --- | --- | --- | --- |
| i64 arithmetic | Field absent: `KeyError` | `None`: arithmetic `TypeError` | `None`: arithmetic `TypeError` |
| Boolean branch | Field absent: `KeyError` | `None`: host branch selects false | `None`: host branch selects false |
| Fixed list length | Field absent: `KeyError` | `(None,None)`: length 2 | `None`: length `TypeError` |
| Map items | Field absent: `KeyError` | Empty mapping: empty iteration | `None`: items `AttributeError` |

Python collection observations lose the outer child's absence before the
operation. Python-language truth coercion is **not** evidence for HGL Boolean
extraction, even when executed in the C++ engine's facade. No host exception
class defines the proposed source error code. Initial harness trials exposed
a mistaken attribute projection on dict snapshots and repeated schema names;
these harness errors were corrected before the recorded measurement.

The separate installed-SDK C++ graph retains the whole bundle in an owning
`Value`, records source and retained child validity, then uses `checked_as<Int>`,
`checked_as<Bool>`, `as_list().size()` or `as_map().items()`. All four unset
operations throw; all five present controls succeed. Present false extracts
successfully and selects false. The invalid list/map failures occur when
requesting the typed collection view, before size or iteration. This native
surface preserves absence through retention; it uses no Python scalar coercion.

The native Map items probe does not establish admission of ordinary retained
Map iteration in HGL. The proposed HGL cases use only scalar reads and list
length; scalar-child `let` retention is itself part of that source extension.

This supports required-read failure by reasoning and native typed extraction;
facade differences remain recorded variations. Errors are caught locally to
observe controls: graph error propagation, stable HGL codes, failure cleanup
and generated HGL execution are not established by this audit.

## Build-command provenance refresh

The original native record and its recorder/CMake inputs are preserved under
`archive/`. The current recorder reads the native translation unit from CMake's
`compile_commands.json`, preserving tokenized flags with private paths replaced
by stable labels. It does not depend on Make's `flags.make`.

The same frozen SDK was built with Unix Makefiles and Ninja, then each binary
ran in three fresh processes. `native_observed.json` records Make and
`native_ninja_observed.json` records Ninja. All nine observations, loaded native
library hashes and SDK header hashes match the original record. Recorder and
CMake hashes changed because command recording changed; the facade record and
native probe source did not change. The archived recorder is historical input,
not the current reproduction entry point.

Offline checks require exactly the Python and C++ facade engines and validate
their full package, runner-source and loaded-library identities. The three native
hgraph library hashes must match the C++ facade identity. Checks compare exact
retained/payload values and types before derived results, so defaulting absence
cannot hide behind an unchanged Boolean result or collection length. Both native
records retain their agreement with archived results.

## Target-artifact provenance refresh

The current recorder requires `--executable` to resolve to the artifact emitted
by CMake's configured `unset_required_reads_native` target manifest, then builds
that target before hashing and running it. A binary from another build is
rejected even if its contents or linked SDK happen to match. Missing or ambiguous
manifest data and failed builds prevent measurement. Single-config builds select
only `CMAKE_BUILD_TYPE` from the cache; multi-config builds require one matching
artifact among `CMAKE_CONFIGURATION_TYPES`. Stale manifests are ignored. Records
include the target, configuration, relative artifact path and manifest hash.

The prior Make/Ninja records and their recorder/CMake inputs remain unchanged
under `archive/compile_commands/`. New three-process runs for each generator use
the same frozen SDK; observations and loaded-library/header identities match
both historical rounds. This refresh changes build provenance, not expected
results. Failure rows must report `outcome: failure` as well as their exception
type; a contradictory success outcome fails offline validation.

The preceding target-identity records and inputs are preserved byte-for-byte in
`archive/target_identity/`. Fresh Make/Ninja Release records use the revised
recorder. `native_reconfigured_observed.json` additionally records three Debug
runs after an actual Ninja Release-to-Debug reconfiguration in a separate build;
the obsolete Release manifest still names the same executable. All observations
and SDK library/header identities agree with the earlier records.

The next refresh preserves those three records and inputs unchanged under
`archive/active_configuration/`. Compile-command selection now uses the chosen
configuration's object output or `CMAKE_INTDIR` argument; conflicting clues,
missing matches and duplicate matches fail. Multi-config commands without any
configuration marker cannot stand in for the selected configuration. Existing
single-config commands and quoted arguments keep their behavior.

`native_multiconfig_debug_observed.json` and
`native_multiconfig_release_observed.json` record three fresh runs each from
one Ninja Multi-Config build. Their target paths, configurations and compiler
commands agree. The Make, Ninja and reconfigured Debug records were also rerun
with this recorder. All nine observations and SDK identities remain unchanged.
For multi-config reproduction, use `-G "Ninja Multi-Config"` and select
`Debug/unset_required_reads_native` or `Release/unset_required_reads_native`.

## Reproduction

```sh
python3 runtime/validation/unset_required_reads/observe.py \
  --python /path/to/python-engine/bin/python --cpp /path/to/cpp-engine/bin/python \
  --output /tmp/unset-public.json
cmake -G Ninja -S runtime/validation/unset_required_reads -B /tmp/unset-native \
  -Dhgraph_DIR=/path/to/sdk/lib/cmake/hgraph \
  -DPython_EXECUTABLE=/path/to/cpp-engine/bin/python -DCMAKE_BUILD_TYPE=Release
cmake --build /tmp/unset-native --parallel 2
python3 runtime/validation/unset_required_reads/native_observe.py \
  --executable /tmp/unset-native/unset_required_reads_native \
  --sdk-include /path/to/sdk/include --build-dir /tmp/unset-native \
  --output /tmp/unset-native.json
python3 runtime/validation/unset_required_reads/check.py
```

Use `-G "Unix Makefiles"` for the other verified generator.
Recorders require new destinations. Three-run equality and identity checks
reject unstable measurements. Offline validation checks source/corpus hashes,
present controls, absence preservation and every recorded variation; it is
not another runtime measurement. Compiler implementations were not inspected
or changed.
