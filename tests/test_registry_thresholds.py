import unittest,tempfile
from pathlib import Path
import numpy as np
from healthcare_ai.registry_simulator import make_patient

class TestCase(unittest.TestCase):
    def setUp(self):
        self.raw=make_patient(7)

    def test_behavior(self):
        from healthcare_ai.registry_thresholds import threshold_for_sensitivity
        t=threshold_for_sensitivity(np.array([0,0,1,1]),np.array([.1,.2,.7,.9]),1);self.assertAlmostEqual(t,.7)

if __name__=="__main__":unittest.main()
