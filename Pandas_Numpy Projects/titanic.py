'''Titanic Survival Prediction Program — Full Explanation

This program builds a machine learning model to predict whether a Titanic passenger survived or not using passenger information like age, class, sex, fare, etc.

The program uses Python, Pandas, NumPy, and Scikit-Learn.

The workflow follows the standard Machine Learning Pipeline:

Load Data → Explore Data → Clean Data → Convert Data → 
Split Data → Train Model → Predict → Evaluate Model'''





import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data=pd.read_csv("train.csv")
print(data.head())    #Shows the first 5 rows of the dataset.
print(data.info())
print(data.describe())  #This gives statistical summary of numeric columns.


print(data.isnull().sum())  #This shows the count of missing values in each column.
data = data.drop(['PassengerId','Name','Cabin','Ticket'], axis=1)  #Dropping columns that are not useful for analysis. axis=1 → remove columns

data['Age'] = data['Age'].fillna(data['Age'].mean()) #Filling missing values in 'Age' column with the mean age.
data['Embarked'] = data['Embarked'].fillna(data['Embarked'].mode()[0]) #Filling missing values in 'Embarked' column with the most frequent value.
data['Fare'] = data['Fare'].fillna(data['Fare'].mean()) #Filling missing values in 'Fare' column with the mean fare.
print(data.isnull().sum())  #Verifying that there are no more missing values.

#convert the variables to numerical values as ml only understands numerical values,this process is called label encoding.
#here sex f=0 and make=1, and for embarked s=0, c=1 and q=2
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()

data['Sex'] = le.fit_transform(data['Sex'])
data['Embarked'] = le.fit_transform(data['Embarked'])
print(data.head())

#we are Predicting whether a passenger survived or not.
X = data.drop("Survived", axis=1)  #this holds all the features except the target variable 'Survived'.
y = data["Survived"]   #this holds the target variable 'Survived' which we want to predict.


#This is where we split the data into training and testing sets.
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42   #80% training data 20% testing data
)    
#here now the data is split into four parts:
#X_train → features for training the model. 
#y_train → target variable for training the model.
#X_test → features for testing the model.
#y_test → target variable for testing the model.

#Train the Model
from sklearn.linear_model import LogisticRegression    #import the ML algorithm

model = LogisticRegression(max_iter=200)   #create the model

model.fit(X_train, y_train)  #This is where learning happens.The model looks at:Passenger data (X_train) and compares it with Actual survival result (y_train)


predictions = model.predict(X_test)  #we give the model new data it hasn't seen before.

#Check Accuracy
from sklearn.metrics import accuracy_score

accuracy = accuracy_score(y_test, predictions)  #Now we compare:Actual survival → y_test andPredicted survival → predictions

print("Model Accuracy:", accuracy)


#Data Visualization

#Survival by Gender
sns.countplot(x='Survived', hue='Sex', data=data)
plt.title("Survival by Gender")
plt.show()

#Survival by Passenger Class
sns.countplot(x='Survived', hue='Pclass', data=data)
plt.title("Survival by Passenger Class")
plt.show()

#Age Distribution
data['Age'].hist(bins=30)
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Count")
plt.show()

#Printing Model Performance

from sklearn.metrics import classification_report

print(classification_report(y_test, predictions))


import joblib

joblib.dump(model, "titanic_model.pkl")