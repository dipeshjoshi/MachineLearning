#FACTORS - factor() function
#Factors are used for categorical columns like gender, directions (east, west, south, north) etc. 

data <- c("East","West","East","North","North","East","West","West","West","East","North")

# Apply the factor function.
factor_data <- factor(data)
print(factor_data)
print(is.factor(factor_data))


#FACTORS IN DATA FRAME 
# On creating any data frame with a column of text data, R treats the text column as categorical data and creates factors on it.
# Create the vectors for data frame.
height <- c(132,151,162,139,166,147,122)
weight <- c(48,49,66,53,67,52,40)
gender <- c("male","male","female","female","male","female","male")

# Create the data frame.
input_data <- data.frame(height,weight,gender)
print(input_data)

# Test if the gender column is a factor.
print(is.factor(input_data$gender))

# Print the gender column so see the levels.
print(input_data$gender)

#CHANGING THE ORDER OF LEVEL 
new_order_data <- factor(factor_data,levels = c("East","West","North","South"))
print(new_order_data)



#GENERATING FACTOR LEVELS - gl() function
gl(n, k, labels)

