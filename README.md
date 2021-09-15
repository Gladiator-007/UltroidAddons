# <p align="center"><a href="https://github.com/Teamultroid/UltroidAddons"><img src="https://github-readme-stats.vercel.app/api/pin?username=Gladiator-007&show_icons=true&theme=dracula&hide_border=true&repo=UltroidAddons"></a></p>
<p align="center">

# UltroidAddons
Plugins repository for [@TheUltroid](https://github.com/Gladiator-007/Ultroid).


# Contributing
If you want to contribute to this repository (adding your plugins/porting from other bots), use the format given below and create a pull request.   
⚠️ First check whether the stuff you push works. Also, if the pull request doesn't follow the below format, it will be closed without prior notice.

```python
# Credits @username (creator of plugin and who ported)   
   
# Ported from (if ported else skip)   
   
# Ported for Ultroid < https://github.com/Gladiator-007/Ultroid >   
```
   
Kindly do not **steal** others works without credits.<br>

# Example Plugin
   Required Import are Automatically Done.

<kbd>This Example Works Everywhere. (e.g. Groups, Personal Chats ...)</kbd>
```python
@ultroid_cmd(pattern="hoi")
async def hello_world_example(event):
    # As telethon is an asyncio based lib, you will have to use `async`/`await` Syntax.
    await event.reply("Hello **World**.")
```

<kbd>This Example Works Only In Groups.</kbd>
```python
@ultroid_cmd(pattern="hoi", groups_only=True,)
async def hello_world_example(event):
    await event.reply("Hello **World**.")
```

If Your plugin need any additional requirements, it can be added to <a href="https://github.com/Gladiator-007/UltroidAddons/blob/main/addons.txt">addons.txt</a><br><br>

<br>

> For More Information See [The Pypi Page](https://pypi.org/project/py-Ultroid).

> Made with 💕 by [@Gladiator-007](https://t.me/Gladiator-007).
