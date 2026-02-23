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
        from healthcare_ai.registry_statistics import grouped_prevalence,encounter_order
        f=labeled_registry(load_registry());r=grouped_prevalence(f);self.assertEqual(int(r['size'].sum()),4800);o=encounter_order(f);self.assertEqual(int(o.encounter_order.max()),6)

if __name__=="__main__":unittest.main()
