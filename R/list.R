#LIST - list() function
#List can contain elements of different types like - number, string, vectors, another list inside it, matrix.

list_data <- list("Red", "Green", c(21,32,11), TRUE, 51.23, 119.1)
vector1 <- 1:4

newList <- list(vector1, list_data, 'cdsdd', 232, 33.53, TRUE)


#NAMING LIST ELEMENTS - The list elements can be given names and they can be accessed using these names.
a <- list(c("jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"))
b <- list(1:31)
c <- list(c("mon", "tue", "wed", "thu", "fri", "sat", "sun")) 
calender <- list(a, b, c)

# Give names to the elements in the list.
names(calender) <- c("month_list", "date_list", "day_list")


#ACCESSING THE LIST ELEMENTS : 
print(calender[1])          #by index
print(calender$day_list)    #by name


#MANIPULATING LIST ELEMENTS :
list_data <- list("Red", "Green", c(21,32,11), TRUE, 51.23, 119.1)

#Adding element in list
list_data[7] <- 1221

#Remove the last element
list_data[7] <- NULL

#updating 3rd element
list_data[3] <- list(c(1:5))


#MERGING LISTS 
# Create two lists.
list1 <- list(1,2,3)
list2 <- list("Sun","Mon","Tue")

# Merge the two lists.
merged_list <- c(list1,list2)

# Print the merged list.
print(merged_list)


 
#CONVERTING LISTS INTO VECTORS - unlist() function
#All the arithmetic operations on vectors can be applied after the list is converted into vectors.
list1 <- list(1:5)
print(list1)

list2 <-list(10:14)
print(list2)

# Convert the lists to vectors.
v1 <- unlist(list1)
v2 <- unlist(list2)
print(v1)
print(v2)

# Now add the vectors
result <- v1+v2
print(result)

