import discord
import re
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType
import sqlite3
import asyncio

class OwnersOnly(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot
        try:
            self.conn = sqlite3.connect("Discord\database\settings.db")
        except Exception as e:
            print(e)

    @commands.command()
    @commands.check(commands.is_owner())
    async def unload(self, ctx, ext):
        try:
            self.bot.unload_extension("cogs."+ext)
            print("Unloaded")
        except Exception as e:
            print(f"Fault: {e}")

    @commands.command()
    @commands.check(commands.is_owner())
    async def load(self, ctx, ext):
        try:
            self.bot.load_extension("cogs."+ext)
            print("loaded")
        except Exception as e:
            print(f"Fault: {e}")

    @commands.command()
    @commands.check(commands.is_owner())
    async def reload(self, ctx, ext):
        try:
            self.bot.unload_extension("cogs."+ext)
            self.bot.load_extension("cogs."+ext)
            await asyncio.sleep(0.5)
            print("REloaded")
        except Exception as e:
            print(f"Fault: {e}")
    
        













def setup(bot):
    bot.add_cog(OwnersOnly(bot))