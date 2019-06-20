from yahoo_fin.stock_info import get_live_price

import discord
from discord.ext import commands

from Core import CommandEnabled
from Helpers import EmbedHelper as Embed

class StockCommand (commands.Cog):
    def __init__ (self, Client : discord.Client):
        self.Client = Client

    @commands.command (aliases = ['stockprice', 'stocks'])
    @commands.check (CommandEnabled)
    async def stock (self, ctx: commands.Context, _Ticker: str):
        Channel = ctx.channel

        await Embed.Embed (
            f'Stock info of: {_Ticker}',
            f'{_Ticker} current price: ${round (get_live_price (_Ticker), 2)}',
            discord.Color.blue (),
            Channel,
            self.Client
        )

def setup (_Client):
    _Client.add_cog (StockCommand (_Client))
