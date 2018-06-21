#lapply

l <- list(a = 1:4, b=rnorm(10), c = 22:53)
lapply(l, mean)
sapply(l, mean)