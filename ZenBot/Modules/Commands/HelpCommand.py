import discord
from discord.ext import commands

from Core import CommandEnabled

class HelpCommand (commands.Cog):
    def __init__ (self, Client: discord.Client):
        self.Client = Client

    @commands.command ()
    @commands.check (CommandEnabled)
    async def help (self, ctx: commands.Context):
        await ctx.send ('Help (Embed here)')

def setup (Client: discord.Client):
    Client.add_cog (HelpCommand (Client))