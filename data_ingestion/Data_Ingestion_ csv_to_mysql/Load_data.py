
from Table_creation import*
import pandas as pd


# This file contains code for loading the csv data into mysql table

#Read the CSV file
df = pd.read_csv("C:/Users/praga/Downloads/parking_final_curated.csv",sep=',',encoding='utf8',low_memory=False)
print(df.head())


#Separate the Column names in csv with underscore("_")
df.columns = df.columns.str.replace(' ','_')

# Trim whitespace

def trim_all_columns(df):
        trim_strings = lambda x: x.strip() if isinstance(x, str) else x
        return df.applymap(trim_strings)



# Write the CSV data to mysql table
df.to_sql('nyparking',con=engine,index=False,if_exists='append')







