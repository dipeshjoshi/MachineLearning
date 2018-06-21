setwd("/Users/z001l92/Dipesh/study/R")
df <- read.csv(file = "hw1_data.csv", stringsAsFactors = FALSE)

#CRUD 

#Retrieve
#select * from df;
df
df[]
df[,]

#Select * from df limit 10;
head(df, n=10)
head(df$Ozone, n=10)
head(df[c(1,2,4,5)], ,n=10)

tail(df, n=10)
tail(df$Ozone, n=10)
tail(df[c(1,2,4,5)], ,n=10)

#select * from df where ozone > 31
df[df$Ozone > 31, ]
df[df$Ozone > 31 & df$Temp > 90, ]
df[which(df$Ozone > 31 & df$Temp > 90), ]

#select columns from df where ozone > 31
df[df$Ozone > 31, c(1, 3, 4)]
df[df$Ozone > 31, c("Ozone", "Wind", "Temp")]
df[which(df$Ozone > 31 & df$Temp > 90), c(1, 3, 4)]

#subset function  
#subset(data_frame, conditions, column selection)
subset(df, df$Ozone > 31 & Temp > 90, select = c("Ozone", "Temp", "Wind"))

#string matching for column
df[grep(12.6, df$Wind, ignore.case = TRUE), ]