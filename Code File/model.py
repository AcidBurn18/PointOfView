import pickle
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.feature_extraction.text import CountVectorizer
import tensorflow as tf
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from sklearn.preprocessing import LabelEncoder
from sklearn import preprocessing
from sklearn.naive_bayes import MultinomialNB

trainset=pd.read_csv('traindataset.csv')
validateset=pd.read_csv('valdataset.csv')
mine=pd.read_csv('minetweet.csv')
newmine=mine.copy()

import nltk
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords

stemer=PorterStemmer()

nltk.download('stopwords')

corpus=[]
for i in range(len(trainset['text'])):
  rev=trainset['text'][i].split()
  rev=[stemer.stem(word) for word in rev if word not in set(stopwords.words('english'))]
  rev=' '.join(rev)
  corpus.append(rev)

encode=preprocessing.LabelEncoder()

trainset['emotion_trans']=encode.fit_transform(trainset['emotion'])

cv=CountVectorizer()
X=cv.fit(corpus)
Y=X.transform(corpus).toarray()


y=trainset['emotion_trans']


mapping=['anger','fear','joy','love','sadness','surprise']



x_train,x_test,y_train,y_test=train_test_split(Y,y,test_size=0.25)

from sklearn.naive_bayes import MultinomialNB
clasify=MultinomialNB()



model=clasify.fit(x_train,y_train)



pred=model.predict(x_test)
file="finalized_mode.sav"
pickle.dump(model,open(file,'wb'))
