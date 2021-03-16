import os
import logging
from pyrogram import filters
from telegraph import upload_file
from config import Config


Jebot = Client(
   "Telegraph Uploader",
   api_id=Config.APP_ID,
   api_hash=Config.API_HASH,
   bot_token=Config.TG_BOT_TOKEN,
)

@Jebot.on_message(filters.photo)
async def telegraph(client, message):
    replied = message.reply_to_message
    if not replied:
        await message.reply(message, text='reply to a supported media file')
        return
    if not (
        (replied.photo and replied.photo.file_size <= 5242880)
        or (replied.animation and replied.animation.file_size <= 5242880)
        or (
            replied.video
            and replied.video.file_name.endswith('.mp4')
            and replied.video.file_size <= 5242880
        )
        or (
            replied.document
            and replied.document.file_name.endswith(
                ('.jpg', '.jpeg', '.png', '.gif', '.mp4'),
            )
            and replied.document.file_size <= 5242880
        )
    ):
        await message.reply(message, text='not supported!')
        return
    download_location = await client.download_media(
        message=message.reply_to_message, file_name='root/nana/',
    )
    try:
        response = upload_file(download_location)
    except Exception as document:
        await message.reply(message, text=document)
    else:
        await message.reply(
            message,
            text=f'**Link: https://telegra.ph{response[0]}**',
            disable_web_page_preview=True,
        )
    finally:
        os.remove(download_location)


print(
    """
Bot Started!
Join @Infinity_BOTs
"""
)

Jebot.run()
