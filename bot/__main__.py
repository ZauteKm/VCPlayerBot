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

import os
import sys
import asyncio
import subprocess
from signal import SIGINT
from asyncio import sleep
from pyrogram import Client, filters, idle
from threading import Thread
from config import Config, db
from pyrogram.types import Message
from bot.plugins.nopm import User
from bot.plugins.extras import USERNAME

ADMINS = Config.ADMINS
CHAT_ID = Config.CHAT_ID
FFMPEG_PROCESSES = db.FFMPEG_PROCESSES

Bot = Client(
    ":memory:",
    Config.API_ID,
    Config.API_HASH,
    bot_token=Config.BOT_TOKEN,
    plugins=dict(root="bot.plugins"),
)
if not os.path.isdir("./downloads"):
    os.makedirs("./downloads")

def stop_and_restart():
    Bot.stop()
    os.system("git pull")
    sleep(10)
    os.execl(sys.executable, sys.executable, *sys.argv)


@Bot.on_message(filters.command(["restart", f"restart@{USERNAME}"]) & filters.user(ADMINS) & (filters.chat(CHAT_ID) | filters.private))
def restart(client, m: Message):
    k = m.reply_text("🔄 `Restarting ...`")
    sleep(3)
    process = FFMPEG_PROCESSES.get(CHAT_ID)
    if process:
        try:
            process.send_signal(SIGINT)
        except subprocess.TimeoutExpired:
            process.kill()
        except Exception as e:
            print(e)
            pass
        FFMPEG_PROCESSES[CHAT_ID] = ""
    Thread(
        target=stop_and_restart
        ).start()
    try:
        k.edit("✅ **Restarted Successfully! \nJoin @tgbotsproject For More!**")
    except:
        pass

Bot.start()
User.start()
print("\nVideo Player Bot Started, Join @tgbotsproject!")

idle()
Bot.stop()
User.stop()
print("\nVideo Player Bot Stopped, Join @tgbotsproject!")
