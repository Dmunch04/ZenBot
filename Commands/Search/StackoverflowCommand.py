import discord
from discord.ext import commands

from Modules import CommandCheck as cmd
from Modules.Searching import StackoverflowSearch as search
from Helpers import EmbedHelper as embed

class CMD_Stackoverflow:
    def __init__ (self, Client):
        self.Client = Client

    @commands.command (pass_context = True)
    async def stackoverflow (self, ctx, *Search):
        Server = ctx.message.server
        Channel = ctx.message.channel

        if cmd.CheckCommand ('Stackoverflow', Server.id) == False:
            return

        Item = ''
        for Word in Search:
            Item += Word
            Item += ' '

        if Item == '':
            await embed.ErrorEmbed (self.Client, 'Specify', Channel)

        else:
            Result = search.Search (Item)

            await embed.ResultLinkEmbed (self.Client, 'Stackoverflow', Result.Title, Result.Tags, Result.Url, Channel)

def setup (_Client):
    _Client.add_cog (CMD_Stackoverflow (_Client))
