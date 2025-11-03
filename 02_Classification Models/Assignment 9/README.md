# Assignment 9 — SVM: Cancer Classification (Kernels Comparison)

Summary
- Compares multiple SVM kernels (linear, poly, rbf, sigmoid) on the cancer dataset. Includes cleaning, scaling, training multiple models, metrics comparison, ROC/AUC curves and visualization.

Dataset
- `samples_cancer.csv` — columns:
  ID, Clump, UnifSize, UnifShape, MargAdh, SingEpiSize, BareNuc, BlandChrom, NormNucl, Mit, Class

How to run
- Open `model.ipynb`. Requires pandas, numpy, scikit-learn, seaborn, matplotlib.

Notes
- Notebook evaluates multiple kernel choices and highlights the best model by metrics like F1-score and AUC.
