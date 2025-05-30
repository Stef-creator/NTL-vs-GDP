import matplotlib.pyplot as plt


def plot_ntl_and_gdp(full_combined_df):
    """
    Plots two side-by-side bar charts for Nighttime Stable Lights and GDP by year.

    Args:
        full_combined_df (pandas.DataFrame): 
            DataFrame containing at least the columns "Year", "Sum of Nighttime stable Lights", and "GDP".
            Each row should represent data for a specific year.

    The function creates a matplotlib figure with two subplots:
        - The first subplot displays the sum of nighttime stable lights for each year.
        - The second subplot displays the GDP for each year.

    Both plots share the x-axis (Year), use gridlines for the y-axis, and have labeled axes and titles.
    """
    fig, axs = plt.subplots(1, 2, figsize=(16, 6), sharex=True)

    # Plot 1: GDP
    axs[0].bar(full_combined_df["Year"], full_combined_df["GDP"], color='skyblue', edgecolor='black')
    axs[0].set_xlabel("Year")
    axs[0].set_ylabel("GDP")
    axs[0].set_title("GDP by Year")
    axs[0].grid(axis='y', linestyle='--', alpha=0.7)

    # Plot 2: Nighttime Lights
    axs[1].bar(full_combined_df["Year"], full_combined_df["Sum of Nighttime stable Lights"], color='skyblue', edgecolor='black')
    axs[1].set_xlabel("Year")
    axs[1].set_ylabel("Sum of Nighttime Stable Lights")
    axs[1].set_title("Nighttime Stable Lights by Year")
    axs[1].grid(axis='y', linestyle='--', alpha=0.7)


    plt.tight_layout()
    plt.show()

    return None