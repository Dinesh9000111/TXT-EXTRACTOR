# --------------M----------------------------------

import os
from os import getenv
# ---------------R---------------------------------
API_ID = int(os.environ.get("API_ID", "24692763"))
# ------------------------------------------------
API_HASH = os.environ.get("API_HASH", "8e3840420e9d0895db3231d87c6d21a5")
# ----------------D--------------------------------
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8032691812:AAHFl2RySTfUwqaEPekpkMvj5kubWVFeDEY")
# -----------------A-------------------------------
BOT_USERNAME = os.environ.get("@ilapssbot")
# ------------------X------------------------------
OWNER_ID = int(os.environ.get("OWNER_ID", "8171835867"))
# ------------------X------------------------------

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "8171835867").split()))
# ------------------------------------------------
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002444091022"))
# ------------------------------------------------
MONGO_URL = os.environ.get("MONGO_URL", "mongodb+srv://jihehod332:OM69Q4epgIEcN3xk@cluster0.qzw02.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
# -----------------------------------------------
PREMIUM_LOGS = int(os.environ.get("PREMIUM_LOGS", "-1002444091022"))
