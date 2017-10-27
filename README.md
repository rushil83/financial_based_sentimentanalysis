# Financial Based Sentiment Analysis

![](http://s2.quickmeme.com/img/22/221bf4d77e7d948c994b933588bcfaf5ea7df787bc0cdc2472674c665db29cc5.jpg)
### though its financial one !!

- Predict the sentiment in the financial news. Classification outputs a class from the set of 5 classes. Classes: (‘very positive’,’positive’,’neutral’,’negative’,’very negative’) and 2 swing class (positive swing or negative swing)

- Most accurate with `Financial Headlines` as articles contains past or future reference of our subject hence `confusing` the model about present situation.


## Result :

First you have to give input and according to the input given, the model will give the result


### Input

![INPUT](https://github.com/rushil83/financial_based_sentimentanalysis/blob/master/images/input.png)


## Sample Results : 

   ### example 1
![Example_1](https://github.com/rushil83/financial_based_sentimentanalysis/blob/master/images/example1.png)


   ### example 2
![Example_2](https://github.com/rushil83/financial_based_sentimentanalysis/blob/master/images/example2.png)


   ### example 3
![Example_3](https://github.com/rushil83/financial_based_sentimentanalysis/blob/master/images/example3.png)


## Features

-  Trained our model on positive and negative words of financial system (with 2 classes(pos/neg) only)
-  Used SGDclassifier as our model which ouputs the probability of each class
-  further based on the pobabilites we classified our 2 class`(swing)` output in 5 classes `(very-pos,pos,neural,neg,ver-neg)`
    example : if a document contain negative swing with probabilty of 0.52 then its of neutral sentiment


classification of classes based on swing output
  - 0.45-0.55 (-ve swing ) Neutral Class
  - 0.55-0.75 (-ve swing) Negative Class
  - 0.75- 1.0 (-ve swing) Very Negative Class
  - similary for positive swing





