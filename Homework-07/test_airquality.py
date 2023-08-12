from helpers import imports_of_your_file, load_air_data

import pandas as pd
import numpy as np

import matplotlib

try:

    import airquality as testfile

except ModuleNotFoundError:

    assert False, "The name of your file is supposed to be 'airquality.py'!"


PM2_5 = [4.07360825, 6.96345188, 13.47961538, 37.58130064, 8.71221074, 21.92315335, 12.72322851, 3.17974304, 4.81888403, 3.68715835,\
    4.19492375, 9.01276596, 9.02389571, 10.03600343, 4.53700855, 6.65648699, 4.61621094, 4.40079723, 4.0696, 4.39694215, 2.79152921,\
    3.68354452, 21.74083904, 1.92079086, 4.18701599, 3.36811744, 7.2202773, 7.04222417, 4.56684028, 5.57896552]

PM10 = [6.67024742, 8.4273431, 15.28023504, 50.77643923, 10.35165289, 29.4187257, 15.69914046, 5.13194861, 6.56188184, 5.880282,\
    6.81492375, 11.68955319, 11.28828221, 12.43233276, 6.68673504, 8.76356877, 7.0690625, 6.97164645, 9.24422609, 10.02411157, 5.74446735,\
    7.12695205, 32.3014726,  5.62289982, 7.7730373, 5.40658031, 10.6602773, 12.27192644, 9.38590278, 9.73862069]


def test_plot_airquality(filename="airquality", allowed_imports={"numpy", "pandas", "matplotlib.pyplot", "helpers"}):
    """ Checks whether plots returned by plot_airquality have the correct attributes. """
    
    df = load_air_data()

    fig, upper_ax, lower_ax = testfile.plot_airquality(df)

    # general checks
    assert isinstance(fig, matplotlib.figure.Figure), "The first returned variable should be a Figure!"
    assert isinstance(upper_ax, matplotlib.axes.Axes), "The third second variable should be an Axes object!"
    assert isinstance(lower_ax, matplotlib.axes.Axes), "The third returned variable should be an Axes object!"

    # upper plot data checks
    assert len(upper_ax.lines) == 2, "You should plot exactly two lines in the upper plot!"
    assert np.allclose(PM2_5, upper_ax.lines[0].get_data()[1]) or np.allclose(PM2_5, upper_ax.lines[1].get_data()[1]),\
    "Neither line of the upper plot contains the correct PM2.5 data!"
    assert np.allclose(PM10, upper_ax.lines[0].get_data()[1]) or np.allclose(PM10, upper_ax.lines[1].get_data()[1]),\
    "Neither line of the upper plot contains the correct PM10 data!"

    # lower plot data checks
    assert len(lower_ax.containers) == 2, "You should have two barplots in the lower plot!"
    lower_ax_bars_a = [artist.get_height() for artist in lower_ax.containers[0]] 
    lower_ax_bars_b = [artist.get_height() for artist in lower_ax.containers[1]]
    assert np.allclose(PM2_5, lower_ax_bars_a) or np.allclose(PM2_5, lower_ax_bars_b),\
    "Neither barplot of the lower plot contains the correct PM2.5 data!"
    assert np.allclose(PM10, lower_ax_bars_a) or np.allclose(PM10, lower_ax_bars_b),\
    "Neither barplot of the lower plot contains the correct PM10 data!"

    # annotation and labeling 
    assert fig._suptitle.get_text() == "Fine Dust Concentrations at Alte Muenze (Osnabrueck) in September 2018", "The suptitle is not correct!"
    assert lower_ax.xaxis.label.get_text() == "Day", "The x-axis is supposed to enumerate the days of the month!"
    assert lower_ax.yaxis.label.get_text() == "Concentration", "The y-axis is supposed to measure the concentration of particles!"
    assert upper_ax.yaxis.label.get_text() == "Concentration", "The y-axis is supposed to measure the concentration of particles!"
    assert upper_ax._axes.yaxis._axes.title.get_text() == "Individual Concentrations", "The title of the upper plot is not correct!"
    assert lower_ax._axes.yaxis._axes.title.get_text() == "Stacked Concentrations", "The title of the lower plot is not correct!"
    assert upper_ax in lower_ax.get_shared_x_axes().get_siblings(lower_ax), "The x-axis is not shared between plots!"
    assert upper_ax.legend_ is not None, "Your upper plot needs a legend!"    

    # imports check
    assert set(imports_of_your_file(filename, testfile)) <= allowed_imports, "You are importing modules that are not allowed."

