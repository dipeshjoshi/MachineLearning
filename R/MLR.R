#read data

df <- read.csv("/Users/z001l92/Dipesh/study/R/MLR.csv")
pairs(df)

train <- df[1:(103*.80), ]
test <- df[ (103*.80) + 1 : 20, ]

model <- lm(Ratio ~ Position + Starters + Last +	Since +	Number + Carried + Weight	+ Barrier +	Distance + Lengths + Odds + Starts + Age, data=train)
results <-predict(model, test)