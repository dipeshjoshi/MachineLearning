setwd("~/Dipesh/study/machineLearning/udemy/Machine Learning A-Z Template Folder/Part 8 - Deep Learning/Section 39 - Artificial Neural Networks (ANN)")

input_df <- read.csv("Churn_Modelling.csv", stringsAsFactors = FALSE)

input_df <- input_df[4:14]

#checking missing values
table(is.na(input_df))

#categorical casting
input_df$Geography <- as.numeric(factor(input_df$Geography, 
                                        levels = c("France", "Germany", "Spain"), 
                                        labels = c(1,2,3)))
input_df$Gender <- as.numeric(factor(input_df$Gender, 
                                     levels = c('Male', 'Female'), 
                                     labels = c(1,2)))


#feature scaling
input_df[-11] <- scale(input_df[-11])


#splitting data in train and test
library(caTools)
split <- sample.split(input_df$Exited, SplitRatio = .7)
train_set <- input_df[split == TRUE, ]
test_set <- input_df[split == FALSE, ]

#Creating Nueral Network
#install.packages("h2o")
library(h2o)
h2o.init(nthreads = -1)
model <- h2o.deeplearning(y = 'Exited', 
                          training_frame = as.h2o(train_set),
                          activation = 'Rectifier', 
                          hidden = c(6,6),
                          epochs = 100,
                          train_samples_per_iteration = -2)
prob_predict <- h2o.predict(model, newdata = as.h2o(test_set))
y_pred <- ifelse(prob_predict > .5, 1, 0)
y_pred <- as.vector(y_pred)

#Evaluation
cm <- table(y_pred, test_set[, 11])

h2o.shutdown()