setwd("~/gitMachineLearning/3-supervisedML/1-regression/4-supportVectorRegressor")

input_df <- read.csv("Position_Salaries.csv")

input_df <- input_df[2:3]

#building model
#install.library("e1071")
library(e1071)

model <- svm(formula = Salary ~ Level, data = input_df, type = "eps-regression")

library(ggplot2)

ggplot()+
  geom_point(aes(x = input_df$Level, y = input_df$Salary), color = 'red') +
  geom_line(aes(x = input_df$Level, y = predict(model, input_df)), color = 'black') + 
  ggtitle("Actual Vs predicted") + 
  xlab("Level") + 
  ylab("Salary")