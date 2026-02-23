import unittest,tempfile
from pathlib import Path
import numpy as np
from healthcare_ai.registry_simulator import make_patient

class TestCase(unittest.TestCase):
    def setUp(self):
        self.raw=make_patient(7)

    def test_behavior(self):
        from healthcare_ai.registry_loading import load_registry
        from healthcare_ai.registry_labels import labeled_registry
        from healthcare_ai.registry_temporal import temporal_patient_split
        from healthcare_ai.leakage import assert_disjoint
        import pandas as pd
        a,b=temporal_patient_split(labeled_registry(load_registry()));self.assertTrue(assert_disjoint(a,b));self.assertLessEqual(pd.to_datetime(a.discharge_time).max(),pd.Timestamp('2022-07-01'));self.assertGreater(pd.to_datetime(b.discharge_time).min(),pd.Timestamp('2022-07-01'))

if __name__=="__main__":unittest.main()
