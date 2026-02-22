import unittest,tempfile
from pathlib import Path
import numpy as np
from healthcare_ai.registry_simulator import make_patient

class TestCase(unittest.TestCase):
    def setUp(self):
        self.raw=make_patient(7)

    def test_behavior(self):
        import subprocess,sys,os
        from healthcare_ai.paths import ROOT
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/'export.csv';result=subprocess.run([sys.executable,'-m','healthcare_ai.registry_cli','export','--output',str(p)],env=dict(os.environ,PYTHONPATH=str(ROOT/'src')),capture_output=True,text=True);self.assertEqual(result.returncode,0,result.stderr);self.assertTrue(p.exists())

if __name__=="__main__":unittest.main()
