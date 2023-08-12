from helpers import imports_of_your_file

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from plotnine import *

try:

    import violin_regression as testfile

except ModuleNotFoundError:

    assert False, 'The name of your file is supposed to be "violin_regression.py"!'


def test_violin_regression(filename='violin_regression', allowed_imports={"numpy", "pandas", "matplotlib.pyplot", "plotnine"}):
    """ Checks whether plots returned by make_violinplot and make_regressionplot have the correct attributes. """

    iris = pd.read_csv('data/iris.csv', index_col=0)
    # set seed to make jitter predictable
    np.random.seed(0)
    fig = testfile.make_violinplot(iris)

    ax = fig.get_axes()[0]
    # general checks

    assert isinstance(fig, matplotlib.figure.Figure), "The returned variable of make_violinplot() should be a Figure!"

    # collect data of plot
    # as far is i can tell
    # scatter is stored in polycollections
    # violin plot in line collection
    # stats in path collection
    # color of scatter in last path collection?? not sure there
    # load reference data
    npzfile = np.load('ref_data/task1/violin/data.npz')

    for i, file in enumerate(npzfile.files):
        # get data of result
        # round to one decimal,
        #a = np.round(ax.collections[i].get_paths()[0].vertices, 1)
        a = ax.collections[i].get_paths()[0].vertices
        assert np.allclose(npzfile[file], a), 'There seems to be a mistake in the data of your violin plot'
        # check if stat color is red
        if i in [5, 7, 9]:
            assert np.all(ax.collections[i].get_fc()[0] == [1., 0., 0., 1.]), 'the stats of the violing plot should be red rgba[1,0,0,1]'


    # test regression plot
    fig = testfile.make_regressionplot(iris)
    ax = fig.get_axes()[0]

    assert isinstance(fig, matplotlib.figure.Figure), "The returned variable of make_regressionplot() should be a Figure!"

    # in collections: 3 polycollections for scatterplot, 1 pathcollection for color band around regression
    # in artists 3 Line2D for regression lines

    # test lines
    npzfile = np.load('ref_data/task1/regression/line_data.npz')
    for i, file in enumerate(npzfile.files):
        # get data of result
        a = ax.artists[i].get_data()
        assert np.allclose(npzfile[file], a), 'There seems to be a mistake in the regression lines of your regression plot'

    # test scatter plots
    npzfile = np.load('ref_data/task1/regression/scatter_data.npz')
    for i, file in enumerate(npzfile.files):
        a = ax.collections[i].get_paths()[0].vertices
        assert np.allclose(npzfile[file], a), 'There seems to be a mistake in the scattered points of your regression plot'

    # testing for imported libraries is hard with ggplot as the whole namespace is imported
    # also not necessary because the plots can only be created using th exact libraries

if __name__ == "__main__":
    test_violin_regression()
    print('pass')