import os
import logging
from pyrogram import Client, filters
from telegraph import upload_file
from config import Config
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import UserNotParticipant, UserBannedInChannel

Jebot = Client(
   "Telegraph Uploader",
   api_id=Config.APP_ID,
   api_hash=Config.API_HASH,
   bot_token=Config.TG_BOT_TOKEN,
)

@Jebot.on_message(filters.command("start") & filters.private)
async def start(client, message):
   if message.chat.type == 'private':
       await Jebot.send_message(
               chat_id=message.chat.id,
               text="""<b>Hey There, I'm Telegraph Bot

I can upload photos or videos to telegraph. Made by @JEBotZ

Hit help button to find out more about how to use me</b>""",   
                            reply_markup=InlineKeyboardMarkup(
                                [[
                                        InlineKeyboardButton(
                                            "Help", callback_data="help"),
                                        InlineKeyboardButton(
                                            "Channel", url="https://t.me/Infinity_BOTs")
                                    ],[
                                      InlineKeyboardButton(
                                            "Source Code", url="https://github.com/ImJanindu/JETelegraphBot")
                                    ]]
                            ),        
            disable_web_page_preview=True,        
            parse_mode="html")

@Jebot.on_message(filters.command("help") & filters.private)
async def help(client, message):
    if message.chat.type == 'private':   
        await Jebot.send_message(
               chat_id=message.chat.id,
               text="""<b>Telegraph Bot Help

Just send a photo or video less than 5mb file size, I'll upload it to telegraph.

@JEBotZ</b>""",
        reply_markup=InlineKeyboardMarkup(
                                [[
                                        InlineKeyboardButton(
                                            "Back", callback_data="start"),
                                        InlineKeyboardButton(
                                            "About", callback_data="about"),
                                  ],[
                                        InlineKeyboardButton(
                                            "Source Code", url="https://github.com/ImJanindu/JETelegraphBot")
                                    ]]
                            ),        
            disable_web_page_preview=True,        
            parse_mode="html")

@Jebot.on_message(filters.command("about") & filters.private)
async def about(client, message):
    if message.chat.type == 'private':   
        await Jebot.send_message(
               chat_id=message.chat.id,
               text="""<b>About Telegraph Bot!</b>

<b>♞ Developer:</b> <a href="https://t.me/ImJanindu">Jason</a>

<b>♞ Support:</b> <a href="https://t.me/InfinityBOTs_Support">Infinity BOTs Support</a>

<b>♞ Library:</b> <a href="https://github.com/pyrogram/pyrogram">Pyrogram</a>

<b>@JEBotZ</b>""",
     reply_markup=InlineKeyboardMarkup(
                                [[
                                        InlineKeyboardButton(
                                            "Back", callback_data="help"),
                                        InlineKeyboardButton(
                                            "Source Code", url="https://github.com/ImJanindu/JETelegraphBot")
                                    ]]
                            ),        
            disable_web_page_preview=True,        
            parse_mode="html")


@Jebot.on_message(filters.photo & filters.private)
async def telegraphvid(c: Client, message: Message):
    if Config.UPDATES_CHANNEL is not None:
        try:
            user = await c.get_chat_member(Config.UPDATES_CHANNEL, message.chat.id)
            if user.status == "kicked":
                await c.send_message(
                    chat_id=message.chat.id,
                    text="Sorry, You are Banned to use me. Contact my [Support Group](https://t.me/InfinityBots_Support).",
                    parse_mode="markdown",
                    disable_web_page_preview=True
                )
                return
        except UserNotParticipant:
            await c.send_message(
                chat_id=message.chat.id,
                text="**Please Join My Updates Channel to use me 😉**",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("Join Updates Channel", url=f"https://t.me/{Config.UPDATES_CHANNEL}")
                        ]
                    ]
                ),
                parse_mode="markdown"
            )
            return
        except Exception:
            await c.send_message(
                chat_id=message.chat.id,
                text="Something went Wrong. Contact my [Support Group](https://t.me/InfinityBots_Support).",
                parse_mode="markdown",
                disable_web_page_preview=True)
            return
    msg = await message.reply_text("Uploading To Telegraph...")
    download_location = await c.download_media(
        message=message, file_name='root/jetg')
    try:
        response = upload_file(download_location)
    except:
        await msg.edit_text("Media file size should be less than 5mb.") 
    else:
        sed = InlineKeyboardMarkup(
                    [[InlineKeyboardButton("Telegraph Link", url=f"https://telegra.ph{response[0]}")]])
         
        await msg.edit(f'**Uploaded To [Telegraph](https://telegra.ph{response[0]})\n\nJoin @JEBotZ**',
            disable_web_page_preview=False,
            reply_markup=sed)
    finally:
        os.remove(download_location)
         
