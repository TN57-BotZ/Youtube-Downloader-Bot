from pyrogram import Client
import sample_config

DOWNLOAD_LOCATION = "./Downloads"
BOT_TOKEN = sample_config.BOT_TOKEN

APP_ID = sample_config.APP_ID
API_HASH = sample_config.API_HASH


plugins = dict(
    root="plugins",
)

Client(
    "YouTubeDlBot",
    bot_token=BOT_TOKEN,
    api_id=APP_ID,
    api_hash=API_HASH,
    plugins=plugins,
    workers=100
).run()
