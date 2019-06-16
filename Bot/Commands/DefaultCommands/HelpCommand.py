import discord
from discord.ext import commands

class HelpCommand (commands.Cog):
    def __init__ (self, Client):
        self.Client = Client

    @commands.command ()
    async def help (self, ctx):
        await ctx.send ('Help (Embed here)')

def setup (_Client):
    _Client.add_cog (HelpCommand (_Client))
