"""Assess the frozen traces plus the separately documented error contract."""
import json


def assess(observations, cases, engine, contract):
    result = {}
    for name, expected in cases.items():
        observed = observations[name]
        matches = all(json.dumps(observed.get(k), sort_keys=True) == json.dumps(v, sort_keys=True)
                      for k, v in expected.items())
        if name == 'duplicate_due':
            expected_error = contract[name][engine]
            lines = observed.get('error_message', '').splitlines()
            index = expected_error['line_index']
            matches = (matches and observed.get('error_type') == expected_error['error_type']
                       and len(lines) > index and lines[index] == expected_error['diagnostic_line'])
        result[name] = 'match' if matches else 'divergence'
    return result
