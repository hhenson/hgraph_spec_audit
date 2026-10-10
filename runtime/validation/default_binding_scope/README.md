# Conventional default binding and phase

Reasoned cases were committed before measurement at
`37f4094a8ed7fb80ff807d1754ff922e4ed15ed3`. Three fresh isolated Python
processes, three fresh ordinary C++ executions and three syntax-only compiler
processes per rejected case agree with those cases. The Python interpreter is
the public-reference environment, fingerprinted before and after measurement;
the ordinary C++ probe records compiler, source and binary fingerprints.
No HGL compiler or native hgraph SDK is executed.

| Case | Python observation | C++ observation |
|---|---|---|
| Enclosing `seed` changes 7 to 9 after definition; omitted/explicit second argument | `[7,5]` | `[9,5]` |
| Default reads earlier formal parameter | Definition raises `NameError` | Source rejected |
| Earlier formal shadows same-spelled outer `first=11` | Default captures outer 11 | Source rejected: parameter hides outer name |
| `sizeof` of earlier formal in default | No corresponding Python fixture | Accepted unevaluated control |
| Function default uses template `N` with 7 and 9 specializations | No corresponding Python fixture | `[7,9]` |
| Construct pair with `first=99`; second initialized from earlier field | `[99,7]` from class-namespace constant | `[99,99]` from constructed instance member |
| Effectful default helper, two omitted calls | `[1,1,1]`: captured once | `[1,2,2]`: evaluated per omitted call |

Python's [default-argument documentation](https://docs.python.org/3.14/tutorial/controlflow.html#default-argument-values)
defines evaluation in the defining scope at function definition, once.
C++ [default arguments, paragraphs 5 and 9](https://eel.is/c++draft/dcl.fct.default)
distinguish declaration lookup, earlier parameter scope, potentially evaluated
parameter exclusion, template lookup and per-omission execution. C++ template
values, ordinary parameters and default member initializers are separate
surfaces; none supplies an implicit HGL rule.

The HGL choice under review keeps defaults in the enclosing declaration binding
closure plus existing generic context, excluding instance fields and formal
argument values. Existing constant/cold phase, specialization and owning
retention rules continue to apply. This is an explicit HGL choice, not an
assertion that Python and C++ defaults have identical semantics. It adds no
numeric generic reification or generic-parameter-default syntax.

Run `python check.py` and `python -m unittest discover -s . -p test_check.py`
for recorded-evidence checks. Measurement takes explicit interpreter/compiler
paths and new isolated build/evidence destinations; private host paths are not
tracked.
