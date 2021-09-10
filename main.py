from utils import start_stream
from user import group_call
from logger import LOGGER
from config import Config
from pyrogram import idle
from bot import bot
import asyncio
import os

if not os.path.isdir("./downloads"):
    os.makedirs("./downloads")
else:
    for f in os.listdir("./downloads"):
        os.remove(f"./downloads/{f}")

async def main():
    await bot.start()
    Config.BOT_USERNAME = (await bot.get_me()).username
    await group_call.start()
    await start_stream()
    LOGGER.warning(f"{Config.BOT_USERNAME} Started.")
    await idle()
    LOGGER.warning("Stoping")
    await group_call.start()
    await bot.stop()

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())


