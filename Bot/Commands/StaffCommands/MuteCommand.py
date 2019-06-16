import discord
from discord.ext import commands

from Bot.Core import PermissionLevel, HasPermission

class MuteCommand (commands.Cog):
    def __init__ (self, Client: discord.Client):
        self.Client = Client

    @HasPermission(PermissionLevel.Moderator)
    @commands.command()
    async def mute(self, ctx = commands.Context, _Members = commands.Greedy[discord.Member], *, _Reason : str = "Muffled"):
        Server = ctx.guild
        """ Mutes 1 or more members """
        mutedrole = discord.utils.get(Server.roles, name = 'Muted')
        if not mutedrole:
            raise Exception("No muted role found")
        Server = ctx.guild
        for Member in _Members:
            await Member.create_dm ()
            await Member.dm_channel.send (f"You have been muted in {Server}\nReason: {_Reason}\n")
            await Server.kick (Member, reason = _Reason)


def setup (_Client: discord.Client):
    _Client.add_cog (MuteCommand (_Client))