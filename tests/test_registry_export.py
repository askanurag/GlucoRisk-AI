import unittest,tempfile
from pathlib import Path
import numpy as np
from healthcare_ai.registry_simulator import make_patient

class TestCase(unittest.TestCase):
    def setUp(self):
        self.raw=make_patient(7)

    def test_behavior(self):
        from healthcare_ai.registry_export import export_registry
        import pandas as pd
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/'features.csv';self.assertEqual(export_registry(p),4800);self.assertEqual(len(pd.read_csv(p)),4800)

if __name__=="__main__":unittest.main()
