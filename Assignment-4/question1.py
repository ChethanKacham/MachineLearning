# Simple Linear Regression
# Importing the libraries
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error


# Importing the datasets
datasets = pd.read_csv('Salary_Data.csv')

X = datasets.iloc[:, :-1].values
Y = datasets.iloc[:, 1].values

# Splitting the dataset into the Training set and Test set
X_Train, X_Test, Y_Train, Y_Test = train_test_split(X, Y, test_size=1/3, random_state=0)

# Training and predicting the model
# Fitting Simple Linear Regression to the training set
regressor = LinearRegression()
regressor.fit(X_Train, Y_Train)
# Predicting the Test set result
Y_Pred = regressor.predict(X_Test)

# Calculating the MSE with sklearn
mse = mean_squared_error(Y_Test, Y_Pred)
print('Mean Squared Error =', mse)


# Visualising the Training set results
plt.scatter(X_Train, Y_Train, color='red')
plt.plot(X_Train, regressor.predict(X_Train), color='blue')
plt.title('Salary vs Experience (Training set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()


# Visualising the Test set results
plt.scatter(X_Test, Y_Test, color='red')
plt.plot(X_Train, regressor.predict(X_Train), color='blue')
plt.title('Salary vs Experience (Test set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()
