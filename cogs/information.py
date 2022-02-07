
import discord
from discord.commands.commands import Option
from discord.enums import ButtonStyle
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType
import sqlite3
import asyncio
from discord.ui.view import View



class info(commands.Cog):
    def __init__(self, bot:discord.Bot) -> None:
        self.bot = bot
        try:
            self.conn = sqlite3.connect("database\data.db")
        except Exception as e:
            print(e)
    
    @commands.slash_command()
    async def ping(self, ctx, arg:Option(str, "Something", required= False)):
        await ctx.respond(f"{arg} {round(self.bot.latency*1000)}ms")
    #alpha
    @commands.command(aliases = ["welcome"])
    async def welcomemsg(self, ctx:commands.Context):
        WelcomeStarterMsg = discord.Embed(title="Set up your welcome message", description="Start by telling us if it is a embed or message",color = discord.Colour.red())
        msgbtn = discord.ui.Button(style=ButtonStyle.primary, label="Message", emoji="💬")
        embbtn = discord.ui.Button(style=ButtonStyle.primary, label="Embed", emoji="📦")
        view =View()
        view.add_item(msgbtn)
        view.add_item(embbtn)
        async def msgcallback(interaction:discord.Interaction):
            msgTips = discord.Embed(title="Set up your welcome message", description="Ok, You chose message. Enter your message")
            await interaction.response.send_message(embed=msgTips)
            
        msgbtn.callback = msgcallback
        WlcMsg=await ctx.send(embed=WelcomeStarterMsg, view=view)
        await asyncio.sleep(5)
        msgbtn.disabled=True
        embbtn.disabled=True
        await WlcMsg.edit(embed=WelcomeStarterMsg, view = view)

    
        
def setup(bot):
    bot.add_cog(info(bot))
        
        
