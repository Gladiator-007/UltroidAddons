# Ultroid - UserBot
# Copyright (C) 2020 Gladiator-007
#
# This file is a part of < https://github.com/Gladiator-007/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/Gladiator-007/Ultroid/blob/main/LICENSE/>.

"""
✘ Commands Available -

•`{i}sspam <reply to sticker>`
   it spam the whole stickers in that pack.

"""

from telethon.tl.functions.messages import GetStickerSetRequest
from telethon.tl.types import InputStickerSetID, InputStickerSetShortName
from telethon.utils import get_input_document

from . import *


@ultroid_cmd(pattern="sspam$")
async def _(e):
    x = await e.get_reply_message()
    if not (x and x.media and hasattr(x.media, "document")):
        return await eod(e, "`Reply To Sticker Only`")
    set = x.document.attributes[1]
    sset = await e.client(
        GetStickerSetRequest(
            InputStickerSetID(
                id=set.stickerset.id,
                access_hash=set.stickerset.access_hash,
            )
        )
    )
    pack = sset.set.short_name
    docs = [
        get_input_document(x)
        for x in (
            await e.client(GetStickerSetRequest(InputStickerSetShortName(pack)))
        ).documents
    ]
    for xx in docs:
        await e.respond(file=(xx))
