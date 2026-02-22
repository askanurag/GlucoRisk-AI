import unittest,tempfile
from pathlib import Path
import numpy as np
from healthcare_ai.registry_simulator import make_patient

class TestCase(unittest.TestCase):
    def setUp(self):
        self.raw=make_patient(7)

    def test_behavior(self):
        from healthcare_ai.registry_audit import registry_fingerprint
        r=registry_fingerprint();self.assertEqual(r['file_count'],800);self.assertEqual(len(r['sha256_manifest']),64)

if __name__=="__main__":unittest.main()
