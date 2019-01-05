#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 18:54:47 2018

@author: z001l92
"""

import pandas as pd

lags = 52
item = 1014588337
pivot_dt = '2018-07-28'

#Read dataset 
dataset = pd.read_csv('Dl_dataset100.csv')
dataset = dataset[dataset['ecom_item_i'] == item ].sort_values(by = 'week_end_date')
dataset_train = dataset[dataset['week_end_date'] < pivot_dt].values
dataset_test = dataset[dataset['week_end_date'] >= pivot_dt].values

X_train = []
Y_train = []

for index in range(lags, len(dataset_train)):
    X_train.append(dataset_train[index-lags:index, 3])
    Y_train.append(dataset_train[index, 3])

X_train = np.array(X_train)
Y_train = np.array(Y_train)