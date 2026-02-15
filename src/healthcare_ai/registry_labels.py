"""Observed return within a configurable horizon, with censoring checks."""
import pandas as pd
import numpy as np
from .registry_features import snapshot_features
from .settings import TARGET
def labeled_registry(raw,horizon_days=30):
    if not isinstance(horizon_days,int) or horizon_days<1:raise ValueError('Positive integer horizon required')
    discharge=pd.to_datetime(raw.discharge_time);end=pd.to_datetime(raw.followup_end)
    event=pd.to_datetime(raw.return_time.replace('',pd.NaT),errors='raise')
    if ((event<=discharge)&event.notna()).any():raise ValueError('Returns must follow discharge')
    positive=event.notna()&(event<=end)&(event<=discharge+pd.Timedelta(days=horizon_days))
    censored=(~positive)&(end<discharge+pd.Timedelta(days=horizon_days))
    if censored.any():raise ValueError('Censored negative outcomes are not permitted')
    out=snapshot_features(raw);out[TARGET]=positive.astype(int).to_numpy();return out
