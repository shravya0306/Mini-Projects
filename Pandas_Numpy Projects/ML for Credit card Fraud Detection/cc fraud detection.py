"""
Credit Card Fraud Detection using Machine Learning

This program builds a machine learning model to detect fraudulent credit card
transactions. Each transaction in the dataset is classified as either normal
or fraudulent.

Workflow of the program:
1. Load the credit card transaction dataset.
2. Inspect the dataset structure and statistics.
3. Check for missing values and data imbalance.
4. Visualize the distribution of fraud vs normal transactions.
5. Separate features (X) and target variable (Class).
6. Split the dataset into training and testing sets.
7. Train a Logistic Regression classification model.
8. Predict whether transactions are fraudulent or normal.
9. Evaluate model performance using accuracy and classification report.
10. Save the trained model for future use.

Technologies used:
- Python
- Pandas and NumPy for data processing
- Scikit-learn for machine learning
- Seaborn and Matplotlib for visualization
"""


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv("creditcard.csv")

print(data.head())
print(data.info())
print(data.describe())

print(data.isnull().sum())

print(data['Class'].value_counts()) #it gives the number of fraud and non-fraud cases

sns.countplot(x='Class', data=data)
plt.title("Fraud vs Normal Transactions")
plt.show()

X = data.drop("Class", axis=1)
y = data["Class"]

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

from sklearn.linear_model import LogisticRegression

model = LogisticRegression(max_iter=2000)

model.fit(X_train, y_train)

predictions = model.predict(X_test)

from sklearn.metrics import accuracy_score, classification_report

accuracy = accuracy_score(y_test, predictions)

print("Accuracy:", accuracy)
print(classification_report(y_test, predictions))


import joblib
joblib.dump(model, "fraud_detection_model.pkl")