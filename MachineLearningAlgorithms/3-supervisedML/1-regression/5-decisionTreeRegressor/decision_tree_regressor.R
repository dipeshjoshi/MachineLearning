setwd("~/gitMachineLearning/3-supervisedML/1-regression/5-decisionTreeRegressor")

input_df <- read.csv("Position_Salaries.csv")

input_df <- input_df[2:3]

#building model
#install.packages("rpart")
library(rpart)

model <- rpart(formula = Salary ~ Level, data = input_df, control = rpart.control(minsplit = 1))

ggplot()+
  geom_point(aes(x = input_df$Level, y = input_df$Salary), color = 'red') +
  geom_line(aes(x = input_df$Level, y = predict(model, input_df)), color = 'black') + 
  ggtitle("Actual Vs predicted") + 
  xlab("Level") + 
  ylab("Salary")



