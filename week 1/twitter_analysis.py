# import pandas,tweepy and vaderSentiment
# pip3 install pandas
# pip3 install tweepy
# pip3 install vaderSentiment

import tweepy
import pandas as pd
import sys
import csv
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt
from collections import Counter
# importing the auth variables from secret.py
import secret

# authenicating with authentication variables
auth = tweepy.OAuthHandler(secret.consumer_key, secret.consumer_secret)
auth.set_access_token(secret.access_token, secret.access_token_secret)

api = tweepy.API(auth)

# search tweets with some keywords
tweets = api.search('IndianFootball', count=300, tweet_mode='extended')
data = pd.DataFrame(data=[tweet.full_text for tweet in tweets], columns=['Tweets'])

# print the first 10 data
print(data.head(10))
print(tweets[0].created_at)


import nltk
nltk.download('vader_lexicon')

sid = SentimentIntensityAnalyzer()


l = []
counter = Counter()

for index, row in data.iterrows():
    ss = sid.polarity_scores(row["Tweets"])
    l.append(ss)
    k = ss['compound']
    if k >= 0.5:
        counter['positive'] += 1
    elif k <= -0.5:
        counter['negative'] += 1
    else:
        counter['neutral'] += 1

se = pd.Series(l)
data['polarity'] = se.values

# print(data.head(100))

positive = counter['positive']
negative = counter['negative']
neutral = counter['neutral']

colors = ['green', 'red', 'grey']
sizes = [positive, negative, neutral]
labels = 'Positive', 'Negative', 'Neutral'

# use matplotlib to plot the chart
plt.pie(
    x=sizes,
    shadow=True,
    colors=colors,
    labels=labels,
    startangle=90
)

plt.title("Sentiment")
plt.show()
