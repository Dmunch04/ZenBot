from yahoo_fin.stock_info import get_live_price

import discord
from discord.ext import commands

class StockCommand (commands.Cog):
    def __init__ (self, Client : discord.Client):
        self.Client = Client
    
    @commands.command (aliases = ['stockprice', 'stocks'])
    async def stock (self, ctx : commands.Context, _Ticker : str):
        Embed = discord.Embed (
            title = f'Stock Info: {_Ticker}',
            description = f'{_Ticker} current price: ${round (get_live_price (_Ticker), 2)}'
        )
        Embed.set_author (
            name = self.Client.user.name,
            url = self.Client.Website,
            icon_url = self.Client.user.avatar_url
        )
        await ctx.send(embed = Embed)

def setup (_Client):
    _Client.add_cog (StockCommand (_Client))