from DAXXMUSIC import app 
import asyncio
import random
from pyrogram import Client, filters
from pyrogram.enums import ChatType, ChatMemberStatus
from pyrogram.errors import UserNotParticipant
from pyrogram.types import ChatPermissions

spam_chats = []

EMOJI = [ "🦋🦋🦋🦋🦋",
          "🧚🌸🧋🍬🫖",
          "🥀🌷🌹🌺💐",
          "🌸🌿💮🌱🌵",
          "❤️💚💙💜🖤",
          "💓💕💞💗💖",
          "🌸💐🌺🌹🦋",
          "🍔🦪🍛🍲🥗",
          "🍎🍓🍒🍑🌶️",
          "🧋🥤🧋🥛🍷",
          "🍬🍭🧁🎂🍡",
          "🍨🧉🍺☕🍻",
          "🥪🥧🍦🍥🍚",
          "🫖☕🍹🍷🥛",
          "☕🧃🍩🍦🍙",
          "🍁🌾💮🍂🌿",
          "🌨️🌥️⛈️🌩️🌧️",
          "🌷🏵️🌸🌺💐",
          "💮🌼🌻🍀🍁",
          "🧟🦸🦹🧙👸",
          "🧅🍠🥕🌽🥦",
          "🐷🐹🐭🐨🐻‍❄️",
          "🦋🐇🐀🐈🐈‍⬛",
          "🌼🌳🌲🌴🌵",
          "🥩🍋🍐🍈🍇",
          "🍴🍽️🔪🍶🥃",
          "🕌🏰🏩⛩️🏩",
          "🎉🎊🎈🎂🎀",
          "🪴🌵🌴🌳🌲",
          "🎄🎋🎍🎑🎎",
          "🦅🦜🕊️🦤🦢",
          "🦤🦩🦚🦃🦆",
          "🐬🦭🦈🐋🐳",
          "🐔🐟🐠🐡🦐",
          "🦩🦀🦑🐙🦪",
          "🐦🦂🕷️🕸️🐚",
          "🥪🍰🥧🍨🍨",
          " 🥬🍉🧁🧇",
        ] 

EVE_TAG = [ "**➠ ɢᴏᴏᴅ ᴇᴠᴇɴɪɴɢ ᴍᴇʀɪ ᴊᴀɴᴀ🤗💘**",
         "**➠ ᴄʜᴀʟᴏ ɴᴀꜱᴛᴀ ᴘᴀɴɪ ʟᴀᴏ😋😇**",
         "**➠ ꜱᴜɴᴏ ɴᴀ ᴍᴇʀɪ ᴛᴀʀᴀꜰ ꜱᴇ Qᴜᴇᴇɴ ᴋᴏ ᴇᴠᴇɴɪɴɢ ʙᴏʟɴᴀ❤️✨**",
         "**➠ ɴᴀꜱᴛᴀ ᴍᴀɪ ᴋʏᴀ ᴋᴀʀᴏɢᴇ ʙᴀʙʏ👀👀**",
         "**➠ ᴛᴜᴍ ᴋᴀʜᴀ ꜱᴇ ʜᴏ ʙʜᴀʏᴀ💥**",
         "**➠  ᴀʙʜɪɪ ꜱᴜʀᴀᴊ ᴋᴀ ᴄᴏʟᴏᴜʀ ʙᴀᴛᴀᴏ🌅**",
         "**➠ ᴛᴜᴍʜᴀʀᴀ ᴛɪɴᴀ ᴀᴜɴᴛʏ ᴋɪ ᴄʜᴏᴛᴏ ʙᴇᴛɪ ᴋɪ ʟᴀᴅᴋɪ ᴘᴜᴊᴀ ᴋᴏ ᴍᴇʀɪ ᴛᴀʀᴀꜰ ꜱᴇ ɢᴏᴏᴅ ᴇᴠᴇɴɪɴɢ ʙᴏʟɴᴀ✨👀**",
         "**➠ ʏᴇ ᴇᴠᴇɴɪɴɢ ᴋᴏ ʙʜɪ ᴋᴜᴄʜ ɴᴀʜɪ ʜᴜᴀ🙂**",
         "**➠ ʏᴇ ᴇᴠᴇɴɪɴɢ ᴍᴀɪ ᴛᴜᴍ ᴍᴇʀɪ ʀᴀɴɪ ʙᴏɴᴏɢɪ ᴋʏᴀ🤗**",
         "**➠ ᴘᴀɢᴀʟ ᴀʙʙ ᴛᴏʜ ᴜᴛʜᴊᴀ ꜱᴀᴀᴍ ʜᴏ ɢᴀʏᴀ ʜᴀɪ🦋✨**",
         "**➠ ʏᴇʜ ᴍᴇʀɪ ᴊᴀɴᴀ ᴛᴇʀᴀ ᴏᴘ ᴡᴀʟᴀ ɢᴏᴏᴅ ᴇᴠᴇɴɪɴɢ ʜᴏ ɢᴀʏᴀ✨💥**",
         "**➠ ꜱᴜʀᴀᴊ ᴅʜᴀʟᴀ Qᴜᴇᴇɴ ᴄʜᴀʟɪɢᴀʏɪ😢🙂**",
         "**➠ ꜱᴀʙ ᴋᴏ ɢᴏᴏᴅ ᴇᴠᴇɴɪɴɢ ʙᴏʟ ᴊᴀʟᴅɪ 💘**",
         "**➠ ᴊᴀɴᴇᴍᴀɴ ᴇᴋ ʀᴏᴍᴀɴᴛɪᴄ ɢᴀɴᴀ ɢᴀᴏ 🙈**",
         "**➠ ᴀᴘᴘ ʙᴀᴛᴀᴏ ɢᴏᴏᴅ ᴇᴠᴇɴɪɴɢ ᴋʏᴜɴ ʙᴏʟ ᴛᴇ ʜᴀɪɴ🙂👀**",
         "**➠ ᴊᴀʟᴅɪ ɢʀᴏᴜᴘ ᴍᴀɪ ᴄʜᴀᴛ ᴋᴀʀᴏ ᴏʀ ᴠᴄ ᴀᴏᴏ ꜱᴜʀᴀᴊ ᴅʜᴀʟɴᴇ ᴡᴀʟᴀ ʜᴀɪ..🌟**",
         "**➠ ʏᴇʜ ᴍᴇʀɪ ᴊᴀɴᴀ ᴇᴠᴇɴɪɴɢ ᴇᴠᴇɴɪɴɢ ᴇᴠᴇɴɪɴɢ ᴇᴠᴇɴɪɴɢ ᴇᴠᴇɴɪɴɢ ᴇᴠᴇɴɪɴɢ ᴇᴠᴇɴɪɴɢ 🌆**",
        ]


