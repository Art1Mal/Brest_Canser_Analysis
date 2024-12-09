Breast Cancer Dataset Analysis and Model Comparison

Overview
This project analyzes the Breast Cancer dataset from the sklearn library. 
It performs data preprocessing, visualization, and classification using three machine learning models: Decision Tree, Random Forest, and AdaBoost. 
The models are compared based on accuracy, precision, recall, F1-score, and confusion matrices.

Features:
* Dataset Visualization: The dataset is visualized in 2D using t-SNE for dimensionality reduction.
* Model Training: Three machine learning models are implemented:
  **Decision Tree
  **Random Forest
  **AdaBoost
* Model Evaluation: The models are compared using multiple performance metrics, including confusion matrices.

Code Breakdown

Data Preprocessing:
* The dataset is normalized using StandardScaler to ensure that all features contribute equally to the models.
Visualization:
* t-SNE: Reduces the high-dimensional dataset to 2 dimensions for visualization.
* Scatter Plot: Data points are color-coded as "Malignant" or "Benign".
Models:
* Decision Tree: Configured with max_depth=7, min_samples_leaf=30, and min_samples_split=10.
* Random Forest: Configured with 100 estimators and max_depth=10.
* AdaBoost: Configured with 400 estimators and a learning rate of 0.38.
Evaluation Metrics:
* Accuracy
* Precision
* Recall
* F1-Score
* Confusion Matrix

Example Output:

Sample output includes:
Random Forest Model:
Accuracy: 0.95
Precision: 0.96
Recall: 0.95
F1-Score: 0.95
Confusion Matrix:
[[52,  1],
 [ 2, 88]]
...
Requirements:
* Python 3.8+
* Libraries:
  ** scikit-learn
  ** pandas
  ** numpy
  ** matplotlib
  ** seaborn

Dataset
The Breast Cancer dataset is a built-in dataset from sklearn.datasets. It includes:
* Features: 30 numeric features
* Labels: Binary classification (“Malignant” or “Benign”)

Results
The project provides insights into the performance of each model. The results are useful for selecting the best algorithm for similar classification tasks.

Contributions
Feel free to submit issues or pull requests to improve this project.
