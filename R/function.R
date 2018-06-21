#SYNTEX
function_name <- funstion(arguments.......){
  .........
  function body
  .........
  ......... #THis is the last argument of function. The return value of a function is the last expression in the function body to be evaluated 
}

#EG : 
new.function <- function(){
  for(a in 1:5){
    print(a^2)
  }
}


sum_func <- function(a, b){
  print(a+b)
}


#CALLING A FUNCTION 
function_name(arguments if defined in function.)


#EG : 
new.function()
sum_func(1,4)



#Lazy evaluation of function : Arguments to functions are evaluated lazily, which means so they are evaluated only when needed by the function body.
func <- function(a, b){
  print(a)
  print(b)
}
# OUTPUT 
#func(1)
#[1] 1
#Error in print(b) : argument "b" is missing, with no default