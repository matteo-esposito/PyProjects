import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

#---------------------------------------------------------------#
#   Step 0 | Preprocessing                                      #
#   __________________________________________________________  #
#                                                               #
#       - Predictor and response splitting                      #
#       - Train/test split                                      #
#       - One-hot encoding                                      #
#       - Feature scaling                                       #
#---------------------------------------------------------------#

## Check current working directory.
os.getcwd()

## Importing the dataset
dataset = pd.read_csv("Churn_Modelling.csv")
X = dataset.iloc[:, 3:13].values
y = dataset.iloc[:, 13].values

# Encoding categorical data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

labelencoder_x_1 = LabelEncoder()
X[:, 1] = labelencoder_x_1.fit_transform(X[:, 1])

labelencoder_x_2 = LabelEncoder()
X[:, 2] = labelencoder_x_2.fit_transform(X[:, 2])

# Only need to one hot encode for country not gender (index 1)
onehotencoder = OneHotEncoder(categorical_features = [1])
X = onehotencoder.fit_transform(X).toarray()

# Avoiding the Dummy Variable Trap
X = X[:, 1:]

## Splitting to training and testing
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size = 0.25, random_state = 0)

## Feature scaling
from sklearn.preprocessing import StandardScaler

sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

#---------------------------------------------------------------#
#   Step 1 | Modeling                                           #
#   __________________________________________________________  #
#                                                               #
#       - Artificial Neural Network                             #
#---------------------------------------------------------------#

## Import keras libraries and packages
import keras
from keras.models import Sequential 
from keras.layers import Dense

## Initialize ANN by defining it as a sequence of layers
## Create Sequential object
classifier = Sequential()

## Add input layer and first hidden layer

























