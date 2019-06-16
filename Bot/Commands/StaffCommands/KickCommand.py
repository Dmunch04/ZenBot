import discord
from discord.ext import commands

from Core import PermissionLevel, HasPermission

class KickCommand (commands.Cog):
    def __init__ (self, Client: discord.Client):
        self.Client = Client

    @HasPermission (PermissionLevel.Moderator)
    @commands.command ()
    async def kick (self, ctx = commands.Context, _Members = commands.Greedy[discord.Member], *, _Reason : str = "The Boot has spoken"):
        """ Kicks 1 or more members """

        Server = ctx.guild

        for Member in _Members:
            await Member.create_dm ()
            await Member.dm_channel.send (f'You have been kicked from {Server}\nReason: {_Reason}\nJoin back at: {Server.invites ()[0]}')

            await Server.kick (Member, reason = _Reason)

def setup (_Client: discord.Client):
    _Client.add_cog (KickCommand (_Client))
