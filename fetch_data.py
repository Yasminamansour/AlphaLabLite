import pandas as pd
# read the csv file containing the data and save them in a data frame df
df = pd.read_csv("fetch_transformation_data.csv", header= None, index_col =0)
def fetch(datasource):
    return df.loc[datasource].reset_index(drop=True)




