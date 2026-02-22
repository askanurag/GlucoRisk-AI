import unittest,tempfile
from pathlib import Path
import numpy as np
from healthcare_ai.registry_simulator import make_patient

class TestCase(unittest.TestCase):
    def setUp(self):
        self.raw=make_patient(7)

    def test_behavior(self):
        from healthcare_ai.registry_training import train_registry
        from healthcare_ai.registry_predict import predict_registry
        b,_=train_registry(include_holdout=False);f=self.raw.drop(columns=['return_time','followup_end']);p=predict_registry(b,f,2);self.assertEqual(len(p),6);self.assertTrue(p.patient_id.eq(self.raw.patient_id.iloc[0]).all())

if __name__=="__main__":unittest.main()
