import discord
from discord.ext import commands

from Modules import CommandCheck as cmd
from Modules.Searching import YoutubeSearch as search
from Helpers import EmbedHelper as embed

class CMD_Youtube:
    def __init__ (self, Client):
        self.Client = Client

    @commands.command()
    async def twitch (self, ctx, *Search):
        Server = ctx.guild
        Channel = ctx.channel

        if cmd.CheckCommand ('Twitch', Server.id) == False:
            return

        Item = ''
        for Word in Search:
            Item += Word
            Item += ' '

        if Item == '':
            await embed.ErrorEmbed (self.Client, 'Specify', Channel)

        else:
            # Do a twitch search instead
            Result = search.SearchVideo (Item)

            await embed.ResultLinkEmbed (self.Client, 'Twitch Channel', Result.Title, Result.Description, Result.Url, Channel)

def setup (_Client):
    _Client.add_cog (CMD_Youtube (_Client))
