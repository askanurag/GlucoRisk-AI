"""Illustrative probability bins; not medically justified risk categories."""
import numpy as np
import pandas as pd
from .probability_checks import check_probabilities
def risk_bands(p,edges=(.1,.3)):
    p=check_probabilities(p)
    if len(edges)!=2 or not 0<edges[0]<edges[1]<1:raise ValueError('Two increasing probability cutoffs required')
    return np.where(p<edges[0],'low_demo',np.where(p<edges[1],'middle_demo','high_demo'))
def band_summary(y,p):
    f=pd.DataFrame({'y':y,'p':p,'band':risk_bands(p)})
    return f.groupby('band').agg(n=('y','size'),observed_fraction=('y','mean'),mean_prediction=('p','mean')).reset_index()
