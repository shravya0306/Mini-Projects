#NLP is a field of Artificial Intelligence and Machine Learning that focuses on helping computers understand, interpret, and process human language.

"""
Spam Detection using Machine Learning (NLP)

This program builds a spam detection model that classifies SMS messages as
'Spam' or 'Ham' (not spam).

Workflow of the program:
1. Load the SMS Spam Collection dataset.
2. Inspect and clean the dataset (handle missing values).
3. Convert text labels (spam/ham) into numeric values.
4. Split the dataset into training and testing sets.
5. Apply NLP using CountVectorizer to convert text messages into numerical features.
6. Train a Naive Bayes classification model on the training data.
7. Use the trained model to predict whether new messages are spam or ham.
8. Evaluate the model using accuracy and classification report.
9. Save the trained model for future use.

Technologies used:
- Python
- Pandas and NumPy for data handling
- Scikit-learn for machine learning
- CountVectorizer for text vectorization (NLP)
"""



import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

#label=spam/ham and message= SMS text
data = pd.read_csv("SMSSpamCollection", sep="\t", names=["label", "message"])

print(data.head())
print(data.info())
print(data.describe())

print(data.isnull().sum())
data["message"] = data["message"].fillna("")
data = data.dropna(subset=["label"])
print(data.isnull().sum())

#Convert Labels to Numbers
from sklearn.preprocessing import LabelEncoder
encoder = LabelEncoder()
data["label"] = encoder.fit_transform(data["label"])

#Features and Target
X = data["message"]
y = data["label"]

#Train/Test Split
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


#Visualize Spam vs Ham
sns.countplot(x='label', data=data)
plt.title("Spam vs Ham Messages")
plt.show()


#Convert Text → Numbers (Start of NLP) : Vectorization
from sklearn.feature_extraction.text import CountVectorizer
vectorizer = CountVectorizer()
X_train = vectorizer.fit_transform(X_train)  #Fit and Transform Training Data
X_test = vectorizer.transform(X_test)   #Only Transform Test Data

#Train Spam Detection Model
#The model learns that certain words strongly indicate spam.
from sklearn.naive_bayes import MultinomialNB
model = MultinomialNB()
model.fit(X_train, y_train)

#Make Predictions
predictions = model.predict(X_test)   #0 → ham and 1 → spam

#Evaluate Model
from sklearn.metrics import accuracy_score, classification_report
accuracy = accuracy_score(y_test, predictions)
print("Accuracy:", accuracy)
print(classification_report(y_test, predictions)) #Creates a Report

#Save the Model
import joblib

joblib.dump(model, "spam_model.pkl")


