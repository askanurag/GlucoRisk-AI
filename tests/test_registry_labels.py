import unittest,tempfile
from pathlib import Path
import numpy as np
from healthcare_ai.registry_simulator import make_patient

class TestCase(unittest.TestCase):
    def setUp(self):
        self.raw=make_patient(7)

    def test_behavior(self):
        from healthcare_ai.registry_labels import labeled_registry
        from healthcare_ai.settings import TARGET
        import pandas as pd
        f=self.raw.copy();dis=pd.Timestamp(f.loc[0,'discharge_time']);f.loc[0,'return_time']=(dis+pd.Timedelta(days=30)).isoformat();self.assertEqual(labeled_registry(f,30).loc[0,TARGET],1);self.assertEqual(labeled_registry(f,7).loc[0,TARGET],0)
        f.loc[0,'return_time']='';f.loc[0,'followup_end']=(dis+pd.Timedelta(days=5)).isoformat()
        with self.assertRaises(ValueError):labeled_registry(f,30)

if __name__=="__main__":unittest.main()
