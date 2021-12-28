import sqlite3
import discord
import datetime
from random import randint
from discord.ext import commands


class GlobalChat(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        try:
            self.conn = sqlite3.connect("Discord\database\settings.db")
        except Exception as e:
            print(e)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def globalchatstart(self, ctx, channel):
        guild_id = ctx.message.guild.id
        channel_id = int(channel.strip('<>#'))
        c = self.conn.cursor()
        c.execute('''INSERT OR IGNORE INTO globalchat(SERVERID, CHANID)VALUES(?,?)''',(guild_id, channel_id))
        self.conn.commit()
        await ctx.send(':white_check_mark: **Channel has been added to global chat!**')

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def globalchatstop(self, ctx):
        guild_id = ctx.message.guild.id
       
        c = self.conn.cursor()
        c.execute('''DELETE FROM rickstatus WHERE SERVERID=?''',(guild_id,))
        self.conn.commit()

        await ctx.send(':white_check_mark: **Channel has been removed from global chat!**')

    @commands.Cog.listener()
    async def on_message(self, message):
        if not message.author.bot:
            if not message.content.startswith('!'):
                c = self.conn.cursor()
                c.execute('''SELECT CHANID FROM globalchat''')
                l = c.fetchall()
                print(l)
                th = list(l[0])
                print(th)
'''                    for ids in :
                        if message.channel.id in th:
                            if not message.content:
                                return
                        
                            if message.channel.id != ids:
                                try:
                                    User = message.author
                                    message_embed = discord.Embed(colour=randint(0, 0xffffff))

                                    message_embed.timestamp = datetime.datetime.utcnow()
                                    message_embed.set_author(icon_url=User.display_avatar.url, name=f'{message.author}')
                                    message_embed.description = f'**Said:** {message.content}'
                                    message_embed.set_footer(text=message.guild.name)
                                    await self.bot.get_channel(ids).send(embed=message_embed)
                                except Exception as e:
                                    print(e)
'''                             



def setup(bot):
    bot.add_cog(GlobalChat(bot))