import discord
from discord.enums import ButtonStyle
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType
import sqlite3
import asyncio
from discord.ui.view import View
import aiohttp
import random
from .utils import request_helper

class Fun(commands.Cog):
    def __init__(self, client: discord.Client) -> None:
        self.client = client

    @discord.app_commands.command(description="Get a random joke from people with good humour")
    async def joke(self, interaction:discord.Interaction):
        joke = await request_helper.get("https://v2.jokeapi.dev/joke/Any")
        if joke["type"] == "twopart":
            await interaction.response.send_message(embed=discord.Embed(title=joke["setup"],description=f"{joke['delivery']}"))
        else:
            await interaction.response.send_message(content=f"{joke['joke']}")        

    @discord.app_commands.command(description="Get a random meme from reddit")
    async def meme(self, interaction:discord.Interaction):
        meme = await request_helper.get("https://meme-api.com/gimme")
        
        if meme["nsfw"] == True:
        # Get another non-nsfw meme
            meme = request_helper.get("https://meme-api.com/gimme") 

        await interaction.response.send_message(embed=discord.Embed(title=meme["title"]).set_image(url=meme["preview"][-1]))

    @discord.app_commands.command(description="Search a term in the Urban Dictionary (srsly wtf)")
    async def urbandictionary(self,interaction:discord.Interaction,term:str):
        resp = await request_helper.get(f"https://unofficialurbandictionaryapi.com/api/search?term={term}&strict=false&matchCase=false&limit=5&page=1&multiPage=false")
        definitions = discord.Embed(title=f"Search Results for \'{term}\'")
        for definition in resp["data"]:
            definitions.add_field(name=f"\n{definition['meaning']}",value=definition["example"],inline=False)
        await interaction.response.send_message(embed=definitions)


    @commands.hybrid_group(invoke_without_command=True,description="Convert a number into binary")
    async def binary(self, ctx, binary: int):
        binary = bin(binary)
        binary = str(binary).removeprefix("0b")
        await ctx.send(f"Binary code is {binary}")

    @binary.command(description = "Convert binary back into integer")
    async def integer(self, ctx, binary: int):
        # convert binary to integer
        binary = bin(binary)
        binary = str(binary).removeprefix("0b")
        binary = int(binary, 2)

        await ctx.send(f"integer code is {binary}")


async def setup(bot: discord.Client):
    await bot.add_cog(Fun(bot))
