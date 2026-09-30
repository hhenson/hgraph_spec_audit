# Released reference audit

Wiring cases repeated three times per runtime against hgraph 0.5.42 (Python)
and 0.8.30 (C++). The runtime assessment is identical to the earlier recorded
comparison: 40 fields match both, one matches C++, four match Python, and four
match neither. The four existing disagreements retain the previously recorded
rules and decisions; this extraction changes no expectation.

The HGL front-end rows in `assessment.json` are copied historical evidence,
not a new compiler run. `provenance.json` identifies the runtime measurement
and expected-trace hash. Reproduce with `tools/compare.py` and the pinned
environments; choose a new output directory for each run.

The archived `reasoned.json` preserves the exact expectations identified by
`provenance.json`. Validation uses that snapshot when reproducing this
release assessment, independently of later specification rulings.
