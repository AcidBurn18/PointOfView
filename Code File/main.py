from prefunc import *
from scrap import scrap

def  main():
        
    trainset=pd.read_csv('traindataset.csv')
    model=pickle.load(open("finalized_mode.sav",'rb'))
    mine=pd.read_csv('minetweet.csv')
    newmine=mine.copy()
    newmine.drop('created_at',axis=1,inplace=True)
    mapping=['anger','fear','joy','love','sadness','surprise']
    newmine.dropna(inplace=True)
    newmine.reset_index(inplace=True)

    #nltk.download('stopwords')
    stemer=PorterStemmer()




    for i in range(len(newmine['text'])):
        reg=re.sub('[^a-zA-Z]',' ',newmine['text'][i])
        newmine['text'][i]=reg
    corpus=[]
    for i in range(len(trainset['text'])):
      rev=trainset['text'][i].split()
      rev=[stemer.stem(word) for word in rev if word not in set(stopwords.words('english'))]
      rev=' '.join(rev)
      corpus.append(rev)


    corpusmine=[]
    for i in range(len(newmine['text'])):
      
      revmine=newmine['text'][i].split()
      revmine=[stemer.stem(word) for word in revmine if word not in set(stopwords.words('english'))]
      revmine=' '.join(revmine)
      corpusmine.append(revmine)


    cv=CountVectorizer()
    X=cv.fit(corpus)
    Xmine=X.transform(corpusmine).toarray()


    pred=model.predict(Xmine)
    sentlabel=[]
    for i in range(len(pred)):
        sentlabel.append(mapping[pred[i]])
    sentcsv=pd.DataFrame(sentlabel,columns=['Sentiment'])
    sentcsv.to_csv(path_or_buf= 'C:/Users/Ansh/Desktop/PointOfView/sentiment.csv',index=False) 

    newmine['Sentiment']=newmine['text']
    setiment=pd.read_csv('C:/Users/Ansh/Desktop/PointOfView/sentiment.csv')
    plt.hist(setiment['Sentiment'])
    plt.show()

    all_word=''.join(i for i in corpusmine)



    '''from wordcloud import WordCloud
    wordcloud = WordCloud(colormap='Reds', width=1000, height=1000, mode='RGBA', background_color='white').generate(all_word)
    plt.figure(figsize=(50,40))
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.margins(x=0, y=0)
    plt.show()
    '''
if __name__=="__main__":
    main()
