import pandas as pd
import seaborn as sns
from sklearn import preprocessing
import matplotlib.pyplot as plt
import warnings
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.svm import LinearSVC

# Suppress warnings
warnings.filterwarnings("ignore")

### Question - 1

# Using pandas dataframe
df = pd.read_csv("train.csv")

# Correlation between Survived and Sex
le = preprocessing.LabelEncoder()
df['Sex'] = le.fit_transform(df.Sex.values)
print(df['Survived'].corr(df['Sex']))
# print(df['Sex'].str.get_dummies().corrwith(df['Survived']/df['Survived'].max()))
# We shouldn't keep this feature

# Two visualizations to describe or show correlations - 1st One
df.corr().style.background_gradient(cmap="Greens")

# Two visualizations to describe or show correlations - 2nd One
matrix = df.corr()
# print(matrix)
sns.heatmap(matrix, annot=True, vmax=1, vmin=-1, center=0, cmap='vlag')
plt.show()
# sns.regplot(x=df['Sex'], y=df['Survived'])
# sns.barplot(x=train_df['Sex'], y=train_df['Survived'])

# Implementing Naïve Bayes method using scikit-learn library and report the accuracy
df_train = pd.read_csv('train.csv')
df_test = pd.read_csv('test.csv')
# Join data to analyse and process the set as one.
df_train['train'] = 1
df_test['train'] = 0
df = df_test.append(df_train, sort=False)
features = ['Age', 'Embarked', 'Fare', 'Parch', 'Pclass', 'Sex', 'SibSp']
target = 'Survived'
df = df[features + [target] + ['train']]
# Categorical values need to be transformed into numeric.
df['Sex'] = df['Sex'].replace(["female", "male"], [0, 1])
df['Embarked'] = df['Embarked'].replace(['S', 'C', 'Q'], [1, 2, 3])
train = df.query('train == 1')
test = df.query('train == 0')
# Drop missing values from the train set.
train.dropna(axis=0, inplace=True)
labels = train[target].values
train.drop(['train', target, 'Pclass'], axis=1, inplace=True)
test.drop(['train', target, 'Pclass'], axis=1, inplace=True)

X_train, X_val, Y_train, Y_val = train_test_split(train, labels, test_size=0.2, random_state=1)

# Naïve Bayes
classifier = GaussianNB()
classifier.fit(X_train, Y_train)
y_pred = classifier.predict(X_val)
# Summary of the predictions made by the classifier
print(classification_report(Y_val, y_pred))
print(confusion_matrix(Y_val, y_pred))
# Accuracy score
print('Accuracy is ', accuracy_score(Y_val, y_pred))

### Question - 2

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