import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.externals import joblib

data = pd.read_csv('fake.csv')

data = data[data["language"] == 'english']

cols = ["title", "text", "type"]

data = data[cols]
data.dropna(inplace=True)

tf_title = TfidfVectorizer(stop_words="english", lowercase=True)
tf_text = TfidfVectorizer(stop_words="english", lowercase=True)

tf_title.fit(data["title"].values.astype('U')[:])
tf_text.fit(data["text"].values.astype('U')[:])

temp = tf_title.transform(data["title"].values.astype('U')[:])
vec_title = temp.toarray()
temp = tf_text.transform(data["text"].values.astype('U')[:])
vec_text = temp.toarray()

Train_text, test_text, Train_labels_text, test_labels_text = train_test_split(vec_text, data["type"][:], test_size=0.1)
Train_title, test_title, Train_labels_title, test_labels_title = train_test_split(vec_title, data["type"][:],
                                                                                  test_size=0.1)

text_clf = LogisticRegression()
text_clf.fit(Train_text, Train_labels_text)
print(text_clf.score(test_text, test_labels_text))

title_clf = LogisticRegression()
title_clf.fit(Train_title, Train_labels_title)
print(title_clf.score(test_title, test_labels_title))

joblib.dump(tf_title, 'title_vectorizer.pkl')
joblib.dump(tf_text, 'text_vectorizer.pkl')

joblib.dump(title_clf, 'title_clf.pkl')
joblib.dump(text_clf, 'text_clf.pkl')

def Classifier(title,text):
    '''
	takes input text and title and returns the prediction
    '''
    temp = tf_title.transform([title])
    vec_title = temp.toarray()
    temp = tf_text.transform([text])
    vec_text = temp.toarray()
    
    return text_clf.predict(vec_text),title_clf.predict(vec_title)
