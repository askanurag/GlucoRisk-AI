"""Hold out later-entering patients and purge training records after cutoff."""
import pandas as pd
from .leakage import assert_disjoint
def temporal_patient_split(frame,cutoff='2022-07-01'):
    cutoff=pd.Timestamp(cutoff);times=pd.to_datetime(frame.discharge_time)
    first=frame.assign(_time=times).groupby('patient_id')._time.min();early=set(first[first<=cutoff].index)
    train=frame[frame.patient_id.isin(early)&(times<=cutoff)].copy()
    test=frame[~frame.patient_id.isin(early)&(times>cutoff)].copy()
    if len(train)==0 or len(test)==0:raise ValueError('Cutoff yields an empty partition')
    assert_disjoint(train,test);return train,test
