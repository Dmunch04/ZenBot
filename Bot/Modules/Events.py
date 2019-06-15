import discord
from discord.ext import commands

class Events (commands.Cog):
    def __init__ (self, Client):
        self.Client = Client

def setup (_Client):
    _Client.add_cog (Events (_Client))
