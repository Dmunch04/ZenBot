import asyncio

import discord
from discord.ext import commands

from Core import PermissionLevel, HasPermission

class BanCommand (commands.Cog):
    def __init__ (self, Client: discord.Client):
        self.Client = Client

    @HasPermission (PermissionLevel.Admin)
    @commands.command ()
    async def ban (self, ctx: commands.Context, _Members: commands.Greedy[discord.Member], _DeleteDays: int = 0, *, _Reason: str = 'The ban hammer has spoken!'):
        """ Bans 1 or more members """

        Server = ctx.guild

        if isinstance (_Members, discord.Member):
            _Members = [_Members]

        for Member in _Members:
            await Member.create_dm ()

            Embed = discord.Embed (
                title = 'You\'ve been banned!',
                description = f'You\'ve been banned from {Server} for {_Reason}!',
                color = 0xff0000
            )
            Embed.set_author (
                name = self.Client.user.name,
                url = self.Client.Website,
                icon_url = self.Client.user.avatar_url
            )

            await Member.dm_channel.send (embed = Embed)

            await Server.ban (Member, delete_message_days = _DeleteDays, reason = _Reason)

    @HasPermission (PermissionLevel.Admin)
    @commands.command ()
    async def unban (self, ctx: commands.Context, _Members: commands.Greedy[discord.Member], _Reason: str = 'Welcome back!'):
        """ Unbans 1 or more members """

        Server = ctx.guild

        if isinstance (_Members, discord.Member):
            _Members = [_Members]

        for Member in _Members:
            await Server.unban (Member, reason = _Reason)

            await Member.create_dm ()

            Embed = discord.Embed (
                title = 'You\'ve been unbanned!',
                description = f'You\'ve been unbanned from {Server} for {_Reason}!',
                color = 0xff0000
            )
            Embed.add_field (
                name = 'Join Back',
                value = f'To rejoin {Server}, [click here]({Server.invites ()[0]} \'{Server.name}\'',
                inline = True
            )
            Embed.set_author (
                name = self.Client.user.name,
                url = self.Client.Website,
                icon_url = self.Client.user.avatar_url
            )

            await Member.dm_channel.send (embed = Embed)

    @HasPermission (PermissionLevel.Admin)
    @commands.command ()
    async def tempban (self, ctx: commands.Context, _Members: commands.Greedy[discord.Member], _DeleteDays: int = 0, _Days: int = 1, *, _Reason: str = 'The ban hammer has spoken!'):
        """ Temporarily bans 1 or more members """

        Server = ctx.guild

        if isinstance (_Members, discord.Member):
            _Members = [_Members]

        for Member in _Members:
            await Member.create_dm ()
            await Member.dm_channel.send (f'You have been banned from {Server} for {_Days} days \nReason: {_Reason}')

            await Server.ban (Member, reason = _Reason)

            GetServer = await self.Client.Database.GetServer (ctx.guild.id)
            GetMember = await GetServer.Members.Get (Member.id)
            GetMember.BanTimeLeft = int (_Days * 86400)

            await Server.unban (Member, reason = 'Temporary Ban Ended')

            await Member.dm_channel.send (f'You have been unbanned from {Server} \nReason: Temporary Ban Ended')

def setup (_Client: discord.Client):
    _Client.add_cog (BanCommand (_Client))
