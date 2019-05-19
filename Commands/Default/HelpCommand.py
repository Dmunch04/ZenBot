import eve

import discord
from discord.ext import commands

import Config
from Modules import CommandCheck as cmd
from Modules import RoleCheck as role
from Helpers import EmbedHelper as embed

class CMD_Help:
    def __init__ (self, Client):
        self.Client = Client

    @commands.command (pass_context = True)
    async def help (self, ctx, _HelpSubject = ''):
        Server = ctx.message.server
        Channel = ctx.message.channel
        Sender = ctx.message.author

        if cmd.CheckCommand ('Help', Server.id) == False:
            return

        Path = Config.Path_Data_Servers + '/' + Server.id + '/settings.eve'

        Data = eve.load (Path)

        if _HelpSubject.lower () == 'music':
            _Path = Data['Path'] + Data['Path_MusicHelp']
            await embed.ListEmbed (self.Client, _Path, Channel)

        elif _HelpSubject.lower () == 'staff' and role.CheckRole (Sender, Data['Role_Staff']) == True:
            _Path = Data['Path'] + Data['Path_StaffHelp']
            await embed.ListEmbed (self.Client, _Path, Sender)

        elif _HelpSubject.lower () == 'management' and role.CheckRole (Sender, Data['Role_Staff']) == True:
            _Path = Data['Path'] + Data['Path_ManagementHelp']
            await embed.ListEmbed (self.Client, _Path, Sender)

        else:
            _Path = Data['Path'] + Data['Path_Help']
            await embed.ListEmbed (self.Client, _Path, Channel)

def setup (_Client):
    _Client.add_cog (CMD_Help (_Client))
