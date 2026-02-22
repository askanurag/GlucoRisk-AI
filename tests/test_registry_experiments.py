import unittest,tempfile
from pathlib import Path
import numpy as np
from healthcare_ai.registry_simulator import make_patient

class TestCase(unittest.TestCase):
    def setUp(self):
        self.raw=make_patient(7)

    def test_behavior(self):
        from healthcare_ai.registry_experiments import registry_configs,read_registry_config
        paths=registry_configs();self.assertEqual(len(paths),120);keys={(c['model'],c['seed'],c['horizon_days']) for c in map(read_registry_config,paths)};self.assertEqual(len(keys),120)

if __name__=="__main__":unittest.main()
