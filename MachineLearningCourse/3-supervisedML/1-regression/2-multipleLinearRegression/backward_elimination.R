input_df <- read.csv("50_startups.csv", stringsAsFactors = FALSE)

#1. Look for missing values. 
table(is.na(input_df))

#2. Categorical casting
input_df$State <- as.factor(input_df$State)

#3. Train Test split
#install.packages('caTools')
library(caTools)
ind <- sample.split(input_df$Profit, SplitRatio = .8)
train_data <- input_df[ind == TRUE, ]
test_data <- input_df[ind == FALSE, ]

#4. building a model
model <- lm(Profit ~ R.D.Spend + Administration + Marketing.Spend + State, data = train_data)
summary(model)

#By looking in to summary of model it can be seen that state column is irrelevent. Because that is having highest p value among all the varibale. So remove state column an d rebuild our model.
model <- lm(Profit ~ R.D.Spend + Administration + Marketing.Spend, data = train_data)
summary(model)

#Now Administration variable is having highest p value so remove that. 
model <- lm(Profit ~ R.D.Spend + Marketing.Spend, data = train_data)
summary(model)

#Now Marketing.spend is having comparatively higher P value which is greter then significance level. (SL = .05). So remove that column as well.
model <- lm(Profit ~ R.D.Spend, data = train_data)
summary(model)

#Now model is ready. Because each variable is having p value less then significance level. 

y_pred <- predict(model, newdata = test_data)