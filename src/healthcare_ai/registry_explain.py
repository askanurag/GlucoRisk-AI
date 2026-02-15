"""Validation permutation importance with patient-separated development data."""
from .importance import feature_importance
from .settings import FEATURES,TARGET
def explain_registry(bundle,validation,seed=42):return feature_importance(bundle['model'],validation[FEATURES],validation[TARGET],seed)
