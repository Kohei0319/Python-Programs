#the code below will allow us to create TwitterBot
#that likes certain hastags and retweets them
#You will neeed Elevated level of approval from twitter developer portal
#this .py file will communicate with secrets.py file to get your keys information
#secrets.py is where you add your api keys, access token keys and so _json

import tweepy as twitter
import secrets
import datetime
import time


#these three lines are coming from library called tweepy
auth = twitter.OAuthHandler(secrets.API_KEY, secrets.API_SECRET_KEY)
auth.set_access_token(secrets.ACCESS_TOKEN, secrets.SECRET_ACCESS_TOKEN)
api = twitter.API(auth)

def bot(hashtags):
    while True:
        print(datetime.datetime.now())

        for hashtag in hashtags:
            for tweet in twitter.Cursor(api.search_tweets, q=hashtag, count=1).items(5):
                try:
                   id=dict(tweet._json)['id'] #finds the id
                   text =dict(tweet._json)['text'] #finds text
                   api.retweet(id) #favorites
                   api.create_favorite(id) #loves/likes tweets
                   print("Tweet ID:", id)
                   print("Tweet Text:", text)
                except twitter.errors.TweepyException as e:
                    print(e)
        time.sleep(10)

bot(['covidlifenepali'])












