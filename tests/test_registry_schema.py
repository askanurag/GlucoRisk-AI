import unittest,tempfile
from pathlib import Path
import numpy as np
from healthcare_ai.registry_simulator import make_patient

class TestCase(unittest.TestCase):
    def setUp(self):
        self.raw=make_patient(7)

    def test_behavior(self):
        from healthcare_ai.registry_schema import validate_patient
        self.assertEqual(len(validate_patient(self.raw)),6)
        f=self.raw.copy();f.loc[0,'feature_time']='2040-01-01'
        with self.assertRaises(ValueError):validate_patient(f)

if __name__=="__main__":unittest.main()
