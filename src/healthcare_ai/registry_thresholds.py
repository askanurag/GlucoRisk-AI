"""Select an educational threshold targeting validation sensitivity."""
import numpy as np
from .metrics import evaluate
def threshold_for_sensitivity(y,p,target=.8):
    if not 0<target<=1 or 1 not in set(y):raise ValueError('Valid target and positive labels required')
    candidates=[]
    for t in np.round(np.linspace(0,1,101),2):
        r=evaluate(y,np.asarray(p),float(t))
        if r['sensitivity']>=target:candidates.append(float(t))
    return max(candidates)
