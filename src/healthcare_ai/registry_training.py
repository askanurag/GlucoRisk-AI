"""Fit only training patients; select threshold only with validation labels."""
from .registry_loading import load_registry
from .registry_labels import labeled_registry
from .registry_split import registry_partitions
from .registry_metrics import registry_metrics
from .pipeline import build
from .thresholds import select_threshold
from .audit import provenance
from .settings import FEATURES,TARGET
from .metrics import evaluate
from .io import write_json
from .persistence import save_bundle
from pathlib import Path
def train_registry(model_name='logistic',seed=42,horizon_days=30,output=None,include_holdout=True):
    frame=labeled_registry(load_registry(),horizon_days);train,val,test=registry_partitions(frame,seed)
    model=build(model_name,seed).fit(train[FEATURES],train[TARGET]);pv=model.predict_proba(val[FEATURES])[:,1]
    threshold=select_threshold(val[TARGET],pv);metadata=provenance(frame,seed)
    report={'model':model_name,'horizon_days':horizon_days,'seed':seed,'validation':evaluate(val[TARGET],pv,threshold),
       'split_patients':{k:int(f.patient_id.nunique()) for k,f in [('train',train),('validation',val),('test',test)]},'metadata':metadata}
    if include_holdout:report['test']=registry_metrics(test[TARGET],model.predict_proba(test[FEATURES])[:,1],test.patient_id,threshold)
    bundle={'model':model,'threshold':threshold,'metadata':dict(metadata,horizon_days=horizon_days)}
    if output:
        output=Path(output);save_bundle(output/'registry_model.joblib',model,threshold,bundle['metadata']);write_json(output/'registry_metrics.json',report)
    return bundle,report
