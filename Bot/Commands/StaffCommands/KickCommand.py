import discord
from discord.ext import commands

from Core import PermissionLevel, HasPermission

class KickCommand (commands.Cog):
    def __init__ (self, Client: discord.Client):
        self.Client = Client

    @HasPermission (PermissionLevel.Moderator)
    @commands.command ()
    async def kick (self, ctx: commands.Context, _Members: commands.Greedy[discord.Member], *, _Reason: str = 'You\'ve been kicked!'):
        """ Kicks 1 or more members """

        Server = ctx.guild
        Invites = await Server.invites ()

        if isinstance (_Members, discord.Member):
            _Members = [_Members]

        for Member in _Members:
            await Embed.DMEmbed (
                'You\'ve been kicked!',
                f'You\'ve been kicked from {Server} for {_Reason}!',
                0xff0000,
                Member,
                self.Client,
                [
                    ('Join Back', f'To rejoin {Server}, [click here]({Invites[0].url} "{Server.name}")')
                ]
            )

            await Server.kick (Member, reason = _Reason)

def setup (_Client: discord.Client):
    _Client.add_cog (KickCommand (_Client))
