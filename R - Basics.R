# PREMABLE
rm(list=ls())
setwd("F:/PRIVATE/Folder Name")
library(dplyr)

# INTROSPECTION
class(x)
help(x)

# VECTORS
v = c(1,2,3)    # creation
v[2]            # slicing
# MANIPULATE
rbind(v1, v2)
cbind(v1, v2)
sort(v)         # sort
rev(v)          # reverse
c(v1, v2)       # concatenation
# CHECK VECTORS
length(v)       # length
x %in% v        # membership
v[v>3]          # keep elts meet condition
which(v>3)      # indices of elts meet condition

# SETS
unique(v)
union(v1, v2)
intersect(v1, v2)
setdiff(v1, v2)

# NAMED VECTORS
v = c(1,2,3)
names(v) = c('a', 'b', 'c')

# BOOLEAN
x==3 & y>3
x==3 | y>3
3 != 2
!y==2
any(TRUE, FALSE)
all(TRUE, FALSE)

# STRINGS
paste("foo", 1:4, sep=".")  #foo.1 foo.2 foo.3 foo.4... use with rownames
paste(c("x","y","z"), collapse="-")  # x-y-z
sprintf("hi %s is %s","my name","elliot")
grep("foo", c("xxx","xfoox","xxx")) # 2
grepl("foo", c("xxx","xfoox","xxx")) # F T F
gsub("foo", "hi", "xfoox")  # xhix

## CREATE MATRIX: 1 vector into matrix
m = matrix(1:6, nrow=2, ncol=3)
rownames(m) = c("row1", "row2")
colnames(m) = c("col1", "col2", "col3")
dim(m)

# FUNCTIONS
fnname<- function(input1, input2=100){
  return( list("output1"=output1, "output2"=output2))
}

# IF LOOPS
if (condition){
  code
} else if (condition){
  code
} else {
  code
}

# FOR LOOPS
for (i in 1:10){
  code
}

# WHILE LOOPS
while (x<10){
  code
  if (x==3){
    break
  }
}

# MAP (fn applied to paired arguments)
Map(sum, c(1,9), c(2,10)) # 1+2, 9+10

#READ DATA
x = read.csv("file.csv")
data = read.xlsx(file = "2015data.xlsx", sheetIndex = 2, header=TRUE) 
x = na.omit(x) # remove NAs
x[is.na(x)] = 0 # replace NAs with 0
data<-scale(origdata) # normalize data

# MATHJAX (LATEX)
library(shiny)
withMathJax(print(" the value is $$ x_1 + 3 $$"))
withMathJax(print(" the value is \\( x_1 + 3 \\)")) #inline

# DO.CALL
do.call(somefunc, list(arg1, arg2, arg3))  #same as somefunc( arg1, arg2, arg3 )

#LINEAR PROGAMMING
Linprog <- lp("max", Objective, ConstrMat, Dir, Rhs, int.vec=foo)
Linprog <- lp("max", c(1,2,3) , matrix(rep(0,6),nrow=2,ncol=3), c("<=","<="), c(9,16), int.vec=1:3)
Linprog$objval
Linprog$solution

#linear regression with a forced intercept
intercept <- 100
fit <- lm(I(y - intercept) ~ 0 + x, df)
dev.new(width=2, height=2)
plot(x,y,pch=19)
abline(intercept, coef(fit), col="red")

#pairwise plot of features
dev.new(width=2, height=2)
with(iris, pairs(iris))

# time your code
library(tictoc)
tic(); code; toc()
