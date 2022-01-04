# load csv in data frame 
import pandas as pd 
df = pd.read_csv('data.csv')
print(df.to_string())
# to_string() => to print the entire dataframes