import os
import asyncio
import yt_dlp
import requests

from ... import app
from pyrogram import filters
from pyrogram.types import Message
from youtubesearchpython import VideosSearch


@app.on_message(filters.command(["song"], ["/", "!", "."]))
async def song(client: app, message: Message):
    aux = await message.reply_text("**ᴘʀᴏᴄᴇssɪɴɢ ...**")
    if len(message.command) < 2:
        return await aux.edit(
            "**ɢɪᴠᴇ ᴍᴜsɪᴄ ɴᴀᴍᴇ \n💞 ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ sᴏɴɢ❗**"
        )
    try:
        song_name = message.text.split(None, 1)[1]
        vid = VideosSearch(song_name, limit = 1)
        song_title = vid.result()["result"][0]["title"]
        song_link = vid.result()["result"][0]["link"]
        ydl_opts = {
            "format": "mp3/bestaudio/best",
            "verbose": True,
            "geo-bypass": True,
            "nocheckcertificate": True,
            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3"
                }
            ],
            "outtmpl": f"downloads/{song_title}",
        }
        await aux.edit("**ᴅᴏᴡɴʟᴏᴀᴅɪɴɢ...**")
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download(song_link)
        await aux.edit("**ᴜᴘʟᴏᴀᴅɪɴɢ...**")
        await message.reply_audio(f"downloads/{song_title}.mp3")
        try:
            os.remove(f"downloads/{song_title}.mp3")
        except:
            pass
        await aux.delete()
    except Exception as e:
        await aux.edit(f"**Error:** {e}")


###### INSTAGRAM REELS DOWNLOAD


@app.on_message(filters.command(["ig"], ["/", "!", "."]))
async def download_instareels(c: app, m: Message):
    try:
        reel_ = m.command[1]
    except IndexError:
        await m.reply_text("Give me an link to download it...")
        return
    if not reel_.startswith("https://www.instagram.com/reel/"):
        await m.reply_text("In order to obtain the requested reel, a valid link is necessary. Kindly provide me with the required link.")
        return
    OwO = reel_.split(".",1)
    Reel_ = ".dd".join(OwO)
    try:
        await m.reply_video(Reel_)
        return
    except Exception:
        try:
            await m.reply_photo(Reel_)
            return
        except Exception:
            try:
                await m.reply_document(Reel_)
                return
            except Exception:
                await m.reply_text("ɪ ᴀᴍ ᴜɴᴀʙʟᴇ ᴛᴏ ʀᴇᴀᴄʜ ᴛᴏ ᴛʜɪs ʀᴇᴇʟ.")



######

@app.on_message(filters.command(["reel"], ["/", "!", "."]))
async def instagram_reel(client, message):
    if len(message.command) == 2:
        url = message.command[1]
        response = requests.post(f"https://lexica-api.vercel.app/download/instagram?url={url}")
        data = response.json()

        if data['code'] == 2:
            media_urls = data['content']['mediaUrls']
            if media_urls:
                video_url = media_urls[0]['url']
                await message.reply_video(f"{video_url}")
            else:
                await message.reply("ɴᴏ ᴠɪᴅᴇᴏ ғᴏᴜɴᴅ ɪɴ ᴛʜᴇ ʀᴇsᴘᴏɴsᴇ. ᴍᴀʏ ʙᴇ ᴀᴄᴄᴏᴜɴᴛʙɪs ᴘʀɪᴠᴀᴛᴇ.")
        else:
            await message.reply("Request was not successful.")
    else:
        await message.reply("ᴘʟᴇᴀsᴇ ᴘʀᴏᴠɪᴅᴇ ᴀ ᴠᴀʟɪᴅ ɪɴsᴛᴀɢʀᴀᴍ ᴜʀʟ ᴜsɪɴɢ ᴛʜᴇ /reels ᴄᴏᴍᴍᴀɴᴅ.")
        
