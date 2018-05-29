'''
There are mainly 5 steps needed in preprocessing.
1. Impute Missing values.
2. Categorocal casting {Encoding Categorocal variables + one hot encoding for creating dummy variables}.
3. train test split.
4. Feature scaling {only if algorithm uses Euclidean distance}.
5. class imbalance problem in classification
'''

#importing libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


#Reading data
data = pd.read_csv('/Users/z001l92/gitMachineLearning/1-preprocessing/Data.csv')
#print data.head(5)

#Separating dependent and independent variables.
X = data.iloc[:,0:3].values
Y = data.iloc[:,3].values

#Handling missing values
from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values='NaN', strategy='mean', axis = 0)
imputer = imputer.fit(X[:, 1:3])
X[:, 1:3] = imputer.transform(X[:, 1:3])

#Categorocal casting
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelEncoder_X = LabelEncoder()
X[:,0] = labelEncoder_X.fit_transform(X[:,0])
oneHotEnc = OneHotEncoder(categorical_features=[0])
X = oneHotEnc.fit_transform(X).toarray()
#Need to encode dependent variable also. Becacuse dependent variable is in string {'yes', 'No'}
labelEncoder_Y = LabelEncoder()
Y = labelEncoder_Y.fit_transform(Y)


#Splitting data in train and test dataset
from sklearn.cross_validation import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = .3)
print X_train
print Y_train


#Feature scaling
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
