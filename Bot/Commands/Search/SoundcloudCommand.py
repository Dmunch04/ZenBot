import discord
from discord.ext import commands

from Modules import CommandCheck as cmd
from Modules.Searching import SoundcloudSearch as search
from Helpers import EmbedHelper as embed

class CMD_Soundcloud:
    def __init__ (self, Client):
        self.Client = Client

    @commands.command()
    async def soundcloud (self, ctx, *Search):
        Server = ctx.guild
        Channel = ctx.channel

        if cmd.CheckCommand ('Soundcloud', Server.id) == False:
            return

        Item = ''
        for Word in Search:
            Item += Word
            Item += ' '

        if Item == '':
            await embed.ErrorEmbed (self.Client, 'Specify', Channel)

        else:
            Result = search.Search (Item)

            await embed.ResultLinkEmbed (self.Client, 'Soundcloud', Result.Title, Result.Author, Result.Url, Channel)

def setup (_Client):
    _Client.add_cog (CMD_Soundcloud (_Client))
