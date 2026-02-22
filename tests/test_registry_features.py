import unittest,tempfile
from pathlib import Path
import numpy as np
from healthcare_ai.registry_simulator import make_patient

class TestCase(unittest.TestCase):
    def setUp(self):
        self.raw=make_patient(7)

    def test_behavior(self):
        from healthcare_ai.registry_features import snapshot_features
        f=snapshot_features(self.raw);self.assertNotIn('return_time',f);self.assertNotIn('followup_end',f);self.assertNotIn('feature_time',f)

if __name__=="__main__":unittest.main()
