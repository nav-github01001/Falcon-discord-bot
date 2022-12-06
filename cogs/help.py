import discord
from discord.enums import ButtonStyle
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType
import sqlite3
import asyncio
from discord.ui import View
class HelpView(View):
    async def on_timeout(self) -> None:
        for item in self.children:
            item.disabled = True
        
        await self.message.edit(view=self)

    @discord.ui.button(emoji="")
    async def previous(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message('Hello!', ephemeral=True)
    
    @discord.ui.select(cls=discord.ui.Select, options=[discord.SelectOption(label="Fun", description="Fun commands for the bot", emoji=])
    async def HelpSelect(self):...

class Help(commands.Cog):
    def __init__(self, client: discord.Client) -> None:
        self.client = client
        try:
            self.conn = sqlite3.connect("./databases/settings.db")
        except Exception as e:
            print(e)
    
    @commands.hybrid_command()
    async def help(self,ctx:commands.Context):
        embed = discord.Embed(title="Help", description="Select an option from the menu for help")       
        await ctx.send(embed=embed, view=HelpView(timeout=30))

    async def raid(self,ctx):
        embed=discord.Embed(title="Settings for Raid Protection", description="**Note**:Only for administrators\n\n")
        embed.add_field(name="> **detectmassjoins [joins/min]**: ", value="Toggle Whether to detect a lot of people trying to join at once\nIf so, the rate of joining also need to be provided")
        embed.add_field(name="> **massjoinpunishment <timeout/kick/ban> [timeout]")
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Help(bot))
