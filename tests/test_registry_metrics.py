import unittest,tempfile
from pathlib import Path
import numpy as np
from healthcare_ai.registry_simulator import make_patient

class TestCase(unittest.TestCase):
    def setUp(self):
        self.raw=make_patient(7)

    def test_behavior(self):
        from healthcare_ai.registry_metrics import registry_metrics
        r=registry_metrics([0,1]*5,[.1,.9]*5,np.repeat(np.arange(5),2));self.assertAlmostEqual(r['patient_mean_brier'],.01);self.assertEqual(r['encounter_metrics']['auroc'],1)

if __name__=="__main__":unittest.main()
