# 🩺 Breast Cancer Dataset Analysis and Model Comparison
A Python-based machine learning project for classifying tumors as malignant or benign using the Breast Cancer dataset. The project demonstrates key concepts in data preprocessing, visualization, model implementation, and performance evaluation.

## 🚀 Features
- **Data Preprocessing**:
  - Normalization of features using `StandardScaler` for equal contribution to models.
  
- **Visualization**:
  - Dimensionality reduction using t-SNE for a 2D representation of the dataset.
  
- **Model Implementation**:
  - Decision Tree Classifier
  - Random Forest Classifier
  - AdaBoost Classifier

- **Performance Metrics**:
  - Accuracy
  - Precision
  - Recall
  - F1-Score
  - Confusion Matrix

## 📊 Dataset
The Breast Cancer dataset from `sklearn.datasets` includes 30 features and labels indicating whether a tumor is benign or malignant.

- **Training and Testing Split**: The dataset is split into training and testing subsets to evaluate model performance.

## 🔧 Requirements
- Python 3.x
- Libraries:
  - `numpy`
  - `pandas`
  - `matplotlib`
  - `seaborn`
  - `sklearn`
## 🏗️ Model Architecture
Three models are implemented for classification:

1. **Decision Tree Classifier**:  
   A basic tree-based model with a maximum depth of 7.

2. **Random Forest Classifier**:  
   An ensemble of 100 decision trees with random feature selection.

3. **AdaBoost Classifier**:  
   An adaptive boosting model with 400 estimators and a learning rate of 0.38.

Each model is trained and tested on normalized features to ensure optimal performance.

---

## 🧪 Experiments Overview
A total of **3 experiments** were conducted to compare the models based on accuracy, precision, recall, and F1-score.

### Best Model
The best performance was achieved with **AdaBoost Classifier**:

**Results**:  
- **Accuracy**: 99.30%  
- **Precision**: 99.31%  
- **Recall**: 99.30%  
- **F1-Score**: 99.30%  

---

### Summary of Results

| Model           | Accuracy  | Precision | Recall    | F1-Score  |
|------------------|-----------|-----------|-----------|-----------|
| Random Forest    | 97.20%    | 97.28%    | 97.20%    | 97.22%    |
| Decision Tree    | 94.40%    | 95.30%    | 94.40%    | 94.53%    |
| **AdaBoost**     | **99.30%**| **99.31%**| **99.30%**| **99.30%** |

---

## 📋 Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/Art1Mal/Brest_Canser_Analysis.git
##📜 *License*
-This project is licensed under the MIT License.
