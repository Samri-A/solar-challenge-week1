# Solar Data Analysis - Benin Malanville

## Overview
This project performs exploratory data analysis (EDA), cleaning, and visualization on solar and weather data collected from Benin (Malanville). The analysis includes handling missing values, outlier detection and imputation, time series analysis, and feature relationship exploration.

## Dataset
- **Source:** `src/data/benin-malanville.csv`
- **Features:**
  - Timestamp, GHI, DNI, DHI, ModA, ModB, WS, WSgust, WD, TModA, TModB, Tamb, RH, Cleaning, Comments

## Main Steps
1. **Data Import & Inspection:**
   - Load the dataset and inspect for missing values and data types.
2. **Data Cleaning:**
   - Convert timestamps, drop irrelevant columns, handle missing values, and impute outliers using Z-score and median replacement.
3. **Time Series Analysis:**
   - Visualize trends for key features over monthly and daily periods.
4. **Impact of Cleaning:**
   - Compare module outputs before and after panel cleaning.
5. **Correlation & Relationship Analysis:**
   - Explore feature correlations and relationships using heatmaps and scatterplots.
6. **Wind & Distribution Analysis:**
   - Visualize wind direction/speed and feature distributions.
7. **Temperature Analysis:**
   - Analyze temperature and humidity relationships.

## How to Run
1. Open `notebooks/benin_eda.ipynb` in Jupyter or VS Code.
2. Run all cells sequentially to reproduce the analysis and visualizations.

## Requirements
- Python 3.x
- pandas, numpy, matplotlib, seaborn, scipy, windrose

Install requirements with:
```
pip install pandas numpy matplotlib seaborn scipy windrose
```

## Output
- Cleaned data saved as `src/data/benin-malanville_clean.csv`
- Visualizations and analysis results in the notebook

