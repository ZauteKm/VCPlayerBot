from utils import get_admins, get_buttons, get_playlist_str, pause, restart, resume, shuffle_playlist, skip
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from pyrogram.errors import MessageNotModified
from pyrogram import Client
from config import Config
from asyncio import sleep
from logger import LOGGER

@Client.on_callback_query()
async def cb_handler(client: Client, query: CallbackQuery):
    admins = await get_admins(Config.CHAT)
    if query.from_user.id not in admins and query.data != "help":
        await query.answer(
            "😒 Played Joji.mp3",
            show_alert=True
            )
        return
    if query.data == "shuffle":
        if not Config.playlist:
            await query.answer("Playlist is empty.", show_alert=True)
            return
        await shuffle_playlist()
        await sleep(1)
        pl=await get_playlist_str()
        
        try:
            await query.message.edit(
                    f"{pl}",
                    parse_mode="Markdown",
                    reply_markup=await get_buttons()
            )
        except MessageNotModified:
            pass

    elif query.data.lower() == "pause":
        if Config.PAUSE:
            await query.answer("Already Paused", show_alert=True)
        else:
            await pause()
            await sleep(1)
        pl=await get_playlist_str()
        try:
            await query.message.edit(f"{pl}",
                disable_web_page_preview=True,
                reply_markup=await get_buttons()
            )
        except MessageNotModified:
            pass
    
    elif query.data.lower() == "resume":   
        if not Config.PAUSE:
            await query.answer("Nothing Paused to resume", show_alert=True)
        else:
            await resume()
            await sleep(1)
        pl=await get_playlist_str()
        try:
            await query.message.edit(f"{pl}",
                disable_web_page_preview=True,
                reply_markup=await get_buttons()
            )
        except MessageNotModified:
            pass

    elif query.data=="skip":   
        if not Config.playlist:
            await query.answer("No songs in playlist", show_alert=True)
        else:
            await skip()
            await sleep(1)
        pl=await get_playlist_str()
        try:
            await query.message.edit(f"{pl}",
                disable_web_page_preview=True,
                reply_markup=await get_buttons()
            )
        except MessageNotModified:
            pass
    elif query.data=="replay":
        if not Config.playlist:
            await query.answer("No songs in playlist", show_alert=True)
        else:
            await restart()
            await sleep(1)
        pl=await get_playlist_str()
        try:
            await query.message.edit(f"{pl}",
                disable_web_page_preview=True,
                reply_markup=await get_buttons()
            )
        except MessageNotModified:
            pass

    elif query.data=="help":
        buttons = [
            [
                InlineKeyboardButton('📢 Channel', url='https://t.me/tgbotsproject'),
                InlineKeyboardButton('Source 🔥', url='https://github.com/ZauteKm/vcVideoPlayer'),
            ]
        ]
        reply_markup = InlineKeyboardMarkup(buttons)

        try:
            await query.message.edit(
                Config.HELP,
                reply_markup=reply_markup

            )
        except MessageNotModified:
            pass
    await query.answer()

