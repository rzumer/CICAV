This directory contains a labeled set of extracted features, as well as a model pre-trained on this data, in the formats used by [Weka](https://www.cs.waikato.ac.nz/ml/weka/). This is the same data used to generate results presented in the original paper<sup>[1](#fn1)</sup>.

The pre-processed, labeled data set is available through [Google Drive](https://drive.google.com/file/d/0ByWm0x8wwapoLTdnVmx5NjhWbmM/view?usp=sharing).

The training parameters and results obtained from `Weka` are as follows:
```
=== Run information ===

Scheme:       weka.classifiers.trees.HoeffdingTree -L 2 -S 1 -E 1.0E-7 -H 0.05 -M 0.01 -G 200.0 -N 0.0
Relation:     animationtype-weka.filters.unsupervised.attribute.Remove-R4-5,8,10-weka.filters.unsupervised.attribute.Remove-R2
Instances:    148
Attributes:   8
              mean transitions/s
              mean gradient mag
              immobile frames
              hist peaks
              texture hist peaks
              mean hist diff
              mean face count
              animation type
Test mode:    10-fold cross-validation

=== Classifier model (full training set) ===

2D (78.000) NB1 NB adaptive1

Time taken to build model: 0.04 seconds

=== Stratified cross-validation ===
=== Summary ===

Correctly Classified Instances         119               80.4054 %
Incorrectly Classified Instances        29               19.5946 %
Kappa statistic                          0.6055
Mean absolute error                      0.171 
Root mean squared error                  0.3278
Relative absolute error                 51.0017 %
Root relative squared error             80.3376 %
Total Number of Instances              148     

=== Detailed Accuracy By Class ===

                 TP Rate  FP Rate  Precision  Recall   F-Measure  MCC      ROC Area  PRC Area  Class
                 0.870    0.268    0.779      0.870    0.822      0.610    0.851     0.812     2D
                 0.000    0.000    0.000      0.000    0.000      0.000    ?         ?         3D
                 0.732    0.130    0.839      0.732    0.782      0.610    0.851     0.817     None
Weighted Avg.    0.804    0.202    0.808      0.804    0.803      0.610    0.851     0.814     

=== Confusion Matrix ===

  a  b  c   <-- classified as
 67  0 10 |  a = 2D
  0  0  0 |  b = 3D
 19  0 52 |  c = None
```

<a name="fn1">1</a>: Zumer, R. & Ratté, S. Int J Multimed Info Retr (2018) 7: 187. https://doi.org/10.1007/s13735-018-0146-2
