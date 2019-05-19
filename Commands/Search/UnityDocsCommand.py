import discord
from discord.ext import commands

from Modules import CommandCheck as cmd
from Modules.Searching import UnityDocsSearch as search
from Helpers import EmbedHelper as embed

class CMD_Unity:
    def __init__ (self, Client):
        self.Client = Client

    @commands.command (pass_context = True)
    async def script (self, ctx, *Search):
        Server = ctx.message.server
        Channel = ctx.message.channel

        if cmd.CheckCommand ('Script', Server.id) == False:
            return

        Item = ''
        for Word in Search:
            Item += Word
            Item += ' '

        if Item == '':
            await embed.ErrorEmbed (self.Client, 'Specify', Channel)

        else:
            Result = search.Search (Item, 'script')

            await embed.ResultLinkEmbed (self.Client, 'Unity Script API', Result.Title, Result.Tags, Result.Url, Channel)

    @commands.command (pass_context = True)
    async def manual (self, ctx, *Search):
        Server = ctx.message.channel
        Channel = ctx.message.channel

        if cmd.CheckCommand ('Manual', Server.id) == False:
            return

        Item = ''
        for Word in Search:
            Item += Word
            Item += ' '

        if Item == '':
            await embed.ErrorEmbed (self.Client, 'Specify', Channel)

        else:
            Result = search.Search (Item, 'manual')

            await embed.ResultLinkEmbed (self.Client, 'Unity Manual', Result.Title, Result.Description, Result.Url, Channel)

def setup (_Client):
    _Client.add_cog (CMD_Unity (_Client))
