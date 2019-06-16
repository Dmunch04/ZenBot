import discord
from discord.ext import commands

from Bot.Core import PermissionLevel, HasPermission

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
            
            Embed=discord.Embed (title="You have been kicked", description=f"You have been kicked from {Server} for {_Reason}", color=0xff0000)
            Embed.set_author (name=self.Client.name, url="https://dmunch04.github.io/ZenBot/",icon_url= self.Client.avatar_url)
            Embed.add_field(name='Join Back', value= f'To rejoin {Server}, [click here]({Server.invites()[0]} "{Server.name}"', inline=True)
            await Member.dm_channel.send (embed=Embed)

            await Server.kick (Member, reason = _Reason)

def setup (_Client: discord.Client):
    _Client.add_cog (KickCommand (_Client))
