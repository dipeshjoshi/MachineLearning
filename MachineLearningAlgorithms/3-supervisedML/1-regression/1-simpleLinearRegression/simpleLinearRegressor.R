setwd("~/gitMachineLearning/3-supervisedML/1-regression/1-simpleLinearRegression")

#Reading dataset
input_data <- read.csv("Salary_Data.csv")


#splitting data set in train and test
ind <- sample(2, nrow(input_data), prob = c(.7,.3), replace = TRUE)
train_data <- input_data[ind == 1, ]
test_data <- input_data[ind == 2, ]

#splitting data set in train and test
#install.packages("caTools")
library('caTools')
split <- sample.split(input_data$Salary, SplitRatio = .7)
train_data <- input_data[split == TRUE, ]
test_data <- input_data[split == FALSE, ]

#train model on training data
model <- lm(Salary~YearsExperience, data = train_data)
pred <- predict(model, newdata = test_data)

#plot
library(ggplot2)
ggplot() +
  geom_point(aes(x = train_data$YearsExperience, y = train_data$Salary), colour = 'green') +
  geom_line(aes(x = train_data$YearsExperience, y = predict(model, newdata = train_data)), colour = 'blue') +
  ggtitle('Salary vs Year of experience in Training set.')

ggplot() +
  geom_point(aes(x = test_data$YearsExperience, y = test_data$Salary), colour = 'green') + 
  geom_line(aes(x = train_data$YearsExperience, y = predict(model, newdata = train_data)), colour = 'blue') +
  ggtitle('Salary vs Year of Experience in TEsting set.')