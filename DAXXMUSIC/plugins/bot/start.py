import time	
import random	
from pyrogram import filters	
from pyrogram.enums import ChatType	
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message	
from youtubesearchpython.__future__ import VideosSearch	

import config	
from DAXXMUSIC import app	
from DAXXMUSIC.misc import _boot_	
from DAXXMUSIC.plugins.sudo.sudoers import sudoers_list	
from DAXXMUSIC.utils.database import get_served_chats, get_served_users, get_sudoers	
from DAXXMUSIC.utils import bot_sys_stats	
from DAXXMUSIC.utils.database import (	
    add_served_chat,	
    add_served_user,	
    blacklisted_chats,	
    get_lang,	
    is_banned_user,	
    is_on_off,	
)	
from DAXXMUSIC.utils.decorators.language import LanguageStart	
from DAXXMUSIC.utils.formatters import get_readable_time	
from DAXXMUSIC.utils.inline import help_pannel, private_panel, start_panel	
from config import BANNED_USERS	
from strings import get_string	



YUMI_PICS = [	
"https://telegra.ph/file/0ad30bd8346bb58fe6d58.jpg",	
"https://telegra.ph/file/8134fa7931e35ba24f721.jpg",	
"https://telegra.ph/file/daaee7888bda72ed29dba.jpg",	
"https://telegra.ph/file/c41810d3f632921d00b43.jpg",	
"https://telegra.ph/file/b912059691f481b8b3439.jpg",	
"https://telegra.ph/file/5aad0a2c595547cfbd59a.jpg",	
"https://telegra.ph/file/a8402f4a91a42893a7928.jpg",	
"https://telegra.ph/file/717dcd9ac67965556bc9f.jpg",	
"https://telegra.ph/file/5e339c35608aedc2c6e86.jpg",	
"https://telegra.ph/file/cb16f4f1f141f88fd9dc3.jpg",	
"https://telegra.ph/file/aaadeab176227f51c0d55.jpg",	
"https://telegra.ph/file/993bfbb0f4c5302b1f65d.jpg",	
"https://telegra.ph/file/729e77a7871fe0075d695.jpg",	
"https://telegra.ph/file/460e59ccd14e203f69166.jpg",	
"https://telegra.ph/file/c706584f9c4d8ec4120c7.jpg",	
"https://telegra.ph/file/ded86839c47bdd843109b.jpg",	
"https://telegra.ph/file/4bbdd86219a0d996c6bbf.jpg",	
"https://telegra.ph/file/3d34c6a50a50d48e0090a.jpg",	
"https://telegra.ph/file/46f3c54fc68bb142e57b7.jpg",	

]	



