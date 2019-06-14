import discord
from discord.ext import commands

from Modules import CommandCheck as cmd
from Modules.Searching import YoutubeSearch as search
from Helpers import EmbedHelper as embed

class CMD_Channel:
    def __init__ (self, Client):
        self.Client = Client

    @commands.command()
    async def channel (self, ctx, *Search):
        Server = ctx.guild
        Channel = ctx.channel

        if cmd.CheckCommand ('YoutubeChannel', Server.id) == False:
            return

        Item = ''
        for Word in Search:
            Item += Word
            Item += ' '

        if Item == '':
            await embed.ErrorEmbed (self.Client, 'Specify', Channel)

        else:
            Result = search.SearchChannel (Item)

            await embed.YoutubeChannel (self.Client, 'YouTube Channel', Result.Title, Result.Description, Result.Url, Channel)

def setup (_Client):
    _Client.add_cog (CMD_Channel (_Client))
