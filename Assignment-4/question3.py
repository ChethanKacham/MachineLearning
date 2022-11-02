import pandas as pd
import seaborn as sns
import warnings
import numpy as np
from scipy.spatial.distance import cdist
import matplotlib.pyplot as plt
from sklearn import metrics
from sklearn.cluster import KMeans
from sklearn import preprocessing

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

# Calculating the Silhouette score for the above cluster
nclusters = 3 # this is the k in kmeans
km = KMeans(n_clusters=nclusters)
km.fit(x)
# Predict the cluster for each data point
y_cluster_kmeans = km.predict(x)
score = metrics.silhouette_score(x, y_cluster_kmeans)
print('Silhouette Score =', score)

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
