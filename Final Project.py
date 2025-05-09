#Import Files#

import pandas as pd
import matplotlib as plt
import seaborn as sns  

#2.1 Load and explore Dataset
df = pd.read_csv('owid-covid-data.csv')
print(df.head())
#print(df.columns())

#Missing Values
df.isnull()

#3.1 Data Cleaning
#Filtering data to  show only South Africa as the location 
filtered_df = df[df['location'] == 'South Africa']
print(filtered_df)

#Dropping rows with incomplete data
df_dropped = df.dropna(how='all', axis = 1 )
print(df_dropped)

#Changing column name from date to datetime
df = df.rename( columns={'date': 'datetime'})
print(df)

#Interpolation of missing data
#df.interpolate(method='polynomial',)
print(df.interpolate())

#4 Basic Data Analysis
print(df.describe())

#Exploratory Data Analysis

