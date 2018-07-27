import numpy as np
import pandas as pd
import os

## Check current working directory.
os.getcwd()

## Importing the dataset
dataset = pd.read_csv("50_Startups.csv")

## Removing last column of original dataset for predictor array + 
## Creating response array (3 = final column)
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 4].values

# Encoding categorical data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder = LabelEncoder()
X[:, 3] = labelencoder.fit_transform(X[:, 3])
onehotencoder = OneHotEncoder(categorical_features = [3])
X = onehotencoder.fit_transform(X).toarray()

# Avoiding the Dummy Variable Trap
X = X[:, 1:]

## Splitting to training and testing
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size = 0.2, random_state = 0)

## Fitting MLR to training
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

## Prediction of test set results
y_pred = regressor.predict(X_test)

## Optimizing model using backward elimination
import statsmodels.formula.api as sm

## Add column of 1's in X matrix, in Y = XB for multiple linear regression
X = np.append(arr = np.ones((50,1)).astype(int), values = X, axis = 1) # 1 for column, 0 for row










