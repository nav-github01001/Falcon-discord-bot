
import discord

# from discord.commands.commands import Option
from discord.enums import ButtonStyle
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType
import sqlite3
import asyncio
from discord.ui import View,Button


class Info(commands.Cog):
    def __init__(self, client: discord.Client) -> None:
        self.client = client
        try:
            self.conn = sqlite3.connect("./databases/data.db")
        except Exception as e:
            print(e)

    @discord.app_commands.command(description="Measure the latency of the bot")
    async def ping(self, interaction:discord.Interaction):
        await interaction.response.send_message(
            f"Latency since last heartbeat:{round(self.client.latency*1000)}ms",
            ephemeral=True,
        )
    
    @commands.hybrid_command()
    async def invite(self, ctx:commands.Context):
        
        AdminLink = Button(style=ButtonStyle.link, label="For administrators", url="https://discord.com/api/oauth2/authorize?client_id=923915598247915540&permissions=8&scope=bot%20applications.commands")
        NonAdminLink = Button(style=ButtonStyle.link, label="Recommended", url="https://discord.com/api/oauth2/authorize?client_id=923915598247915540&permissions=1110216543415&scope=bot%20applications.commands")
        view = View().add_item(AdminLink).add_item(NonAdminLink)
        await ctx.send(embed =discord.Embed(title="Invite Me!", description="", colour=discord.Colour(0xFFFFFF)),view=view)  # type: ignore
    # alpha


async def setup(bot):
    await bot.add_cog(Info(bot))
