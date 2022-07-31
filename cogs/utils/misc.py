import datetime
from discord.ext.commands import check
time = datetime.timedelta(1,1,1,1,1,1,1)
DISCORD_EPOCH = datetime.datetime(1970,1,1,7,30)

def falcondevelonly():
    async def chk(ctx):
        if ctx.guild is None:
            return False
        return ctx.guild.id == 897312479191912489
    return check(chk)