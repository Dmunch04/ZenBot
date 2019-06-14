import discord
from discord.ext import commands

from Modules import CommandCheck as cmd
from Helpers import EmbedHelper as embed

class CMD_About:
    def __init__ (self, Client):
        self.Client = Client

    @commands.command
    async def about (self, ctx):
        Server = ctx.guild
        Channel = ctx.channel

        if cmd.CheckCommand ('About', Server.id) == False:
            return

        await embed.OtherEmbed (self.Client, 'About', 'About me, ZenBot', "Hello guys! My name is Boto. I'm the helper of Make Indies. My best buddy, Munchii, is the one that learned me everything I know. The important thing: I'm always here to help. To get my help, do !help", discord.Color.blue (), Channel)

def setup (_Client):
    _Client.add_cog (CMD_About (_Client))
