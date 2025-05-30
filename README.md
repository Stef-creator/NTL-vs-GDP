# Nighttime Lights and China's GDP: A Data-Driven Assessment

This repository investigates the credibility of reported Chinese GDP data using satellite-recorded nighttime light intensity as a proxy for economic activity. The project builds on the hypothesis that institutional reforms under Xi Jinping—specifically the transition to “Top-Level Design” governance—have improved the alignment between observed economic indicators and reported GDP figures.

## Objective

To assess whether China's officially reported GDP data became more aligned with nighttime light data following institutional reforms implemented around the Third Plenary Session of the 18th CPC Central Committee in 2013.

## Methodology

- **Data Sources**:
  - **World Bank** GDP data (1992–2021)
  - **NOAA Nighttime Light Data** (via preprocessed CSVs)
  
- **Analysis**:
  - Clean and merge NTL and GDP data
  - Log-transform GDP for comparability
  - Regression analysis with robust standard errors (HC1)
  - Diagnostics: RESET, Breusch-Pagan, Shapiro-Wilk, Jarque-Bera, Durbin-Watson

- **Key Equations**:
  - Measurement error model linking true and reported GDP to satellite light
  - Elasticity regression between log(NTL) and log(GDP)

## Results

- Preliminary OLS results show a strong relationship between NTL and GDP
- Robust standard errors (HC1) used for inference  

## Citations

Citations are managed using a `.bib` file. See `references.bib` for the full list.

## Requirements

- Python 3.9+
- `pandas`, `numpy`, `matplotlib`, `statsmodels`, `scipy`
- Optional: `jupyter`, for citation rendering

## Getting Started

1. Clone this repo
2. Install dependencies: `pip install -r requirements.txt`
3. Run the notebook: `jupyter notebook notebook/ntl_gdp_analysis.ipynb`

## License

MIT License

---

*Author: Stefan Pilegaard Pedersen*  
*Location: Copenhagen, Denmark*  
*Contact: [LinkedIn](https://www.linkedin.com/in/stefan-pilegaard-pedersen)*
