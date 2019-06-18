from yahoo_fin.stock_info import get_live_price

import discord
from discord.ext import commands

from Helpers import EmbedHelper as Embed

class StockCommand (commands.Cog):
    def __init__ (self, Client : discord.Client):
        self.Client = Client

    @commands.command (aliases = ['stockprice', 'stocks'])
    async def stock (self, ctx: commands.Context, _Ticker: str):
        Channel = ctx.channel

        await Embed.Embed (
            f'Stock Info: {_Ticker}',
            f'{_Ticker} current price: ${round (get_live_price (_Ticker), 2)}',
            discord.Color.black ()
            Channel,
            self.Client
        )

def setup (_Client):
    _Client.add_cog (StockCommand (_Client))
