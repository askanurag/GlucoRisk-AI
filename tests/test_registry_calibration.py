import unittest,tempfile
from pathlib import Path
import numpy as np
from healthcare_ai.registry_simulator import make_patient

class TestCase(unittest.TestCase):
    def setUp(self):
        self.raw=make_patient(7)

    def test_behavior(self):
        from healthcare_ai.registry_calibration import fit_calibrated
        from healthcare_ai.registry_loading import load_registry
        from healthcare_ai.registry_labels import labeled_registry
        from healthcare_ai.registry_split import registry_partitions
        from healthcare_ai.settings import FEATURES,TARGET
        t,v,_=registry_partitions(labeled_registry(load_registry()));m=fit_calibrated(t);p=m.predict_proba(v[FEATURES]);self.assertEqual(p.shape,(960,2));np.testing.assert_allclose(p.sum(axis=1),1)

if __name__=="__main__":unittest.main()
