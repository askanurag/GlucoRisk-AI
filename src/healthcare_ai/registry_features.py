"""Only numeric discharge-available predictors enter model inputs."""
import pandas as pd
from .settings import FEATURES
def snapshot_features(raw):
    out=raw[['patient_id','encounter_id','site','discharge_time']+FEATURES].copy()
    if (pd.to_datetime(raw.feature_time)>pd.to_datetime(raw.discharge_time)).any():raise ValueError('Post-discharge feature leakage')
    return out
