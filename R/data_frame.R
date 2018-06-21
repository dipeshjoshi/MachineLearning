#DataFrames 
#df_name <- data.frame(v1, v2, v3......) {where v1 is vector1 and so on.}

id <- c(1,2,3,4)
name <- c("Dipesh", "Paras", "Roby", "venky")
pass <- factor(c("P", "P", "F", "P"))
gender <- factor(c("M", "M", "F", "M"), levels = c("M", "F"))

df1 <- data.frame(id, name, pass, gender)
str(df1)

# By default data.frame() converts string vector in to factor. To avoid that use this command.
df1 <- data.frame(id, name, pass, gender, stringsAsFactors = FALSE)
str(df1)

# Retrieving data from data frame 
df[row_index , column_index]

#ranges in rows and columns
df[row_start_index : row_end_index, col_start_index : col_end_index]

#particular rows and columns
df[c(1,3), c(1,4)]
df[c(1,3), c("name", "salary")]

#Except specified column. But we can not use column name here, we need to use column number.
df[c(1,3), -c(5)]


df[1,"gender"]
df[,"gender"]
df[1,]

#fetching particular column
#dataFrame$column_name
df$name

#CATEGORICAL VARIABLES [Always change categorical variables in to Factor]
#Changing column in to factor
df$gender = factor(df$gender)

#Finding frequency. {only for categorical variables}
table(df$gender)
table(df$gender, df$experience)

#Visulization of categorical data
#pie chart
pie(table(df$gender))

#bar plot
barplot(table(df$gender))


#NUMERICAL VARIABLES
sal = df$salary

#Min
min(sal)

#Max
max(sal)

#Range
range(sal)

#Mean 
mean(sal)

#Median
median(sal)

#Variance
var(sal)

#Standard Deviation
sd(sal)

#Visualization of numerical variable
#Histogram
hist(sal)

#Boxplots
boxplot(sal)
boxplot(sal,horizontal = TRUE)


#QUERIES ON DATA FRAME
#Applying condition for some column
female_emp <- subset(df, gender %in% "F")

highly_paid_emp <- subset(df, salary > 90000)

