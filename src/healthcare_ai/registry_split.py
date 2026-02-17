"""Group-random patient separation; repeated encounters cannot cross splits."""
from .splits import split
from .leakage import assert_disjoint
def registry_partitions(frame,seed=42):
    train,validation,test=split(frame,seed);assert_disjoint(train,validation,test)
    return train,validation,test
