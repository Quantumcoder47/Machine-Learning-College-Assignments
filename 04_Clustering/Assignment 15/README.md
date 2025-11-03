# Assignment 15 — DBSCAN Weather Station Clustering

Summary
- Applies DBSCAN to cluster weather station observations and detect outliers. Covers data cleaning, feature engineering (aridity index, elevation/pressure ratios), parameter optimization (eps, min_samples), and visualization of clusters and outliers.

Dataset
- `WeatherStation.csv` — columns include:
  Formatted Date, Summary, Precip Type, Temperature (C), Apparent Temperature (C), Humidity, Wind Speed (km/h), Wind Bearing (degrees), Visibility (km), Loud Cover, Pressure (millibars), Daily Summary

How to run
- Open `model.ipynb`. Requires pandas, numpy, scikit-learn, seaborn, matplotlib.

Notes
- The WeatherStation CSV is large and may take longer to process; consider sampling for quick experimentation.
