# Notebooks

This folder contains the Jupyter Notebook used for experimentation, data preprocessing, feature engineering, model training, and model evaluation for the Silent Burnout AI project.

## File Included

- `silent_burnout_experiment.ipynb`

## Description

The notebook includes the complete machine learning workflow used to build the Silent Burnout AI system.

It covers:

- Loading the dataset
- Data cleaning and preprocessing
- Handling missing values
- Feature engineering from LMS behavioral and academic data
- Train-test splitting
- Model training
- Model comparison
- Evaluation using accuracy, precision, recall, F1-score, confusion matrix, and ROC-AUC
- Saving the final trained model using Joblib

## Models Tested

The notebook compares multiple machine learning algorithms, including:

- Logistic Regression
- Decision Tree
- Random Forest
- K-Nearest Neighbors
- Support Vector Machine
- Gradient Boosting

## Final Model

Gradient Boosting was selected as the final model because it showed better performance and generalization for predicting student disengagement risk.

## Output Files Generated

The notebook generates and saves the following files:

```text
models/gradient_boosting_model.pkl
models/imputer.pkl
models/feature_order.pkl
