import discord
import re
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType
import sqlite3


class economysys(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot
        try:
            self.conn = sqlite3.connect("database\data.db")
        except Exception as e:
            print("Database error: "+ e)


            
    @commands.command(aliases=["bal"])
    @commands.cooldown(1, 30, BucketType.user)
    async def balance(self,ctx, user:discord.Member=None):
        if user == None:
            user = ctx.author
        else:
            user = user
        c = self.conn.cursor()
        c.execute('''INSERT OR IGNORE INTO balance(USERID,WALLET,BANK,BANK_SPACE)VALUES(?,?,?,?)''', (user.id,250,0,2000))
        self.conn.commit()
        c.execute('''SELECT * FROM balance WHERE USERID=?''', (user.id,))
        l = c.fetchall()
        
        for list in l:
            userid, wallet, bank, bank_space = list
        balem = discord.Embed(title=f"{user.name}\'s Balance", description=f"\nWallet = {wallet}\nBank = {bank}/{bank_space}", color=discord.Colour.random())
        await ctx.send(embed=balem) 

    
    @commands.command(aliases=["dep"])
    async def deposit(self,ctx, amt=None):
        if amt ==None:
            return await ctx.send("You have not specified the amount")
        amt = int(amt)
        
        user = ctx.author

        c = self.conn.cursor()
        c.execute('''INSERT OR IGNORE INTO balance(USERID,WALLET,BANK,BANK_SPACE)VALUES(?,?,?,?)''', (user.id,250,0,2000))
        self.conn.commit()
        c.execute('''SELECT * FROM balance WHERE USERID=?''', (user.id,))
        l = c.fetchall()
        
        for list in l:
            userid, wallet, bank, bank_space = list
        if amt < wallet and amt < int(bank_space - bank):
            wallet = wallet - amt
            bank = bank + amt
            c.execute('''UPDATE balance SET WALLET=? WHERE USERID=?''', (wallet,user.id))
            c.execute('''UPDATE balance SET BANK=? WHERE USERID=?''', (bank,user.id))
            self.conn.commit()
            await ctx.send(f"You have deposited **{amt}** to your bank")
        else:
            return await ctx.send("yOu DoNt HaVe EnOuGh MoNeY iN yOuR wAlLeT oR sPaCe In YoUr BaNk")

    @commands.command(aliases = ["with"])
    async def withdraw(self, ctx, amt=None):
        if amt==None :
            return await ctx.send("You have not specified the amount")
        amt = int(amt)
        user = ctx.author
        c =self.conn.cursor()
        c.execute('''INSERT OR IGNORE INTO balance(USERID,WALLET,BANK,BANK_SPACE)VALUES(?,?,?,?)''', (user.id,250,0,2000))
        self.conn.commit()
        c.execute('''SELECT * FROM balance WHERE USERID=?''', (user.id,))
        l = c.fetchall()        
        for list in l:
            userid, wallet, bank, bank_space = list
        if amt < bank:
            wallet = wallet + amt
            bank = bank - amt
            c.execute('''UPDATE balance SET WALLET=? WHERE USERID=?''', (wallet,user.id))
            c.execute('''UPDATE balance SET BANK=? WHERE USERID=?''', (bank,user.id))
            self.conn.commit()
            await ctx.send(f"You have deposited **{amt}** to your bank")
        else:
            await ctx.send("yOu DoNt HaVe EnOuGh MoNeY iN yOuR bAnK")
    
    






def setup(bot):
    bot.add_cog(economysys(bot))    
