from DavesLogger import Logs

import discord
from discord.ext import commands

from Bot.Core import PermissionLevel, HasPermission

class MuteCommand (commands.Cog):
    def __init__ (self, Client: discord.Client):
        self.Client = Client

    @HasPermission (PermissionLevel.Moderator)
    @commands.command ()
    async def mute (self, ctx: commands.Context, _Members = commands.Greedy[discord.Member], *, _Reason: str = 'You\'ve been muted!'):
        """ Mutes 1 or more members """

        Server = ctx.guild

        MutedRole = discord.utils.get (Server.roles, name = 'Muted')

        if not MutedRole:
            Logs.Error (f'No muted role found!\nServer: {Server.id} && {Server.name}')

            return None

        for Member in _Members:
            await Member.create_dm ()
            Embed=discord.Embed (title="You have been muted", description=f"You have been muted from {Server} for {_Reason}", color=0xff0000)
            Embed.set_author (name=self.Client.name, url="https://dmunch04.github.io/ZenBot/", icon_url= self.Client.avatar_url)
            await Member.dm_channel.send (embed=Embed)

            await Member.add_roles (MutedRole, reason = _Reason)

def setup (_Client: discord.Client):
    _Client.add_cog (MuteCommand (_Client))
