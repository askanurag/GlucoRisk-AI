import unittest,tempfile
from pathlib import Path
import numpy as np
from healthcare_ai.registry_simulator import make_patient

class TestCase(unittest.TestCase):
    def setUp(self):
        self.raw=make_patient(7)

    def test_behavior(self):
        from healthcare_ai.registry_simulator import make_patient
        self.assertTrue(make_patient(1).equals(make_patient(1)));self.assertFalse(make_patient(1).equals(make_patient(2)));self.assertEqual(make_patient(1).patient_id.nunique(),1)

if __name__=="__main__":unittest.main()
