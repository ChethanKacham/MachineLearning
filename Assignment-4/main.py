import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import pandas as pd
import seaborn as sns
import warnings
import numpy as np
from scipy.spatial.distance import cdist
import matplotlib.pyplot as plt
from sklearn import metrics
from sklearn.cluster import KMeans
from sklearn import preprocessing

# Question - 1

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


# Question - 2

sns.set(style="white", color_codes=True)

# Ignoring the warnings
warnings.filterwarnings("ignore")

# Reading the datafile
dataset = pd.read_csv('K-Mean_Dataset.csv')

# Replacing the null values with the mean
# print(dataset.isnull().any())
dataset['MINIMUM_PAYMENTS'].fillna(dataset['MINIMUM_PAYMENTS'].mean(), inplace=True)
dataset['CREDIT_LIMIT'].fillna(dataset['CREDIT_LIMIT'].mean(), inplace=True)
# print(dataset.isnull().any())

x = dataset.iloc[:, 1:]

nclusters = 3 # this is the k in kmeans
km = KMeans(n_clusters=nclusters)
km.fit(x)

# Elbow method to know the number of clusters
distortions = []
inertias = []
mapping1 = {}
mapping2 = {}
K = range(1, 11)
for k in K:
    kmeans = KMeans(n_clusters=k, init='k-means++', max_iter=300, n_init=10, random_state=0)
    kmeans.fit(x)
    distortions.append(sum(np.min(cdist(x, kmeans.cluster_centers_, 'euclidean'), axis=1)) / x.shape[0])
    inertias.append(kmeans.inertia_)
    # For inertias
    mapping1[k] = kmeans.inertia_
    # For distortion
    # mapping2[k] = sum(np.min(cdist(x, kmeans.cluster_centers_, 'euclidean'), axis=1)) / x.shape[0]

for key, val in mapping1.items():
    print(f'{key} : {val}')

plt.plot(K, inertias)
plt.title('Elbow method')
plt.xlabel('Number of Clusters')
plt.ylabel('Inertias')
plt.show()

# Calculating the silhouette score for the above cluster
# Predict the cluster for each data point
y_cluster_kmeans = km.predict(x)
score = metrics.silhouette_score(x, y_cluster_kmeans)
print('Silhouette Score =', score)


# Question - 3

# Applying feature scaling
scaler = preprocessing.StandardScaler()
scaler.fit(x)
x_scaled_array = scaler.transform(x)
x_scaled = pd.DataFrame(x_scaled_array, columns=x.columns)

nclusters = 3 # this is the k in kmeans
km = KMeans(n_clusters=nclusters)
km.fit(x_scaled)

y_scaled_cluster_kmeans = km.predict(x_scaled)
score = metrics.silhouette_score(x_scaled, y_scaled_cluster_kmeans)
print('Silhouette Score after scaling =', score)