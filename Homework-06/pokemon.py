import pandas as pd
import numpy as np


def most_common(df):
    """
    Function to return the most common pokemon type combination and its highest atk value.
    
    Args:
    - df: pokemon.csv data frame
    """
    
    # load in pokemon dataset
    pokemon = pd.read_csv("Pokemon_no_duplicates.csv")
    
    # filter out pokemon with only one type and getting most common combi
    df = df.loc[~pd.isna(df['Type 2'])]
    most_common_index = list(df[['Type 1', 'Type 2']].value_counts().idxmax())
    most_common = df.loc[df['Type 1'] == most_common_index[0], :]
    # excluding single type pokemon
    most_common = most_common.loc[most_common['Type 2'] == most_common_index[1], :]
    
    # return pokemon with most common type combination and highest atk
    highest_atk = most_common.loc[most_common['Attack'].idxmax(), 'Name']
    return highest_atk
    
    
    

if __name__ == "__main__":

    # use this for your own testing!

    df = pd.read_csv('Pokemon_no_duplicates.csv', index_col=0)
    name = most_common(df)
    print(name)
