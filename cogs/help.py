import discord
from discord.ext import commands


class Helpme(commands.Cog):
    def __init__(self, bot:discord.Bot) -> None:
        self.bot = bot
    
    @commands.group()
    async def help(self,ctx):
        helpEM = discord.Embed(title=f"Help command for THE SMART BOT hehe!",color=discord.Color.og_blurple())
        helpEM.add_field(name="💼 Moderation")