@Jebot.on_message(filters.video & filters.private)
async def telegraphvid(c: Client, message: Message):
    if Config.UPDATES_CHANNEL is not None:
        try:
            user = await c.get_chat_member(Config.UPDATES_CHANNEL, message.chat.id)
            if user.status == "kicked":
                await c.send_message(
                    chat_id=message.chat.id,
                    text="Sorry, You are Banned to use me. Contact my [Support Group](https://t.me/InfinityBots_Support).",
                    parse_mode="markdown",
                    disable_web_page_preview=True
                )
                return
        except UserNotParticipant:
            await c.send_message(
                chat_id=message.chat.id,
                text="**Please Join My Updates Channel to use me 😉**",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("Join Updates Channel", url=f"https://t.me/{Config.UPDATES_CHANNEL}")
                        ]
                    ]
                ),
                parse_mode="markdown"
            )
            return
        except Exception:
            await c.send_message(
                chat_id=message.chat.id,
                text="Something went Wrong. Contact my [Support Group](https://t.me/InfinityBots_Support).",
                parse_mode="markdown",
                disable_web_page_preview=True)
            return
    msg = await message.reply_text("Uploading To Telegraph...")
    download_location = await c.download_media(
        message=message, file_name='root/jetg')
    try:
        response = upload_file(download_location)
    except:
        await msg.edit_text("Media file size should be less than 5mb.") 
    else:
        sed = InlineKeyboardMarkup(
                    [[InlineKeyboardButton("Telegraph Link", url=f"https://telegra.ph{response[0]}")]])
         
        await msg.edit('**Uploaded To [Telegraph](https://telegra.ph{response[0]})\n\nJoin @JEBotZ**',
            disable_web_page_preview=False,
            reply_markup=sed)
    finally:
        os.remove(download_location)
         
@Jebot.on_message(filters.animation & filters.private)
async def telegraphvid(c: Client, message: Message):
    if Config.UPDATES_CHANNEL is not None:
        try:
            user = await c.get_chat_member(Config.UPDATES_CHANNEL, message.chat.id)
            if user.status == "kicked":
                await c.send_message(
                    chat_id=message.chat.id,
                    text="Sorry, You are Banned to use me. Contact my [Support Group](https://t.me/InfinityBots_Support).",
                    parse_mode="markdown",
                    disable_web_page_preview=True
                )
                return
        except UserNotParticipant:
            await c.send_message(
                chat_id=message.chat.id,
                text="**Please Join My Updates Channel to use me 😉**",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("Join Updates Channel", url=f"https://t.me/{Config.UPDATES_CHANNEL}")
                        ]
                    ]
                ),
                parse_mode="markdown"
            )
            return
        except Exception:
            await c.send_message(
                chat_id=message.chat.id,
                text="Something went Wrong. Contact my [Support Group](https://t.me/InfinityBots_Support).",
                parse_mode="markdown",
                disable_web_page_preview=True)
            return
    msg = await message.reply_text("Uploading To Telegraph...")
    download_location = await c.download_media(
        message=message, file_name='root/jetg')
    try:
        response = upload_file(download_location)
    except:
        await msg.edit_text("Media file size should be less than 5mb.") 
    else:
        sed = InlineKeyboardMarkup(
                    [[InlineKeyboardButton("Telegraph Link", url=f"https://telegra.ph{response[0]}")]])
         
        await msg.edit('**Uploaded To [Telegraph](https://telegra.ph{response[0]})\n\nJoin @JEBotZ**',
            disable_web_page_preview=False,
            reply_markup=sed)
    finally:
        os.remove(download_location)


@Jebot.on_callback_query()
async def button(bot, update):
      cb_data = update.data
      if "help" in cb_data:
        await update.message.delete()
        await help(bot, update.message)
      elif "about" in cb_data:
        await update.message.delete()
        await about(bot, update.message)
      elif "start" in cb_data:
        await update.message.delete()
        await start(bot, update.message)

print(
    """
Bot Started!
Join @Infinity_BOTs
"""
)

Jebot.run()
