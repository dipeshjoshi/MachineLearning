#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 15:55:25 2018

@author: z001l92
"""



"""
This is the phase 1 of the project in which we will do following: [Only one item]
    1. We will preprocess our data to make time series (By including lags as column of our input data.)
    2. We will Define our network and train our model
    3. We will do static validation of test set. By static i mean, we will be training our model only once and will make 10 weeks predictions with the same trained model. 
    4. Visualize the result
    5. Calculate the error matrics. 
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler

from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers import Dropout


# STEP 1 : PREPROCESSING DATA.
item_id = 1014588337
pivot_dt = '2018-07-28'
lags = 52

#Reading dataset
data = pd.read_csv("Dl_dataset100.csv")
data = data[data['ecom_item_i'] == item_id].sort_values(by='week_end_date')
train_data = data[data['week_end_date'] < pivot_dt]
test_data = data[data['week_end_date'] >= pivot_dt]


train_data = train_data.iloc[:, 3:4].values
test_data = test_data.iloc[:, 3:4].values

#Scale training and testing data

sc = MinMaxScaler()
scaled_train_data = sc.fit_transform(train_data)
scaled_test_data = sc.fit_transform(test_data)


#Prepare training data
X_train = []
Y_train = []

print(scaled_train_data[0:60,0])

for index in range(lags , len(scaled_train_data)):
    X_train.append(scaled_train_data[index-lags : index, 0])
    Y_train.append(scaled_train_data[index, 0])
    
X_train = np.array(X_train)
Y_train = np.array(Y_train)


#Reshaping input training data
X_train = np.reshape(X_train, (X_train.shape[0], X_train.shape[1], 1))


#STEP 2 : DEFINING NETWORK AND TRAINING OUR MODEL.
model = Sequential()
model.add(LSTM(units = 100, return_sequences=True, input_shape = (X_train.shape[1], 1)))
model.add(Dropout(.2))


model.add(LSTM(units = 100, return_sequences=True))
model.add(Dropout(.2))


model.add(LSTM(units = 100, return_sequences=True))
model.add(Dropout(.2))


model.add(LSTM(units = 100))
model.add(Dropout(.2))

model.add(Dense(units=1))

# Compiling the RNN
model.compile(optimizer = 'adam', loss = 'mean_squared_error')

# Fitting the RNN to the Training set
model.fit(X_train, Y_train, epochs = 100, batch_size = 32)




#STEP 3 : MAKING PREDICTIONS AND STATIC VALIDATION.

predictions = []

full_data = data.iloc[:,3:4].values
full_data = full_data.reshape(-1,1)
full_data = sc.transform(full_data)



for index in range(len(scaled_train_data),len(full_data)):
    current_week_data = full_data[index-lags:index,0]
    current_week_data = np.array(current_week_data)
    current_week_data = np.reshape(current_week_data, (1,52,1))
    pred = model.predict(current_week_data)[0]
    predictions.append(sc.inverse_transform(pred[0]))

predictions = np.array(predictions)
predictions = predictions.reshape((10,1))


#STEP 4 : VISULIZING RESULTS.
plt.plot(test_data, color = 'red', label = 'Actual Demand')
plt.plot(predictions, color = 'green', label = 'Predicted Demand')
plt.title("Item Demand Forecasting")
plt.xlabel('Week number')
plt.ylabel('Demand of item')
plt.legend()
plt.show()


'''
tmp = full_data[129:181,0]
tmp = np.array(tmp)
tmp = np.reshape(tmp, (1,52,1))
pred = model.predict(tmp)
pred = sc.inverse_transform(pred)
'''


#STEP 5 : CALCULATE ERROR MATRICS.
mse = ((test_data - predictions) ** 2).mean(axis = 0)








