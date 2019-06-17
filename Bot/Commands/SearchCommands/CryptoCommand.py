from cryptocompare import get_price

import discord
from discord.ext import commands

class CryptoCommand (commands.Cog):
    def __init__ (self, Client : discord.Client):
        self.Client = Client
    
    @commands.command (aliases = ['cryptocurrency', 'cryptoprice'])
    async def crypto (self, ctx : commands.Context, _Ticker : str):

        Price = get_price (_Ticker, curr = 'USD')[_Ticker]['USD']
        Embed = discord.Embed (
            title = f'Cryptocurrency Info: {_Ticker}',
            description = f'{_Ticker} current price: ${Price}'
        )
        Embed.set_author (
            name = self.Client.user.name,
            url = self.Client.Website,
            icon_url = self.Client.user.avatar_url
        )
        await ctx.send(embed = Embed)

def setup (_Client):
    _Client.add_cog (CryptoCommand (_Client))