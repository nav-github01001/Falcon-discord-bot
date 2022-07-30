import asyncio
import json
import logging
import typing
import discord
from discord.ext import commands

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='./EnderBot.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

COGS_LIST = ("cogs.owner","cogs.fun", "cogs.information", )
EXTENSION_LIST = ("jishaku",)
with open("config.json") as f:
    _json = json.load(f)


class FalconClient(commands.Bot):
    def __init__(self, *, intents: discord.Intents) -> None:
        super().__init__(intents=intents, command_prefix=commands.when_mentioned_or("!?"))

    async def on_command_error(self, context, exception) -> None:
        error = discord.Embed(color=0xff0000, title="Error!", description=exception).set_footer(text="If this occurs more often, contact support")
        await context.send(embed=error)

intents = discord.Intents.all()
client = FalconClient(intents=intents)

for cog in COGS_LIST:
    asyncio.run(client.load_extension(cog))

for ext in EXTENSION_LIST:
    asyncio.run(client.load_extension(ext))

client.run(_json["token"], log_handler=None)
