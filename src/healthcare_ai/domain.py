import numpy as np
def interaction_features(frame):
    out=frame.copy();out['bmi_glucose_interaction']=out.bmi*out.glucose
    out['activity_per_sleep_hour']=out.activity_minutes/out.sleep_hours.clip(lower=1)
    return out
def simulate_glucose_trace(hours=24,seed=42):
    rng=np.random.default_rng(seed);t=np.linspace(0,hours,int(hours*12))
    values=95+8*np.sin(t*2*np.pi/24)+rng.normal(0,3,len(t))
    for meal in [8,13,19]:values+=35*np.exp(-.5*((t-meal)/.7)**2)
    return t,values
def trace_summary(values):
    return {'mean':float(np.mean(values)),'std':float(np.std(values)),'coefficient_of_variation':float(np.std(values)/np.mean(values))}
