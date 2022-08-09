import asyncio
from helpers.filters import command
from config import BOT_NAME, SUPPORT_GROUP, START_IMG
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery



@Client.on_message(command("help") & filters.private & ~filters.group & ~filters.edited)
async def help_cmd(client: Client, message: Message):
    await message.reply_sticker("CAACAgUAAx0CZIiVngABAoCAYqWU-JzBZtfz14vr_DfDkJyy7X8AAjYGAAIsk1lUo7RMhQfOm28eBA")
    await message.reply_photo(f"{START_IMG}", caption=f"""
❄ **ᴀᴠᴀɪʟᴀʙʟᴇ ᴄᴏᴍᴍᴀɴᴅs ɪɴ {BOT_NAME} :**

๏ /play : Şarkı başlatır.
๏ /pause : Yayını durdur.
๏ /resume : Devam ettir.
๏ /skip : Şarkı ve Video yayın durdur.
๏ /end : Sonlandır.
๏ /ping : Botun durumunu gör.
๏ /join : Asistanı sokar.
๏ /id : Gurub ve Kendi Bilginizi verir.
๏ /song : Şarkı adını yazın.
๏ /search :Açmak istediğiniz linki yapıştırın.

✨ **sᴜᴅᴏ ᴄᴏᴍᴍᴀɴᴅs :**

๏ /broadcast : ʙʀᴏᴀᴅᴄᴀsᴛ ᴀ ᴍᴇssᴀɢᴇ ᴛᴏ sᴇʀᴠᴇᴅ ᴄʜᴀᴛs ᴏғ ᴛʜᴇ ʙᴏᴛ.
๏ /eval or /sh : ʀᴜɴs ᴛʜᴇ ɢɪᴠᴇɴ ᴄᴏᴅᴇ ᴏɴ ᴛʜᴇ ʙᴏᴛ's ᴛᴇʀᴍɪɴᴀʟ.
๏ /rmw : ᴄʟᴇᴀʀs ᴀʟʟ ᴛʜᴇ ᴄᴀᴄʜᴇ ᴩʜᴏᴛᴏs ᴏɴ ᴛʜᴇ ʙᴏᴛ's sᴇʀᴠᴇʀ.
๏ /rmp : ᴄʟᴇᴀʀs ᴛʜᴇ ʀᴀᴡ ғɪʟᴇs ᴏғ ᴛʜᴇ ʙᴏᴛ.
๏ /rmd : ᴄʟᴇᴀʀs ᴛʜᴇ ᴅᴏᴡɴʟᴏᴀᴅᴇᴅ ғɪʟᴇs ᴏɴ ᴛʜᴇ ʙᴏᴛ's sᴇʀᴠᴇʀ.""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💫 sᴜᴩᴩᴏʀᴛ 💫", url=f"https://t.me/{redbyteteam}"
                    ),
                    InlineKeyboardButton(
                        "❄ sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ​ ❄", url="hhttps://github.com/Pexxil"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "✨ ᴄʟᴏsᴇ ✨", callback_data="close_play"
                    )
                ]
            ]
       ),
    )
