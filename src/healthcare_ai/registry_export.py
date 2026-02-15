"""Export derived feature tables to an explicitly chosen output folder."""
from pathlib import Path
from .registry_loading import load_registry
from .registry_labels import labeled_registry
def export_registry(path,horizon_days=30):
    p=Path(path);p.parent.mkdir(parents=True,exist_ok=True);frame=labeled_registry(load_registry(),horizon_days)
    frame.to_csv(p,index=False);return len(frame)
