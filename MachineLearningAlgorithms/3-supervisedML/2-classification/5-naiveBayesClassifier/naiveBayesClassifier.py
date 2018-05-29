import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#Reading dataset
data = pd.read_csv("/Users/z001l92/gitMachineLearning/3-supervisedML/2-classification/Social_Network_Ads.csv")

X = data.iloc[:, 1:4].values
Y = data.iloc[:, 4].values

#Categorical casting
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
lbe_X = LabelEncoder()
X[:, 0] = lbe_X.fit_transform(X[:, 0])
ohe_X = OneHotEncoder(categorical_features=[0])
X = ohe_X.fit_transform(X).toarray()

#train test split
from sklearn.cross_validation import train_test_split
X_train, X_test, Y_train,Y_test = train_test_split(X,Y,test_size = .25)

#No need of feature scaling, because naive bayes classifier is not based on euclidean distance.

#building a Model
from sklearn.naive_bayes import GaussianNB
model = GaussianNB()
model.fit(X_train,Y_train)

#predict outputs
Y_pred = model.predict(X_test)

#Evaluating results
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(Y_test,Y_pred)
print(cm)
