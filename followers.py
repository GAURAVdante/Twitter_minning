#!/usr/local/env python

import tweepy
from tweepy import OAuthHandler
import simplejson as json

consumer_key = 'gLDzwf04s32QjjIj17PGBo4WB'
consumer_secret = 'hJl8Y23S3wASY8L3KPcKUhWlGKTHmocv2BTkNzlZ1HyME4cqIX'
access_token = '933511403456970752-PAwmIub38XxQUMjOO9OspKBKb1KlW6X'
access_secret =  '3hwxqsn9dTAFDZ73YFupTmESXpOOso19Aue6rn5tfqNpb'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)





def process_or_store(tweet):
    print(json.dumps(tweet))





#for status in tweepy.Cursor(api.home_timeline).items(10):
    # Process a single status
#    process_or_store(status._json)


for friend in tweepy.Cursor(api.friends).items(2):
 process_or_store(friend._json)




