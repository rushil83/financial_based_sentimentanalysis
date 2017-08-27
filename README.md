# Finance Based Sentiment Analysis
           visit README.pdf for result and full description

#### ●  Predict the sentiment in the financial news. Classification outputs a class from the set of

#### ● 5 classes. Classes: (‘very positive’,’positive’,’neutral’,’negative’,’very negative’) and 2

#### ● swing class (positive swing or negative swing)

#### ● Most accurate with Financial Headlines as articles contains past or future reference of

#### ● our subject hence confusing the model about present situation.

## Dependencies

#### ● from ​sklearn.feature_extraction.text ​ import ​TfidfVectorizer

#### ● from ​sklearn.pipeline ​ import ​Pipeline

#### ● from ​sklearn.linear_model ​ import ​SGDClassifier

## Features

```
● positive and negative words of financial system
● Used SGDclassifier to classify our input into +ve or -ve swing
● Used probabilities to classify further into very negative, negative or neutral similarly done
for positive
● E.g. swing is negative with probability of 0.52 then it is neutral similarly
○ 0.45-0.55 (-ve swing ) Neutral Class
○ 0.55-0.75 (-ve swing) Negative Class
○ 0.75- 1.0 (-ve swing) Very Negative Class
```


### Datasets

Used research paper of Bill McDonalds and Tim Loughran (from University of Notre Dame) to
get positive and negative words of financial system




