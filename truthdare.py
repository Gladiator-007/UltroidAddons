# Ultroid - UserBot
# Copyright (C) 2020 Gladiator-007
#
# This file is a part of < https://github.com/Gladiator-007/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/Gladiator-007/Ultroid/blob/main/LICENSE/>.

"""
✘ Commands Available -

• `{i}truth`
   `Get Truth Task.`

• `{i}dare`
   `Get Dare Task.`
"""

import requests as r
from bs4 import BeautifulSoup as bs

from . import *

link = "https://fungenerators.com/random/truth-or-dare?option="


@ultroid_cmd(pattern="truth$")
async def gtruth(ult):
    m = await eor(ult, "`Generating a Truth Statement.. `")
    nl = link + "truth"
    ct = r.get(nl).content
    bsc = bs(ct, "html.parser", from_encoding="utf-8")
    cm = bsc.find_all("h2")[0].text
    await m.edit(f"**#TruthTask**\n\n`{cm}`")


@ultroid_cmd(pattern="dare$")
async def gtruth(ult):
    m = await eor(ult, "`Generating a Dare Task.. `")
    nl = link + "dare"
    ct = r.get(nl).content
    bsc = bs(ct, "html.parser", from_encoding="utf-8")
    cm = bsc.find_all("h2")[0].text
    await m.edit(f"**#DareTask**\n\n`{cm}`")
