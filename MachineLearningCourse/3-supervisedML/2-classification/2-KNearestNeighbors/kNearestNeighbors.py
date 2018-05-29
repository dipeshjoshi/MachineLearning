import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#Reading dataset
data = pd.read_csv("/Users/z001l92/gitMachineLearning/3-supervisedML/2-classification/Social_Network_Ads.csv")

#breaking into dependent and independent variables
X = data.iloc[:, 2:4].values
Y = data.iloc[:, 4].values


#Missing values imputation.

#Categorical casting
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
X_lbl = LabelEncoder()
X[:, 0] = X_lbl.fit_transform(X[:, 0])

X_enc = OneHotEncoder(categorical_features=[0])
X = X_enc.fit_transform(X).toarray()


#train test split
from sklearn.cross_validation import train_test_split
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size = .25)


#Feature scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)


#model Building
from sklearn.neighbors import KNeighborsClassifier
model = KNeighborsClassifier(n_neighbors = 5, metric = 'minkowski', p=2)
model.fit(X_train, Y_train)

#predict output
Y_pred = model.predict(X_test)


#Evaluating output
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(Y_test, Y_pred)
print(cm)
