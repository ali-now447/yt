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

# دالة لحذف الملفات والمجلدات غير الضرورية
def delete_unnecessary_files():
    folders_to_delete = ['downloads']
    unnecessary_files = ['thump']  # يمكن إضافة أنماط ملفات أخرى هنا
    now = datetime.now()
    cutoff = now - timedelta(days=30)  # تحديد فترة 30 يوماً

    # حذف المجلدات المحددة
    for folder in folders_to_delete:
        folder_path = os.path.join(os.getcwd(), folder)
        if os.path.exists(folder_path) and os.path.isdir(folder_path):
            for root, dirs, files in os.walk(folder_path, topdown=False):
                for name in files:
                    file_path = os.path.join(root, name)
                    file_creation_time = datetime.fromtimestamp(os.path.getctime(file_path))
                    if file_creation_time < cutoff:
                        print(f"Deleting file: {file_path}")
                        os.remove(file_path)
                for name in dirs:
                    dir_path = os.path.join(root, name)
                    try:
                        os.rmdir(dir_path)
                        print(f"Deleting directory: {dir_path}")
                    except OSError:
                        pass
            try:
                os.rmdir(folder_path)
                print(f"Deleting main directory: {folder_path}")
            except OSError:
                pass

    # حذف الملفات غير الضرورية في الجذر
    for filename in os.listdir(os.getcwd()):
        file_path = os.path.join(os.getcwd(), filename)
        if os.path.isfile(file_path):
            if any(filename.startswith(prefix) for prefix in unnecessary_files):
                file_creation_time = datetime.fromtimestamp(os.path.getctime(file_path))
                if file_creation_time < cutoff:
                    print(f"Deleting file: {file_path}")
                    os.remove(file_path)

# جدولة وظيفة الحذف لتعمل كل نصف ساعة
schedule.every(30).minutes.do(delete_unnecessary_files)

# تشغيل البوت وجدولة المهام
def run():
    print("🎊 I AM ALIVE 🎊")
    app.start()

    # تنفيذ المهام المجدولة في الخلفية
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    run()