@app.on_message(filters.command(["start"]) & filters.private & ~BANNED_USERS)	
@LanguageStart	
async def start_pm(client, message: Message, _):	
    await add_served_user(message.from_user.id)	
    if len(message.text.split()) > 1:	
        name = message.text.split(None, 1)[1]	
        if name[0:4] == "help":	
            keyboard = help_pannel(_)	
            return await message.reply_photo(	
                random.choice(YUMI_PICS),	
                caption=_["help_1"].format(config.SUPPORT_CHAT),	
                reply_markup=keyboard,	
            )	
        if name[0:3] == "sud":	
            await sudoers_list(client=client, message=message, _=_)	
            if await is_on_off(2):	
                return await app.send_message(	
                    chat_id=config.LOGGER_ID,	
                    text=f"{message.from_user.mention} ᴊᴜsᴛ sᴛᴀʀᴛᴇᴅ ᴛʜᴇ ʙᴏᴛ ᴛᴏ ᴄʜᴇᴄᴋ <b>sᴜᴅᴏʟɪsᴛ</b>.\n\n<b>ᴜsᴇʀ ɪᴅ :</b> <code>{message.from_user.id}</code>\n<b>ᴜsᴇʀɴᴀᴍᴇ :</b> @{message.from_user.username}",	
                )	
            return	
        if name[0:3] == "inf":	
            m = await message.reply_text("🔎")	
            query = (str(name)).replace("info_", "", 1)	
            query = f"https://www.youtube.com/watch?v={query}"	
            results = VideosSearch(query, limit=1)	
            for result in (await results.next())["result"]:	
                title = result["title"]	
                duration = result["duration"]	
                views = result["viewCount"]["short"]	
                thumbnail = result["thumbnails"][0]["url"].split("?")[0]	
                channellink = result["channel"]["link"]	
                channel = result["channel"]["name"]	
                link = result["link"]	
                published = result["publishedTime"]	
            searched_text = _["start_6"].format(	
                title, duration, views, published, channellink, channel, app.mention	
            )	
            key = InlineKeyboardMarkup(	
                [	
                    [	
                        InlineKeyboardButton(text=_["S_B_8"], url=link),	
                        InlineKeyboardButton(text=_["S_B_9"], url=config.SUPPORT_CHAT),	
                    ],	
                ]	
            )	
            await m.delete()	
            await app.send_photo(	
                chat_id=message.chat.id,	
                photo=thumbnail,	
                caption=searched_text,	
                reply_markup=key,	
            )	
            if await is_on_off(2):	
                return await app.send_message(	
                    chat_id=config.LOGGER_ID,	
                    text=f"{message.from_user.mention} ᴊᴜsᴛ sᴛᴀʀᴛᴇᴅ ᴛʜᴇ ʙᴏᴛ ᴛᴏ ᴄʜᴇᴄᴋ <b>ᴛʀᴀᴄᴋ ɪɴғᴏʀᴍᴀᴛɪᴏɴ</b>.\n\n<b>ᴜsᴇʀ ɪᴅ :</b> <code>{message.from_user.id}</code>\n<b>ᴜsᴇʀɴᴀᴍᴇ :</b> @{message.from_user.username}",	
                )	
    else:	
        out = private_panel(_)	
        served_chats = len(await get_served_chats())	
        served_users = len(await get_served_users())	
        UP, CPU, RAM, DISK = await bot_sys_stats()	
        await message.reply_sticker("CAACAgIAAxkBAAIFN2WyTFRbUAJe50AE40U3bMIS7Gj-AAIyAANkYXEufJi7Pr5eNa4eBA"),
        await message.sleep(0.2)
        await message.delete()
        await message.reply_photo(	
            random.choice(YUMI_PICS),	
            caption=_["start_2"].format(message.from_user.mention, app.mention, UP, DISK, CPU, RAM,served_users,served_chats),	
            reply_markup=InlineKeyboardMarkup(out),	
        )	
        if await is_on_off(2):	
            return await app.send_message(	
                chat_id=config.LOGGER_ID,	
                text=f"{message.from_user.mention} ᴊᴜsᴛ sᴛᴀʀᴛᴇᴅ ᴛʜᴇ ʙᴏᴛ.\n\n<b>ᴜsᴇʀ ɪᴅ :</b> <code>{message.from_user.id}</code>\n<b>ᴜsᴇʀɴᴀᴍᴇ :</b> @{message.from_user.username}",	
            )	


@app.on_message(filters.command(["start"]) & filters.group & ~BANNED_USERS)	
@LanguageStart	
async def start_gp(client, message: Message, _):	
    out = start_panel(_)	
    uptime = int(time.time() - _boot_)	
    await message.reply_photo(	
        random.choice(YUMI_PICS),	
        caption=_["start_1"].format(app.mention, get_readable_time(uptime)),	
        reply_markup=InlineKeyboardMarkup(out),	
    )	
    return await add_served_chat(message.chat.id)	


@app.on_message(filters.new_chat_members, group=-1)	
async def welcome(client, message: Message):	
    for member in message.new_chat_members:	
        try:	
            language = await get_lang(message.chat.id)	
            _ = get_string(language)	
            if await is_banned_user(member.id):	
                try:	
                    await message.chat.ban_member(member.id)	
                except:	
                    pass	
            if member.id == app.id:	
                if message.chat.type != ChatType.SUPERGROUP:	
                    await message.reply_text(_["start_4"])	
                    return await app.leave_chat(message.chat.id)	
                if message.chat.id in await blacklisted_chats():	
                    await message.reply_text(	
                        _["start_5"].format(	
                            app.mention,	
                            f"https://t.me/{app.username}?start=sudolist",	
                            config.SUPPORT_CHAT,	
                        ),	
                        disable_web_page_preview=True,	
                    )	
                    return await app.leave_chat(message.chat.id)	

                out = start_panel(_)	
                await message.reply_photo(	
                    random.choice(YUMI_PICS),	
                    caption=_["start_3"].format(	
                        message.from_user.mention,	
                        app.mention,	
                        message.chat.title,	
                        app.mention,	
                    ),	
                    reply_markup=InlineKeyboardMarkup(out),	
                )	
                await add_served_chat(message.chat.id)	
                await message.stop_propagation()	
        except Exception as ex:	
            print(ex)
            
