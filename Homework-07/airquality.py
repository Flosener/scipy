from helpers import load_air_data

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def main():

    df = load_air_data()

    fig, upper_ax, lower_ax = plot_airquality(df)

    plt.tight_layout()

    plt.show()


def plot_airquality(data):
    """ Plots air quality at Alte Muenze, Osnabrueck in September 2018 as measured by fine dust concentration levels. """

    # Create figure and two subplots
    fig, axes = plt.subplots(nrows=2, sharex=True)
    
    # Define x, y labels with airquality data
    x = data.index
    y_pm_25 = data["PM2.5"]
    y_pm_10 = data["PM10"]
    
    # Upper subplot
    axes[0].plot(x,y_pm_25, label="PM2.5")
    axes[0].plot(x,y_pm_10, label="PM10")
    axes[0].set(title="Individual Concentrations", ylabel="Concentration", yticks=[0,10,20,30,40,50])
    axes[0].legend(loc=0) # best location
    
    # Lower subplot
    axes[1].bar(x,y_pm_25, color="#1f77b4")
    axes[1].bar(x, y_pm_10, bottom=y_pm_25, color="#ff7f0e")
    axes[1].set(title="Stacked Concentrations", xlabel="Day", ylabel="Concentration", yticks=[0,20,40,60,80])
    
    # Setting suptitle
    fig.suptitle("Fine Dust Concentrations at Alte Muenze (Osnabrueck) in September 2018")
    
    # return the figure with both subplot axes
    return fig, axes[0], axes[1]


if __name__ == "__main__":
    main()
