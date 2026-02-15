"""Load 800 patient shards; cache a validated snapshot within one process."""
from pathlib import Path
from functools import lru_cache
import pandas as pd
from .paths import ROOT
from .registry_schema import validate_patient
def patient_paths(directory=None):return sorted(Path(directory or ROOT/'data/registry').glob('patient_*.csv'))
@lru_cache(maxsize=2)
def _snapshot(signature):
    tables=[]
    for path,_,_ in signature:tables.append(validate_patient(pd.read_csv(path,keep_default_na=False)))
    if not tables:raise ValueError('No patient registry files found')
    result=pd.concat(tables,ignore_index=True)
    if result.encounter_id.duplicated().any():raise ValueError('Duplicate encounter identifiers across shards')
    return result
def load_registry(directory=None,reload=False):
    if reload:_snapshot.cache_clear()
    paths=patient_paths(directory);signature=tuple((str(p),p.stat().st_mtime_ns,p.stat().st_size) for p in paths)
    return _snapshot(signature).copy()
