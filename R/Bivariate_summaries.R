#Relationship between variables
#Numeric and Categorical
plot(salary ~ gender, data = df)

tapply(df$salary, df$gender, mean)
tapply(df$salary, df$gender, sd)


#Numeric and Numerical
plot(salary ~ experience, data = df)
plot(salary ~ experience, data = df, pch=as.integer(gender), col=as.integer(gender))

legend("topright", legend = c("Male", "Female"), pch=c(1,2), col=c(2,4))