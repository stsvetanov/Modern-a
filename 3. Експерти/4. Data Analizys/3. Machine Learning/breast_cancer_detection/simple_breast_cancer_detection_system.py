# Simple Breast Cancer Detection System

import matplotlib.pyplot as plt
import pandas as pd

# Phase 0 - Data Preparation
from sklearn.datasets import load_breast_cancer

# Import The Breast Cancer Dataset From The SKLearn Library

data = load_breast_cancer()

# Convert The SkLearn Bunch Object To Pandas DataFrame

print(data.feature_names)

dataset = pd.DataFrame(data.data, data.target, columns=data.feature_names)
dataset['target'] = data.target

print(dataset.head(7))
print(dataset.tail())

input("Press enter to continue.")

# Data Exploration

X = dataset.iloc[:, 0:29].values
Y = dataset.iloc[:, 30].values

print('Breast Cancer Dataset Dimensions: {}'.format(dataset.shape))

"""**The Number Of Patients Who Have Cancer Versus Those Who Do Not Have Cancer**"""

print(dataset['target'].value_counts())

"""**1 - Benign; 0 - Malignant**

**Visualizing The Data**
"""

num_bins = 10
dataset.hist(bins=num_bins, figsize=(20,15))
plt.savefig("hr_histogram_plots")
plt.show()

"""**Finding Missing Data**"""

dataset.isnull().sum()

dataset.isna().sum()

"""**Splitting The Dataset**"""

from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.25, 
                                                    random_state = 0)

"""**Feature Scaling**"""

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()

X_train = sc.fit_transform(X_train)
X_test = sc.fit_transform(X_test)

"""**Using Logistic Regression To Train The Model**"""

from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression(random_state = 0)

classifier.fit(X_train, Y_train)

Y_pred = classifier.predict(X_test)

"""**Compute Accuracy Of Logistic Regression**"""

import seaborn as sns
def seaborn_plot_cm(cm, model_name):
  sns.heatmap(cm, annot = True, fmt = '.2f', 
            xticklabels = ['Benign', 'Malignant'], yticklabels = ['Benign', 'Malignant'])
  plt.ylabel('True Class')
  plt.xlabel('Predicted Class')

  plt.title(model_name)
  plt.savefig(model_name)

from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
def print_classification_report(classifier_name, Y_pred, Y_test):
  print(classifier_name + ' Accuracy: {:.3f}'.format(accuracy_score(Y_test, 
                                                                   Y_pred)))

  cm = confusion_matrix(Y_test, Y_pred)
  print(classification_report(Y_test, Y_pred))
  seaborn_plot_cm(cm, classifier_name)

print_classification_report('Logistic Regression', Y_pred, Y_test)

"""**Using KNearest Neighbors To Train The Model**"""

from sklearn.neighbors import KNeighborsClassifier
kneighbors_classifier = KNeighborsClassifier(n_neighbors = 5, 
                                             metric = 'minkowski', p = 2)

kneighbors_classifier.fit(X_train, Y_train)

kNeighbors_Y_pred = kneighbors_classifier.predict(X_test)

print_classification_report('KNeighbors', kNeighbors_Y_pred, Y_test)

"""**Using SVM To Train The Model**"""

from sklearn.svm import SVC
svm_classifier = SVC(kernel = 'linear', random_state = 0)
svm_classifier.fit(X_train, Y_train)

svm_Y_pred = svm_classifier.predict(X_test)

print_classification_report('SVM', svm_Y_pred, Y_test)

"""**Using Gaussian Naive Bayes To Train The Model**"""

from sklearn.naive_bayes import GaussianNB
gbNB_classifier = GaussianNB()

gbNB_classifier.fit(X_train, Y_train)

gb_NB_Y_pred = gbNB_classifier.predict(X_test)
print_classification_report('Gaussian Naive Bayes', gb_NB_Y_pred, Y_test)

"""**Using Decision Tree To Train The Model**"""

from sklearn.tree import DecisionTreeClassifier
dc_tree_classifier = DecisionTreeClassifier()

dc_tree_classifier.fit(X_train, Y_train)

dc_tree_Y_pred = dc_tree_classifier.predict(X_test)
print_classification_report('Decision Tree', dc_tree_Y_pred, Y_test)

"""**Using Random Forest To Train The Model**"""

from sklearn.ensemble import RandomForestClassifier
rd_forest_classifier = RandomForestClassifier(n_estimators = 10, 
                                              criterion = 'entropy', 
                                              random_state = 0)

rd_forest_classifier.fit(X_train, Y_train)

rd_forest_Y_pred = rd_forest_classifier.predict(X_test)
print_classification_report('Random Forest', rd_forest_Y_pred, Y_test)

