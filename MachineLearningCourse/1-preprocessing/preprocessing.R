setwd("~/gitMachineLearning/1-preprocessing")
#Reading data
input_df <- read.csv('Data.csv', stringsAsFactors = FALSE)


# 1. Missing values
input_df[is.na(input_df$Age), "Age"] <- mean(input_df$Age, na.rm = TRUE)
input_df[is.na(input_df$Salary), "Salary"] <- mean(input_df$Salary, na.rm = TRUE)

# 2. Categorical casting
input_df$Country <- as.factor(input_df$Country)
input_df$Purchased <- as.factor(input_df$Purchased)
 

# OR this way.
input_df$Country = factor(input_df$Country,
                         levels = c('France', 'Spain', 'Germany'),
                         labels = c(1, 2, 3))
input_df$Purchased = factor(input_df$Purchased,
                            levels = c('No', 'Yes'),
                            labels = c(0, 1))

# 3. Spliting data into train and test dataset
library(caTools)
ind <- sample.split(input_df$Purchased, SplitRatio = .7)
train_data <- input_df[ind == TRUE, ]
test_data <- input_df[ind == FALSE, ]
