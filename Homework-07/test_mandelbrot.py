from helpers import imports_of_your_file

import pandas as pd
import numpy as np

import matplotlib

try:

    import mandelbrot as testfile

except ModuleNotFoundError:

    assert False, "The name of your file is supposed to be 'mandelbrot.py'!"


def test_visualize_mandelbrot(filename="mandelbrot", allowed_imports={"numpy", "pandas", "matplotlib.pyplot", "helpers"}):
    """ Checks whether returned heatmap has the correct attributes. """

    fig, ax = testfile.visualize_mandelbrot()

    # general checks
    assert isinstance(fig, matplotlib.figure.Figure), "The first returned variable should be a Figure!"
    assert isinstance(ax, matplotlib.axes.Axes), "The second second variable should be an Axes object!"

    # data checks
    assert len(ax.images) == 1, "You should plot exactly one image (the Mandelbrot Set)!"
    assert ax.images[0]._A.shape == (300, 400), "The image should have shape (300, 400)!"
    assert ax.images[0].cmap.name == "turbo", "The heatmap should use the colormap 'turbo'!"
    assert np.sum(ax.images[0]._A, axis=0).mean() == 113.755, "The underlying data of your plot seems to be incorrect!"

    # annotation and labeling checks
    assert ax.axison == False, "The axis should be turned off!"
    assert len(ax.texts) == 1, "There should be exactly one annotation!"
    assert ax.texts[0].get_text() == "Seahorse Valley", "The annotation text is incorrect!"
    assert ax.texts[0].xy == (147, 170), "The annotation location is incorrect!"

    # imports check
    assert set(imports_of_your_file(filename, testfile)) <= allowed_imports, "You are importing modules that are not allowed."

