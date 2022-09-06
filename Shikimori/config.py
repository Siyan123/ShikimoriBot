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
    BOT_ID = "1970819227"
    BOT_USERNAME = '@No_one_caresx_bot'
    ANILIST_REDIRECT_URL = "https://anilist.co/api/v2/oauth/pin"
    ANILIST_CLIENT = "7905"
    ANILIST_SECRET = "lkXFhQKakw1VJdqGS4HDe7BkDjcZu5SpmOw5wyVp"
    API_ID = 8781248   # integer value, dont use ""
    API_HASH = "329a9246cc001b67895fd68a85d0f867"
    TOKEN = '1970819227:AAGxSeg5YGA8QJRobdhEm042sRcYAPodBrk' # This var used to be API_KEY but it is now TOKEN, adjust accordingly.
    OWNER_ID = 1174557449  # If you dont know, run the bot and do /id in your private chat with it, also an integer
    OWNER_USERNAME = 'rqveriie'
    MONGO_DB_URI = "mongodb://Itachi:vMl3AGWVUcHh0enN@cluster0-shard-00-00.ydoa8.mongodb.net:27017,cluster0-shard-00-01.ydoa8.mongodb.net:27017,cluster0-shard-00-02.ydoa8.mongodb.net:27017/myFirstDatabase?ssl=true&replicaSet=atlas-133a3e-shard-0&authSource=admin&retryWrites=true"
    SUPPORT_CHAT = "TestGin"  # Your own group for support, do not add the @
    JOIN_LOGGER = (
        -1001713790723
    )  # Prints any new group the bot is added to, prints just the name and ID.
    EVENT_LOGS = (
        -1001713790723
    )  # Prints information like gbans, sudo promotes, AI enabled disable states that may help in debugging and shit
    ERROR_LOGS = (
        -1001713790723
    )  # Prints information Error

    # RECOMMENDED
    SQLALCHEMY_DATABASE_URI = "postgresql://frfkdjnf:iMaKcmNYWUV2wRlkXYLhi8Od5g_EVJet@kesavan.db.elephantsql.com/frfkdjnf"  # needed for any database modules
    LOAD = []
    NO_LOAD = ["rss", "cleaner", "connection", "math"]
    WEBHOOK = False
    INFOPIC = True
    URL = None
    DOWN_PATH = ".GinRobot/downloads"
    TEMP_DOWNLOAD_DIRECTORY = ".GinRobot/downloads"
    SPAMWATCH_API = "3624487efd8e4ca9c949f1ab99654ad1e4de854f41a14afd00f3ca82d808dc8c"  # go to support.spamwat.ch to get key
    SPAMWATCH_SUPPORT_CHAT = "@SpamWatchSupport"
    ALLOW_CHATS = "-1001713790723"
    # OPTIONAL
    ##List of id's -  (not usernames) for users which have sudo access to the bot.
    DRAGONS = get_user_list("elevated_users.json", "sudos")
    ##List of id's - (not usernames) for developers who will have the same perms as the owner
    DEV_USERS = get_user_list("elevated_users.json", "devs")
    ##List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    DEMONS = get_user_list("elevated_users.json", "supports")
    # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    TIGERS = get_user_list("elevated_users.json", "tigers")
    WOLVES = get_user_list("elevated_users.json", "whitelists")
    DONATION_LINK = None  # EG, paypal
    CERT_PATH = None
    PORT = 5000
    SESSION_STRING = "1BVtsOLUBu1dSCdXASy3Rkre0zkkQkj9o_dU94XGqpLudqruad4GlGx8-wdGYTZSmpjBg1Z_dLuC-_aDLN0kD_i4h5_Ug17msimBkPosxsr-jOjKbW6kRYAnH_z_1DnlmGb_B5PSuX7bl3GsnsZ2TfyUzSInvKe19_fP3WzPb0RhjgBw8uIGl4UvNuAVAyfbWQtTIJ78nFYyTSbIn88yvzEWsW9P5EnyoMFnMav_UZD8DBJHO-wfSKWJNaIAPM5lXhBrbbUW718yAmcXKVHzaZaVfUBQAs_2xFOUrdffUss3r6T8mi8WUaYwRItp4gYn9XaOh4orgsQzLbqo8mnvH671UG2AqXEY="
    DEL_CMDS = True  # Delete commands that users dont have access to, like delete /ban if a non admin uses it.
    STRICT_GBAN = True
    STRICT_GMUTE = True
    WORKERS = (
        8  # Number of subthreads to use. Set as number of threads your processor uses
    )
    HEROKU_API_KEY = None
    HEROKU_APP_NAME = None
    CF_API_KEY = None 
    LASTFM_API_KEY = None
    STRING_SESSION = "1BVtsOLUBu1dSCdXASy3Rkre0zkkQkj9o_dU94XGqpLudqruad4GlGx8-wdGYTZSmpjBg1Z_dLuC-_aDLN0kD_i4h5_Ug17msimBkPosxsr-jOjKbW6kRYAnH_z_1DnlmGb_B5PSuX7bl3GsnsZ2TfyUzSInvKe19_fP3WzPb0RhjgBw8uIGl4UvNuAVAyfbWQtTIJ78nFYyTSbIn88yvzEWsW9P5EnyoMFnMav_UZD8DBJHO-wfSKWJNaIAPM5lXhBrbbUW718yAmcXKVHzaZaVfUBQAs_2xFOUrdffUss3r6T8mi8WUaYwRItp4gYn9XaOh4orgsQzLbqo8mnvH671UG2AqXEY="
    BAN_STICKER = ""  # banhammer marie sticker id, the bot will send this sticker before banning or kicking a user in chat.
    ALLOW_EXCL = True  # Allow ! commands as well as / (Leave this to true so that blacklist can work)
    CASH_API_KEY = (
        "-V48U2FLLKRHSVD4X"  # Get your API key from https://www.alphavantage.co/support/#api-key
    )
    TIME_API_KEY = "-1CUBX1HXGNHW"  # Get your API key from https://timezonedb.com/api
    WALL_API = (
        "2455acab48f3a935a8e703e54e26d121"  # For wallpapers, get one from https://wall.alphacoders.com/api.php
    )
    AI_API_KEY = "awoo"  # For chatbot, get one from https://coffeehouse.intellivoid.net/dashboard
    BL_CHATS = []  # List of groups that you want blacklisted.
    SPAMMERS = None
    REM_BG_API_KEY = "xYCR1ZyK3ZsofjH7Y6hPcyzC"
    OPENWEATHERMAP_ID = "887da2c60d9f13fe78b0f9d0c5cbaade"
    TRIGGERS = "/ !"
    ARQ_API_KEY = "GXQTZC-ISXBUN-YIZFUZ-MGJBGY-ARQ"
    ARQ_API_URL = "http://arq.hamker.dev"
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
