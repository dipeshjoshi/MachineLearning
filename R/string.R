# STRING MANIPULATION

# CONCATINATING STRING - paste() function

a <- "Hello"
b <- 'How'
c <- "are you? "

print(paste(a,b,c))
print(paste(a,b,c, sep = "-"))
print(paste(a,b,c, sep = "", collapse = ""))


#FORMATTING STRING AND NUMBERS - format() function 
#Syntex : format(x, digits, nsmall, scientific, width, justify = c("left", "right", "centre", "none"))
# Total number of digits displayed. Last digit rounded off.
result <- format(23.123456789, digits = 9)
print(result)

# Display numbers in scientific notation.
result <- format(c(6, 13.14521), scientific = TRUE)
print(result)

# The minimum number of digits to the right of the decimal point.
result <- format(23.47, nsmall = 5)
print(result)

# Format treats everything as a string.
result <- format(6)
print(result)

# Numbers are padded with blank in the beginning for width.
result <- format(13.7, width = 6)
print(result)

# Left justify strings.
result <- format("Hello", width = 8, justify = "l")
print(result)

# Justfy string with center.
result <- format("Hello", width = 8, justify = "c")
print(result)


#COUNTING NUMBER OF CHARACTERS - nchar() funtion
result <- nchar("Count the number of characters")
print(result)


#CHANGING THE CASE - toupper() or tolower() fucntion
print(toupper('dipesh joshi'))
print(tolower('Dipesh joshi'))


#EXTRACTING THE PART OF STRING - substring() function
#Syntex : substring(x,first,last)
name <- 'Dipesh joshi'
print(substring(name, 3,9))
