#using PYCORD beta
import this
import discord
import json
import asyncio
import os
import sqlite3
from discord.colour import Color
from discord.embeds import Embed
from discord.ext import commands
from discord.guild import Guild


BOT_COGS = (
    "cogs.norickroll",
    "cogs.owner",
    "cogs.economy",
    "cogs.globalchat"
)
intents = discord.Intents.all()

class asmartguy(commands.AutoShardedBot):
    def __init__(self):
        super().__init__(command_prefix="!?",
        owner_id=881095807565172776,
        case_insensitive=True)
        try:
            self.conn = sqlite3.connect("Discord\database\settings.db")
        except Exception as e:
            print(e)

    async def on_ready(self):
        print("The smart bot is online and more smarter than ever")

    async def on_message(self, message):
        if not message.author.bot:
            await self.process_commands(message)
        else:
            return

    async def on_guild_join(self, guild:Guild):
        id = guild.id
        c = self.conn.cursor()
        try:
            c.execute('''INSERT OR IGNORE INTO rickstatus(SERVERID,confirm)VALUES(?,?)''', (id, "False"))
            self.conn.commit()
        except Exception as e:
            print(e)
    def turn_on(self):
        self.remove_command("help")
        try:
            for cogs in BOT_COGS:
                self.load_extension(cogs)
                print(f"Loaded {cogs}")
            print("All Cogs checked and are ready to run")
            with open("Discord\credentials.json", "r") as cred:
                m =json.load(cred)
                        
            super().run(m["token"])
        except Exception as ex:
            print(f"An unexpected error happened: {ex}")

if __name__ == '__main__':
    asmartguy().turn_on()



