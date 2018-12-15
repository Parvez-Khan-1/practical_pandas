import pandas as pd

"""
DIFFERENT WAYS OF RENAMING A CALLING
"""
# read dataset
data_frame = pd.read_table('data.csv')

# show all columns
data_frame.columns

# WAY 1: rename column order_id by Order_ID and quantity by QUANTITY
data_frame.rename(columns={'order_id': 'Order_ID', 'quantity': 'Quantity'}, inplace=True)

# WAY 2:
new_cols = ['Order_Id', 'Quantity', 'Item Name', 'Choice Description', 'Item Price']
data_frame.columns = new_cols

# WAY 3 We can even rename column names when we are reading a file
new_data_frame = pd.read_table('data.csv', names=new_cols, header=0)


# WAY 4, Consider we have 500 columns in our dataset, so in that case how can we replace all spaces in the column name
new_data_frame.columns = new_data_frame.columns.str.replace(' ', '_')
print(new_data_frame.columns)
