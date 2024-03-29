import sys
import csv
import random
import string
from glob import iglob
from pathlib import Path

from utils import get_twitter_client
from constants import ICBC_DATA_START_YEAR, ICBC_DATA_END_YEAR, MIN_CRASHES, \
                      AREA_2_FILE_GLOB, DEFAULT_AREA, MAX_SITE_NAME_LENGHTH, muni_accounts


def get_area():
    ret_area = sys.argv[1] if len(sys.argv) >= 2 else DEFAULT_AREA

    if ret_area not in AREA_2_FILE_GLOB:
        raise ValueError(f"Invalid area arg: {ret_area}")

    return ret_area


def get_tweet_text(area=DEFAULT_AREA):
    location_crashnums = _get_crash_data(area=area)
    site, num_crashes, muni = random.choice(location_crashnums)
    muni_rep = muni_accounts.get(string.capwords(muni), string.capwords(muni))
    location_type = "intersection" if "&" in site else "street"

    if len(site) > MAX_SITE_NAME_LENGHTH:
        site = f"{site[:MAX_SITE_NAME_LENGHTH - 3]}..."

    ret_text = (f"Today's featured dangerous {location_type}:\n"
                f"{string.capwords(site)}, {muni_rep}\n"
                f"with {num_crashes} crashes causing injury or death "
                f"{ICBC_DATA_START_YEAR}-{ICBC_DATA_END_YEAR}")

    return ret_text


def _get_crash_data(area=DEFAULT_AREA):
    data_file_glob = AREA_2_FILE_GLOB.get(area)
    location_crashnums = []

    for fp in iglob(data_file_glob):
        with open(fp, encoding="utf16") as f:
            reader = csv.reader(f, delimiter='\t')
            next(reader)
            curr_muni = Path(fp).stem.capitalize()
            location_crashnums.extend((r[0], r[1], curr_muni)
                                      for r in reader if int(r[1].replace(',', '')) > MIN_CRASHES)

    return location_crashnums


if __name__ == '__main__':
    area = get_area()
    client = get_twitter_client()
    text_to_tweet = get_tweet_text(area=area)
    response = client.create_tweet(text=text_to_tweet)
