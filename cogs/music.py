import asyncio
import json
import discord
import wavelink
import config
from discord.ext import commands


class Music(commands.Cog):
    def __init__(self, client: commands.Bot) -> None:
        self.client = client
        self.repeat = {}




    @commands.Cog.listener()
    async def on_wavelink_node_ready(self, node: wavelink.Node):
        print(f"Node: <{node.identifier}> is ready!")

    async def duroconv(self, seconds: float):
        minute = seconds / 60
        hours = minute / 60
        m1 = hours * 60
        h1 = m1 * 60
        sec = h1 - seconds
        total = []
        total.append(minute)
        total.append(hours)
        total.append(sec)
        return total

    @commands.command()
    async def play(self, ctx: commands.Context, *, search: wavelink.YouTubeTrack):
        if not ctx.voice_client:
            vc: wavelink.Player = await ctx.author.voice.channel.connect(
                cls=wavelink.Player
            )
        else:
            vc: wavelink.Player = ctx.voice_client
        duration = search.duration
        title = search.title
        thumbnail = search.thumbnail
        author = search.author
        url = search.uri
        minute, hours, seconds = await self.duroconv(duration)
        await vc.play(search)

        pinfoem = discord.Embed(
            title=f"Now Playing: {title} by {author}",
            url=url,
            color=discord.Colour.green(),
            description=f"Duration = {int(hours)} hours {int(minute)} minutes {int(seconds)} seconds",
        )
        pinfoem.set_image(url=thumbnail)
        await ctx.send(embed=pinfoem)
        while True:
            if self.repeat[str(ctx.guild.id)]:
                if not vc.is_playing():
                    await asyncio.sleep(0.25)
                    await vc.play()

    @commands.command()
    async def pause(self, ctx: commands.Context):
        if not ctx.voice_client:
            return await ctx.send("The bot is not connected to music channel")

        else:
            vc: wavelink.Player = ctx.voice_client

        await vc.pause()
        await ctx.send("⏸️ **Paused music!**")

    @commands.command()
    async def resume(self, ctx: commands.Context):
        if not ctx.voice_client:
            return await ctx.send("The bot is not connected to music channel")

        else:
            vc: wavelink.Player = ctx.voice_client

        if vc.is_paused():
            await vc.resume()
            await ctx.send("⏯️ **Resumed music!**")
        elif not vc.is_playing():
            await ctx.send("VC is not playing anything")
        else:
            await ctx.send("The vc is already playing")

    @commands.command()
    async def stop(self, ctx: commands.Context):
        if not ctx.voice_client:
            return await ctx.send("The bot is not connected to music channel")

        else:
            vc: wavelink.Player = ctx.voice_client

        if vc.is_playing():
            await vc.stop()
            await ctx.send("🛑 **Stopped music!**")
        else:
            await ctx.send("🛑 Nothing is playing on VC")

    @commands.command()
    async def disconnect(self, ctx: commands.Context):
        if not ctx.voice_client:
            return await ctx.send("The bot is not connected to music channel")

        else:
            vc: wavelink.Player = ctx.voice_client

        if vc.is_connected():
            await vc.disconnect(force=True)
            await ctx.send("🛑 **Disconnected from VC**")
        else:
            await ctx.send("❌ Bot already disconnected")

    @commands.command()
    async def connect(self, ctx: commands.Context, voicec: discord.VoiceChannel = None):
        if voicec == None:
            if ctx.voice_client:
                return await ctx.send("The bot is already connected to music channel")
            else:

                await ctx.author.voice.channel.connect(cls=wavelink.Player)

        else:
            await voicec.connect(cls=wavelink.Player)


"""    @commands.group()
    async def loop(self, ctx: discord.ctx):
        if self.repeat[str(ctx.guild.id)]:
            del self.repeat[str(ctx.guild.id)]
            return await ctx.send("➰**Loop Stopped**")
        else:
            self.repeat[str(ctx.guild.id)] = True
            await ctx.send("➰ **Loop Started**")
"""


async def setup(bot):
    await bot.add_cog(Music(bot))
