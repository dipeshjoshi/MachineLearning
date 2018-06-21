res <- tryCatch(
  {
    a <- 1
    b <- 2
    c <- a+s
    b
  },
  error = function(err){
    paste("error", sep='')
  }
)



