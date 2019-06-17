from google.google import search

import discord
from discord.ext import commands

class GoogleCommand (commands.Cog):
    def __init__ (self, Client : discord.Client):
        self.Client = Client
    
    @commands.command ()
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

def setup (_Client):
    _Client.add_cog (GoogleCommand (_Client))