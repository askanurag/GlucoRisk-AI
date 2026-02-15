"""Inference from raw registry snapshots; no outcome columns required."""
from .registry_features import snapshot_features
from .batch_inference import predict_batches
def predict_registry(bundle,raw,batch_size=128):return predict_batches(bundle,snapshot_features(raw),batch_size)
