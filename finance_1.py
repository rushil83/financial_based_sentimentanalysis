from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import SGDClassifier

pos = open('pos.txt','r').read().replace('\n',',')
neg = open('neg.txt','r').read().replace('\n',' ')

words = [pos,neg]
classes = ['positive','negative']


text_clf = Pipeline([('vect', TfidfVectorizer(stop_words='english')),('clf', SGDClassifier(loss='modified_huber', penalty='l2',
                                                            alpha=1e-3, n_iter=8, random_state=42))])
text_clf = text_clf.fit(words,classes)
x_test=[]
temp = str(input())
x_test.append(temp)
output=text_clf.predict(x_test)

if text_clf.predict_proba(x_test)[0][0]>=0.75:
    print('very negative')
elif 0.75>text_clf.predict_proba(x_test)[0][0]>=0.55:
    print('negative')
elif 0.55>text_clf.predict_proba(x_test)[0][0]>=0.45:
    print('neutral')
elif 0.45>text_clf.predict_proba(x_test)[0][0]>=0.25:
    print('positive')
elif text_clf.predict_proba(x_test)[0][0]>0.25:
    print('very positive')


text_clf2 = Pipeline([('vect', TfidfVectorizer(stop_words='english')),('clf', SGDClassifier(loss='hinge', penalty='l2',
                                                            alpha=1e-3, n_iter=8, random_state=42))])
text_clf2 = text_clf2.fit(words,classes)
output=text_clf2.predict(x_test)
print('swing : ',output)