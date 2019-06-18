from google.google import search, calculate, convert_currency

import discord
from discord.ext import commands

from Helpers import EmbedHelper as Embed

class GoogleCommand (commands.Cog):
    def __init__ (self, Client : discord.Client):
        self.Client = Client
    
    @commands.command (aliases = ['search'])
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

    @commands.command (aliases = ['calculator', 'googlecalculate'])
    async def calculate (self, ctx : commands.Context, *, _Query : str):
        Result = calculate(_Query)
        Embed = discord.Embed (
            title = f'Google Calculator: **{_Query}**',
            description = f'{Result.value}'
        )
        Embed.set_author (
            name = self.Client.user.name,
            url = self.Client.Website,
            icon_url = self.Client.user.avatar_url
        )

    @commands.command (aliases = ['currency', 'currencycovert'])
    async def convert (self, ctx : commands.Context, _Value, _From, *,_To = 'USD'):
        Result = convert_currency(_Value, _From, _To)
        Embed = discord.Embed (
            title = f'Currency Conversion: {_Value} {_From} to {_To}',
            description = f'{Result.value} {_To}'
        )
        Embed.set_author (
            name = self.Client.user.name,
            url = self.Client.Website,
            icon_url = self.Client.user.avatar_url
        )

def setup (_Client):
    _Client.add_cog (GoogleCommand (_Client))
