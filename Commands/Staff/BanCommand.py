import eve

import discord
from discord.ext import commands

import Config
from Modules import CommandCheck as cmd
from Modules import RoleCheck as role
from Helpers import EmbedHelper as embed

class CMD_Ban:
    def __init__ (self, Client):
        self.Client = Client

    @commands.command (pass_context = True)
    async def ban (self, ctx, _User : discord.User):
        Server = ctx.message.server
        Channel = ctx.message.channel
        Message = ctx.message

        if cmd.CheckCommand ('Ban', Server.id) == False:
            return

        Path = Config.Path_Data_Servers + '/' + Server.id + '/settings.eve'

        Data = eve.load (Path)

        if role.CheckRole (Sender, Data['Role_Ban']) == False:
            await embed.ErrorEmbed (self.Client, 'Permission', Channel)
            return

        await self.Client.ban (_User, 0)

        await self.Client.delete_message (Message)

    @commands.command (pass_context = True)
    async def unabn (self, ctx, _User : discord.User):
        Server = ctx.message.server
        Message = ctx.message
        Channel = ctx.message.channel

        if cmd.CheckCommand ('Unban', Server.id) == False:
            return

        Path = Config.Path_Data_Servers + '/' + Server.id + '/settings.eve'

        Data = eve.load (Path)

        if role.CheckRole (Sender, Data['Role_Unban']) == False:
            await embed.ErrorEmbed (self.Client, 'Permission', Channel)
            return

        await self.Client.ban (Server, _User)

        await self.Client.delete_message (Message)

def setup (_Client):
    _Client.add_cog (CMD_Ban (_Client))
