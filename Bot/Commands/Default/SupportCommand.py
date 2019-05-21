import discord
from discord.ext import commands

from Modules import CommandCheck as cmd
from Helpers import EmbedHelper as embed

class CMD_Support:
    def __init__ (self, Client):
        self.Client = Client

    @commands.command (pass_context = True)
    async def support (self, ctx, _Desc):
        Server = ctx.message.server
        Channel = ctx.message.channel

        if cmd.CheckCommand ('Support', Server.id) == False:
            return

        # Start support thread

def setup (_Client):
    _Client.add_cog (CMD_Support (_Client))
