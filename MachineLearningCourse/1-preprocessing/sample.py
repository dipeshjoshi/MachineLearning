#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  8 02:02:44 2018

@author: z001l92
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


#Reading data
data = pd.read_csv("data.csv")

#Separating dependent and independent variables
X = data.iloc[:,0:3].values
Y = data.iloc[:,3].values

#Handling Missing value
from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values='NaN', strategy="mean", axis=0)
imputer = imputer.fit(X[:,1:3])
X[:, 1:3] = imputer.transform(X[:,1:3])


#Categorical casting
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

labelEnc_X = LabelEncoder()
X[:, 0] = labelEnc_X.fit_transform(X[:, 0])
oneHotEnc = OneHotEncoder(categorical_features=[0])
X = oneHotEnc.fit_transform(X).toarray()
labelEnc_Y = LabelEncoder()
Y = labelEnc_Y.fit_transform(Y)


#Splitting data into training and testing data
from sklearn.cross_validation import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size = 0.3)


#Fature scaling
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
