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

    @commands.command()
    @commands.check(commands.is_owner())
    async def presence(self, interaction, presence: str, name: str, twitch_url=None):
        if presence.lower() == "game":
            await self.bot.change_presence(activity=discord.Game(name=name))
        elif presence.lower() == "stream" and twitch_url is not None:
            # Setting `Streaming ` status
            await self.bot.change_presence(
                activity=discord.Streaming(name=name, url=twitch_url)
            )
        elif presence.lower() == "listen":
            # Setting `Listening ` status
            await self.bot.change_presence(
                activity=discord.Activity(
                    type=discord.ActivityType.listening, name=name
                )
            )
        elif presence.lower() == "watch":
            #   Setting `Watching ` status
            await self.bot.change_presence(
                activity=discord.Activity(type=discord.ActivityType.watching, name=name)
            )


async def setup(bot):
    await bot.add_cog(OwnersOnly(bot))
