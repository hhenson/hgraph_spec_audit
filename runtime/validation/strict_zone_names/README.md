# Exact timezone names: construction versus provider validation

This bounded follow-up to the [temporal scalar audit](../temporal_scalars/README.md)
uses its own installed-package provenance. The expectations in
[reasoned.json](reasoned.json) precede measurement; [observed.json](observed.json)
records identical results from three fresh processes per probe (30 processes).
No compiler was inspected or modified, and no native build was performed.

| Names | `ZoneId` construction | Ad-hoc JSON decoding | Configured-provider `at_zone` |
|---|---|---|---|
| `UTC`, `Etc/UTC` | Exact spelling retained | Exact spelling retained | Accepted, offset 0 |
| `America/New_York`, `US/Eastern` | Exact spelling retained | Exact spelling retained | Accepted, offset -14400 |
| `utc`, `america/new_york` | Exact spelling retained | Exact spelling retained | Rejected |
| `Etc/Unknown`, `Missing/Zone` | Exact spelling retained | Exact spelling retained | Rejected |

The instant is `2026-09-03T09:30:00`. All four failures are precisely
`ValueError: unknown time-zone identifier`; no UTC fallback is observed.
Accepted zoned values retain the input name. `US/Eastern` does not equal
`America/New_York`, despite their equal offsets at this instant.

Construction and `from_json_builder(ZoneId)` accept all eight strings both
outside a provider context and inside a configured one. Their success does
not establish provider membership or strict provider-validating decoding.
The measured validation operation is `temporal.at_zone`; this audit does not
exercise a separately configurable strict decoder or HGL literal decoding.
All names here are syntactically plausible; malformed-name syntax is outside
this corpus. These finite cases do not establish every TZDB catalog entry.

Historical Python hgraph 0.5.41 lacks `ZoneId` and `ZonedDateTime`; its probe
records availability only. No surrogate Python types or parity claim are
introduced. The native package reports 0.0.0; artifact/source/loaded-library
digests, not the development version string, identify the measured engine.

A separate HGL clarification can require exact, case-sensitive membership in
the configured provider's catalog, retain exact link-name identity and forbid
synthetic unknown-zone fallback. That is a language requirement; the permissive
native constructor and ad-hoc JSON decoder do not define HGL strict decoding.

```sh
python3 runtime/validation/strict_zone_names/observe.py \
  --python /path/to/historical-python/bin/python \
  --cpp /path/to/native/bin/python \
  --output /tmp/new-strict-zone-names.json
python3 runtime/validation/strict_zone_names/check.py
python3 -m unittest discover -s runtime/validation/strict_zone_names
```

The observer refuses overwrite and requires stable repeated results and full
identities. Checks preserve all successes and exact failures, reject invented
Python coverage and validate provenance consistency without authenticating the
wheel independently. The aggregate recorded checker includes this corpus.
