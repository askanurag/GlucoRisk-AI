"""Patient registry validation, including follow-up and snapshot availability."""
import pandas as pd
import numpy as np
from .domain_contract import validate_recording
from .settings import FEATURES
def validate_patient(frame):
    validate_recording(frame)
    if frame.patient_id.nunique()!=1:raise ValueError('One patient per registry file')
    dates=pd.to_datetime(frame.discharge_time)
    if dates.duplicated().any() or not dates.is_monotonic_increasing:raise ValueError('Unique chronological discharge snapshots required')
    if (pd.to_datetime(frame.followup_end)<dates).any():raise ValueError('Follow-up precedes discharge')
    if (frame[FEATURES]<0).any().any():raise ValueError('Nonnegative simulator features required')
    if not {'encounter_id','site'}<=set(frame):raise ValueError('Encounter ID and site required')
    if frame.encounter_id.duplicated().any():raise ValueError('Duplicate encounter IDs')
    return frame
