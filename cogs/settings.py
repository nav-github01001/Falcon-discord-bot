import discord

# from discord.commands.commands import Option
from discord.enums import ButtonStyle
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType
import asyncio
from discord.ui import View, Button


class Settings(commands.Cog):
    def __init__(self, client: discord.Client) -> None:
        self.client = client

    @commands.hybrid_command()
    @commands.has_permissions(administratior=True)
    async def setup(self, ctx):
        ...


    # alpha


async def setup(bot):
    await bot.add_cog(Settings(bot))
