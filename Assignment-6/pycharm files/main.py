import pandas as pd
from sklearn.preprocessing import StandardScaler, normalize
import warnings
from sklearn.decomposition import PCA
from sklearn.cluster import AgglomerativeClustering
import seaborn as sns
from sklearn import metrics
from sklearn.cluster import KMeans
from matplotlib import pyplot as plt

# Ignoring the warnings
warnings.filterwarnings("ignore")
# Preprocessing the data by removing the categorical column and filling the null values
# Reading dataset CC.csv
dataset = pd.read_csv('./../CC GENERAL.csv')
# Replacing null values with mean
# print(dataset.isnull().any())
dataset['MINIMUM_PAYMENTS'].fillna(dataset['MINIMUM_PAYMENTS'].mean(), inplace=True)
dataset['CREDIT_LIMIT'].fillna(dataset['CREDIT_LIMIT'].mean(), inplace=True)
# print(dataset.isnull().any())
x = dataset.iloc[:, 1:18]

# Apply StandardScaler() and normalize() functions to scale and normalize raw input data
scaler = StandardScaler()
X_Scale = scaler.fit_transform(x)
# print("After scaling", X_Scale)
normalized_arr = normalize(X_Scale)
# print("After normalizing", normalized_arr)
# Using PCA with K=2
pca = PCA(n_components=2)
principalComponents = pca.fit_transform(x)
principalDf = pd.DataFrame(data=principalComponents, columns=['principal component 1', 'principal component 2'])
finalDf = pd.concat([principalDf, dataset[['TENURE']]], axis=1)
print('CC dataset finalDf after scaling and normalizing:')
print(finalDf)

# Applying Agglomerative Clustering with k = 2,3,4 and 5 on reduced features and
# visualize result for each k value using scatter plot
# Agglomerative Clustering and scatter plot with k = 5
clustering_model_pca = AgglomerativeClustering(n_clusters=5, affinity='euclidean', linkage='ward')
clustering_model_pca.fit(finalDf)
data_labels_pca = clustering_model_pca.labels_
sns.scatterplot(x=finalDf['principal component 1'],
                y=finalDf['principal component 2'],
                hue=data_labels_pca,
                palette="rainbow").set_title('Agglomerative Clustering Scatter plot for k = 5')
# Agglomerative Clustering and scatter plot with k = 4
clustering_model_pca = AgglomerativeClustering(n_clusters=4, affinity='euclidean', linkage='ward')
clustering_model_pca.fit(finalDf)
data_labels_pca = clustering_model_pca.labels_
sns.scatterplot(x=finalDf['principal component 1'],
                y=finalDf['principal component 2'],
                hue=data_labels_pca,
                palette="rainbow").set_title('Agglomerative Clustering Scatter plot for k = 4')
# Agglomerative Clustering and scatter plot with k = 3
clustering_model_pca = AgglomerativeClustering(n_clusters=3, affinity='euclidean', linkage='ward')
clustering_model_pca.fit(finalDf)
data_labels_pca = clustering_model_pca.labels_
sns.scatterplot(x=finalDf['principal component 1'],
                y=finalDf['principal component 2'],
                hue=data_labels_pca,
                palette="rainbow").set_title('Agglomerative Clustering Scatter plot for k = 3')
# Agglomerative Clustering and scatter plot with k = 2
clustering_model_pca = AgglomerativeClustering(n_clusters=2, affinity='euclidean', linkage='ward')
clustering_model_pca.fit(finalDf)
data_labels_pca = clustering_model_pca.labels_
sns.scatterplot(x=finalDf['principal component 1'],
                y=finalDf['principal component 2'],
                hue=data_labels_pca,
                palette="rainbow").set_title('Agglomerative Clustering Scatter plot for k = 2')

# Evaluating different variations using Silhouette Scores
# Silhouette Scores for 2 clusters
nclusters = 2
km = KMeans(n_clusters=nclusters)
km.fit(x)
y_cluster_kmeans = km.predict(x)
score2 = metrics.silhouette_score(x, y_cluster_kmeans)
print('Silhouette Score for 2 clusters =', score2)
# Silhouette Scores for 3 clusters
nclusters = 3
km = KMeans(n_clusters=nclusters)
km.fit(x)
y_cluster_kmeans = km.predict(x)
score3 = metrics.silhouette_score(x, y_cluster_kmeans)
print('Silhouette Score for 3 clusters =', score3)
# Silhouette Scores for 4 clusters
nclusters = 4
km = KMeans(n_clusters=nclusters)
km.fit(x)
y_cluster_kmeans = km.predict(x)
score4 = metrics.silhouette_score(x, y_cluster_kmeans)
print('Silhouette Score for 4 clusters =', score4)
# Silhouette Scores for 5 clusters
nclusters = 5
km = KMeans(n_clusters=nclusters)
km.fit(x)
y_cluster_kmeans = km.predict(x)
score5 = metrics.silhouette_score(x, y_cluster_kmeans)
print('Silhouette Score for 5 clusters =', score5)

# Visualizing different Silhouette Scores with a bar chart
silhouetteScores = [score2, score3, score4, score5]
clusters = ['2 Clusters', '3 Clusters', '4 Clusters', '5 Clusters']
fig = plt.figure(figsize=(10, 7))
plt.bar(clusters, silhouetteScores, color='red', width=0.4)
plt.xlabel("No. of clusters")
plt.ylabel("Silhouette Score")
plt.title("Silhouette Scores for different no. of clusters")
plt.show()