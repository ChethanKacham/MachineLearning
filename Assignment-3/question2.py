import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.svm import LinearSVC

# Suppress warnings
warnings.filterwarnings("ignore")

# Using pandas dataframe
glass = pd.read_csv("glass.csv")

# Two visualizations to describe or show correlations - 1st One
glass.corr().style.background_gradient(cmap="Greens")

# Two visualizations to describe or show correlations - 2nd One
matrix = glass.corr()
#print(matrix)
sns.heatmap(matrix, annot=True, vmax=1, vmin=-1, center=0, cmap='vlag')
plt.show()

features = ['Rl', 'Na', 'Mg', 'Al', 'Si', 'K', 'Ca', 'Ba', 'Fe']
target = 'Type'

X_train, X_val, Y_train, Y_val = train_test_split(glass[::-1], glass['Type'], test_size=0.2, random_state=1)

# Implementing Naïve Bayes method using scikit-learn library and report the accuracy

classifier = GaussianNB()
classifier.fit(X_train, Y_train)
y_pred = classifier.predict(X_val)
# Summary of the predictions made by the classifier
print(classification_report(Y_val, y_pred))
print(confusion_matrix(Y_val, y_pred))
# Accuracy score
print('Accuracy is', accuracy_score(Y_val, y_pred))


# Implementing Linear SVM method using scikit-learn library and report the accuracy

classifier = LinearSVC()
classifier.fit(X_train, Y_train)
y_pred = classifier.predict(X_val)
# Summary of the predictions made by the classifier
print(classification_report(Y_val, y_pred))
print(confusion_matrix(Y_val, y_pred))
# Accuracy score
print('Accuracy is', accuracy_score(Y_val, y_pred))