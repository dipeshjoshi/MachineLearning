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
model <- glm(formula = Purchased ~ . , 
             data = train_set,
             family = 'binomial')

prob_preds <- predict( model, newdata = test_set[-4], type = 'response')

y_pred <- ifelse(prob_preds > 0.5, 1, 0)

#Evaluation by confusion matrix
cm <- table(y_pred, test_set$Purchased)