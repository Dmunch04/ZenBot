from cryptocompare import get_price

import discord
from discord.ext import commands

from Helpers import EmbedHelper as Embed

class CryptoCommand (commands.Cog):
    def __init__ (self, Client : discord.Client):
        self.Client = Client

    @commands.command (aliases = ['cryptocurrency', 'cryptoprice'])
    async def crypto (self, ctx: commands.Context, _Ticker: str):
        Channel = ctx.channel

        Price = get_price (_Ticker, curr = 'USD')[_Ticker]['USD']

        await Embed.Embed (
            self.Client,
            f'Cryptocurrency Info: {_Ticker}',
            f'{_Ticker} current price: ${Price}'
            discord.Color.black (),
            Channel,
            self.Client
        )

def setup (_Client):
    _Client.add_cog (CryptoCommand (_Client))
