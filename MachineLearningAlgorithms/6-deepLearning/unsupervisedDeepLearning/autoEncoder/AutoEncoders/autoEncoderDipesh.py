#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 13:22:08 2019

@author: z001l92
"""

import numpy as np
import pandas as pd
import torch
# for Nueral network
import torch.nn as nn
#For parallel computation
import torch.nn.parallel
#For optimiser
import torch.optim as optim
import torch.utils.data
#For stochastic gradient descent
from torch.autograd import variable


#Importing dataset
movies = pd.read_csv('ml-1m/movies.dat', sep = '::', header = None, engine = 'python', encoding = 'latin-1')   
ratings = pd.read_csv('ml-1m/ratings.dat', sep = '::', header = None, engine = 'python', encoding = 'latin-1')   
users = pd.read_csv('ml-1m/users.dat', sep = '::', header = None, engine = 'python', encoding = 'latin-1')  

#Preparing training and test set
training_set = pd.read_csv('ml-100k/u1.base', delimiter = '\t',header = None)
training_set = np.array(training_set)

test_set = pd.read_csv('ml-100k/u1.test', delimiter = '\t', header = None)
test_set = np.array(test_set)

#Getting number of users and movies 
nb_users = int(max( max(training_set[:,0]), max(test_set[:,0])))
nb_movies = int(max( max(training_set[:,1]), max(test_set[:,1])))


#Creating matrix 
def convert(data):
    mat = []
    for u in range(1, nb_users+1):
        row = np.zeros(nb_movies)
        mov = data[:,1][data[:,0] == u]
        rat = data[:,2][data[:,0] == u]
        row[mov-1] = rat
        mat.append(row)
    return mat
        
        
training_set = convert(training_set)
test_set = convert(test_set)


#Converting data into torch tensors
training_set = torch.FloatTensor(training_set)
test_set = torch.FloatTensor(test_set)

#Creating architecture of Neural network.
class SAE(nn.Module):
    def __init__(self, ):
        super(SAE, self).__init__()
        self.fc1 = nn.Linear(nb_movies, 20)
        self.fc2 = nn.Linear(20, 10)
        self.fc3 = nn.Linear(10, 20)
        self.fc4 = nn.Linear(20, nb_movies)
        self.activation = nn.Sigmoid()
    
    def forward(self, x):
        x = self.activation(self.fc1(x))
        x = self.activation(self.fc2(x))
        x = self.activation(self.fc3(x))
        x = self.fc4(x)
        return x
    
sae = SAE()
criterion = nn.MSELoss()
optimizer = optim.RMSprop(sae.parameters(), lr = 0.01, weight_decay = 0.5)

#Tarining SAE
nb_epochs = 200
for epoch in range(1, nb_epochs + 1):
    train_loss = 0
    s = 0.
    for u in range(nb_users):
        inputdata = variable(training_set[u]).unsqueeze(0)  
        target = inputdata.clone()
        if torch.sum(target.data > 0) > 0:
            output = sae(inputdata)
            target.require_grad = False
            output[target == 0] = 0
            loss = criterion(output, target)
            mean_corrector = nb_movies / float(torch.sum(target.data > 0) + 1e-10)
            loss.backward()
            train_loss = np.sqrt(loss.item() * mean_corrector)
            s += 1.
            optimizer.step()    
    print('epoch : ' + str(epoch) + ' loss : ' + str(train_loss / s))
            
                


#Testing SAE

        
        
                
        
