#MATRICES - Extension of vector from 1-D to 2-D.
  #Matrix is same as Vector, but only 1 extra dimension is added. Vector is 1-D, Matrix is 2-D.
  #Like vector matrix contains elements of same type, but agrranged in row and column formats.
  

#1. Creating matrix. matrix() function



#Matrices are the R objects in which the elements are arranged in a two-dimensional rectangular layout.

matrix(data, nrow, ncol, byrow, dimnames)

m <- matrix(c(1:12), nrow = 4, byrow = TRUE)
print(m)

m1 <- matrix(c(1:14), nrow = 4, byrow = TRUE) # at missing palces numbers starts repeating.

# Define the column and row names.
rownames = c("row1", "row2", "row3", "row4")
colnames = c("col1", "col2", "col3")

m2 <- matrix(c(1:12), nrow = 4, byrow = TRUE, dimnames = list(rownames, colnames))
print(m2)




#ACCESSING ELEMENTS OF MATRICES :
metrix_name[row_index, col_index]
print(m2[2,3])

#Complete row 
metrix_name[row_index, ]
print(m2[2, ])

#Complete column
metrix_name[ , col_index]
print(m2[ ,3])


#MATRIX COMPUTATION 
matrix1 <- matrix(c(3, 9, -1, 4, 2, 6), nrow = 2)
matrix2 <- matrix(c(5, 2, 0, 9, 3, 4), nrow = 2)

# Add the matrices.
result <- matrix1 + matrix2
cat("Result of addition","\n")
print(result)

# Subtract the matrices
result <- matrix1 - matrix2
cat("Result of subtraction","\n")
print(result)

# Multiply the matrices.
result <- matrix1 * matrix2
cat("Result of multiplication","\n")
print(result)

# Divide the matrices
result <- matrix1 / matrix2
cat("Result of division","\n")
print(result)