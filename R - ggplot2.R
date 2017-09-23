dev.new(width=2, height=2)

#boxplots
p<- ggplot(data, aes(x=entities, y=attribute))
p + geom_boxplot()
#no outliers
p + geom_boxplot(outlier.shape = NA)
p + scale_y_continuous(limits = c(lowerValue, upperValue))
# rotate axes labesl
p + theme(
   axis.text.x=element_text(angle=90, size=8, hjust=0, vjust=0),
   axis.title.x=element_text(angle=10, color='red'))
# axes titles
P + xlab('The Years of Cinema')


#histograms
ggplot(data, aes(x=col)) + geom_bar(stat="bin")
#barplots
ggplot(data, aes(x=entities, y=barheight)) + geom_bar(stat="identity")