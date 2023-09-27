import csv
import random
import string
from pathlib import Path
import datetime

from utils import get_twitter_client

from constants import muni_accounts

MAX_LOC_LEN = 197


def get_tweet_text():
    datum = _get_data()

    role_verb = f"{datum['ROLE'].lower()}{' was killed' if datum['FATAL_VICTIM_COUNT'] == '1' else 's were killed'}"
    muni = string.capwords(datum['CITY'])
    display_muni = muni_accounts.get(muni, muni)

    if datum['LOCATION_NAME']:
        location_preposition = "at" if "&" in datum['LOCATION_NAME'] else "on"
        location = datum['LOCATION_NAME'].split("#")[0].strip()
        # To keep within Twitter char limit
        location = f"{datum['LOCATION_NAME'][:MAX_LOC_LEN - 3]}..." if len(location) > MAX_LOC_LEN else location
        full_location = f"{location_preposition} {string.capwords(location)}, {display_muni}"
    else:
        full_location = f"in {display_muni}"

    ret_text = (f"In this month in {datum['ACCIDENT_YEAR']}\n"
                f"{datum['FATAL_VICTIM_COUNT']} {role_verb} in a car crash {full_location}")

    return ret_text


def _get_data():
    data_fpath = Path(__file__).parent / "data" / "RDAR-22116-Report-data.tsv"
    curr_month = datetime.datetime.now().strftime("%B")

    with open(data_fpath) as f:
        reader = csv.DictReader(f, delimiter='\t')
        ret_rows = [r for r in reader if r['ACCIDENT_MONTH'] == curr_month]

    return random.choice(ret_rows)


if __name__ == '__main__':
    client = get_twitter_client()
    text_to_tweet = get_tweet_text()
    response = client.create_tweet(text=text_to_tweet)
