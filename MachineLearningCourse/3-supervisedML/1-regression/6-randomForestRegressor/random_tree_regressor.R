setwd("~/gitMachineLearning/3-supervisedML/1-regression/6-randomForestRegressor")

input_df <- read.csv("Position_Salaries.csv")

input_df <- input_df[2:3]

#building model
# install.packages('randomForest')
library(randomForest)
set.seed(1234)
model <- randomForest(x = input_df[1],
                      y = input_df[, 2], ntree = 500)

pred <- predict(model, newdata = data.frame(Level = 6.5))

#Visualization 
#For continuos graph
sequence <- seq(min(input_df$Level), max(input_df$Level), by = .01)
ggplot()+
  geom_point(aes(x = input_df$Level, y = input_df$Salary), color = 'red') +
  geom_line(aes(x = sequence, y = predict(model, newdata = data.frame(Level = sequence))), color = 'black') + 
  ggtitle("Actual Vs predicted") + 
  xlab("Level") + 
  ylab("Salary")