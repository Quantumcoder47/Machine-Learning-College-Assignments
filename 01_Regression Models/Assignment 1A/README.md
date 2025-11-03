# Assignment 1A — Linear Regression for CO2 Emission Prediction

Summary
- This notebook demonstrates linear regression to predict CO2 emissions from vehicle/fuel consumption features. It covers data loading, exploration, preprocessing, model training (LinearRegression), evaluation (MSE, RMSE, R2) and visualization.

Dataset
- `fuel_consumption_dataset.csv` — columns:
  MODELYEAR, MAKE, MODEL, VEHICLECLASS, ENGINESIZE, CYLINDERS, TRANSMISSION, FUELTYPE, FUELCONSUMPTION_CITY, FUELCONSUMPTION_HWY, FUELCONSUMPTION_COMB, FUELCONSUMPTION_COMB_MPG, CO2EMISSIONS

How to run
- Open `model.ipynb` and run cells top-to-bottom. Requires pandas, numpy, matplotlib, seaborn, scikit-learn.

Notes
- The notebook uses standard sklearn pipeline steps (train_test_split, LinearRegression, metrics). Clear outputs before sharing.
