import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os

## Check current working directory.
os.getcwd()

## Importing the dataset
dataset = pd.read_csv("Salary_Data.csv")

## Removing last column of original dataset for predictor array + 
## Creating response array (3 = final column)
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 1].values

## Splitting to training and testing
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size = 1/3, random_state = 0)

## Fitting SLR to training
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

y_pred = regressor.predict(X_test)

## Visualizing the result
plt.scatter(X_train,y_train,color = "red")
plt.plot(X_train,regressor.predict(X_train), color = "blue")
plt.title("Salary vs. Experience (Training set)")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.show()

