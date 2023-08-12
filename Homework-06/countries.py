import pandas as pd
import numpy as np


def aggregate_european_countries():
    """
    Function for finding (non-)european countries with max net migration and min population density in the countries dataset.
    """
    
    # load in the countries dataset and take a look at it
    df = pd.read_csv("countries.csv")
    df.head(10)
    
    # find european countries and keep only necessary columns
    df = df[df['Subcontinent'] == 'Europe']
    
    # (not) in EU; reset indices to start with 0
    not_eu = df.loc[df['In EU'] == False].reset_index()
    eu = df.loc[df['In EU'] == True].reset_index()
    
    # aggregate to pd df for net migration and pop dens by using indices of max/min
    net_migration = pd.DataFrame({'not in eu' : not_eu.loc[not_eu['Net migration'].idxmax()], 'in eu' : eu.loc[eu['Net migration'].idxmax()]})
    pop_dens = pd.DataFrame({'not in eu' : not_eu.loc[not_eu['Pop. Density'].idxmin()], 'in eu' : eu.loc[eu['Pop. Density'].idxmin()]})
    
    # return the resulting data frame
    return pd.DataFrame({'max net migration' : net_migration.loc['Net migration'],
                            'max net migration country' : net_migration.loc['Country'],
                            'min pop density' : pop_dens.loc['Pop. Density'],
                            'min pop density country' : pop_dens.loc['Country']})
    


if __name__ == "__main__":

    # use this for your own testing!
    agg_df = aggregate_european_countries()
    print(agg_df)
