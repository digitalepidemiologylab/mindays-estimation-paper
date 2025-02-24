# Minimum Days Estimation for Reliable Dietary Intake Information

This repository contains the analysis code associated with our paper "Minimum Days Estimation for Reliable Dietary Intake Information: Findings from a Digital Cohort". The study analyzes data from the "Food & You" digital cohort to determine optimal duration for dietary intake estimation.

## Requirements
Python 3.12 with standard scientific computing libraries (pandas, numpy, scipy, statsmodels, pingouin, matplotlib, seaborn)

## Repository Structure
- **Analysis Notebooks**
  - `preprocessing.ipynb`: Initial data cleaning and preparation
  - `LMM_method.ipynb`: Linear Mixed Model analysis (LMM). Models to analyze day-of-week effects on nutrient intake, accounting for demographic factors (age, BMI, gender). Generates heatmaps showing significant variations in intake patterns across weekdays.
  - `CV_method.ipynb`: Coefficient of Variation method (CV). Applies the Variance Ratio method to determine minimum days needed for reliable dietary assessment. Calculates within-person and between-person variations for different nutrients and reliability thresholds.
  - `ICC_method.ipynb`: Intraclass Correlation Coefficient analysis (ICC). To assess measurement reliability across multiple days (described as ICC Method 1 in the paper).
  - `ICC_day_combinations.ipynb`: Optimal day combinations analysis. Analyzes different combinations of days to identify optimal sampling patterns. Determines which specific day combinations yield the most reliable dietary intake estimates. This is described as ICC Method 2 in the paper.

- **Supporting Code**
  - `config/`: Configuration settings and variables
  - `utils/`: Helper functions for data processing and ICC calculations

- **Outputs**
  - `figures/`: Generated visualizations
  - `outputs/`: Analysis results

- **Data**
  - `data/`: Data directory (not publicly available due to privacy)

## Citation
```
Singh, R., Verest, M.T.E., Salathé, M. (2024). Minimum Days Estimation for Reliable 
Dietary Intake Information: Findings from a Digital Cohort.
```

## Contact
- Rohan Singh (rohan.singh@epfl.ch)
- Marcel Salathé (marcel.salathe@epfl.ch)