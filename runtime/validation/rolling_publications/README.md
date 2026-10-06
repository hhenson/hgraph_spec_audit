# Rolling arrival publications and readiness

The [rolling contract](https://github.com/hhenson/hgraph_spec/blob/4ab161c83c37268e4293373f175e5e19173573fc/language/docs/design/rolling-publications.md)
states that the delta is the arriving ordinary value. It clarifies all-valid
as the current retained count/span, correcting earlier runtime TS-31 sticky
wording to the existing language definition. The reasoned corpora preceded
their graph measurements; no baseline disagreement was rewritten as a match.

Two artifacts record three fresh identical processes per engine, six eval
attempts per process, 72 total. Historical Python reports 0.5.41; native
reports 0.0.0. Package/source/native-library digests identify actual runtimes.

[observed.json](observed.json) tests direct `TSW[int]` replay into a compute
returning `delta_value` to its own same-shaped output. Native preserves all
arrivals, equal repeats and silence, with raw null empty/all-silent output.
Historical Python's eval harness binds TS[int] to the TSW parameter and fails
with `IncorrectTypeBinding` for every case; this is not runtime parity.

[composed_observed.json](composed_observed.json) independently constructs the
actual public `to_window` operator, then a same-shaped TSW pass-through, then
a scalar recorder node. It records both the original window input and the
pass-through's own output, without substituting custom window logic:

- Native current-span readiness for Max=5us/Min=1us at offsets 0,2,8 is
  false/true/false. Both independently held windows agree and every arrival
  publishes despite being unready. Native tick windows preserve arrivals and
  evictions.
- Native `to_window` with Min=0 reports input readiness false while the
  same-shaped pass-through output and direct-replay window report true. This
  operator discrepancy is preserved, not adopted as the source rule.
- Historical Python tick forwarding fails on its own NumPy delta type:
  `Expected <class 'int'>, got <class 'numpy.int64'>`. The observer does not
  cast or repair the returned delta. The recorded failure preserves class,
  exact type-mismatch cause and application phase; volatile subscriber IDs
  and unused NumPy storage from the exception's object repr are omitted.
- Historical Python positive-duration minimum suppresses the first delta and
  reports all-valid true even when its value is null. It later remains true
  after the long-gap eviction. The second window consequently lacks the
  first arrival. These are explicit disagreements.

Direct native eviction observation exposes one removed scalar (20 after
both older duration entries were evicted). This audit does not infer complete
removed-value coverage or introduce an eviction observation API. It also does
not establish arbitrary payload/structural nesting, timed-input syntax,
idle metadata sampling, exact-age boundary behavior or references.

```sh
python3 runtime/validation/rolling_publications/observe.py \
  --python /path/to/historical-python/bin/python \
  --cpp /path/to/native/bin/python --output /tmp/rolling-direct-fresh.json
python3 runtime/validation/rolling_publications/composed_observe.py \
  --python /path/to/historical-python/bin/python \
  --cpp /path/to/native/bin/python --output /tmp/rolling-composed-fresh.json
python3 runtime/validation/rolling_publications/check.py
python3 -m unittest discover -s runtime/validation/rolling_publications
```

Six tests reject omitted arrivals, invented Python coverage, hidden native
operator differences and a fabricated sticky-readiness result.
