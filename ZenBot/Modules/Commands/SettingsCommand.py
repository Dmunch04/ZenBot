import discord
from discord.ext import commands

class SettingsCommand (commands.Cog):
    def __init__ (self, Client: commands.Bot):
        self.Client = Client

    @commands.command (aliases = ['set'])
    async def setting (self, ctx: commands.Context, Setting: str, *, Value: str):
        await ctx.send (Setting + ' = ' + Value)

def setup (Client: commands.Bot):
    Client.add_cog (SettingsCommand (Client))