#To get working directory. Default plac where r will look.
getwd()

#To read csv file.  
df <- read.csv("/Users/z001l92/Dipesh/study/R/sample_test.csv")

#By default each string column will be converted to factors.
df <- read.csv("/Users/z001l92/Dipesh/study/R/sample_test.csv", stringsAsFactors = FALSE)

department <- df$dept



