# CVD19-Tracker-PY

# CVD19-Tracker-PY

## Overview
CVD19-Tracker-PY is a Python-based project for analyzing and visualizing COVID-19 data, including cases, deaths, and vaccination progress for selected countries.

## Features
- Data cleaning and preprocessing of COVID-19 datasets.
- Visualization of:
  - Total cases over time.
  - Total deaths over time.
  - Daily new cases.
  - Cumulative vaccinations.
  - Percentage of vaccinated population.
- Calculation of death rates.

## Data Sources
- `owid-covid-data.csv`: Contains global COVID-19 data.
- `vaccinations.csv`: Contains vaccination data.

## Requirements
- Python 3.x
- Libraries:
  - pandas
  - matplotlib
  - seaborn

## Usage
1. Clone the repository.
2. Ensure the required datasets (`owid-covid-data.csv` and `vaccinations.csv`) are in the project directory.
3. Run `Final Project.py` to execute the analysis and generate visualizations.

## Visualizations
- Line plots for total cases, deaths, and daily new cases.
- Vaccination progress over time.

## Insights
- Death rate calculation: `total_deaths / total_cases * 100`.

