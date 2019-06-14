import discord
from discord.ext import commands

from Modules import CommandCheck as cmd
from Helpers import EmbedHelper as embed

class CMD_About:
    def __init__ (self, Client):
        self.Client = Client

    @commands.command()
    async def dict (self, ctx, _Word):
        Server = ctx.guild
        Channel = ctx.channel

        if cmd.CheckCommand ('Dict', Server.id) == False:
            return

        # Check the dictionary

def setup (_Client):
    _Client.add_cog (CMD_About (_Client))
