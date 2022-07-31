from typing import Optional
import datetime
from .utils import colorsigns, misc
import discord
from discord.ext import commands



class FalconDevelOnly(commands.Cog):
    def __init__(self, client:commands.Bot) -> None:
        self.client = client
    @commands.Cog.listener()
    async def on_member_join(self, member:discord.Member):
        if not member.guild.id == 897312479191912489:
            return
        
        await member.add_roles(member.guild.get_role(1003173466297610300))
    
    

async def setup(client:commands.Bot):
    await client.add_cog(FalconDevelOnly(client))