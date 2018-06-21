import pandas as pd
import numpy as np


data = pd.read_csv("/Users/z001l92/gitMachineLearning/3-supervisedML/2-classification/HealthyfyMedata.csv")

data = data[data['gender'].isnull() == False]



#Making proper data frame
col_name = ['gender', 'age', 'start_bmi', 'activity_factor', 'OS', 'hypothyroid', 'diabetes', 'pcos', 'physical', 'hypertension', 'high_blood_pressure', 'cholesterol', 'medical_conditions', 'devicebrand', 'paid']
data = data[col_name]
#To Know which columns has missing values.
#print(data.isnull().any()) # Age, start_bmi and activity_factor has some missing values.

X = data.iloc[:,0:14].values
Y = data.iloc[:,14].values

#Imputation of missing values
from sklearn.preprocessing import Imputer
imp = Imputer(missing_values='NaN', strategy='mean', axis=0)
X[:, 1:4] = imp.fit_transform(X[:, 1:4])

#Converting numpy array to dataframe again to check if any missing values is still there or not?
tmp = pd.DataFrame(X)
#print(tmp.isnull().any())

#Categorical casting
#If Categorical variable having binary values then only use LabelEncoder, Otherwise use both LabelEncoder and OneHotEncoder to create dummy variable. But when you use OneHotEncoder dont forget to delete one dummy variable to get rid of dummy variable trap.
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
lbl_gender =  LabelEncoder()
X[:,0] = lbl_gender.fit_transform(X[:,0])
lbl_OS = LabelEncoder()
X[:,4] = lbl_OS.fit_transform(X[:,4])
lbl_deviceBrand = LabelEncoder()
X[:,13] = lbl_deviceBrand.fit_transform(X[:,13])

ohe_OS = OneHotEncoder(categorical_features = [0])
X = ohe_OS.fit_transform(X).toarray()
X = X[:,1:]   # Removing one dummy variable.
print(X[0:10,0:5])

ohe_OS = OneHotEncoder(categorical_features = [4])
X = ohe_OS.fit_transform(X).toarray()
X = X[:, 1:] # Removing one dummy variable.
print(X[0:10,0:5])

ohe_OS = OneHotEncoder(categorical_features = [14])
X = ohe_OS.fit_transform(X).toarray()
X = X[:, 1:] # Removing one dummy variable.
print(X)


#Removing one dummy variable for each Categorical Feature.
tmp = pd.DataFrame(X)
print(tmp)
