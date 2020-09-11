Xtemp = read.csv("Xtemp.csv", sep=",", header = T)
Ytemp = read.csv("Ytemp.csv", sep=",", header = T)
Xhumid = read.csv("Xhumid.csv", sep=",", header = T)
Yhumid = read.csv("Yhumid.csv", sep=",", header = T)


smp_size <- floor(0.7 * nrow(Xtemp))
set.seed(123)
train_ind<- sample(seq_len(nrow(Xtemp)), size = smp_size)
Xtemp_train <- Xtemp[train_ind, ]
Xtemp_test <- Xtemp[-train_ind, ]
Ytemp_train = Ytemp[train_ind, ]
Ytemp_test = Ytemp[-train_ind, ]
Xhumid_train <- Xhumid[train_ind, ]
Xhumid_test <- Xhumid[-train_ind, ]
Yhumid_train = Yhumid[train_ind, ]
Yhumid_test = Yhumid[-train_ind, ]


space = read.csv("space.txt", sep=' ', header=F)
space=space[,-7]
space
list_of_rooms[[1]]



# QP regression

library("quadprog");
X <- data.matrix(Xtemp_train[c('x1B1A','temperature','rB122', 'rB123', 'rB124', 'rB125', 'rB126')])
XX <- cbind(1,X)
Y <- Ytemp_train[,1]
b <- c(1,rep(0,ncol(X)))
Dmat <- t(XX)%*%XX
dd <- t(Y)%*%XX
Amat <- t(cbind(0,rbind(1,diag(ncol(X)))))
solver = solve.QP(Dmat = Dmat, factorized = FALSE, dvec = dd, Amat = Amat, bvec = b, meq = 1)
solver

X <- data.matrix(Xhumid_train[c('humidity', 'x1B1A', 'x52A')])
XX <- cbind(1,X)
Y <- Yhumid_train[,1]
b <- c(1,rep(0,ncol(X)))
Dmat <- t(XX)%*%XX
dd <- t(Y)%*%XX
Amat <- t(cbind(0,rbind(1,diag(ncol(X)))))
solver = solve.QP(Dmat = Dmat, factorized = FALSE, dvec = dd, Amat = Amat, bvec = b, meq = 1)
solver


# comparison

X <- data.matrix(Xtemp_test[c('x1B1A','temperature','rB122', 'rB123', 'rB124', 'rB125', 'rB126')])
XX <- cbind(1,X)
predicted = XX %*% solver$solution
compare_matrix = data.frame(Ytemp_test[,1], predicted)
colnames(compare_matrix) = c("Real Value", "Predicted Value")
compare_matrix

sum = 0
for(i in 1:10){
  temp=(compare_matrix[i,1] - compare_matrix[i,2])^2
  sum = sum+temp
}
sum  


t.test(compare_matrix[,1], compare_matrix[,2])           



# drawing plots

library(ggplot2)
library(reshape2)

x  <- 1:10
Real <- compare_matrix[,1]
Predicted <- compare_matrix[,2]
df <- data.frame(x, Real, Predicted)

df2 <- melt(data = df, id.vars = "x")
p = ggplot(data = df2, aes(x = x, y = value, colour = variable)) + geom_line()
p + labs(colour = "Values") + labs(x = "Time") + labs(x = "Temperature")+ylim(15,35)
