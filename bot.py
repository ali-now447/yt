import os
import schedule
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

# دالة لحذف الملفات القديمة
def delete_old_files():
    folder = 'path_to_your_files_folder'  # ضع هنا مسار المجلد الخاص بك
    now = datetime.now()
    cutoff = now - timedelta(days=30)  # تحديد فترة 30 يوماً

    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        if os.path.isfile(file_path):
            file_creation_time = datetime.fromtimestamp(os.path.getctime(file_path))
            if file_creation_time < cutoff:
                print(f"Deleting file: {file_path}")
                os.remove(file_path)

# جدولة وظيفة الحذف لتعمل كل ساعة
schedule.every().hour.do(delete_old_files)

# تشغيل البوت وجدولة المهام
def run():
    print("🎊 I AM ALIVE 🎊")
    app.start()

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    run()