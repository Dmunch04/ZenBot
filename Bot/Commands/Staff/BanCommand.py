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

    @commands.command()
    async def ban (self, ctx, _User : discord.User, *, _Reason : str):
        Server = ctx.guild
        Channel = ctx.channel
        Message = ctx.message

        if cmd.CheckCommand ('Ban', Server.id) == False:
            return

        Path = Config.Path_Data_Servers + '/' + Server.id + '/settings.eve'

        Data = eve.load (Path)

        if role.CheckRole (Sender, Data['Role_Ban']) == False:
            await embed.ErrorEmbed (self.Client, 'Permission', Channel)
            return
        # DMs the user before they get banned
        await _User.create_dm()
        await _User.dm_channel.send(f'You have been banned from {0} for {1}'.format(Server, _Reason))
        
        # Bans the user
        await Server.ban (_User, 0, reason = _Reason)
        
        # Deletes the command
        await Message.delete()

    @commands.command()
    async def unban (self, ctx, _User : discord.User, *, _Reason):
        Server = ctx.guild
        Message = ctx.message
        Channel = ctx.channel
        
        if cmd.CheckCommand ('Unban', Server.id) == False:
            return

        Path = Config.Path_Data_Servers + '/' + Server.id + '/settings.eve'

        Data = eve.load (Path)

        if role.CheckRole (Sender, Data['Role_Unban']) == False:
            await embed.ErrorEmbed (self.Client, 'Permission', Channel)
            return

        await Server.unban (_User, reason = _Reason)

        await Message.delete()

def setup (_Client):
    _Client.add_cog (CMD_Ban (_Client))
