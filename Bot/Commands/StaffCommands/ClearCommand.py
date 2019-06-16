import discord
from discord.ext import commands

from Bot.Core import PermissionLevel, HasPermission

class ClearCommand (commands.Cog):
    def __init__ (self, Client):
        self.Client = Client

    @HasPermission (PermissionLevel.Moderator)
    @commands.command ()
    async def clear (self, ctx: commands.Context, _Messages: int = 1):
        Sender = ctx.author
        Channel = ctx.channel
        await Channel.purge (limit = _Messages)
        Embed = discord.Embed (title = "CHAT CLEARED", description = f'{Sender} cleared {_Messages} from this channel')
        Embed.set_author (name=self.Client.name, url="https://dmunch04.github.io/ZenBot/",icon_url=self.Client.avatar_url)
        await ctx.send ()

def setup (_Client):
    _Client.add_cog (ClearCommand (_Client))
