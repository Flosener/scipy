import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def main():

    fig, ax = make_heatmap()

    plt.tight_layout()

    plt.show()
    

def make_heatmap():
    """ Plots frequencies of Pokemon type combinations in a heatmap. """
    
    # Load in the pokemon data as pandas dataframe
    df = pd.read_csv("data/pokemon_no_duplicates.csv", index_col=0)
    
    # preprocess to get type combination counts as quadratic data and replace NaN with zero's
    combination_counts = df.groupby(["Type 1", "Type 2"])["Name"].count().unstack().fillna(0)
    
    # create figure and axis objects and plot heatmap and colorbar
    fig, ax = plt.subplots()
    heatmap = ax.imshow(combination_counts, cmap="inferno")
    fig.colorbar(heatmap)
    
    # axis labeling
    ticklbs = ["Bug", "Dark", "Dragon", "Electric", "Fairy", "Fighting", "Fire", "Flying", 
               "Ghost", "Grass", "Ground", "Ice", "Normal", "Poison", "Psychic", "Rock", "Steel", "Water"]
    
    ax.set(title="Pokemon Type Combination Frequencies", xlabel="Type 2", ylabel="Type 1", yticks=range(0,18), xticks=range(0,18))
    ax.set_xticklabels(ticklbs, rotation="45", ha="right", rotation_mode="anchor")
    ax.set_yticklabels(ticklbs)
    
    # return figure and axis
    return fig, ax


if __name__ == "__main__":
    main()
