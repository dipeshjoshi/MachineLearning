import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Reading dataset
data = pd.read_csv("/Users/z001l92/gitMachineLearning/3-supervisedML/2-classification/Social_Network_Ads.csv")
X = data.iloc[:, 1:4].values
Y = data.iloc[:, 4].values

#Categorical casting
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
X_lbl = LabelEncoder()
X[:, 0] = X_lbl.fit_transform(X[:, 0])
X_enc = OneHotEncoder(categorical_features=[0])
X = X_enc.fit_transform(X).toarray()


#Train Test split
from sklearn.cross_validation import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = .25)


#Feature scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)


#Model Building
from sklearn.svm import SVC
model = SVC(kernel = 'linear')
model.fit(X_train, Y_train)

#Predicting output
Y_pred = model.predict(X_test)

#Evaluating results
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(Y_test, Y_pred)
print(cm)
