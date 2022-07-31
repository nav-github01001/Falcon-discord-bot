from typing import Optional
import datetime
from .utils import colorsigns, misc
import discord
from discord import app_commands
from discord.ext import commands

class Moderation(commands.Cog):
    def __init__(self, client:commands.Bot) -> None:
        self.client = client
    
    @commands.hybrid_command()
    @app_commands.describe(
        member="The Member you want to time out", 
        hours = "duration of the Time-out (optional)",
        minutes="duration of the Time-out (optional)",
        seconds = "duration of the Time-out (optional)",
        reason = "The reason, shows up in the audit log"
    )
    async def timeout(self, ctx:commands.Context, member:discord.Member ,hours:Optional[int] = None, minutes:Optional[int] = None, seconds:Optional[int]=None, *, reason:Optional[str] = None):
        """
        Time-outs/Mutes a user.
        member = The Member you want to time out
        hours,minutes,seconds = duration of the Time-out (optional)
        reason = The reason, shows up in the audit log
        """
        time = None
        delta = None
        if hours or minutes or seconds:
            time= datetime.timedelta(hours=hours , minutes=minutes, seconds=seconds)
            delta = (datetime.datetime.utcnow().timestamp() - time.total_seconds())
        
        parsed_time_msg = f"<t:{int(delta)}:R>" if delta else "Unlimited"
        await member.timeout(time, reason=reason or f"Caused by {ctx.author.name+ctx.author.discriminator}")
        
        TEmbed = discord.Embed(color=int(colorsigns.SignEnum.DANGER),title="⏰ Timed out!", description=f"The user {member.mention} has been timed out.\nThe mute will persist about {parsed_time_msg}")

        await ctx.send(embed=TEmbed)

    @commands.hybrid_command()
    async def purge(self, ctx:commands.Context, limit:Optional[int]=50):
        await ctx.channel.purge(limit = limit+1)
        await ctx.send(f"♻️ Successfully Purged {limit} messages", delete_after=5.0)

async def setup(client:commands.Bot):
    await client.add_cog(Moderation(client))