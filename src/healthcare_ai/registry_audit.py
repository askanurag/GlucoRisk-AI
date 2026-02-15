"""Record a registry fingerprint and patient leakage checks."""
import hashlib,json
from .data_fingerprint import manifest
from .registry_loading import patient_paths
from .leakage import assert_disjoint
def registry_fingerprint():
    files=manifest(patient_paths());digest=hashlib.sha256(json.dumps(files,sort_keys=True).encode()).hexdigest()
    return {'sha256_manifest':digest,'file_count':len(files),'total_bytes':sum(f['bytes'] for f in files)}
def audit_partitions(train,val,test):
    assert_disjoint(train,val,test)
    return {'patients_disjoint':True,'rows':{k:len(f) for k,f in [('train',train),('validation',val),('test',test)]}}
