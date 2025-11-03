# Assignment 5 — Logistic Regression: Cancer Classification

Summary
- Uses logistic regression to classify tumors (benign vs malignant). The notebook demonstrates cleaning (handling '?'), feature selection, scaling, model training and evaluation using confusion matrix, precision/recall, F1-score and ROC.

Dataset
- `samples_cancer.csv` — columns:
  ID, Clump, UnifSize, UnifShape, MargAdh, SingEpiSize, BareNuc, BlandChrom, NormNucl, Mit, Class

How to run
- Open `model.ipynb`. Requires pandas, numpy, scikit-learn, seaborn, matplotlib.

Notes
- The notebook maps Class values (2 -> benign, 4 -> malignant) and visualizes feature correlations.
