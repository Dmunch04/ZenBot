from DavesLogger import Logs

import discord
from discord.ext import commands

class Events (commands.Cog):
    def __init__ (self, Client: discord.Client):
        self.Client = Client

    @commands.Cog.listener ()
    async def on_ready (self):
        Logs.Server ('Bot is running! Awaiting user interaction...')

def setup (Client: discord.Client):
    Client.add_cog (Events (Client))