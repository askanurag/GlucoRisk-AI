import unittest,tempfile
from pathlib import Path
import numpy as np
from healthcare_ai.registry_simulator import make_patient

class TestCase(unittest.TestCase):
    def setUp(self):
        self.raw=make_patient(7)

    def test_behavior(self):
        from healthcare_ai.registry_quality import registry_quality
        r=registry_quality(self.raw);self.assertEqual(r['patients'],1);self.assertEqual(r['encounters'],6);self.assertEqual(r['missing_numeric'],0)

if __name__=="__main__":unittest.main()
