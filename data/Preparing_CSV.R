crimes <- read.csv("BostonCrime.csv")
crimes <- crimes[-c(1,2,4,6:10,13:17)]
labels <- crimes[1]
crimes <- crimes[-c(1)]

write.csv(crimes, "crimes.csv")
write.csv(labels, "labels.csv")