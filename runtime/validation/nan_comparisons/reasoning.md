# NaN comparison hypotheses before observation

This audit tests existing runtime operators, not new HGL constructors or a
chosen language rule. A NaN supplied by the Python test harness is only a
reference-runtime fixture; it does not admit `nan` or `float("nan")` source
syntax. No NaN payload bits, sign, quiet/signaling distinction or bit-pattern
identity is asserted.

For f64 NaN compared with itself or a finite operand, the conventional IEEE
candidate expectation is false for equality and every ordered comparison,
and true for inequality. Test both operand orders. The independently supplied
NaN must still be a present valid publication; false is a comparison result,
not a missing publication. Equal finite inputs provide positive controls:
eq/le/ge true and ne/lt/gt false. A trailing silent position remains silent.

The existing HGL OP-10 reference states ln(negative) produces NaN. Freeze that
expectation for ln(-1.0); ln(1.0) must produce present zero. If a reference
instead raises a domain error, retain the error. Also compare ln(-1.0) with
itself using the existing graph operators, keeping any upstream error distinct
from a false/true comparator result.

Probe registered graph operators through public eval_node on each genuine
engine; do not substitute Python equality for native operator execution.
math.isnan in the observer is only an external classification of captured
float data. A source-level is_nan/isnan primitive is separately discovered and,
if exposed, executed; absence is a capability limit, not implemented semantics.

An eventual source test could use `value != value` to recognize NaN only after
that comparison rule is deliberately specified. No native float bit identity,
JSON NaN token, tolerant-equality shortcut or invented constructor is needed.
