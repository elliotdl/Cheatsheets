# What does this create?

all_comb <- function(n){
  z <- rep(0,n)
  answer <- t(apply(combn(0:n,n-1),2,function(k) {z[k]=1;z}))
  return(rbind(z,answer,rep(1,n)))
}