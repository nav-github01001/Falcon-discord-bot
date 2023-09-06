import discord

# from discord.commands.commands import Option
from discord.ext import commands



class Raid(commands.Cog):
    def __init__(self, client: discord.Client) -> None:
        self.client = client

    @commands.group()
    async def raid(self, ctx):
        embed = discord.Embed(
            title="Settings for Raid Protection",
            description="**Note**:Only for administrators\n\n",
        )
        embed.add_field(
            name="> **detectmassjoins [joins/min]**: ",
            value="Toggle Whether to detect a lot of people trying to join at once\nIf so, the rate of joining also need to be provided",
        )
        embed.add_field(name="> **massjoinpunishment <timeout/kick/ban> [timeout]")
        await ctx.send(embed=embed)

    @commands.hybrid_command(description="Lockdown the entire server immediately")
    @commands.has_permissions(
        manage_guild=True, manage_channels=True, manage_roles=True
    )
    async def lockdown_server(self, ctx: commands.Context):
        """
        Immediately lock down the server with one command
        """
        roles = ctx.guild.fetch_roles()
        for invites in ctx.guild.invites():
            invites.delete(reason="Active Raid in the Server")
        for role in roles:
            for channel in ctx.guild.fetch_channels():
                channel.set_permissions(role, send_messages=False)


async def setup(bot):
    await bot.add_cog(Raid(bot))
