import eve

import discord
from discord.ext import commands

import Config
from Modules import CommandCheck as cmd
from Helpers import EmbedHelper as embed

class CMD_Rule:
    def __init__ (self, Client):
        self.Client = Client

    @commands.command()
    async def rules (self, ctx):
        Server = ctx.guild
        Channel = ctx.channel

        if cmd.CheckCommand ('Rules', Server.id) == False:
            return

        Path = Config.Path_Data_Servers + '/' + Server.id + '/settings.eve'

        Data = eve.load (Path)

        await embed.ListEmbed (self.Client, Data['Path_Rules'], Channel)

def setup (_Client):
    _Client.add_cog (CMD_Rule (_Client))
