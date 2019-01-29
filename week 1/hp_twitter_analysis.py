# import pandas,tweepy and vaderSentiment
#pip3 install pandas
#pip3 install tweepy
#pip3 install vaderSentiment

import tweepy
import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer
#importing the auth variables from secret.py
import secret

# authenicating with authentication variables
auth = tweepy.OAuthHandler(secret.consumer_key, secret.consumer_secret)
auth.set_access_token(secret.access_token, secret.access_token_secret)

api = tweepy.API(auth)

# search tweets with some keywords
tweets = api.search('Windows', count=300, tweet_mode='extended')
data = pd.DataFrame(data=[tweet.full_text for tweet in tweets], columns=['Tweets'])

#print the first 10 data
print(data.head(10))
print(tweets[0].created_at)
