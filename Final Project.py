#Import Files#
import math
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns  

#2.1 Load and explore Dataset
df = pd.read_csv('owid-covid-data.csv')
print(df.head())
#print(df.columns())

#Missing Values
df.isnull()

#3.1 Data Cleaning
#Filtering data to  show only South Africa as the location 
filtered_df = df[df['location'].isin(['South Africa','Singapore','Switzerland','Malaysia','Australia'])]
print(filtered_df)

#Dropping rows with incomplete data
df_dropped = df.dropna(how='all', axis = 1 )
print(df_dropped)

#Changing column name from date to datetime
df['date'] = pd.to_datetime(df['date'])

#Interpolation of missing data
df = df.infer_objects(copy=False)
print(df.interpolate())

#4 Basic Data Analysis
print(df.describe())

#Exploratory Data Analysis

#Line Plot for total cases over time for South Africa, Singapore, Switzerland, Malaysia and Australia

locations = filtered_df['location'].unique()

plt.figure(figsize=(10, 6))

for location in locations:
    location_data = filtered_df[filtered_df['location'] == location]
    plt.plot(location_data['date'], location_data['total_cases'], label=location)

plt.title('Total cases vs Datetime')
plt.xlabel('Date')
plt.ylabel('Total Cases')
plt.legend()
plt.show()

#Line plot for Total deaths over time for South Africa,Singapore, Switzerland, Malaysia and Australia
locations = filtered_df['location'].unique()

plt.figure(figsize=(10, 6))

for location in locations:
    location_data = filtered_df[filtered_df['location'] == location]
    plt.plot(location_data['date'], location_data['total_deaths'], label=location)

plt.title('Total Deaths vs Time')
plt.xlabel('Date')
plt.ylabel('Total death')
plt.legend()
plt.show()

#Comparing daily new cases over time for South Africa, Singapore, Switzerland, Malaysia and Australia
locations = filtered_df['location'].unique()

plt.figure(figsize=(10, 6))

for location in locations:
    location_data = filtered_df[filtered_df['location'] == location]
    plt.plot(location_data['date'], location_data['new_cases'], label=location)

plt.title('Daily new cases for different locations')
plt.xlabel('Date')
plt.ylabel('New cases')
plt.legend()
plt.show()

#Calculate the death rate : total_deaths/ total_cases

filtered_df['total_deaths'] = pd.to_numeric(filtered_df['total_deaths'], errors='coerce')
filtered_df['total_cases'] = pd.to_numeric(filtered_df['total_cases'], errors='coerce')
death_rate = (filtered_df['total_deaths' ]/ filtered_df['total_cases'].replace(0, float('nan'))) * 100
filtered_df['death_rate'] = death_rate
print(filtered_df['death_rate'])

#Section 5 Visualizing Vaccination Progress

#Section 7 Inisghts and reporting