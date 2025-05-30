import pandas as pd
import numpy as np
import wbdata

# === Load World Bank Data for China GDP ===
def load_china_gdp():
    """
    Fetches and processes China's annual GDP data from the World Bank.

    Returns:
        pandas.DataFrame: A DataFrame containing the following columns for years 1992–2021:
            - 'year': The year of the GDP record.
            - 'GDP': China's GDP in current US dollars.
            - 'Log(GDP)': The natural logarithm of the GDP value.

    Notes:
        - The function retrieves data using the 'wbdata' package.
        - Dates are converted to datetime, and the year is extracted.
        - Only data from 1992 to 2021 is included.
        - The DataFrame is sorted by year in ascending order.
    """
    gdp_china = wbdata.get_dataframe(
    indicators={"NY.GDP.MKTP.CD": "GDP"},
    country="CN"
    ).reset_index()

# Convert date and extract year
    gdp_china["date"] = pd.to_datetime(gdp_china["date"])
    gdp_china["year"] = gdp_china["date"].dt.year

# Filter for years 1992–2021 and sort
    gdp_china = gdp_china[(gdp_china["year"] >= 1992) & (gdp_china["year"] <= 2021)]
    gdp_china = gdp_china[["year", "GDP"]].sort_values("year")

# Compute log of GDP
    gdp_china["Log(GDP)"] = np.log(gdp_china["GDP"])

    return gdp_china

# === Load Nighttime Light Datasets ===
def read_china_nlt():
    """
    Reads Chinese GDP data from two CSV files and returns them as pandas DataFrames.

    Returns:
        tuple: A tuple containing two pandas DataFrames:
            - data1 (DataFrame): Data from "China Data.csv".
            - data2 (DataFrame): Data from "China Data 2.csv".
    """
    data1 = pd.read_csv("data/China Data.csv")
    data2 = pd.read_csv("data/China Data 2.csv")

    return data1, data2

def combine_ntl_gdp_data(data1, data2, gdp_china):
    """
    Merges nighttime light datasets and GDP data into combined DataFrames.

    Args:
        data1 (pd.DataFrame): DataFrame from "China Data.csv".
        data2 (pd.DataFrame): DataFrame from "China Data 2.csv".
        gdp_china (pd.DataFrame): DataFrame containing China's GDP data.

    Returns:
        tuple: A tuple of three DataFrames:
            - combined_df_1: Merged DataFrame of data1 and GDP data.
            - combined_df_2: Merged DataFrame of yearly summed data2 and GDP data.
            - full_combined_df: Concatenation of the above two DataFrames.
    """
    # Prepare first dataset
    dataset_1 = data1[["Year", "Sum of Nighttime stable Lights:", "Log(Sum of Nighttime stable Lights)"]].copy()
    # Prepare second dataset
    dataset_2 = data2[["year", "total_sol"]].copy()

    # Summing total_sol by year and taking the logarithm
    yearly_summed = dataset_2.groupby("year")["total_sol"].sum().reset_index()
    yearly_summed["Log(Sum of Nighttime stable Lights)"] = np.log(yearly_summed["total_sol"])
    yearly_summed["Sum of Nighttime stable Lights"] = yearly_summed["total_sol"]

    # Rename columns for consistency
    yearly_summed.rename(columns={"year": "Year"}, inplace=True)
    gdp_china = gdp_china.rename(columns={"year": "Year"})
    dataset_1.rename(columns={"Sum of Nighttime stable Lights:": "Sum of Nighttime stable Lights"}, inplace=True)

    # Combine both datasets with GDP data
    combined_df_1 = pd.merge(dataset_1, gdp_china, on="Year", how="outer").dropna(axis=0)
    combined_df_2 = pd.merge(yearly_summed, gdp_china, on="Year", how="outer").dropna(axis=0)
    combined_df_2 = combined_df_2.drop("total_sol", axis=1)
    full_combined_df = pd.concat([combined_df_1, combined_df_2], ignore_index=True)

    return combined_df_1, combined_df_2, full_combined_df
