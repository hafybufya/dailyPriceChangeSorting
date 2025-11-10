import time
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

csv_in_use = "historicalData.csv"
date_column = "Date"
y_axis = "Close/Last"
# colors for plots
colour_1 = "#2596be"
colour_2 = "#e63946"

# daily change = todays closing price - yesterdays closing price
def read_nordic_data():
    '''
    reads historicalData.csv file and parses the year column as a date and sets it as an index
    '''
   
    nordic_df = pd.read_csv(csv_in_use , parse_dates=[date_column],  index_col=date_column)
    return nordic_df

df = read_nordic_data()


def add_daily_price_change( column="Close/Last"):
    """
    """
    
    df["Daily Price Change"] = df[column].diff()
    return df

df = add_daily_price_change()


daily_change_array = df["Daily Price Change"].dropna().to_numpy()


# # Time the NumPy sort
# start = time.time()
# sorted_array = np.sort(daily_change_array)
# end = time.time()

# print("Sorted NumPy array (first 7 values):")
# print(sorted_array[:7])
# print(f"\nIt took {end - start:.6f} seconds to sort the array using NumPy.")

sizes = []
times = []

for n in range (7,366):
    sample = daily_change_array[:n]
    start = time.time()
    np.sort(sample)
    end = time.time()
    sizes.append(n)
    times.append(end - start)

#plot of results
n_values_arr = np.array(sizes)
nlogn = n_values_arr * np.log(n_values_arr)

#normalise nlogn to match scale of data
nlogn_scaled = nlogn / nlogn.max() * max(times)

#plot of results

plt.figure(figsize=(8, 5))
plt.plot(sizes, times, linestyle='-', color=colour_1 )
plt.plot(sizes, nlogn_scaled, label="Theoretical O(n log n)", color=colour_2, linestyle="--")
plt.title("Time Taken to Sort n Elements with NumPy sort")
plt.xlabel("Number of Elements (n)")
plt.ylabel("Time Taken (seconds)")
plt.grid(True)
plt.show()