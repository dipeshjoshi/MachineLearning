#Import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#reading data
data = pd.read_csv('Salary_data.csv')
#seperating data
X = data.iloc[ : , 0].values
Y = data.iloc[ : , 1].values

print X
print Y

#No Missing values

#No categorical casting

#train test split
from sklearn.cross_validation import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = .3, random_state = 0)

#No feature scaling required

# fitting model
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, Y_train)

# predicting
y_pred = regressor.predict(X_test)

print y_pred
