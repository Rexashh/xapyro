# Copyright (C) 2022 Pyro-ManUserbot
#
# This file is a part of < https://github.com/mrismanaziz/PyroMan-Userbot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/mrismanaziz/PyroMan-Userbot/blob/main/LICENSE/>.
#
# t.me/SharingUserbot & t.me/Lunatic0de

import asyncio

from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from pyrogram.types import Message
from requests import get                                                                  
from config import PREFIX                                                     
from Xapyro import app, CMD_HELP

CMD_HELP.update(
    {
        "Broadcast": """
『 **Broadcast** 』
  `gcast` -> Mengirim ke seluruh group.
"""
    }
)

while 0 < 6:
    _GCAST_BLACKLIST = get(
        "https://raw.githubusercontent.com/mrismanaziz/Reforestation/master/blacklistgcast.json"                                                    )
    if _GCAST_BLACKLIST.status_code != 200:
        if 0 != 5:
            continue
        GCAST_BLACKLIST = [-1001473548283, -1001390552926]
        break
    GCAST_BLACKLIST = _GCAST_BLACKLIST.json()
    break

del _GCAST_BLACKLIST


@app.on_message(filters.command("gcast", PREFIX) & filters.me)
async def gcast_cmd(client: Client, message: Message):
    text = (
        message.text.split(None, 1)[1]
        if len(
            message.command,
        )
        != 1
        else None
    )
    if message.reply_to_message:
        text = message.reply_to_message.text or message.reply_to_message.caption
    if not text:
        return await edit_or_reply(message, "**Berikan Sebuah Pesan atau Reply**")
    Man = await edit_or_reply(message, "`Started global broadcast...`")
    done = 0
    error = 0
    async for dialog in client.iter_dialogs():
        if dialog.chat.type in ("group", "supergroup"):
            chat = dialog.chat.id
            if chat not in GCAST_BLACKLIST:
                try:
                    await client.send_message(chat, text)
                    await asyncio.sleep(0.1)
                    done += 1
                except FloodWait as e:
                    await asyncio.sleep(e.value)
                    await client.send_message(chat, text)
                    done += 1
                except Exception:
                    error += 1
    await Man.edit_text(
        f"**Berhasil Mengirim Pesan Ke** `{done}` **Grup, Gagal Mengirim Pesan Ke** `{error}` **Grup**"
    )
