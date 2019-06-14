import json

import discord
from discord.ext import commands

import Config
from Modules import CommandCheck as cmd
from Helpers import EmbedHelper as embed

class CMD_User:
    def __init__ (self, Client):
        self.Client = Client

    @commands.command()
    async def user (self, ctx, _User : discord.User):
        Server = ctx.guild
        Channel = ctx.channel

        if cmd.CheckCommand ('User', Server.id) == False:
            return

        Path = Config.Path_Data_Servers + '/' + Server.id + '/Users/' + _User.name + '#' + _User.discriminator + '/' + 'UserFile.eve'

        Data = json.load (Path)

        I_Name = Data['Name']
        I_Tag = Data['Tag']
        I_Roles = Data['Roles']
        I_Karma = Data['Thanks']
        I_Activity = Data['Activity']
        I_Warns = Data['Warnings']

        await embed.UserEmbed (self.Client, I_Name, I_Tag, I_Roles, I_Karma, I_Activity, I_Warns, Channel)

def setup (_Client):
    _Client.add_cog (CMD_User (_Client))
