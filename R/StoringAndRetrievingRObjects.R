# Storing and retrieving R objects 
# dput() and dget() : 
#     dput()    : For writing R object in file. 
#     dget()    : For getting R object back. 

df <- data.frame(a=1, b=4)
dput(df, file = "df.R")
new_df <- dget("df.R")

#dump() and source() : 
#     dump()    : dput() can write only one R object, but dump() can write multiple R objects. 
#     source()  : source() is used to get all R objects which is being wrote by dump() function.
df <- data.frame(a=1, b=4)
v <- c(1,5,1,6,7,6)
l <- list("s", 2, "2.4", "klcxjld", c(2,5,1))

dump(c("df","v","l"),file="Robj.R")

rm(df,v,l)

source("Robj.R") # for getting all saved R objects in specified file in to current envirnoment.