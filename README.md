# **Double Bottom Pattern Detection using Machine Learning**

<h2 align="center">

![pandas](https://img.shields.io/badge/pandas-v2.2.3-white)
![matplotlib](https://img.shields.io/badge/matplotlib-v3.9.3-blue)
![plotly](https://img.shields.io/badge/plotly-v5.24.1-red)
![seaborn](https://img.shields.io/badge/seaborn-v0.13.2-lightblue)
![sklearn](https://img.shields.io/badge/sklearn-v1.5.2-orange)

</h2>

<div align="center">

![license](https://img.shields.io/badge/license-Apache_2.0-green)

</div>

This repository provides an end-to-end solution for detecting **Double Bottom chart patterns** using Machine Learning (ML). It includes data preparation, feature engineering, model training, evaluation, and visualization to identify patterns in OHLC data.

---

## 📑 **Table of Contents**

- [**Double Bottom Pattern Detection using Machine Learning**](#double-bottom-pattern-detection-using-machine-learning)
  - [📑 **Table of Contents**](#-table-of-contents)
  - [🚀 **Overview**](#-overview)
  - [📊 **Dataset**](#-dataset)
    - [Data Format](#data-format)
  - [🛠️ **Methodology**](#️-methodology)
  - [⚙️ **Requirements**](#️-requirements)
  - [💻 **Installation**](#-installation)
  - [📁 **Project Structure**](#-project-structure)
  - [📈 **Results**](#-results)
    - [Accuracy on Test Set](#accuracy-on-test-set)
  - [📊 Visualizations](#-visualizations)
  - [Contributing](#contributing)
  - [Support](#support)
  - [Acknowledgements](#acknowledgements)

---

## 🚀 **Overview**  

This project focuses on detecting Double Bottom patterns in financial data using machine learning techniques. The Double Bottom pattern is a technical chart formation that signals a potential reversal in a downtrend, making it crucial for traders and analysts.

To effectively differentiate and identify these patterns, the use of polynomial fitting (polyfit) plays a critical role. By approximating the underlying shape of price movements, polyfit helps smooth and highlight key structural components, such as:

- Local minima (the "bottoms" of the pattern)
- Neckline levels, which serve as resistance or breakout points
- The overall symmetry and curvature of the pattern

This smoothing technique allows us to distinguish Double Bottom formations from random noise or unrelated price fluctuations, improving the feature extraction process for downstream machine learning models.


<a>
    <img src="/docs/images/overview.png">
</a>

The project contemplates a standard pipeline for obtaining the results.

Key highlights:
- General analysis 
- Feature engineering for time series data.  
- Scalable ML pipeline with GridSearchCV for hyperparameter tuning.  
- Performance evaluation using metrics like accuracy, AUROC, precision, and recall.  
- Visualizations for interpretability 
---

## 📊 **Dataset**

- **Source:** The dataset consists of time series data with labels indicating the presence or absence of the Double Bottom pattern.  
- **Features:** The features were designed based on the recognition of characteristics present in the price patterns, taking into account local maxima and minima, as well as their positioning within the time window:
  
   - `Abs Extrema Duration`
   - `Low Threshold Count`
   - `Max Between Min`
   - `Pattern Extrema Duration`
   - `Min Deviation` 
   - `Min Mean`  

### Data Format
The data should be provided in CSV format with the following structure:  
| Feature 1 | Feature 2 | ... | Label |  
|-----------|-----------|------|-------|  
| Value 1   | Value 2   | ...  | 0/1   |  

- **Label:**  
   - `1`: Double Bottom pattern detected.  
   - `0`: No pattern.  

---

## 🛠️ **Methodology**

The project follows the standard ML workflow:  

1. **Feature Engineering**: Creation of meaningful features from raw data to improve model performance.  
2. **Model Training and Tuning**:  
   - Algorithms: Random Forest, Gradient Boosting, and SVM.  
   - GridSearchCV for hyperparameter optimization.  
   - Cross-validation.  
3. **Evaluation**: Using metrics such as accuracy, precision, recall, F1-score, and AUROC.  
4. **Interpretability**: Visualizations for feature importance.  
---

## ⚙️ **Requirements**

The project uses Python 3.8+ and the following libraries:  

- **NumPy**  
- **Pandas**  
- **Scikit-learn**  
- **Matplotlib**  
- **Seaborn**  

You can install all the dependencies using `requirements.txt`.  

---

## 💻 **Installation**

To get started, clone the repository and install the dependencies:  

```bash
# Clone the repository
git clone https://github.com/TA-Experiments-WSC/double-bottom-detection-ml.git

# Navigate to the project folder
cd double-bottom-detection-ml

# Install required libraries
pip install -r requirements.txt
```

## 📁 **Project Structure**
```bash

double-bottom-detection-ml/
│
├── data/                     # Dataset folder
│   ├── raw/                  # Raw data
│   │   ├── benchmark_data.pkl
│   │   └── labels.csv
│   │
│   └── processed/            # Processed data
│       └── features.csv
│
├── notebooks/   # Jupyter Notebooks for analysis and experiments
│   ├── utils/
│   │   └── plotting.py
│   │
│   ├── 01_general_analysis.ipynb
│   ├── 02_feature_engineering.ipynb
│   ├── 03_EDA.ipynb
│   └── 04_train.ipynb
│
├── requirements.txt          # Dependencies
├── LICENSE                 
└── README.md                 # Project documentation
```

## 📈 **Results** 

### Accuracy on Test Set
 * **Accuracy**: `0.90` 
 * **AUROC Score**: `0.89` 
  
 * ### Classification Report 
| Class | Precision | Recall | F1-Score | Support | 
| --- | --- | --- | --- | --- | 
| No Pattern | 1.00 | 0.81 | 0.90 | 16 | 
| Double Bottom | 0.83 | 1.00 | 0.91 | 15 |

## 📊 Visualizations


<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px; border: 1px solid black;">
    <!-- First Row -->
    <div style="border: 1px solid black; padding: 5px;">
        <img src="\docs\results\confusion_matrix.png" alt="Graph 1" style="width: 50%; height: auto;">
        <p style="text-align: center;">Graph 1</p>
    </div>
    <div style="border: 1px solid black; padding: 5px;">
        <img src="\docs\results\report.png" alt="Graph 2" style="width: 50%; height: auto;">
        <p style="text-align: center;">Graph 2</p>
    </div>
    <div style="border: 1px solid black; padding: 5px;">
        <img src="\docs\results\feature_importance.png" alt="Graph 3" style="width: 50%; height: auto;">
        <p style="text-align: center;">Graph 3</p>
    </div>
    <div style="border: 1px solid black; padding: 5px;">
        <img src="\docs\results\roc_curve.png" alt="Graph 4" style="width: 50%; height: auto;">
        <p style="text-align: center;">Graph 4</p>
    </div>
</div>

## Contributing

First off, thanks for taking the time to contribute! Contributions are what makes the open-source community such an amazing place to learn, inspire, and create. Any contributions you make will benefit everybody else and are **greatly appreciated**.

Please try to create bug reports that are:

- _Reproducible._ Include steps to reproduce the problem.
- _Specific._ Include as much detail as possible: which version, what environment, etc.
- _Unique._ Do not duplicate existing opened issues.
- _Scoped to a Single Bug._ One bug per report.

Please adhere to this project's [code of conduct](docs/CODE_OF_CONDUCT.md).

## Support

Reach out to the maintainer at one of the following places:

- [GitHub discussions](https://github.com/TA-Experiments-WSC/double-bottom-detection-ml/discussions)

## Acknowledgements

Thanks for these resources:
- https://pandas.pydata.org/
- https://matplotlib.org/
- https://plotly.com/
- https://seaborn.pydata.org/
- https://scikit-learn.org/stable/