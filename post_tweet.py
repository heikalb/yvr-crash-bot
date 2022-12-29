import os
import csv
import random
import string
from glob import iglob
from pathlib import Path

import tweepy

from constants import ICBC_DATA_START_YEAR, ICBC_DATA_END_YEAR, MIN_CRASHES, \
                      AREA_2_FILE_GLOB


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


def get_tweet_text(area="Vancouver"):
    location_crashnums = _get_crash_data(area=area)
    site, num_crashes, muni = random.choice(location_crashnums)
    location_type = "intersection" if "&" in site else "street"

    ret_text = (f"Today's featured dangerous {location_type}:\n"
                f"{string.capwords(site)}, {muni}\n"
                f"with {num_crashes} crashes causing injury or death "
                f"{ICBC_DATA_START_YEAR}-{ICBC_DATA_END_YEAR}")

    return ret_text


def _get_crash_data(area="Vancouver"):
    data_file_glob = AREA_2_FILE_GLOB.get(area)
    location_crashnums = []

    for fp in iglob(data_file_glob):
        with open(fp, encoding="utf16") as f:
            reader = csv.reader(f, delimiter='\t')
            next(reader)
            curr_muni = Path(fp).stem.capitalize()
            location_crashnums.extend((r[0], r[1], curr_muni)
                                      for r in reader if int(r[1]) > MIN_CRASHES)

    return location_crashnums


if __name__ == '__main__':
    area = random.choice(["Vancouver", "Metro Vancouver"])
    client = get_twitter_client()
    text_to_tweet = get_tweet_text(area=area)
    response = client.create_tweet(text=text_to_tweet)
