import os
import datetime

import tweepy


def get_twitter_client():
    consumer_key = os.getenv("TWITTER_CONSUMER_KEY")
    consumer_secret = os.getenv("TWITTER_CONSUMER_SECRET")
    access_token = os.getenv("TWITTER_ACCESS_TOKEN")
    access_token_secret = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")
    bearer_token = os.getenv("TWITTER_BEARER_TOKEN")

    twitter_client = tweepy.Client(consumer_key=consumer_key,
                                   consumer_secret=consumer_secret,
                                   access_token=access_token,
                                   access_token_secret=access_token_secret,
                                   bearer_token=bearer_token)

    return twitter_client


def get_tweet_text():
    return f"This is a drone bird. Testing testing... {datetime.datetime.now()}"


if __name__ == '__main__':
    client = get_twitter_client()
    text_to_tweet = get_tweet_text()

    response = client.create_tweet(text=text_to_tweet)
