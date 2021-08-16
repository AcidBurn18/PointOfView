import tweepy
from tweepy import OAuthHandler
import pandas as pd
import re
#import pickle
def scrap():
    #Get your keys from Twitter Developer Program
    access_token = ''
    access_token_secret = ''
    consumer_key = ''
    consumer_secret = ''
    auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
    auth.set_access_token(access_token,access_token_secret)
    api=tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)
    tweets=[]
    count=1
    user_tweets=[]
    user_data=api.user_timeline(screen_name="warikoo",count=200,include_rts=False,exclude_replies=True,
                                tweet_mode='extended')
    temp=[]
    user_data_filter=[]
    a=open('c.txt','w',encoding='utf-8')
    for info in user_data[:200]:
        pattern=re.sub("[@][\w]*","",info.full_text)
        final_text_without_tag=re.sub("^\s","",pattern)
        final_text_without_links=re.sub('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',"",final_text_without_tag)
        a.writelines(str(final_text_without_links))
        user_data_list=[info.id,info.created_at,final_text_without_links]
        #temp.append(info.full_text)
        user_data_tu=tuple(user_data_list)
        user_tweets.append(user_data_tu)
    a.close()
    userdf=pd.DataFrame(user_tweets,columns=['id','created_at','text'])
    userdf.to_csv(path_or_buf= 'C:/Users/Ansh/Desktop/PointOfView/PreFinal/minetweet.csv',index=False) 

scrap()
