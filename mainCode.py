# ---------------------------------------------------------------------
# IMPORTED FUNCTIONS USED IN PROGRAM
# ---------------------------------------------------------------------

import time
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

csv_in_use = "historicalData.csv"
date_column = "Date"
price_change_column = "Close/Last"

# colors for plots
colour_1 = "#2596be"
colour_2 = "#e63946"

## ---------------------------------------------------------------------
# FUNCTION: Read CSV data into DataFrame
# ---------------------------------------------------------------------

def read_nordic_data():
    
    """

    Reads historicalData.csv file and converts to Dandas dataframe

    Returns
    -------

    pandas Dataframe -> Returns fertility df with saved date_column variable as the index

    """
   
    nordic_df = pd.read_csv(csv_in_use , parse_dates=[date_column],  index_col=date_column)
    return nordic_df

df = read_nordic_data()

# ---------------------------------------------------------------------
# FUNCTION: Add daily price change column
# ---------------------------------------------------------------------

def add_daily_price_change(column=price_change_column):
    """

    Calculates difference between variables in price_change_column

    Returns
    -------

    pandas Dataframe -> Returns df with added column "Daily Price Change"

    """

    ## Daily Price change = value today - value yesteday
    df["Daily Price Change"] = df[column].diff()

    return df

df = add_daily_price_change(price_change_column)

# Convert Daily Price Change column to numpy array and remove missing value in first row
daily_change_array = df["Daily Price Change"].dropna().to_numpy()


def plot_graph(numpy_array):
    sizes = [] # List of sample sizes tested
    times = [] # Sorting times

    for n in range (7,366):
        sample = numpy_array[:n]
        start = time.time()
        np.sort(sample)
        end = time.time()
        sizes.append(n)
        times.append(end - start)

    # Computing nlogn
    n_values_arr = np.array(sizes)
    nlogn = n_values_arr * np.log(n_values_arr)

    # Normalise nlogn to match scale of data
    nlogn_scaled = nlogn / nlogn.max() * max(times)

    # Plot of results

    plt.figure(figsize=(8, 5))
    plt.plot(sizes, times, linestyle='-', color=colour_1 )
    plt.plot(sizes, nlogn_scaled, label="Theoretical O(n log n)", color=colour_2, linestyle="--")
    plt.title("Time Taken to Sort n Elements with NumPy sort")
    plt.xlabel("Number of Elements (n)")
    plt.ylabel("Time Taken (seconds)")
    plt.grid(True)
    plt.show()

    return np.sort(numpy_array), nlogn


# Pure function to calculate nlogn -> struggling with main one
def compute_nlogn(n_values): 
    n_values = np.array(n_values)
    return n_values * np.log(n_values)


if __name__ == "__main__":
   
    add_daily_price_change(price_change_column)

