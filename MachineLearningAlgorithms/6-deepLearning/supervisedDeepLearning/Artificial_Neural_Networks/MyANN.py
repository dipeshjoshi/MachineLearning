#-------------------------------- Preprocessing Steps --------------------------------
import pandas as pd
import numpy as np

#Reading Data
data = pd.read_csv("/Users/z001l92/gitMachineLearning/6-deepLearning/Artificial_Neural_Networks/Churn_Modelling.csv")
X = data.iloc[:, 3:13].values
Y = data.iloc[:, 13].values

#Categorical casting
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
lbl_x1 = LabelEncoder()
X[:, 1] = lbl_x1.fit_transform(X[:, 1])
lbl_x2 = LabelEncoder()
X[:, 2] = lbl_x2.fit_transform(X[:, 2])

#creating dummy variables only for Geography column. Because it is having more then 2 category, No need to create dummy variable for Gender Because label encoder already encoded the values in 0 and 1.
ohe = OneHotEncoder(categorical_features=[1])
X = ohe.fit_transform(X).toarray()
X = X[:, 1:13]
#print(X)

#Train test split
from sklearn.cross_validation import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=.25)

#Feature scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.fit_transform(X_test)

#-------------------------------- Building ANN --------------------------------

#import libraries
import keras
from keras.models import Sequential
from keras.layers import Dense
#initialize ANN
network = Sequential()

#Add input layer and first hidden layer
network.add(Dense(output_dim = 6, init = 'uniform', activation = 'relu', input_dim = 11))

#Adding one more Hidden layers
network.add(Dense(output_dim = 6, init = 'uniform', activation = 'relu'))

#Add output layers
network.add(Dense(output_dim = 1, init = 'uniform', activation = 'sigmoid'))

#compile the network
network.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])

#fit the network to the training Data
network.fit(X_train, Y_train, batch_size = 10, nb_epoch = 100)

#Make a prediction
Y_pred = network.predict(X_test)
Y_pred = (Y_pred > .5)

#Evaluating the model performance
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(Y_test, Y_pred)
print(cm)
