# VECTORS : Vector contains elements of same type.

#1. CREATING A VECTOR : { c() fucntion is used to create vector.}
v <- 1:4
print(v)

v1 <- seq(1,10, by = 2)
print(v1)

v2 <- c('apple','red',5,TRUE)
print(v2)

v3 <- c(1, 2.1)
print(v3)

v4 <- c(c(1,2,3),4,5,6)

v5 <- c(1:4,5,6)


#2. NAMING THE VECTOR :
#option 1. 
price <- c(7,3,4)
fruites <- c("Apple", "Orange", "Banana")
names(price) <- fruites

#option 2. 
price <- c(Apple=7, Orange=3, Banana=4)

#option 3. 
price <- c("Apple"=7, "Orange"=3, "Banana"=4)


#3 SINGLE VALUE = VECTOR OF LENGTH 1.
my_apples <- 5
my_oranges <- "six" 


#4 COERCION / CASTING FOR VECTORS
cards <- c(2,4,7,3,'A', 10, 'J', 'Q', 8, 9, 'k') #Autmatically all elemnets being coverted in to character. 


#5 VECTOR CALCULUS
price <- c(Apple=7, Banana=3, Mango=4, Orange=6, Grape=8)
discount <- c(3,1,2,2,5)
tax <- c(2,1,1,2,3)
bought <- c(3,1,6,2,7)

#Element wise computations If vector and scaler 
price * 3 
price + 3 
price - 3
price / 3
price ^ 3


# Create two vectors.
v1 <- c(3,8,4,5,0,11)
v2 <- c(4,11,0,8,1,2)

# Vector addition.
final_price <- price+tax
print(final_price)

# Vector substraction.
discounted_price <- price-discount
print(discounted_price)

# Vector multiplication.
invoice <- final_price * bought
print(invoice)

# Vector division.
discount_percentage <- discount/price
print(discount_percentage)

#Vector comaprision.  
price > discount 



#6 ACCESSING VECTORS ELEMENTS / SUNSETTING VECTOR. {we use [] for subsetting vectors.}
price <- c(Apple=7, Banana=3, Mango=4, Orange=6, Grape=8)
price[1]
price["Apple"]

# for selecting multiple elements
seasonal_fruits <- price[c(3,4)]
print(seasonal_fruits)

seasonal_fruits <- price[c("Mango", "Orange")]
print(seasonal_fruits)

# Accessing vector elements using logical indexing.
seasonal_fruits <- price[c(FALSE,FALSE,TRUE,TRUE,FALSE)]
print(seasonal_fruits)

# All but some. Accessing vector elements using negative indexing.
seasonal_fruits <- price[c(-1,-2,-5)]
print(seasonal_fruits)

# Accessing vector elements using 0/1 indexing.
seasonal_fruits <- price[c(0,0,1,1,0)]
print(seasonal_fruits)


#7 VECTOR ELEMENT RECYCLING  
#If we apply arithmetic operations to two vectors of unequal length, then the elements of the shorter vector are recycled to complete the operations.
v1 <- c(3,8,4,5,0,11)
v2 <- c(4,11)
# V2 becomes c(4,11,4,11,4,11)

add.result <- v1+v2
print(add.result)

sub.result <- v1-v2
print(sub.result)


#VECTOR ELEMENT SORTING
v <- c(3,8,4,5,0,11, -9, 304)
sort_resut <- sort(v)
resv_sort <- sort(v, decreasing = TRUE)
print(sort_resut)
print(resv_sort)

w <- c("Red","Blue","yellow","violet")
sort_resut <- sort(w)
resv_sort <- sort(w, decreasing = TRUE)
print(sort_resut)
print(resv_sort)