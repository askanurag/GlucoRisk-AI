"""Reproducible longitudinal synthetic patients; no real health records."""
import numpy as np
import pandas as pd
def make_patient(patient_number,encounters=6):
    if patient_number<1 or encounters<2:raise ValueError('Positive patient number and at least two encounters required')
    rng=np.random.default_rng(10000+patient_number);rows=[];age=int(rng.integers(25,85));burden=int(rng.integers(0,5))
    first=pd.Timestamp('2020-01-01')+pd.Timedelta(days=int(rng.integers(0,1200)));site=['SIM-A','SIM-B','SIM-C'][patient_number%3]
    for episode in range(encounters):
        stay=int(rng.integers(1,12));prior=episode;comorb=max(0,burden+int(rng.integers(-1,2)));meds=int(rng.integers(1,13));delay=int(rng.integers(1,23))
        admission=first+pd.Timedelta(days=episode*90);discharge=admission+pd.Timedelta(days=stay)
        p=1/(1+np.exp(-(-3+.35*prior+.42*comorb+.04*delay+.012*(age-50))))
        returned=bool(rng.random()<p);event=discharge+pd.Timedelta(days=int(rng.integers(1,61))) if returned else pd.NaT
        rows.append({'patient_id':'REG-SYN-%04d'%patient_number,'encounter_id':'REG-%04d-%02d'%(patient_number,episode),'site':site,
         'admission_time':admission.isoformat(),'discharge_time':discharge.isoformat(),'feature_time':discharge.isoformat(),
         'followup_end':(discharge+pd.Timedelta(days=75)).isoformat(),'return_time':event.isoformat() if returned else '',
         'age':age,'length_of_stay':stay,'prior_admissions':prior,'comorbidity_count':comorb,'medication_count':meds,'followup_delay':delay})
    return pd.DataFrame(rows)
