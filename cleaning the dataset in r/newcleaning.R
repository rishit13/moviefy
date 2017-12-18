library(readr)
dataset<-read.csv('imdb.csv')
dataset1<-dataset1[(dataset1$ratingCount>100000),]
dataset1 <- dataset1[!(is.na(dataset1$title)) ,]
dataset1$FilmNoir<-NULL
dataset1$News<-NULL
dataset1$RealityTV<-NULL
dataset1$Short<-NULL
dataset1$TalkShow<-NULL
dataset1$Western<-NULL
dataset1$History<-NULL
dataset1$GameShow<-NULL
dataset1$Music<-NULL
dataset1$Musical<-NULL
