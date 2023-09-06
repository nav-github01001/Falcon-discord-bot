import discord

# from discord.commands.commands import Option
from discord.enums import ButtonStyle
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType
import asyncio
from discord.ui import View, Button


class Levelling(commands.Cog):
    def __init__(self, client: discord.Client) -> None:
        self.client = client

    @commands.Cog.listener()
    async def on_message(self,message):
        ... 

    @commands.hybrid_group()
    async def level(self,ctx):
        ...

    
    # alpha


async def setup(bot):
    await bot.add_cog(Levelling(bot))
