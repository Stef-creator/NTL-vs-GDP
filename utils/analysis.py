import pandas as pd
from statsmodels.stats.diagnostic import linear_reset, het_breuschpagan
from scipy.stats import shapiro, jarque_bera
from statsmodels.stats.stattools import durbin_watson
import statsmodels.formula.api as smf

def run_ols_regressions(combined_df_1: pd.DataFrame, combined_df_2: pd.DataFrame):
    """
    Runs OLS regression of Log(GDP) on Log(Sum of Nighttime stable Lights) for two dataframes
    and returns the fitted models with robust standard errors.

    Parameters:
        combined_df_1 (pd.DataFrame): First dataframe containing columns 'Log(GDP)' and 'Log(Sum of Nighttime stable Lights)'.
        combined_df_2 (pd.DataFrame): Second dataframe with the same columns.

    Returns:
        tuple: (model_1, model_2) - Fitted OLS models with robust standard errors.
    """
    model_1 = smf.ols('Q("Log(GDP)") ~ Q("Log(Sum of Nighttime stable Lights)")', data=combined_df_1).fit(cov_type='HC1')
    model_2 = smf.ols('Q("Log(GDP)") ~ Q("Log(Sum of Nighttime stable Lights)")', data=combined_df_2).fit(cov_type='HC1')
    
    return model_1, model_2

def run_regression_diagnostics(model):
    """
    Performs diagnostic tests on a regression model and prints the results with pass/fail status.

    Parameters:
        model: Fitted OLS model (statsmodels RegressionResults).

    Prints:
        Model diagnostic test results and interpretations.
    """
    # Perform diagnostic tests
    reset = linear_reset(model, power=2, use_f=True)
    bp = het_breuschpagan(model.resid, model.model.exog)
    model_shapiro = shapiro(model.resid)
    jb = jarque_bera(model.resid)
    dw = durbin_watson(model.resid)

    # Interpretation thresholds
    def interpret(pval, alpha=0.05):
        return "Pass" if pval > alpha else "Fail"

    print("\nDiagnostic Test Results:")
    print("{:<25} {:<12} {:<12} {:<8}".format("Test", "Statistic", "p-value", "Result"))
    print("-" * 65)
    print("{:<25} {:<12.4f} {:<12.4f} {:<8}".format("RESET (F-stat)", reset.statistic, reset.pvalue, interpret(reset.pvalue)))
    print("{:<25} {:<12.4f} {:<12.4f} {:<8}".format("Breusch-Pagan", bp[0], bp[1], interpret(bp[1])))
    print("{:<25} {:<12.4f} {:<12.4f} {:<8}".format("Shapiro-Wilk", model_shapiro.statistic, model_shapiro.pvalue, interpret(model_shapiro.pvalue)))
    print("{:<25} {:<12.4f} {:<12.4f} {:<8}".format("Jarque-Bera", jb.statistic, jb.pvalue, interpret(jb.pvalue)))
    print("{:<25} {:<12.4f} {:<12} {:<8}".format("Durbin-Watson", dw, "N/A", "–"))