@app.on_message(filters.command(["evetag"], prefixes=["/", "@", "#"]))
async def mention_allvc(client, message):
    chat_id = message.chat.id
    if message.chat.type == ChatType.PRIVATE:
        return await message.reply("๏ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴏɴʟʏ ғᴏʀ ɢʀᴏᴜᴘs.")

    is_admin = False
    try:
        participant = await client.get_chat_member(chat_id, message.from_user.id)
    except UserNotParticipant:
        is_admin = False
    else:
        if participant.status in (
            ChatMemberStatus.ADMINISTRATOR,
            ChatMemberStatus.OWNER
        ):
            is_admin = True
    if not is_admin:
        return await message.reply("๏ ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴀᴅᴍɪɴ ʙᴀʙʏ, ᴏɴʟʏ ᴀᴅᴍɪɴs ᴄᴀɴ ᴛᴀɢ ᴍᴇᴍʙᴇʀs. ")
    if chat_id in spam_chats:
        return await message.reply("๏ ᴘʟᴇᴀsᴇ ᴀᴛ ғɪʀsᴛ sᴛᴏᴘ ʀᴜɴɴɪɴɢ ᴍᴇɴᴛɪᴏɴ ᴘʀᴏᴄᴇss...")
    spam_chats.append(chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.get_chat_members(chat_id):
        if not chat_id in spam_chats:
            break
        if usr.user.is_bot:
            continue
        usrnum += 1
        usrtxt += f"[{usr.user.first_name}](tg://user?id={usr.user.id}) "

        if usrnum == 1:
            txt = f"{usrtxt} {random.choice(EVE_TAG)}"
            await client.send_message(chat_id, txt)
            await asyncio.sleep(4)
            usrnum = 0
            usrtxt = ""
    try:
        spam_chats.remove(chat_id)
    except:
        pass



@app.on_message(filters.command(["eveningstop", "evenstop", "evestop"]))
async def cancel_spam(client, message):
    if not message.chat.id in spam_chats:
        return await message.reply("๏ ᴄᴜʀʀᴇɴᴛʟʏ ɪ'ᴍ ɴᴏᴛ ᴛᴀɢɢɪɴɢ ʙᴀʙʏ.")
    is_admin = False
    try:
        participant = await client.get_chat_member(message.chat.id, message.from_user.id)
    except UserNotParticipant:
        is_admin = False
    else:
        if participant.status in (
            ChatMemberStatus.ADMINISTRATOR,
            ChatMemberStatus.OWNER
        ):
            is_admin = True
    if not is_admin:
        return await message.reply("๏ ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴀᴅᴍɪɴ ʙᴀʙʏ, ᴏɴʟʏ ᴀᴅᴍɪɴs ᴄᴀɴ ᴛᴀɢ ᴍᴇᴍʙᴇʀs.")
    else:
        try:
            spam_chats.remove(message.chat.id)
        except:
            pass
        return await message.reply("๏ ᴍᴇɴᴛɪᴏɴ ᴘʀᴏᴄᴇss sᴛᴏᴘᴘᴇᴅ ๏")
