# https://github.com/Art1Mal/Brest_Canser_Analysis.git
"""
Breast Cancer Dataset Analysis and Model Comparison
"""
"""
Intro:
This script performs data analysis, visualization, and classification using the Breast Cancer dataset from the sklearn library. 
It evaluates three machine learning models: Decision Tree, Random Forest, and AdaBoost. 
The results are compared based on accuracy, precision, recall, F1-score, and confusion matrices.
"""
########################################################
"""
The features of the dataset are normalized using StandardScaler to ensure that each feature contributes equally to the models.
"""
from sklearn.datasets import load_breast_cancer

my_data = load_breast_cancer()

print(my_data.DESCR)

#######################################################
from sklearn.manifold import TSNE
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

###################################
"""
The features of the dataset are normalized using StandardScaler to ensure that each feature contributes equally to the models.
"""
from sklearn.preprocessing import StandardScaler

normalized_data = StandardScaler().fit_transform(my_data.data)
# Using t-SNE for Dimensionality Reduction
"""
t-SNE is applied to reduce the high-dimensional dataset to 2 components for visualization purposes.
"""
visualizaton = TSNE(n_components=2, random_state=70, perplexity=40, n_iter=1500)
vizualizaton_data = visualizaton.fit_transform(normalized_data)

# Creating a DataFrame for visualization
visualizaton_df = pd.DataFrame(np.vstack((vizualizaton_data.T, my_data.target)).T, columns=['X', 'Y', 'label'])
visualizaton_df['label'].replace({0.0: 'Malignant', 1.0: 'Benign'}, inplace=True)

# Data Visualization
"""
A scatter plot is generated using seaborn to visualize the data in two dimensions. 
The data points are colored based on their labels (Malignant or Benign).
"""
sns.FacetGrid(visualizaton_df, hue='label', height=7, palette={'Malignant': 'red', 'Benign': 'green'}).map(
    plt.scatter, 'X', 'Y').add_legend()
plt.title("Visualization of Breast Cancer Dataset")
plt.show()
########################################################
# Model Training
# Train-Test Split
"""
The dataset is split into training and testing subsets.
"""
from sklearn.model_selection import train_test_split

X_train, X_test, Y_train, Y_test = train_test_split(my_data.data, my_data.target, test_size=0.25, random_state=53, )
print(f"Training data: {X_train.shape}, {Y_train.shape}")
print(f"Testing data: {X_test.shape}, {Y_test.shape}")
#########################################################
# Decision Tree Classifier
from sklearn.tree import DecisionTreeClassifier

model_decision_tree = DecisionTreeClassifier(
    criterion='gini',
    max_depth=7,
    min_samples_leaf=30,
    min_samples_split=10,
    splitter='best',
    max_features=None,
    random_state=53
)
model_decision_tree.fit(X_train, Y_train)
#########################################################
# Random Forest Classifier
from sklearn.ensemble import RandomForestClassifier

model_random_forest = RandomForestClassifier(
    criterion='gini',
    n_estimators=100,
    max_depth=10,
    min_samples_split=5,
    min_samples_leaf=3,
    max_features='sqrt',
    random_state=53)
model_random_forest.fit(X_train, Y_train)
########################################################
# AdaBoost Classifier
from sklearn.ensemble import AdaBoostClassifier

model_adaboost = AdaBoostClassifier(
    n_estimators=400,
    learning_rate=0.38,
    algorithm='SAMME.R',
    random_state=63)
model_adaboost.fit(X_train, Y_train)
########################################################
# Model Evaluation
"""
The following metrics are calculated for each model:
Accuracy: Proportion of correctly predicted instances.
Precision: Proportion of true positives among predicted positives.
Recall: Proportion of true positives among actual positives.
F1-Score: Harmonic mean of precision and recall.
Confusion Matrix: Summary of prediction results.
"""
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score

# Generating Predictions with Decision Tree, Random Forest, and AdaBoost Models
random_forest_prediction = model_random_forest.predict(X_test)
decision_tree_prediction = model_decision_tree.predict(X_test)
ada_boost_prediction = model_adaboost.predict(X_test)
# Random Forest Model:
random_forest_accuracy = accuracy_score(Y_test, random_forest_prediction)
random_forest_confusion = confusion_matrix(Y_test, random_forest_prediction)
random_forest_precision = precision_score(Y_test, random_forest_prediction, average='weighted')
random_forest_recall = recall_score(Y_test, random_forest_prediction, average='weighted')
random_forest_f1 = f1_score(Y_test, random_forest_prediction, average='weighted')

print(f"Random Forest Model:")
print(f"Random Forest Accuracy: {random_forest_accuracy}")
print(f"Random Forest Precision: {random_forest_precision}")
print(f"Random Forest Recall: {random_forest_recall}")
print(f"Random Forest F1-Score: {random_forest_f1}")
print(f"Confusion Matrix For Random Forest:{random_forest_confusion}")

# Decision Tree Model:
decision_tree_accuracy = accuracy_score(Y_test, decision_tree_prediction)
decision_tree_confusion = confusion_matrix(Y_test, decision_tree_prediction)
decision_tree_precision = precision_score(Y_test, decision_tree_prediction, average='weighted')
decision_tree_recall = recall_score(Y_test, decision_tree_prediction, average='weighted')
decision_tree_f1 = f1_score(Y_test, decision_tree_prediction, average='weighted')

print(f"Decision Tree Model Results:")
print(f"Decision Tree Accuracy: {decision_tree_accuracy}")
print(f"Decision Tree Precision: {decision_tree_precision}")
print(f"Decision Tree Recall: {decision_tree_recall}")
print(f"Decision Tree F1-Score: {decision_tree_f1}")
print(f"Confusion Matrix For Decision Tree: {decision_tree_confusion}")

# AdaBoost Model:
ada_boost_accuracy = accuracy_score(Y_test, ada_boost_prediction)
ada_boost_confusion = confusion_matrix(Y_test, ada_boost_prediction)
ada_boost_precision = precision_score(Y_test, ada_boost_prediction, average='weighted')
ada_boost_recall = recall_score(Y_test, ada_boost_prediction, average='weighted')
ada_boost_f1 = f1_score(Y_test, ada_boost_prediction, average='weighted')

print(f"AdaBoost Model Results:")
print(f"AdaBoost Accuracy: {ada_boost_accuracy}")
print(f"AdaBoost Precision: {ada_boost_precision}")
print(f"AdaBoost Recall: {ada_boost_recall}")
print(f"AdaBoost F1-Score: {ada_boost_f1}")
print(f"Confusion Matrix For AdaBoost:{ada_boost_confusion}")
###########################################################
results = pd.DataFrame({
    "Model": ["Decision Tree", "Random Forest", "AdaBoost"],
    "Accuracy": [decision_tree_accuracy, random_forest_accuracy, ada_boost_accuracy],
    "Precision": [decision_tree_precision, random_forest_precision, ada_boost_precision],
    "Recall": [decision_tree_recall, random_forest_recall, ada_boost_recall],
    "F1-score": [decision_tree_f1, random_forest_f1, ada_boost_f1]
})
print(results)
if decision_tree_accuracy > random_forest_accuracy and decision_tree_accuracy > ada_boost_accuracy:
    best_model = "Decision Tree"
elif random_forest_accuracy > decision_tree_accuracy and random_forest_accuracy > ada_boost_accuracy:
    best_model = "Random Forest"
else:
    best_model = "AdaBoost"
print(f"The winner: {best_model}")
#############################################################