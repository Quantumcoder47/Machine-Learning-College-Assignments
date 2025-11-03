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

01_Regression Models
- Assignment 1A — `model.ipynb` — dataset: `fuel_consumption_dataset.csv`
- Assignment 1B — `model.ipynb` — dataset: `used_cars_dataset.csv`
- Assignment 2 — `model.ipynb` — dataset: `housing_price_dataset.csv`
- Assignment 3 — `model.ipynb` — dataset: `salary_data.csv`
- Assignment 4 — `model.ipynb` — dataset: `china_gdp.csv`

02_Classification Models
- Assignment 5 — `model.ipynb` — dataset: `samples_cancer.csv`
- Assignment 6 — `model.ipynb` — dataset: `teleCust.csv`
- Assignment 7 — `model.ipynb` — dataset: `drug.csv`
- Assignment 8 — `model.ipynb` — dataset: `pima-indians-diabetes.data.csv`
- Assignment 9 — `model.ipynb` — dataset: `samples_cancer.csv`

03_Neural Networks
- Assignment 10 — `model.ipynb` — dataset: `pima-indians-diabetes.data.csv`
- Assignment 11 — `model.ipynb`

04_Clustering
- Assignment 12 — `model.ipynb` — dataset: `iris.csv`
- Assignment 13 — `model.ipynb` — dataset: `Cust_Segmentation.csv`
- Assignment 14 — `model.ipynb` — dataset: `Vehicle.csv`
- Assignment 15 — `model.ipynb` — dataset: `WeatherStation.csv`

> If you add/remove datasets or notebooks, update this README accordingly.

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

---