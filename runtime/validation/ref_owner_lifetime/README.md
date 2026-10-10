# Reference ownership and scalar capability observations

Reasoned traces were frozen before measurement. Public Python and current
C++ wheel probes run in three fresh processes; the direct C++ probe builds
against a copied installed SDK and also runs in three fresh processes. Source,
package, binary, compiler and SDK fingerprints identify measured artifacts;
installed versions alone do not establish source revisions. All recorded
checker assertions preserve observed divergences rather than silently making
implementation behavior the required result.

| Case | Reasoned result | Observed result |
|---|---|---|
| Save reference to branch-owned producer; branch stops in cycle 3 | `[7, 8, 8, null, null, null]`; logical expiry starts next cycle | C++ public/native `[7, 8, 8, 8, null, null]`; target stays readable until child storage is reused. Python records first three observations then raises `AttributeError`. |
| Save reference through stopped relay to a surviving outer input | `[7, 8, 20, 21, 9, 10]` | Matches both public runtimes and native C++. |
| Alias versus distinct equal-valued endpoints | Same endpoint equals; distinct endpoints differ | Matches both public runtimes and native C++; comparison does not read target values. |
| Boolean scalar capabilities | Equal Boolean values have equal hashes; `false < true` | Matches Python ordinary values and the native C++ scalar operations. Public C++ interpreter Boolean operations are Python ordinary operations, not a second native comparison. |

The owner-expiry expectation follows TS-23's dictionary-child timing together
with GRF-25's logical finalization and the rule that references do not prolong
target lifetime. Generalizing the explicit timing to stopped nested endpoint
owners requires a concise spec clarification. This audit does not claim that
conditional HGL tests already execute or conform. The outer-owner control
shows that stopping a forwarding relay must not invalidate a surviving target.

The captured reference output remains designation-valid after the target
expires; the followed ordinary input becomes invalid. Independent step ticks
separate those observations and allow silence to be checked.

Run the evidence-only checker with `python check.py`; run its corruption tests
with `python -m unittest discover -s . -p test_check.py`. Measurement scripts
require independent interpreter paths or an installed SDK/binary, provided
through command arguments; private host paths are not tracked.
