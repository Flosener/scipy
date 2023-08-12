from pandas.api.types import CategoricalDtype
from load_data import load_data

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def to_categorical(series):

    # cast to ordered cat
    ord_cat = CategoricalDtype(categories=['A00-A04', 'A05-A14', 'A15-A34', 'A35-A59', 'A60-A79', 'A80+'], ordered=True)
    
    # return the resulting ordered categorical series
    return series.astype(ord_cat)


if __name__ == "__main__":

    df = load_data()
    ser = to_categorical(df["AgeGroup"])
    print(ser)
