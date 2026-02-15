"""Training-group cross-fitted sigmoid calibration; never fit on holdout."""
from sklearn.calibration import CalibratedClassifierCV
from sklearn.model_selection import GroupKFold
from .pipeline import build
from .settings import FEATURES,TARGET
def fit_calibrated(train,seed=42):
    cv=list(GroupKFold(3).split(train,train[TARGET],train.patient_id))
    for fit_ix,cal_ix in cv:
        if len(set(train.iloc[fit_ix][TARGET]))!=2 or len(set(train.iloc[cal_ix][TARGET]))!=2:raise ValueError('Both classes required in calibration folds')
    model=CalibratedClassifierCV(build(seed=seed),method='sigmoid',cv=cv)
    return model.fit(train[FEATURES],train[TARGET])
