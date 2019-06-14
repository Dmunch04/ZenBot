import discord
from discord.ext import commands

from Modules import CommandCheck as cmd
from Helpers import EmbedHelper as embed

class CMD_Update:
    def __init__ (self, Client):
        self.Client = Client

    @commands.command()
    async def update (self, ctx):
        Server = ctx.guild
        Channel = ctx.channel

        if cmd.CheckCommand ('Update', Server.id) == False:
            return

        await embed.OtherEmbed (self.Client, 'Update', 'You tried to update ;)', discord.Color.blue (), Channel)

def setup (_Client):
    _Client.add_cog (CMD_Update (_Client))
