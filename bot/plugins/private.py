"""
vcVideoPlayer, Telegram Video Chat Bot
Copyright (c) 2021  Zaute Km

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>
"""

import asyncio
from config import Config
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pyrogram.errors import MessageNotModified

CHAT_ID = Config.CHAT_ID
USERNAME = Config.BOT_USERNAME
HOME_TEXT = "**Hi [{}](tg://user?id={})**, \n\nI'm **Telegram VC Video Player Bot**. \nI Can Stream Videos On Telegram Voice Chat From YouTube & Telegram Video Files!"
HELP_TEXT = """
🏷️ **Setting Up:**

\u2022 Start a voice chat in your channel or group.
\u2022 Add bot and user account in chat with admin rights.
\u2022 Use /stream [youtube link] or /stream as a reply to an video file.

🏷️ **Common Commands:**

\u2022 `/start` - Start the bot.
\u2022 `/help` - Show the help message.

🏷️ **Admin Only Commands:**

\u2022 `/stream` - Start streaming the Video.
\u2022 `/radio` - Start streaming the Radio.
\u2022 `/stopradio` - Stop streaming the Radio.
\u2022 `/endstream` - Stop streaming the Video.
"""


@Client.on_callback_query()
async def cb_handler(client: Client, query: CallbackQuery):
    if query.data=="help":
        buttons = [
            [
                InlineKeyboardButton("🗣️ Feedback", url="https://t.me/zautebot"),
                InlineKeyboardButton("Channel 📢", url="https://t.me/tgbotsproject"),
            ],
            [
                InlineKeyboardButton("🔰 Source Code 🔰", url="https://github.com/ZauteKm/vcVideoPlayer"),
            ],
            [
                InlineKeyboardButton("🏘️ Home", callback_data="home"),
                InlineKeyboardButton("Close ❌", callback_data="close"),
            ]
            ]
        reply_markup = InlineKeyboardMarkup(buttons)
        try:
            await query.edit_message_text(
                HELP_TEXT,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass

    elif query.data=="home":
        buttons = [
            [
                InlineKeyboardButton("🗣️ Feedback", url="https://t.me/zautebot"),
                InlineKeyboardButton("Channel 📢", url="https://t.me/tgbotsproject"),
            ],
            [
                InlineKeyboardButton("🔰 Source Code 🔰", url="https://github.com/ZauteKm/vcVideoPlayer"),
            ],
            [
                InlineKeyboardButton("⛑️ Help", callback_data="help"),
                InlineKeyboardButton("Close ❌", callback_data="close"),
            ]
            ]
        reply_markup = InlineKeyboardMarkup(buttons)
        try:
            await query.edit_message_text(
                HOME_TEXT.format(query.from_user.first_name, query.from_user.id),
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass

    elif query.data=="close":
        try:
            await query.message.delete()
            await query.message.reply_to_message.delete()
        except:
            pass


@Client.on_message(filters.command(["start", f"start@{USERNAME}"]) & (filters.chat(CHAT_ID) | filters.private))
async def start(client, message):
    buttons = [
            [
                InlineKeyboardButton("🗣️ Feedback", url="https://t.me/zautebot"),
                InlineKeyboardButton("Channel 📢", url="https://t.me/tgbotsproject"),
            ],
            [
                InlineKeyboardButton("🔰 Source Code 🔰", url="https://github.com/ZauteKm/vcVideoPlayer"),
            ],
            [
                InlineKeyboardButton("⛑️ Help", callback_data="help"),
                InlineKeyboardButton("Close ❌", callback_data="close"),
            ]
            ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await message.reply_text(text=HOME_TEXT.format(message.from_user.first_name, message.from_user.id), reply_markup=reply_markup)

@Client.on_message(filters.command(["help", f"help@{USERNAME}"]) & (filters.chat(CHAT_ID) | filters.private))
async def help(client, message):
    buttons = [
            [
                InlineKeyboardButton("🗣️ Feedback", url="https://t.me/zautebot"),
                InlineKeyboardButton("Channel 📢", url="https://t.me/tgbotsproject"),
            ],
            [
                InlineKeyboardButton("🔰 Source Code 🔰", url="https://github.com/ZauteKm/vcVideoPlayer"),
            ],
            [
                InlineKeyboardButton("🏘️ Home", callback_data="home"),
                InlineKeyboardButton("Close ❌", callback_data="close"),
            ]
            ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await message.reply_text(text=HELP_TEXT, reply_markup=reply_markup)
