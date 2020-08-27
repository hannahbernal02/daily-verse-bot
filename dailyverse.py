import tweepy
import logging
from config import create_api
import time
import requests

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


def tweet_verse(api):
    # https://beta.ourmanna.com/api/v1/get/?format=json

    # make a get request to get the verse of the day
    response = requests.get("https://beta.ourmanna.com/api/v1/get/?format=json")
    response_json = response.json()
    # gets Bible verse
    verse = response_json["verse"]["details"]["text"]
    reference = response_json["verse"]["details"]["reference"]

    tweet = """
            {}
            
        - {}
            """.format(verse, reference)

    print(tweet)

    api.update_status(tweet)

def main():
    api = create_api()
    interval = 60 * 60 * 24 # tweet once a day
    while True:
        tweet_verse(api)
        logger.info("Waiting...")
        time.sleep(interval) # in seconds

if __name__ == "__main__":
    main()