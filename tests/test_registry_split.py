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
        from healthcare_ai.registry_split import registry_partitions
        a,b,c=registry_partitions(labeled_registry(load_registry()));self.assertEqual(a.patient_id.nunique(),480);self.assertEqual(b.patient_id.nunique(),160);self.assertEqual(c.patient_id.nunique(),160)

if __name__=="__main__":unittest.main()
