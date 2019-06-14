import json

import discord
from discord.ext import commands

import Config
from Modules import CommandCheck as cmd
from Modules import RoleCheck as role
from Helpers import EmbedHelper as embed

class CMD_Mute:
    def __init__ (self, Client):
        self.Client = Client

    @commands.command (pass_context = True)
    async def mute (self, ctx, _User : discord.Member, *, Reason):
        Server = ctx.message.server
        Channel = ctx.message.channel
        Message = ctx.message

        if cmd.CheckCommand ('Mute', Server.id) == False:
            return

        Path = Config.Path_Data_Servers + '/' + Server.id + '/settings.eve'

        Data = json.load (Path)

        if role.CheckRole (Sender, Data['Role_Mute']) == False:
            await embed.ErrorEmbed (self.Client, 'Permission', Channel)
            return

        RoleOverwrite = Channel.overwrites_for (_User) or \
        discord.PermissionOverwrite ()
        RoleOverwrite.send_messages = False
        RoleOverwrite.add_reactions = False

        await self.Client.edit_channel_permissions (
            Channel,
            _User,
            RoleOverwrite
        )

        # DMs user after they get muted
        await _User.create_dm()
        await _User.dm_channel.send(f'You have been muted from {0} for {1}'.format(Server, Reason))

        await self.Client.delete_message (Message)

    @commands.command (pass_context = True)
    async def unmute (self, ctx, _User : discord.User):
        Server = ctx.message.server
        Channel = ctx.message.channel
        Message = ctx.message

        if cmd.CheckCommand ('Unmute', Server.id) == False:
            return

        Path = Config.Path_Data_Servers + '/' + Server.id + '/settings.eve'

        Data = json.load (Path)

        if role.CheckRole (Sender, Data['Role_Unmute']) == False:
            await embed.ErrorEmbed (self.Client, 'Permission', Channel)
            return

        RoleOverwrite = Channel.overwrites_for (_User) or \
        discord.PermissionOverwrite ()
        RoleOverwrite.send_messages = True
        
        await self.Client.edit_channel_permissions (
            Channel,
            _User,
            RoleOverwrite
        )
        # DMs user when unmuted
        await _User.create_dm()
        await _User.dm_channel.send(f'You have been unmuted from {0}'.format(Server))

        await self.Client.delete_message (Message)

def setup (_Client):
    _Client.add_cog (CMD_Mute (_Client))
