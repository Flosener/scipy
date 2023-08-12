import pandas as pd
import matplotlib.pyplot as plt
from plotnine import *


def make_scatterplot(iris, my_iris):
    """ 
    Function for plotting an advanced visualization of the iris dataset, 
    including scattered subplots per species with color encoding.
    
    Args:
    iris -- the iris dataset
    my_iris -- sub-dataset of iris
    """
    
    # scatterplot with plotnine
    fig = (ggplot(iris, aes(x = 'petalWidth', y = 'petalLength', color = 'sepalWidth'))
                   + geom_point()
                   + facet_wrap('species')
                  ).draw()
    
    # axes labeling and scatterplotting with matplotlib
    fig.suptitle('petalWidth, petalLength and sepalWidth per Species', fontsize=12)
    fig.get_axes()[1].scatter(x=my_iris['petalWidth'], y=my_iris['petalLength'], c='red', s=5)
    
    return fig


if __name__ == "__main__":

    iris = pd.read_csv('data/iris.csv', index_col=0)
    my_iris = pd.read_csv('data/my_iris.csv', index_col=0)
    fig = make_scatterplot(iris, my_iris)
    plt.show()

