from google.google import search, calculate, convert_currency

import discord
from discord.ext import commands

class GoogleCommand (commands.Cog):
    def __init__ (self, Client : discord.Client):
        self.Client = Client
    
    @commands.command (aliases = ['search'])
    async def google (self, ctx : commands.Context, *, _Query : str):
        Result = search(_Query)[0]
        Name = Result.name.replace("http","]\nhttp")


        Embed = discord.Embed (
            title = f'Top Google Search Result for: **{_Query}**',
            description = f''
        )
        Embed.set_author (
            name = self.Client.user.name,
            url = self.Client.Website,
            icon_url = self.Client.user.avatar_url
        )
        Embed.add_field (
            name = f'[{Name}',
            value = Result.description
        )
        await ctx.send(embed = Embed)

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