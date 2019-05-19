import discord
from discord.ext import commands

from Modules import CommandCheck as cmd
from Modules.Searching import WikipediaSearch as search
from Helpers import EmbedHelper as embed

class CMD_Wikipedia:
    def __init__ (self, Client):
        self.Client = Client

    @commands.command (pass_context = True)
    async def wiki (self, ctx, *Search):
        Server = ctx.message.server
        Channel = ctx.message.channel

        if cmd.CheckCommand ('Wikipedia', Server.id) == False:
            return

        Item = ''
        for Word in Search:
            Item += Word
            Item += ' '

        if Item == '':
            await embed.ErrorEmbed (self.Client, 'Specify', Channel)

        else:
            Result = search.Search (Item)

            await embed.ResultLinkEmbed (self.Client, 'Wikipedia', Result.Title, Result.Content, Result.Url, Channel)

def setup (_Client):
    _Client.add_cog (CMD_Wikipedia (_Client))
