import discord
import re
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType
import sqlite3
import asyncio


class OwnersOnly(commands.Cog):
    def __init__(self, client) -> None:
        self.client = client
        
    @commands.command()
    @commands.is_owner()
    async def unload(self, interaction, ext):
        try:
            await self.client.unload_extension("cogs." + ext)
            print("Unloaded")
        except Exception as e:
            print(f"Fault: {e}")

    @commands.command()
    @commands.is_owner()
    async def load(self, ctx, ext):
        try:
            await self.client.load_extension("cogs." + ext)
            print("loaded")
        except Exception as e:
            print(f"Fault: {e}")

    @commands.command()
    @commands.is_owner()
    async def reload(self, interaction, ext):
        try:
            await self.client.unload_extension("cogs." + ext)
            await self.client.load_extension("cogs." + ext)
            await asyncio.sleep(0.5)
            print("REloaded")
        except Exception as e:
            print(f"Fault: {e}")


async def setup(bot):
    await bot.add_cog(OwnersOnly(bot))
