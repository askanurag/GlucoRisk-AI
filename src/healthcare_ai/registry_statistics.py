"""Endpoint prevalence summaries by site and encounter order."""
from .settings import TARGET
def grouped_prevalence(frame,group='site'):
    if group not in frame:raise ValueError('Unknown grouping column')
    return frame.groupby(group)[TARGET].agg(['size','mean','sum']).reset_index()
def encounter_order(frame):
    f=frame.sort_values(['patient_id','discharge_time']).copy();f['encounter_order']=f.groupby('patient_id').cumcount()+1;return f
