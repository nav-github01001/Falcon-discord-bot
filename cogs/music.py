import asyncio
import discord


from discord.ext import commands


class Music(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        self.repeat = {}

        bot.loop.create_task(self.connect_nodes())

    async def connect_nodes(self):
        await self.bot.wait_until_ready()
        # await wavelink.NodePool.create_node(
        #    bot = self.bot,
        #    host = '173.249.9.178',
        #    port = 5074,
        #    password ="EpikHostOnTop"

        # )

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
    async def play(self, interaction: commands.Context, *, search: wavelink.YouTubeTrack):
        if not interaction.voice_client:
            vc: wavelink.Player = await interaction.author.voice.channel.connect(
                cls=wavelink.Player
            )
        else:
            vc: wavelink.Player = interaction.voice_client
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
        await interaction.response.send_message(embed=pinfoem)
        while True:
            if self.repeat[str(interaction.guild.id)]:
                if not vc.is_playing():
                    await asyncio.sleep(0.25)
                    await vc.play()

    @commands.command()
    async def pause(self, interaction: commands.Context):
        if not interaction.voice_client:
            return await interaction.response.send_message("The bot is not connected to music channel")

        else:
            vc: wavelink.Player = interaction.voice_client

        await vc.pause()
        await interaction.response.send_message("⏸️ **Paused music!**")

    @commands.command()
    async def resume(self, interaction: commands.Context):
        if not interaction.voice_client:
            return await interaction.response.send_message("The bot is not connected to music channel")

        else:
            vc: wavelink.Player = interaction.voice_client

        if vc.is_paused():
            await vc.resume()
            await interaction.response.send_message("⏯️ **Resumed music!**")
        elif not vc.is_playing():
            await interaction.response.send_message("VC is not playing anything")
        else:
            await interaction.response.send_message("The vc is already playing")

    @commands.command()
    async def stop(self, interaction: commands.Context):
        if not interaction.voice_client:
            return await interaction.response.send_message("The bot is not connected to music channel")

        else:
            vc: wavelink.Player = interaction.voice_client

        if vc.is_playing():
            await vc.stop()
            await interaction.response.send_message("🛑 **Stopped music!**")
        else:
            await interaction.response.send_message("🛑 Nothing is playing on VC")

    @commands.command()
    async def disconnect(self, interaction: commands.Context):
        if not interaction.voice_client:
            return await interaction.response.send_message("The bot is not connected to music channel")

        else:
            vc: wavelink.Player = interaction.voice_client

        if vc.is_connected():
            await vc.disconnect(force=True)
            await interaction.response.send_message("🛑 **Disconnected from VC**")
        else:
            await interaction.response.send_message("❌ Bot already disconnected")

    @commands.command()
    async def connect(self, interaction: commands.Context, voicec: discord.VoiceChannel = None):
        if voicec == None:
            if interaction.voice_client:
                return await interaction.response.send_message("The bot is already connected to music channel")
            else:

                await interaction.author.voice.channel.connect(cls=wavelink.Player)

        else:
            await voicec.connect(cls=wavelink.Player)

    @commands.group()
    async def loop(self, interaction: commands.Context):
        if self.repeat[str(interaction.guild.id)]:
            del self.repeat[str(interaction.guild.id)]
            return await interaction.response.send_message("➰**Loop Stopped**")
        else:
            self.repeat[str(interaction.guild.id)] = True
            await interaction.response.send_message("➰ **Loop Started**")


def setup(bot):
    bot.add_cog(Music(bot))
