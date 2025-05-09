#Import Files#

import pandas as pd
import matplotlib as plt
import seaborn as sns  

#2.1 Load and explore Dataset
df = pd.read_csv('owid-covid-data.csv')
print(df.head())
print(df.column())
print(df.isnull().sum())

#2.2 Data Cleaning


#Basic Data Analysis
print(df.describe())

#Data Visualization 