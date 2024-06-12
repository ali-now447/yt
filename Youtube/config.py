import os

class Config(object):
     
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7119200505:AAGHUKz6yKtWgPXEtU1bvI0AQea6m4pjTAo")
    API_ID = int(os.environ.get("API_ID", 20737573))
    API_HASH = os.environ.get("API_HASH", "4332b91fef7ae7a15a9f1147d7a483e5")
    #Add your channel id. For force Subscribe.
    CHANNEL = os.environ.get("CHANNEL", "1299814737")
    #Skip or add your proxy from https://github.com/rg3/youtube-dl/issues/1091#issuecomment-230163061
    HTTP_PROXY = ''
