#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 10:45:52 2018

@author: z001l92
"""

from keras.models import Sequential
from keras.layers import LSTM
from keras.layers import Dense
from keras.layers import Dropout

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
import datetime as dt


pivot_dt = '2018-07-28'
#Read dataset.
dataset = pd.read_csv("Dl_dataset100.csv")
dataset = dataset[(dataset['ecom_item_i'] == 1014588337)].sort_values(by = 'week_end_date')
train_dataset = dataset[dataset['week_end_date'] < pivot_dt]
test_dataset = dataset[dataset['week_end_date'] >= pivot_dt]


train_d = train_dataset.iloc[:, 3:4].values
test_d = test_dataset.iloc[:, 3:4].values

#Feature Scaling
sc = MinMaxScaler(feature_range=(0,1))
scaled_training_set = sc.fit_transform(train_d)


#Creating data structure with 60 timesteps and 1 output
X_train = []
Y_train = []

lags = 52
for index in range(lags, len(scaled_training_set)):
    X_train.append(scaled_training_set[index-lags:index, 0])
    Y_train.append(scaled_training_set[index, 0])

X_train = np.array(X_train)
Y_train = np.array(Y_train)   


#Reshaping
X_train = np.reshape(X_train, (X_train.shape[0], X_train.shape[1], 1))

regressor = Sequential()

regressor.add(LSTM(units = 200, return_sequences= True, input_shape = (X_train.shape[1], 1)))
regressor.add(Dropout(.2))

regressor.add(LSTM(units = 200, return_sequences= True))
regressor.add(Dropout(.2))

regressor.add(LSTM(units = 200, return_sequences= True))
regressor.add(Dropout(.2))

regressor.add(LSTM(units = 200, return_sequences= True))
regressor.add(Dropout(.2))

regressor.add(LSTM(units = 200))
regressor.add(Dropout(.2))

#Adding output Layer
regressor.add(Dense(units = 1))

#Compiling the network
regressor.compile(optimizer = 'adam', loss='mean_squared_error')

#FItting the RNN to the training set
regressor.fit(X_train, Y_train, epochs=100, batch_size=32)



#making the prediction and visualising the results
#getting predicted results


pivot_dt = dt.datetime.strptime(pivot_dt, '%Y-%m-%d')
start_dt = pivot_dt + dt.timedelta(weeks = -52)
start_dt = dt.datetime.strftime(start_dt,'%Y-%m-%d' )

inputs = dataset[dataset['week_end_date'] >= start_dt]
inputs = inputs.iloc[:, 3:4].values
inputs = inputs.reshape(-1,1)
inputs = sc.transform(inputs)

X_test = []

for index in range(52, 62):
    X_test.append(inputs[index-52 : index, 0])
X_test = np.array(X_test)
X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))

predicted_demand = regressor.predict(X_test)
predicted_demand = sc.inverse_transform(predicted_demand)
    

plt.plot(test_d, color = 'green', label = 'Acutual Demand')
plt.plot(predicted_demand, color = 'blue', label = 'Predicted Demand')
plt.title('Item Demand Forecasting')
plt.xlabel('Time')
plt.ylabel('Demand')
plt.legend()
plt.show()