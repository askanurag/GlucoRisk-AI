import unittest,tempfile
from pathlib import Path
import numpy as np
from healthcare_ai.registry_simulator import make_patient

class TestCase(unittest.TestCase):
    def setUp(self):
        self.raw=make_patient(7)

    def test_behavior(self):
        from healthcare_ai.registry_training import train_registry
        from healthcare_ai.registry_loading import load_registry
        from healthcare_ai.registry_labels import labeled_registry
        from healthcare_ai.registry_split import registry_partitions
        from healthcare_ai.registry_explain import explain_registry
        b,_=train_registry(include_holdout=False);_,v,_=registry_partitions(labeled_registry(load_registry()));r=explain_registry(b,v);self.assertEqual(len(r),6)

if __name__=="__main__":unittest.main()
