#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 14:53:44 2018

@author: z001l92
"""

#Imports
from keras.models import Sequential
from keras.layers import Convolution2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense
from keras.preprocessing.image import ImageDataGenerator



#Initializing neural network.
classifier = Sequential()

#Convolution layer
classifier.add(Convolution2D(32, 3,3, activation='relu', input_shape =(64,64,3))) 

#Pooling layer
classifier.add(MaxPooling2D(pool_size=(2,2)))

#Flattening
classifier.add(Flatten())

#Buidling an Full connection
classifier.add(Dense(output_dim = 128, activation='relu'))

classifier.add(Dense(output_dim = 1, activation= 'sigmoid'))

classifier.compile(optimizer='adam', loss = 'binary_crossentropy', metrics = ['accuracy'])


#Part 2 : REading iamges from directpry and fitting the CNN to the images.
train_datagen = ImageDataGenerator(
        rescale=1./255,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True)

test_datagen = ImageDataGenerator(rescale=1./255)

training_set = train_datagen.flow_from_directory(
        'dataset/training_set',
        target_size=(64,64),
        batch_size=32,
        class_mode='binary')

test_set = test_datagen.flow_from_directory(
        'dataset/test_set',
        target_size=(64, 64),
        batch_size=32,
        class_mode='binary')

classifier.fit_generator(
        training_set,
        steps_per_epoch=8000,
        epochs=25,
        validation_data=test_set,
        validation_steps=2000)