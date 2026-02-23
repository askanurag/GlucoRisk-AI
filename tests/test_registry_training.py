import unittest,tempfile
from pathlib import Path
import numpy as np
from healthcare_ai.registry_simulator import make_patient

class TestCase(unittest.TestCase):
    def setUp(self):
        self.raw=make_patient(7)

    def test_behavior(self):
        from healthcare_ai.registry_training import train_registry
        b,r=train_registry(include_holdout=False);self.assertNotIn('test',r);self.assertFalse(b['metadata']['clinical_validation']);self.assertEqual(r['split_patients']['train'],480)

if __name__=="__main__":unittest.main()
