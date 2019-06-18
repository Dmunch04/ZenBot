from google.google import search

import discord
from discord.ext import commands

from Helpers import EmbedHelper as Embed

class GoogleCommand (commands.Cog):
    def __init__ (self, Client : discord.Client):
        self.Client = Client

    @commands.command ()
    async def google (self, ctx : commands.Context, *, _Query : str):
        Channel = ctx.channel

        Result = search(_Query)[0]
        Name = Result.name.replace("http","]\nhttp")

        await Embed.Embed (
            self.Client,
            f'Top Google Search Result for: **{_Query}**',
            f'',
            discord.Color.black (),
            Channel,
            self.Client,
            [
                (f'[{Name}]', Result.description)
            ]
        )

def setup (_Client):
    _Client.add_cog (GoogleCommand (_Client))
