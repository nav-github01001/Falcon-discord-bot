import discord
import re
from discord.ext import commands
from discord.ui import Button, View
from discord.ext.commands.cooldowns import BucketType
import sqlite3
import asyncio
from byeastley import RickRollDetector

class NopeRickRoll(commands.Cog):
    
    def __init__(self, bot) -> None:
        self.bot = bot
        try:
            self.conn = sqlite3.connect("database\settings.db")
        except Exception as e:
            print(e)

    

    @commands.Cog.listener()
    async def on_message(self,message:discord.Message):
        c = self.conn.cursor()
        c.execute('''SELECT * FROM rickstatus WHERE SERVERID=?''', (message.guild.id,))
        a = c.fetchall()
        status = a[0][1]
        btn = Button(label="Report False Positive", style=discord.ButtonStyle.danger, emoji="🚩")
        view = View()
        view.add_item(btn)

        for i in message.content.split(" "):
            i = i.replace("<","").replace(">", "") #Removes <> that could be used to hide embeds
            
            if "https://" in i and await RickRollDetector().find(i):
                status = str(status)
                
                if status.lower() == "True".lower():
                    async def bcallback(interaction):
                        print(f"This link was not a rickroll link : {i}")
                        await interaction.response.send_message("Ok Reported!")
                        

                    btn.callback = bcallback 
                    RickEM=discord.Embed(title="That is a Rickroll Link",description="Dont Click on that.", color= discord.Color.red(), url="https://github.com/CodeWithSwastik/rickroll-detector")
                    RickEM.set_footer(text="Made with open source")
                    rickMSG =await message.reply(embed = RickEM, view = view)
                    await asyncio.sleep(5)
                    btn.disabled = True
                    await rickMSG.edit(embed = RickEM, view=view)
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