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

# بدء تشغيل البوت
print("🎊 I AM ALIVE 🎊")
app.run()