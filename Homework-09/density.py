import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def make_densityplot(iris):
    """ 
    Function to plot joint density of sepalWidth and petalWidth of the iris dataset for each species, 
    plus the marginal density of the two variables on the side of the plot. 
    """
    
    # set seaborn style to get a grid
    sns.set(style="darkgrid")
    
    # use level function to create a grid with joint and marginal density plots
    joint_grid = sns.JointGrid(data = iris, x = 'sepalWidth', y = 'petalWidth', hue='species')
    joint_grid.plot_joint(sns.kdeplot)
    joint_grid.plot_marginals(sns.kdeplot, shade=True)
    
    # return the resulting JointGrid object
    return joint_grid
    

if __name__ == "__main__":

    iris = pd.read_csv('data/iris.csv', index_col=0)
    fig = make_densityplot(iris)
    plt.show()
