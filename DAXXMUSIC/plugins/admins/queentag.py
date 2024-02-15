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

QUEN_TAG = [ "**➠ ʜʟᴏ ᴀʟʟʟ**",
         "**➠ ᴋᴀɪ ʀᴀɢᴜ6 ᴊ🙁**",
         "**➠ ᴍᴀᴛᴇ ʙʜᴀᴜɴɪ ᴅᴀᴋᴀɴɪ ᴍᴜ ᴋᴀʜᴀʀᴀ ʙʜᴀᴜɴɪ ɴᴜʜᴀ👀**",
         "**ᴍᴜ ɪɴꜱᴛᴀ ᴜꜱᴇ ᴋᴀʀᴇɴɪ🥀",
         "**➠ ᴍᴜ ᴋᴀʜᴀᴋᴜ ᴍᴏ ᴘʜᴏᴛᴏ ᴅɪᴇɴɪ ɢᴏᴛᴇ ᴘʀᴏʙʟᴇᴍ ʜᴇɪᴄʜɪ**",
         "**➠  😂 ʜᴍ ᴍᴜ ʀᴀɢɪʟᴇ ᴛᴀᴍᴀ ɢʀᴏᴜᴘ ᴜᴅɪᴊɪʙᴀ✨**",
         "**➠ ꜱᴇ ᴀꜱɪꜰ ᴋᴜ ᴛᴀ ᴍᴜ ᴘʜᴏᴛᴏ ᴍᴀɢᴜɴɪ ꜱɪᴇ ᴍᴀᴛᴇ ᴋᴀɪ ᴘʜᴏᴛᴏ ᴍᴀɢᴜᴄʜɪ**",
         "**➠ @mr_naveen70 ʜʟᴏ ᴘᴀɢʟ **",
         "**➠ ᴍᴜ ᴛᴀ ꜱᴀʜɪᴛᴀ ᴀᴜᴜ ᴋᴇʙᴇ ᴋᴀᴛʜᴀ ʜᴇʙɪɴɪ**",
         "**➠ ᴍᴏ ʙᴀʀᴛʜᴅᴀʏ 10 ɴᴏᴠ ʀᴇ**",
         "**➠ ᴍᴏʀᴏ ɢʀᴀᴅᴜᴀᴛɪᴏɴ ʟᴀꜱᴛ ʏᴇᴀʀ✨**",
         "**➠ ᴍᴜ ᴇɪ ɢʀᴏᴜᴘ ʀᴇ ᴛʜɪʟɪ ꜰɪʀꜱᴛ🌟**",
         "**➠ ᴄʜɪɪɪ ʏᴇ ᴋᴇᴍɪᴛɪ ᴋᴀ ʜᴜɢ 😑**",
         "**➠ ᴍᴜ ᴡɪᴛʜᴏᴜᴛ ᴋɪɴɢ ʀᴀ Qᴜᴇᴇɴ 🤗**",
         "**➠ ᴋɴ ᴇᴛᴇ ᴊᴀʟᴅɪ ꜱᴏɪᴘᴀᴅɪʙɪ ᴀᴜᴜ ᴛᴋ ᴘᴀʀᴇ😁**",
         "**➠ ɴᴀɪ ᴋʜᴀɪɴɪ ᴋʜᴀɪʙᴀ ʟᴀᴛᴇ ᴀᴄʜɪɪ😌**",
         "**➠ ᴄʜᴏᴛᴏ ʙᴀᴅᴀ ᴋɪᴄʜɪ ɴᴜʜᴀ ᴀᴍᴇ ꜱᴀᴍꜱᴛᴇ ꜱᴀɴɢᴀ ᴛᴀᴍᴇ ʙʜɪ ᴍᴏʀᴏ ꜱᴀɴɢᴀ💘**",
        ]


@app.on_message(filters.command(["queenisback"], prefixes=["/", "@", "#"]))
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
            txt = f"{usrtxt} {random.choice(QUEN_TAG)}"
            await client.send_message(chat_id, txt)
            await asyncio.sleep(4)
            usrnum = 0
            usrtxt = ""
    try:
        spam_chats.remove(chat_id)
    except:
        pass



@app.on_message(filters.command(["queenstop", "bhagish", "queenof"]))
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
