import discord
from discord.ext import commands

from Modules import CommandCheck as cmd
from Helpers import EmbedHelper as embed

class CMD_Translate:
    def __init__ (self, Client):
        self.Client = Client

    @commands.command (pass_context = True)
    async def translate (self, ctx, _Text, _From, _To):
        Server = ctx.message.server
        Channel = ctx.message.channel

        if cmd.CheckCommand ('Translate', Server.id) == False:
            return

        # Translate

def setup (_Client):
    _Client.add_cog (CMD_Translate (_Client))
