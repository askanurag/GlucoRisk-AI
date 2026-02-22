import unittest,tempfile
from pathlib import Path
import numpy as np
from healthcare_ai.registry_simulator import make_patient

class TestCase(unittest.TestCase):
    def setUp(self):
        self.raw=make_patient(7)

    def test_behavior(self):
        from healthcare_ai.registry_loading import load_registry,patient_paths
        f=load_registry();self.assertEqual(len(patient_paths()),800);self.assertEqual(f.patient_id.nunique(),800);self.assertEqual(len(f),4800)

if __name__=="__main__":unittest.main()
