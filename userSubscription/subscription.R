setwd("/Users/z001l92/Dipesh/study/machineLearning/healthifyme")

data <- read.csv("data.csv", stringsAsFactors = FALSE)


# Exploratory data analysis.
summary(data)                #It will give each and every details of each column in th data set. And there are 9000 missing values in user_id column. And we are not including user_id for building our model. Since user_id does not contribute for predicting the dependent variable.  
#SO first of all remove all the rows where user_id is missing. Because replacing missing user_id will not make any sense.  
data  <- data[complete.cases(data[, 2]), ]
summary(data)


#1. Checking for any missing values in dataset 
table(is.na(data$age))              # -> 9002 values missing    
table(is.na(data$gender))
table(is.na(data$start_bmi))        # -> 10471 values missing
table(is.na(data$activity_factor))  # -> 7 values missing
table(is.na(data$OS))
table(is.na(data$hypothyroid))
table(is.na(data$diabetes))
table(is.na(data$pcos))
table(is.na(data$physical))
table(is.na(data$hypertension))
table(is.na(data$high_blood_pressure))
table(is.na(data$cholesterol))
table(is.na(data$medical_conditions))
table(is.na(data$devicebrand))
table(is.na(data$paid))

#2. Filling missing values. 

# one of the simplest approach for filling missing values is to replace missing values with average value of that column. But this apporach might result in bad accuracy. But due to time constraints i am replacing missing values with average value of the column.
data[is.na(data$age), "age"] <- median(data$age, na.rm = TRUE)
data[is.na(data$start_bmi), "start_bmi"] <- median(data$start_bmi, na.rm = TRUE)
data[is.na(data$activity_factor), "activity_factor"] <- median(data$activity_factor, na.rm = TRUE)

#Now verify again if everything is correct or not. 
table(is.na(data$age))
table(is.na(data$start_bmi))        
table(is.na(data$activity_factor))

#3. Finding correlation between numerical variables. 
cor(data[,c(4,5,6)])
pairs(data[,c(4,5,6)])



#4. Categorical casting. [Converting categorical variables in to factors.]
data$gender <- as.factor(data$gender)
data$OS <- as.factor(data$OS)
data$hypothyroid <- as.factor(data$hypothyroid)
data$diabetes <- as.factor(data$diabetes)
data$pcos <- as.factor(data$pcos)
data$physical <- as.factor(data$physical)
data$hypertension <- as.factor(data$hypertension)
data$high_blood_pressure <- as.factor(data$high_blood_pressure)
data$cholesterol <- as.factor(data$cholesterol)
data$medical_conditions <- as.factor(data$medical_conditions)
data$devicebrand <- as.factor(data$devicebrand) #There are 156 levels for device brand. i am assuming that there would not be any new device brand for out of sample data. and thats why converting this column in to factor.
data$paid <- as.factor(data$paid)



#5. Data partitioning in to training and testing for crossvalidation
ind <- sample(2, nrow(data), replace = TRUE, prob = c(.7,.3))

train_data <- data[ind==1, ]
test_data <- data[ind==2, ]
summary(data)
summary(train_data)
summary(test_data)


#6. Data representation.
#box plots 
boxplot(train_data$age, train_data$paid)
boxplot(train_data$start_bmi, train_data$paid)
boxplot(train_data$activity_factor, train_data$paid)



# Dependent variable 
table(train_data$paid)  # This shows there are only 1041 observation having paid value 1 and rest has 0, So there is class imbalance problem in the dataset. 
prop.table(table(data$paid)) #class distribution is 99.96% for class 0 and 1.03% for class 1. 
barplot(prop.table(table(data$paid)), col = rainbow(2), ylim = c(0,0.5), main = "Class Distribution")



#OverSampling
install.packages("ROSE")
library("ROSE")
over <- ovun.sample(paid~gender+age+start_bmi+activity_factor+OS+hypothyroid+diabetes+pcos+physical+hypertension+high_blood_pressure+cholesterol+medical_conditions+devicebrand, data = train_data, method = "over", N = 126994)$data
barplot(prop.table(table(over$paid)), col = rainbow(2), ylim = c(0,0.5), main = "Class Distribution after oversampling.")



#7. Model training and predicting against the test dataset.
library(e1071)
model <- svm(paid~gender+age+start_bmi+activity_factor+OS+hypothyroid+diabetes+pcos+physical+hypertension+high_blood_pressure+cholesterol+medical_conditions+devicebrand, data = over)
paid <- predict(model, test_data)
pred <- data.frame(paid)

table(is.na(test_data$index))


#Creating output dataframe
output <- as.data.frame(test_data$paid) 
output$paidPred <- paid



#8. Evaluating results. 
#Confusion matrix
conf_mat <- table(unlist(pred), test_data$paid)
accuracy <- sum(diag(conf_mat))/sum(conf_mat)
misclassification_error <- 1-accuracy



#For Improving results following things can be done. 
#1. Missing value replacement. 
#2. Ensemble methods
