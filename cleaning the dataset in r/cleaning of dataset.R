dataset=read_csv('imdbnew.csv')
dataset$url<-NULL
dataset$tid<-NULL
dataset$fn<-NULL
dataset$nrOfWins<-NULL
dataset$wordsInTitle<-NULL
dataset$X45<-NULL
dataset$nrOfNominations<-NULL
dataset$type<-NULL
dataset$nrOfNewsArticles<-NULL
dataset<-dataset[(dataset$nrOfGenre<4),]
dataset$X46<-NULL
dataset$X47<-NULL
dataset$X48<-NULL
dataset<-dataset[(dataset$year>1999),]
dataset<-dataset[(dataset$Action<2),]
dataset<-dataset[(dataset$duration>100),]
table(is.na(dataset$title))
dataset <- dataset[!(is.na(dataset$title)) ,]
dataset$nrOfPhotos<-NULL
dataset <- dataset[!(is.na(dataset$imdbRating)) ,]
dataset$FilmNoir<-NULL
dataset$GameShow<-NULL
dataset$News<-NULL
dataset=read_csv('newimdbratings1.csv')

dataset<-dataset[(dataset$ratingCount>1000000),]




