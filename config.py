import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Telegram API
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
BOT_TOKEN = getenv("BOT_TOKEN")

# Database
MONGO_DB_URI = getenv("MONGO_DB_URI")

# Limits
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 1700))

# ===== FIX STARTS HERE =====
LOG_GROUP_ID = getenv("LOG_GROUP_ID")

if not LOG_GROUP_ID:
    raise SystemExit("[FATAL] LOG_GROUP_ID is missing. Set it in Heroku Config Vars.")

LOG_GROUP_ID = int(LOG_GROUP_ID)
LOGGER_ID = LOG_GROUP_ID
# ===== FIX ENDS HERE =====

OWNER_ID = int(getenv("OWNER_ID"))

# Heroku
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

# API
API_URL = getenv("API_URL", "https://api.thequickearn.xyz")
API_KEY = getenv("API_KEY")

# Git
UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/nonsecularman/IstkharMusic",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv("GIT_TOKEN")

# Support
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/NexaCoders")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/NexaMeetup")

# Assistant
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))

PRIVACY_LINK = getenv(
    "PRIVACY_LINK",
    "https://telegra.ph/Privacy-Policy-for-IstkharMusic-08-14",
)

# Spotify
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET")

PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))

# Telegram limits
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 2145386496))

# Sessions
STRING1 = getenv("STRING_SESSION")
STRING2 = getenv("STRING_SESSION2")
STRING3 = getenv("STRING_SESSION3")
STRING4 = getenv("STRING_SESSION4")
STRING5 = getenv("STRING_SESSION5")

# Runtime vars
BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}

# Images
START_IMG_URL = getenv("START_IMG_URL", "https://files.catbox.moe/bs5gni.jpg")
PING_IMG_URL = getenv("PING_IMG_URL", "https://files.catbox.moe/fa1xas.jpg")
PLAYLIST_IMG_URL = "https://files.catbox.moe/pfjgmf.jpg"
STATS_IMG_URL = "https://files.catbox.moe/st6utj.jpg"

def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60 ** i for i, x in enumerate(reversed(stringt.split(":"))))

DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))

# URL validation
if SUPPORT_CHANNEL and not re.match("(?:http|https)://", SUPPORT_CHANNEL):
    raise SystemExit("[ERROR] SUPPORT_CHANNEL url must start with https://")

if SUPPORT_GROUP and not re.match("(?:http|https)://", SUPPORT_GROUP):
    raise SystemExit("[ERROR] SUPPORT_GROUP url must start with https://")
