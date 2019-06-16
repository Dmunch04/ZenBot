import discord
from discord.ext import commands

from Core import PermissionLevel, HasPermission

class BanCommand (commands.Cog):
    def __init__ (self, Client: discord.Client):
        self.Client = Client

    @HasPermission (PermissionLevel.Admin)
    @commands.command ()
    async def ban (self, ctx: commands.Context, _Members = commands.Greedy[discord.Member], _DeleteDays: int = 0, *, _Reason: str = 'The ban hammer has spoken!'):
        """ Bans 1 or more members from the server """

        for Member in _Members:
            await Member.create_dm ()
            await Member.dm_channel.send (f'You have been banned from {ctx.guild} for {_Reason}')

            await Member.ban (delete_message_days = _DeleteDays, reason = _Reason)

    @HasPermission (PermissionLevel.Admin)
    @commands.command ()
    async def unban (self, ctx: commands.Context, _Member: discord.Member, _Reason: str = 'Welcome back!'):
        """ Unbans a member from the server """

        await _Member.unban (reason = _Reason)

        await Member.create_dm ()
        await Member.dm_channel.send (f'You have been unbanned from {ctx.guild} for {_Reason}')

def setup (_Client: discord.Client):
    _Client.add_cog (BanCommand (_Client))
