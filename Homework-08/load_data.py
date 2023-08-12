import pandas as pd
import numpy as np


def load_data():

    # load in the two datasets
    cov_data = pd.read_csv("data/RKI_COVID.csv", parse_dates=["ReportingDate"], index_col=0)
    counties_data = pd.read_csv("data/RKI_Counties.csv", index_col=0)
    
    # merge dataframes after renaming
    counties_data.rename(columns = {"RS":"IdCounty"}, inplace=True)
    covid_df = cov_data.merge(counties_data, on="IdCounty", how="left") # preserve original index
    
    # drop unnecessary cols
    covid_df = covid_df[["ReportingDate", "AgeGroup", "Sex", "#Cases", "#Deaths", "IdCounty", "#Recovered", "county"]]
    
    # set index to dates column, sort index by date
    covid_df = covid_df.set_index("ReportingDate")
    covid_df.sort_index(inplace=True)
    
    # return the resulting dataframe
    return covid_df

if __name__ == "__main__":

    df = load_data()
    print(df)
