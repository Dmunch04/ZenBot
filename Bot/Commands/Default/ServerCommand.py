import discord
from discord.ext import commands

from Modules import CommandCheck as cmd
from Helpers import EmbedHelper as embed

class CMD_Server:
    def __init__ (self, Client):
        self.Client = Client

    @commands.command (pass_context = True)
    async def server (self, ctx):
        Server = ctx.message.server
        Channel = ctx.message.channel

        if cmd.CheckCommand ('Server', Server.id) == False:
            return

        await embed.ServerEmbed (self.Client, Server, Channel)

    @commands.command (pass_context = True)
    async def users (self, ctx):
        Server = ctx.message.server

        if cmd.CheckCommand ('Users', Server.id) == False:
            return

        await self.Client.say ('There are currently {0} members!'.format (Server.member_count))

    @commands.command (pass_context = True)
    async def invite (self, ctx):
        Server = ctx.message.server

        if cmd.CheckCommand ('Invite', Server.id) == False:
            return

        await self.Client.say ('Invite Link: {0}'.format (discord.invites_from (Server)[0])) # Find the invite

def setup (_Client):
    _Client.add_cog (CMD_Server (_Client))
