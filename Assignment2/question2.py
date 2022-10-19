import pandas as pd
import matplotlib.pyplot as plt

# Reading the data file data.csv
df = pd.read_csv("./data.csv")
# Printing basic statistical description about the data
print("Statistical description of data")
print(df.describe())
'''print("Statistical description of Duration")
print(df.Duration.describe())
print("Statistical description of Pulse")
print(df.Pulse.describe())
print("Statistical description of Maxpulse")
print(df.Maxpulse.describe())
print("Statistical description of Calories")
print(df.Calories.describe())'''
# Replacing the null values with the mean
df['Duration'].fillna(df['Duration'].mean(), inplace=True)
df['Pulse'].fillna(df['Pulse'].mean(), inplace=True)
df['Maxpulse'].fillna(df['Maxpulse'].mean(), inplace=True)
df['Calories'].fillna(df['Calories'].mean(), inplace=True)
# Select at least two columns and aggregate the data using: min, max, count, mean
result = df.agg({'Pulse': ['min', 'max', 'count', 'mean'], 'Calories': ['min', 'max', 'count', 'mean']})
# result = df.groupby(['Duration', 'Pulse', 'Maxpulse']).agg({'Calories': ['min', 'max', 'count', 'mean']})
# result.columns = ['cal_min', 'cal_max', 'count', 'cal_mean']
# result.reset_index()
# result = df.groupby(['Duration', 'Pulse']).agg(['min', 'max', 'count', 'mean'])
# result = df.groupby(['Duration', 'Pulse', 'Maxpulse']).agg(['min', 'max', 'count', 'mean'])
print("Grouping by Duration, Pulse and Maxpulse and aggregating the calories data using min, max, count, mean")
print(result)
# Filter the dataframe to select the rows with calories values between 500 and 1000
print("Data containing calories between 500 and 1000")
print(df[(df['Calories'] > 500) & (df['Calories'] < 1000)])
# Filtering the dataframe to select the rows with calories values > 500 and pulse < 100
print("Data containing calories greater than 500 and pulse less than 100")
print(df[(df['Calories'] > 500) & (df['Pulse'] < 100)])
# A new dataframe that contains all the columns from df except “Maxpulse”
df_modified = df.drop("Maxpulse", axis=1)
print("Modified data frame which does not contains Maxpulse column")
print(df_modified)
# Deleting the “Maxpulse” column from the main dataframe
df = df.drop("Maxpulse", axis=1)
print("Main data frame after deleting Maxpulse column")
print(df)
# Converting the datatype of Calories column to int datatype
df['Calories'] = df['Calories'].astype(int)
print("Data type of data")
print(df.dtypes)
# Create a scatter plot for the two columns (Duration and Calories)
df.plot.scatter(x='Duration', y='Calories', title='Scatter plot between two columns (Duration and Calories)')
plt.show()