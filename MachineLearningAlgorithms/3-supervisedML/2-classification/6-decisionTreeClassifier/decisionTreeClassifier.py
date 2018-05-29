import pandas as pd
import numpy as np


data = pd.read_csv("/Users/z001l92/gitMachineLearning/3-supervisedML/2-classification/Social_Network_Ads.csv")

X = data.iloc[:, 1:4].values
Y = data.iloc[:, 4].values


#Categorical casting
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
lbl_x = LabelEncoder()
X[:,0] = lbl_x.fit_transform(X[:,0])
ohe_x = OneHotEncoder(categorical_features=[0])
X = ohe_x.fit_transform(X).toarray()
print(X)

#train_test_split
from sklearn.cross_validation import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size = .25)


#building Model
from sklearn.tree import DecisionTreeClassifier
model = DecisionTreeClassifier()
model.fit(X_train,Y_train)

#predicting outputs
Y_pred = model.predict(X_test)

#Evaluating results
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(Y_test, Y_pred)
print(cm)
