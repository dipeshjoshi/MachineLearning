#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 17:22:18 2018

@author: z001l92
"""
#Imports
from keras.models import Sequential
from keras.layers import LSTM
from keras.layers import Dense
from keras.layers import Dropout

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler

#Read dataset.
input_data_train = pd.read_csv("Google_Stock_Price_Train.csv")
training_set = input_data_train.iloc[:,1:2].values
 

#Feature Scaling 
sc = MinMaxScaler(feature_range=(0,1))
scaled_training_set = sc.fit_transform(training_set)


#Creating data structure with 60 timesteps and 1 output
X_train = []
Y_train = []

for index in range(60, len(scaled_training_set)):
    X_train.append(scaled_training_set[index-60:index, 0])
    Y_train.append(scaled_training_set[index, 0])

X_train = np.array(X_train)
Y_train = np.array(Y_train)   

#Reshaping
X_train = np.reshape(X_train, (X_train.shape[0], X_train.shape[1], 1))

#Create RNN Architechture
regressor = Sequential()

# DOUBT HERE
#Adding First LSTM Layer and some dropout regularization. 
regressor.add(LSTM(units= 100, return_sequences= True, input_shape = (X_train.shape[1],1)))
regressor.add(Dropout(.2))

#Adding Second LSTM Layer and some dropout regularization. 
regressor.add(LSTM(units= 100, return_sequences= True))
regressor.add(Dropout(.2))

#Adding Third LSTM Layer and some dropout regularization. 
regressor.add(LSTM(units= 100, return_sequences= True))
regressor.add(Dropout(.2))

#Adding Fourth LSTM Layer and some dropout regularization. 
regressor.add(LSTM(units= 100))
regressor.add(Dropout(.2))

#Adding output Layer
regressor.add(Dense(units = 1))

#Compiling the network
regressor.compile(optimizer = 'adam', loss='mean_squared_error')

#FItting the RNN to the training set
regressor.fit(X_train, Y_train, epochs=100, batch_size=32)



#making the prediction and visualising the results

#Getting the Actual stock price
input_data_test = pd.read_csv("Google_Stock_Price_Test.csv")
testing_set = input_data_test.iloc[:, 1:2].values

#Getting predicted results for stock price of 2017
total_data_set = pd.concat((input_data_train['Open'], input_data_test['Open']), axis=0)
inputs = total_data_set[len(total_data_set) - len(input_data_test)-60 : ].values
inputs = inputs.reshape(-1,1)
inputs = sc.transform(inputs)

X_test = []
for index in range(60,80):
    X_test.append(inputs[index-60:index, 0])
X_test = np.array(X_test)
X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))

predicted_stock_price = regressor.predict(X_test)
predicted_stock_price = sc.inverse_transform(predicted_stock_price)

#Visulising the result.
plt.plot(testing_set, color = 'green', label = 'Acutual google stock price')
plt.plot(predicted_stock_price, color = 'blue', label = 'Predicted google stock price')
plt.title('Google stock price prediction')
plt.xlabel('Time')
plt.ylabel('Google stock price')
plt.legend()
plt.show()
 