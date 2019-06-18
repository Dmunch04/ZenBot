from google.google import search

import discord
from discord.ext import commands

from Helpers import URLFinder as URL
from Helpers import EmbedHelper as Embed

class GoogleCommand (commands.Cog):
    def __init__ (self, Client : discord.Client):
        self.Client = Client

    @commands.command ()
    async def google (self, ctx : commands.Context, *, _Search: str):
        Channel = ctx.channel

        Result = search (_Search)[0]

        Name, Link = URL.FindURL (Result.name)

        if not Link.startswith ('http://') or Link.startswith ('https://'):
            Link = 'http://' + Link

        await Embed.Embed (
            f'Google result of: {_Search}',
            f'',
            discord.Color.blue (),
            Channel,
            self.Client,
            [
                (f'[{Name}]({Link} "{_Search}")', Result.description)
            ]
        )

def setup (_Client):
    _Client.add_cog (GoogleCommand (_Client))
