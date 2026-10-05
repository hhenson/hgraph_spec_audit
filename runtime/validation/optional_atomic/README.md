# Optional fields in complete atomic structs

Six fresh processes (three per runtime) execute 54 eval calls over three
Python-authored CompoundScalar shapes. Both engines preserve unset versus
present zero, empty list versus unset, and a present struct whose optional
fields are all unset. Replacing a complete snapshot with an unset field does
not retain its previous payload. Empty/all-silent raw recorder results remain
`None`; the audit does not rewrite them into dense HGL results.

The intended owning-value rule requires present nested payloads to be retained
independently. Native captures preserve the original optional list after its
source is extended. Historical Python captures alias that list and change;
`observed.json` and the checker preserve this disagreement.

The default-`None` field on an `int` annotation is observed separately from an
explicit Python `Optional[int]` annotation. This adds no HGL nullable type
syntax and makes no claim about structural field clearing, recursive types,
abstract families, whole-output invalidation or read-only field access.

Run `observe.py --python <python-runtime> --cpp <native-runtime> --output <new-json>`
for fresh evidence. `check.py` and `python -m unittest discover -s
runtime/validation/optional_atomic` validate the recorded evidence and reject
lost presence, zero/empty substitution and hidden aliases. Engine/source/binary
fingerprints identify the measured runtimes; HGL compiler execution is separate.
