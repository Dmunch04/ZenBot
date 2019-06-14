import eve

import discord
from discord.ext import commands

import Config
from Modules import CommandCheck as cmd
from Modules import RoleCheck as role
from Helpers import EmbedHelper as embed

class CMD_Kick:
    def __init__ (self, Client):
        self.Client = Client

    @commands.command (pass_context = True)
    async def kick (self, ctx, _User : discord.User, *, Reason):
        Server = ctx.message.server
        Channel = ctx.message.channel
        Message = ctx.message

        if cmd.CheckCommand ('Kick', Server.id) == False:
            return

        Path = Config.Path_Data_Servers + '/' + Server.id + '/settings.eve'

        Data = eve.load (Path)

        if role.CheckRole (Sender, Data['Role_Kick']) == False:
            await embed.ErrorEmbed (self.Client, 'Permission', Channel)
            return

        await _User.create_dm()
        await _User.dm_channel.send(f'You have been kicked from {0} for {1}'.format(Server, Reason))


        await self.Client.kick (_User)

        await self.Client.delete_message (Message)

def setup (_Client):
    _Client.add_cog (CMD_Kick (_Client))
