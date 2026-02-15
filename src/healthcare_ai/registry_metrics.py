"""Encounter-weighted and patient-averaged descriptive performance."""
import numpy as np
import pandas as pd
from .metrics import evaluate
from .cluster_bootstrap import cluster_auc
def registry_metrics(y,p,patient_ids,threshold=.5):
    y,p,g=np.asarray(y),np.asarray(p),np.asarray(patient_ids)
    if not len(y)==len(p)==len(g):raise ValueError('Aligned arrays required')
    per_patient=pd.DataFrame({'patient':g,'error':(y-p)**2}).groupby('patient').error.mean()
    return {'encounter_metrics':evaluate(y,p,threshold),'patient_mean_brier':float(per_patient.mean()),
      'patient_cluster_auc_interval':cluster_auc(y,p,g,repetitions=100)}
