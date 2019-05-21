import eve

import discord
from discord.ext import commands

import Config
from Modules import CommandCheck as cmd
from Modules import RoleCheck as role
from Helpers import EmbedHelper as embed

class CMD_Role:
    def __init__ (self, Client):
        self.Client = Client

    @commands.command (pass_context = True)
    async def role (self, ctx, _Role):
        Server = ctx.message.server
        Channel = ctx.message.channel
        Sender = ctx.message.author

        if cmd.CheckCommand ('Role', Server.id) == False:
            return

        Role = discord.utils.get (Server.roles, name = _Role)

        if role.CheckRole (Sender, Role) == True:
            await self.Client.remove_roles (Sender, Role)
        else:
            await self.Client.add_roles (Sender, Role)

    @commands.command (pass_context = True)
    async def roles (self, ctx):
        Server = ctx.message.server
        Channel = ctx.message.channel

        if cmd.CheckCommand ('Roles', Server.id) == False:
            return

        Path = Config.Path_Data_Servers + '/' + Server.id + '/settings.eve'

        Data = eve.load (Path)

        Roles = Data['Roles_Addable'].split (',')

        await embed.OtherEmbed (self.Client, 'Roles', f'Joinable roles in {Server.name}', '\n'.join (Roles), discord.Color.purple (), Channel)

def setup (_Client):
    _Client.add_cog (CMD_Role (_Client))
