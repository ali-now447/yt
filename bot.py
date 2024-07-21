import os
import time
from datetime import datetime, timedelta
from pyrogram import Client
from Youtube.config import Config

# إنشاء عميل Pyrogram
app = Client(
    "my_bot",
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    bot_token=Config.BOT_TOKEN,
    plugins=dict(root="Youtube")
)




def run():
    print("🎊 I AM ALIVE 🎊")
    app.start()
    
