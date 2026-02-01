# Synthetic patient registry report

## Validation completed

```json
{
  "project": "CareReturn-AI",
  "files": 1271,
  "python_files": 148,
  "notebooks": 80,
  "unit_tests_passed": 64,
  "registry_patient_files": 800,
  "registry_patients": 800,
  "registry_encounters": 4800,
  "registry_configs_executed": 120,
  "original_tabular_configs_executed": 30,
  "domain_scenarios_executed": 12,
  "github_actions_workflow_files": 0,
  "notebook_execution": "Sequential Python cell execution with captured stdout and rendered figures; not a Jupyter kernel",
  "clinical_validation": false
}
```

## Registry data audit

```json
{
  "patients": 800,
  "encounters": 4800,
  "sites": {
    "SIM-B": 1602,
    "SIM-C": 1602,
    "SIM-A": 1596
  },
  "encounters_per_patient_min": 6,
  "encounters_per_patient_max": 6,
  "missing_numeric": 0,
  "first_discharge": "2020-01-03",
  "last_discharge": "2024-07-11",
  "fingerprint": {
    "sha256_manifest": "8f48f56ca934b4d86aab49f39997842a8a099a5fa7a683c3c14230131624c07c",
    "file_count": 800,
    "total_bytes": 782504
  }
}
```

## Prespecified logistic baseline

```json
{
  "model": "logistic",
  "horizon_days": 30,
  "seed": 42,
  "validation": {
    "auroc": 0.7055553204992595,
    "average_precision": 0.26726771812040595,
    "brier": 0.12182310193530183,
    "balanced_accuracy": 0.658324518722234,
    "sensitivity": 0.6896551724137931,
    "specificity": 0.6269938650306749,
    "tp": 100,
    "tn": 511,
    "fp": 304,
    "fn": 45,
    "n": 960,
    "threshold": 0.19
  },
  "split_patients": {
    "train": 480,
    "validation": 160,
    "test": 160
  },
  "metadata": {
    "data_sha256": "9b6d5751e97f64233988c87bd23dbaec6dcf3f4a6232da61889e5c56a0b41ecc",
    "seed": 42,
    "python": "3.12.14",
    "sklearn": "1.8.0",
    "numpy": "2.3.5",
    "data_origin": "synthetic",
    "clinical_validation": false
  },
  "test": {
    "encounter_metrics": {
      "auroc": 0.6842272294509679,
      "average_precision": 0.2509130560289523,
      "brier": 0.11908279476399794,
      "balanced_accuracy": 0.646091187982651,
      "sensitivity": 0.6376811594202898,
      "specificity": 0.6545012165450121,
      "tp": 88,
      "tn": 538,
      "fp": 284,
      "fn": 50,
      "n": 960,
      "threshold": 0.19
    },
    "patient_mean_brier": 0.11908279476399794,
    "patient_cluster_auc_interval": {
      "lower": 0.6220001595513791,
      "upper": 0.7359462739518562,
      "valid_repetitions": 100,
      "patients": 160
    }
  }
}
```

## 120 validation-only configurations

All six algorithms, five seeds and four horizons were executed. Horizons define different outcomes and are not interchangeable clinical tasks. Holdout scores were not computed by the grid.

