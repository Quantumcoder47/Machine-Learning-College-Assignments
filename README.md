## Machine Learning College Assignments

Comprehensive collection of Jupyter-based college assignments covering regression, classification, neural networks, and clustering. Each assignment includes a notebook (`model.ipynb`) and associated datasets (CSV files) used for teaching and hands-on experiments.

---

## Table of Contents
- Repository overview
- Technology used
- Key features
- Folder / Assignment mapping
- Dataset information
- How to run (procedures)
- Requirements
- Highlights
- Learnings & outcomes
- Notes & next steps

---

## Repository overview
This repository groups together college assignments for machine learning topics. The main folders are:

- `01_Regression Models` — Linear and nonlinear regression exercises
- `02_Classification Models` — Binary and multiclass classification tasks
- `03_Neural Networks` — Intro to neural networks and deep learning
- `04_Clustering` — Unsupervised learning and cluster analysis

Each assignment folder typically contains:
- `model.ipynb` — the Jupyter notebook with the solution and explanation
- one or more `.csv` datasets used in the notebook

## Technology used

- Python 3.x
- Jupyter Notebook
- numpy, pandas — data manipulation
- matplotlib, seaborn — plotting and visualization
- scikit-learn — classic ML algorithms (linear models, tree-based, clustering, metrics)
- statsmodels — (where applicable) statistical modeling
- tensorflow / keras — neural networks (Assignment 10/11 may use these)

Note: specific notebooks might import additional libraries; see the top cells of each `model.ipynb` for exact imports.

## Key features

- Hands-on, notebook-based implementations for core ML topics: regression, classification, neural networks, clustering.
- Clean directory structure matching course modules.
- Real datasets included (CSV) so notebooks are runnable locally.

## Folder / Assignment mapping (found in repository)

Each assignment folder contains a short `README.md`, a `model.ipynb` notebook, and one or more datasets (CSV) where applicable. Quick mapping below — open the assignment folder or its `README.md` for details and column headers.

01_Regression Models
- Assignment 1A — Linear Regression for CO2 Emission Prediction
   - Files: `model.ipynb`, `fuel_consumption_dataset.csv`, `README.md`
- Assignment 1B — Linear Regression for Car Price Prediction
   - Files: `model.ipynb`, `used_cars_dataset.csv`, `README.md`
- Assignment 2 — Simple House Price Prediction
   - Files: `model.ipynb`, `housing_price_dataset.csv`, `README.md`
- Assignment 3 — Linear Regression (Gradient Descent from Scratch)
   - Files: `model.ipynb`, `salary_data.csv`, `README.md`
- Assignment 4 — Non-Linear Regression: China GDP Prediction
   - Files: `model.ipynb`, `china_gdp.csv`, `README.md`

02_Classification Models
- Assignment 5 — Logistic Regression: Cancer Classification
   - Files: `model.ipynb`, `samples_cancer.csv`, `README.md`
- Assignment 6 — KNN: Telecommunications Customer Classification
   - Files: `model.ipynb`, `teleCust.csv`, `README.md`
- Assignment 7 — Drug Classification
   - Files: `model.ipynb`, `drug.csv`, `README.md`
- Assignment 8 — Naive Bayes: Diabetes Prediction
   - Files: `model.ipynb`, `pima-indians-diabetes.data.csv`, `README.md`
- Assignment 9 — SVM Cancer Classification (Kernels Comparison)
   - Files: `model.ipynb`, `samples_cancer.csv`, `README.md`

03_Neural Networks
- Assignment 10 — Classification Algorithms Comparison (Diabetes)
   - Files: `model.ipynb`, `pima-indians-diabetes.data.csv`, `README.md`
- Assignment 11 — XOR Neural Network / Perceptron Examples
   - Files: `model.ipynb`, `README.md`

04_Clustering
- Assignment 12 — Iris Classification / Neural Network Experiments
   - Files: `model.ipynb`, `iris.csv`, `README.md`
- Assignment 13 — Customer Segmentation (Clustering)
   - Files: `model.ipynb`, `Cust_Segmentation.csv`, `README.md`
- Assignment 14 — Hierarchical Clustering for Vehicle Grouping
   - Files: `model.ipynb`, `Vehicle.csv`, `README.md`
- Assignment 15 — DBSCAN Weather Station Clustering
   - Files: `model.ipynb`, `WeatherStation.csv`, `README.md`

## Dataset information

All datasets are provided in CSV format inside each assignment folder. Typical columns and dataset sources may vary by assignment — open the CSV or the first cells of the notebook to see column names and any preprocessing steps.

Common datasets and notes:
- `fuel_consumption_dataset.csv` — vehicle fuel-cycle/consumption examples for regression
- `used_cars_dataset.csv` — price prediction exercises for regression
- `housing_price_dataset.csv` — house price prediction (regression)
- `salary_data.csv` — salary vs experience linear regression
- `china_gdp.csv` — time-series / regression style analysis for GDP
- `samples_cancer.csv` — cancer dataset for classification and evaluation
- `pima-indians-diabetes.data.csv` — classic diabetes classification dataset
- `iris.csv` — classic clustering / classification example
- `Cust_Segmentation.csv`, `Vehicle.csv`, `WeatherStation.csv` — clustering and segmentation examples

## How to run (procedures)

1. Clone the repository (already in this workspace if you see the folders above).
2. Create a Python virtual environment (recommended):

   - Windows PowerShell:
     ```powershell
     python -m venv .venv; .\.venv\Scripts\Activate.ps1
     ```

3. Install common packages (see Requirements section below). Example:
   ```powershell
   python -m pip install --upgrade pip; pip install jupyter numpy pandas matplotlib seaborn scikit-learn tensorflow
   ```
4. Start Jupyter Notebook or JupyterLab in the repository root:
   ```powershell
   jupyter notebook
   ```
5. Open an assignment notebook, run the cells sequentially. Many notebooks include explanatory markdown and step-by-step code.

## Requirements

Below is a suggested minimal set of packages used across the notebooks. Pin versions as needed for reproducibility.

Suggested pip install:
```
pip install jupyter numpy pandas matplotlib seaborn scikit-learn statsmodels tensorflow keras
```

Optional (for GPU/advanced deep learning): install the appropriate `tensorflow` package matching your CUDA/cuDNN setup.

## Highlights

- Clear, assignment-by-assignment notebooks that follow a teaching flow: load data -> explore -> preprocess -> model -> evaluate -> visualize.
- Multiple real-world small datasets included so you can reproduce the results offline.
- Covers end-to-end workflows for common ML tasks.

## Learnings & outcomes

After working through these notebooks you should be able to:

- Load and inspect CSV datasets using pandas
- Visualize relationships using matplotlib and seaborn
- Build and evaluate regression and classification models with scikit-learn
- Train and evaluate simple neural networks with Keras/TensorFlow
- Apply clustering methods (K-Means, hierarchical clustering) and interpret cluster results
- Practice a reproducible notebook workflow for experiments

## Notes & next steps

- If you plan to share or grade, clear outputs before committing large notebook outputs.
- Consider adding a `requirements.txt` or `environment.yml` (conda) for reproducibility.
- Add tests or a small runner script if you want programmatic evaluation across assignments.

## Contact

- Repository owner & maintainer: `Quantumcoder47 aka Karan Prabhat` — https://github.com/Quantumcoder47
- Email : prabhatkaran47@gmail.com
---