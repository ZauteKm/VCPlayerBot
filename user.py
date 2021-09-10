from pytgcalls import PyTgCalls
from pyrogram import Client
from config import Config
from logger import LOGGER

USER = Client(
    Config.SESSION,
    Config.API_ID,
    Config.API_HASH,
    plugins=dict(root="userplugins")
    )
group_call = PyTgCalls(USER, cache_duration=180)