| Configuration | Validation AUROC | Validation Brier |
|---|---:|---:|
| extra_trees_seed101_h14.json | 0.5851393188854489 | 0.07309596988217694 |
| extra_trees_seed101_h30.json | 0.5996393006786433 | 0.13899743359172423 |
| extra_trees_seed101_h45.json | 0.6480150462962964 | 0.1787218092730215 |
| extra_trees_seed101_h7.json | 0.5588631465517241 | 0.03303689688987634 |
| extra_trees_seed11_h14.json | 0.5993680672268908 | 0.08089850862912235 |
| extra_trees_seed11_h30.json | 0.6523235137902101 | 0.13646275377950673 |
| extra_trees_seed11_h45.json | 0.6944970470726403 | 0.1757979625772202 |
| extra_trees_seed11_h7.json | 0.6246526399364829 | 0.04350042072491743 |
| extra_trees_seed23_h14.json | 0.6184465715715716 | 0.06915841301980934 |
| extra_trees_seed23_h30.json | 0.6364887311099531 | 0.13060314502182743 |
| extra_trees_seed23_h45.json | 0.6547800336032457 | 0.18190540725006707 |
| extra_trees_seed23_h7.json | 0.5645394273861996 | 0.029802496443788497 |
| extra_trees_seed42_h14.json | 0.6599977227996552 | 0.06552815582291861 |
| extra_trees_seed42_h30.json | 0.6733573090755236 | 0.12403967100289141 |
| extra_trees_seed42_h45.json | 0.7026324284666178 | 0.16907770076881648 |
| extra_trees_seed42_h7.json | 0.6896310327787843 | 0.026318802423551765 |
| extra_trees_seed67_h14.json | 0.6381677503050145 | 0.06927381367236997 |
| extra_trees_seed67_h30.json | 0.6425677521167795 | 0.13829952173839707 |
| extra_trees_seed67_h45.json | 0.6686421493839467 | 0.1832785566662792 |
| extra_trees_seed67_h7.json | 0.6353804347826087 | 0.03971761792478932 |
| hist_gradient_seed101_h14.json | 0.5630507263634199 | 0.07857603417825926 |
| hist_gradient_seed101_h30.json | 0.5794743429286608 | 0.14579493376242178 |
| hist_gradient_seed101_h45.json | 0.6347164351851851 | 0.18509910483272887 |
| hist_gradient_seed101_h7.json | 0.5413523706896551 | 0.035474221552675496 |
| hist_gradient_seed11_h14.json | 0.5761949579831933 | 0.08576385009072848 |
| hist_gradient_seed11_h30.json | 0.6265443265004503 | 0.14256101146164965 |
| hist_gradient_seed11_h45.json | 0.6751527037126529 | 0.18304962755197113 |
| hist_gradient_seed11_h7.json | 0.5746327907899961 | 0.04655223190846403 |
| hist_gradient_seed23_h14.json | 0.6234202952952953 | 0.07207926235071321 |
| hist_gradient_seed23_h30.json | 0.5991564616988014 | 0.14108500254147707 |
| hist_gradient_seed23_h45.json | 0.6244359655875792 | 0.1947811600881281 |
| hist_gradient_seed23_h7.json | 0.5627615837623616 | 0.030104373788039273 |
| hist_gradient_seed42_h14.json | 0.6618194830755217 | 0.06733700775012415 |
| hist_gradient_seed42_h30.json | 0.6443325576475565 | 0.13113056324848366 |
| hist_gradient_seed42_h45.json | 0.6795539251650771 | 0.17628446430157135 |
| hist_gradient_seed42_h7.json | 0.6775242958326471 | 0.027362071487869198 |
| hist_gradient_seed67_h14.json | 0.6370866859199085 | 0.0709503168606762 |
| hist_gradient_seed67_h30.json | 0.6130542320415162 | 0.14408394056882876 |
| hist_gradient_seed67_h45.json | 0.662869921072489 | 0.18809102881524367 |
| hist_gradient_seed67_h7.json | 0.6378260869565218 | 0.041001419520162646 |
| knn_seed101_h14.json | 0.5428078113836629 | 0.0770787037037037 |
| knn_seed101_h30.json | 0.5871392035074899 | 0.1426851851851852 |
| knn_seed101_h45.json | 0.6278819444444443 | 0.1857592592592593 |
| knn_seed101_h7.json | 0.5109779094827587 | 0.034833333333333334 |
| knn_seed11_h14.json | 0.5872470588235295 | 0.08288425925925927 |
| knn_seed11_h30.json | 0.6140665532556904 | 0.14129166666666668 |
| knn_seed11_h45.json | 0.6461291645828533 | 0.18611111111111114 |
| knn_seed11_h7.json | 0.5745831679237793 | 0.045 |
| knn_seed23_h14.json | 0.61498998998999 | 0.07186574074074074 |
| knn_seed23_h30.json | 0.6246987363210005 | 0.13476851851851854 |
| knn_seed23_h45.json | 0.6325277170584236 | 0.18972685185185187 |
| knn_seed23_h7.json | 0.5306678025112042 | 0.03174074074074074 |
| knn_seed42_h14.json | 0.6229525529042437 | 0.06864814814814817 |
| knn_seed42_h30.json | 0.6312037232917284 | 0.13024537037037037 |
| knn_seed42_h45.json | 0.673094644167278 | 0.17530092592592597 |
| knn_seed42_h7.json | 0.6329064404546203 | 0.027504629629629632 |
| knn_seed67_h14.json | 0.5957900264088585 | 0.07250925925925926 |
| knn_seed67_h30.json | 0.6123069102606901 | 0.1440833333333333 |
| knn_seed67_h45.json | 0.6657642970053812 | 0.18686111111111112 |
| knn_seed67_h7.json | 0.6423913043478261 | 0.04020833333333333 |
| logistic_seed101_h14.json | 0.6844189092641104 | 0.07072449460572229 |
| logistic_seed101_h30.json | 0.6603673846967094 | 0.1348882916630443 |
| logistic_seed101_h45.json | 0.6723379629629629 | 0.17530711979403515 |
| logistic_seed101_h7.json | 0.6647359913793104 | 0.03192686728527028 |
| logistic_seed11_h14.json | 0.6881478991596639 | 0.07784546106602971 |
| logistic_seed11_h30.json | 0.6886791726643626 | 0.1315620986887246 |
| logistic_seed11_h45.json | 0.6917436038638113 | 0.17466024151422363 |
| logistic_seed11_h7.json | 0.7183902342199285 | 0.042730394878289335 |
| logistic_seed23_h14.json | 0.6585648148148148 | 0.06849870047530762 |
| logistic_seed23_h30.json | 0.6748957790515894 | 0.12673166297020214 |
| logistic_seed23_h45.json | 0.6754083805820441 | 0.17853208676433188 |
| logistic_seed23_h7.json | 0.6733953109374421 | 0.0291753612658508 |
| logistic_seed42_h14.json | 0.7046308495583858 | 0.06476938809420785 |
| logistic_seed42_h30.json | 0.7055553204992595 | 0.12182310193530183 |
| logistic_seed42_h45.json | 0.7153220836390317 | 0.16672462365429266 |
| logistic_seed42_h7.json | 0.6991434689507495 | 0.02632159758773045 |
| logistic_seed67_h14.json | 0.6562060817593551 | 0.06948129933483296 |
| logistic_seed67_h30.json | 0.6630830627295073 | 0.13629144962556747 |
| logistic_seed67_h45.json | 0.6866307921942729 | 0.17975920156428782 |
| logistic_seed67_h7.json | 0.7086141304347826 | 0.03942959182447839 |
| naive_bayes_seed101_h14.json | 0.6806233627054061 | 0.07066909027976011 |
| naive_bayes_seed101_h30.json | 0.6575222133256633 | 0.13530041277300983 |
| naive_bayes_seed101_h45.json | 0.6701909722222222 | 0.1758049320288107 |
| naive_bayes_seed101_h7.json | 0.6751077586206896 | 0.031922715078840445 |
| naive_bayes_seed11_h14.json | 0.6903126050420167 | 0.07746595971630424 |
| naive_bayes_seed11_h30.json | 0.6901648051358238 | 0.13134039276474302 |
| naive_bayes_seed11_h45.json | 0.6933338577987065 | 0.1743754796751649 |
| naive_bayes_seed11_h7.json | 0.7167526796347756 | 0.04262012510913235 |
| naive_bayes_seed23_h14.json | 0.6596753003003003 | 0.06831652457304623 |
| naive_bayes_seed23_h30.json | 0.6728602136529442 | 0.12682383647571496 |
| naive_bayes_seed23_h45.json | 0.6734191583454616 | 0.17850013550683597 |
| naive_bayes_seed23_h7.json | 0.66661728212156 | 0.029146660699616685 |
| naive_bayes_seed42_h14.json | 0.7100798646692366 | 0.06459817275703118 |
| naive_bayes_seed42_h30.json | 0.7036005923418659 | 0.1221942660822782 |
| naive_bayes_seed42_h45.json | 0.7157329420396186 | 0.16691266431072252 |
| naive_bayes_seed42_h7.json | 0.7144621973315763 | 0.02627529687404141 |
| naive_bayes_seed67_h14.json | 0.6593874998069528 | 0.06931975339893372 |
| naive_bayes_seed67_h30.json | 0.6626430153864828 | 0.13639451597276792 |
| naive_bayes_seed67_h45.json | 0.6905028117581613 | 0.17930659332184345 |
| naive_bayes_seed67_h7.json | 0.7069836956521739 | 0.03937612147055466 |
| random_forest_seed101_h14.json | 0.5835913312693499 | 0.07423820372526439 |
| random_forest_seed101_h30.json | 0.5913603184104355 | 0.14088050697775714 |
| random_forest_seed101_h45.json | 0.6464525462962962 | 0.17961461341080368 |
| random_forest_seed101_h7.json | 0.5488617995689655 | 0.03345132466518397 |
| random_forest_seed11_h14.json | 0.5795226890756302 | 0.08179596966455062 |
| random_forest_seed11_h30.json | 0.6462963105510696 | 0.13737602145267416 |
| random_forest_seed11_h45.json | 0.6821458875358931 | 0.1787721415809004 |
| random_forest_seed11_h7.json | 0.5865298729654624 | 0.044147082334306434 |
| random_forest_seed23_h14.json | 0.6122685185185186 | 0.07016512456133155 |
| random_forest_seed23_h30.json | 0.6288920010422094 | 0.13415435285610763 |
| random_forest_seed23_h45.json | 0.6332582223995413 | 0.18772133847177078 |
| random_forest_seed23_h7.json | 0.5987443979406645 | 0.029788276226021745 |
| random_forest_seed42_h14.json | 0.6576147952959548 | 0.06637029678476189 |
| random_forest_seed42_h30.json | 0.642623228263169 | 0.12800506392005592 |
| random_forest_seed42_h45.json | 0.6945619955979456 | 0.1711575653445271 |
| random_forest_seed42_h7.json | 0.6855748641080547 | 0.026623768209806595 |
| random_forest_seed67_h14.json | 0.6245772266065388 | 0.07027592279515939 |
| random_forest_seed67_h30.json | 0.6222269430366302 | 0.14072708304209558 |
| random_forest_seed67_h45.json | 0.6649078261061142 | 0.18531678844539742 |
| random_forest_seed67_h7.json | 0.6026086956521739 | 0.040176613457665725 |

## Limits

All patients, sites and outcomes are simulated. No clinical performance claim, real patient data, external validation or medically justified threshold is supplied. Patient-cluster intervals describe conditional sampling variability only. Notebook outputs were generated by sequential Python cell execution, not a Jupyter kernel. Local training generates trusted joblib artifacts; binary weights are not bundled. No GitHub Actions workflow is present. Adding these files to an older checkout does not automatically delete old workflow files.
