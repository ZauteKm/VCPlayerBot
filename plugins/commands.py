from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, InputMediaDocument
from plugins.controls import is_admin
from pyrogram import Client, filters
from utils import update, is_admin
from config import Config
from logger import LOGGER
import os

HOME_TEXT = "<b>Hey  [{}](tg://user?id={}) 🙋‍♂️\n\nIam A Bot Built To Play or Stream Videos In Telegram VoiceChats.\nI Can Stream Any YouTube Video Or A Telegram File Or Even A YouTube Live.</b>"
admin_filter=filters.create(is_admin) 

@Client.on_message(filters.command(['start', f"start@{Config.BOT_USERNAME}"]))
async def start(client, message):
    buttons = [
        [
            InlineKeyboardButton('📢 Channel', url='https://t.me/ZauteKm'),
            InlineKeyboardButton('Source 🔥', url='https://github.com/ZauteKm/vcVideoPlayer')
        ],
        [
            InlineKeyboardButton('👨🏼‍🦯 Help', callback_data='help'),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await message.reply(HOME_TEXT.format(message.from_user.first_name, message.from_user.id), reply_markup=reply_markup)



@Client.on_message(filters.command(["help", f"help@{Config.BOT_USERNAME}"]))
async def show_help(client, message):
    buttons = [
        [
            InlineKeyboardButton('📢 Channel', url='https://t.me/tgbotsproject'),
            InlineKeyboardButton('Source 🔥', url='https://github.com/ZauteKm/vcVideoPlayer'),
        ]
        ]
    reply_markup = InlineKeyboardMarkup(buttons)
    if Config.msg.get('help') is not None:
        await Config.msg['help'].delete()
    Config.msg['help'] = await message.reply_text(
        Config.HELP,
        reply_markup=reply_markup
        )
@Client.on_message(filters.command(['repo', f"repo@{Config.BOT_USERNAME}"]))
async def repo_(client, message):
    buttons = [
        [
            InlineKeyboardButton('🔥 Repository', url='https://github.com/ZauteKm/vcVideoPlayer'),
            InlineKeyboardButton('Channel 📢', url='https://t.me/ZauteKm'),
            
        ],
    ]
    await message.reply("<b>The source code of this bot is public and can be found at <a href=https://github.com/Zautekm/vcVideoPlayer>vcVideoPlayer.</a>\nYou can deploy your own bot and use in your group.\n\nFeel free to star☀️ the repo if you liked it 🙃.</b>", reply_markup=InlineKeyboardMarkup(buttons))

@Client.on_message(filters.command(['restart', 'update', f"restart@{Config.BOT_USERNAME}", f"update@{Config.BOT_USERNAME}"]) & admin_filter)
async def update_handler(client, message):
    await message.reply("Updating and restarting the bot.")
    await update()

@Client.on_message(filters.command(['logs', f"logs@{Config.BOT_USERNAME}"]) & admin_filter)
async def get_logs(client, message):
    logs=[]
    if os.path.exists("ffmpeg.txt"):
        logs.append(InputMediaDocument("ffmpeg.txt", caption="FFMPEG Logs"))
    if os.path.exists("ffmpeg.txt"):
        logs.append(InputMediaDocument("botlog.txt", caption="Bot Logs"))
    if logs:
        await message.reply_media_group(logs)
        logs.clear()
    else:
        await message.reply("No log files found.")
