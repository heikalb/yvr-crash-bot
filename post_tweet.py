import os
import csv
import random
import string

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
    muni = "Vancouver"

    with open("data/vancouver.csv", encoding="utf16") as f:
        reader = csv.reader(f, delimiter='\t')
        next(reader)
        location_crashnums = [r for r in reader if int(r[1]) > 60]

    location, num_crashes = random.choice(location_crashnums)
    location_type = "intersection" if "&" in location else "street"

    ret_text = (f"Today's featured dangerous {location_type}:\n"
                f"{string.capwords(location)} ({muni})\n"
                f"with {num_crashes} crashes causing injury or death 2017-2021")

    return ret_text


if __name__ == '__main__':
    client = get_twitter_client()
    text_to_tweet = get_tweet_text()

    response = client.create_tweet(text=text_to_tweet)
