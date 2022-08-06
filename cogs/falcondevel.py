from enum import Enum
from typing import Literal, Optional
import datetime
from .utils import colorsigns, misc
import discord
from discord.ext import commands


class LangRoles(Enum):
    ...


class FalconDevelOnly(commands.Cog):
    def __init__(self, client: commands.Bot) -> None:
        self.client = client

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        if not member.guild.id == misc.FALCON_DEVEL_GUILD_ID:
            return
        
        if not member.bot:
            await member.add_roles(member.guild.get_role(1003173466297610300))
        else:
            await member.add_roles(member.guild.get_role(1003211005356163123))

    @commands.hybrid_command()
    async def discord(self,ctx,platform):...

async def setup(client: commands.Bot):
    await client.add_cog(FalconDevelOnly(client),guild=897312479191912489)
