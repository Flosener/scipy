from helpers import imports_of_your_file

import pandas as pd
import numpy as np

import matplotlib

try:

    import heatmap as testfile

except ModuleNotFoundError:

    assert False, "The name of your file is supposed to be 'heatmap.py'!"

TYPES = ["Bug", "Dark", "Dragon", "Electric", "Fairy", "Fighting", "Fire", "Flying", "Ghost", "Grass", "Ground", "Ice", "Normal",\
    "Poison", "Psychic", "Rock", "Steel", "Water"]


def test_make_heatmap(filename="heatmap", allowed_imports={"numpy", "pandas", "matplotlib.pyplot"}):
    """ Checks whether returned heatmap has the correct attributes. """

    fig, ax = testfile.make_heatmap()

    # general checks
    assert isinstance(fig, matplotlib.figure.Figure), "The first returned variable should be a Figure!"
    assert isinstance(ax, matplotlib.axes.Axes), "The second second variable should be an Axes object!"

    # data checks
    assert len(ax.images) == 1, "You should plot exactly one image (that of the heatmap)!"
    assert ax.images[0]._A.shape == (18, 18), "The heatmap should be quadratic!"
    assert ax.images[0].cmap.name == "inferno", "The heatmap should use the colormap 'inferno'!"
    assert np.all(np.sum(ax.images[0]._A, axis=0) == [3, 16, 14, 6, 18, 19, 9, 87, 12, 18, 30, 10, 4, 31, 27, 14, 19, 13]), "The underlying\
        frequencies of your heatmap seem to be incorrect! Use raw counts of type combinations. "

    # annotation and labeling 
    assert ax.get_title() == "Pokemon Type Combination Frequencies", "The title is not correct!"
    assert ax.xaxis.label.get_text() == "Type 2", "The x-axis is not labeled correctly!"
    assert ax.yaxis.label.get_text() == "Type 1", "The y-axis is not labeled correctly!"
    assert np.all(sorted([label.get_text() for label in ax.get_xticklabels()]) == TYPES), "The x-ticks seem to be incorrect!"
    assert np.all(sorted([label.get_text() for label in ax.get_yticklabels()]) == TYPES), "The x-ticks seem to be incorrect!"
    assert ax.images[0].colorbar is not None, "There should be a colorbar!"

    # imports check
    assert set(imports_of_your_file(filename, testfile)) <= allowed_imports, "You are importing modules that are not allowed."

