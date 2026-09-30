"""Bind current evidence to the unchanged source corpus and audit adapters."""
import hashlib
import json
from pathlib import Path
import sys
import unittest

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from shared_cases import encode, literal, read


class Evidence(unittest.TestCase):
    def test_current_shared_cases_and_all_results(self):
        cases, hashes = read(HERE.parents[1] / 'stdlib/hgl/hgraph')
        self.assertEqual(len(cases),84)
        self.assertEqual(len({(c['module'],c['name']) for c in cases}),45)
        for engine, failures in [('python',[77]),('cpp',[])]:
            report = json.loads((HERE / f'{engine}.json').read_text())
            self.assertEqual(report['sources'],hashes)
            self.assertEqual(report['harness_sha256'],hashlib.sha256((HERE/'replay.py').read_bytes()).hexdigest())
            self.assertEqual(report['reader_sha256'],hashlib.sha256((HERE/'shared_cases.py').read_bytes()).hexdigest())
            self.assertEqual(len(report['cases']),len(cases))
            self.assertEqual([r['index'] for r in report['cases'] if not r['matches']],failures)
            for case,row in zip(cases,report['cases']):
                self.assertEqual(row['function'],case['function'])
                self.assertEqual(row['expected'],json.loads(json.dumps(case['expected'],default=encode)))
                self.assertEqual(row['matches'],row['observed']==row['expected'])
        cpp = json.loads((HERE/'hgl-cpp.json').read_text())
        self.assertEqual(cpp['sources'],hashes)
        shared = {c['name'] for c in cases}
        observed = {t['name'] for g in cpp['groups'] for t in g['tests'] if t['result']=='ok'}
        self.assertTrue(shared <= observed)
        self.assertTrue(all(g['passed'] for g in cpp['groups']))
        self.assertEqual(cpp['tests'],47)

    def test_reader_handles_silence_calendar_and_negative_duration(self):
        self.assertEqual(literal('[_, -2, 1.5, true, "a,b"]'),[None,-2,1.5,True,'a,b'])
        self.assertEqual(literal('0us - 1us').days,-1)
        self.assertEqual(literal('@1969-12-31T23:59Z').year,1969)


if __name__ == '__main__': unittest.main()
