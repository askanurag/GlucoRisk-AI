"""120 reproducibility configurations: 6 models x 5 seeds x 4 horizons."""
import json
from .paths import ROOT
from .models import NAMES
from .registry_training import train_registry
def registry_configs():return sorted((ROOT/'configs/registry').glob('*.json'))
def read_registry_config(path):
    cfg=json.loads(path.read_text())
    if cfg['model'] not in NAMES or cfg['horizon_days'] not in [7,14,30,45] or not isinstance(cfg['seed'],int):raise ValueError('Invalid registry configuration')
    return cfg
def run_registry_grid(limit=None):
    results=[]
    for path in registry_configs()[:limit]:
        cfg=read_registry_config(path);_,report=train_registry(cfg['model'],cfg['seed'],cfg['horizon_days'],include_holdout=False)
        results.append({'config':path.name,'validation':report['validation']})
    return results
