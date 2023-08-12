from helpers import imports_of_your_file

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from plotnine import *

try:

    import scatterplot as testfile

except ModuleNotFoundError:

    assert False, 'The name of your file is supposed to be "scatterplot.py"!'


def test_scatterplot(filename='scatterplot', allowed_imports={"numpy", "pandas", "matplotlib.pyplot", "plotnine"}):
    """ Checks whether plots returned by make_scatterplot have the correct attributes. """

    iris = pd.read_csv('data/iris.csv', index_col=0)
    my_iris = pd.read_csv('data/my_iris.csv', index_col=0)


    np.random.seed(0)
    fig = testfile.make_scatterplot(iris, my_iris)

    assert isinstance(fig, matplotlib.figure.Figure), "The returned variable of make_scatterplot() should be a Figure!"

    try:
        ax1, ax2, ax3 = fig.get_axes()
    except ValueError:
        assert False, 'Your figure should have three axes'

    # test ax1
    npzfile = np.load('ref_data/task2/ax1.npz')
    assert np.allclose(npzfile['offsets'], ax1.collections[0].get_offsets()), 'Something is wrong with the data of the scatterplot in axes 1'
    assert np.allclose(npzfile['color'], np.asarray(ax1.collections[0].get_fc())), 'Something is wrong with the color of the scatterplot in axes 1'

    # test ax2
    npzfile = np.load('ref_data/task2/ax2.npz')
    assert np.allclose(npzfile['offset_versicolor'], ax2.collections[0].get_offsets()), 'Something is wrong with the data of the versicolor scatterplot in axes 2'
    assert np.allclose(npzfile['color_versicolor'], np.asarray(ax2.collections[0].get_fc())), 'Something is wrong with the color of the versicolor scatterplot in axes 2'

    assert np.allclose(npzfile['offset_my_iris'], ax2.collections[1].get_offsets()), 'Something is wrong with the data of the myiris scatterplot in axes 2'
    assert np.allclose(npzfile['color_my_iris'], np.asarray(ax2.collections[1].get_fc())), 'Something is wrong with the color of the myiris scatterplot in axes 2'

    # test ax3
    npzfile = np.load('ref_data/task2/ax3.npz')
    assert np.allclose(npzfile['offsets'], ax3.collections[0].get_offsets()), 'Something is wrong with the data of the scatterplot in axes 3'
    assert np.allclose(npzfile['color'], np.asarray(ax3.collections[0].get_fc())), 'Something is wrong with the color of the scatterplot in axes 3'

    # test title
    assert fig._suptitle.get_text() == 'petalWidth, petalLength and sepalWidth per Species', 'The suptitle is not correct!'



if __name__ == "__main__":
    test_scatterplot()
    print('pass')