from load_data import load_data

import pandas as pd
import numpy as np


def seven_day_window(df):

    # keep only important cols
    df = df[["#Cases", "#Deaths", "#Recovered"]]
    
    # resample and get sum of every day
    df = df.resample("1D").sum()
    
    # window function for sum in 7 days
    df = df.rolling(7).sum()
    
    # shift by one day
    df = df.shift(1, freq="d")
    
    # return resulting data frame
    return df


if __name__ == "__main__":

    df = load_data()
    weekly_window = seven_day_window(df)
    print(weekly_window)
    
    # plot the data
    weekly_window.plot()

