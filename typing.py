# (c) Shrimadhav U.K
# aka Spechide
#
# Ported for Ultroid - UserBot
#
# This file is a part of < https://github.com/Gladiator-007/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/Gladiator-007/Ultroid/blob/main/LICENSE/>.

"""
✘ Commands Available -

• `{i}type <msg>`
    Edits the Message and shows like someone is typing.
"""

import asyncio

from . import *


@ultroid_cmd(pattern="type ?(.*)", fullsudo=True)
async def _(event):
    input_str = event.pattern_match.group(1)
    if not input_str:
        return await eor(event, "Give me something to type !")
    shiiinabot = "\u2060" * 602
    okla = await eor(event, shiiinabot)
    typing_symbol = "|"
    previous_text = ""
    await okla.edit(typing_symbol)
    await asyncio.sleep(0.4)
    for character in input_str:
        previous_text = previous_text + "" + character
        typing_text = previous_text + "" + typing_symbol
        await okla.edit(typing_text)
        await asyncio.sleep(0.4)
        await okla.edit(previous_text)
        await asyncio.sleep(0.4)
