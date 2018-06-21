#Multi variate summaries

pairs(df) #Wont work. Only works with numerical variables.
pairs(df[, -c(1,2,3,6)])

#Correlation matrics
cor(df[, -c(1,2,3,6)])

#Aggregation [Similar to tapply function. But this is for multivariate]
aggregate(salary ~ gender, data=df, FUN = mean)
aggregate(salary ~ gender + experience, data=df, FUN = mean)
aggregate(salary ~ gender + experience, data=df, FUN = sd)
aggregate(salary ~ gender + experience, data=df, FUN = length)



#Side by side box plots. BOX PLOT IS ALWAYS BETWEEN CATEGORICAL AND NUMERICAL VARIABLES.

df$gender <- factor(df$gender)
df$experience <- factor(df$experience)

boxplot(df$salary)
plot(salary ~ gender, data = df)
plot(salary ~ experience, data = df)
