from pyrogram import filters
from pyrogram.types import Message
import random 
from DAXXMUSIC import app
from datetime import datetime

@app.on_message(filters.left_chat_member)
async def member_has_left(_, m: Message):
    left_gif = "https://telegra.ph/file/d28047520fad932521368.mp4"
    await m.reply_animation(
        animation=left_gif,
        caption=f"๏ sᴀᴅ ᴛᴏ sᴇᴇ ʏᴏᴜ ʟᴇᴀᴠɪɴɢ {m.from_user.mention}\n๏ ᴛᴀᴋᴇ ᴄᴀʀᴇ.!"
    )
