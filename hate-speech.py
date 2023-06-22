import pandas as pd
import numpy as np
dataset=pd.read_csv("labeled_data.csv")
print(dataset)
print(dataset.describe())
dataset['labels']=dataset['class'].map({0:"hate speech",1:"offensive language",2:"neither"})
data=dataset[["tweet",'labels']]
print(data)
#re-regression,nltk-national language toolkit ,stopwords-most common words like is they that 
import re
import nltk
from nltk.corpus import stopwords
nltk.download("stopwords")
#stammers are bringing it into orginal from like using to use etc
stemmer=nltk.SnowballStemmer("english")
stopwords=set(stopwords.words("english"))
#cleaning data by eliminating all the words that are common and website links
import string
def clean(text):
    text=str(text).lower()
    text=re.sub('https://\s+www\.s+.','',text)
    text=re.sub('\[.*?\]','',text)
    text=re.sub('<.*?>','',text)
    text=re.sub('\n','',text)
    text=re.sub('\w*\d\w*','',text)
    text=re.sub('[%s]'%re.escape(string.punctuation),'',text)

    text=[word for word in text.split(' ') if word  not in stopwords]
    text=" ".join(text)
    #stemming
    text=[stemmer.stem(word) for word in text.split(" ")]
    text=" ".join(text)
    return text
data['tweet']= data['tweet'].apply(clean)
print(data)
x=np.array(data['tweet'])
y=np.array(data['labels'])
print(x,y)
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.33,random_state=42)
#building ml module
from sklearn.tree import DecisionTreeClassifier
dt=DecisionTreeClassifier()
dt.fit(x_train,y_train)
y_pred=dt.predict(x_test)
from sklearn.metrics import confusion_matrix
cn=confusion_matrix(y_test,y_pred)
print(cn)
""" #result
array([[ 158,   47,  260],
       [  33, 1145,  201],
       [ 246,  228, 5861]], dtype=int64)"""
import seaborn as sns
import matplotlib.pyplot as ply
sns.heatmap(cn,annot=True,fmt='f',cmap="YlGnBu")
from sklearn.metrics import accuracy_score
accuracy_score(y_test,y_pred)

#trying sample example
sample="lets kill everyone in the city"
sample=clean(sample)
cv=CountVectorizer()
dt1=cv.transform([sample]).toarray()
print(dt.predict(dt1))

def predict(text):
    text=clean(text)
    cv=CountVectorizer()
    dt1=cv.transform([sample]).toarray()
    print(dt.predict(dt1))


