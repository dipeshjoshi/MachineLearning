setwd("~/gitMachineLearning/3-supervisedML/1-regression/3-polynomialRegressor")


input_df <- read.csv("Position_Salaries.csv", stringsAsFactors = FALSE)

input_df <- input_df[2:3]

#linear model
lin_model <- lm(Salary~Level, data = input_df)

#polynomial model
input_df$Level2 <- input_df$Level^2
input_df$Level3 <- input_df$Level^3
input_df$Level4 <- input_df$Level^4
input_df$Level5 <- input_df$Level^5
pol_model <- lm(Salary~Level + Level2 + Level3 + Level4 + Level5, data = input_df)


#visualizing predictions
library(ggplot2)
ggplot()+
  geom_point(aes(x = input_df$Level, y = input_df$Salary), colour = 'red') +
  geom_line(aes(x = input_df$Level, y = predict(lin_model, newdata = input_df)), colour = 'blue') +
  ggtitle("Actual vs Fitted line.") +
  xlab('Level') + 
  ylab('Salary')


ggplot()+
  geom_point(aes(x = input_df$Level, y = input_df$Salary), colour = 'red') +
  geom_line(aes(x = input_df$Level, y = predict(pol_model, input_df)), colour = 'black') +
  ggtitle("Actual vs fitted polynomial model") + 
  xlab('Level') + 
  ylab('Salary')


#predict 
pred <- predict(pol_model, newdata = data.frame(Level = 6.5, Level2 = 6.5^2, Level3 = 6.5^3, Level4 = 6.5^4, Level5 = 6.5^5))

