from pyrogram.errors import BotInlineDisabled
from pyrogram import Client, filters
from logger import LOGGER
from config import Config

async def is_reply(_, client, message):
    if Config.REPLY_MESSAGE:
        return True
    else:
        return False
reply_filter=filters.create(is_reply)

@Client.on_message(reply_filter & filters.private & ~filters.bot & filters.incoming & ~filters.service & ~filters.me & ~filters.chat([777000, 454000]))
async def reply(client, message): 
    try:
        inline = await client.get_inline_bot_results(Config.BOT_USERNAME, "ETHO_ORUTHAN_PM_VANNU")
        m=await client.send_inline_bot_result(
            message.chat.id,
            query_id=inline.query_id,
            result_id=inline.results[0].id,
            hide_via=True
            )
        old=Config.msg.get(message.chat.id)
        if old:
            await client.delete_messages(message.chat.id, [old["msg"], old["s"]])
        Config.msg[message.chat.id]={"msg":m.updates[1].message.id, "s":message.message_id}
    except BotInlineDisabled:
        LOGGER.error(f"Error: Inline Mode for @{Config.BOT_USERNAME} is not enabled. Enable from @Botfather to enable PM Permit.")
        await message.reply(f"{Config.REPLY_MESSAGE}\n\n<b>You can't use this bot in your group, for that you have to make your own bot from the [SOURCE CODE](https://github.com/ZauteKm/vcVideoPlayer) below.</b>", disable_web_page_preview=True)
    except Exception as e:
        LOGGER.error(e)
        pass
