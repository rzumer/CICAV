# Feature Extractor
This Python module extracts features from input data clips to CSV and ARFF formats. Features extracted include all the ones described in the original paper<sup>[1](#fn1)</sup> and additional unselected features that did not show improvements in test results, but may be useful to other researchers or users.

## Requirements
* [Python 2.7](https://www.python.org/download/releases/2.7/) with `arff`, `numpy`, `opencv-python`, `PeakUtils`, `scenedetect`, `scikit-image`, `scikit-learn`, `scipy`, and `unicodecsv` (best collected via `pip`).

## Usage
Run as a module via `python feature-extractor base_path`, where `base_path` is the directory housing labeled pre-processed input (e.g. `data/out`). Labeling is done by splitting files into subdirectories (e.g. `Animation` and `NotAnimation`).

The original model (available in the `trained` directory) is trained using [Weka](https://www.cs.waikato.ac.nz/ml/weka/). One should expect superior results by using a more sophisticated training method.

<a name="fn1">1</a>: Zumer, R. & Ratté, S. Int J Multimed Info Retr (2018) 7: 187. https://doi.org/10.1007/s13735-018-0146-2
