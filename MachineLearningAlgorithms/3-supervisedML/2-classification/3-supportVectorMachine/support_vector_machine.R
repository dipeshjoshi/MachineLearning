setwd("~/gitMachineLearning/3-supervisedML/2-classification/")

input_df <- read.csv("Social_Network_Ads.csv", stringsAsFactors = FALSE)

input_df <- input_df[2:5]

#Categorical casting
input_df$Gender <- as.numeric(factor(input_df$Gender, 
                                     levels = c('Male', 'Female'),
                                     labels = c(1,2)))
input_df$Purchased <- as.factor(input_df$Purchased)

#Splitting in train and test set
library(caTools)
ind <- sample.split(input_df$Purchased, SplitRatio = .8)
train_set <- input_df[ind == TRUE, ]
test_set <- input_df[ind == FALSE, ]

#Feature scaling
train_set[-4] <- scale(train_set[-4])
test_set[-4] <- scale(test_set[-4])

#model building
#install.packages("e1071")
library(e1071)
model <- svm(formula = Purchased ~ . , 
             data = train_set,
             type = 'C-classification', # Default type for classification is C-classification.
             kernel = "linear")
y_pred <- predict(model, newdata = test_set )

#Evaluation by confusion matrix
cm <- table(y_pred, test_set$Purchased)