"""Registry-level patient, encounter and observation summaries."""
import pandas as pd
from .settings import FEATURES
def registry_quality(raw):
    per_patient=raw.groupby('patient_id').size()
    return {'patients':int(raw.patient_id.nunique()),'encounters':len(raw),'sites':raw.site.value_counts().to_dict(),
      'encounters_per_patient_min':int(per_patient.min()),'encounters_per_patient_max':int(per_patient.max()),
      'missing_numeric':int(raw[FEATURES].isna().sum().sum()),'first_discharge':str(pd.to_datetime(raw.discharge_time).min().date()),
      'last_discharge':str(pd.to_datetime(raw.discharge_time).max().date())}
