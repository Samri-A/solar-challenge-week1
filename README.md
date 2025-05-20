# Solar Challenge Week 1

## Overview

This project analyzes and visualizes meteorological data from Benin, Sierra Leone, and Togo to support solar energy research. It includes data cleaning, exploratory data analysis (EDA), and visualization notebooks.

## Project Structure

```
.
├── app/
|     |__ app.py
|     |__ utils.py
├── scripts/
├── src/
│   ├── data/
│   └── notebooks/
├── tests/
├── requirements.txt
├── README.md
└── .github/
    └── workflows/
        └── unittests.yml
```

- **app/**: Application code for dashboard app.
- **scripts/**: Utility scripts.
- **src/data/**: Raw and cleaned datasets.
- **src/notebooks/**: Jupyter notebooks for EDA and analysis.
- **tests/**: Unit tests.
- **requirements.txt**: Python dependencies.
- **.github/workflows/unittests.yml**: GitHub Actions workflow for CI.

## Requirements

- Python 3.x
- pandas
- numpy
- matplotlib
- seaborn
- scipy
- windrose

Install all dependencies with:
```sh
pip install -r requirements.txt
```

## How to Run

1. Open any notebook in `src/notebooks/` (e.g., `compare_countries.ipynb`) using Jupyter or VS Code.
2. Run all cells sequentially to reproduce the analysis and visualizations.

## Data

- Raw and cleaned datasets are in [`src/data/`](src/data/).
- Example: `benin-malanville.csv` (raw), `benin-malanville_clean.csv` (cleaned). {for some purpose it is not included on the repo}


## Testing

Unit tests can be added to the [`tests/`](tests/) directory. Tests can run automatically on each push using GitHub Actions ([`.github/workflows/unittests.yml`](.github/workflows/unittests.yml)).

## Output

- Cleaned data saved in `src/data/`
- Visualizations and analysis results in the notebooks
- Visualizations data in dashboard app

