import urbandictionary as urban

import discord 
from discord.ext import commands

from Helpers import EmbedHelper as Embed

class UrbanDictionaryCommand (commands.Cog):
    def __init__ (self, Client : discord.Client):
        self.Client = Client

    @commands.command (aliases = ['urban', 'urbandict'])
    async def urbandictionary (self, ctx : commands.Context, *, _Query : str):
        Channel = ctx.channel
        UrbanDefs = urban.define(_Query)
        if UrbanDefs:
            Definition = UrbanDefs[0].definition
        
        await Embed.Embed (
            f'Urban Dictionary Definition for: {_Query}',
            Definition,
            discord.Color.blue (),
            Channel,
            self.Client
        )

        

def setup (_Client):
    _Client.add_cog (UrbanDictionaryCommand (_Client))