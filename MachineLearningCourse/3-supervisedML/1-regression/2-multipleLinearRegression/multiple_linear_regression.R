setwd("~/gitMachineLearning/3-supervisedML/1-regression/2-multipleLinearRegression")

input_df <- read.csv("50_Startups.csv", stringsAsFactors = FALSE)

#1. Categorical casting
input_df$State <- as.factor(input_df$State)


#2. divide in train test split
#install.packages("caTools")
library('caTools')
ind <- sample.split(Y = input_df$Profit, SplitRatio = .8)
train_data <- input_df[ind == TRUE, ]
test_data <- input_df[ind == FALSE, ]

#3. model building
model <- lm(train_data$Profit ~ ., data = train_data)
y_pred <- predict(model, newdata = test_data)

#4. Error calculations
#RMSE
difference <- test_data$Profit - y_pred

rmse <- sqrt(mean(difference^2))

#MAPE
mape <- mean(abs(difference/test_data$Profit)) * 100

#MSE
mse <- mean(difference^2)

