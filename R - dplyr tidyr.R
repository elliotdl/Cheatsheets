# DATAFRAME
x = data.frame("a" = c(1,2), "b" = c(3,4), stringsAsFactors=FALSE)
head(x)
x[1,1]
x['row','col']
x[c(TRUE,FALSE),]
x<-factor(c('low','med','high')) #CREATE FACTORS

# ROWS
nrow(x)
rownames(x)
x[1:2,]          # slice
df[df$col==3,]   # slice by filter

# COLUMNS
ncol(x)
colnames(x)
x["name"] # single slice (returns df)
x$name    # single slice (returns vector)
x[c('a','b')] # re-arrange / mult slice (by name)
df$col = NULL #delete col
unique(x$a) # unique vals of cols
table(x$a) # tally values

# FILTER : KEEP ROWS MEETING A CRITERIA
filter(df, a==1, b>2) # AND
filter(df, a==1 | b>2) # OR
filter(df, a %in% c("x","y")) # MULT VALUES
filter(df, !a %in% c("x","y"))
filter(df, grepl("x",a)) # str.contains

# SELECT: KEEP COLS BY NAME
select(df, a, b, c)
select(df, a:c)
select(df, contains("a"))
select(df, starts_with("a"))

# CHAINING OR PIPELINING
(x1-x2)^2 %>% sum() %>% sqrt()

# ARRANGE : sort rows
df %>% arrange(a, desc(b))

#MUTATE: ADD ON NEW VARS FUNCTION OF OLD VARS
df %>% mutate(Speed = Distance/AirTime*60)
df %>% mutate(newvar=ifelse( colA==1 | colB!=3 , 1, 0 )) #conditional mutation

#SUMMARISE: SPLIT BY CRITERIA (group_by), APPLY FUNCTION TO EACH GROUP, COMBINE
df %>% group_by(a) %>% summarise(new = mean(b))
df %>% group_by(a) %>% summarise(new1=n(), new2=mean(b), new3=n_distinct(c))
df %>% group_by(a,b) %>% summarise(new = n()) # multiple groups

df[df$a==1 & df$b>2, ] # old filter
df[ , c("a", "b", "c") ] # old select
df[order(df$a), c("a","b")] # old arrange
df$Speed <- df$Distance / df$Time*60 # old mutate
sapply(iris[1:4],mean)  # old summary fn
with(iris, tapply(Sepal.Length, list(Species, Petal.Width), mean)) # matrix of factors
aggregate(Sepal.Length~Species+Petal.Width, data=iris, FUN=mean) # gathered table of factors

# lookup
left_join(origtable, lookuptable, by="samecol")

#TIDYR

#gather turns wide data into long
gather(origdata, NewKeyColName, NewValueColName, OldColsWithValues)