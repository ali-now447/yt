# ©️ LISA-KOREA | @SSSi5 | mmmsc | LISA-KOREA/YouTube-Video-Download-Bot

# [⚠️ Do not change this repo link ⚠️] :- https://github.com/LISA-KOREA/YouTube-Video-Download-Bot

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ForceReply
from Youtube.config import Config
from Youtube.script import Translation
from Youtube.forcesub import handle_force_subscribe


########################🎊 Lisa | NT BOTS 🎊######################################################
@Client.on_callback_query(filters.regex("cancel"))
async def cancel(client, callback_query):
    await callback_query.message.delete()

# About command handler
@Client.on_message(filters.private & filters.command("about"))
async def about(client, message):
    if Config.CHANNEL:
      fsub = await handle_force_subscribe(client, message)
      if fsub == 400:
        return
    await message.reply_text(
        text=Translation.ABOUT_TXT,
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(
        [
            [InlineKeyboardButton('⛔️ Close', callback_data='cancel')]
        ]
    ))


# Start command handler
# Start command handler
@Client.on_message(filters.private & filters.command("start"))
async def start(client, message):
    if Config.CHANNEL:
        fsub = await handle_force_subscribe(client, message)
        if fsub == 400:
            return

    # إرسال الصورة مع القائمة الانلاين
    photo_url = 'https://telegra.ph/file/21270c748132fa563ffdc.jpg'  # رابط الصورة التي ترغب في استخدامها
    await client.send_photo(
        chat_id=message.chat.id,
        photo=photo_url,
        caption=Translation.START_TEXT.format(message.from_user.first_name),
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('📍 Update Channel', url='https://t.me/mmmsc'),
                ],
                [
                    InlineKeyboardButton('👩‍💻 Developer', url='https://t.me/SSSi5'),
                    InlineKeyboardButton('👥 For more', url='https://t.me/lllcz'),
                ],
                [
                    InlineKeyboardButton('⛔️ Close', callback_data='cancel')
                ]
            ]
        )
    )

# Help command handler
@Client.on_message(filters.command("help"))
def help(client, message):
    help_text = """
    هَهلا عُمري بيك !

للتحميل فيد ار ريلز فقط أرسل رابط الفيديو .

لتحميل مقاطع الوصوتية استخدم الاوامر :

 **يوت - بحث - تحميل - yt - song**
    
Enjoy using the bot!

   ©️ Channel : @mmmsc
    """
    message.reply_text(help_text)

########################🎊 Lisa | NT BOTS 🎊######################################################
