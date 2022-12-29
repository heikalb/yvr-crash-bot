"""Manually test whether your Twitter credentials can post"""
import datetime

import tweepy

# Fill in twitter credentials here
consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""
bearer_token = ""

client = tweepy.Client(consumer_key=consumer_key,
                       consumer_secret=consumer_secret,
                       access_token=access_token,
                       access_token_secret=access_token_secret,
                       bearer_token=bearer_token)

response = client.create_tweet(text=f"This is a drone bird. Testing testing..."
                                    f" {datetime.datetime.now()}")
print(response)
