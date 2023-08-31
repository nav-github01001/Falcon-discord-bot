from typing import Optional
import datetime
import sqlite3
from discord import Embed
from .utils import colorsigns, misc
import discord
from discord import app_commands
from discord.ext import commands


class Moderation(commands.Cog):
    def __init__(self, client: commands.Bot) -> None:
        self.client = client
        try:
            self.conn = sqlite3.connect("./databases/settings.db")
        except Exception as e:
            print(e)

    @commands.command()
    @commands.has_permissions(manage_messages = True)
    async def purge(self, ctx: commands.Context, limit: Optional[int] = 50, reason:Optional[str]=None):
        await ctx.channel.purge(limit=limit + 1,reason=reason)
        await ctx.send(f"♻️ Successfully Purged {limit} message(s)", delete_after=5.0)

    @commands.hybrid_command()
    @commands.has_permissions(manage_messages = True)
    async def lock(self,ctx:commands.Context, channel:Optional[discord.TextChannel], role:Optional[discord.Role]):
        if not role:
            role = ctx.message.guild.default_role
        if channel:
            return await channel.set_permissions(role, send_messages=False)
        await ctx.channel.set_permissions(role, send_messages=False)
        await ctx.send(f"🔐 Successfully locked {ctx.channel.mention} for `@{role.name}`")


    @commands.hybrid_command()
    @commands.has_permissions(manage_messages = True)
    async def unlock(self,ctx:commands.Context, channel:Optional[discord.TextChannel],role:Optional[discord.Role]):
        if not role:
            role = ctx.message.guild.default_role
        if channel:
            return await channel.set_permissions(role, send_messages=True)
        await ctx.channel.set_permissions(role, send_messages=True)
        await ctx.send(f"🔐 Successfully unlocked {ctx.channel.mention} for `@{role.name}")

async def setup(client: commands.Bot):
    await client.add_cog(Moderation(client))
