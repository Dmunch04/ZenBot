import eve

import discord
from discord.ext import commands

import Config
from Modules import CommandCheck as cmd
from Modules import RoleCheck as role
from Helpers import EmbedHelper as embed
from BanCommand import ban

class CMD_Warn:
    def __init__ (self, Client):
        self.Client = Client

    @commands.command()
    async def warn (self, ctx, _User : discord.User, *, _Reason):
        Server = ctx.guild
        Message = ctx.message
        Channel = ctx.channel

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

        # DMs user when they get warned
        await _User.create_dm()
        await _User.dm_channel.send(f'You have been warned from {0} for {1}'.format(Server, _Reason))

        if int (Data['Warns']) > int (Settings['WarnsToBan']):
            # DMs user when banned for too many warns
            await _User.create_dm()
            await _User.dm_channel.send(f'You have been banned from {0} for getting too many warnings'.format(Server))
            await self.Client.ban (_User, 0, reason = 'Too many warnings')

        await self.Client.delete_message (Message)

def setup (_Client):
    _Client.add_cog (CMD_Warn (_Client))
