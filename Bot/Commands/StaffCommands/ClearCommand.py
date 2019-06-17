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
        Sender = ctx.author

        await Channel.purge (limit = _Messages)

        Embed = discord.Embed (
            title = 'Chat Cleared!',
            description = f'{Sender.mention} cleared {str (_Messages)} from this channel!'
        )
        Embed.set_author (
            name = self.Client.user.name,
            url = self.Client.Website,
            icon_url = self.Client.user.avatar_url
        )

        await ctx.send (embed = Embed)

def setup (_Client):
    _Client.add_cog (ClearCommand (_Client))
