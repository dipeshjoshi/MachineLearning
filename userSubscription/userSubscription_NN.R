setwd("~/Dipesh/study/machineLearning/healthifyme")

# Reading and geting column of interest. 
input_df <- read.csv('data.csv', stringsAsFactors = FALSE)
input_df <- input_df[complete.cases(input_df[, 2]), ]
input_df <- input_df[-c(1,2,8,17)]

#missing values
table(is.na(input_df$age))
table(is.na(input_df$start_bmi))
table(is.na(input_df$activity_factor))

input_df[is.na(input_df$age), "age"]<- mean(input_df$age, na.rm = TRUE)
input_df[is.na(input_df$start_bmi), "start_bmi"]<- mean(input_df$start_bmi, na.rm = TRUE)
input_df[is.na(input_df$activity_factor), "activity_factor"]<- mean(input_df$activity_factor, na.rm = TRUE)


#categorical casting
input_df$gender <- as.numeric(factor(input_df$gender, 
                          levels = c('male', 'female'),
                          labels = c(0,1)))
input_df$OS <- as.numeric(factor(input_df$OS,
                      levels = c('android', 'ios', 'both'),
                      labels = c(1,2,3)))

#feature scaling
input_df[-14] <- scale(input_df[-14])

#splitting data in train and test data
library(caTools)
ind <- sample.split(input_df$paid, SplitRatio = .7)
train_data <- input_df[ind == TRUE, ]
test_data <- input_df[ind == FALSE, ]

#oversampling or undersampling
#install.packages('ROSE')
library(ROSE)
oversampled_data <- ovun.sample(formula = paid ~ ., 
                                data = train_data,
                                method = 'over',
                                N = 127264)$data
barplot(prop.table(table(oversampled_data$paid)), col = rainbow(2), ylim = c(0,0.5), main = "Class Distribution after oversampling.")

#creating Neural Network
#install.packages('h2o')
library(h2o)
h2o.init(nthreads = -1)
model <- h2o.deeplearning(y = 'paid',
                 training_frame = as.h2o(oversampled_data),
                 activation = 'Rectifier',
                 hidden = c(7,7),
                 epochs = 100,
                 train_samples_per_iteration = -2)

#Making predictions
prob_pred <- h2o.predict(model, newdata = as.h2o(test_data))
y_pred <- ifelse(prob_pred > 0.5, 1, 0)
y_pred <- as.vector(y_pred)

#Evaluating
cm <- table(y_pred, test_data[, 14])