import eve

import discord
from discord.ext import commands

import Config
from Modules import CommandCheck as cmd
from Modules import RoleCheck as role
from Helpers import EmbedHelper as embed

class CMD_Warn:
    def __init__ (self, Client):
        self.Client = Client

    @commands.command (pass_context = True)
    async def warn (self, ctx, _User : discord.User):
        Server = ctx.message.server
        Message = ctx.message
        Channel = ctx.message.channel

        if cmd.CheckCommand ('Warn', Server.id) == False:
            return

        Path = Config.Path_Data_Servers + '/' + Server.id + '/settings.eve'

        Data = eve.load (Path)

        if role.CheckRole (Sender, Data['Role_Warn']) == False:
            await embed.ErrorEmbed (self.Client, 'Permission', Channel)
            return

        Path = Config.Path_Data_Servers + '/' + Server.id + '/Users/' + _User.name + '#' + _User.discriminator + '/' + 'UserFile.eve'

        Data = eve.load (Path)

        Data['Warns'] = int (Data['Warns']) + 1

        eve.save (Data, Path)

        Path = Config.Path_Data_Servers + '/' + Server.id +'/settings.eve'

        Settings = eve.load (Path)

        if int (Data['Warns']) > int (Settings['WarnsToBan']):
            await self.Client.ban (_User, 0)

        await self.Client.delete_message (Message)

def setup (_Client):
    _Client.add_cog (CMD_Warn (_Client))
