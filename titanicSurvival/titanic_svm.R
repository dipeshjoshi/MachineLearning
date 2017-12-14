setwd("/Users/z001l92/Dipesh/study/machineLearning/kaggle/titanic/")

# STEP 1. Reading data
titanic.train <- read.csv("train.csv", stringsAsFactors = FALSE)
titanic.test <- read.csv("test.csv", stringsAsFactors = FALSE)

titanic.test$Survived <- NA


# Step 2. Checking for any missing values. 
#Train
table(is.na(titanic.train$Survived))
table(is.na(titanic.train$Age))
table(is.na(titanic.train$Embarked))
table(is.na(titanic.train$Fare))


#Test
table(is.na(titanic.test$Survived))
table(is.na(titanic.test$Age))
table(is.na(titanic.test$Embarked))
table(is.na(titanic.test$Fare))


# Step 3. Replacing missing values
#Train
titanic.train[is.na(titanic.train$Age) , "Age"] <- median(titanic.train$Age, na.rm = TRUE)
titanic.train[titanic.train$Embarked=="", "Embarked"] <- "C"

#Test
titanic.test[is.na(titanic.test$Age), "Age"] <- median(titanic.test$Age, na.rm = TRUE)
titanic.test[is.na(titanic.test$Fare), "Fare"] <- median(titanic.test$Fare, na.rm = TRUE)
titanic.test[titanic.test$Embarked=="", "Embarked"] <- "C"


# Step 4. Categorical casting
#Training
titanic.train$Pclass <- as.factor(titanic.train$Pclass)
titanic.train$Sex <- as.factor(titanic.train$Sex)
titanic.train$Embarked <- as.factor(titanic.train$Embarked)
titanic.train$Survived <- as.factor(titanic.train$Survived)

#Testing
titanic.test$Pclass <- as.factor(titanic.test$Pclass)
titanic.test$Sex <- as.factor(titanic.test$Sex)
titanic.test$Embarked <- as.factor(titanic.test$Embarked)

# Step 5. Building a model
survived_equation <- "Survived ~ Pclass + Sex + Age + SibSp + Parch + Fare + Embarked"
survived_formula <- as.formula(survived_equation)

#Logistic regression 
lr_model <- glm(formula = survived_formula, data = titanic.train,family = binomial)


#SVM
#library(e1071)
#svm_model <- svm(formula(survived_formula), data=titanic.train)

# Step 6. Testing  
test <- titanic.test[,c("Pclass", "Sex" , "Age" , "SibSp" , "Parch" , "Fare" , "Embarked")]
survived <- predict(lr_model, newdata = test, type="response")

# Step 7. Creating the final output data frame for submiting the results
PassengerId <- titanic.test$PassengerId
output_df <- as.data.frame(PassengerId)
output_df$Survived <- survived

#Writing output into csv
write.csv(output_df, file = "kaggle_submission.csv" , row.names = FALSE)