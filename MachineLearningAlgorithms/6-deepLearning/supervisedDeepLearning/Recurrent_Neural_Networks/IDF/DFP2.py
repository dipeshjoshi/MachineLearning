#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 17:13:23 2018

@author: z001l92
"""

"""
1. We will be adding more additional features other then lags.

2. In this phase we will do dynamic validation. Means as soon as we get the testing data row we will predict for that and for next testing observation we will take this predicted demand as input.
That is, for predicting t+1 demand we will take t predicted demand as input
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from keras.models import Sequential
from keras.layers import LSTM
from keras.layers import Dropout
from keras.layers import Dense


#Preprocessing data
item_id = 1014588337
pivot_dt = '2018-07-28'
lags = 52

data = pd.read_csv("Dl_dataset100.csv")
train_data = data[(data['week_end_date'] < pivot_dt) & (data['ecom_item_i'] == item_id)].sort_values(by = 'week_end_date')
test_data = data[(data['week_end_date'] >= pivot_dt) & (data['ecom_item_i'] == item_id)].sort_values(by = 'week_end_date')

ind = range(3,55)

ind = ind[:1] + ind[2:]

train_data = train_data.iloc[:,ind]


