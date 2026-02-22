import unittest,tempfile
from pathlib import Path
import numpy as np
from healthcare_ai.registry_simulator import make_patient

class TestCase(unittest.TestCase):
    def setUp(self):
        self.raw=make_patient(7)

    def test_behavior(self):
        from healthcare_ai.registry_riskbands import risk_bands
        self.assertEqual(list(risk_bands([0,.1,.3,1])),['low_demo','middle_demo','high_demo','high_demo'])
        with self.assertRaises(ValueError):risk_bands([.5],(.4,.2))

if __name__=="__main__":unittest.main()
