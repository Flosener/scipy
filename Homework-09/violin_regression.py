import pandas as pd
import matplotlib.pyplot as plt
from plotnine import *
import numpy as np


def make_violinplot(iris):
    """ Function that plots a violin plot of the iris dataset with jittered datapoints per species. """

    return (ggplot(iris, aes(x = 'species', y = 'petalLength'))
     + geom_violin() # add violin plot for the three species
     + geom_jitter(mapping = aes(color = 'petalWidth'), height = 0.3, width = 0.3) # jitter data points above with color encoding
     + stat_summary(color = 'red') # summary statistics mean and stddev in red
    ).draw()


def make_regressionplot(iris):
    """ Function that plots a regression plot of the iris dataset with scattered datapoints per species. """
    
    return (ggplot(iris, aes(x = 'petalWidth', y = 'petalLength', fill = 'species'))
            + geom_point() # add scatter points to the plot per species
            + geom_smooth(method = 'lm') # add a linear regression per species
            + xlim(0, iris['petalWidth'].max())
            + ylim(0, iris['petalLength'].max())
           ).draw()

if __name__ == "__main__":

    iris = pd.read_csv('data/iris.csv', index_col=0)
    np.random.seed(0)
    fig = make_violinplot(iris)
    plt.show()

    fig = make_regressionplot(iris)
    plt.show()
