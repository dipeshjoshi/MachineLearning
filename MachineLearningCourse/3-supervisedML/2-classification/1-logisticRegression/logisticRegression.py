#impoting libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#Reading dataset
data = pd.read_csv("/Users/z001l92/gitMachineLearning/3-supervisedML/2-classification/Social_Network_Ads.csv")

#Separating dependent and independent variables
X = data.iloc[:, 1:4].values
Y = data.iloc[:, 4].values


#Handling missing data, But no missing data
#print data.describe()


#Categorical casting
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
lbl_x = LabelEncoder()
X[:, 0] = lbl_x.fit_transform(X[:, 0])
enc_x = OneHotEncoder(categorical_features=[0])
X = enc_x.fit_transform(X).toarray()
#print X[0:10]


#Train test split
from sklearn.cross_validation import train_test_split
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=.25)


#feature scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)



#Building model
from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
model.fit(X_train, Y_train)

#pridictions from model
y_pred = model.predict(X_test)
#print y_pred


#Evaluationg using confusion matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(Y_test, y_pred)

print(cm)
