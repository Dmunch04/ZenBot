import PCPPScraper.pcpartpickerscraper as pcpp

import discord
from discord.ext import commands

from Core import CommandEnabled
from Helpers import EmbedHelper as Embed

class PCPartPickerCommand (commands.Cog):
    def __init__ (self, Client : discord.Client):
        self.Client = Client
    
    @commands.command (aliases = ['pcpps'])
    @commands.check (CommandEnabled)
    async def pcpartpickersearch (self, ctx : commands.Context, *, _Query):
        Channel = ctx.channel
        result = pcpp.searchComponents(1, _Query)[0]
        await Embed.Embed(
            f'PCPartPicker Component Search Top Result for: {_Query}',
            f'[{result.name}]({result.link})\nPrice: {result.price}',
            discord.Color.blue(),
            Channel,
            self.Client
        )
        
def setup (_Client):
    _Client.add_cog (PCPartPickerCommand (_Client))