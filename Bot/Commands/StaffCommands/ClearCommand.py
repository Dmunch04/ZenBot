import discord
from discord.ext import commands

from Helpers import EmbedHelper as Embed
from Core import PermissionLevel, HasPermission, CommandEnabled

class ClearCommand (commands.Cog):
    def __init__ (self, Client):
        self.Client = Client

    @HasPermission (PermissionLevel.Moderator)
    @commands.command (aliases = ['prune', 'clearchat'])
    @commands.check (CommandEnabled)
    async def clear (self, ctx: commands.Context, _Messages: int = 1):
        Channel = ctx.channel
        Sender = ctx.author

        await Channel.purge (limit = _Messages)

        await Embed.Embed (
            'Chat Cleared!',
            f'{Sender.mention} cleared {str (_Messages)} messages from this channel!',
            discord.Color.purple (),
            Channel,
            self.Client
        )

def setup (_Client):
    _Client.add_cog (ClearCommand (_Client))
