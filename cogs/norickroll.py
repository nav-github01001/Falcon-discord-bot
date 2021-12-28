import discord
import re
from discord.ext import commands

from discord.ext.commands.cooldowns import BucketType
import sqlite3
from byeastley import RickRollDetector

class NopeRickRoll(commands.Cog):
    
    def __init__(self, bot) -> None:
        self.bot = bot
        try:
            self.conn = sqlite3.connect("Discord\database\settings.db")
        except Exception as e:
            print(e)

    

    @commands.Cog.listener()
    async def on_message(self,message:discord.Message):
        c = self.conn.cursor()
        c.execute('''SELECT * FROM rickstatus WHERE SERVERID=?''', (message.guild.id,))
        a = c.fetchall()
        status = a[0][1]

        for i in message.content.split(" "):
            i = i.replace("<","").replace(">", "") #Removes <> that could be used to hide embeds
            
            if "https://" in i and await RickRollDetector().find(i):
                status = str(status)
                if status.lower() == "True".lower(): 
                    RickEM=discord.Embed(title="That is a Rickroll Link",description="Dont Click on that.", color= discord.Color.red(), url="https://github.com/CodeWithSwastik/rickroll-detector")
                    RickEM.set_footer(text="Made with open source")
                    await message.reply(embed = RickEM)
                break

    @commands.command(aliases = ["norickroll"])
    async def rickrollmode(self, ctx, alVal:str):

        if alVal == "True":
            c = self.conn.cursor()
            c.execute('''UPDATE rickstatus SET confirm=? WHERE SERVERID=?''', (alVal, ctx.guild.id))
            self.conn.commit()
            rickEM=discord.Embed(title="I have succesfully enabled the Rickroll Feature 🤣", description="Now we will alert u whenever someone sends you a link ✅")
            await ctx.send(embed=rickEM)
        elif alVal == "False":
            c = self.conn.cursor()
            c.execute('''UPDATE rickstatus SET confirm=? WHERE SERVERID=?''', (alVal, ctx.guild.id))
            self.conn.commit()
            rickEM=discord.Embed(title="I have succesfully disabled the Rickroll Feature 🤣", description="So sad ur rickrolling yourself(i meant risking)")
            await ctx.send(embed=rickEM)
        else:
            await ctx.send("Invalid args")           




def setup(bot):
    bot.add_cog(NopeRickRoll(bot))