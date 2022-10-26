import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Question - 1

# Creating the random vector of size 15 having only Integers in the range 1-20
arr = np.random.randint(1, 20, 15, dtype=int)
print("Original array:")
print(arr)
# Reshaping the array to 3 by 5
reshape_arr = arr.reshape(3, 5)
print("Reshaped array:")
print(reshape_arr)
# Printing the array shape
print("Array shape:")
print(reshape_arr.shape)
# Replacing the max in each row by zero
# Copying into the new array and then assigning the maximum value to zero in each row
new_arr = np.copy(reshape_arr)
new_arr[np.arange(len(reshape_arr)), np.argmax(reshape_arr, axis=1)] = 0
print("Updated array after replacing the max in each row by zero(First occurrence):")
print(new_arr)
# Another method for replacing the max in each row by zero
new_arr1 = np.where(reshape_arr == [
        [i]
        for i in np.amax(reshape_arr, axis=1)
    ], 0, reshape_arr)
print("Updated array after replacing the max in each row by zero(All occurrence):")
print(new_arr1)

# Question - 2

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

# Question - 3

# Data given for plotting
languages = 'Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++'
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
colors = ["blue", "orange", "green", "red", "violet", "brown"]
# Exploding Java part
explode = (0.1, 0, 0, 0,0,0)
# Plot in the pie chart
plt.pie(popularity, startangle=140, labels=languages, explode=explode, colors=colors, shadow=True
        , wedgeprops={'edgecolor': 'black'}, autopct='%1.1f%%')
plt.axis('equal')
plt.show()
