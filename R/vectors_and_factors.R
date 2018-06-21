#Vectors and Factors.

#Factors used for categorical data.
#c() is used for combining.
id <- c(1,2,3,4)

#To get the structure of vector.
str(vector1)


#Length of vector
length(vector1)

name <- c("Dipesh", "Paras", "Roby", "venky")

pass <- factor(c("P", "P", "F", "P"))

str(pass)


gender <- factor(c("M", "M", "F", "M"), levels = c("M", "F"))


#Retrieving data from vectors and factors.
#vector_name[index]
#vector_name[start index : end index]
name[1:3]