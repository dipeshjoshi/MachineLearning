#There are 6 different types of data onjects in R.
# 1. Vectors
animal <- c("Dog", "Cat", "Lion", "Monkey")
age <- c(2,4,1,6,8,2,8)
height <- c(4.2, 3.5, 5.2, 5.3, 3.5, 6.3)



l1 = list(1:5)
l2 = list(10:14)
v1 <- unlist(l1)
v2 <- unlist(l2)
print(v1)
print(v2)
l3 <- v1 + v2
print(l3)