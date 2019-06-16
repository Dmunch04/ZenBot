import discord
from discord.ext import commands

from Core import PermissionLevel, HasPermission

class ClearCommand (commands.Cog):
    def __init__ (self, Client):
        self.Client = Client

    @HasPermission (PermissionLevel.Moderator)
    @commands.command ()
    async def clear (self, ctx: commands.Context, _Messages: int = 1):
        Channel = ctx.channel

def setup (_Client):
    _Client.add_cog (ClearCommand (_Client))
