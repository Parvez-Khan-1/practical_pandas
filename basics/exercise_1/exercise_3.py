"""
Different Ways Of Removing Rows and Columns From a Pandas DataFrame
"""
import pandas as pd

data_frame = pd.read_table('data.csv')

data_frame.columns

# Drop a single columns
data_frame.drop('choice_description', axis=1, inplace=True)

# Drop list of columns
data_frame.drop(['item_name', 'item_price'], axis=1, inplace=True)

# Drop rows from dataframe
data_frame.drop([0], axis=0, inplace=True)

print(data_frame.head())