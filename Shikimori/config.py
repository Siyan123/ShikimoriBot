# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
import json
import os

from Shikimori.vars import HEROKU_API_KEY, HEROKU_APP_NAME, REDIS_URL

def get_user_list(config, key):
    with open("{}/Senku/{}".format(os.getcwd(), config), "r") as json_file:
        return json.load(json_file)[key]


LOGGER = True
    # REQUIRED
    # Login to https://my.telegram.org and fill in these slots with the details given by it
    






class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
