import datetime
from discord.ext.commands import check

DISCORD_EPOCH = datetime.datetime(1970, 1, 1, 7, 30)
FALCON_DEVEL_GUILD_ID = 897312479191912489
class _MissingSentinel:
    __slots__ = ()

    def __eq__(self, other) -> bool:
        return False

    def __bool__(self) -> bool:
        return False

    def __hash__(self) -> int:
        return 0

    def __repr__(self):
        return '...'

def falcondevelonly():
    async def chk(ctx):
        if ctx.guild is None:
            return False
        return ctx.guild.id == FALCON_DEVEL_GUILD_ID

    return check(chk)
