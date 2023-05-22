import csv
import random
import string
from pathlib import Path
import datetime

from utils import get_twitter_client


def get_tweet_text():
    datum = _get_data()
    role = f"{datum['ROLE'].lower()}{'' if datum['FATAL_VICTIM_COUNT'] == '1' else 's'}"
    location_preposition = "at" if "&" in datum['LOCATION_NAME'] else "on"
    datum['LOCATION_NAME'] = datum['LOCATION_NAME'] + " # 001700 to 1800"
    location = datum['LOCATION_NAME'].split("#")[0].strip()

    # To keep within Twitter char limit
    location = f"{datum['LOCATION_NAME'][:172 - 3]}..." if len(location) > 172 else location

    ret_text = (f"Traffic death anniversary:\n"
                f"{datum['FATAL_VICTIM_COUNT']} {role} died in a car crash\n"
                f"{location_preposition} {string.capwords(location)}, {string.capwords(datum['CITY'])}\n"
                f"on a day in {datum['ACCIDENT_MONTH']} {datum['ACCIDENT_YEAR']}")

    return ret_text


def _get_data():
    data_fpath = Path(__file__).parent / "data/RDAR-22116-Report-data.tsv"
    curr_month = datetime.datetime.now().strftime("%B")

    with open(data_fpath) as f:
        reader = csv.DictReader(f, delimiter='\t')
        ret_rows = [r for r in reader if r['ACCIDENT_MONTH'] == curr_month]

    return random.choice(ret_rows)


if __name__ == '__main__':
    client = get_twitter_client()
    text_to_tweet = get_tweet_text()
    print(text_to_tweet)
    exit()
    response = client.create_tweet(text=text_to_tweet)
