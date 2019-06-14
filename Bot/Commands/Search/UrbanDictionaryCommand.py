import discord
from discord.ext import commands

from Modules import CommandCheck as cmd
from Modules.Searching import UrbanDictionarySearch as search
from Helpers import EmbedHelper as embed

class CMD_Urban:
    def __init__ (self, Client):
        self.Client = Client

    @commands.command()
    async def urban (self, ctx, *Search):
        Server = ctx.guild
        Channel = ctx.channel

        if cmd.CheckCommand ('UrbanDictionary', Server.id) == False:
            return

        Item = ''
        for Word in Search:
            Item += Word
            Item += ' '

        if Item == '':
            await embed.ErrorEmbed (self.Client, 'Specify', Channel)

        else:
            Result = search.Search (Item)

            await embed.UrbanEmbed (self.Client, Result.Word, Result.Definition, Result.Example, Result.Upvotes, Result.Downvotes, Channel)

def setup (_Client):
    _Client.add_cog (CMD_Urban (_Client))
