import discord
from discord.enums import ButtonStyle
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType
import sqlite3
import asyncio
from discord.ui.view import View
import aiohttp


class Fun(commands.Cog):
    def __init__(self, client: discord.Client) -> None:
        self.client = client
        """try:
            self.conn = sqlite3.connect("database\settings.db")
        except Exception as e:
            print(e)"""

    @discord.app_commands.command()
    async def randomfacts(self, interaction: discord.Interaction):
        async with aiohttp.ClientSession() as session:
            async with session.get(
                "https://uselessfacts.jsph.pl/random.txt?language=en"
            ) as rqst:
                if rqst.status == 200:
                    rf = await rqst.text()
        fqcts = discord.Embed(title="A new fact has arrived", description=rf)
        await interaction.response.send_message(embed=fqcts)

    @discord.app_commands.command()
    async def joke(self, interaction):
        async with aiohttp.ClientSession() as session:
            async with session.get(
                "https://v2.jokeapi.dev/joke/Any?blacklistFlags=nsfw,religious,political,racist,sexist&format=txt&type=single"
            ) as rqst:
                if rqst.status == 200:
                    rf = await rqst.text()
        jke = discord.Embed(title="A new joke has arrived", description=rf)
        await interaction.response.send_message(embed=jke)

    @commands.group(aliases=["bin"], invoke_without_command=True)
    async def binary(self, ctx, binary: int):
        binary = bin(binary)
        binary = str(binary).removeprefix("0b")
        await ctx.send(f"Binary code is {binary}")

    @binary.command()
    async def integer(self, ctx, binary: int):
        # convert binary to integer
        binary = bin(binary)
        binary = str(binary).removeprefix("0b")
        binary = int(binary, 2)

        await ctx.send(f"integer code is {binary}")


async def setup(bot: discord.Client):
    await bot.add_cog(Fun(bot))
