from email.mime import base
import discord
from discord.commands.commands import Option
from discord.enums import ButtonStyle
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType
import sqlite3
import asyncio
from discord.ui.view import View
import aiohttp

class fun(commands.Cog):
    def __init__(self, bot:discord.Bot) -> None:
        self.bot = bot
        try:
            self.conn = sqlite3.connect("database\settings.db")
        except Exception as e:
            print(e)

    @commands.command(aliases=["ranfacts"])
    async def randomfacts(self,ctx):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://uselessfacts.jsph.pl/random.txt?language=en") as rqst:
                if rqst.status == 200:
                    rf = await rqst.text()
        fqcts = discord.Embed(title = "A new fact has arrived", description=rf)
        await ctx.send(embed=fqcts)
    
    @commands.command(aliases = ["lol"])
    async def joke(self,ctx):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://v2.jokeapi.dev/joke/Any?blacklistFlags=nsfw,religious,political,racist,sexist&format=txt&type=single") as rqst:
                if rqst.status == 200:
                    rf = await rqst.text()        
        jke = discord.Embed(title = "A new joke has arrived", description=rf)
        await ctx.send(embed=jke)

    @commands.group(aliases=["bin"], invoke_without_command= True)
    async def binary(self,ctx,binary:int):
        binary = bin(binary)
        binary = str(binary).removeprefix("0b")
        await ctx.send(f"Binary code is {binary}")

    @binary.command()
    async def integer(self,ctx,binary:int):
        #convert binary to integer
        binary = bin(binary)
        binary = str(binary).removeprefix("0b")
        binary = int(binary,2)
        
        await ctx.send(f"integer code is {binary}")

        pass
        
        




def setup(bot:discord.Bot):
    bot.add_cog(fun(bot))
        