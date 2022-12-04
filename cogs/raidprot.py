
import discord
# from discord.commands.commands import Option
from discord.enums import ButtonStyle
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType
import sqlite3
import asyncio
from discord.ui import View,Button


class Raid(commands.Cog):
    def __init__(self, client: discord.Client) -> None:
        self.client = client
        try:
            self.conn = sqlite3.connect("./databases/settings.db")
        except Exception as e:
            print(e)

    @commands.group()
    async def raid(self,ctx):
        embed=discord.Embed(title="Settings for Raid Protection", description="**Note**:Only for administrators\n\n")
        embed.add_field(name="> **detectmassjoins [joins/min]**: ", value="Toggle Whether to detect a lot of people trying to join at once\nIf so, the rate of joining also need to be provided")
        embed.add_field(name="> **massjoinpunishment <timeout/kick/ban> [timeout]")
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Raid(bot))
