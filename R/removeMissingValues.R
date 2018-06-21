a <- c(1,4,7,NA,5,8,NA)
b <- c('a','b',NA,'s','g','f',NA)


complete.cases(a)
#Returns logical vector having true if NA is not there. For multiple vectors it returns TRUE only if both vector having non NA value. If any one of the vector is having NA then will return FALSE.
#eg : TRUE  TRUE  TRUE FALSE  TRUE  TRUE FALSE 
#eg : TRUE  TRUE FALSE FALSE  TRUE  TRUE FALSE
x <- a[complete.cases(a)]
y <- a[complete.cases(a,b)]



is.na(a)
#Returns logical vector having true if NA is there.
#eg : FALSE FALSE FALSE  TRUE FALSE FALSE  TRUE
x <- a[!is.na(a)]


x <- na.omit(a)
