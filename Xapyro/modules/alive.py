
from config import PREFIX
from config import ALIVE_EMOJI, ALIVE_LOGO, ALIVE_TEKS_CUSTOM, BOT_VER, CHANNEL, GROUP
from Xapyro.helpers.basic import edit_or_reply
import asyncio
import time
from datetime import datetime
from pyrogram import filters
from Xapyro import app, StartTime, CMD_HELP
from sys import version_info

from pyrogram import __version__ as __pyro_version__
from pyrogram.types import Message

CMD_HELP.update(
    {
        "Alive": """
『 **Alive** 』
  `alive` -> Show off to people with your bot using this command.
  `ping` -> Shows you the response speed of the bot.
"""
    }
)

modules = PREFIX
emoji = ALIVE_EMOJI
alive_text = ALIVE_TEKS_CUSTOM

@Client.on_message(filters.command(["alive", "awake"], cmd) & filters.me)
async def alive(client: Client, message: Message):
    xx = await edit_or_reply(message, "⚡")
    await asyncio.sleep(2)
    apa = client.send_video if ALIVE_LOGO.endswith(".mp4") else client.send_photo
    uptime = await get_readable_time((time.time() - StartTime))
    capt = (
        f"**[xapyro-userbot](https:/t.me/rexaprivateroom) is Up and Running.**\n\n"
        f"<b>{alive_text}</b>\n\n"
        f"{emoji} <b>Master :</b> {client.me.mention} \n"
        f"{emoji} <b>Modules :</b> <code>{len(modules)} Modules</code> \n"
        f"{emoji} <b>Bot Version :</b> <code>{BOT_VER}</code> \n"
        f"{emoji} <b>Python Version :</b> <code>{python_version()}</code> \n"
        f"{emoji} <b>Pyrogram Version :</b> <code>{versipyro}</code> \n"
        f"{emoji} <b>Bot Uptime :</b> <code>{uptime}</code> \n\n"
        f"    **[𝗦𝘂𝗽𝗽𝗼𝗿𝘁](https://t.me/{GROUP})** | **[𝗖𝗵𝗮𝗻𝗻𝗲𝗹](https://t.me/{CHANNEL})** | **[𝗢𝘄𝗻𝗲𝗿](tg://user?id={client.me.id})**"
    )
    photo = ALIVE_LOGO
    await m.delete()
    if m.reply_to_message:
        await app.send_photo(
            m.chat.id,
            photo= ALIVE_LOGO,
            caption=reply_msg,
            reply_to_message_id=m.reply_to_message.message_id,
        )
    else:
        await app.send_photo(m.chat.id, photo, caption=reply_msg)
