library(data.table)

setnames(imdbtwo,"X25","mood")
imdbtwo$mood=factor(imdbtwo$mood,
                    levels=c('sad','normal','happy'),
                    labels=c(1,2,3))
imdbtwo$year<-NULL
imdbtwo$ratingCount<-scale(imdbtwo$ratingCount)
imdbtwo$nrOfUserReviews<-scale(imdbtwo$nrOfUserReviews)
train<-imdbtwo[1:120,]
test<-imdbtwo[121:140,]
library(xgboost)
train=train[2:20]
train[] <- lapply(train, as.numeric)

classifier=xgboost(data=as.matrix(train[-20]),label = train$mood,nrounds = 15)
test[] <- lapply(test, as.numeric)

y_pred=predict(classifier,as.matrix(test$mood))

y_pred = as.data.frame(y_pred)


library(e1071)
classifier1=svm(formula= mood ~.,
                
                data= train,
               
                type='C-classification',
                kernel='linear')
test<-test[2:20]
y_pred1 = predict(classifier1,newdata = test[-19])

y_pred1 = as.data.frame((y_pred1))
cm=table(test[, 19], y_pred1)



library(h2o)
h2o.init()
train.h20<-as.h2o(train)

library(caret)
folds=createFolds(train$mood,k=10)
cv=lapply(folds,function(x){
  training_fold=train[-x, ]
  test_fold=train[x, ]
  classifier=xgboost(data=as.matrix(train[-20]),label = train$mood,nrounds = 5)
  
  y_pred1=predict(classifier,newdata=as.matrix(test_fold[-20]))
  cm=table(test_fold[,20],y_pred1)
  accuracy=(cm[1,1]+cm[2,2]/cm[1,1])+cm[2,2]+library(xgboost)
train=train[5:24]
train[] <- lapply(train, as.numeric)

classifier=xgboost(data=as.matrix(train[-20]),label = train$mood,nrounds = 5)

cm[1,2]+cm[2,1]
  return (accuracy)

})
accuracy=mean(as.numeric(cv))


