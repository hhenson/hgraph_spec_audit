# Empty sparse delta validity

The user ruling of 2026-10-10 replaces the earlier undecided empty-event
policy: applying an empty sparse delta to an invalid endpoint makes it valid
and ticks an empty delta; applying it to a valid endpoint is silent. It does
not initialize children or copy a producer's event identity. Atomic complete
snapshots and rolling arrival payloads keep their existing publication rules.

[reasoned.json](reasoned.json) was frozen before execution. Eighteen cases
cover initial application, repeated application, held values, revalidation
after invalidation of a seeded valid endpoint, and same-cycle set cancellation. Each reference engine
ran in three fresh processes. The recorded identities fingerprint the installed
packages and native binaries; they do not establish a Git source revision.

| Public reference behavior | Python | C++ |
|---|---|---|
| Initial empty set or map | First application ticks, repeat silent | Same |
| Initial empty fixed list, struct or growing list | No tick; remains invalid | Same |
| Initial zero-size fixed list | No tick; remains invalid | Public authoring error |
| Initial empty struct | No tick; remains invalid | Same |
| Empty application after a populated value | Silent; held value retained | Same |
| Empty after invalidating a set or map | Source revalidates and ticks; valid pass-through destination stays silent | Same |
| Empty after invalidating a fixed list or struct | Source remains invalid | Same |
| Add then remove the same set member in each cycle | Producer ticks twice; pass-through records only the first empty application | Same |
| Structural tuple | No public `TST` authoring marker | Same |
| Populate a growing list through the tested public adapter | Authoring error | Supported |

The list and struct initialization/revalidation differences are retained as
differences from the accepted rule. Unsupported tuple authoring is not evidence
about atomic tuples or compiled HGL structural tuples. The growing-list Python
error is not converted to silence. These are public reference observations,
not validation of the new compiler implementations.

[observed.json](observed.json) retains producer and endpoint metadata,
notifications, raw eval results, input horizons, independent dense adaptation,
and every failed or unsupported surface. Empty payloads remain distinct from
absent publications. Historical publication-boundary evidence is unchanged. The initial unseeded
revalidation records are retained in [history/initial-unseeded](history/initial-unseeded/README.md);
the active fixed-list and struct cases seed a valid endpoint before invalidating it.

```sh
python3 runtime/validation/empty_delta_validity/observe.py \
  --python <python-reference> --cpp <cpp-reference> --output <new-result.json>
python3 runtime/validation/empty_delta_validity/check.py
python3 -m unittest discover -s runtime/validation/empty_delta_validity
```

The checker verifies identities, input hashes, state/publication consistency,
complete notification traces (including invalidations), raw-result presence,
dense horizons and recomputed assessments. Its corruption tests
reject masking a disagreement, inventing a tick, substituting silence for an
empty payload, dropping an unsupported case and changing the reasoning hash.
